# Statistical skeptical review

Requested model: gpt-6-sol, high reasoning. Read-only review of the frozen five-page PDF, source code, and daily summary. The reviewer checked raw Parquet metadata but did not rerun the full 283 million-row aggregation.

1. **Major: The Codex inference depends on window and trend.** The exact linear model with 14, 21, 30, 45, and 60 days on each side gives Codex changes of -1.37%, -1.20%, -0.62%, +0.88%, and +2.48%, respectively. Their 95% intervals are [-2.27%, -0.47%], [-2.22%, -0.17%], [-1.64%, 0.41%], [-0.83%, 2.63%], and [0.25%, 4.76%]. A 30-day separate quadratic trend gives -1.59% [-2.97%, -0.18%]. These exploratory variants show model dependence. Report them, explain the planned 30-day primary window, and restrict the conclusion to its specification. Regenerate all outputs from revised analysis.
2. **Moderate: Broader Codex windows span a changing background trend.** Seven-day means fell from 706,767 posts and 409,491 active identifiers in the week beginning March 17 to 664,028 posts and 388,176 active identifiers in the week beginning April 7. The longer fits span that decline and later flattening. Collection logs were unavailable, so the reviewer could not determine whether activity or coverage changed. State this beside the event result.
3. **Minor: Figure 1 connects missing months.** The first plotted monthly series joined observed months across 18 absent months through August 2026, including all of 2007. Insert gaps and inspect the regenerated figure.

The original PDF table values agreed with the derived JSON. Both figures were readable at the rendered page size. Raw Parquet metadata confirmed 283,488,780 rows, 2,308 row groups, and the reported schema.
