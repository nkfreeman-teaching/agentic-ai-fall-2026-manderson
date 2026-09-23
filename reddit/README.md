# Reddit posting analysis

This working-paper example analyzes the supplied `data/user_daily_post_counts.parquet` file. The source file is private and is excluded by this directory's `.gitignore`. The analysis treats its three fields as observed counts. Collection coverage, the meaning of a counted "post," and the mapping from identifier to account are not independently verified.

Install the pinned environment with `pixi install`. Run the 1% row-group prototype with `MPLBACKEND=Agg pixi run python analyze.py --sample`. Run the full aggregation and event models with `MPLBACKEND=Agg pixi run python analyze.py`. Generate LaTeX variables and figures with `MPLBACKEND=Agg pixi run python generate_outputs.py`, then compile from `paper/` with `latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex`. The full scan uses Parquet row groups so it does not load the 283 million-row input at once.

`derived/summary.json` and `derived/daily_summary.parquet` contain aggregate results. The paper's numeric values and exhibits are generated from these outputs. `MPLBACKEND=Agg pixi run python -m pytest -q` checks the row-group boundary logic. The paper is in `paper/main.pdf`. The project review and effort report are in `writing-loop/` and `report.html`.
