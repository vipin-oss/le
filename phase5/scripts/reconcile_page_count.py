#!/usr/bin/env python3
"""Compare corresponding phase4/v1.0 and phase5/v1.1 TeX source inventories.

This is a source-content audit only. The token counts include comments and TeX
commands and must not be reported as prose word counts or as a page-by-page
causal allocation of the PDF page-count difference.
"""
from __future__ import annotations

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[2]
GROUPS = ("sections", "appendices", "tables/source")
TOKEN = re.compile(r"\b[\w'-]+\b", re.UNICODE)


def count(path: Path) -> int:
    return len(TOKEN.findall(path.read_text(errors="replace")))


def main() -> None:
    total_old = total_new = 0
    print("group,file,v1_0_source_tokens,v1_1_source_tokens,delta")
    missing: list[str] = []
    for group in GROUPS:
        old_root = ROOT / "phase4" / "manuscript" / group
        new_root = ROOT / "phase5" / "master" / group
        old_files = {p.name: p for p in old_root.glob("*.tex")}
        new_files = {p.name: p for p in new_root.glob("*.tex")}
        for name in sorted(old_files.keys() | new_files.keys()):
            if name not in old_files or name not in new_files:
                missing.append(f"{group}/{name}")
                continue
            a, b = count(old_files[name]), count(new_files[name])
            total_old += a
            total_new += b
            print(f"{group},{name},{a},{b},{b-a:+d}")
    print(f"TOTAL,,{total_old},{total_new},{total_new-total_old:+d}")
    if missing:
        raise SystemExit("Unpaired source files: " + ", ".join(missing))


if __name__ == "__main__":
    main()
