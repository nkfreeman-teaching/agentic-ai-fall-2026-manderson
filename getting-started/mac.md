# Getting started on a Mac

This guide sets up a Mac to run the two workshop exercises with Codex, OpenAI's coding agent. It covers opening the Terminal, downloading the workshop materials, installing Codex and Pixi (a tool that creates Python environments), running the customer segmentation exercise, and adding what the Reddit exercise needs (a data file and LaTeX). Windows users should follow the [Windows guide](windows.md) instead. The [workshop transcript](../sessions/2026-09-25-transcript.md) and [recording](https://alabama.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=8d3f444c-8b6a-490b-9738-b4d00129a3a7) show both exercises being started live.

Each exercise requires the following:

- A ChatGPT account. The Plus plan gives full Codex access, and eligible students can claim four free months through OpenAI's [Back to School offer](https://help.openai.com/en/articles/20001493-chatgpt-back-to-school-offer-for-students) by October 31, 2026. The Free plan offers only limited Codex access in the desktop app.
- A Mac with an internet connection and a few gigabytes of free disk space (more for the optional full LaTeX install in step 7).
- No Python or programming experience. The agent writes and runs the code.

## 1. Open the Terminal and learn six commands

The Terminal is a window where commands are typed instead of clicked. Even students who plan to use the Codex desktop app need it to install Pixi and to check that installs worked.

To open it, press Command+Space, type `Terminal`, and press Return. A window opens with a prompt ending in `%`. Type a command after the prompt and press Return to run it.

| Command | What it does |
|---|---|
| `pwd` | Prints the folder the Terminal is currently in |
| `ls` | Lists the files in the current folder |
| `cd agentic-ai` | Moves into the folder named `agentic-ai` |
| `cd ..` | Moves up one folder |
| `cd ~` | Returns to the home folder |
| `open .` | Opens the current folder in Finder |

Three habits make the Terminal much easier to use:

- Type `cd ` (with a trailing space), then drag a folder from Finder into the Terminal window. The Terminal fills in the folder's full path, so pressing Return moves into that folder.
- Press Tab partway through a file or folder name, and the Terminal completes it.
- Press Control+C to stop a command that is running. Paste with Command+V as usual.

## 2. Download the workshop materials

1. Open the [workshop repository](https://github.com/nkfreeman-teaching/agentic-ai-fall-2026-manderson), click the green **Code** button, and choose **Download ZIP**.
2. Double-click `agentic-ai-fall-2026-manderson-main.zip` in the Downloads folder. Finder unzips it into a folder with the same name.
3. Create a working folder named `agentic-ai` in the home folder (the folder with the house icon in the Finder sidebar). Keeping the work outside Desktop and Documents avoids problems if iCloud syncs those folders, since the Python environments contain thousands of small files.
4. Copy `customer-segmentation-base` (and later `reddit-base`) from the unzipped folder into `agentic-ai`.

Working in a copy of a starter folder matters for two reasons. The original stays unchanged if an attempt needs to start over, and the agent cannot look at the completed example in the neighboring folder and copy it.

The same step from the Terminal is:

```bash
mkdir -p ~/agentic-ai
cp -R ~/Downloads/agentic-ai-fall-2026-manderson-main/customer-segmentation-base ~/agentic-ai/
```

## 3. Install Codex

Codex comes in two forms, and either one works for the exercises. The desktop app is easier to start with and has a dictation button for spoken prompts. The command-line version runs inside the Terminal, which is what the workshop demo used.

**Desktop app.** OpenAI's desktop app is now called the ChatGPT desktop app, and Codex is one mode inside it. Download it from OpenAI's [quickstart page](https://learn.chatgpt.com/docs/quickstart), open it, and sign in with the ChatGPT account. Choose **Codex** from the menu at the top of the sidebar (it switches between ChatGPT and Codex).

**Command-line version.** Paste this into the Terminal and press Return:

```bash
curl -fsSL https://chatgpt.com/codex/install.sh | sh
```

Students who already use Homebrew can run `brew install --cask codex` instead. Close the Terminal window, open a new one, and run `codex --version`. A version number means the install worked. The first time `codex` starts, choose **Sign in with ChatGPT** and finish signing in in the browser.

## 4. Install Pixi

Pixi creates a separate Python environment inside each project folder, so the packages one project needs never conflict with another. The exercises ask the agent to use it. Paste this into the Terminal:

```bash
curl -fsSL https://pixi.sh/install.sh | sh
```

Close the Terminal window, open a new one, and run `pixi --version`. If a version number appears, Pixi is installed and the agent can use it. If the ChatGPT desktop app was open during the install, quit it (Command+Q) and reopen it so that it can find Pixi.

## 5. Optional: install Git

Codex works without Git, but the desktop app uses Git to show exactly what changed and to undo changes. Run `git --version` in the Terminal. If Git is missing, macOS offers to install the Command Line Developer Tools. Accept, wait for the install to finish, and run `git --version` again.

## 6. Run the customer segmentation exercise

The starter folder contains eight data files, a dictated `transcript.txt` that describes the assignment, and a `SETUP.md` with writing and review guidance for the agent. The data are in Parquet, a compact format that a double-click will not open. That is expected, because the agent reads the files.

**Open the folder in Codex.**

- *Desktop app:* In Codex, add a project (or open a folder) and select `~/agentic-ai/customer-segmentation-base`. Leave the permission setting beneath the message box at its default, so Codex asks before doing anything outside the folder.
- *Terminal:* Run `cd ~/agentic-ai/customer-segmentation-base`, then `codex`. Answer yes when Codex asks whether to trust the folder.

The model name appears in the app beneath the message box and in the Terminal at the top of the session. GPT-6 Sol at medium effort is a good default (type `/model` in the Terminal to change it). Effort controls how much the model reasons before it acts.

**Work in stages.** The full exercise ends in a review loop in which many reviewer agents score the work over several rounds, and that loop uses a large share of a Plus plan's weekly Codex usage. Sending the prompts below one at a time shows results sooner and makes it less likely that a usage limit interrupts the work midway. Read the agent's reply after each prompt before sending the next one.

Prompt 1 asks for questions and a plan before any work begins:

```text
Read SETUP.md and transcript.txt. They describe my assignment. Before you run
anything, ask me about any choice that would change the result, then give me a
step-by-step plan. Use Pixi to create the environment in this folder. Do not
start the review loop yet.
```

Answer its questions in plain language. It is fine to say, "I don't know, what do you recommend and why?"

Prompt 2 runs the analysis and builds the first drafts:

```text
The plan looks good. Run the analysis, prototyping on a small sample first,
and build first versions of the DOCX report and the HTML explorer. When you
finish, summarize what you found and open the explorer in my browser.
```

Prompt 3 adds one round of independent criticism:

```text
Spawn two subagents as independent skeptical reviewers, one focused on
methods and one on marketing, as described in SETUP.md. Each should return
specific findings with a proposed fix for each. Verify every finding yourself,
tell me which ones you accept or reject and why, then apply the accepted fixes.
```

Prompt 4 is optional and runs the full scored review loop:

```text
Run the scored review loop described in SETUP.md, with three independent
reviewer subagents per pass and the scoring and stopping rules it gives.
Finish with the process overview.
```

In the Terminal, `/status` shows the model and session settings. If a usage limit is reached, the work can continue after the limit resets. In the Terminal, `codex resume` reopens the previous session.

**Understand the result.** Everything the agent produces is the student's responsibility. Open the report and the explorer and ask about anything unclear, for example, "Why did you choose five segments instead of four?" or "Walk me through how the spending features are calculated, step by step." The results do not need to match the completed example in `customer-segmentation/`. A different, well-justified segmentation is a good outcome.

## 7. Run the Reddit exercise

The Reddit exercise asks the agent to write a short research paper in LaTeX, a typesetting system common in academic writing. It needs two things the customer exercise does not.

**Download the data file.** Download [`user_daily_post_counts.parquet`](https://drive.google.com/file/d/1SzuIzRBhRdKuvNmBKqvhI-WFv4lRfXBr/view?usp=sharing) (approximately 756 MB) from Google Drive. Move it into `~/agentic-ai/reddit-base/data/`, and check that the file name is exactly `user_daily_post_counts.parquet`.

**LaTeX through Pixi (recommended).** No separate install is needed. Tectonic is a small LaTeX engine that Pixi can install inside the project, and it downloads whatever LaTeX packages the paper needs the first time it compiles. The first Reddit prompt below asks the agent to set it up.

**Full LaTeX install (optional).** Students who want LaTeX for their own papers, outside these exercises, can install [MacTeX](https://www.tug.org/mactex/), which includes the TeXShop editor and every common package. MacTeX is a download of roughly 6 GB. The same page offers BasicTeX, which is much smaller but installs fewer packages. After installing, open a new Terminal and run `latexmk -v` to confirm the install. With MacTeX installed, the agent can use `latexmk` instead of Tectonic.

**Prompts.** Open `~/agentic-ai/reddit-base` in Codex as in step 6, and use the same staged approach. The first prompt differs.

```text
Read SETUP.md and transcript.txt. They describe my assignment. Before you run
anything, ask me about any choice that would change the result, then give me a
step-by-step plan. Use Pixi to create the environment in this folder, and add
tectonic from conda-forge to that environment to compile the LaTeX paper. The
data file is large, so prototype on a small sample before scanning all of it.
Do not start the review loop yet.
```

The transcript asks the agent to search published research through the Crossref API, whose "polite pool" asks callers to identify themselves with an email address. Give the agent a university email address when it asks. Continue with prompts 2 through 4 from step 6, replacing "DOCX report and the HTML explorer" with "LaTeX paper" and the methods and marketing reviewers with the reviewer perspectives in the Reddit `SETUP.md`.

## Troubleshooting

| Problem | Fix |
|---|---|
| `command not found: codex` or `command not found: pixi` | Close the Terminal window and open a new one. Installers update settings that only new windows read. |
| The agent says Pixi is not installed | Quit and reopen the ChatGPT desktop app, or start a new Terminal session, after installing Pixi. |
| Codex asks for approval before running a command | Read the command, then approve it if it works inside the project folder. Asking first is the safe default. |
| A usage limit message appears | Wait for the limit to reset, then continue. In the Terminal, `codex resume` reopens the session. |
| The agent seems stuck | Click the stop button in the app, or press Escape in the Terminal, then describe what should happen next. |
