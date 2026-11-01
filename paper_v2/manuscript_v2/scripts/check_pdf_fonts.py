#!/usr/bin/env python3
"""Fail if pdffonts reports a font whose embedded-resource flag is not yes.

`pdffonts` has a free-form multiword `type` column (for example `Type 3`).
The three yes/no flags therefore must be parsed from the right, not by fixed
whitespace-separated field number.
"""
from __future__ import annotations

from pathlib import Path
import re
import sys

STATUS_AT_END = re.compile(r"\s+(yes|no)\s+(yes|no)\s+(yes|no)\s+\d+\s+\d+\s*$", re.I)


def inspect(text: str) -> tuple[int, list[str]]:
    rows = 0
    problems: list[str] = []
    for line_no, line in enumerate(text.splitlines(), 1):
        stripped = line.strip()
        if not stripped or stripped.lower().startswith("name ") or set(stripped) <= {"-", " "}:
            continue
        match = STATUS_AT_END.search(line)
        if not match:
            problems.append(f"line {line_no}: could not parse pdffonts row: {line}")
            continue
        rows += 1
        embedded, _subset, _unicode = (value.lower() for value in match.groups())
        if embedded != "yes":
            problems.append(f"line {line_no}: font is not embedded: {line}")
    if rows == 0:
        problems.append("no font rows found in pdffonts output")
    return rows, problems


def main() -> int:
    if len(sys.argv) != 2:
        print(f"Usage: {Path(sys.argv[0]).name} PDFFONTS.txt", file=sys.stderr)
        return 2
    path = Path(sys.argv[1])
    try:
        text = path.read_text(errors="replace")
    except OSError as exc:
        print(f"ERROR: cannot read pdffonts report {path}: {exc}", file=sys.stderr)
        return 2
    rows, problems = inspect(text)
    if problems:
        for problem in problems:
            print("ERROR:", problem)
        return 1
    print(f"All {rows} reported PDF font resources are embedded (pdffonts emb=yes).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
