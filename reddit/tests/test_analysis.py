"""Checks for the row-group boundary logic on a small known dataset."""

from datetime import date

import polars as pl

import analyze


def test_row_group_boundary_merges_one_account(tmp_path, monkeypatch):
    source = tmp_path / "counts.parquet"
    rows = pl.DataFrame(
        {
            "user_id": [1, 1, 1, 2, 2],
            "post_date_utc": [
                date(2025, 1, 1),
                date(2025, 1, 2),
                date(2025, 1, 3),
                date(2025, 1, 1),
                date(2025, 1, 2),
            ],
            "post_count": [1, 2, 20, 3, 4],
        }
    )
    rows.write_parquet(source, row_group_size=2)
    monkeypatch.setattr(analyze, "SOURCE", source)
    summary, daily, _ = analyze.summarize_row_groups(sample=False)
    assert summary["account_count"] == 2
    assert summary["total_posts"] == 30
    assert summary["duplicate_user_date_rows"] == 0
    assert summary["sort_order_violations"] == 0
    assert daily["posts"].sum() == 30
    assert daily["posts_from_20_plus_days"].sum() == 20
