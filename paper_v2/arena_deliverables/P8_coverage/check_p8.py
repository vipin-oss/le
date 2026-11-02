#!/usr/bin/env python3
"""Self-check for the P8 coverage batch. Prints PASS and exits 0 only if every gate holds.

Gates
  1. refs_P8.bib parses; keys unique; no key collides with the paper's own bibliography
     (the 362 keys inside paper_v2/overleaf_package.zip + paper_v2/refs*.bib).
  2. 15-25 references per area, 60-100 in total.
  3. Every entry has authors, year, title, journal, volume, pages, DOI, a verification level
     in R0-R3, a target section in the allowed list, and an inside/outside statement.
  4. refs_P8.csv has exactly one row per bib key, with the same DOI.
  5. pdfs_needed_P8.csv rows all correspond to a bib key and a real DOI.
  6. No PDFs, no Drive identifiers or links, no absolute sandbox paths in the deliverables.

    python3 check_p8.py
"""
import csv
import glob
import os
import re
import sys
import zipfile

HERE = os.path.dirname(os.path.abspath(__file__))
PAPER = os.path.abspath(os.path.join(HERE, "..", ".."))
SECTIONS = {"s04b_flexted", "s08b_aniso", "s10_surface", "s11_interfaces", "s12_size",
            "s13_multiphysics", "s13b_bg", "s15_applications", "s16c_taxonomy", "s17_open"}
fails = []


def fail(msg):
    fails.append(msg)


def bib_entries(path):
    txt = open(path, encoding="utf8").read()
    out = []
    for m in re.finditer(r"@(\w+)\{([^,]+),(.*?)\n\}", txt, re.S):
        fields = dict(re.findall(r"(\w+)\s*=\s*\{(.*?)\},?\s*\n", m.group(3) + "\n"))
        out.append((m.group(2).strip(), fields))
    return out


def existing_keys():
    keys = set()
    for f in glob.glob(os.path.join(PAPER, "refs*.bib")):
        keys |= set(re.findall(r"@\w+\{([^,]+),", open(f, encoding="utf8", errors="replace").read()))
    zp = os.path.join(PAPER, "overleaf_package.zip")
    if os.path.exists(zp):
        with zipfile.ZipFile(zp) as z:
            for n in z.namelist():
                if re.search(r"refs.*\.bib$", n):
                    keys |= set(re.findall(r"@\w+\{([^,]+),",
                                           z.read(n).decode("utf8", errors="replace")))
    return {k.strip() for k in keys}


def main():
    bib = os.path.join(HERE, "refs_P8.bib")
    csvp = os.path.join(HERE, "refs_P8.csv")
    needp = os.path.join(HERE, "pdfs_needed_P8.csv")
    for p in (bib, csvp, needp, os.path.join(HERE, "outlines_P8.md"),
              os.path.join(HERE, "coverage_gaps.md")):
        if not os.path.exists(p):
            fail("missing deliverable: %s" % os.path.basename(p))
    if fails:
        print("\n".join(fails))
        return 1

    ents = bib_entries(bib)
    keys = [k for k, _ in ents]
    if len(keys) != len(set(keys)):
        fail("duplicate keys inside refs_P8.bib")
    clash = sorted(set(keys) & existing_keys())
    if clash:
        fail("keys collide with the paper's bibliography: %s" % clash)
    if not 60 <= len(ents) <= 100:
        fail("total reference count %d outside 60-100" % len(ents))

    per_area = {}
    for k, f in ents:
        for fld in ("author", "year", "title", "journal", "volume", "pages", "doi"):
            if not f.get(fld):
                fail("%s missing field %s" % (k, fld))
        if not f.get("doi", "").startswith("10."):
            fail("%s has no DOI" % k)
        # area and verification level live in the CSV, checked below
    for row in csv.DictReader(open(csvp, encoding="utf8")):
        per_area[row["area"]] = per_area.get(row["area"], 0) + 1
        if row["verification"] not in ("R0", "R1", "R2", "R3"):
            fail("%s bad verification level %r" % (row["key"], row["verification"]))
        if row["fits_section"] not in SECTIONS:
            fail("%s target section %r not in the allowed list" % (row["key"], row["fits_section"]))
        if not re.search(r"inside|outside", row["inside_or_outside_template"].lower()):
            fail("%s has no inside/outside statement" % row["key"])
        if len(row["what_it_shows"].split()) < 8:
            fail("%s has no real 'what it shows' sentence" % row["key"])
    for a in ("a", "b", "c", "d"):
        n = per_area.get(a, 0)
        if not 15 <= n <= 25:
            fail("area %s has %d refs, outside 15-25" % (a, n))

    rows = list(csv.DictReader(open(csvp, encoding="utf8")))
    if sorted(r["key"] for r in rows) != sorted(keys):
        fail("refs_P8.csv and refs_P8.bib do not list the same keys")
    doi_by_key = {k: f.get("doi") for k, f in ents}
    for r in rows:
        if doi_by_key.get(r["key"]) != r["doi"]:
            fail("%s DOI differs between bib and csv" % r["key"])

    for r in csv.DictReader(open(needp, encoding="utf8")):
        if r["key"] not in doi_by_key:
            fail("pdfs_needed row %s not in the bib" % r["key"])
        if not r["doi"].startswith("10."):
            fail("pdfs_needed row %s has no DOI" % r["key"])

    for p in glob.glob(os.path.join(HERE, "*")):
        if p.lower().endswith(".pdf"):
            fail("PDF file present in the deliverable folder: %s" % os.path.basename(p))
    for name in os.listdir(HERE):
        p = os.path.join(HERE, name)
        if not os.path.isfile(p) or name.endswith(".py"):
            continue
        txt = open(p, encoding="utf8", errors="replace").read()
        for pat, why in ((r"drive\.google|docs\.google|/home/user/work|1[A-Za-z0-9_-]{32}", "Drive id/link"),
                         (r"/home/user/", "absolute sandbox path")):
            if re.search(pat, txt):
                fail("%s contains a %s" % (name, why))

    if fails:
        print("FAIL")
        for f in fails:
            print(" -", f)
        return 1
    print("PASS — %d refs, areas %s, all checks green"
          % (len(ents), {a: per_area[a] for a in sorted(per_area)}))
    return 0


if __name__ == "__main__":
    sys.exit(main())
