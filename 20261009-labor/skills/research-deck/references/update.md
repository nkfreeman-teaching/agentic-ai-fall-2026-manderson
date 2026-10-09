# Updating an existing deck

The deck folder holds `sources.json` (what the deck draws on) and `manifest.json` (the state of those
sources at the last snapshot). An update changes only what the project's changes warrant, because the
user may have edited slides by hand since the last build.

## 1. Check

From the project root, run `<skill>/scripts/sources.py check <deck>`, where `<skill>` is this skill's
folder.

| Exit | Meaning | Next |
|---|---|---|
| 0 | Nothing watched changed and every cited number and figure matches the project | Say the deck is current, give the snapshot date, and stop. Offer the review round only if the user asked for one. |
| 3 | Something changed | Classify the changes (step 2). |
| 1 | A slide cites a macro or figure the project no longer has | Treat each as a claim-level change (step 2). |

If `manifest.json` is missing, the deck was never snapshotted (e.g., it was built before this skill or
by hand). Compare the slides to the project directly, using the "out of date" lines and a read of the
deck, then snapshot after the update.

The check also lists commits since the snapshot. Read `git log -p <snapshot commit>..HEAD -- <watched
paths>` for watched documents (the plan, results notes, the manuscript) whose text changed, since a
hash change in a document says nothing about which claim moved.

## 2. Classify each change

| Kind | Example | Action |
|---|---|---|
| Value refresh | `\gateATT` moved from 0.371 to 0.379; a figure was regenerated with the same story | `sources.py sync` updates it. Re-read the slide to confirm its title still holds. |
| Claim change | An interval now includes zero; a rank or sign flipped; a gate passed that had failed, or the reverse; a figure now shows a different pattern | Rewrite the slide's title, notes, and any slide that leads into it. A claim change upstream (motivation, RQ) can change the arc. |
| New or dropped result | A new analysis stage, a new exported figure or macro family, a result the plan retired | Propose adding, moving, or cutting slides against the time budget in `arc.md`. A new result displaces something; say what. |
| No deck effect | A watched file changed but no slide draws on it and it adds no result | List it in one line and do nothing. |

Judge a value refresh by what the audience would take away, not by the size of the change. A 2 percent
shift that moves a p-value across 0.05, or an interval across zero, is a claim change.

## 3. Show the plan and ask

Show the update as a short table of slide, change, kind, and proposed edit. List the value refreshes as
one line with their count, and spell out each claim change and new result. Ask in one round for
approval, together with any inclusion questions that a new result raises. Recommend an option in
each.

## 4. Apply

Run `sources.py sync <deck>` for the value refreshes, reset any geometry marked as mirroring a changed
number, edit the approved slides in `src/deck.html`, and
leave every other slide byte-for-byte as it was. Then continue from step 6 of Create in `SKILL.md`
(build, render, self-check, review-round offer). Run `sources.py snapshot <deck>` only after the last
change of the session, so the manifest describes the deck as delivered.
