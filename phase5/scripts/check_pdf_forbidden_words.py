#!/usr/bin/env python3
"""PDF forbidden-word gate: scan built PDF text for internal/process tokens.

Fails if any forbidden word or phrase appears in the extracted PDF text.
The forbidden list includes internal ledger IDs, referee-register language,
ledger terminology, and HTML artifacts that must never reach the printed PDF.

Usage:
    python3 phase5/scripts/check_pdf_forbidden_words.py build/main.txt
"""
from __future__ import annotations

import sys
from pathlib import Path

FORBIDDEN = [
    "Class A", "Class B", "Class C",
    "OCL-",
    "WP6-", "WP8",
    "mock referee",
    "source-only",
    "referee register",
    "open-claim",
    "gate",
    "build",
    "not checked here",
    "&amp;",
    "ledger",
]


def main() -> int:
    if len(sys.argv) != 2:
        print(f"Usage: {Path(sys.argv[0]).name} PDF_TEXT", file=sys.stderr)
        return 2
    text_path = Path(sys.argv[1])
    if not text_path.is_file():
        print(f"ERROR: PDF text not found: {text_path}", file=sys.stderr)
        return 2
    text = text_path.read_text(errors="replace")
    found: list[str] = []
    for token in FORBIDDEN:
        if token.lower() in text.lower():
            found.append(token)
    if found:
        print("ERROR: forbidden tokens found in PDF text:")
        for token in found:
            print(f"  {token!r}")
        return 1
    print("PASS: no forbidden tokens in PDF text")
    return 0


if __name__ == "__main__":
    sys.exit(main())
