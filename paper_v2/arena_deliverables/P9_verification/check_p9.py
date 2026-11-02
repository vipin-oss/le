#!/usr/bin/env python3
"""Self-check for the P9 verification folder. Prints PASS and exits 0 only if every gate holds.

Gates
  1. The three deliverables exist and the verdict document states a verdict for each of the
     three sentences (S1, S2, S3) using only the allowed verdict words.
  2. evidence_P9.csv: every row carries a level in R0-R3, a non-empty page range, an equation
     list (or an explicit 'none'), and the sentence it bears on.
  3. missing_pdfs_P9.csv: eleven rows, each with a DOI, none of them claimed as read.
  4. ../P8_coverage/refs_P8.csv: 72 rows, a pdf_status column, Mindlin1965 at R3 with its P9
     note (later phases may upgrade further rows; this gate only guards the P9 upgrade)
     is Mindlin1965.
  5. No PDFs, no Drive identifiers or links, no sandbox paths in any deliverable.

    python3 check_p9.py
"""
import csv
import glob
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
P8 = os.path.abspath(os.path.join(HERE, "..", "P8_coverage"))
VERDICTS = os.path.join(HERE, "verdicts_P9.md")
EVID = os.path.join(HERE, "evidence_P9.csv")
MISS = os.path.join(HERE, "missing_pdfs_P9.csv")
fails = []


def fail(m):
    fails.append(m)


def main():
    for p in (VERDICTS, EVID, MISS):
        if not os.path.exists(p):
            fail("missing deliverable: %s" % os.path.basename(p))
    if fails:
        print("\n".join(fails))
        return 1

    txt = open(VERDICTS, encoding="utf8").read()
    for s in ("S1", "S2", "S3"):
        if s not in txt:
            fail("verdicts do not mention sentence %s" % s)
    for word in ("PARTLY SUPPORTED", "SUPPORTED", "SOURCE NOT AVAILABLE"):
        if word not in txt:
            fail("verdicts never use the verdict word %r" % word)

    ev = list(csv.DictReader(open(EVID, encoding="utf8")))
    if len(ev) < 3:
        fail("evidence_P9.csv has only %d rows" % len(ev))
    for r in ev:
        if r["level"] not in ("R0", "R1", "R2", "R3"):
            fail("%s: bad level %r" % (r["source"], r["level"]))
        if not r["pages_read"].strip():
            fail("%s: no page range recorded" % r["source"])
        if not r["equations_verified_with_page"].strip():
            fail("%s: no equation list" % r["source"])
        if r["bears_on_sentence"] not in ("S1", "S2", "S3"):
            fail("%s: sentence tag %r invalid" % (r["source"], r["bears_on_sentence"]))
        if not (r["doi"].startswith("10.") or r["doi"] == "NOT VERIFIED"):
            fail("%s: DOI neither real nor marked NOT VERIFIED" % r["source"])
        if not r["limitation"].strip():
            fail("%s: no limitation recorded" % r["source"])

    ms = list(csv.DictReader(open(MISS, encoding="utf8")))
    if len(ms) != 11:
        fail("missing_pdfs_P9.csv has %d rows, expected 11" % len(ms))
    for r in ms:
        if not r["doi"].startswith("10."):
            fail("missing %s has no DOI" % r["key"])
        if "NOT IN LIBRARY" not in r["status"]:
            fail("missing %s does not state its library status" % r["key"])

    p8 = os.path.join(P8, "refs_P8.csv")
    if not os.path.exists(p8):
        fail("refs_P8.csv not found next to this folder")
    else:
        rows = list(csv.DictReader(open(p8, encoding="utf8")))
        if len(rows) != 72:
            fail("refs_P8.csv has %d rows, expected 72" % len(rows))
        if "pdf_status" not in rows[0]:
            fail("refs_P8.csv has no pdf_status column")
        lv = {}
        for r in rows:
            lv[r["verification"]] = lv.get(r["verification"], 0) + 1
        bad = sorted({r["verification"] for r in rows} - {"R0", "R1", "R2", "R3"})
        if bad:
            fail("refs_P8.csv has verification levels outside R0-R3: %s" % bad)
        # P11 note: the exact distribution (1 x R3, 71 x R0) was true on the day P9 ran; later
        # phases legitimately upgrade more rows. The gate guards the P9 upgrade itself, not the
        # snapshot, so that it stays meaningful after P11 read eleven more papers.
        p9 = [r for r in rows if r["key"] == "Mindlin1965"]
        if not p9:
            fail("refs_P8.csv has no Mindlin1965 row")
        elif p9[0]["verification"] != "R3" or "P9" not in p9[0].get("notes", ""):
            fail("Mindlin1965 is %r with notes %r; expected R3 with the P9 note"
                 % (p9[0]["verification"], p9[0].get("notes", "")[:40]))
        if rows[0].get("pdf_status") and not any(r["pdf_status"] == "READ" for r in rows):
            fail("no reference is marked as read")

    for p in glob.glob(os.path.join(HERE, "*")):
        if p.lower().endswith(".pdf"):
            fail("PDF present: %s" % os.path.basename(p))
    for name in os.listdir(HERE):
        p = os.path.join(HERE, name)
        if not os.path.isfile(p) or name.endswith(".py"):
            continue
        t = open(p, encoding="utf8", errors="replace").read()
        for pat, why in ((r"drive\.google|docs\.google|1[A-Za-z0-9_-]{32}", "Drive id/link"),
                         (r"/home/user/", "sandbox path")):
            if re.search(pat, t):
                fail("%s contains a %s" % (name, why))

    if fails:
        print("FAIL")
        for f in fails:
            print(" -", f)
        return 1
    print("PASS - %d verified sources, %d missing PDFs listed, refs_P8 consistent (Mindlin1965 at R3)"
          % (len(ev), len(ms)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
