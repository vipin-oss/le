#!/usr/bin/env python3
"""Build-log gate: fail on float/layout defects in the TeX build log.

Fails when the build log contains any of:
  * "Float too large for page"
  * "Float(s) lost"
  * "Overfull \\hbox" or "Overfull \\vbox" with size > 1 pt
  * "Underfull \\vbox" too high

Usage:
    python3 phase5/scripts/check_build_log_floats.py BUILD_LOG
"""
from __future__ import annotations

import re
import sys
from pathlib import Path


def main() -> int:
    if len(sys.argv) != 2:
        print(f"Usage: {Path(sys.argv[0]).name} BUILD_LOG", file=sys.stderr)
        return 2
    log_path = Path(sys.argv[1])
    if not log_path.is_file():
        print(f"ERROR: build log not found: {log_path}", file=sys.stderr)
        return 2
    text = log_path.read_text(errors="replace")
    errors: list[str] = []

    # Float too large for page / floats lost
    if re.search(r"Float too large for page", text):
        errors.append("Float too large for page")
    if re.search(r"Float\(s\) lost", text):
        errors.append("Float(s) lost")

    # Overfull hbox/vbox > 1 pt
    # TeX log line: "Overfull \hbox (12.3pt too wide)"
    # Use character class [\\] to match a literal backslash without
    # raw-string escaping confusion.
    overfull_re = re.compile(
        r"Overfull [\\](hbox|vbox) [(](?P<size>[-+]?[0-9.]+)pt too (wide|high)"
    )
    for match in overfull_re.finditer(text):
        size = float(match.group("size"))
        if size > 1.0:
            kind = match.group(1)
            errors.append(f"Overfull \\{kind} {size:.1f}pt too {match.group(3)}")

    # Underfull vbox too high
    underfull_re = re.compile(
        r"Underfull [\\](vbox) [(](?P<size>[-+]?[0-9.]+)pt too high[)]"
    )
    for match in underfull_re.finditer(text):
        size = float(match.group("size"))
        errors.append(f"Underfull \\vbox {size:.1f}pt too high")

    if errors:
        print("ERROR: build-log layout defects detected:")
        for e in errors[:30]:
            print(f"  {e}")
        if len(errors) > 30:
            print(f"  ... and {len(errors) - 30} more")
        return 1
    print("PASS: no float or overfull/underfull defects in build log")
    return 0


if __name__ == "__main__":
    sys.exit(main())
