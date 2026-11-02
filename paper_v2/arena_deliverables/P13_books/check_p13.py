#!/usr/bin/env python3
"""Self-check for the P13 book-evidence batch. Prints PASS and exits 0 only if every gate holds.

Gates
  1. The five deliverables exist: report.md, evidence.csv, books_status.csv,
     books_inventory.csv, refs_P13.bib.
  2. evidence.csv uses only the six P13 keys, at least three rows per key, a sentence tag in
     {S1..S5, -}, a quote of at most 15 words, a non-empty equation/theorem field, a non-empty
     page field, kind in {quote, absence} and verbatim in {yes, eq, na}.
  3. Every review sentence S1..S5 is covered by at least one evidence row, and the number of
     machine-unverifiable absence rows is reported rather than hidden.
  4. None of the six new keys collides with a key already present in P8_coverage/refs_P8.csv or
     P8_coverage/refs_P8.bib.
  5. books_status.csv has the six rows, flags Auld1973 as a fragment, carries an ISBN for every
     book and a DOI only for the two books whose copyright page prints one.
  6. books_inventory.csv records Nowacki as NOT SUPPLIED.
  7. report.md states a verdict from the allowed set for S1..S5, answers the transfer-function
     question and answers the Quintanilla question.
  8. No PDF in this folder, no Google Drive identifier/link/folder name, no absolute sandbox
     path, no http(s) URL and no .tex file in this folder.

    python3 check_p13.py
"""
import csv
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
P8 = os.path.abspath(os.path.join(HERE, "..", "P8_coverage"))
KEYS = ["Tzou2015", "Eringen1999", "Ignaczak2010", "Deymier2013", "Laude2015", "Auld1973"]
VERDICTS = ("SUPPORTED", "PARTLY SUPPORTED", "PARTLY", "NOT SUPPORTED", "SOURCE NOT AVAILABLE")
DOI_BOOKS = {"Eringen1999", "Deymier2013"}
fails = []


def fail(msg):
    fails.append(msg)


def read(path):
    with open(path, encoding="utf8") as fh:
        return fh.read()


def main():
    for name in ("report.md", "evidence.csv", "books_status.csv", "books_inventory.csv", "refs_P13.bib"):
        if not os.path.exists(os.path.join(HERE, name)):
            fail("missing deliverable: %s" % name)
    if fails:
        print("\n".join(fails))
        return 1

    # ---- gate 2 and 3: evidence table
    rows = list(csv.DictReader(open(os.path.join(HERE, "evidence.csv"), encoding="utf8")))
    if not rows:
        fail("evidence.csv is empty")
    need = {"key", "claim", "quote", "eq_theorem", "page", "sentence", "kind", "verbatim"}
    if not need.issubset(set(rows[0].keys())):
        fail("evidence.csv header missing columns: %s" % sorted(need - set(rows[0].keys())))
    per_key, sentences, absence = {}, set(), 0
    for r in rows:
        k = r["key"]
        per_key[k] = per_key.get(k, 0) + 1
        if k not in KEYS:
            fail("evidence row for unknown key %r" % k)
        if r["sentence"] != "-":
            if r["sentence"] not in ("S1", "S2", "S3", "S4", "S5"):
                fail("%s: sentence tag %r not in S1..S5/-" % (k, r["sentence"]))
            else:
                sentences.add(r["sentence"])
        q = (r["quote"] or "").strip()
        if not q:
            fail("%s p%s: empty quote" % (k, r["page"]))
        elif len(q.split()) > 15:
            fail("%s p%s: quote has %d words (limit 15)" % (k, r["page"], len(q.split())))
        if not (r["eq_theorem"] or "").strip():
            fail("%s p%s: empty equation/theorem field" % (k, r["page"]))
        if not (r["page"] or "").strip():
            fail("%s: empty page field" % k)
        if r["kind"] not in ("quote", "absence"):
            fail("%s p%s: kind %r not in {quote, absence}" % (k, r["page"], r["kind"]))
        if r["verbatim"] not in ("yes", "eq", "na"):
            fail("%s p%s: verbatim %r not in {yes, eq, na}" % (k, r["page"], r["verbatim"]))
        if r["kind"] == "absence":
            absence += 1
            if r["verbatim"] != "na":
                fail("%s: absence row must carry verbatim=na" % k)
    for k in KEYS:
        if per_key.get(k, 0) < 3:
            fail("%s has %d evidence rows (need >= 3)" % (k, per_key.get(k, 0)))
    for s in ("S1", "S2", "S3", "S4", "S5"):
        if s not in sentences:
            fail("review sentence %s has no evidence row" % s)

    # ---- gate 4: key collisions with the earlier batches
    old = set()
    p8csv = os.path.join(P8, "refs_P8.csv")
    if os.path.exists(p8csv):
        old |= {r["key"] for r in csv.DictReader(open(p8csv, encoding="utf8"))}
    p8bib = os.path.join(P8, "refs_P8.bib")
    if os.path.exists(p8bib):
        old |= set(re.findall(r"@\w+\{([^,]+),", read(p8bib)))
    for k in KEYS:
        if k in old:
            fail("key %s collides with an existing key in P8_coverage" % k)

    # ---- gate 5: book status
    status = list(csv.DictReader(open(os.path.join(HERE, "books_status.csv"), encoding="utf8")))
    got = {r["key"] for r in status}
    if got != set(KEYS):
        fail("books_status.csv keys %s != %s" % (sorted(got), sorted(KEYS)))
    for r in status:
        if not (r.get("isbn") or "").strip():
            fail("%s: no printed ISBN recorded" % r["key"])
        has_doi = bool((r.get("doi") or "").strip())
        if has_doi and r["key"] not in DOI_BOOKS:
            fail("%s: DOI recorded but no DOI is printed in that book" % r["key"])
        if not has_doi and r["key"] in DOI_BOOKS:
            fail("%s: printed DOI is missing from books_status.csv" % r["key"])
        if not (r.get("completeness") or "").strip():
            fail("%s: empty completeness field" % r["key"])
        if r["key"] == "Auld1973" and "fragment" not in r["completeness"].lower():
            fail("Auld1973 is not flagged as a fragment (only Volume I was supplied)")
        if r["key"] != "Auld1973" and "fragment" in r["completeness"].lower():
            fail("%s is flagged as a fragment; say so in the report as well" % r["key"])

    # ---- gate 6: inventory keeps the missing book missing
    inv = list(csv.DictReader(open(os.path.join(HERE, "books_inventory.csv"), encoding="utf8")))
    now = [r for r in inv if r["key"].lower().startswith("nowacki")]
    if not now:
        fail("books_inventory.csv has no Nowacki row")
    else:
        if "NOT SUPPLIED" not in (now[0]["status"] or "").upper():
            fail("Nowacki is not marked NOT SUPPLIED")

    # ---- gate 7: report answers the questions
    report = read(os.path.join(HERE, "report.md"))
    for s in ("S1", "S2", "S3", "S4", "S5"):
        line = [ln for ln in report.splitlines() if ln.strip().startswith("| %s " % s)]
        if not line:
            fail("report.md has no verdict row for %s" % s)
        elif not any(v in line[0] for v in VERDICTS):
            fail("report.md verdict row for %s carries no allowed verdict" % s)
    for token in ("transfer function", "Quintanilla"):
        if token.lower() not in report.lower():
            fail("report.md does not answer the %r question" % token)

    # ---- gate 8: hygiene
    for name in sorted(os.listdir(HERE)):
        if name.lower().endswith(".pdf"):
            fail("PDF in the deliverable folder: %s" % name)
        if name.lower().endswith(".tex"):
            fail("TeX file in the deliverable folder: %s" % name)
    forbidden = ("google_drive", "drive.google.com", "docs.google.com", "http://", "https://",
                 "/home/user", "My Drive")
    for name in ("report.md", "evidence.csv", "books_status.csv", "books_inventory.csv", "refs_P13.bib"):
        text = read(os.path.join(HERE, name))
        for bad in forbidden:
            if bad in text:
                fail("%s contains forbidden token %r" % (name, bad))
        if re.search(r"\b[A-Za-z0-9_-]{33,}\b", text) and name != "refs_P13.bib":
            fail("%s contains a long opaque token that may be an identifier" % name)

    if fails:
        print("\n".join(fails))
        return 1
    print("P13 book evidence: %d rows over %d books (%d absence rows that need the book text to "
          "confirm by eye); sentences S1-S5 all covered." % (len(rows), len(per_key), absence))
    print("PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
