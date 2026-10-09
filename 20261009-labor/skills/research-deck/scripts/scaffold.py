"""Create a research deck folder from this skill's slide template.

Run:  python scaffold.py DEST   (any Python 3.10+, standard library only)

Copies ../template to DEST (which must not exist), then writes DEST/sources.json, the list of project
outputs the deck draws on (see references/update.md), and creates DEST/figures. The template is set in
Liberation Serif (metric-compatible with Times New Roman, SIL OFL), with a monospace face kept only for
code. This script never modifies the template, and it exits with a message instead of guessing when the
template no longer matches what it expects.
"""

import argparse
import json
import shutil
import sys
from pathlib import Path

SKILL = Path(__file__).resolve().parent.parent
TEMPLATE = SKILL / "template"

DEFAULT_SOURCES = {
    "numbers": ["results/latex/numbers.tex"],
    "figures_dir": "results/figures",
    "watch": [
        "results/figures/*.png",
        "results/tables/*.csv",
        "results/*.json",
        "docs/*.md",
    ],
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Scaffold a research deck from the skill's template.")
    parser.add_argument("dest", type=Path, help="New deck folder, e.g., slides/conference (must not exist).")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if args.dest.exists():
        sys.exit(f"{args.dest} exists; an existing deck is updated, not scaffolded (see references/update.md)")
    if "var(--serif)" not in (TEMPLATE / "src" / "deck.html").read_text():
        sys.exit(f"template is not set in var(--serif); check {TEMPLATE}")
    shutil.copytree(TEMPLATE, args.dest, ignore=shutil.ignore_patterns("__pycache__"))
    (args.dest / "figures").mkdir(exist_ok=True)
    (args.dest / "sources.json").write_text(json.dumps(DEFAULT_SOURCES, indent=2) + "\n")
    print(f"scaffolded {args.dest}; edit sources.json to match this project's outputs")


if __name__ == "__main__":
    main()
