#!/usr/bin/env python3
"""Verify reference collection counts against Section 14 taxonomy text.

Counts bib entries from references_local.bib, collects cited keys from the .tex
files transitively included by main.tex, parses the three numbers printed in
sec14_taxonomy.tex, and fails when they disagree. Also fails when a cited key
is missing from the bibliography.

Usage:
    python3 phase5/scripts/verify_reference_counts.py
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
MASTER = ROOT / "phase5" / "master"
MAIN = MASTER / "main.tex"
BIB = MASTER / "references_local.bib"
SEC14 = MASTER / "sections/sec14_taxonomy.tex"


def uncomment(text: str) -> str:
    """Remove TeX comments, preserving escaped percent signs."""
    output: list[str] = []
    for line in text.splitlines():
        kept: list[str] = []
        i = 0
        while i < len(line):
            if line[i] == "%":
                backslashes = 0
                j = i - 1
                while j >= 0 and line[j] == "\\":
                    backslashes += 1
                    j -= 1
                if backslashes % 2 == 0:
                    break
            kept.append(line[i])
            i += 1
        output.append("".join(kept))
    return "\n".join(output)


def active_tex_files(path: Path, seen: set[Path] | None = None) -> list[Path]:
    """Return all TeX files transitively included from main.tex."""
    seen = seen or set()
    path = path.resolve()
    if path in seen:
        return []
    if not path.is_file():
        raise AssertionError(f"missing active TeX input: {path}")
    seen.add(path)
    text = uncomment(path.read_text(encoding="utf-8"))
    result = [path]
    for match in re.finditer(r"\\(?:input|include)\s*\{([^}]+)\}", text):
        name = match.group(1).strip()
        child = (MASTER / name) if not name.startswith("/") else Path(name)
        if child.suffix != ".tex":
            child = child.with_suffix(".tex")
        result.extend(active_tex_files(child, seen))
    return result


def collect_cited_keys(files: list[Path]) -> set[str]:
    keys: set[str] = set()
    pattern = re.compile(r"\\(?:cite|citep|citet|textcite|parencite)\s*(?:\[[^\]]*\])?\{([^}]+)\}")
    for tex in files:
        text = uncomment(tex.read_text(encoding="utf-8", errors="replace"))
        for m in pattern.finditer(text):
            for k in re.split(r"\s*,\s*", m.group(1)):
                k = k.strip()
                if k:
                    keys.add(k)
    return keys


def count_bib_entries(path: Path) -> int:
    text = path.read_text(encoding="utf-8-sig")
    return sum(1 for line in text.splitlines() if line.strip().startswith("@"))


def parse_sec14_numbers(path: Path) -> tuple[int, int, int]:
    """Parse the three counts printed in sec14_taxonomy.tex.

    Expected sentence: "Of the N bibliography entries, M keys are cited ... and K are not."
    """
    text = path.read_text(encoding="utf-8")
    m = re.search(
        r"Of the (?P<bib>\d+) bibliography entries?,? (?P<cited>\d+) keys are cited[^.]*? and (?P<uncited>\d+) are not\.",
        text,
    )
    if not m:
        raise AssertionError("Could not parse reference counts from sec14_taxonomy.tex")
    return int(m.group("bib")), int(m.group("cited")), int(m.group("uncited"))


def bib_keys(path: Path) -> set[str]:
    text = path.read_text(encoding="utf-8-sig")
    return {m.group(1) for m in re.finditer(r"@\w+\{([^,]+),", text)}


def main() -> int:
    files = active_tex_files(MAIN)
    bib_count = count_bib_entries(BIB)
    cited = collect_cited_keys(files)
    cited_count = len(cited)
    uncited_computed = bib_count - cited_count

    # Parse the numbers printed in sec14
    sec14_bib, sec14_cited, sec14_uncited = parse_sec14_numbers(SEC14)

    # Check cited keys exist in bib
    bibkey_set = bib_keys(BIB)
    missing_cited = sorted(cited - bibkey_set)

    print(f"Active TeX files: {len(files)}")
    print(f"Bib entries: {bib_count} (from references_local.bib)")
    print(f"Cited keys:  {cited_count} (from .tex cites)")
    print(f"Uncited:     {uncited_computed} (= bib - cited)")
    print(f"sec14 text:  bib={sec14_bib} cited={sec14_cited} uncited={sec14_uncited}")

    errors: list[str] = []
    if bib_count != sec14_bib:
        errors.append(f"bib entries {bib_count} != sec14 {sec14_bib}")
    if cited_count != sec14_cited:
        errors.append(f"cited keys {cited_count} != sec14 {sec14_cited}")
    if uncited_computed != sec14_uncited:
        errors.append(f"uncited {uncited_computed} != sec14 {sec14_uncited}")
    if missing_cited:
        errors.append(f"cited keys missing from bib: {missing_cited}")

    if errors:
        print("ERROR:", "; ".join(errors))
        return 1
    print("Reference counts verified against sec14_taxonomy.tex.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
