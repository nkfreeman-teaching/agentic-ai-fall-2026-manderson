# The review round

One or two reviewers each see the deck as a first-time attendee would and report whether the talk's
arc lands in its time slot. They work blind to each other and to this conversation, return a fix with
every finding, and change nothing. The main session verifies, the user approves, and only then does
anything change.

## Contents

- 1. Freeze
- 2. Write the intended takeaways
- 3. Dispatch the reviewers
- 4. Collect and adjudicate
- 5. Approve, apply, and offer a second round

## 1. Freeze

Build and render first, with exit 0 from both. Then copy the inputs into a round folder outside the
project (e.g., a temporary folder), `<temp>/deck-review/round-<n>/`:

- `light/slide-NN.png`, the audience view (light theme, every build shown);
- `outline.md`, from `outline.py <deck>` (titles, visible text, word counts, and notes);
- `brief.md`, from `assets/reviewer-brief.md` with its placeholders filled in (talk length, slide
  count, venue or audience, and the round folder path).

Edit nothing in the deck from here until every report is in. A reviewer who reads a slide that changed
mid-round reviewed a deck that no longer exists.

## 2. Write the intended takeaways

Before dispatch, write `<round folder>/intended.md`, which no reviewer sees. It holds the problem in
one sentence, why it matters in one sentence, each research question, and each headline finding with
its number and certainty. This is the answer key: the round's main test is whether each reviewer's
recall (Part A of the brief) matches it.

## 3. Dispatch the reviewers

A reviewer must start with no memory of the work. It gets the round folder and nothing else: no deck
source, no project files, no conversation history, and no intended takeaways. Two reviewers catch more
than one, and two reviewers built on different models catch more than two built on the same one,
since they share fewer blind spots. Use whatever the agent tool offers, in this order of preference:

1. **A fresh sub-agent**, if the tool can start one with a clean context. Give it this prompt: "You
   are a reviewer. Read `<round>/brief.md` and follow it exactly. View each PNG in `<round>/light/` in
   order before opening `outline.md`. Write nothing to disk; return your report as your final
   message. Do not ask questions; state any uncertainty in the report."
2. **A second agent tool run from the command line**, read-only, with every light PNG attached in
   slide order and the brief as the prompt. Run it in the background, send its output to a file in
   the round folder, and record its exit code. Note which model it used.
3. **A new session the user runs**, in this tool or another one, if neither of the above is
   available. Give the user the round folder path and the exact prompt from option 1, and wait for the
   pasted report.

Start every reviewer before reading any report, so none waits on another. If a reviewer cannot run
(a missing command, a failed login), tell the user and run the round with the remaining reviewer only
if the user agrees. Never write a report in a reviewer's place.

## 4. Collect and adjudicate

When every report is in (and any command-line reviewer exited 0):

1. **Score the recall.** Compare each reviewer's Part A answers with `intended.md`. A problem, research
   question, or finding that a reviewer missed or got wrong is a BLOCKER, whatever the reviewer rated it,
   because it is the failure the round exists to catch. Find the slide responsible.
2. **Verify every finding against the slides.** Open the PNG or the source the finding names. Mark each
   one confirmed, refuted (say why), or a matter of taste. A finding only one reviewer raised gets the
   same check as a shared one.
3. **Check every proposed fix against the deck's own rules** (`arc.md`): it must not push a slide over
   the text budget, add a mid-talk caveat, invent a number, or break the time budget. A fix that does
   any of these is rejected or rewritten, and the reason is recorded.
4. **Record disagreements, do not average them.** Where the reviewers rate the same issue differently,
   or one proposes a fix the other's report argues against, give both positions and the one you
   recommend.

## 5. Approve, apply, and offer a second round

Show the adjudicated list, most severe first: the slide, the finding, who raised it, the verdict, and
the fix to apply. Put the recall result first ("Both reviewers recovered the problem and both research
questions; the second reviewer missed the second finding, traced to slide 9's title"). Then ask which
fixes to apply, recommending the confirmed BLOCKER and MAJOR fixes.

Apply the approved fixes, then rebuild, re-render, rerun `outline.py`, and look at the changed slides
again as images. Ask whether to run a second round, recommending one only if a BLOCKER was fixed,
since the fix itself is then untested. A second round uses a fresh round folder and fresh reviewers who
have not seen the first round's reports. Never run a third round unprompted.
