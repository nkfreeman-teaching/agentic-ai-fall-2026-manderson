# Skills

A skill is a folder of instructions (and sometimes scripts) that an agent loads when a task calls for it. Each folder here has a `SKILL.md` file whose header gives the skill's name and a description of when to use it, which is the format that most agent tools with skill support read (e.g., Codex and Claude Code). The two skills here are written for any such tool and name no provider.

- `research-deck/` builds a research talk as a self-contained HTML slide deck with speaker notes, a light and dark theme, and a PDF export. It asks about the talk (length, audience, venue, byline) before planning, confirms a slide plan before writing slides, ties every number on a slide to the project's exported results, and offers a blind review in which fresh reviewers read the rendered slides as first-time attendees. Rendering the slides needs the `playwright` Python package and a Chromium browser.
- `resume-prompt/` prints a verified handoff prompt that a fresh agent session can start from, which is a way to manage a context window that has grown long.

## Installing them

Each tool keeps user-level skills in its own folder, so the simplest route is to ask the agent to install them. From this folder, a prompt along the following lines works:

> Here are two skills in `skills/`. Read both, then help me install them as user-level skills for this tool so they are available in every project. Adapt anything that does not fit my setup (e.g., how Python environments are run here), and tell me what you changed.

The skills are starting points, so edit them to fit the work (e.g., a different default talk length, a color scheme, or extra sections in the handoff prompt).
