# Agentic AI workshops

This repository pairs a [workshop deck](slides/agentic-ai.html) ([PDF](slides/agentic-ai.pdf)) with two completed agentic AI examples and two student starters. The examples show how an agent can analyze data, build deliverables, seek independent criticism, verify findings, and revise its work. The starters let students run those processes themselves. Their results and review scores need not match the completed examples.

## Examples and starters

| Exercise | Completed example | Student starter |
|---|---|---|
| Customer segmentation | [Analysis and instructions](customer-segmentation/README.md), [DOCX report](customer-segmentation/output/full/customer_segmentation_report.docx), [interactive explorer](customer-segmentation/output/full/segment_explorer.html), and [review overview](customer-segmentation/output/full/process_overview.html) | [Source data, transcript, and setup guide](customer-segmentation-base/SETUP.md) |
| Reddit posting | [Analysis and instructions](reddit/README.md), [working paper](reddit/paper/main.pdf), and [analysis and review report](reddit/report.html) | [Transcript, data placeholder, and setup guide](reddit-base/SETUP.md) |

The completed folders contain code, generated results, and review records. Each starter contains its original transcript and a `SETUP.md` with writing and review guidance. The customer starter includes its source data. The Reddit starter contains an empty `data/` placeholder because its source file is not tracked here.

To begin an exercise, copy its starter folder to a working location. Ask Codex to read `SETUP.md` and `transcript.txt`, clarify consequential choices, and plan the work before running the analysis. Students create their own environment, analysis code, deliverables, and review record in that copy. The setup guides contain the writing and review instructions needed for the exercises.

## Environments

The completed examples are separate [Pixi](https://pixi.sh) projects. Run `pixi install` inside `customer-segmentation/` or `reddit/`, then follow that folder's README. There is no Pixi project at the repository root. Both existing Pixi manifests specify `linux-64`; they do not promise an identical install on macOS or Windows. The starters intentionally have no Pixi manifests because creating an environment is part of each transcript's assignment.

## Data

The customer segmentation example uses eight Parquet files from the simulated [Complete Journey dataset](https://github.com/cunningjames/completejourney_py). They are included unchanged in both `customer-segmentation/data/` and `customer-segmentation-base/data/`.

The Reddit example uses a proprietary Parquet file that is excluded from this repository. Obtain [`user_daily_post_counts.parquet`](https://drive.google.com/file/d/1SzuIzRBhRdKuvNmBKqvhI-WFv4lRfXBr/view?usp=sharing) (approximately 756 MB) and place it in `reddit/data/` for the completed example or `reddit-base/data/` for the starter. Access to the file may depend on the link's sharing permissions. Do not commit the source file.
