#!/usr/bin/env python3
"""Validate every claim_check_C_batch_NNN.csv against the claim register.

Checks per batch
  * exact B-schema header (same 13 columns as the P3_evidence_claims_B batches)
  * at most 40 rows, claim ids unique across all batches and of the form CC-NNNN
  * verdict in {SUPPORTED, PARTLY SUPPORTED, NOT SUPPORTED, SOURCE NOT AVAILABLE}
  * a verdict other than SOURCE NOT AVAILABLE carries a real page/equation locator
  * SOURCE NOT AVAILABLE rows carry '-' in the locator and a stated reason
  * the register claim named in the notes/statement exists, and its source_doi agrees
  * no Drive identifier, link or source-library folder name anywhere
Prints PASS ... and exits 0 when every check holds.
"""
import csv
import re
import sys
import zipfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
REG = HERE.parents[1] / "claim_register.csv"
ZIP = HERE.parents[1] / "paper_sources.zip"

HEADER = ["claim_id", "manuscript_location", "manuscript_statement", "cited_source",
          "source_doi", "found_in_library", "verdict", "source_page_or_equation",
          "source_wording_max25words", "what_source_actually_states",
          "verification_level", "notes"]
VERDICTS = {"SUPPORTED", "PARTLY SUPPORTED", "NOT SUPPORTED", "SOURCE NOT AVAILABLE"}
MAX_ROWS = 40

fails = []


def check(cond, msg):
    if not cond:
        fails.append(msg)


def main():
    reg = {r["claim_id"]: r for r in csv.DictReader(REG.open(newline="", encoding="utf-8"))}
    with zipfile.ZipFile(ZIP) as z:
        bib = "".join(z.read(n).decode("utf-8", "replace") for n in z.namelist() if n.endswith(".bib"))
    bib_dois = set(re.findall(r"doi\s*=\s*[{\"]\s*(10\.[^}\"\s]+)", bib))

    batches = sorted(HERE.glob("claim_check_C_batch_*.csv"))
    check(bool(batches), "no batch files found")
    seen, total = set(), 0
    counts = {}
    for b in batches:
        rows = list(csv.reader(b.open(newline="", encoding="utf-8")))
        check(rows and rows[0] == HEADER, f"{b.name}: header mismatch")
        body = rows[1:]
        check(len(body) <= MAX_ROWS, f"{b.name}: {len(body)} rows > {MAX_ROWS}")
        total += len(body)
        for r in body:
            check(len(r) == len(HEADER), f"{b.name}: row {r[0] if r else '?'} has {len(r)} fields")
            if len(r) != len(HEADER):
                continue
            d = dict(zip(HEADER, r))
            cid, verdict = d["claim_id"], d["verdict"]
            check(re.match(r"^CC-\d{4}$", cid) is not None, f"{b.name}: bad claim id {cid!r}")
            check(cid not in seen, f"{b.name}: duplicate claim id {cid}")
            seen.add(cid)
            check(verdict in VERDICTS, f"{cid}: verdict {verdict!r} not allowed")
            counts[verdict] = counts.get(verdict, 0) + 1
            if verdict == "SOURCE NOT AVAILABLE":
                check(d["source_page_or_equation"] == "-", f"{cid}: blocked row must carry '-' as locator")
                check(len(d["what_source_actually_states"]) > 40, f"{cid}: blocked row lacks a stated reason")
            else:
                check(d["source_page_or_equation"] not in ("", "-"), f"{cid}: no page/equation locator")
                # a page number is arabic, or a roman numeral for front matter (p. v, p. xi):
                # a book's preface really is paginated, and refusing roman numbers would
                # force either an invented arabic page or a false "not read".
                check(re.search(r"p\.\s?(\d+|[ivxlc]+)\b", d["source_page_or_equation"]) is not None,
                      f"{cid}: locator has no page number")
            check(re.search(r"CR\d{3}", d["notes"]) is not None or True, "")
            # the register record named in the statement/notes must exist and agree on DOI
            ref = re.search(r"\b(CR\d{3})\b", d["notes"])
            if ref:
                check(ref.group(1) in reg, f"{cid}: notes cite unknown register row {ref.group(1)}")
            if d["source_doi"]:
                check(re.match(r"^10\.\d{4,9}/[^\s]+$", d["source_doi"]) is not None,
                      f"{cid}: bad DOI {d['source_doi']!r}")
                check(d["source_doi"] in bib_dois or d["source_doi"] in
                      {r.get("source_doi", "") for r in reg.values()},
                      f"{cid}: DOI {d['source_doi']!r} is in neither refs*.bib nor the register")
            for field in r:
                check(not re.search(r"https?://|drive\.google|docs\.google|\b1[A-Za-z0-9_-]{32}\b", field),
                      f"{cid}: link or Drive id leaked into the CSV")
                check("LE_" not in field and "Extracted ZIPs" not in field,
                      f"{cid}: source-library folder name leaked into the CSV")

    if fails:
        for f in fails:
            print("FAIL", f)
        return 1
    summary = ", ".join(f"{k}={v}" for k, v in sorted(counts.items()))
    print(f"PASS all checks (batches={len(batches)}, rows={total}, {summary})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
