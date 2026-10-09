---
name: research-deck
description: "Builds or updates a research talk (e.g., a 15-minute conference talk) from a research project's results, as a self-contained HTML slide deck with speaker notes, a light and dark theme, a PDF export, and figures and numbers drawn from the project's exported outputs. Before planning, it asks the user about the talk (length, audience, venue, byline). With no deck in the project it plans the talk arc (motivation, gap, research questions, results, brief limitations and next steps), confirms the plan with the user, and builds it; with an existing deck it checks which results moved since the deck's last snapshot and proposes only the slide changes they warrant. Offers an optional blind review round in which fresh reviewers read the rendered slides as first-time attendees and return findings with fixes. Use when the user asks for a conference talk, research presentation, results deck, or talk slides for a project, or asks whether a project's deck is current after new results. Not for workshops, lectures, general-purpose decks, or PowerPoint files."
---

# research-deck

A research talk has one job: a listener who has never seen the work leaves knowing why the problem
matters, what was asked, and what was found. Everything in this skill serves that. The slides show,
the speaker says, and the paper carries the caveats.

The skill folder holds everything it needs. `template/` is the slide engine (an editable
`src/deck.html`, a `build.py` that inlines fonts, figures, and data into one offline HTML file, and a
`render.py` that screenshots every slide and exports the PDF). `scripts/` holds the helpers named
below. In the steps below, `<skill>` is the folder this file sits in. Run every script with the
project's Python environment (e.g., `pixi run python <skill>/scripts/outline.py ...`). Every script
except `render.py` uses only the standard library; `render.py` needs the `playwright` package and a
Chromium browser, so add them to the project environment if they are missing.

## Mode

Look for a deck folder: the one the user names, otherwise any `slides/*/sources.json` in the project.

| Found | Mode |
|---|---|
| no deck | **Create** at `slides/conference/` (or the user's path) |
| one deck | **Update** that deck |
| several decks | ask which one, newest first |

## Rules that hold in both modes

- **Ask in batches.** When the agent tool has a structured question feature, use it. Put every open
  question in one round, give a recommended answer for each with the reason, and wait for the
  answers before acting on them.
- **Draw only on exported outputs.** Numbers come from the project's numbers file (cited on the slide
  as `<span data-n="macro">value</span>`), figures from its exported figures folder, and claims from
  its documents. Obey the project's own instructions on disclosure (e.g., a rule on suppressing small
  cells). Never read raw data to make a slide, and never invent a result, citation, or figure
  meaning. Mark a gap with `TODO:` in the notes and report it.
- **Text only where it earns its place.** A slide carries a claim title and a visual. Body text appears
  only to cue the speaker or to show a fact the audience must see. `outline.py` measures this.
- **No caveats mid-talk.** Limitations get one slide near the end (at most three). Detail a questioner
  may want goes in backup slides after the closing slide, which take no time.
- **Ask when inclusion is a judgment.** When it is unclear whether a result, exploratory analysis, or
  prior study belongs in the time slot, ask with a recommendation rather than deciding silently.
- **Never commit.** Report the files; the user commits.

## Create

1. **Ask about the talk.** Before reading deeply, ask in one round for whatever the user has not
   already said:
   - the speaking time, and whether questions come out of that time;
   - the audience (a specialist session, a general academic audience, practitioners) and how much
     method detail they expect;
   - the venue and date;
   - the speaker's name and affiliation for the byline;
   - any required elements (e.g., a funder acknowledgment or a sponsor's template).

   Recommend 15 minutes with questions separate if the user has no slot yet.
2. **Read the project.** Read its instructions file for agents (if it has one), its plan or
   manuscript, results documents, the numbers file, and the figure list. Read `references/arc.md`
   and `references/authoring.md` now.
3. **Plan the talk.** Draft the slide plan in the form `references/arc.md` gives (one row per slide
   with part, claim title, visual, source, and time), sized to the speaking time. Show it, then ask
   in one round for approval plus every open inclusion question. Write no slides until the plan is
   approved.
4. **Scaffold.** Run `<skill>/scripts/scaffold.py slides/conference`, then edit `sources.json` so its
   numbers file, figures folder, and watch patterns match this project. If the project has no numbers
   file, say so and offer to add one (a LaTeX file of `\newcommand{\name}{value}` lines written by the
   analysis code), since a deck whose numbers are typed by hand cannot be checked against the results.
5. **Write the slides** in `src/deck.html`, using the layout catalog in `references/authoring.md`.
   Delete the template's example slides. Put the byline from step 1 on the title and closing slides.
   Every slide gets `data-time`, `data-title`, and full-sentence notes.
6. **Sync, build, render.** From the project root run `<skill>/scripts/sources.py sync <deck>`. Then,
   from the deck folder, run `build.py` and `render.py <temp folder>/render --pdf`. A non-zero exit
   from either is a defect to fix, not a warning.
7. **Check it yourself.** Run `<skill>/scripts/outline.py <deck>` and fix every TEXT-HEAVY slide or
   say why it stays. Look at every rendered PNG in both themes against the review list in
   `references/authoring.md`. Sweep slide text and notes for filler and for sentence fragments in the
   notes.
8. **Offer the review round** (below). After the last change, run `sources.py snapshot <deck>`.

## Update

Read `references/update.md` first. In short, run `sources.py check <deck>`. Exit 0 means the deck is
current, so say so and stop. Exit 3 means something changed: sort each change into one of three kinds,
i.e., a value refresh `sync` handles, a claim that changes, or a new or dropped result. Show the update
plan and ask, apply it, then continue from step 6 of Create. Edit only the slides the changes touch,
since the user may have edited the rest by hand.

## Review round

After a build that passes your own check, ask whether to run the review round, recommending it for a
new deck or after claim-level changes. If yes, follow `references/review-round.md`. In short, render,
freeze, and give one or two fresh reviewers (with no access to this conversation or the project) the
slide images and the brief in `assets/reviewer-brief.md`. Edit nothing while they run. Verify every
finding, show the accepted and rejected list, apply what the user approves, rebuild, re-render, and
ask whether to run a second round. Never run a third round unprompted.

## Final response

Report the deck folder, the built HTML and PDF, the slide count and last timing target against the
speaking time, and the TEXT-HEAVY count. Say what the visual check covered and what the review round
changed (or that it was skipped). List any `TODO:` gaps and any slide whose claim changed in an
update. Name what was not checked, e.g., the speaker view, which the render does not open.

## Resources

- `template/` is the slide engine that `scaffold.py` copies. `template/fonts/` holds Liberation Serif
  and JetBrains Mono subsets with their open font licenses.
- `scripts/scaffold.py` copies the template and writes `sources.json`.
- `scripts/sources.py` has three commands (`check`, `sync`, `snapshot`) that tie slides to the
  project's numbers and figures.
- `scripts/outline.py` prints the deck as text with per-slide visible word counts.
- `references/arc.md` covers the talk arc, slide budget, visual rules, and plan format.
- `references/authoring.md` covers the layout catalog, builds, presenting keys, and the visual review
  list.
- `references/update.md` covers the update procedure and how to classify changes.
- `references/review-round.md` covers dispatch, adjudication, and applying fixes.
- `assets/reviewer-brief.md` is the brief each reviewer receives.
