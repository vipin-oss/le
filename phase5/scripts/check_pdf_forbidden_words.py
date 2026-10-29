#!/usr/bin/env python3
"""PDF forbidden-word gate: scan built PDF text for internal/process tokens.

Fails if any forbidden word or phrase appears in the extracted PDF text.
Common English words (gate, build, script, verifier) are matched with word
boundaries to avoid false positives on words like "propagate" or "building".

Usage:
    python3 phase5/scripts/check_pdf_forbidden_words.py PDF_TEXT
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

# Tokens matched as case-insensitive substrings (specific phrases/IDs).
FORBIDDEN_SUBSTRING = [
    "Class A", "Class B", "Class C",
    "OCL-", "WP6-", "WP8",
    "mock referee", "source-only", "referee register",
    "open-claim", "not checked here", "&amp;", "ledger",
    "held copy", "repository", "claim table", "verification record",
    "UNNUMBERED", "app:", "claimed bridge", "Not recorded",
]

# Common English words matched with word boundaries (case-insensitive)
# to avoid false positives (e.g. "propagate" containing "gate",
# "building" containing "build").
FORBIDDEN_WORD = [
    "gate", "build", "script", "verifier",
]

# Regex patterns matched case-insensitively (unless noted).
FORBIDDEN_PATTERN = [
    (r"eq:\d", True),        # equation reference style like eq:4.18
    (r"\bVERIFIED\b", False),   # all-caps status label (case-sensitive)
    (r"\bCONDITIONAL\b", False), # all-caps status label (case-sensitive)
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

    # Substring matches (case-insensitive)
    lower = text.lower()
    for token in FORBIDDEN_SUBSTRING:
        if token.lower() in lower:
            found.append(token)

    # Word-boundary matches (case-insensitive)
    for word in FORBIDDEN_WORD:
        if re.search(rf"\b{re.escape(word)}\b", text, re.I):
            found.append(word)

    # Regex pattern matches (pattern, case_insensitive flag)
    for pattern, case_insensitive in FORBIDDEN_PATTERN:
        flags = re.I if case_insensitive else 0
        if re.search(pattern, text, flags):
            found.append(pattern)

    if found:
        print("ERROR: forbidden tokens found in PDF text:")
        for token in found:
            print(f"  {token!r}")
        return 1
    print("PASS: no forbidden tokens in PDF text")
    return 0


if __name__ == "__main__":
    sys.exit(main())
