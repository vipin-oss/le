#!/usr/bin/env python3
"""Verify reference collection counts: total bib entries, cited keys, uncited keys.

Expected (per Section 14 taxonomy reconciliation):
  bib entries   : 147
  cited keys    : 110
  uncited keys  : 37
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
MASTER = ROOT / "phase5" / "master"
MAIN = MASTER / "main.tex"
BIB = MASTER / "references_local.bib"

EXPECTED_BIB = 148
EXPECTED_CITED = 111
EXPECTED_UNCITED = 37


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


def main() -> int:
    files = active_tex_files(MAIN)
    bib_count = count_bib_entries(BIB)
    cited = collect_cited_keys(files)
    cited_count = len(cited)
    uncited = bib_count - cited_count

    print(f"Active TeX files: {len(files)}")
    print(f"Bib entries: {bib_count} (expected {EXPECTED_BIB})")
    print(f"Cited keys:  {cited_count} (expected {EXPECTED_CITED})")
    print(f"Uncited keys: {uncited} (expected {EXPECTED_UNCITED})")

    errors = []
    if bib_count != EXPECTED_BIB:
        errors.append(f"bib entries {bib_count} != {EXPECTED_BIB}")
    if cited_count != EXPECTED_CITED:
        errors.append(f"cited keys {cited_count} != {EXPECTED_CITED}")
    if uncited != EXPECTED_UNCITED:
        errors.append(f"uncited keys {uncited} != {EXPECTED_UNCITED}")

    if errors:
        print("ERROR:", "; ".join(errors))
        return 1
    print("Reference counts verified.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
