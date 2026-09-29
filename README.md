# Agentic AI workshops

**Setting up your own computer?** Start with the step-by-step guide for [Mac](getting-started/mac.md) ([PDF](getting-started/mac.pdf)) or [Windows](getting-started/windows.md) ([PDF](getting-started/windows.pdf)). It covers everything from downloading these files to running both exercises, and it assumes no programming experience.

This repository pairs a [workshop deck](slides/agentic-ai.html) ([PDF](slides/agentic-ai.pdf)) with two completed agentic AI examples and two student starters. The examples show how an agent can analyze data, build deliverables, seek independent criticism, verify findings, and revise its work. The starters let students run those processes themselves. Their results and review scores need not match the completed examples.

## Getting started

The getting-started guides for [Mac](getting-started/mac.md) ([PDF](getting-started/mac.pdf)) and [Windows](getting-started/windows.md) ([PDF](getting-started/windows.pdf)) list what a computer and ChatGPT account need before setup, then cover downloading these materials, opening a terminal, installing Codex, Pixi, and Git, and running both exercises with staged prompts. The Reddit exercise also needs a data file and LaTeX, and the guides cover both.

## Workshop recording and transcript

The [recording](https://alabama.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=8d3f444c-8b6a-490b-9738-b4d00129a3a7) of the September 25, 2026 workshop is on Panopto. An [edited transcript](sessions/2026-09-25-transcript.md) with section timestamps accompanies it, and it lists each place where the edited text corrects a fact misstated in the recording. The session covered the following points:

- **Terms.** Artificial intelligence (AI) is a field dating from the 1950s. Machine learning is the part of AI that learns patterns from data, deep learning is the part of machine learning that uses many-layered neural networks, and large language models (LLMs) are one kind of deep learning model. An LLM is one form of AI, not a synonym for it.
- **Chat assistants and agents.** A chat assistant answers questions, and the user carries out the work. An agent uses the same kind of model but acts on the user's behalf by reading files, running code, and checking results.
- **Model and harness.** The model is like a computer's processor, and the harness (e.g., Codex or Claude Code) is like its operating system. The harness supplies tools, a system prompt with the provider's guardrails, memory files, and skills. Any program on the computer that can be run from a terminal becomes a tool the agent can use.
- **Context.** Everything the model sees on a turn, including the system prompt and every tool result, counts against a limited context window measured in tokens. When the window fills, the harness summarizes older material, and details can be lost without notice. Long or cluttered context can reduce accuracy before the window is full.
- **From prompts to loops and goals.** Practice has moved from crafting prompts, to curating context, to designing loops in which an agent works, checks, and revises until a checkable goal is met. Speaking a long, unedited description of the vision, concerns, and uncertainties (Andrej Karpathy's "ramble") is a fast way to give an agent that context.
- **Longer tasks.** METR's measurements show that the length of human task an agent can complete on its own has grown quickly. Claude Opus 4.6 succeeds half the time on software tasks that take a human expert about 12 hours.
- **Independent review.** An agent that grades its own work is biased. A second agent, ideally from a different provider, can be told to find what is wrong and propose fixes. The main agent verifies each finding before acting on it and escalates disagreements to the person.
- **Ownership.** Anything an agent produces on a person's behalf is that person's work. Ask the agent to explain any result, method, or figure that is unclear, for example by having it rebuild a step in a notebook and walk through it.
- **Sensitive data.** An agent can build and test an analysis on synthetic data that matches the real data's columns and types. The person then runs the finished analysis on the real data without the model seeing it.

## Student offer

OpenAI's [2026 Back to School offer](https://help.openai.com/en/articles/20001493-chatgpt-back-to-school-offer-for-students) provides eligible students at U.S. colleges and universities with four free monthly billing periods of ChatGPT Plus. Students must verify enrollment, provide a valid payment method, and claim the offer by October 31, 2026. The subscription renews at $20 per month after the promotional period unless canceled. The linked page has the full eligibility and billing terms.

## Further reading and viewing

- [Andrej Karpathy, Intro to Large Language Models](https://www.youtube.com/watch?v=zjkBMFhNj_g) is a general-audience video on the models that agents use.
- [Anthropic, Building effective agents](https://www.anthropic.com/engineering/building-effective-agents) explains common agent designs and when they are useful.
- [Sebastian Raschka, Components of a Coding Agent](https://magazine.sebastianraschka.com/p/components-of-a-coding-agent) explains how tools, context, and memory fit around a model.
- [Boris Cherny, Claude Code best practices](https://code.claude.com/docs/en/best-practices) provides practical guidance for working with a coding agent.
- [Simon Willison, Agentic Engineering Patterns](https://simonwillison.net/2026/Feb/23/agentic-engineering-patterns/) introduces his ongoing writing about using coding agents and checking their work.
- [Ethan Mollick, Management as AI superpower](https://www.oneusefulthing.org/p/management-as-ai-superpower) examines how to assign and evaluate agent work in business settings.

## Examples and starters

| Exercise | Completed example | Student starter |
|---|---|---|
| Customer segmentation | [Analysis and instructions](customer-segmentation/README.md), [DOCX report](customer-segmentation/output/full/customer_segmentation_report.docx), [interactive explorer](customer-segmentation/output/full/segment_explorer.html), and [review overview](customer-segmentation/output/full/process_overview.html) | [Source data, transcript, and agent instructions](customer-segmentation-base/SETUP.md) |
| Reddit posting | [Analysis and instructions](reddit/README.md), [working paper](reddit/paper/main.pdf), and [analysis and review report](reddit/report.html) | [Transcript, data placeholder, and agent instructions](reddit-base/SETUP.md) |

The completed folders contain code, generated results, and review records. Each starter contains its original transcript and a `SETUP.md` file, which gives the agent its writing and review instructions. The customer starter includes its source data. The Reddit starter contains an empty `data/` placeholder because its source file is not tracked here.

To begin an exercise, copy its starter folder to a working location. Ask Codex to read `SETUP.md` and `transcript.txt`, clarify consequential choices, and plan the work before running the analysis. The [getting-started guides](#getting-started) give the exact steps and prompts. Students create their own environment, analysis code, deliverables, and review record in that copy.

## Environments

Students do not need to run the completed examples, because their outputs are already in the repository. The completed examples are separate [Pixi](https://pixi.sh) projects. To rerun one, run `pixi install` inside `customer-segmentation/` or `reddit/`, then follow that folder's README. There is no Pixi project at the repository root. Both manifests are locked for Linux (`linux-64`), macOS (`osx-arm64` and `osx-64`), and Windows (`win-64`). The examples were run on Linux, and the macOS and Windows environments resolve but have not been tested on those systems. The starters intentionally have no Pixi manifests because creating an environment is part of each transcript's assignment. The PDF versions of the getting-started guides are built from the markdown by `getting-started/build/build-pdf.sh`, which should be rerun after any edit to a guide.

## Data

The customer segmentation example uses eight Parquet files from the simulated [Complete Journey dataset](https://github.com/cunningjames/completejourney_py). They are included unchanged in both `customer-segmentation/data/` and `customer-segmentation-base/data/`.

The Reddit example uses a proprietary Parquet file that is excluded from this repository. Obtain [`user_daily_post_counts.parquet`](https://drive.google.com/file/d/1SzuIzRBhRdKuvNmBKqvhI-WFv4lRfXBr/view?usp=sharing) (approximately 756 MB) and place it in the `data/` folder of the working copy of `reddit-base` (step 7 of the getting-started guides), or in `reddit/data/` to rerun the completed example. Google Drive warns that it cannot scan a file this large for viruses, and **Download anyway** continues the download. Do not commit the source file.
