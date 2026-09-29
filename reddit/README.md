# Reddit posting analysis

Students do not need to run this example. The finished paper is `paper/main.pdf`, and `report.html` opens in a web browser to show how the agent and its reviewers built it.

This working-paper example analyzes the supplied `data/user_daily_post_counts.parquet` file. The source file is proprietary and is not included in this repository, and this directory's `.gitignore` excludes a local copy. The analysis treats its three fields as observed counts. Collection coverage, the meaning of a counted "post," and the mapping from identifier to account are not independently verified.

Install the pinned environment with `pixi install`. Run the 1% row-group prototype with `MPLBACKEND=Agg pixi run python analyze.py --sample`. Run the full aggregation and event models with `MPLBACKEND=Agg pixi run python analyze.py`. Generate LaTeX variables and figures with `MPLBACKEND=Agg pixi run python generate_outputs.py`, then compile from `paper/` with `latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex`, which needs a LaTeX installation such as MacTeX or MiKTeX. Without one, `pixi exec --spec tectonic -- tectonic main.tex` compiles the same file. On Windows, PowerShell does not accept the `MPLBACKEND=Agg` prefix, so run `$env:MPLBACKEND = "Agg"` once and then each `pixi run` command without the prefix. The full scan uses Parquet row groups so it does not load the 283 million-row input at once.

`derived/summary.json` and `derived/daily_summary.parquet` contain aggregate results. The paper's numeric values and exhibits are generated from these outputs. `MPLBACKEND=Agg pixi run python -m pytest -q` checks the row-group boundary logic. The paper is in `paper/main.pdf`. The project review and effort report are in `writing-loop/` and `report.html`.
