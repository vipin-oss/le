#!/usr/bin/env python3
"""B23 independent recount: ledger, bibliography hygiene, figure mirrors.

Counts are recomputed straight from the CSV / TeX / bib files instead of calling
phase5/scripts/validate_claim_ledger.py or phase5/verification/verify_reference_hygiene.py.
"""
from __future__ import annotations

import csv
import glob
import hashlib
import os
import re
from collections import Counter

ROOT = "/home/user/b23_src/phase5"
MASTER = os.path.join(ROOT, "master")

# ---------------- ledger ----------------
rows = list(csv.DictReader(open(os.path.join(ROOT, "reports", "OPEN_CLAIMS_LEDGER.csv"))))
print("ledger rows:", len(rows))
print("classes:", dict(sorted(Counter(r["class"] for r in rows).items())))
print("ledger columns:", ", ".join(rows[0].keys()))
fresh = [r for r in rows if "2026-10-27" in (r.get("evidence_mode") or "")]
print("rows whose evidence_mode names 2026-10-27:", len(fresh), [r["ledger_row_id"] for r in fresh])
print("rows with empty resolved_by:", sum(1 for r in rows if not (r.get("resolved_by") or "").strip()))

# ---------------- bibliography ----------------
tex = []
for p in glob.glob(os.path.join(MASTER, "**", "*.tex"), recursive=True):
    tex.append(open(p, encoding="utf-8", errors="ignore").read())
blob = "\n".join(tex)
cited = set()
for m in re.finditer(r"\\cite[pt]?\*?(?:\[[^\]]*\])*\{([^}]*)\}", blob):
    for k in m.group(1).split(","):
        k = k.strip()
        if k:
            cited.add(k)
bib = open(os.path.join(MASTER, "references_local.bib"), encoding="utf-8").read()
entries = set(re.findall(r"@\w+\s*\{\s*([^,\s]+)\s*,", bib))
print("unique cited keys:", len(cited))
print("bib entries:", len(entries))
print("cited keys missing from bib:", sorted(cited - entries))
print("bib entries never cited:", len(entries - cited))
doi = len(re.findall(r"\bdoi\s*=", bib))
print("entries carrying a doi field:", doi)

# ---------------- figure mirrors ----------------
svgs = {
    "source": os.path.join(MASTER, "figures/source/fig12-solution-workflow.svg"),
    "rendered": os.path.join(MASTER, "figures/rendered/fig12-solution-workflow.svg"),
}
digests = {}
for name, path in svgs.items():
    h = hashlib.sha256(open(path, "rb").read()).hexdigest()
    digs = h[:16]
    digests[name] = h
    print(f"fig12 {name:9s} sha256 {digs} size {os.path.getsize(path)}")
pdf_alias = os.path.join(MASTER, "figures/source/fig12-solution-workflow.pdf")
print("fig12 pdf twin present:", os.path.exists(pdf_alias))
print("source and rendered SVG identical:", digests["source"] == digests["rendered"])

steps = re.findall(r">Step\s*(\d+)<", open(svgs["source"], encoding="utf-8").read())
print("step labels in source SVG:", sorted(set(steps), key=int), "count", len(set(steps)))
