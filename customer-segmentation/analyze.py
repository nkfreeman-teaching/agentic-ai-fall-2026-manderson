"""Build household shopping segments from the local Complete Journey parquet files."""

from __future__ import annotations

import argparse
import itertools
import json
from pathlib import Path

import numpy as np
import polars as pl
from sklearn.cluster import KMeans
from sklearn.metrics import adjusted_rand_score, silhouette_score


DATA = Path(__file__).parent / "data"
OUTPUT = Path(__file__).parent / "output"
BASE_DEPARTMENTS = ["GROCERY", "DRUG GM", "PRODUCE", "MEAT", "MEAT-PCKGD"]


def source_checks(transactions: pl.LazyFrame, products: pl.LazyFrame) -> dict:
    summary = transactions.select(
        pl.len().alias("purchase_lines"),
        pl.col("household_id").n_unique().alias("households"),
        pl.col("basket_id").n_unique().alias("baskets"),
        pl.col("transaction_timestamp").min().alias("first_purchase"),
        pl.col("transaction_timestamp").max().alias("last_purchase"),
        pl.col("sales_value").sum().alias("retailer_receipts"),
        (pl.col("sales_value") == 0).sum().alias("zero_sales_lines"),
        (pl.col("quantity") == 0).sum().alias("zero_quantity_lines"),
    ).collect().to_dicts()[0]
    summary["first_purchase"] = summary["first_purchase"].isoformat()
    summary["last_purchase"] = summary["last_purchase"].isoformat()
    summary["unmatched_product_lines"] = transactions.join(
        products.select("product_id"),
        on="product_id",
        how="anti",
    ).select(pl.len()).collect().item()
    summary["fuel_receipts"] = transactions.join(
        products.select("product_id", "department"),
        on="product_id",
        how="left",
    ).filter(pl.col("department") == "FUEL").select(pl.col("sales_value").sum()).collect().item()
    return summary


def household_features(transactions: pl.LazyFrame, products: pl.LazyFrame) -> pl.DataFrame:
    lines = (
        transactions
        .join(
            products.select("product_id", "department", "brand"),
            on="product_id",
            how="left",
        )
        .with_columns(
            pl.when(pl.col("department").is_in(pl.lit(BASE_DEPARTMENTS)))
            .then(pl.col("department"))
            .otherwise(pl.lit("OTHER"))
            .alias("department_group"),
        )
    )
    fuel = lines.group_by("household_id").agg(
        pl.when(pl.col("department") == "FUEL")
        .then(pl.col("sales_value"))
        .otherwise(0)
        .sum()
        .alias("fuel_receipts"),
    )
    core = lines.filter((pl.col("department") != "FUEL").fill_null(True))
    basket = (
        core
        .group_by("household_id", "basket_id")
        .agg(
            pl.col("sales_value").sum().alias("basket_receipts"),
        )
        .group_by("household_id")
        .agg(
            pl.len().alias("basket_count"),
            pl.col("basket_receipts").mean().alias("mean_basket_receipts"),
        )
    )
    aggregates = core.group_by("household_id").agg(
        pl.col("sales_value").sum().alias("receipts"),
        pl.col("retail_disc").sum().alias("retail_discount"),
        pl.when(pl.col("brand") == "Private")
        .then(pl.col("sales_value"))
        .otherwise(0)
        .sum()
        .alias("private_receipts"),
        pl.col("transaction_timestamp").max().alias("last_purchase"),
        pl.col("week").n_unique().alias("active_weeks"),
        *[
            pl.when(pl.col("department_group") == department)
            .then(pl.col("sales_value"))
            .otherwise(0)
            .sum()
            .alias(f"dept_{department.lower().replace('-', '_').replace(' ', '_')}")
            for department in BASE_DEPARTMENTS + ["OTHER"]
        ],
    )
    end = transactions.select(pl.col("transaction_timestamp").max()).collect().item()
    features = (
        aggregates
        .join(basket, on="household_id", how="inner")
        .join(fuel, on="household_id", how="left")
        .with_columns(
            (pl.col("basket_count") / 53).alias("baskets_per_week"),
            ((pl.lit(end) - pl.col("last_purchase")).dt.total_days()).alias("recency_days"),
            (pl.col("retail_discount") / (pl.col("receipts") + pl.col("retail_discount")))
            .fill_nan(0)
            .fill_null(0)
            .alias("retail_discount_share"),
            (pl.col("private_receipts") / pl.col("receipts"))
            .fill_nan(0)
            .fill_null(0)
            .alias("private_label_share"),
            (pl.col("fuel_receipts") / (pl.col("receipts") + pl.col("fuel_receipts")))
            .fill_nan(0)
            .fill_null(0)
            .alias("fuel_share_total"),
        )
        .with_columns(
            *[
                (pl.col(f"dept_{department.lower().replace('-', '_').replace(' ', '_')}") / pl.col("receipts"))
                .fill_nan(0)
                .fill_null(0)
                .alias(f"share_{department.lower().replace('-', '_').replace(' ', '_')}")
                for department in BASE_DEPARTMENTS + ["OTHER"]
            ],
        )
        .with_columns(
            (pl.col("share_meat") + pl.col("share_meat_pckgd")).alias("share_meat_combined"),
        )
        .collect()
        .sort("household_id")
    )
    return features


def model_matrix(features: pl.DataFrame, include_fuel: bool = False) -> tuple[np.ndarray, list[str]]:
    activity = ["baskets_per_week", "mean_basket_receipts", "recency_days"]
    value = ["retail_discount_share", "private_label_share"]
    mix = [f"share_{department.lower().replace('-', '_').replace(' ', '_')}" for department in BASE_DEPARTMENTS]
    if include_fuel:
        mix.append("fuel_share_total")
    groups = [activity, value, mix]
    columns = activity + value + mix
    values = features.select(columns).to_numpy().astype(float)
    values[:, :3] = np.log1p(np.maximum(values[:, :3], 0))
    # Robust clipping and scaling keep extreme households from defining all distances.
    lower = np.quantile(values, 0.01, axis=0)
    upper = np.quantile(values, 0.99, axis=0)
    values = np.clip(values, lower, upper)
    median = np.median(values, axis=0)
    scale = np.quantile(values, 0.75, axis=0) - np.quantile(values, 0.25, axis=0)
    scale[scale == 0] = 1
    values = (values - median) / scale
    start = 0
    for group in groups:
        stop = start + len(group)
        values[:, start:stop] /= np.sqrt(len(group))
        start = stop
    if not np.isfinite(values).all():
        raise ValueError("The model matrix contains non-finite values")
    return values, columns


def choose_clusters(values: np.ndarray) -> tuple[np.ndarray, list[dict], int]:
    candidates = []
    baseline_labels = {}
    for k in range(2, min(8, len(values) - 1) + 1):
        model = KMeans(n_clusters=k, random_state=42, n_init=20)
        labels = model.fit_predict(values)
        sizes = np.bincount(labels)
        silhouette = silhouette_score(values, labels)
        stability = []
        for seed in range(5):
            rng = np.random.default_rng(seed + 100)
            subset = rng.choice(len(values), size=int(0.8 * len(values)), replace=False)
            replica = KMeans(n_clusters=k, random_state=seed + 100, n_init=10)
            replica.fit(values[subset])
            stability.append(adjusted_rand_score(labels, replica.predict(values)))
        candidates.append({
            "k": k,
            "silhouette": round(float(silhouette), 4),
            "stability_ari": round(float(np.mean(stability)), 4),
            "smallest_segment": int(sizes.min()),
            "smallest_share": round(float(sizes.min() / len(values)), 4),
        })
        baseline_labels[k] = labels
    eligible = [row for row in candidates if row["smallest_share"] >= 0.05 and row["stability_ari"] >= 0.8]
    pool = eligible or [row for row in candidates if row["smallest_share"] >= 0.05] or candidates
    selected = max(pool, key=lambda row: (row["silhouette"], -row["k"]))["k"]
    return baseline_labels[selected], candidates, selected


def summarize(features: pl.DataFrame, labels: np.ndarray, source: dict, candidates: list[dict], selected: int) -> tuple[dict, pl.DataFrame]:
    tagged = features.with_columns(pl.Series("segment", labels + 1))
    demographics = pl.read_parquet(DATA / "demographics.parquet")
    redemptions = pl.read_parquet(DATA / "coupon_redemptions.parquet")
    redemption_counts = redemptions.group_by("household_id").agg(pl.len().alias("redemptions"))
    tagged = (
        tagged
        .join(demographics.select("household_id", "age", "income", "household_comp"), on="household_id", how="left")
        .join(redemption_counts, on="household_id", how="left")
        .with_columns(pl.col("redemptions").fill_null(0))
    )
    shares = [f"share_{department.lower().replace('-', '_').replace(' ', '_')}" for department in BASE_DEPARTMENTS]
    metrics = ["basket_count", "baskets_per_week", "mean_basket_receipts", "receipts", "recency_days", "retail_discount_share", "private_label_share", "fuel_share_total", "active_weeks", "share_meat_combined"] + shares
    overview = tagged.group_by("segment").agg(
        pl.len().alias("households"),
        pl.col("age").is_not_null().sum().alias("with_demographics"),
        (pl.col("redemptions") > 0).sum().alias("redeeming_households"),
        *[pl.col(metric).median().alias(metric) for metric in metrics],
    ).sort("segment")
    records = overview.to_dicts()
    total = len(tagged)
    for row in records:
        row["share"] = row["households"] / total
        row["redeeming_share"] = row["redeeming_households"] / row["households"]
    source["demographic_file_rows"] = demographics.height
    source["demographic_households"] = int(tagged["age"].is_not_null().sum())
    source["coupon_redemptions"] = redemptions.height
    source["households_under_four_baskets"] = int((features["basket_count"] < 4).sum())
    source["median_baskets"] = float(features["basket_count"].median())
    source["median_receipts"] = float(features["receipts"].median())
    source["profile_quantiles"] = features.select(
        pl.col("basket_count").quantile(0.1).alias("baskets_p10"),
        pl.col("basket_count").quantile(0.9).alias("baskets_p90"),
        pl.col("receipts").quantile(0.1).alias("receipts_p10"),
        pl.col("receipts").quantile(0.9).alias("receipts_p90"),
        pl.col("recency_days").quantile(0.9).alias("recency_p90"),
    ).to_dicts()[0]
    source["grocery_receipts"] = float(features["receipts"].sum())
    source["model_households"] = total
    source["fuel_only_households"] = source["households"] - total
    source["demographic_coverage"] = source["demographic_households"] / total
    campaigns = pl.read_parquet(DATA / "campaigns.parquet")
    descriptions = pl.read_parquet(DATA / "campaign_descriptions.parquet")
    source["redemptions_without_campaign_assignment"] = redemptions.join(
        campaigns,
        on=["campaign_id", "household_id"],
        how="anti",
    ).height
    dated_redemptions = redemptions.join(descriptions, on="campaign_id", how="left")
    source["redemptions_outside_campaign_dates"] = dated_redemptions.filter(
        (pl.col("redemption_date") < pl.col("start_date"))
        | (pl.col("redemption_date") > pl.col("end_date")),
    ).height
    context = (
        campaigns
        .join(descriptions, on="campaign_id", how="inner")
        .group_by("campaign_type")
        .agg(
            pl.len().alias("household_campaign_assignments"),
            pl.col("household_id").n_unique().alias("assigned_households"),
            pl.col("campaign_id").n_unique().alias("campaigns"),
        )
        .sort("campaign_type")
    )
    redeemed = (
        redemptions
        .join(descriptions.select("campaign_id", "campaign_type"), on="campaign_id")
        .group_by("campaign_type")
        .agg(
            pl.len().alias("redemption_events"),
            pl.col("household_id").n_unique().alias("redeeming_households"),
        )
    )
    campaign_context = context.join(redeemed, on="campaign_type", how="left").to_dicts()
    tagged_ids = tagged.select("household_id", "segment").lazy()
    category_lines = (
        pl.scan_parquet(DATA / "transactions.parquet")
        .join(tagged_ids, on="household_id", how="inner")
        .join(
            pl.scan_parquet(DATA / "products.parquet").select("product_id", "department", "product_category", "brand"),
            on="product_id",
            how="left",
        )
    )
    offer_evidence = {}
    for key, condition in {
        "oral_hygiene": pl.col("product_category") == "ORAL HYGIENE PRODUCTS",
        "private_meat": pl.col("department").is_in(pl.lit(["MEAT", "MEAT-PCKGD"])) & (pl.col("brand") == "Private"),
    }.items():
        purchase = (
            category_lines
            .filter(condition)
            .group_by("segment", "household_id")
            .agg(
                pl.col("basket_id").n_unique().alias("purchase_baskets"),
                pl.col("sales_value").sum().alias("receipts"),
            )
            .group_by("segment")
            .agg(
                pl.len().alias("buying_households"),
                pl.col("purchase_baskets").median().alias("median_baskets_among_buyers"),
                pl.col("receipts").sum().alias("receipts"),
            )
            .sort("segment")
            .collect()
        )
        offer_evidence[key] = purchase.to_dicts()
    return {
        "source": source,
        "model": {"selected_k": selected, "candidates": candidates},
        "segments": records,
        "campaign_context": campaign_context,
        "offer_evidence": offer_evidence,
        "overall": {
            metric: float(features[metric].median())
            for metric in metrics
        },
    }, tagged


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--sample", action="store_true", help="Run an end-to-end household sample")
    args = parser.parse_args()
    transactions = pl.scan_parquet(DATA / "transactions.parquet")
    products = pl.scan_parquet(DATA / "products.parquet")
    if args.sample:
        ids = transactions.select("household_id").unique().collect()["household_id"].sample(n=75, seed=42)
        transactions = transactions.filter(pl.col("household_id").is_in(pl.lit(ids.to_list())))
    source = source_checks(transactions, products)
    features = household_features(transactions, products)
    values, columns = model_matrix(features)
    labels, candidates, selected = choose_clusters(values)
    result, tagged = summarize(features, labels, source, candidates, selected)
    result["model"]["features"] = columns
    if not args.sample:
        with_fuel_values, _ = model_matrix(features, include_fuel=True)
        with_fuel_labels, _, with_fuel_k = choose_clusters(with_fuel_values)
        result["model"]["fuel_inclusion_sensitivity"] = {
            "selected_k": with_fuel_k,
            "agreement_ari": round(float(adjusted_rand_score(labels, with_fuel_labels)), 4),
        }
        if selected == with_fuel_k:
            changed = min(
                int(np.count_nonzero(labels != np.array(permutation)[with_fuel_labels]))
                for permutation in itertools.permutations(range(selected))
            )
            result["model"]["fuel_inclusion_sensitivity"]["changed_households"] = changed
        retained = features.filter(pl.col("basket_count") >= 4)
        retained_values, _ = model_matrix(retained)
        retained_labels = KMeans(n_clusters=selected, random_state=42, n_init=20).fit_predict(retained_values)
        result["model"]["sparse_history_sensitivity"] = {
            "retained_households": len(retained),
            "agreement_ari": round(
                float(adjusted_rand_score(labels[features["basket_count"].to_numpy() >= 4], retained_labels)),
                4,
            ),
        }
    folder = OUTPUT / ("sample" if args.sample else "full")
    folder.mkdir(parents=True, exist_ok=True)
    (folder / "results.json").write_text(json.dumps(result, indent=2), encoding="utf-8")
    tagged.select("household_id", "segment").write_parquet(folder / "household_segments.parquet")
    print(json.dumps({"source": source, "model": result["model"], "segments": result["segments"]}, indent=2))


if __name__ == "__main__":
    main()
