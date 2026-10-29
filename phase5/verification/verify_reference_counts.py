#!/usr/bin/env python3
"""Reproduce the reference and literature-matrix counts stated in Section 14.

Counts only: this script does not check DOI resolution, source content, or
whether a cited work supports a sentence. It exits non-zero if a count changes
so the text can be updated.
"""
from __future__ import annotations

import csv
import glob
import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MATRIX = ROOT / "reports" / "literature-evidence-matrix.csv"
BIB = ROOT / "master" / "references_local.bib"

EXPECTED = {
    "matrix_rows": 97,
    "matrix_doi_nonblank": 52,
    "matrix_doi_blank": 45,
    "matrix_oa_yes": 13,
    "matrix_fulltext_yes": 15,
    "matrix_fulltext_methodology": 1,
    "matrix_multilabel_rows": 0,
    "bib_entries": 144,
    "bib_cited_keys": 107,
    "bib_uncited_keys": 37,
}


def main() -> int:
    rows = list(csv.DictReader(MATRIX.open(encoding="utf-8", newline="")))
    ids = [r["record_id"] for r in rows]
    assert len(ids) == len(set(ids)), "duplicate record_id in matrix"
    got: dict[str, int] = {
        "matrix_rows": len(rows),
        "matrix_doi_nonblank": sum(1 for r in rows if r["doi"].strip()),
        "matrix_doi_blank": sum(1 for r in rows if not r["doi"].strip()),
        "matrix_oa_yes": sum(1 for r in rows if r["inventory_open_access_flag"] == "yes"),
        "matrix_fulltext_yes": sum(1 for r in rows if r["inventory_full_text_flag"] == "yes"),
        "matrix_fulltext_methodology": sum(
            1 for r in rows if r["inventory_full_text_flag"] == "methodology"
        ),
        "matrix_multilabel_rows": sum(
            1 for r in rows if ";" in r["theory_family"] or "|" in r["theory_family"]
        ),
    }
    bib_text = BIB.read_text(encoding="utf-8")
    bib_keys = re.findall(r"^@\w+\{([^,\s]+),", bib_text, flags=re.M)
    cited: set[str] = set()
    for path in (
        glob.glob(str(ROOT / "master" / "sections" / "*.tex"))
        + glob.glob(str(ROOT / "master" / "appendices" / "*.tex"))
        + glob.glob(str(ROOT / "master" / "frontmatter" / "*.tex"))
    ):
        text = Path(path).read_text(encoding="utf-8")
        for m in re.finditer(r"\\cite[a-zA-Z]*\*?(?:\[[^\]]*\])*\{([^}]*)\}", text):
            cited.update(k.strip() for k in m.group(1).split(",") if k.strip())
    got["bib_entries"] = len(bib_keys)
    got["bib_cited_keys"] = len(cited & set(bib_keys))
    got["bib_uncited_keys"] = len(set(bib_keys) - cited)

    status = 0
    for key, want in EXPECTED.items():
        ok = got[key] == want
        print(f"{'PASS' if ok else 'CHANGED'}: {key} = {got[key]} (stated {want})")
        status |= 0 if ok else 1
    print(f"Matrix raw theory labels (distinct): {len(set(r['theory_family'] for r in rows))}")
    print("Scope: counts only; no DOI, source, or claim check.")
    return status


if __name__ == "__main__":
    raise SystemExit(main())
