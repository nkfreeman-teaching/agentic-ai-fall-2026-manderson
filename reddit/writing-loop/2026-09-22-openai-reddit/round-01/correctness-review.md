# Correctness and evidence review

Reviewer: `/root/round1_correctness`. Requested model: `gpt-6-sol`, high reasoning. Reviewed the frozen PDF, matching source and summaries. Overall score: **4/5**.

| Dimension | Score |
|---|---:|
| Logical flow | 4 |
| Visual clarity and print quality | 4 |
| Correctness | 4 |
| Direct communication | 4 |
| First-use abbreviations | 5 |
| Nick Voice | 4 |

1. **Minor, page 2, `paper/main.tex` line 35.** "Complete days" could imply complete capture despite unknown coverage. Say "30 observed calendar days on each side" and verify against the date-presence check in `analyze.py`.
2. **Minor, page 4, line 51.** Figure 2 says "active users" and the prose refers to posting frequency, though the file counts identifiers and the exhibit does not show posts per identifier. Relabel or calculate the rate; verify the rendered chart.
3. **Minor, page 3, line 44.** Figure 1 compresses nearly all pre-2024 values near zero and leaves substantial page whitespace. A recent-period inset or tighter layout would improve readability. All figures remained legible in color and grayscale.
4. **Minor, page 6, line 103.** Reference 1 omits Scientific Reports article number 10413. Add it and verify against the publisher record.

The reviewer reconstructed the two 30-day ordinary least squares point estimates from the 60 observations in `derived/summary.json`: 0.157052% and -0.619531%, matching Table 1. Stored raw and Holm-adjusted values also match. Study descriptions and release dates agree with the publisher, ACL, Anthropic, and OpenAI sources. Window sensitivity and coverage limits are stated plainly.

Could not check: The raw Parquet file was absent from the frozen packet, so the reviewer did not independently validate source rows, identifier mapping, daily aggregates, or coverage. The full pipeline and robust confidence intervals were not independently recomputed.
