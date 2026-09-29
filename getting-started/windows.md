# Getting started on Windows

This guide takes you from a Windows computer with nothing installed to running the two workshop exercises with Codex, OpenAI's coding agent. You do not need any programming experience, because the agent writes and runs the code. On a Mac, use the [Mac guide](mac.md) instead.

The guide has seven steps:

1. Download the workshop materials and set up a working folder.
2. Open PowerShell.
3. Install Codex.
4. Install Pixi.
5. Install Git.
6. Run the customer segmentation exercise.
7. Run the Reddit exercise.

If you missed the workshop, the [recording](https://alabama.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=8d3f444c-8b6a-490b-9738-b4d00129a3a7) and the [edited transcript](../sessions/2026-09-25-transcript.md) show both exercises being started live.

## Before you start

Check each item before you install anything.

- **Windows 10 or 11.** To check, open **Settings**, then **System**, then **About**.
- **At least 10 GB of free disk space.** To check, open **Settings**, then **System**, then **Storage**.
- **Permission to install software.** Windows will show boxes that ask, "Do you want to allow this app to make changes to your device?" You need to be able to click **Yes**. On a laptop managed by your university, installs may be blocked or ask for an administrator password. If they do, ask your IT help desk or use a personal computer. Do not try to work around a university security setting.
- **A ChatGPT account.** The Plus plan ($20 a month) is the plan these exercises were built for. Eligible U.S. students can get four free months through OpenAI's [Back to School offer](https://help.openai.com/en/articles/20001493-chatgpt-back-to-school-offer-for-students) by claiming it before October 31, 2026. The offer asks for a payment method and renews at $20 a month unless you cancel, so put a reminder in your calendar now.
- **If you stay on the Free plan,** Codex works only in the desktop app, with the smaller GPT-6 Luna model. Free access is meant for quick tasks, so you can start the customer exercise, but the later review prompts may not finish.
- **Time and power.** Setup involves several downloads, and the agent works for many minutes after each prompt. Keep the computer plugged in and awake while the agent works, because the work pauses when the computer sleeps.

You do not need Windows Subsystem for Linux (WSL). Codex runs directly on Windows.

## 1. Download the materials and set up a working folder

You will copy two starter folders, one per exercise, into a new folder named `agentic-ai` in your home folder. In this guide, `C:\Users\name` means your home folder, where `name` is your Windows user name.

1. Open the [workshop repository](https://github.com/nkfreeman-teaching/agentic-ai-fall-2026-manderson) in your web browser.
2. Click the green **Code** button, then click **Download ZIP**.
3. Press Windows+E to open File Explorer, and click **Downloads** in the left panel.
4. Right-click `agentic-ai-fall-2026-manderson-main.zip` and choose **Extract All**, then click **Extract**. Double-clicking the ZIP only previews it, and the agent cannot work on files that are still inside a ZIP.
5. A new folder opens. It usually contains another folder with the same name, `agentic-ai-fall-2026-manderson-main`. Open that inner folder. You should see `customer-segmentation-base` and `reddit-base`.
6. Click the address bar at the top of File Explorer, type `%USERPROFILE%`, and press Enter. This opens your home folder.
7. Create a folder. On Windows 11, click **New** at the top left, then **Folder**. On Windows 10, right-click an empty area and choose **New**, then **Folder**. Name it `agentic-ai` and press Enter.
8. Go back to the inner download folder from item 5.
9. Click `customer-segmentation-base`, then hold Control and click `reddit-base`, so both are selected. Press Control+C to copy them.
10. Open the `agentic-ai` folder in your home folder and press Control+V to paste.

**Check.** The `agentic-ai` folder now contains `customer-segmentation-base` and `reddit-base`. Open `customer-segmentation-base`. You should see `SETUP`, `transcript`, and a `data` folder. File Explorer hides file endings such as `.md` and `.txt`, so the files may appear without them.

Two points about this setup:

- **Why the home folder.** Desktop and Documents are often synced by OneDrive. The agent creates thousands of small files, and OneDrive can lock them while the agent is writing, which causes errors.
- **Why a copy.** If an attempt goes wrong, you can delete the copy and paste a fresh one. The copy also keeps the agent away from the completed examples in the download, so it cannot copy their answers.

## 2. Open PowerShell

PowerShell is a window where you type commands instead of clicking. You need it to install Pixi and Git and to check that each install worked.

1. Press the Windows key, type `PowerShell`, and press Enter. On Windows 11, the app may be called **Terminal**. It opens PowerShell too.
2. A window opens with a line such as `PS C:\Users\name>`. This line is the prompt.
3. To run a command, type or paste it after the prompt and press Enter. Paste with Control+V or a right-click.

Try it now. Type `cd ~\agentic-ai` and press Enter, then type `ls` and press Enter. You should see `customer-segmentation-base` and `reddit-base`.

These commands are all you need:

| Command | What it does |
|---|---|
| `pwd` | Shows which folder PowerShell is in |
| `ls` | Lists the files in that folder |
| `cd agentic-ai` | Moves into the folder named `agentic-ai` |
| `cd ..` | Moves up one folder |
| `cd ~` | Returns to your home folder (`~` is short for `C:\Users\name`) |
| `explorer .` | Opens the current folder in File Explorer |

Three tips:

- Press Tab partway through a file or folder name, and PowerShell finishes it for you.
- On Windows 11, right-click a folder in File Explorer and choose **Open in Terminal**. PowerShell opens inside that folder.
- Press Control+C to stop a command that is running.

## 3. Install Codex

Codex comes in two forms. **Use the desktop app** unless you already use PowerShell comfortably. The desktop app is easier to start with and has a button for speaking your prompts. The workshop demo used the command-line version, which runs in PowerShell and needs the Plus plan.

**Desktop app (recommended).** The desktop app is called ChatGPT, and Codex is one mode inside it.

1. Go to OpenAI's [quickstart page](https://learn.chatgpt.com/docs/quickstart) and follow the link to install the ChatGPT desktop app from the Microsoft Store. If the Store is blocked, paste this into PowerShell instead and press Enter:

   ```powershell
   winget install --id 9PLM9XGG6VKS -s msstore
   ```

   If PowerShell asks whether you agree to the source terms, type `Y` and press Enter.

2. Open ChatGPT from the Start menu and sign in with your ChatGPT account.
3. Choose **Codex** from the menu at the top of the sidebar, which switches between ChatGPT and Codex.
4. In **Settings**, leave the agent setting at **Windows native**.

**Command-line version (alternative, needs Plus).** Paste this into PowerShell and press Enter:

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://chatgpt.com/codex/install.ps1 | iex"
```

Then check the install:

1. Close PowerShell and open a new window. Installers change settings that only new windows read.
2. Type `codex --version` and press Enter. You should see a version number.

The first time you run `codex`, choose **Sign in with ChatGPT** and finish signing in in your browser.

## 4. Install Pixi

Pixi creates a separate Python environment, i.e., a private set of Python tools, inside each exercise folder. The exercises ask the agent to use it, so you install it once and the agent does the rest.

1. Paste this into PowerShell and press Enter:

   ```powershell
   powershell -ExecutionPolicy Bypass -c "irm -useb https://pixi.sh/install.ps1 | iex"
   ```

2. Close PowerShell and open a new window.
3. Type `pixi --version` and press Enter. You should see a version number.
4. If the ChatGPT app was open during the install, quit it and open it again, so that it can find Pixi. If its icon still shows near the clock after you close the window, right-click the icon and choose **Quit**.

If the install command fails, `winget install prefix-dev.pixi` is another way to install Pixi.

## 5. Install Git (recommended)

Git records every change to the files in a folder. With Git installed, Codex can show you exactly what it changed and undo a change. OpenAI recommends Git for Codex on Windows.

1. Paste this into PowerShell and press Enter:

   ```powershell
   winget install --id Git.Git
   ```

2. If Windows asks whether to allow the app to make changes, click **Yes**.
3. Close PowerShell and open a new window.
4. Type `git --version` and press Enter. You should see a version number.

If `winget` is not recognized, download Git from [git-scm.com](https://git-scm.com/downloads/win) instead and accept the installer's default choices.

## 6. Run the customer segmentation exercise

The `customer-segmentation-base` folder has three things:

- `transcript.txt`, a dictated description of the assignment.
- `SETUP.md`, instructions written for the agent.
- `data`, eight data files in Parquet, a compact data format. Windows cannot open them, and that is expected, because the agent reads them.

### Open the folder in Codex

**Desktop app.**

1. In Codex, click **Add new project** (or press Control+O).
2. Go to `C:\Users\name\agentic-ai`, click `customer-segmentation-base` once, and click **Select Folder**. You can also type `%USERPROFILE%\agentic-ai\customer-segmentation-base` in the address bar.
3. Find the permission control beneath the message box and choose **Ask for approval**.
4. Check the model name, which is also beneath the message box. On Plus, choose GPT-6 Sol at medium effort. On Free, GPT-6 Luna is the one available. Effort controls how long the model thinks before it acts.

The first time Codex runs a command, Windows may ask, "Do you want to allow this app to make changes to your device?" Codex is setting up its safety sandbox, which keeps it inside the exercise folder. Click **Yes**. If you cannot (for example, on a university laptop), Codex falls back to a weaker sandbox and keeps working.

**Command-line version.**

1. In PowerShell, type `cd ~\agentic-ai\customer-segmentation-base` and press Enter.
2. Type `codex` and press Enter.
3. When Codex asks whether to trust the folder, choose the option that lets it work in this folder. Do not choose read-only.
4. The model name appears at the top of the session. Type `/model` to choose GPT-6 Sol at medium effort.

### When Codex asks permission

In **Ask for approval** mode, Codex changes files inside the exercise folder on its own. It stops and asks before it uses the internet or touches anything outside the folder.

- **Say yes** when it asks to install packages with `pixi`, to download LaTeX packages, to search Crossref or the web, or to open a file in your browser. The exercises need these. If Codex offers to stop asking about the same kind of command, choosing that option is fine.
- **Say no, and ask it why,** if a command would delete files outside the exercise folder or asks for your password.

### Check your usage before each prompt

Every prompt uses part of your Codex allowance, which resets every five hours and also has a weekly limit. See how much is left on the [usage dashboard](https://chatgpt.com/codex/settings/usage), or type `/status` in the command-line version. Prompt 4 uses a large share of a Plus plan's weekly allowance, so start it only when most of the week's allowance remains. If Codex offers to sell you extra credits when you reach a limit, you do not need them. Wait for the reset instead.

### Send the prompts one at a time

Copy each prompt below into Codex, send it, and read the reply before you send the next one. Working in stages shows you results sooner, and a usage limit is less likely to stop the work halfway.

**Prompt 1** asks for questions and a plan before any work begins:

```text
Read SETUP.md and transcript.txt. They describe my assignment. Before you run
anything, ask me about any choice that would change the result, then give me a
step-by-step plan. Use Pixi to create the environment in this folder. If Git
is installed, set up a Git repository in this folder so I can see and undo
your changes. Do not start the review loop yet.
```

*You should see* numbered questions and then a plan. No results exist yet. Answer the questions in plain language. It is fine to say, "I don't know, what do you recommend and why?" The agent will likely ask for an email address, because the transcript asks it to search published research through Crossref, a free research database that asks users to identify themselves. Give your university email address.

**Prompt 2** runs the analysis and builds the first drafts:

```text
The plan looks good. Run the analysis, prototyping on a small sample first,
and build first versions of the DOCX report and the HTML explorer. When you
finish, summarize what you found, list the exact name and location of every
file you created, and open the explorer in my browser.
```

*You should see* a summary of the customer groups the agent found, a list of files, and the explorer open in your browser. The DOCX report is a Word document, so double-click it in File Explorer to open it. To open the folder in File Explorer, type `explorer .` in PowerShell from the exercise folder, or ask Codex to open it.

**Prompt 3** adds one round of independent criticism:

```text
Spawn two subagents as independent skeptical reviewers, one focused on
methods and one on marketing, as described in SETUP.md. Each should return
specific findings with a proposed fix for each. Verify every finding yourself,
tell me which ones you accept or reject and why, then apply the accepted fixes.
```

Subagents are extra copies of the agent that Codex starts to review the work. *You should see* a list of findings, each marked accepted or rejected with a reason, and updated files.

**Prompt 4 (optional)** runs the full scored review loop:

```text
Run the scored review loop described in SETUP.md, with three independent
reviewer subagents per pass and the scoring and stopping rules it gives.
Finish with the process overview.
```

*You should see* several rounds of scores that should rise over time, and a process overview, i.e., an HTML page that records the scores and changes.

### Understand the result

You are responsible for everything the agent produces for you. Open the report and the explorer, and ask about anything unclear. For example:

- "Why did you choose five segments instead of four?"
- "Walk me through how the spending features are calculated, step by step."

Your results do not need to match the completed example in the `customer-segmentation` folder of the download. A different, well-justified segmentation is a good outcome.

## 7. Run the Reddit exercise

The Reddit exercise asks the agent to write a short research paper in LaTeX, a typesetting system common in academic writing. It needs a large data file that is not in the download.

### Get the data file

1. Check that `C:\Users\name\agentic-ai\reddit-base` exists. If it does not, copy `reddit-base` from the download as in step 1.
2. Open the [data file on Google Drive](https://drive.google.com/file/d/1SzuIzRBhRdKuvNmBKqvhI-WFv4lRfXBr/view?usp=sharing). You do not need to sign in.
3. Click the download button (a downward arrow, usually near the top right).
4. Google says it cannot scan the file for viruses because it is large. Click **Download anyway**.
5. Wait for the download to finish. The file is about 756 MB.
6. Move `user_daily_post_counts.parquet` from Downloads into `C:\Users\name\agentic-ai\reddit-base\data\`.

**Check.** In File Explorer, right-click the file and choose **Properties**. The name must be `user_daily_post_counts` with type "PARQUET File" (File Explorer may hide the `.parquet` ending), and the size about 756 MB. If your browser renamed it (for example, with a `(1)` at the end), rename it.

### LaTeX

You do not need to install LaTeX yourself. The first Reddit prompt asks the agent to add Tectonic, a small LaTeX program, inside the exercise folder. The first time the paper compiles, Tectonic downloads the pieces it needs, so say yes when Codex asks.

If you want LaTeX for your own papers later, you can install [MiKTeX](https://miktex.org/download). It is not needed for these exercises.

### Send the prompts one at a time

Open `C:\Users\name\agentic-ai\reddit-base` in Codex as in step 6, check your usage, and send these prompts one at a time.

**Prompt 1:**

```text
Read SETUP.md and transcript.txt. They describe my assignment. Before you run
anything, ask me about any choice that would change the result, then give me a
step-by-step plan. Use Pixi to create the environment in this folder, and add
tectonic from conda-forge to that environment to compile the LaTeX paper. If
Git is installed, set up a Git repository in this folder. The data file is
large, so prototype on a small sample before scanning all of it. Do not start
the review loop yet.
```

*You should see* numbered questions and a plan. As in the customer exercise, give your university email address when it asks for one for Crossref.

**Prompt 2:**

```text
The plan looks good. Run the analysis, prototyping on a small sample first,
then on the full file. Write the first complete version of the LaTeX paper and
compile it to PDF with tectonic. When you finish, summarize what you found,
list the exact name and location of every file you created, and open the PDF.
```

*You should see* a summary of the findings, a list of files, and the paper open as a PDF. The full data file is large, so this prompt can take a long time.

**Prompt 3:**

```text
Spawn two subagents as independent skeptical reviewers of the paper, with the
different perspectives described in SETUP.md. Each should return specific
findings with a proposed fix for each. Verify every finding yourself, tell me
which ones you accept or reject and why, then apply the accepted fixes and
recompile the paper.
```

*You should see* a list of findings, each marked accepted or rejected with a reason, and an updated PDF.

**Prompt 4 (optional):**

```text
Run the scored review loop described in SETUP.md, with three independent
reviewer subagents per round and the scoring and stopping rules it gives.
Finish with the process report.
```

*You should see* several rounds of scores and a process report that records them.

## Troubleshooting

| Problem | What to do |
|---|---|
| `codex` or `pixi` "is not recognized as the name of a cmdlet" | Close PowerShell and open a new window. Installers change settings that only new windows read. |
| "running scripts is disabled on this system" | Run `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`, type `Y`, and try again. If Windows says a policy overrides the setting, your computer is managed by your university. Ask your IT help desk or use a personal computer. |
| `winget` is not recognized, or the Microsoft Store is blocked | Install ChatGPT from the [quickstart page](https://learn.chatgpt.com/docs/quickstart), Pixi with the install command in step 4, and Git from [git-scm.com](https://git-scm.com/downloads/win). |
| The agent says Pixi is not installed | Quit the ChatGPT app completely (see step 4) and open it again, or open a new PowerShell window. |
| Codex asks for approval before running a command | See "When Codex asks permission" in step 6. |
| Codex asks before every single file change | You chose read-only. In the app, set the permission control to **Ask for approval**. In PowerShell, type `/permissions` and choose the option that lets Codex work in the folder. |
| Codex says its sandbox setup failed | You declined, or could not approve, the Windows administrator box. Codex keeps working with a weaker sandbox, which is fine for these exercises. |
| Files are locked, or an install fails partway | Check that your folder is `C:\Users\name\agentic-ai` and not inside OneDrive, Desktop, or Documents. |
| A usage limit message appears | Wait for the limit to reset. You do not need to buy credits. Then continue as in the next row. |
| The computer went to sleep, or you closed Codex | In the app, click the conversation in the sidebar and send "Continue where you left off." In PowerShell, run `codex resume` from the exercise folder. |
| The agent seems stuck | Click the stop button in the app, or press Escape in PowerShell. Then describe what should happen next. |
| You cannot find a file the agent made | Ask Codex, "Where is the file you just created? Open its folder in File Explorer." |
| You want to start an exercise over | Delete the folder in `agentic-ai` and copy a fresh one from the download, as in step 1. |
