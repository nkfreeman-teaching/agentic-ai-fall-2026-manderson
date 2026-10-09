---
name: resume-prompt
description: "Prints a self-contained handoff prompt in the reply, as one fenced block the user copies into a fresh agent session to pick up the current work, and saves nothing. Use whenever the user types /resume-prompt or asks for a resume prompt, handoff prompt, continuation prompt, a prompt for a new or fresh session, or a way to pick up where this session left off, and when a session is stopping with work genuinely unfinished. Do NOT use when the user hands over an existing resume prompt to continue from (read it and continue instead), or asks for a run log, status register, or progress document (those are files, and this skill never writes one)."
---

# resume-prompt

A long session fills the model's context window, and once the window is full the tool summarizes or
drops older material, sometimes without saying what it lost. Starting a fresh session with a short,
verified handoff is often better than continuing. The next session starts with no memory of this one.
The prompt is the only thing it gets, so it must let a capable reader who has never seen this work act
correctly on its first turn: know where to work, what binds it, what is done and verified, what is open
and whose call each open item is, and what this session learned the hard way.

## Output contract

- Print the prompt in the reply, inside one fenced code block, so it copies cleanly. Wrap lines at
  about 100 characters.
- Save nothing. Do not write the prompt to a file, the repository, or the tool's memory, since a saved
  handoff goes stale while it looks current. Write a file only if the user asks for one in this same
  request.
- Outside the block, add at most two sentences: anything the user must know before pasting (for
  example a job still running, or a record you found to be stale), and nothing else.

## Verify before writing

Every factual claim in the prompt is something this session confirmed, because the next session
will act on it without re-checking. Before drafting, look rather than recall:

- `git branch --show-current` and `git status --short` (summarize the uncommitted state; do not paste
  it).
- Running jobs: the process list filtered to the project (e.g., `ps -eo pid,etime,cmd`), with each
  job's log path.
- For each run you will report: its exit code and the check or assertion line from its log.
- The durable records this session wrote or edited (a progress file, a plan's review section): open
  them and point to the right section by its heading.

If a claim cannot be checked, leave it out or mark it unverified in the prompt. If a durable record
contradicts what the prompt will say, say so outside the block and offer to fix the record. Do not
fix it silently, since the user may want to look first.

## Structure

Use these sections in this order. Leave out a section that has nothing in it rather than writing
"none".

1. **Opening, no heading.** The absolute working directory and branch, an instruction to read the
   project's instructions file for agents first (if it has one), and the standing rulings that bind
   the work and that a fresh session could break: commit policy, which checks are deferred or
   required, folder rules, anything the user decided this session that is not yet written into the
   instructions file. Do not restate rules that file already carries, unless this session saw one
   broken or nearly broken.
2. **WHERE THINGS STAND.** First point to the durable record by path and section heading. Then give
   a short summary of what was done, each item with its exit code, check count, and log path,
   followed by what is uncommitted. Point to the record rather than repeating it; the summary is for
   orientation only.
3. **RUNNING NOW** (only if something is running). Process ID, log path, what completion looks like,
   how to check it without disturbing it, and what to do on success and on failure.
4. **OPEN ITEMS.** Numbered, in the order the user is likely to take them, with a note that the next
   session should ask which comes first. For each item, give what it is in ordinary words with the
   handle in parentheses, where it lives (`path:line`), its measured cost or "cost unknown", whose
   decision it is, and any proposed fix with the alternative considered. Separate decisions the user
   owes from mechanical work the session can do.
5. **NOTES FOR RUNNING THINGS.** Lessons from this session that the next one would otherwise learn
   again: commands that hang or fail, tool limits, tools that misbehaved and the workaround, patterns
   that worked (launch commands, ways to check progress).
6. **Scratch locations.** Absolute paths of anything outside the repository the next session needs,
   such as probes, baselines, or extracted data, with one line on what each holds.

## Writing rules

- Self-contained. Every handle (a finding number, a step name) gets a plain-words gloss on first use,
  since the reader has not seen the plan.
- Whole sentences and absolute paths. Numbers carry their units and the code or log that produced
  them.
- Write it as the user speaking to the next session ("my ruling", "ask me"), since the user is the
  one who pastes it.
- No secrets, tokens, or credentials. No log tails; quote the exit code and the one line that matters.
- Length follows the work: a small task needs ten lines, and a multi-step research pipeline may need
  a hundred. Cut anything the reader could get faster from the record the prompt already points to.
