# Progress

The initial full analysis and five-page working paper were completed on 2026-09-22. The 1% prototype scanned 2,830,860 account-day rows. The full scan covered 283,488,780 rows and 2,308 Parquet row groups. It found zero null cells, nonpositive counts, duplicate user-date rows, and sort-order violations. The last three dates were excluded from trend figures because observed counts fell sharply at the source-file boundary.

The two primary release-window estimates and uncertainty intervals are in `../../derived/summary.json`. The raw source is unchanged. Crossref verified the two research-paper DOIs and bibliographic identities using the supplied contact email. The source claims were checked against the publisher/PMC and ACL Anthology pages.

| Round | Reviewed snapshot | Overall scores | Mean | Open major findings | Decision |
|---|---|---|---|---|---|
| Initial skeptical review | `skeptical-base/` | Not scored | N/A | Coverage unknown | Verified and revised |
| 1 | `round-01/` | 3, 4, 4 | 3.67 | Page layout | Revised for round 2 |
| 2 | `round-02/` | 4, 4, 4 | 4.00 | None | Stopped at success threshold; minor fixes applied |

The skeptical reviews found that Codex's estimate changes sign across windows, the product announcements do not measure adoption, and the source lacks coverage records. We verified and added window and quadratic sensitivity, qualified the release dates and observed corpus, and added a model-window figure. The 30-day point estimates were independently re-derived with NumPy least squares. The coverage issue remains a stated limit rather than an implied behavioral finding. Early unobserved months became gaps in the long-history exploratory chart.

For round 1, the parent accepted the layout, identifier-label, caption, ambiguous "planned" and "complete" wording, and missing article-number findings. The long-history figure was removed from the paper because it compressed early years and forced a mostly empty page; it remains an exploratory generated artifact. The revised five-page render places the recent series, primary table, sensitivity table, and event-window figure with their interpretations. The latest compile has zero Overfull/Underfull lines and zero undefined-reference lines. Round 2 will score that revised frozen PDF.

The second round identified minor research-question scope, caption, threshold, punctuation, and layout issues. The working paper was corrected after the round-two snapshot was scored. It now names the local announcement question, identifies the plotted series as trailing means, correctly describes the high-count day exclusion, hides hyperlink borders, and keeps the closing section together. The final PDF was recompiled and inspected in color and grayscale.

Review agent timing uses dispatch-to-receipt wall time where both timestamps were captured; unavailable exact completion times are marked as such in the HTML report. No token or cost estimates are inferred.
