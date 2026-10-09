"""Track the project outputs a research deck draws on, and report or apply changes since the last snapshot.

Run from the project root (any Python 3.10+, standard library only):
  python sources.py check DECK
  python sources.py sync DECK
  python sources.py snapshot DECK

DECK is the deck folder (e.g., slides/conference). DECK/sources.json names, relative to the project root:
  numbers      LaTeX files of \\newcommand (or \\providecommand){\\name}{value} macros (the project's single-source numbers)
  figures_dir  the folder the deck's figures are copied from
  watch        glob patterns of every other output whose change should prompt a look at the deck

Slides cite a number as <span data-n="name">value</span> and a figure as src="figures/<file>".

check     prints what changed since DECK/manifest.json: watched files added, removed, or changed;
          macro values changed, with the slides that cite each; cited numbers or figures on the slides
          that no longer match the project; new macros no slide cites; and, for context, commits since the snapshot that touch a
          watched file.
          Writes nothing. Exit 0 when the deck is current, 3 when anything changed, 1 on an error.
sync      rewrites each data-n span to the current macro value and copies each cited figure from
          figures_dir into DECK/figures. Changes nothing else. Exit 1 if a citation cannot be resolved.
snapshot  records the current state in DECK/manifest.json. Run it after a build that passed review.
"""

import argparse
import hashlib
import json
import re
import shutil
import subprocess
import sys
from datetime import datetime
from pathlib import Path

MACRO = re.compile(r"^\s*\\(?:newcommand|renewcommand|providecommand)\{\\([A-Za-z]+)\}\{(.*)\}\s*(?:%.*)?$")
SPAN = re.compile(r'(<span data-n="([A-Za-z]+)">)(.*?)(</span>)', re.S)
FIGURE = re.compile(r'src="figures/([^"]+)"')
SLIDE_START = re.compile(r'<section class="slide[" ]')


def latex_to_text(value: str) -> str:
    """Render a macro value the way a slide shows it (percent signs, separators, minus signs)."""
    text = value.replace(r"\%", "%").replace(r"\&", "&").replace("{,}", ",").replace(r"\,", "\u2009").replace(r"\$", "$")
    text = text.replace("$", "").replace("--", "\u2013")
    return re.sub(r"(^|[\s(])-(?=\d|\.\d)", "\\1\u2212", text)


def load_numbers(root: Path, files: list[str]) -> dict[str, str]:
    numbers: dict[str, str] = {}
    for name in files:
        for line in (root / name).read_text().splitlines():
            match = MACRO.match(line)
            if match:
                numbers[match.group(1)] = match.group(2)
    return numbers


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()[:16]


def watched_files(root: Path, sources: dict) -> dict[str, str]:
    paths = set(sources.get("numbers", []))
    for pattern in sources.get("watch", []):
        paths |= {str(p.relative_to(root)) for p in root.glob(pattern) if p.is_file()}
    return {p: sha(root / p) for p in sorted(paths) if (root / p).is_file()}


def slide_citations(html: str) -> list[dict]:
    """Per slide (1-based, in source order): the cited macros with their shown text, and the figures."""
    starts = [m.start() for m in SLIDE_START.finditer(html)] + [len(html)]
    slides = []
    for i in range(len(starts) - 1):
        body = html[starts[i] : starts[i + 1]]
        slides.append(
            {
                "n": i + 1,
                "spans": [(m.group(2), m.group(3)) for m in SPAN.finditer(body)],
                "figures": sorted(set(FIGURE.findall(body))),
            }
        )
    return slides


def git_head(root: Path) -> str | None:
    result = subprocess.run(["git", "-C", str(root), "rev-parse", "HEAD"], capture_output=True, text=True)
    return result.stdout.strip() if result.returncode == 0 else None


def check(root: Path, deck: Path, sources: dict) -> int:
    manifest_path = deck / "manifest.json"
    numbers = load_numbers(root, sources.get("numbers", []))
    html = (deck / "src" / "deck.html").read_text()
    slides = slide_citations(html)
    cited: dict[str, list[int]] = {}
    for s in slides:
        for name in dict(s["spans"]):
            cited.setdefault(name, []).append(s["n"])
    changed = False

    if manifest_path.exists():
        manifest = json.loads(manifest_path.read_text())
        print(f"Snapshot: {manifest['created']} at commit {str(manifest.get('git_head'))[:8]}")
        old_files, new_files = manifest["files"], watched_files(root, sources)
        for label, items in [
            ("added", sorted(set(new_files) - set(old_files))),
            ("removed", sorted(set(old_files) - set(new_files))),
            ("changed", sorted(p for p in set(old_files) & set(new_files) if old_files[p] != new_files[p])),
        ]:
            if items:
                changed = True
                print(f"\nWatched files {label} ({len(items)}):")
                for p in items:
                    print(f"  {p}")
        old_numbers = manifest["numbers"]
        moved = sorted(n for n in set(old_numbers) & set(numbers) if old_numbers[n] != numbers[n])
        if moved:
            changed = True
            print(f"\nMacro values changed ({len(moved)}):")
            for n in moved:
                where = ", ".join(f"slide {k}" for k in cited.get(n, [])) or "not cited"
                print(f"  \\{n}: {old_numbers[n]} -> {numbers[n]}   ({where})")
        gone = sorted(set(old_numbers) - set(numbers))
        if gone:
            changed = True
            print(f"\nMacros removed: {', '.join(gone)}")
        head = manifest.get("git_head")
        if head and git_head(root) not in (None, head):
            # Listed for context only: the hash comparison above already decides whether content changed,
            # and a commit that adds an unchanged watched file (or the deck itself) is not a change.
            log = subprocess.run(
                ["git", "-C", str(root), "log", "--oneline", f"{head}..HEAD", "--", *sorted(set(old_files) | set(new_files))],
                capture_output=True,
                text=True,
            ).stdout.strip()
            if log:
                print(f"\nCommits since the snapshot that touch watched files (context; read their diffs):\n{log}")
    else:
        changed = True
        print("No manifest.json: the deck has never been snapshotted, so every comparison below is against the slides only.")

    stale, errors = [], []
    for s in slides:
        for name, shown in s["spans"]:
            if name not in numbers:
                errors.append(f"slide {s['n']}: cites \\{name}, which no numbers file defines")
            elif shown.strip() != latex_to_text(numbers[name]):
                stale.append(f"slide {s['n']}: \\{name} shows {shown.strip()!r}, project has {latex_to_text(numbers[name])!r}")
        for fig in s["figures"]:
            src = root / sources.get("figures_dir", "") / fig
            local = deck / "figures" / fig
            if not src.exists():
                if not local.exists():
                    errors.append(f"slide {s['n']}: figures/{fig} exists in neither the deck nor the project")
                continue
            if not local.exists() or sha(local) != sha(src):
                stale.append(f"slide {s['n']}: figures/{fig} differs from {src.relative_to(root)}")
    if stale:
        changed = True
        print(f"\nSlides out of date with the project ({len(stale)}), fixed by `sync`:")
        for line in stale:
            print(f"  {line}")
    uncited = sorted(set(numbers) - set(cited))
    print(f"\nMacros no slide cites ({len(uncited)} of {len(numbers)}): {', '.join(uncited) or 'none'}")
    for line in errors:
        print(f"ERROR: {line}")
    if errors:
        return 1
    print("\nRESULT: " + ("changes found" if changed else "deck is current"))
    return 3 if changed else 0


def sync(root: Path, deck: Path, sources: dict) -> int:
    numbers = load_numbers(root, sources.get("numbers", []))
    src_path = deck / "src" / "deck.html"
    html = src_path.read_text()
    missing = sorted({m.group(2) for m in SPAN.finditer(html)} - set(numbers))
    if missing:
        print(f"ERROR: slides cite macros no numbers file defines: {', '.join(missing)}")
        return 1
    edits = []

    def replace(match: re.Match) -> str:
        new = latex_to_text(numbers[match.group(2)])
        if match.group(3).strip() != new:
            edits.append(f"\\{match.group(2)}: {match.group(3).strip()!r} -> {new!r}")
        return match.group(1) + new + match.group(4)

    html = SPAN.sub(replace, html)
    if edits:
        src_path.write_text(html)
    copied = []
    for fig in sorted(set(FIGURE.findall(html))):
        src = root / sources.get("figures_dir", "") / fig
        local = deck / "figures" / fig
        if src.exists() and (not local.exists() or sha(local) != sha(src)):
            local.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src, local)
            copied.append(fig)
        elif not src.exists() and not local.exists():
            print(f"ERROR: figures/{fig} exists in neither the deck nor {sources.get('figures_dir')}")
            return 1
    print(f"numbers updated: {len(edits)}")
    for line in edits:
        print(f"  {line}")
    print(f"figures copied: {len(copied)}" + (f" ({', '.join(copied)})" if copied else ""))
    return 0


def snapshot(root: Path, deck: Path, sources: dict) -> int:
    manifest = {
        "created": datetime.now().isoformat(timespec="seconds"),
        "git_head": git_head(root),
        "files": watched_files(root, sources),
        "numbers": load_numbers(root, sources.get("numbers", [])),
    }
    (deck / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n")
    print(f"wrote {deck / 'manifest.json'}: {len(manifest['files'])} files, {len(manifest['numbers'])} macros")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Report or apply project changes to a research deck.")
    parser.add_argument("command", choices=["check", "sync", "snapshot"])
    parser.add_argument("deck", type=Path, help="Deck folder holding sources.json and src/deck.html.")
    parser.add_argument("--root", type=Path, default=Path.cwd(), help="Project root (default: current directory).")
    args = parser.parse_args()
    sources_path = args.deck / "sources.json"
    if not sources_path.exists():
        sys.exit(f"{sources_path} not found; scaffold the deck first")
    sources = json.loads(sources_path.read_text())
    return {"check": check, "sync": sync, "snapshot": snapshot}[args.command](args.root.resolve(), args.deck, sources)


if __name__ == "__main__":
    sys.exit(main())
