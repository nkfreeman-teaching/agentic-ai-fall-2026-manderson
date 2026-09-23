# Customer segmentation student setup

This folder starts the customer segmentation exercise. Read `transcript.txt` for the assignment. The eight Parquet files in `data/` are the source data. Keep them unchanged. Ask Codex to read this file and the transcript before it plans or runs the work, and resolve consequential choices with the student. Create the Pixi environment, analysis, report, explorer, and process overview in this folder. A different defensible segmentation or review trajectory is acceptable.

## Analysis and writing

- Prototype on a small sample before a full run. Inspect file schemas and representative rows, then check household counts, join keys, missing values, and counts before and after filters and joins. Write derived results outside `data/`.
- Explain the features used to group households, the reason for the chosen number of groups, and sensitivity to reasonable alternatives. Distinguish observed shopping patterns from explanations the data cannot test. The Complete Journey release is simulated, and coupon ideas are hypotheses for a randomized test, not measured commercial effects.
- Write the DOCX report for a decision maker who has not examined the data. State methods, results, and limits directly. Define abbreviations at first use and explain necessary terms. Use figures where they clarify a finding, with readable labels, units, and nearby interpretation. Keep the HTML explorer understandable without reading the report.

## Independent review loop

1. Agree on the audience, deliverables, scoring dimensions, and stopping rule before review. Save an identifiable version of both the report and explorer for every scored pass so scores refer to the exact versions reviewed.
2. After the first complete versions, ask two independent skeptical reviewers to challenge the analysis from different perspectives, such as methods and marketing. Require specific findings and proposed fixes. Verify each finding before changing the analysis or deliverables.
3. For each scored pass, give the same frozen report and explorer to three independent reviewers. Score each deliverable from 1 to 5 on accuracy, clarity, decision value, visual quality, and usability and completeness. Require exact findings and suggested fixes. Compute each deliverable's pass score as the mean of its 15 dimension scores, three reviewers times five dimensions. Mark checks that could not be performed.
4. Open the DOCX or a faithful PDF rendering and the HTML explorer. Inspect figures at their intended size and test the explorer's controls. Inspect figures in actual grayscale when color carries information. Verify supported findings, revise, regenerate affected outputs, and inspect them again. Do not carry a prior score onto a changed version.
5. Plan for three scored passes. Continue beyond three only if at least one deliverable gains 0.25 points or more in its latest pass and useful issues remain. Stop when both deliverables plateau without a material open issue or after five passes. Report scores, changes, checks actually performed, and observed agent timing in the final process overview. If independent reviewers are unavailable, say so rather than presenting one agent's review as independent.

This guide supplies the writing and review instructions for this exercise. Model names in the dictated transcript are examples; choose agents by available capability. No personal style file or installed skill is required.
