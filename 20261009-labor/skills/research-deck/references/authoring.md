# Authoring reference

## The stage

Every slide is a `<section class="slide">` laid out at 1920×1080 px and scaled to the window, so
sizes in the CSS are real pixels on a 1080p screen. The default padding is 92 px top, 132 px sides,
and 120 px bottom, and the slide number sits in the bottom-right corner. Keep content inside that
box; the render script flags anything that leaves the slide.

## Layout catalog

Each layout has one example slide in `template/src/deck.html`. Copy the example, then change it.

| Layout | Markup | Use for |
|---|---|---|
| Title | `section.slide.s-title` with `.lockup`, `.left h1 em`, `.sub`, `.byline` | The opening slide. Put an optional diagram in `svg.art` on the right. |
| Cards | `.cards` (three columns), `.cards.two`, `.cards.tall`, each `.card.accent.b-<color>` with `.label`, `h3`, `p`, `.foot` | Two or three parallel ideas. |
| Comparison | `.versus` with two `.pane.b-<color>` (`.bar`, `.body`) and a `.takeaway` | Before and after, A versus B. |
| Figure | `.figure` with `.frame` (an `img` or inline SVG) and `.read` | One exhibit and how to read it. |
| Stats | `.stats` with `.stat.b-<color>` (`.num`, `.what`) | Two to four headline numbers. |
| Table | `table.tbl`, numeric cells `td.n`, highlighted row `tr.hl` | A small table, one per slide. |
| Tick list | `ul.ticks.b-<color>`, with the lead term in `<b>` | Lists of three to five items. |
| Code | `pre.code` with spans `.k` `.s` `.c` `.h` `.d` | Short commands or config, 12 lines at most. |
| Definitions | `dl.gloss` with `.g.b-<color>` (`dt`, `dd`) | A glossary to leave up during questions. |
| Section | `section.slide.s-section` with `.n`, `h2`, `.lede` | A divider in a talk longer than about 20 minutes. |
| Closing | `section.slide.s-close` with `.lockup`, `h1`, `.byline` | "Questions" or a closing line. |

Every content slide opens with `.kicker` ("02 · Results") and an `h2`. Use `h2.long` for a title
that runs past one line at 76 px. `.lede`, `.small`, `.source` (a bottom-left source line), and
`.chip.b-<color>` cover the remaining text needs.

**Color carries meaning.** The categorical tokens are `amber`, `indigo`, `teal`, `orange`,
`violet`, `green`, `blue`, and `crimson`; `.t-<color>` colors text and `.b-<color>` sets `--c` for
a component. Assign one color per concept and keep it across the deck (e.g., one color per research
question, reused on every slide that answers it). The deck's accent is `--brand`, set in the tokens at
the top of the style block, and `.b-brand` applies it.

**Diagrams are inline SVG** drawn with the tokens (`fill="var(--c-teal)"`), so they follow the
theme. Charts that need data go in `data/<name>.json`, which the build inlines as a constant through
a DATA marker (see `build.py`), and are drawn in the script's deck-specific section. Give a clickable
chart the class `interactive` so a click on it does not advance the slide.

## Writing the slides

- **Titles state the claim.** "Matching removes most of the age gap", not "Results". The title is
  the sentence the audience should remember.
- **One job per slide.** A slide motivates, defines, compares, shows a result, explains a method, or
  closes a section. Split a slide that does two.
- **Short on the slide, full in the notes.** Slide text is phrases and short sentences; the notes
  carry what the speaker says, in whole sentences. Notes open with the timing target and the click
  count ("**Target 2:30 to 3:45.** Two clicks."), then one item per click.
- **Never invent** results, citations, affiliations, or figure meanings. Mark a gap in the notes with
  `TODO:` and report it.
- **Define terms at first use**, on the slide or in the notes, and keep the glossary slide in sync.

## Builds and timing

A `.f` element appears on the next click; `data-f="n"` puts several elements in step n. Builds cost
time, and a deck with many reveals runs past its slot, so reveal only where the order of ideas
matters (a comparison, a sequence), and leave reference slides static. Keep `data-time` targets cumulative, and check that the last target
leaves room for questions.

## Presenting

Keys: arrows or space to advance, `S` opens the speaker view (current slide, next build, notes,
timer, target time), `T` toggles the theme, `F` full screen, `B` black screen, a number plus `Enter`
jumps to a slide, and `?` shows the help. The speaker view is a pop-up, so the browser must allow
pop-ups for the file. The deck opens in the light theme; projectors in bright rooms favor it.

## PDF export

`render.py --pdf` prints the light theme with every build shown, one slide per page at 1920×1080.
Chrome's PDF output drops some effects, so avoid gradient text (`background-clip: text`), which
prints as a filled rectangle. Use a solid `--brand` color instead. Animations
are switched off in print.

## Visual review list

Read every PNG in both themes. Check each slide for:

1. Text outside the padded box, or colliding with the slide number or the source line.
2. Overlapping elements, including SVG labels that sit on lines, points, or other labels.
3. Titles that wrap to three lines, or a lone word on a second line.
4. Cards or panes of visibly different text length in a row meant to be parallel.
5. Figures that are too small to read at projection distance, stretched, or cropped. Figure text
   should be at least about 18 px at the 1920 stage.
6. Contrast in the dark theme, especially tinted text on tinted panels and figure images with white
   backgrounds (the `.frame` keeps a white backing for them).
7. Colors that do not match the concept they stood for on earlier slides.
8. Anything that only appears after a build and is covered or misplaced in the all-builds render.

The serif subset covers Latin, Greek, the basic arrows (←, →, ↔), and common math operators (≤, ≥, ≈,
≠, ∑, √, ∞, −). Check marks (✓) and other symbols outside it fall back to a system face, which may not match the weight or baseline. Check any
slide that uses such symbols, and draw heavy notation as inline SVG or an image.
