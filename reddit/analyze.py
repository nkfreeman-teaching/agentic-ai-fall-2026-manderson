"""Stream user-day counts into auditable daily and account summaries."""

from __future__ import annotations

import argparse
import json
from collections import defaultdict
from datetime import date, timedelta
from pathlib import Path

import numpy as np
import polars as pl
import pyarrow.parquet as pq
import statsmodels.api as sm
from statsmodels.stats.multitest import multipletests


SOURCE = Path("data/user_daily_post_counts.parquet")
OUTPUT = Path("derived")
EVENTS = {
    "Claude Code research preview": date(2025, 2, 24),
    "Codex research preview": date(2025, 5, 16),
}


def summarize_row_groups(sample: bool) -> tuple[dict, pl.DataFrame, dict]:
    parquet = pq.ParquetFile(SOURCE)
    indices = (
        np.linspace(
            start=0,
            stop=parquet.metadata.num_row_groups - 1,
            num=24,
            dtype=int,
        )
        if sample
        else range(parquet.metadata.num_row_groups)
    )
    daily = defaultdict(lambda: np.zeros(5, dtype=np.int64))
    totals_chunks = []
    days_chunks = []
    maxima_chunks = []
    pending = None
    previous_key = None
    duplicate_rows = 0
    sort_order_violations = 0
    nonpositive_rows = 0
    null_rows = 0
    rows = 0
    count_histogram = np.zeros(1001, dtype=np.int64)

    for index in indices:
        frame = pl.from_arrow(parquet.read_row_group(int(index)))
        rows += frame.height
        null_rows += sum(frame.null_count().row(0))
        nonpositive_rows += frame.filter(pl.col("post_count") <= 0).height
        users = frame.get_column("user_id").to_numpy()
        dates = frame.get_column("post_date_utc").cast(pl.Int32).to_numpy()
        counts = frame.get_column("post_count").to_numpy()
        duplicate_rows += int(
            np.count_nonzero((users[1:] == users[:-1]) & (dates[1:] == dates[:-1]))
        )
        sort_order_violations += int(
            np.count_nonzero(
                (users[1:] < users[:-1])
                | ((users[1:] == users[:-1]) & (dates[1:] < dates[:-1]))
            )
        )
        if not sample and previous_key == (int(users[0]), int(dates[0])):
            duplicate_rows += 1
        if not sample and previous_key is not None:
            sort_order_violations += int(previous_key > (int(users[0]), int(dates[0])))
        previous_key = (int(users[-1]), int(dates[-1]))
        count_histogram += np.bincount(
            np.minimum(counts, 1000),
            minlength=1001,
        )

        day_group = frame.group_by("post_date_utc").agg(
            pl.len().alias("active_users"),
            pl.col("post_count").sum().alias("posts"),
            pl.col("post_count")
            .filter(pl.col("post_count") >= 20)
            .sum()
            .alias("posts_from_20_plus_days"),
            (pl.col("post_count") >= 20).sum().alias("users_with_20_plus_posts"),
        )
        for row in day_group.iter_rows(named=True):
            daily[row["post_date_utc"]] += np.array(
                [
                    row["active_users"],
                    row["posts"],
                    row["posts_from_20_plus_days"],
                    row["users_with_20_plus_posts"],
                    1,
                ],
                dtype=np.int64,
            )

        account_group = (
            frame.group_by("user_id")
            .agg(
                pl.len().alias("active_days"),
                pl.col("post_count").sum().alias("total_posts"),
                pl.col("post_count").max().alias("max_daily_posts"),
            )
            .sort("user_id")
        )
        ids = account_group.get_column("user_id").to_numpy()
        active = account_group.get_column("active_days").to_numpy().astype(np.int32)
        posts = account_group.get_column("total_posts").to_numpy().copy()
        maxima = account_group.get_column("max_daily_posts").to_numpy().copy()
        if not sample and pending is not None and pending[0] == ids[0]:
            active[0] += pending[1]
            posts[0] += pending[2]
            maxima[0] = max(maxima[0], pending[3])
            pending = None
        if pending is not None:
            totals_chunks.append(np.array([pending[2]], dtype=np.int64))
            days_chunks.append(np.array([pending[1]], dtype=np.int32))
            maxima_chunks.append(np.array([pending[3]], dtype=np.int64))
        pending = (int(ids[-1]), int(active[-1]), int(posts[-1]), int(maxima[-1]))
        if len(ids) > 1:
            totals_chunks.append(posts[:-1].copy())
            days_chunks.append(active[:-1].copy())
            maxima_chunks.append(maxima[:-1].copy())
        if (int(index) + 1) % 300 == 0:
            print(f"Read {int(index) + 1}/{parquet.metadata.num_row_groups} row groups", flush=True)

    if pending is not None:
        totals_chunks.append(np.array([pending[2]], dtype=np.int64))
        days_chunks.append(np.array([pending[1]], dtype=np.int32))
        maxima_chunks.append(np.array([pending[3]], dtype=np.int64))
    totals = np.concatenate(totals_chunks)
    active_days = np.concatenate(days_chunks)
    maxima = np.concatenate(maxima_chunks)
    top_count = max(1, int(np.ceil(totals.size * 0.001)))
    top_posts = int(np.partition(totals, totals.size - top_count)[-top_count:].sum())
    daily_frame = pl.DataFrame(
        [
            {
                "date": day,
                "active_users": int(values[0]),
                "posts": int(values[1]),
                "posts_from_20_plus_days": int(values[2]),
                "users_with_20_plus_posts": int(values[3]),
            }
            for day, values in daily.items()
        ]
    ).sort("date")
    summary = {
        "source_rows": parquet.metadata.num_rows,
        "analyzed_rows": rows,
        "row_groups": len(indices),
        "schema": str(parquet.schema_arrow),
        "null_cells": null_rows,
        "nonpositive_rows": nonpositive_rows,
        "duplicate_user_date_rows": duplicate_rows,
        "sort_order_violations": sort_order_violations,
        "account_count": int(totals.size),
        "total_posts": int(totals.sum()),
        "first_date": str(daily_frame["date"].min()),
        "last_date": str(daily_frame["date"].max()),
        "observed_dates": daily_frame.height,
        "calendar_days": (
            daily_frame["date"].max() - daily_frame["date"].min()
        ).days + 1,
        "single_day_accounts": int(np.count_nonzero(active_days == 1)),
        "account_total_median": float(np.median(totals)),
        "account_total_p99": float(np.quantile(totals, 0.99)),
        "account_total_p999": float(np.quantile(totals, 0.999)),
        "account_max_daily_posts": int(maxima.max()),
        "top_point_one_percent_accounts": top_count,
        "top_point_one_percent_post_share": top_posts / int(totals.sum()),
        "user_day_count_ge_20": int(count_histogram[20:].sum()),
        "user_day_count_ge_100": int(count_histogram[100:].sum()),
    }
    if not sample:
        assert rows == parquet.metadata.num_rows
        assert int(daily_frame["posts"].sum()) == summary["total_posts"]
        assert sort_order_violations == 0
    return summary, daily_frame, {"counts_0_to_1000": count_histogram.tolist()}


def event_models(daily: pl.DataFrame) -> list[dict]:
    rows = daily.to_dicts()
    lookup = {row["date"]: row for row in rows}
    results = []
    for label, event in EVENTS.items():
        for window in [14, 21, 30, 45, 60]:
            offsets = list(range(-window, 0)) + list(range(1, window + 1))
            dates = [event + timedelta(days=offset) for offset in offsets]
            if any(day not in lookup for day in dates):
                results.append(
                    {
                        "event": label,
                        "date": str(event),
                        "window_days": window,
                        "status": "incomplete window",
                    }
                )
                continue
            specifications = [("posts", "linear")]
            if window == 30:
                specifications.extend(
                    [
                        ("posts_excluding_20_plus_days", "linear"),
                        ("posts", "quadratic"),
                    ]
                )
            for outcome, trend in specifications:
                y_values = []
                x_values = []
                for offset, day in zip(offsets, dates):
                    row = lookup[day]
                    value = row["posts"]
                    if outcome == "posts_excluding_20_plus_days":
                        value -= row["posts_from_20_plus_days"]
                    y_values.append(np.log1p(value))
                    weekday = day.weekday()
                    trend_terms = [1.0, offset, int(offset > 0), max(offset, 0)]
                    if trend == "quadratic":
                        trend_terms.extend([offset**2, max(offset, 0) ** 2])
                    x_values.append(trend_terms + [int(weekday == index) for index in range(1, 7)])
                design = np.array(x_values)
                fit = sm.OLS(np.array(y_values), design).fit(
                    cov_type="HAC",
                    cov_kwds={"maxlags": 7},
                )
                ci = fit.conf_int(alpha=0.05)[2]
                result = {
                    "event": label,
                    "date": str(event),
                    "window_days": window,
                    "outcome": outcome,
                    "trend": trend,
                    "status": "estimated",
                    "level_change_pct": float(np.expm1(fit.params[2]) * 100),
                    "level_change_ci_low_pct": float(np.expm1(ci[0]) * 100),
                    "level_change_ci_high_pct": float(np.expm1(ci[1]) * 100),
                    "level_change_p": float(fit.pvalues[2]),
                    "pre_mean_posts": float(np.mean([lookup[day]["posts"] for day in dates[:window]])),
                    "post_mean_posts": float(np.mean([lookup[day]["posts"] for day in dates[window:]])),
                }
                if window == 30:
                    result["removed_post_share"] = sum(
                        lookup[day]["posts_from_20_plus_days"] for day in dates
                    ) / sum(lookup[day]["posts"] for day in dates)
                    if outcome == "posts" and trend == "linear":
                        trend_design = design.copy()
                        trend_design[:, 4:] = 1 / 7
                        result["offsets"] = offsets
                        result["observed_posts"] = [lookup[day]["posts"] for day in dates]
                        result["fitted_trend_posts"] = np.expm1(
                            fit.predict(trend_design)
                        ).tolist()
                results.append(result)
    primary = [
        result
        for result in results
        if result.get("outcome") == "posts"
        and result.get("window_days") == 30
        and result.get("trend") == "linear"
        and result["status"] == "estimated"
    ]
    if primary:
        adjusted = multipletests(
            pvals=[r["level_change_p"] for r in primary],
            alpha=0.05,
            method="holm",
        )[1]
        for result, pvalue in zip(primary, adjusted):
            result["holm_p"] = float(pvalue)
    return results


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--sample", action="store_true")
    args = parser.parse_args()
    summary, daily, histogram = summarize_row_groups(sample=args.sample)
    summary["events"] = event_models(daily) if not args.sample else []
    print(
        json.dumps(
            obj=summary,
            indent=2,
            default=str,
        ),
        flush=True,
    )
    if not args.sample:
        OUTPUT.mkdir(exist_ok=True)
        daily.write_parquet(OUTPUT / "daily_summary.parquet")
        (OUTPUT / "summary.json").write_text(
            json.dumps(
                obj=summary,
                indent=2,
            )
        )
        (OUTPUT / "count_histogram.json").write_text(json.dumps(histogram))


if __name__ == "__main__":
    main()
