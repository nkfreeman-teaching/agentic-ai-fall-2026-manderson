# Getting started on Windows

This guide sets up a Windows computer to run the two workshop exercises with Codex, OpenAI's coding agent. It covers opening PowerShell, downloading the workshop materials, installing Codex and Pixi (a tool that creates Python environments), running the customer segmentation exercise, and adding what the Reddit exercise needs (a data file and LaTeX). Mac users should follow the [Mac guide](mac.md) instead. The [workshop transcript](../sessions/2026-09-25-transcript.md) and [recording](https://alabama.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=8d3f444c-8b6a-490b-9738-b4d00129a3a7) show both exercises being started live.

Each exercise requires the following:

- A ChatGPT account. The Plus plan gives full Codex access, and eligible students can claim four free months through OpenAI's [Back to School offer](https://help.openai.com/en/articles/20001493-chatgpt-back-to-school-offer-for-students) by October 31, 2026. The Free plan offers only limited Codex access in the desktop app.
- A Windows 10 or 11 computer with an internet connection and a few gigabytes of free disk space (more for the optional full LaTeX install in step 7).
- No Python or programming experience. The agent writes and runs the code.

Codex runs natively on Windows using PowerShell. Windows Subsystem for Linux (WSL) is not needed for these exercises.

## 1. Open PowerShell and learn six commands

PowerShell is a window where commands are typed instead of clicked. Even students who plan to use the Codex desktop app need it to install Pixi and to check that installs worked.

To open it, press the Windows key, type `PowerShell`, and press Enter. On Windows 11, the app may be called Terminal, and it opens PowerShell by default. A window opens with a prompt such as `PS C:\Users\name>`. Type a command after the prompt and press Enter to run it.

| Command | What it does |
|---|---|
| `pwd` | Prints the folder PowerShell is currently in |
| `ls` | Lists the files in the current folder |
| `cd agentic-ai` | Moves into the folder named `agentic-ai` |
| `cd ..` | Moves up one folder |
| `cd ~` | Returns to the home folder (`C:\Users\name`) |
| `explorer .` | Opens the current folder in File Explorer |

Three habits make PowerShell much easier to use:

- On Windows 11, right-click a folder in File Explorer and choose **Open in Terminal**. PowerShell opens already inside that folder.
- Press Tab partway through a file or folder name, and PowerShell completes it.
- Press Control+C to stop a command that is running. Paste with Control+V or a right-click.

## 2. Download the workshop materials

1. Open the [workshop repository](https://github.com/nkfreeman-teaching/agentic-ai-fall-2026-manderson), click the green **Code** button, and choose **Download ZIP**.
2. In the Downloads folder, right-click `agentic-ai-fall-2026-manderson-main.zip` and choose **Extract All**, then **Extract**. Double-clicking the ZIP only previews its contents, and an agent cannot work on files that are still inside a ZIP.
3. Create a working folder named `agentic-ai` directly in the home folder, i.e., `C:\Users\name\agentic-ai`. The Documents and Desktop folders are often synced by OneDrive, which can lock files while the agent is writing them and slow down the thousands of small files in a Python environment.
4. Copy `customer-segmentation-base` (and later `reddit-base`) from the extracted folder into `agentic-ai`. Extract All usually creates a folder inside a folder with the same name, so open the inner folder to find the starter folders.

Working in a copy of a starter folder matters for two reasons. The original stays unchanged if an attempt needs to start over, and the agent cannot look at the completed example in the neighboring folder and copy it.

## 3. Install Codex

Codex comes in two forms, and either one works for the exercises. The desktop app is easier to start with and has a dictation button for spoken prompts. The command-line version runs inside PowerShell, which is what the workshop demo used.

**Desktop app.** OpenAI's desktop app is now called the ChatGPT desktop app, and Codex is one mode inside it. Install it from the Microsoft Store through OpenAI's [quickstart page](https://learn.chatgpt.com/docs/quickstart), or run this in PowerShell:

```powershell
winget install --id 9PLM9XGG6VKS -s msstore
```

Open the app, sign in with the ChatGPT account, and choose **Codex** from the menu at the top of the sidebar (it switches between ChatGPT and Codex). Leave the agent setting at **Windows native**.

**Command-line version.** Paste this into PowerShell and press Enter:

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://chatgpt.com/codex/install.ps1 | iex"
```

Close PowerShell, open a new window, and run `codex --version`. A version number means the install worked. The first time `codex` starts, choose **Sign in with ChatGPT** and finish signing in in the browser.

## 4. Install Pixi

Pixi creates a separate Python environment inside each project folder, so the packages one project needs never conflict with another. The exercises ask the agent to use it. Paste this into PowerShell:

```powershell
powershell -ExecutionPolicy Bypass -c "irm -useb https://pixi.sh/install.ps1 | iex"
```

Students who prefer the Windows package manager can run `winget install prefix-dev.pixi` instead. Close PowerShell, open a new window, and run `pixi --version`. If a version number appears, Pixi is installed and the agent can use it. If the ChatGPT desktop app was open during the install, close it completely and reopen it so that it can find Pixi.

## 5. Recommended: install Git

Codex works without Git, but the desktop app uses Git to show exactly what changed and to undo changes. OpenAI recommends it for Codex on Windows. Run this in PowerShell, then close and reopen PowerShell:

```powershell
winget install --id Git.Git
```

## 6. Run the customer segmentation exercise

The starter folder contains eight data files, a dictated `transcript.txt` that describes the assignment, and a `SETUP.md` with writing and review guidance for the agent. The data are in Parquet, a compact format that Windows does not know how to open. That is expected, because the agent reads the files.

**Open the folder in Codex.**

- *Desktop app:* In Codex, click **Add new project** (or press Control+O) and select `C:\Users\name\agentic-ai\customer-segmentation-base`. Leave the permission setting beneath the message box at its default, so Codex asks before doing anything outside the folder.
- *PowerShell:* Run `cd ~\agentic-ai\customer-segmentation-base`, then `codex`. Answer yes when Codex asks whether to trust the folder.

The model name appears in the app beneath the message box and in PowerShell at the top of the session. GPT-6 Sol at medium effort is a good default (type `/model` in PowerShell to change it). Effort controls how much the model reasons before it acts.

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

In PowerShell, `/status` shows the model and session settings. If a usage limit is reached, the work can continue after the limit resets. In PowerShell, `codex resume` reopens the previous session.

**Understand the result.** Everything the agent produces is the student's responsibility. Open the report and the explorer and ask about anything unclear, for example, "Why did you choose five segments instead of four?" or "Walk me through how the spending features are calculated, step by step." The results do not need to match the completed example in `customer-segmentation\`. A different, well-justified segmentation is a good outcome.

## 7. Run the Reddit exercise

The Reddit exercise asks the agent to write a short research paper in LaTeX, a typesetting system common in academic writing. It needs two things the customer exercise does not.

**Download the data file.** Download [`user_daily_post_counts.parquet`](https://drive.google.com/file/d/1SzuIzRBhRdKuvNmBKqvhI-WFv4lRfXBr/view?usp=sharing) (approximately 756 MB) from Google Drive. Move it into `C:\Users\name\agentic-ai\reddit-base\data\`, and check that the file name is exactly `user_daily_post_counts.parquet`. File Explorer hides file extensions by default, so the name may appear as `user_daily_post_counts`.

**LaTeX through Pixi (recommended).** No separate install is needed. Tectonic is a small LaTeX engine that Pixi can install inside the project, and it downloads whatever LaTeX packages the paper needs the first time it compiles. The first Reddit prompt below asks the agent to set it up.

**Full LaTeX install (optional).** Students who want LaTeX for their own papers, outside these exercises, can install [MiKTeX](https://miktex.org/download), which downloads packages the first time a document needs them. The command is `winget install MiKTeX.MiKTeX`. MiKTeX's `latexmk` tool also needs Perl, which `winget install StrawberryPerl.StrawberryPerl` installs. After installing both, open a new PowerShell window and run `latexmk -v` to confirm the install. With MiKTeX installed, the agent can use `latexmk` instead of Tectonic.

**Prompts.** Open `C:\Users\name\agentic-ai\reddit-base` in Codex as in step 6, and use the same staged approach. The first prompt differs.

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
| `codex` or `pixi` "is not recognized as the name of a cmdlet" | Close PowerShell and open a new window. Installers update settings that only new windows read. |
| "running scripts is disabled on this system" | Run `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`, answer `Y`, and try again. This lets PowerShell run scripts created on this computer. |
| The agent says Pixi is not installed | Close the ChatGPT desktop app completely and reopen it, or start a new PowerShell window, after installing Pixi. |
| Codex asks for approval before running a command | Read the command, then approve it if it works inside the project folder. Asking first is the safe default. |
| Files are locked or an install fails partway | Check that the project is not inside a OneDrive folder, and move it to `C:\Users\name\agentic-ai` if it is. |
| A usage limit message appears | Wait for the limit to reset, then continue. In PowerShell, `codex resume` reopens the session. |
| The agent seems stuck | Click the stop button in the app, or press Escape in PowerShell, then describe what should happen next. |
