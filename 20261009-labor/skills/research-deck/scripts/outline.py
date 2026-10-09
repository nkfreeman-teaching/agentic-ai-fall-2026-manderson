"""Print a deck as a Markdown outline: per slide, the title, timing target, visible text, figures, and notes.

Run:  python outline.py DECK [--max-words N] [--no-notes]   (any Python 3.10+, standard library only)

DECK is the deck folder; the script reads DECK/src/deck.html. Visible words exclude the title, the kicker,
SVG text (figure labels), and the speaker notes. A slide whose visible words exceed --max-words (default
30) is marked TEXT-HEAVY, and the summary line counts them, so the text budget in references/arc.md is a
measured check rather than a judgment. Title, closing, and backup slides (data-time="") are exempt. --no-notes drops the notes, giving the view the audience has.
"""

import argparse
import sys
from html.parser import HTMLParser
from pathlib import Path

VOID = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "source", "track", "wbr"}
SKIP = {"script", "style"}


class DeckParser(HTMLParser):
    """Collect each section.slide's parts. Every open tag is pushed with the role it gives its text."""

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.slides: list[dict] = []
        self.stack: list[tuple[str, str | None]] = []

    def role(self) -> str | None:
        for _, r in reversed(self.stack):
            if r is not None:
                return r
        return None

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        a = dict(attrs)
        classes = (a.get("class") or "").split()
        if tag == "section" and "slide" in classes:
            self.slides.append(
                {
                    "kind": " ".join(c for c in classes if c != "slide"),
                    "title": a.get("data-title", ""),
                    "time": a.get("data-time", ""),
                    "heading": [],
                    "kicker": [],
                    "body": [],
                    "svg": [],
                    "notes": [],
                    "figures": [],
                }
            )
        if tag == "img" and self.slides and a.get("src"):
            self.slides[-1]["figures"].append(a["src"])
        if tag in VOID:
            return
        if tag == "section" and "slide" in classes:
            r = "slide"
        elif tag in SKIP:
            r = "skip"
        elif tag == "aside" and "notes" in classes:
            r = "notes"
        elif tag == "svg":
            r = "svg"
        elif "kicker" in classes:
            r = "kicker"
        elif tag in {"h1", "h2"}:
            r = "heading"
        else:
            r = None
        self.stack.append((tag, r))

    def handle_endtag(self, tag: str) -> None:
        if tag in VOID:
            return
        for i in range(len(self.stack) - 1, -1, -1):
            if self.stack[i][0] == tag:
                del self.stack[i:]
                return

    def handle_data(self, data: str) -> None:
        text = " ".join(data.split())
        if not text or not any(r == "slide" for _, r in self.stack):
            return  # outside every slide, e.g., the help overlay after the last section
        r = self.role()
        if r == "skip":
            return
        self.slides[-1][r if r not in (None, "slide") else "body"].append(text)


def main() -> int:
    parser = argparse.ArgumentParser(description="Print a deck's slides as a Markdown outline.")
    parser.add_argument("deck", type=Path)
    parser.add_argument("--max-words", type=int, default=30)
    parser.add_argument("--no-notes", action="store_true")
    args = parser.parse_args()
    deck_parser = DeckParser()
    deck_parser.feed((args.deck / "src" / "deck.html").read_text())
    heavy = 0
    for i, s in enumerate(deck_parser.slides, start=1):
        words = len(" ".join(s["body"]).split())
        flag = ""
        exempt = "s-title" in s["kind"] or "s-close" in s["kind"] or s["time"] == ""
        if words > args.max_words and not exempt:
            heavy += 1
            flag = "  TEXT-HEAVY"
        print(f"## Slide {i}: {' '.join(s['heading']) or s['title']}")
        print(f"target {s['time'] or '?'} | layout {s['kind'] or 'content'} | visible words {words}{flag}")
        if s["kicker"]:
            print(f"kicker: {' '.join(s['kicker'])}")
        if s["body"]:
            print(f"on slide: {' | '.join(s['body'])}")
        if s["figures"]:
            print(f"figures: {', '.join(s['figures'])}")
        if s["svg"]:
            print(f"diagram labels: {' | '.join(s['svg'])}")
        if s["notes"] and not args.no_notes:
            print(f"notes: {' '.join(s['notes'])}")
        print()
    print(f"slides={len(deck_parser.slides)} text_heavy={heavy} (more than {args.max_words} visible words)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
