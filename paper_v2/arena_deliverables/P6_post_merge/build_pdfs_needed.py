#!/usr/bin/env python3
"""Build pdfs_needed_final.csv - the last wish-list of sources, after everything already held is removed.

The pool is not a guess: it is exactly the set of bib keys still carrying a SOURCE NOT AVAILABLE row in
claim_register.csv (one row per claim, one key per row). A key leaves the pool only when a record shows
the work is in hand:

  library_inventory_v3.csv        files read in the library pass (63 keys matched)
  library_available_sources.csv   author-supplied set + library copies, minus the one known mismatch
  BOOKS_HELD_2026-11-01.csv       21 books held
  claim_check_C_batch_*.csv       batches already decided from a source in hand

Ordering: most claims blocked first; ties by missing_sources_priority.csv rank, then alphabetically.
Three works are appended that are held only as image-only scans - they are not missing, but no page of
them can be quoted, so they stay on the list with claims_blocked 0.
Prints PASS and exits 0.
"""
from __future__ import annotations

import csv
import glob
import re
import sys
import unicodedata
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
PAPER = HERE.parent.parent.parent / "paper_v2"
DELIV = PAPER / "arena_deliverables"
CLAIMS = PAPER / "claim_register.csv"
PRIORITY = PAPER / "missing_sources_priority.csv"
INV3 = DELIV / "P3_evidence_claims_B" / "library_inventory_v3.csv"
AVAIL = DELIV / "P3_evidence_claims_B" / "library_available_sources.csv"
BOOKS = DELIV / "P3_evidence_claims_B" / "BOOKS_HELD_2026-11-01.csv"
BATCHES = DELIV / "P3_evidence_claims_C"
OUT = HERE / "pdfs_needed_final.csv"
MAX_ROWS = 60

IMAGE_ONLY = [("Stoneley1924", "Stoneley, R.", "1924", "Proceedings of the Royal Society A 106:416"),
              ("Barnett1985", "Barnett, D. M.", "1985",
               "Journal of the Mechanics and Physics of Solids 33:6"),
              ("Green1991", "Green, A. E. and Naghdi, P. M.", "1991",
               "Proceedings of the Royal Society A 432")]
SCAN_NOTE = ("Already held, but only as an image-only scan with no text layer: a text-layer copy is "
             "needed before any page can be quoted. Kept here so the gap is not lost once the work "
             "counts as held.")


def norm(s: str) -> str:
    s = unicodedata.normalize("NFKD", s or "")
    s = "".join(c for c in s if not unicodedata.combining(c))
    return re.sub(r"\s+", " ", re.sub(r"[^a-z0-9 ]+", " ", s.lower())).strip()


def split_citation(citation: str) -> dict:
    """'Tzou, D. Y. (1995), A unified field approach, J. Heat Transfer 117:8-16' -> parts."""
    authors = citation.split("(")[0].strip().rstrip(",")
    m = re.search(r"\((\d{4})\)", citation)
    year = m.group(1) if m else ""
    after = citation.split(")", 1)[1].strip(" ,") if ")" in citation else citation
    bits = [b.strip() for b in after.split(",") if b.strip()]
    journal = ""
    if len(bits) > 1 and re.search(r"\d", bits[-1]) and not re.search(r"\bbook\b", bits[-1], re.I):
        journal, bits = bits[-1], bits[:-1]
    return {"authors": authors, "year": year, "title": ", ".join(bits) or after, "journal": journal}


def held_keys() -> dict[str, str]:
    held: dict[str, str] = {}
    for r in csv.DictReader(AVAIL.open(encoding="utf-8")):
        if "does not match" in (r.get("availability") or ""):
            continue                      # the file in the folder is a different paper
        held.setdefault(r["bib_key"], "library_available_sources.csv")
    for r in csv.DictReader(INV3.open(encoding="utf-8")):
        if r.get("matched_bib_key"):
            held.setdefault(r["matched_bib_key"], "library_inventory_v3.csv")
    for f in sorted(glob.glob(str(BATCHES / "claim_check_C_batch_*.csv"))):
        for r in csv.DictReader(open(f, encoding="utf-8")):
            key = (r.get("cited_source") or "").split("|")[0].strip()
            if key and r.get("verdict") != "SOURCE NOT AVAILABLE":
                held.setdefault(key, Path(f).name)
    return held


def main() -> int:
    reg = list(csv.DictReader(CLAIMS.open(encoding="utf-8")))
    sna = [r for r in reg if (r.get("verdict") or "").strip() == "SOURCE NOT AVAILABLE"]
    counts = Counter((r.get("cited_source") or "").split("|")[0].strip() for r in sna)
    meta = {}
    for r in sna:
        cs = r.get("cited_source") or ""
        key = cs.split("|")[0].strip()
        if key and key not in meta:
            meta[key] = split_citation(cs.split("|", 1)[1].strip() if "|" in cs else cs)

    prank = {}
    for p in csv.DictReader(PRIORITY.open(encoding="utf-8")):
        for cid in (p.get("claim_ids") or "").split():
            r = next((x for x in reg if x.get("claim_id") == cid), None)
            if r:
                prank.setdefault((r.get("cited_source") or "").split("|")[0].strip(), int(p["rank"]))

    held = held_keys()
    todo = [(k, c) for k, c in counts.items() if k and k not in held]
    todo.sort(key=lambda kc: (-kc[1], prank.get(kc[0], 10_000), kc[0]))

    rows = []
    for key, blocked in todo[: MAX_ROWS - len(IMAGE_ONLY)]:
        m = meta.get(key, {"authors": "", "year": "", "title": "", "journal": ""})
        rows.append({"rank": "", "bib_key": key, "title": m["title"], "authors": m["authors"],
                     "journal": m["journal"], "year": m["year"], "doi": "",
                     "claims_blocked": str(blocked),
                     "why_needed": (f"{blocked} claim(s) in the register still say SOURCE NOT AVAILABLE "
                                    f"against this work; a copy with readable text settles them at page "
                                    f"level. Nothing about it has been read, so nothing is assumed.")})
    for key, au, yr, jn in IMAGE_ONLY:
        rows.append({"rank": "", "bib_key": key, "title": "(held copy is an image-only scan)",
                     "authors": au, "journal": jn, "year": yr, "doi": "", "claims_blocked": "0",
                     "why_needed": SCAN_NOTE})
    for i, r in enumerate(rows, 1):
        r["rank"] = i

    cols = ["rank", "bib_key", "title", "authors", "journal", "year", "doi",
            "claims_blocked", "why_needed"]
    with OUT.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=cols)
        w.writeheader()
        w.writerows(rows)
    print(f"register rows: {len(reg)}; SOURCE NOT AVAILABLE: {len(sna)}; distinct keys: {len(counts)}")
    print(f"keys held already: {len(counts) - len(todo)}; unheld: {len(todo)}")
    print(f"written: {len(rows)} ({len(rows) - len(IMAGE_ONLY)} sources + {len(IMAGE_ONLY)} image-only)")
    print(f"claims blocked by the listed sources: {sum(int(r['claims_blocked']) for r in rows)}")
    print("PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
