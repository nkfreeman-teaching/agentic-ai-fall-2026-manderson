# The talk arc

## Contents

- The arc and its time budget
- What each part must do
- Showing instead of telling
- The plan format
- Backup slides

## The arc and its time budget

Plan to the speaking time the user gave at intake. A 15-minute research talk has 11 to 13 timed
slides. Scale the minutes in proportion for other lengths, keeping roughly one content slide per 1 to
1.5 minutes. The budget assumes questions are separate; if the slot includes them, plan to the slot
minus the question time the user names.

| Part | Slides | Minutes (15-min talk) | Required |
|---|---|---|---|
| Title | 1 | 0.5 | yes |
| Motivation: the problem and why it matters | 1 to 2 | 2.5 | yes |
| Gap: what is known and what is missing | 0 to 1 | 1 | only if the contribution depends on it |
| Research questions | 1 | 1 | yes |
| Approach: data and design, as one picture | 1 to 2 | 2 | yes |
| Results: one headline finding per slide | 3 to 4 | 6 | yes |
| What it means | 0 to 1 | 1 | if the implication is not already the last result's title |
| Limitations and next steps | 1 | 1 | yes, brief |
| Close | 1 | 0 | yes |

Results get the largest share. If the plan runs long, cut the gap slide, the second motivation slide,
or a method detail before cutting a result.

## What each part must do

**Title.** The title states the topic in plain words, and the subtitle (the italic line) can carry the
finding. The byline carries the name, affiliation, venue, and date the user gave at intake.

**Motivation.** It answers why anyone outside the subfield should care. Open on the phenomenon (a
timeline, a map, a striking exported number shown large), not on the literature. The listener should
be able to repeat the problem in one sentence by the end of this part.

**Gap.** It is one slide at most, and only when the contribution is defined by what earlier work did
not do. Show at most three prior studies, each as one line naming what it established and the specific
thing it did not do. The gap is the last line, stated as the thing this work does. Cite as "Author
(year)" on the slide and give the full reference in the notes. Use only citations the project's own
documents already carry.

**Research questions.** Show one to three numbered questions, each in one line. Give each question a
categorical color and keep that color for every later slide that answers it, so the listener can track
which result answers which question. The RQ slide is one of the two places a short list is allowed.

**Approach.** Show the design as a diagram, e.g., a treatment timeline, a unit-and-comparison schematic,
or a data pipeline with counts at each stage. Name the method in the title or a label and explain it in
the notes. Estimator detail, robustness specifications, and data-cleaning rules belong in backup slides.

**Results.** One finding per slide. The title is the finding as a sentence ("Posting about the treated board
rose about 40 percent relative to its comparison boards"), the exhibit is the evidence, and the RQ color ties it back.
Cite every number through `data-n`. When an exhibit carries more than the finding needs, crop the
story, not the figure: highlight the relevant series or annotate the one number, and leave the full
exhibit to a backup slide. A null or failed result is still a result; state it plainly with its bound
(e.g., the effect size the design could have detected). The title carries the finding's certainty as the
project reports it: an estimate whose interval includes zero is not titled as a rise, and a
prespecified gate that failed is not titled as a finding. A result slide answers its research question directly. A related measure that
only supports the answer (e.g., a share of forum newcomers when the question is who drove a rise)
belongs in the notes or a backup slide, because first-time viewers miss an answer that sits on a
backup slide while the main slide shows only the supporting measure.

**What it means.** One slide for the implication for practice, policy, or the field, if the last result
title does not already say it. A short recap of the answers, one line per research question in its
color, works well here. Never draw arrows between findings unless the study tests the link, since an
arrow from another paper's result to this one reads as a causal claim.

**Limitations and next steps.** One slide with at most three limitations and at most three next steps,
each one line. Pick the limitations a careful listener would raise, not every caveat in the plan. The
second short list allowed in the deck is here.

**Close.** A closing line or "Questions", the contact line, and nothing else.

## Showing instead of telling

The speaker should never have to read the slide aloud. Test every slide this way: if the visual were
removed, would the speaker lose a cue or the audience lose a fact? Keep the text that passes and cut
the rest.

- **Cited numbers live in HTML text.** A `data-n` span inside an SVG `<text>` element does not work, so
put a cited number in an HTML element over or beside the diagram. Geometry that mirrors a number
(a bar width, a segment's flex value) cannot follow the macro; mark it with an HTML comment so an
update resets it by hand.
- **Text budget.** At most 30 visible words per content slide, excluding the title, kicker, figure
  labels, and the slide number. `outline.py` counts this and marks TEXT-HEAVY slides. Fix each one, or
  name the slide and the reason it stays in the final response.
- **Prefer, in order:** an exported figure; a simple inline SVG diagram drawn with the theme tokens;
  stat tiles of one to three exported numbers; a small table (at most five rows); text.
- **Figures at projection distance.** Paper figures often use 8 to 10 pt labels, which are too small on
  a projector. If an exported figure's labels would fall below about 18 px at the 1920 stage, propose
  regenerating a presentation variant through the project's own exhibit script and export path. Ask
  first, because that changes the project, not the deck.
- **Builds are rare.** Reveal in steps only where order carries meaning (a timeline, a before and
  after). Every build costs time against a 15-minute slot.
- **Notes carry the talk.** Notes open with the timing target and click count ("**Target 2:30 to
  3:45.** One click."), then the words the speaker will say, in whole sentences. Definitions, the
  method's name and logic, and the caveat a questioner may raise all go here.

## The plan format

Show the plan as a table before writing slides, then ask for approval and the open inclusion questions
in the same round of questions.

| # | Part | Claim title | Visual | Source | Ends at |
|---|---|---|---|---|---|
| 4 | RQ | Did the platform shock move activity toward the treated board? | Two numbered questions, colored | plan Section 1 | 4:00 |
| 7 | Result (RQ1) | The treated board rose about 40 percent against its synthetic control, within noise | `fig_gap_path.png`, post-period shaded | `\effectPct`, `\effectCIlo`, plan 6.1 | 8:30 |

Below the table, list what the plan leaves out and why (e.g., "Sensitivity grid: backup slide 15, since
the headline result does not depend on it"). The user is deciding on the omissions as much as on the
inclusions.

## Backup slides

Slides after the closing slide are backup for questions. Give them `data-time=""` and a kicker of
"Backup". They hold the full exhibits, robustness checks, and method detail the timed slides left out.
They do not count toward the slide budget or the text budget, but they still follow the citation rules.
