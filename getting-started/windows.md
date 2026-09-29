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

If you missed the workshop, the [recording](https://alabama.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=8d3f444c-8b6a-490b-9738-b4d00129a3a7) and the [edited transcript](../sessions/2026-09-25-transcript.md) show the download, Pixi, and a live Codex run on the customer data (from 00:23:17), and explain both exercises (from 00:45:20). The demo used the Desktop and a shorter prompt, so follow this guide's folders and prompts instead.

## Before you start

Check each item before you install anything.

- **Windows 11, or an up-to-date Windows 10.** To check, press Windows+R, type `winver`, and press Enter. Windows 11 works best. On Windows 10, the window should say **Version 22H2**, the final Windows 10 release. If it shows anything else, run Windows Update first. If your university prevents updates, ask your IT help desk or use another computer.
- **At least 10 GB of free disk space.** To check, open **Settings**, then **System**, then **Storage**.
- **Memory.** Note how much your computer has (**Settings**, then **System**, then **About**, then **Installed RAM**). The customer exercise is small. The Reddit exercise has only been run on a workstation, so on a laptop with 8 GB, read the memory estimate Codex gives after Reddit prompt 2 carefully before you run the full file.
- **Permission to install software.** Windows will show boxes that ask, "Do you want to allow this app to make changes to your device?" You need to be able to click **Yes**. On a laptop managed by your university, installs may be blocked or ask for an administrator password. If they do, ask your IT help desk or use a personal computer. Do not try to work around a university security setting.
- **A ChatGPT account.** The Plus plan ($20 a month) is the plan these exercises were built for. Eligible U.S. students can get four free months through OpenAI's Back to School offer by [claiming it](https://chatgpt.com/students/2026/) before October 31, 2026, and the [offer terms](https://help.openai.com/en/articles/20001493-chatgpt-back-to-school-offer-for-students) give the details. Keep these points in mind:
  - Claim it while signed in to the ChatGPT account you will use for Codex.
  - The offer does not apply to a Plus subscription billed through Apple or Google.
  - It asks for a payment method and renews at $20 a month unless you cancel, so put a reminder in your calendar now.
  - If you cancel early, the unused free months are lost.
- **If you are on the Free or Go plan,** Codex works only in the desktop app, with the smaller GPT-6 Luna model, and OpenAI is still rolling out that access. After you sign in (step 3), check that the app offers **Codex** before you install anything else. If it does not, wait for access or use a Plus account. Free and Go access is meant for quick tasks. Start with customer prompts 1 and 2, and stop when Codex reports a limit. The review prompts and the Reddit exercise may not fit, so check your allowance before you download the Reddit file or start a review prompt.
- **The Reddit data file.** The Reddit exercise needs a separate download of about 790 MB (step 7). You can do the customer exercise first.
- **Time and power.** Setup involves several downloads, and the agent works for many minutes after each prompt. Nobody has timed a full setup or exercise on a laptop yet, so do not start right before a deadline. The work pauses when the computer sleeps, so keep it plugged in with the lid open (step 3 also turns on a setting that keeps it awake).

You do not need Windows Subsystem for Linux (WSL). Codex runs directly on Windows.

## 1. Download the materials and set up a working folder

You will copy two starter folders, one per exercise, into a new folder named `agentic-ai` in your home folder. In this guide, `C:\Users\name` means your home folder, where `name` is your Windows user name.

1. Open the [workshop repository](https://github.com/nkfreeman-teaching/agentic-ai-fall-2026-manderson) in your web browser.
2. Click the green **Code** button, then click **Download ZIP**.
3. Press Windows+E to open File Explorer, and click **Downloads** in the left panel.
4. Right-click `agentic-ai-fall-2026-manderson-main.zip` and choose **Extract All**, then click **Extract**. Double-clicking the ZIP only previews it, and the agent cannot work on files that are still inside a ZIP.
5. A new folder opens. It usually contains another folder with the same name. Open that inner folder. You should see `customer-segmentation-base` and `reddit-base`.
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

Codex comes in two forms. **Use the desktop app** unless you already use PowerShell comfortably. The desktop app is easier to start with and has a button for speaking your prompts (on Plus, and speaking uses part of your Codex allowance). The workshop demo used the command-line version, which runs in PowerShell and needs the Plus plan.

**Desktop app (recommended).** The desktop app is called ChatGPT, and Codex is one mode inside it.

1. Click this [ChatGPT for Windows download link](https://get.microsoft.com/installer/download/9PLM9XGG6VKS?cid=website_cta_psi) and open the small file it downloads. It installs ChatGPT through the Microsoft Store. If the Store window does not open, paste this into PowerShell instead and press Enter:

   ```powershell
   winget install --id 9PLM9XGG6VKS -s msstore
   ```

   If PowerShell asks whether you agree to the source terms, type `Y` and press Enter. If your university blocks Microsoft Store installs, both routes fail, so ask your IT help desk to install the ChatGPT desktop app, or use a personal computer.

2. Open ChatGPT from the Start menu and sign in with your ChatGPT account. If it asks you to choose a workspace, choose your personal account, the one where you claimed the student offer.
3. Choose **Codex** from the menu at the top of the sidebar, which switches between ChatGPT and Codex.
4. Open **Settings** (Control+Comma), choose **General**, and turn on **Prevent sleep while running**, so the agent keeps working while you step away.
5. You do not need to change any other setting. If you ever see a choice between **Windows native** and **WSL**, keep **Windows native**.

**Command-line version (alternative, needs Plus).** Paste this into PowerShell and press Enter:

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://chatgpt.com/codex/install.ps1 | iex"
```

If it asks "Start Codex now? [y/N]", type `n` and press Enter. Then check the install:

1. Close PowerShell, then open it again as in step 2. Installers change settings that only new windows read.
2. Type `codex --version` and press Enter. You should see a version number.

The first time you run `codex`, choose **Sign in with ChatGPT** and finish signing in in your browser.

## 4. Install Pixi

Pixi creates a separate Python environment, i.e., a private set of Python tools, inside each exercise folder. The exercises ask the agent to use it, so you install it once and the agent does the rest.

1. Paste this into PowerShell and press Enter:

   ```powershell
   powershell -ExecutionPolicy Bypass -c "irm -useb https://pixi.sh/install.ps1 | iex"
   ```

2. Close PowerShell, then open it again as in step 2.
3. Type `pixi --version` and press Enter. You should see a version number.
4. If the ChatGPT app was open during the install, quit it and open it again, so that it can find Pixi. If its icon still shows near the clock after you close the window, right-click the icon and choose **Quit**.

If the install command fails, paste this into PowerShell instead and press Enter:

```powershell
winget install prefix-dev.pixi
```

## 5. Install Git (recommended)

Git records every change to the files in a folder. With Git installed, Codex can show you exactly what it changed and undo a change. OpenAI recommends Git for Codex on Windows.

1. Paste this into PowerShell and press Enter:

   ```powershell
   winget install --id Git.Git -e --source winget
   ```

2. If PowerShell asks whether you agree to the source terms, type `Y` and press Enter.
3. If Windows asks whether to allow the app to make changes, click **Yes**.
4. Close PowerShell, then open it again as in step 2.
5. Type `git --version` and press Enter. You should see a version number.
6. If the ChatGPT app is open, quit it and open it again (see step 4), so that it can find Git.

If `winget` is not recognized, download Git from [git-scm.com](https://git-scm.com/downloads/win) instead and accept the installer's default choices.

## 6. Run the customer segmentation exercise

The `customer-segmentation-base` folder has three things:

- `transcript.txt`, a dictated description of the assignment.
- `SETUP.md`, instructions written for the agent.
- `data`, eight data files in Parquet, a compact data format. Windows cannot open them, and that is expected, because the agent reads them.

To read `transcript.txt` or `SETUP.md` yourself, right-click it and choose **Open with**, then **Notepad** (if Notepad is not listed, click **Choose another app**, then **Notepad**). To see a finished result before you start, go to the inner download folder from step 1, open `customer-segmentation`, then `output`, then `full`, and double-click `segment_explorer.html`.

### Open the folder in Codex

**Desktop app.**

1. In Codex, click **Add new project** next to **Chats** in the sidebar (or press Control+O).
2. In the window that opens, click the address bar at the top, type the line below, and press Enter. Then click **Select Folder**.

   ```text
   %USERPROFILE%\agentic-ai\customer-segmentation-base
   ```

3. Find the permission control beneath the message box and choose **Ask for approval**.
4. Click the model control beneath the message box. It is called **Power** and shows a short list.
   - On Plus, choose **6 Sol Medium** (it may read **6.1 Sol Medium**). If neither is listed, click **Advanced**, pick the newest **Sol** model, and set the effort to **Medium**. If the only Sol model is **GPT-5.6 Sol** (this happened in the Windows app in September 2026), use it at **Medium**, and check your usage after each prompt, because it uses your allowance about twice as fast as GPT-6 Sol.
   - On Free or Go, choose **Luna High**, which is the Luna choice.
   - Avoid **Astra**, **Extra High**, **Max**, **Ultra**, and **Fast**. Astra allows about a third as many messages as Sol, Ultra starts extra subagents, and Fast uses your allowance 2.5 times as quickly.
5. Check that the chat runs on your computer. The control beneath the message box should say **Local** (or **Work in: This computer**), not **Worktree** or **Cloud**, because the data files exist only on your computer.

The first time Codex runs a command, Windows may ask, "Do you want to allow this app to make changes to your device?" Codex is setting up its safety sandbox, which keeps it inside the exercise folder. Click **Yes**. If you cannot (for example, on a university laptop), Codex tries a weaker sandbox. If commands then run, continue. If they still fail, ask your IT help desk or use a personal computer, and do not switch the permission control to **Full access** to get past the error.

**Command-line version.**

1. In PowerShell, type `cd ~\agentic-ai\customer-segmentation-base` and press Enter.
2. Type `codex` and press Enter.
3. When Codex asks whether to trust the folder, choose the option that lets it work in this folder. If it starts in read-only mode anyway, type `/permissions` and choose **Ask for approval** (older versions call it **Auto**).
4. The model name appears at the top of the session. Type `/model` and choose GPT-6 Sol (or GPT-6.1 Sol, if listed) with medium effort. If neither is listed, choose GPT-5.6 Sol with medium effort.

### When Codex asks permission

In **Ask for approval** mode, Codex changes files inside the exercise folder on its own. It stops and asks before it uses the internet or touches anything outside the folder.

- **Say yes** when it asks to install packages with `pixi`, to download LaTeX packages, to search Crossref or the web, or to open a file in your browser. The exercises need these. If Codex offers to stop asking about the same kind of command, choosing that option is fine.
- **Say yes** when it asks to run `git` commands such as `git init`, `git add`, `git commit`, or `git config` (which records your name and email for this folder). Git keeps its records in a protected hidden folder, so Codex asks first.
- **Say yes** if it asks to download a test browser for Playwright, a tool that lets the agent open the explorer and click through it. The download is a few hundred MB and stays in your user folder.
- **Say no** if it asks to install a program for the whole computer, such as LibreOffice, Python from python.org, or anything installed with `winget`. Reply, "Do not install software outside this folder. Use a Pixi package instead, or skip that check and tell me you skipped it."
- **Say no, and ask it why,** if a command would delete files outside the exercise folder, asks for your password, or opens a Windows box asking to allow changes (other than the first sandbox setup described above).

### Check your usage before each prompt

Every prompt uses part of your Codex allowance, which resets every five hours and also has a weekly limit. See how much is left on the [usage dashboard](https://chatgpt.com/codex/settings/usage), or type `/status` in the command-line version. OpenAI estimates that Plus allows roughly 15 to 150 Sol messages every five hours, depending on the task, and subagents' work counts too. Write down the percentage left before and after each prompt. After prompts 1 and 2, you will know roughly what a prompt costs you. The scored review loop (the last, optional prompt) uses a large share of a Plus plan's weekly allowance, so start it only when most of the week's allowance remains. If Codex offers to sell you extra credits when you reach a limit, you do not need them. Wait for the reset instead.

### Send the prompts one at a time

Copy each prompt below into Codex, send it, and read the reply before you send the next one. On GitHub, the copy icon at the top right of each gray box copies the whole prompt. In the PDF, drag across all the text in the box, copy it, and paste it (the line breaks are fine). Codex has finished when it stops working and waits for your reply. Working in stages shows you results sooner, and a usage limit is less likely to stop the work halfway.

**First message: check the folder and tools.** Before prompt 1, send this:

```text
Tell me the full path of the folder you are working in and list what it
contains. Then run pixi --version and git --version and tell me what each
prints. Do not change anything.
```

*You should see* a path ending in `customer-segmentation-base`, the files `SETUP.md` and `transcript.txt`, a `data` folder with eight files, and two version numbers (a note that Git is missing is fine). If the path ends in anything else, you opened the wrong folder, so open the right one as described above. If Pixi is not found, see the Troubleshooting row about Pixi.

**Prompt 1** asks for questions and a plan before any work begins:

```text
Read SETUP.md and transcript.txt. They describe my assignment. Before you run
anything, ask me about any choice that would change the result, then give me a
step-by-step plan. Use Pixi to create the environment in this folder. If Git
is installed, set up a Git repository in this folder and commit the unchanged
starter files first, so I can see and undo your changes. Do not start the
review loop yet.
```

*You should see* numbered questions and then a plan. No results exist yet. Answer the questions in plain language. It is fine to say, "I don't know, what do you recommend and why?" The agent will likely ask for an email address, because the transcript asks it to search published research through Crossref, a free research database. Crossref works without an email, but giving one (your university address is fine) puts your searches in a faster, more reliable queue. The agent may also ask what name and email to record with its Git commits. Your name and university email are fine, and they stay on your computer.

**Before you send prompt 2, check the plan.** The plan should name the folder ending in `-base`, mention the data files, and say where the report and explorer will be saved. If any of these is missing, or a step is unclear, ask about it and wait for a revised plan.

**Prompt 2** runs the analysis and builds the first drafts:

```text
I checked the plan. Carry it out: run the analysis, prototyping on a small
sample first, and build first versions of the DOCX report and the HTML
explorer. When you finish, summarize what you found, list the exact name and
location of every file you created, and open the explorer in my browser. Then
stop. Do not start reviewer subagents or the review loop until I ask.
```

*You should see* a summary of the customer groups the agent found, a list of files, and the explorer open in your browser. The DOCX report is a Word document, so double-click it in File Explorer to open it. If you do not have Word, your university's Microsoft 365 account or Google Docs can open it. To open the folder in File Explorer, type `explorer .` in PowerShell from the exercise folder, or ask Codex to open it.

**Prompt 3** adds one round of independent criticism. Subagents are extra copies of the agent that Codex starts to review the work.

```text
Spawn two subagents as independent skeptical reviewers, one focused on
methods and one on marketing, as described in SETUP.md. Each should return
specific findings with a proposed fix for each. Verify every finding yourself,
tell me which ones you accept or reject and why, then apply the accepted fixes.
Then stop. Do not start the scored review loop until I ask.
```

*You should see* a list of findings, each marked accepted or rejected with a reason, and updated files.

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
5. Wait for the download to finish. The file is about 790 MB. If Microsoft Edge says the file isn't commonly downloaded, point to it in the downloads list, click the three dots (**...**), choose **Keep**, then **Keep anyway**.
6. Press Windows+E and click **Downloads** in the left panel. Right-click `user_daily_post_counts.parquet` and choose **Cut** (the scissors icon on Windows 11).
7. Click the address bar, type the line below, and press Enter.

   ```text
   %USERPROFILE%\agentic-ai\reddit-base\data
   ```

8. Press Control+V. The file moves into the `data` folder.

**Check.** In File Explorer, right-click the file and choose **Properties**. The name must be `user_daily_post_counts` with type "PARQUET File" (File Explorer may hide the `.parquet` ending), and the size about 755 MB (792,034,341 bytes). If your browser renamed it (for example, with a `(1)` at the end), rename it.

### LaTeX

You do not need to install LaTeX yourself. The first Reddit prompt asks the agent to add Tectonic, a small LaTeX program, inside the exercise folder. The first time the paper compiles, Tectonic downloads the pieces it needs, so say yes when Codex asks.

If you want LaTeX for your own papers later, you can install [MiKTeX](https://miktex.org/download). It is not needed for these exercises.

### Send the prompts one at a time

Open the Reddit folder in Codex the same way as in step 6:

1. Click **Add new project** (or press Control+O), click the address bar, type the line below, press Enter, and click **Select Folder**.

   ```text
   %USERPROFILE%\agentic-ai\reddit-base
   ```

2. Set the permission control to **Ask for approval**.
3. Choose the same model as in step 6 (**6 Sol Medium**, or **Luna High** on Free or Go).
4. Check that the chat runs **Local**.
5. Check your usage.
6. Send the first message from step 6. This time the path should end in `reddit-base`, and the `data` folder should contain `user_daily_post_counts.parquet`.

Then send these prompts one at a time.

**Prompt 1:**

```text
Read SETUP.md and transcript.txt. They describe my assignment. Before you run
anything, ask me about any choice that would change the result, then give me a
step-by-step plan. Use Pixi to create the environment in this folder, and add
tectonic from conda-forge to that environment to compile the LaTeX paper. If
Git is installed, set up a Git repository in this folder and commit the
unchanged starter files first. The data file has about 283 million rows, so
prototype on a small sample, and read the full file in pieces (for example,
Parquet row groups) so it fits in a laptop's memory. Do not start the review
loop yet.
```

*You should see* numbered questions and a plan. As in the customer exercise, answer the Crossref email question the same way. Check the plan as in step 6, and also check that it mentions `data/user_daily_post_counts.parquet` and a sample run before the full run.

**Prompt 2** runs the analysis on a sample only:

```text
I checked the plan. Build the environment and run the analysis on a small
sample only. Then tell me how much memory and disk space the full run will
need, how long you expect it to take on this computer, and whether this
computer has enough. Wait for me before you run the full file.
```

*You should see* results from the sample and an estimate for the full run. If Codex says this computer does not have enough memory or disk space, ask it what to change before you continue.

**Prompt 3** runs the full file and writes the paper:

```text
Go ahead with the full file. Write the first complete version of the LaTeX
paper and compile it to PDF with tectonic. When you finish, summarize what you
found, list the exact name and location of every file you created, and open
the PDF. Then stop. Do not start reviewer subagents or the review loop until
I ask.
```

*You should see* a summary of the findings, a list of files, and the paper open as a PDF. In the completed example, the first full analysis and paper took about 9 minutes on a fast Linux workstation with the larger Astra model. It has not been timed on a laptop, and a laptop will likely take longer.

**Prompt 4:**

```text
Spawn two subagents as independent skeptical reviewers of the paper, with the
different perspectives described in SETUP.md. Each should return specific
findings with a proposed fix for each. Verify every finding yourself, tell me
which ones you accept or reject and why, then apply the accepted fixes and
recompile the paper. Then stop. Do not start the scored review loop until I
ask.
```

*You should see* a list of findings, each marked accepted or rejected with a reason, and an updated PDF.

**Prompt 5 (optional):**

```text
Run the scored review loop described in SETUP.md, with three independent
reviewer subagents per round and the scoring and stopping rules it gives.
Finish with the process report.
```

*You should see* several rounds of scores and a process report that records them.

### Understand the result

Open the PDF and ask about anything unclear. For example:

- "Which result in the paper would change most if the definition of a bot changed? Show me."
- "Rebuild the main figure step by step and explain each step."

Your paper does not need to match `reddit/paper/main.pdf` in the download.

## What to try next

- Ask for a different number of customer groups, and ask the agent to compare the two results.
- Run the customer exercise again with Luna, in a separate folder. In `agentic-ai`, create a folder (Windows 11: **New**, then **Folder**) named `luna`. Copy `customer-segmentation-base` from the download into `luna`, as in step 1. In Codex, open the `customer-segmentation-base` folder inside `luna` as in step 6, choose **Luna High**, and send prompts 1 and 2. Compare the two folders' results and the usage each run took. If File Explorer ever asks whether to replace files, choose **Skip these files**, because replacing overwrites your finished work.
- Try a dataset of your own. If it is sensitive, ask the agent to build and test the analysis on made-up data with the same columns, then run the finished analysis on the real data yourself.

## Troubleshooting

| Problem | What to do |
|---|---|
| `codex` or `pixi` "is not recognized as the name of a cmdlet" | Close PowerShell and open it again as in step 2. Installers change settings that only new windows read. If it still fails, run the install command again (for Pixi, you can use the alternative command at the end of step 4), then open a new window. If it fails after that, restart the computer and try once more before asking for help. |
| "running scripts is disabled on this system" | Run the command under "If scripts are disabled" below this table. |
| `winget` is not recognized | Install ChatGPT with the download link in step 3, Pixi with the install command in step 4, and Git from [git-scm.com](https://git-scm.com/downloads/win). |
| Your university blocks Microsoft Store installs | Ask your IT help desk to install the ChatGPT desktop app, or use a personal computer. |
| The agent says Pixi or Git is not installed | Quit the ChatGPT app completely (see step 4) and open it again. If it still says Pixi is missing, send: "Pixi is installed at `$env:USERPROFILE\.pixi\bin\pixi.exe`. Use that full path for every pixi command." |
| Git cannot be installed | Skip it. The exercises work without Git, and Codex will say that Git is missing. |
| Codex asks for approval before running a command | See "When Codex asks permission" in step 6. |
| Codex asks before every single file change | You chose read-only. In the app, set the permission control to **Ask for approval**. In PowerShell, type `/permissions` and choose **Ask for approval** (older versions call it **Auto**). |
| Codex says its sandbox setup failed | You declined, or could not approve, the Windows administrator box. If Codex still runs commands with its weaker sandbox, continue. If commands fail, ask your IT help desk or use a personal computer. Do not switch to **Full access**. |
| Files are locked, or an install fails partway | Check that your folder is `C:\Users\name\agentic-ai` and not inside OneDrive, Desktop, or Documents. |
| A usage limit message appears | Wait for the limit to reset. You do not need to buy credits. Then continue as in the next row. |
| The computer went to sleep, or you closed Codex | In the app, click the conversation in the sidebar and send "Continue where you left off." In PowerShell, run `codex resume` from the exercise folder. |
| The agent seems stuck | Click the stop button in the app, or press Escape in PowerShell. Then describe what should happen next. |
| You cannot find a file the agent made | Ask Codex, "Where is the file you just created? Open its folder in File Explorer." |
| Codex says it cannot find `SETUP.md`, or mentions `customer-segmentation` or `reddit` without `-base` | You opened the wrong folder. Start a new chat and open `agentic-ai/customer-segmentation-base` (or `reddit-base`) as in step 6. |
| Codex says the Reddit `data` folder is empty | Repeat "Get the data file" in step 7, then check the file's name and size. |
| The model named in step 6 is not in the list | Click **Advanced** in the model control and pick the newest **Sol** model at **Medium**. If only GPT-5.6 Sol is offered, use it. |
| You want to start an exercise over | Delete the folder in `agentic-ai` and copy a fresh one from the download, as in step 1. For the Reddit exercise, first move `user_daily_post_counts.parquet` out of `reddit-base/data` into `agentic-ai`, and move it back into the new `data` folder afterward. |

### If scripts are disabled

If PowerShell says "running scripts is disabled on this system", paste this into PowerShell, press Enter, type `Y`, and press Enter again. Then try the command that failed.

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

This lets PowerShell run scripts for your user account only. If Windows says a policy overrides the setting, your computer is managed by your university, so ask your IT help desk or use a personal computer.
