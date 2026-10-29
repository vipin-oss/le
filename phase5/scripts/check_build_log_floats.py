#!/usr/bin/env python3
"""Build-log gate: fail on float/layout defects in the TeX build log.

Fails when the build log contains any of:
  * "Float too large for page"
  * "Float(s) lost"
  * "Overfull \\hbox" with size >= 1 pt (threshold is 1 pt per gate rules)
  * "Overfull \\vbox ... too high" with size >= 1 pt
  * "Underfull \\vbox ... while \\output is active"
  * Real TeX underfull hbox message at very high badness (>= 10000)

Prints each finding as a GitHub Actions annotation line.

Usage:
    python3 phase5/scripts/check_build_log_floats.py BUILD_LOG
"""
from __future__ import annotations

import re
import sys
from pathlib import Path


def annotate(title: str, finding: str) -> None:
    """Print a GitHub Actions error annotation (capped at ~50 lines)."""
    print(f"::error title={title}::{finding}")


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

    # Overfull hbox >= 1 pt (threshold is 1 pt per gate rules)
    # TeX log line: "Overfull \hbox (3.2pt too wide)"
    overfull_hbox_re = re.compile(
        r"Overfull [\\](hbox) [(](?P<size>[-+]?[0-9.]+)pt too (wide|high)"
    )
    for match in overfull_hbox_re.finditer(text):
        size = float(match.group("size"))
        if abs(size) >= 1.0:
            errors.append(f"Overfull \\hbox {size:.1f}pt too {match.group(3)}")

    # Overfull vbox too high >= 1 pt
    overfull_vbox_re = re.compile(
        r"Overfull [\\](vbox) [(](?P<size>[-+]?[0-9.]+)pt too high"
    )
    for match in overfull_vbox_re.finditer(text):
        size = float(match.group("size"))
        if abs(size) >= 1.0:
            errors.append(f"Overfull \\vbox {size:.1f}pt too high")

    # Real TeX underfull vbox message:
    # "Underfull \vbox (badness N) has occurred while \output is active"
    underfull_vbox_re = re.compile(
        r"Underfull [\\]vbox [(]badness (?P<badness>[0-9]+)[)] "
        r"has occurred while [\\]output is active"
    )
    for match in underfull_vbox_re.finditer(text):
        badness = int(match.group("badness"))
        errors.append(
            f"Underfull \\vbox (badness {badness}) has occurred while \\output is active"
        )

    # Real TeX underfull hbox message (only at extreme badness):
    # "Underfull \hbox (badness N) in paragraph"
    underfull_hbox_re = re.compile(
        r"Underfull [\\]hbox [(]badness (?P<badness>[0-9]+)[)] in paragraph"
    )
    for match in underfull_hbox_re.finditer(text):
        badness = int(match.group("badness"))
        if badness >= 10000:
            errors.append(
                f"Underfull \\hbox (badness {badness}) in paragraph"
            )

    # Print annotations (cap at ~50 lines)
    for e in errors[:50]:
        annotate("Build-log float/layout defect check", e)

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
