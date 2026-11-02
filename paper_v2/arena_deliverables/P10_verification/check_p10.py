#!/usr/bin/env python3
"""Self-check for the P10 verification folder. Prints PASS and exits 0 only if every gate holds.

Gates
  1. refs_P10.bib parses; the two active entries are Oh2016 and Hobiny2022 with the expected
     DOIs; their keys clash neither with the paper's existing keys nor with refs_P8.bib.
  2. The commented Gupta2026HeatMap block is present, carries the right DOI, and says why it is
     commented (duplicate of an existing refs.bib key).
  3. evidence_P10.csv: three rows; the Gupta row is R3 and lists eq. (2.15) with a page 6.
  4. verdicts_P10.md: names the section file, quotes all three sentences' verdict words, and
     states that the eleven missing PDFs were re-searched.
  5. No PDFs, no Drive identifiers or links, no sandbox paths in the folder.

    python3 check_p10.py
"""
import csv
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
P8 = os.path.abspath(os.path.join(HERE, "..", "P8_coverage"))
BIB = os.path.join(HERE, "refs_P10.bib")
EVID = os.path.join(HERE, "evidence_P10.csv")
VERD = os.path.join(HERE, "verdicts_P10.md")
fails = []


def fail(m):
    fails.append(m)


def active_entries(text):
    out = {}
    for m in re.finditer(r"^@(\w+)\{([^,]+),(.*?)^\}", text, re.S | re.M):
        body = m.group(3)
        out[m.group(2).strip()] = body
    return out


def main():
    for p in (BIB, EVID, VERD):
        if not os.path.exists(p):
            fail("missing deliverable: %s" % os.path.basename(p))
    if fails:
        print("\n".join(fails))
        return 1

    text = open(BIB, encoding="utf8").read()
    ent = active_entries(text)
    if sorted(ent) != ["Hobiny2022", "Oh2016"]:
        fail("active bib keys are %s, expected ['Hobiny2022', 'Oh2016']" % sorted(ent))
    expect = {"Oh2016": "10.1038/srep23630", "Hobiny2022": "10.3390/math10010121"}
    for k, doi in expect.items():
        if k in ent and doi not in ent[k]:
            fail("%s does not carry DOI %s" % (k, doi))

    existing = set()
    ex_path = os.path.join(P8, "existing_keys.txt")
    if os.path.exists(ex_path):
        existing = set(open(ex_path, encoding="utf8").read().split())
    p8keys = set()
    p8csv = os.path.join(P8, "refs_P8.csv")
    if os.path.exists(p8csv):
        p8keys = {r["key"] for r in csv.DictReader(open(p8csv, encoding="utf8"))}
    clash = sorted(set(ent) & (existing | p8keys))
    if clash:
        fail("keys clash with existing bibliography or refs_P8: %s" % clash)

    if "Gupta2026HeatMap" not in text:
        fail("the commented Gupta2026HeatMap entry is missing")
    if "10.1007/s00161-026-01472-6" not in text:
        fail("the Gupta DOI is missing from refs_P10.bib")
    if not re.search(r"already in the paper's refs\.bib", text, re.I):
        fail("refs_P10.bib does not explain why Gupta2026HeatMap is commented")
    if re.search(r"(?m)^\s*@article\{Gupta2026HeatMap", text):
        fail("Gupta2026HeatMap is present as an active entry; it already exists in refs.bib")

    rows = list(csv.DictReader(open(EVID, encoding="utf8")))
    if len(rows) != 3:
        fail("evidence_P10.csv has %d rows, expected 3" % len(rows))
    g = [r for r in rows if r["source"].startswith("Gupta")]
    if not g:
        fail("no Gupta row in evidence_P10.csv")
    else:
        g = g[0]
        if g["level"] != "R3":
            fail("Gupta row level is %r, expected R3" % g["level"])
        if "2.15" not in g["equations_verified_with_page"]:
            fail("Gupta row does not cite eq. (2.15)")
        if not re.search(r"2\.15\s*\(p\.\s*6\)", g["equations_verified_with_page"]):
            fail("Gupta row does not tie eq. (2.15) to page 6")

    vt = open(VERD, encoding="utf8").read()
    for token in ("s12b_wider.tex", "PARTLY SUPPORTED", "SUPPORTED", "SOURCE NOT AVAILABLE",
                  "review-paper-v2", "(2.15)"):
        if token not in vt:
            fail("verdicts_P10.md is missing %r" % token)
    if "re-searched" not in vt and "searched again" not in vt:
        fail("verdicts_P10.md does not record the re-search for the missing PDFs")

    for name in os.listdir(HERE):
        if name.lower().endswith(".pdf"):
            fail("PDF present in the deliverable folder: %s" % name)
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
    print("PASS - refs_P10.bib: 2 active + 1 commented (duplicate of refs.bib); "
          "Gupta 2026 R3 at eq. (2.15) p. 6; verdicts name the section and the re-search")
    return 0


if __name__ == "__main__":
    sys.exit(main())
