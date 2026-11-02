#!/usr/bin/env python3
"""Self-check for the P11 verification batch. Prints PASS and exits 0 only if every gate holds.

Gates
  1. The four deliverables exist: report.md, evidence_P11.csv, missing_P11.csv, README.md.
  2. evidence_P11.csv covers exactly the eleven target keys, at least three rows each, every row
     with a sentence tag in {S1, S2, S3}, a quote of at most 15 words (or the explicit absence
     marker), an equation reference and a page.
  3. refs_P8.csv has one row per bib key (unchanged), and the eleven target rows are at R2/R3 with
     pdf_status READ -- i.e. the upgrade claimed in the report is actually in the data.
  4. missing_P11.csv lists no outstanding item that is simultaneously marked READ.
  5. The report states a verdict for S1, S2 and S3 from the allowed set.
  6. No PDFs in this folder; no Drive identifiers, links or absolute sandbox paths in any
     deliverable text file of this folder; no http(s) URL at all.

    python3 check_p11.py
"""
import csv
import glob
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
P8 = os.path.abspath(os.path.join(HERE, "..", "P8_coverage"))
KEYS = ["Toupin1962", "Toupin1964", "Mindlin1964", "GreenRivlin1964", "Hutson1962", "White1962",
        "Liu2000", "Hussein2014", "Sigalas1992", "Kushwaha1993", "Zubko2013"]
VERDICTS = ("SUPPORTED", "PARTLY SUPPORTED", "NOT SUPPORTED", "SOURCE NOT AVAILABLE")
fails = []


def fail(msg):
    fails.append(msg)


def main():
    for name in ("report.md", "evidence_P11.csv", "missing_P11.csv", "README.md"):
        if not os.path.exists(os.path.join(HERE, name)):
            fail("missing deliverable: %s" % name)
    if fails:
        print("\n".join(fails))
        return 1

    rows = list(csv.DictReader(open(os.path.join(HERE, "evidence_P11.csv"), encoding="utf8")))
    if not rows:
        fail("evidence_P11.csv is empty")
    per_key = {}
    for r in rows:
        k = r["key"]
        per_key[k] = per_key.get(k, 0) + 1
        if k not in KEYS:
            fail("evidence row for unknown key %r" % k)
        if r["sentence"] not in ("S1", "S2", "S3"):
            fail("%s: sentence tag %r not in S1/S2/S3" % (k, r["sentence"]))
        q = (r["quote"] or "").strip()
        if not q:
            fail("%s p%s: empty quote" % (k, r["page"]))
        elif not q.startswith("NOT QUOTABLE"):
            if len(q.split()) > 15:
                fail("%s p%s: quote has %d words (limit 15)" % (k, r["page"], len(q.split())))
            if not r["eq"].strip():
                fail("%s p%s: no equation reference" % (k, r["page"]))
            if not r["page"].strip():
                fail("%s: no page" % k)
        else:
            if not r["note"].strip():
                fail("%s p%s: absence row without a note saying what was counted" % (k, r["page"]))
        if not re.match(r"^(\d+|040802-\d+|abstract)$", r["page"].strip()):
            fail("%s: page %r is not a printed page number" % (k, r["page"]))
    for k in KEYS:
        if per_key.get(k, 0) < 3:
            fail("%s has %d evidence rows (need at least 3)" % (k, per_key.get(k, 0)))
    if sorted(per_key) != sorted(KEYS):
        fail("evidence keys %s != the eleven target keys" % sorted(per_key))
    for sent in ("S1", "S2", "S3"):
        if not any(r["sentence"] == sent for r in rows):
            fail("no evidence row tagged %s" % sent)

    p8csv = os.path.join(P8, "refs_P8.csv")
    p8rows = list(csv.DictReader(open(p8csv, encoding="utf8")))
    by_key = {r["key"]: r for r in p8rows}
    bib_keys = set(re.findall(r"@\w+\{([^,]+),",
                              open(os.path.join(P8, "refs_P8.bib"), encoding="utf8").read()))
    if set(by_key) != bib_keys:
        fail("refs_P8.csv and refs_P8.bib no longer list the same keys")
    for k in KEYS:
        r = by_key.get(k)
        if r is None:
            fail("refs_P8.csv has no row for %s" % k)
            continue
        if r["verification"] not in ("R2", "R3"):
            fail("%s is still %s in refs_P8.csv" % (k, r["verification"]))
        if r["pdf_status"] != "READ":
            fail("%s has pdf_status %r, expected READ" % (k, r["pdf_status"]))
        if "P11" not in r["notes"]:
            fail("%s notes do not record the P11 reading" % k)
        if not re.search(r"p\. ?\d+", r["notes"]):
            fail("%s notes carry no page number" % k)

    miss = list(csv.DictReader(open(os.path.join(HERE, "missing_P11.csv"), encoding="utf8")))
    real = [r for r in miss if r.get("key", "").strip().lower() != "none"]
    for r in real:
        if by_key.get(r["key"], {}).get("pdf_status") == "READ":
            fail("missing_P11.csv lists %s as missing although refs_P8.csv says READ" % r["key"])
    if len(real) > 0:
        fail("%d rows in missing_P11.csv: the eleven were all found" % len(real))

    rep = open(os.path.join(HERE, "report.md"), encoding="utf8").read()
    for sent in ("S1", "S2", "S3"):
        if "### %s" % sent not in rep:
            fail("report.md has no verdict block for %s" % sent)
    for v in ("**PARTLY SUPPORTED**", "**SUPPORTED**"):
        if v not in rep:
            fail("report.md never states %s" % v)
    if not all(any(v in line for v in VERDICTS)
               for line in rep.splitlines() if re.match(r"### S[123]\b", line)):
        fail("a verdict line in report.md carries no verdict from the allowed set")
    for k in KEYS:
        if k not in rep:
            fail("report.md never mentions %s" % k)

    for p in glob.glob(os.path.join(HERE, "*")):
        if p.lower().endswith(".pdf"):
            fail("PDF present in the deliverable folder: %s" % os.path.basename(p))
    for name in os.listdir(HERE):
        p = os.path.join(HERE, name)
        if not os.path.isfile(p) or name.endswith(".py"):
            continue
        txt = open(p, encoding="utf8", errors="replace").read()
        for pat, why in ((r"drive\.google|docs\.google", "Drive link"),
                         (r"https?://", "URL"),
                         (r"/home/user/", "absolute sandbox path"),
                         (r"1[A-Za-z0-9_-]{32}", "Drive id"),
                         (r"\bfile_id\b|folder_id", "drive reference")):
            if re.search(pat, txt, re.I):
                fail("%s contains a %s" % (name, why))

    if fails:
        print("FAIL")
        for f in fails:
            print(" -", f)
        return 1
    print("PASS — %d evidence rows over %d keys; refs_P8 upgraded (R3 %d, R2 %d); no PDFs, no links"
          % (len(rows), len(per_key),
             sum(1 for k in KEYS if by_key[k]["verification"] == "R3"),
             sum(1 for k in KEYS if by_key[k]["verification"] == "R2")))
    return 0


if __name__ == "__main__":
    sys.exit(main())
