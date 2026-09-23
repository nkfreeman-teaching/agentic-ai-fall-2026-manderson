# Reddit student setup

This folder starts the research exercise. Read `transcript.txt` for the assignment. The `data/` folder contains only a placeholder. Download [`user_daily_post_counts.parquet`](https://drive.google.com/file/d/1SzuIzRBhRdKuvNmBKqvhI-WFv4lRfXBr/view?usp=sharing) (approximately 756 MB) and place it in `data/`. Access may depend on the link's sharing permissions. Keep that source file unchanged and out of Git.

Ask Codex to read this file and the transcript before it plans or runs the work. The transcript is the assignment, not a specification of the answer. Resolve consequential choices with the student, then create the Pixi environment, analysis, working paper, and process report in this folder. A different defensible analysis or review trajectory is acceptable.

## Analysis and writing

- Prototype the analysis on a small sample before scanning the full file. Check row counts, date coverage, nulls, identifier behavior, and representative rows. Record counts before and after filters and joins. Preserve the source Parquet file and write derived results elsewhere.
- Export reported numbers from analysis code into the LaTeX paper so rerunning the analysis updates the paper. Trace each important number, table, and figure back to its input and method. Verify external dates, citations, and claims against sources.
- Write directly for research readers. State the question, method, evidence, and limits in plain terms. Define an abbreviation at first use, explain necessary technical terms, and remove decorative or mannered prose. Label figure axes and units, explain how to read each exhibit, and state the supported takeaway in the paper.
- Treat observed posting counts as counts. An identifier does not establish that an account is a bot. A tool announcement does not measure adoption or prove that a tool changed posting. Explain what the data can and cannot establish.

## Independent review loop

1. Before review, agree on the paper's audience, claims, review dimensions, success rule, and a maximum of five scored rounds. Save an identifiable draft for each round so every score belongs to the exact paper the reviewers saw.
2. After the first complete analysis and paper, ask two independent skeptical reviewers to challenge the methods and interpretation from different perspectives. Have each give specific findings and proposed fixes. Verify each finding against the data, code, sources, and rendered paper before revising.
3. For each scored round, give the same frozen paper to three independent reviewers. Cover argument and audience, correctness and evidence, and communication and presentation. Each reviewer gives a 1–5 overall score, relevant dimension scores, exact findings, and suggested fixes. Use the mean of the three overall scores to track rounds. Review direct writing, defined abbreviations, logical flow, visual quality, and claim support. Mark any check that a reviewer could not perform.
4. Inspect every figure and every paper page as rendered, including actual grayscale previews for figures. Resolve supported findings, regenerate affected outputs, and inspect them again. Do not assign an old score to a changed draft.
5. Stop when all three overall scores are at least 4 and no major issue remains, after two consecutive rounds without a higher mean, or after five rounds. Report the scores, substantive changes, checks actually performed, unresolved limits, and observed agent timing in the final process report. If independent reviewers are unavailable, say so rather than presenting one agent's review as independent.

This guide supplies the writing and review instructions for this exercise. Model names in the dictated transcript are examples; choose agents by available capability. No personal style file or installed skill is required.
