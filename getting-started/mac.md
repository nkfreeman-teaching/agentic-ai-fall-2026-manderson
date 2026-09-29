# Getting started on a Mac

This guide takes you from a Mac with nothing installed to running the two workshop exercises with Codex, OpenAI's coding agent. You do not need any programming experience, because the agent writes and runs the code. On Windows, use the [Windows guide](windows.md) instead.

The guide has seven steps:

1. Download the workshop materials and set up a working folder.
2. Open the Terminal.
3. Install Codex.
4. Install Pixi.
5. Install Git.
6. Run the customer segmentation exercise.
7. Run the Reddit exercise.

If you missed the workshop, the [recording](https://alabama.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=8d3f444c-8b6a-490b-9738-b4d00129a3a7) and the [edited transcript](../sessions/2026-09-25-transcript.md) show the download, Pixi, and a live Codex run on the customer data (from 00:23:17), and explain both exercises (from 00:45:20). The demo used the Desktop and a shorter prompt, so follow this guide's folders and prompts instead.

## Before you start

Check each item before you install anything.

- **macOS 14 (Sonoma) or newer.** The ChatGPT desktop app needs it. To check, open the Apple menu (top-left corner of the screen) and choose **About This Mac**. If the macOS number is lower than 14, open **System Settings**, then **General**, then **Software Update**. If no update to 14 or later is offered, this Mac cannot run the app, so use another computer. Also note whether the **Chip** or **Processor** line says Apple or Intel, because step 3 needs it.
- **At least 10 GB of free disk space.** To check, open the Apple menu, choose **System Settings**, then **General**, then **Storage**.
- **Memory.** Note how much your Mac has (Apple menu, **About This Mac**, then the **Memory** line). The customer exercise is small. The Reddit exercise has only been run on a workstation, so on a laptop with 8 GB, read the memory estimate Codex gives after Reddit prompt 2 carefully before you run the full file.
- **Your Mac login password.** Some installs ask for it. On a Mac managed by your university, installs may be blocked. If they are, ask your IT help desk or use a personal computer. Do not try to work around a university security setting.
- **A ChatGPT account.** The Plus plan ($20 a month) is the plan these exercises were built for. Eligible U.S. students can get four free months through OpenAI's Back to School offer by [claiming it](https://chatgpt.com/students/2026/) before October 31, 2026, and the [offer terms](https://help.openai.com/en/articles/20001493-chatgpt-back-to-school-offer-for-students) give the details. Keep these points in mind:
  - Claim it while signed in to the ChatGPT account you will use for Codex.
  - The offer does not apply to a Plus subscription billed through Apple or Google.
  - It asks for a payment method and renews at $20 a month unless you cancel, so put a reminder in your calendar now.
  - If you cancel early, the unused free months are lost.
- **If you are on the Free or Go plan,** Codex works only in the desktop app, with the smaller GPT-6 Luna model, and OpenAI is still rolling out that access. After you sign in (step 3), check that the app offers **Codex** before you install anything else. If it does not, wait for access or use a Plus account. Free and Go access is meant for quick tasks. Start with customer prompts 1 and 2, and stop when Codex reports a limit. The review prompts and the Reddit exercise may not fit, so check your allowance before you download the Reddit file or start a review prompt.
- **The Reddit data file.** The Reddit exercise needs a separate download of about 790 MB (step 7). You can do the customer exercise first.
- **Time and power.** Setup involves several downloads, and the agent works for many minutes after each prompt. Nobody has timed a full setup or exercise on a laptop yet, so do not start right before a deadline. The work pauses when the Mac sleeps, so keep it plugged in with the lid open (step 3 also turns on a setting that keeps it awake).

## 1. Download the materials and set up a working folder

You will copy two starter folders, one per exercise, into a new folder named `agentic-ai` in your home folder.

1. Open the [workshop repository](https://github.com/nkfreeman-teaching/agentic-ai-fall-2026-manderson) in your web browser.
2. Click the green **Code** button, then click **Download ZIP**.
3. Open Finder and press Option+Command+L to open your Downloads folder.
4. Look for a folder named `agentic-ai-fall-2026-manderson-main`. Safari often unzips downloads for you. If you see only a file named `agentic-ai-fall-2026-manderson-main.zip`, double-click it to unzip it.
5. In Finder, press Shift+Command+H to open your home folder. It has your user name and a house icon.
6. Choose **File**, then **New Folder**. Name the new folder `agentic-ai` and press Return.
7. Go back to Downloads and open the `agentic-ai-fall-2026-manderson-main` folder.
8. Click `customer-segmentation-base`, then hold Command and click `reddit-base`, so both are selected. Press Command+C to copy them.
9. Open the `agentic-ai` folder in your home folder and press Command+V to paste.

**Check.** The `agentic-ai` folder now contains `customer-segmentation-base` and `reddit-base`. Open `customer-segmentation-base`. You should see `SETUP.md`, `transcript.txt`, and a `data` folder.

Two points about this setup:

- **Why the home folder.** Desktop and Documents are often synced to iCloud. The agent creates thousands of small files, and syncing them causes slowdowns and errors.
- **Why a copy.** If an attempt goes wrong, you can delete the copy and paste a fresh one. The copy also keeps the agent away from the completed examples in the download, so it cannot copy their answers.

## 2. Open the Terminal

The Terminal is a window where you type commands instead of clicking. You need it to install Pixi and to check that each install worked.

1. Press Command+Space, type `Terminal`, and press Return.
2. A window opens with a line ending in `%`. This line is the prompt.
3. To run a command, type or paste it after the prompt and press Return. Paste with Command+V, as usual.

Try it now. Type `cd ~/agentic-ai` and press Return, then type `ls` and press Return. You should see `customer-segmentation-base` and `reddit-base`.

These commands are all you need:

| Command | What it does |
|---|---|
| `pwd` | Shows which folder the Terminal is in |
| `ls` | Lists the files in that folder |
| `cd agentic-ai` | Moves into the folder named `agentic-ai` |
| `cd ..` | Moves up one folder |
| `cd ~` | Returns to your home folder (`~` is short for your home folder) |
| `open .` | Opens the current folder in Finder |

Three tips:

- Press Tab partway through a file or folder name, and the Terminal finishes it for you.
- Type `cd ` (with a space after it), then drag a folder from Finder into the Terminal window and press Return. The Terminal moves into that folder.
- Press Control+C to stop a command that is running.

## 3. Install Codex

Codex comes in two forms. **Use the desktop app** unless you already use the Terminal comfortably. The desktop app is easier to start with and has a button for speaking your prompts (on Plus, and speaking uses part of your Codex allowance). The workshop demo used the command-line version, which runs in the Terminal and needs the Plus plan.

**Desktop app (recommended).** The desktop app is called ChatGPT, and Codex is one mode inside it.

1. Go to OpenAI's [quickstart page](https://learn.chatgpt.com/docs/quickstart?setup=app). Under **Setup**, make sure **Desktop** is selected, then click the download button for macOS. If About This Mac said **Intel**, download the [Intel version](https://persistent.oaistatic.com/codex-app-prod/ChatGPT-latest-x64.dmg) instead.
2. The download is about 700 MB and may be named `Codex.dmg`. Open it in Downloads and drag the app icon into Applications.
3. Open ChatGPT from Applications. If macOS asks whether you are sure you want to open it, click **Open**. Then sign in with your ChatGPT account. If it asks you to choose a workspace, choose your personal account, the one where you claimed the student offer.
4. Choose **Codex** from the menu at the top of the sidebar, which switches between ChatGPT and Codex.
5. Open **Settings** (Command+Comma), choose **General**, and turn on **Prevent sleep while running**, so the agent keeps working while you step away.

**Command-line version (alternative, needs Plus).** Paste this into the Terminal and press Return:

```bash
curl -fsSL https://chatgpt.com/codex/install.sh | sh
```

If it asks "Start Codex now? [y/N]", type `n` and press Return. Then check the install:

1. Close the Terminal window, then press Command+N to open a new one. Installers change settings that only new windows read.
2. Type `codex --version` and press Return. You should see a version number.

If you already use Homebrew (a tool for installing Mac software), `brew install --cask codex` works too. The first time you run `codex`, choose **Sign in with ChatGPT** and finish signing in in your browser.

## 4. Install Pixi

Pixi creates a separate Python environment, i.e., a private set of Python tools, inside each exercise folder. The exercises ask the agent to use it, so you install it once and the agent does the rest.

1. Paste this into the Terminal and press Return:

   ```bash
   curl -fsSL https://pixi.sh/install.sh | sh
   ```

2. Close the Terminal window, then press Command+N to open a new one.
3. Type `pixi --version` and press Return. You should see a version number.
4. If the ChatGPT app was open during the install, quit it with Command+Q and open it again, so that it can find Pixi.

## 5. Install Git (recommended)

Git records every change to the files in a folder. With Git installed, Codex can show you exactly what it changed and undo a change. Codex works without Git, but it is easier to follow with it.

1. Type `git --version` in the Terminal and press Return.
2. If you see a version number, Git is already installed. Go to step 6.
3. If a box asks to install the command line developer tools, click **Install**, then **Agree**. Leave the box open until it says the software was installed, which can take a while.
4. Type `git --version` again. You should see a version number.

## 6. Run the customer segmentation exercise

The `customer-segmentation-base` folder has three things:

- `transcript.txt`, a dictated description of the assignment.
- `SETUP.md`, instructions written for the agent.
- `data`, eight data files in Parquet, a compact data format. Double-clicking them does nothing useful, and that is expected, because the agent reads them.

To read `transcript.txt` or `SETUP.md` yourself, right-click it and choose **Open With**, then **TextEdit**. To see a finished result before you start, go to the unzipped download in Downloads, open `customer-segmentation`, then `output`, then `full`, and double-click `segment_explorer.html`.

### Open the folder in Codex

**Desktop app.**

1. In Codex, click **Add new project** next to **Chats** in the sidebar (or press Command+O).
2. In the window that opens, press Shift+Command+G, type the line below, and press Return. Then click **Open**.

   ```text
   ~/agentic-ai/customer-segmentation-base
   ```

3. Find the permission control beneath the message box and choose **Ask for approval**.
4. Click the model control beneath the message box. It is called **Power** and shows a short list.
   - On Plus, choose **6 Sol Medium** (it may read **6.1 Sol Medium**). If neither is listed, click **Advanced**, pick the newest **Sol** model, and set the effort to **Medium**. If the only Sol model is **GPT-5.6 Sol** (this happened in the Windows app in September 2026), use it at **Medium**, and check your usage after each prompt, because it uses your allowance about twice as fast as GPT-6 Sol.
   - On Free or Go, choose **Luna High**, which is the Luna choice.
   - Avoid **Astra**, **Extra High**, **Max**, **Ultra**, and **Fast**. Astra allows about a third as many messages as Sol, Ultra starts extra subagents, and Fast uses your allowance 2.5 times as quickly.
5. Check that the chat runs on your computer. The control beneath the message box should say **Local** (or **Work in: This computer**), not **Worktree** or **Cloud**, because the data files exist only on your computer.

**Command-line version.**

1. In the Terminal, type `cd ~/agentic-ai/customer-segmentation-base` and press Return.
2. Type `codex` and press Return.
3. When Codex asks whether to trust the folder, choose the option that lets it work in this folder. If it starts in read-only mode anyway, type `/permissions` and choose **Ask for approval** (older versions call it **Auto**).
4. The model name appears at the top of the session. Type `/model` and choose GPT-6 Sol (or GPT-6.1 Sol, if listed) with medium effort. If neither is listed, choose GPT-5.6 Sol with medium effort.

### When Codex asks permission

In **Ask for approval** mode, Codex changes files inside the exercise folder on its own. It stops and asks before it uses the internet or touches anything outside the folder.

- **Say yes** when it asks to install packages with `pixi`, to download LaTeX packages, to search Crossref or the web, or to open a file in your browser. The exercises need these. If Codex offers to stop asking about the same kind of command, choosing that option is fine.
- **Say yes** when it asks to run `git` commands such as `git init`, `git add`, `git commit`, or `git config` (which records your name and email for this folder). Git keeps its records in a protected hidden folder, so Codex asks first.
- **Say yes** if it asks to download a test browser for Playwright, a tool that lets the agent open the explorer and click through it. The download is a few hundred MB and stays in your user folder.
- **Say no** if it asks to install a program for the whole computer, such as Homebrew, LibreOffice, or anything installed with `brew`. Reply, "Do not install software outside this folder. Use a Pixi package instead, or skip that check and tell me you skipped it."
- **Say no, and ask it why,** if a command would delete files outside the exercise folder, starts with `sudo`, or asks for your password.

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

*You should see* a summary of the customer groups the agent found, a list of files, and the explorer open in your browser. The DOCX report is a Word document, so double-click it in Finder to open it. If you do not have Word, your university's Microsoft 365 account, Pages, or Google Docs can open it. To open the folder in Finder, type `open .` in the Terminal from the exercise folder, or ask Codex to open it.

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

1. Check that `~/agentic-ai/reddit-base` exists. If it does not, copy `reddit-base` from the download as in step 1.
2. Open the [data file on Google Drive](https://drive.google.com/file/d/1SzuIzRBhRdKuvNmBKqvhI-WFv4lRfXBr/view?usp=sharing). You do not need to sign in.
3. Click the download button (a downward arrow, usually near the top right).
4. Google says it cannot scan the file for viruses because it is large. Click **Download anyway**.
5. Wait for the download to finish. The file is about 790 MB.
6. Click the Finder icon (the blue face) in the Dock, then press Option+Command+L to open Downloads.
7. Press Command+N to open a second Finder window. In it, press Shift+Command+H, then open `agentic-ai`, then `reddit-base`, then `data`.
8. Drag `user_daily_post_counts.parquet` from the Downloads window into the `data` window. Finder moves it.

**Check.** In Finder, click the file once and press Command+I. The name must be exactly `user_daily_post_counts.parquet`, and the size about 792 MB (Google Drive lists it as 755M, and both are right). If your browser renamed it (for example, with a `(1)` at the end), rename it.

### LaTeX

You do not need to install LaTeX yourself. The first Reddit prompt asks the agent to add Tectonic, a small LaTeX program, inside the exercise folder. The first time the paper compiles, Tectonic downloads the pieces it needs, so say yes when Codex asks.

If you want LaTeX for your own papers later, you can install [MacTeX](https://www.tug.org/mactex/), which is a download of about 6 GB. It is not needed for these exercises.

### Send the prompts one at a time

Open the Reddit folder in Codex the same way as in step 6:

1. Click **Add new project** (or press Command+O), press Shift+Command+G, type the line below, press Return, and click **Open**.

   ```text
   ~/agentic-ai/reddit-base
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
- Run the customer exercise again with Luna, in a separate folder. In `agentic-ai`, choose **File**, then **New Folder** named `luna`. Copy `customer-segmentation-base` from the download into `luna`, as in step 1. In Codex, open the `customer-segmentation-base` folder inside `luna` as in step 6, choose **Luna High**, and send prompts 1 and 2. Compare the two folders' results and the usage each run took. If Finder ever asks whether to replace a folder, click **Stop**, because replacing deletes your finished work.
- Try a dataset of your own. If it is sensitive, ask the agent to build and test the analysis on made-up data with the same columns, then run the finished analysis on the real data yourself.

## Troubleshooting

| Problem | What to do |
|---|---|
| `command not found: codex` or `command not found: pixi` | Close the Terminal window and press Command+N to open a new one. Installers change settings that only new windows read. If it still fails, run the install command again, then open a new window. If it fails after that, restart the Mac and try once more before asking for help. |
| The agent says Pixi is not installed | Quit the ChatGPT app with Command+Q and open it again. If it still says so, send: "Pixi is installed at ~/.pixi/bin/pixi. Use that full path for every pixi command." |
| Git cannot be installed | Skip it. The exercises work without Git, and Codex will say that Git is missing. |
| Codex asks for approval before running a command | See "When Codex asks permission" in step 6. |
| Codex asks before every single file change | You chose read-only. In the app, set the permission control to **Ask for approval**. In the Terminal, type `/permissions` and choose **Ask for approval** (older versions call it **Auto**). |
| An install asks for a password you do not have, or is blocked | Your Mac is probably managed by your university. Ask your IT help desk, or use a personal computer. |
| A usage limit message appears | Wait for the limit to reset. You do not need to buy credits. Then continue as in the next row. |
| The Mac went to sleep, or you closed Codex | In the app, click the conversation in the sidebar and send "Continue where you left off." In the Terminal, run `codex resume` from the exercise folder. |
| The agent seems stuck | Click the stop button in the app, or press Escape in the Terminal. Then describe what should happen next. |
| You cannot find a file the agent made | Ask Codex, "Where is the file you just created? Open its folder in Finder." |
| Codex says it cannot find `SETUP.md`, or mentions `customer-segmentation` or `reddit` without `-base` | You opened the wrong folder. Start a new chat and open `agentic-ai/customer-segmentation-base` (or `reddit-base`) as in step 6. |
| Codex says the Reddit `data` folder is empty | Repeat "Get the data file" in step 7, then check the file's name and size. |
| The model named in step 6 is not in the list | Click **Advanced** in the model control and pick the newest **Sol** model at **Medium**. If only GPT-5.6 Sol is offered, use it. |
| You want to start an exercise over | Delete the folder in `agentic-ai` and copy a fresh one from the download, as in step 1. For the Reddit exercise, first move `user_daily_post_counts.parquet` out of `reddit-base/data` into `agentic-ai`, and move it back into the new `data` folder afterward. |
