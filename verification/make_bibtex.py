#!/usr/bin/env python3
"""
B5d — convert LITERATURE_BASE.csv (and optionally REFERENCE_AUDIT.csv) to BibTeX.

What it does
-----------
1. Reads verification/LITERATURE_BASE.csv.
2. Builds a stable key:  FamilyYearWord   e.g. Eringen1983Differential
   - first author's family name, no accents/punctuation
   - 4-digit year
   - first informative word of the title (skips stop words)
   - de-duplicates with a, b, c ... if two records collide
3. Checks duplicate DOIs and duplicate keys, and reports both.
4. Prints (and optionally writes) the records that have NO DOI.
5. --enrich fetches the missing author lists from Crossref by DOI.

The --enrich path needs network access to api.crossref.org. If the sandbox blocks
it (as this one does), run the script where Crossref is reachable, or paste the
output of a Crossref query into the CSV's `authors` column by hand.

Usage
-----
    python make_bibtex.py                        # report + write literature_base.bib
    python make_bibtex.py --out custom.bib
    python make_bibtex.py --enrich               # fetch authors for blank rows first
    python make_bibtex.py --check-only           # no file written
"""
import argparse
import csv
import os
import re
import sys
import unicodedata

HERE = os.path.dirname(os.path.abspath(__file__))
CSV_PATH = os.path.join(HERE, "LITERATURE_BASE.csv")

STOP = {"a", "an", "on", "of", "the", "in", "for", "to", "and", "with", "some", "new",
        "towards", "toward", "from", "by", "at", "as", "is", "are"}


def ascii_word(s: str) -> str:
    s = unicodedata.normalize("NFKD", s)
    s = "".join(c for c in s if not unicodedata.combining(c))
    return re.sub(r"[^A-Za-z]", "", s)


def first_family(authors: str) -> str:
    if not authors:
        return "Anon"
    first = authors.split(";")[0].strip()
    fam = first.split()[-1] if first.split() else first
    return ascii_word(fam) or "Anon"


def title_word(title: str) -> str:
    for w in re.split(r"[^A-Za-z]+", title):
        if w and w.lower() not in STOP:
            return ascii_word(w).capitalize()
    return "Untitled"


def make_key(rec):
    return f"{first_family(rec['authors'])}{rec['year']}{title_word(rec['title'])}"


def fmt_authors(a: str) -> str:
    """'Biot' or 'Green; Naghdi' -> 'Biot, M. A.' style is not reconstructible from
    family names alone, so emit 'Family, X.' placeholders only when a full name is known."""
    parts = [p.strip() for p in a.split(";") if p.strip()]
    return " and ".join(parts)


def enrich_from_crossref(records, quiet=False):
    """Fill blank author fields by asking Crossref for the DOI."""
    import json
    import time
    import urllib.parse
    import urllib.request

    ua = "BraveBibtex/1.0 (mailto:verifier@example.org)"
    filled = 0
    for r in records:
        if r["authors"].strip() or not r["DOI"]:
            continue
        url = "https://api.crossref.org/works/" + urllib.parse.quote(r["DOI"])
        try:
            req = urllib.request.Request(url, headers={"User-Agent": ua})
            with urllib.request.urlopen(req, timeout=30) as fh:
                m = json.loads(fh.read().decode())["message"]
            names = []
            for au in m.get("author", []):
                fam = au.get("family") or au.get("name") or ""
                giv = au.get("given", "")
                names.append(f"{fam}, {giv}".strip(", "))
            if names:
                r["authors"] = "; ".join(names)
                filled += 1
        except Exception as exc:                      # noqa: BLE001
            if not quiet:
                print(f"  ! {r['DOI']}: {exc}", file=sys.stderr)
        time.sleep(0.2)
    return filled


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--csv", default=CSV_PATH)
    ap.add_argument("--out", default=os.path.join(HERE, "literature_base.bib"))
    ap.add_argument("--enrich", action="store_true")
    ap.add_argument("--check-only", action="store_true")
    args = ap.parse_args()

    with open(args.csv, encoding="utf-8") as fh:
        records = list(csv.DictReader(fh))
    print(f"read {len(records)} records from {os.path.basename(args.csv)}")

    # ---- duplicate DOIs
    seen_doi, dup_doi = {}, []
    for r in records:
        d = r["DOI"].strip().lower()
        if not d:
            continue
        if d in seen_doi:
            dup_doi.append((d, seen_doi[d], r["id"]))
        else:
            seen_doi[d] = r["id"]
    print(f"duplicate DOIs: {len(dup_doi)}")
    for d, a, b in dup_doi:
        print(f"  {d}  ({a} / {b})")

    # ---- keys
    used, keys = {}, []
    for r in records:
        base = make_key(r)
        key = base
        n = 0
        while key.lower() in used:
            n += 1
            key = base + chr(ord("a") + n - 1)
        used[key.lower()] = r["id"]
        keys.append(key)
    print(f"keys generated: {len(keys)} (unique: {len(set(keys))})")

    # ---- no-DOI records
    nodoi = [r for r in records if not r["DOI"].strip()]
    print(f"records without DOI: {len(nodoi)}")
    for r in nodoi:
        print(f"  {r['id']}  {r['authors'][:30]:30s} {r['year']}  {r['title'][:60]}")

    blank = [r for r in records if not r["authors"].strip()]
    print(f"records without authors: {len(blank)}"
          + ("   (run with --enrich to fill from Crossref)" if blank else ""))

    if args.enrich and blank:
        n = enrich_from_crossref(records)
        print(f"enriched {n} author lists from Crossref")

    if args.check_only:
        return 0

    with open(args.out, "w", encoding="utf-8") as fh:
        fh.write("% generated by make_bibtex.py from LITERATURE_BASE.csv\n")
        fh.write("% keys are FamilyYearWord; verify before submission\n\n")
        for r, key in zip(records, keys):
            fh.write(f"@article{{{key},\n")
            if r["authors"].strip():
                fh.write(f"  author  = {{{fmt_authors(r['authors'])}}},\n")
            fh.write(f"  title   = {{{r['title']}}},\n")
            fh.write(f"  journal = {{{r['venue']}}},\n")
            fh.write(f"  year    = {{{r['year']}}},\n")
            if r["DOI"].strip():
                fh.write(f"  doi     = {{{r['DOI']}}},\n")
            fh.write(f"  note    = {{type: {r['type']}; area: {r['sub_area']}}}\n")
            fh.write("}\n\n")
    print(f"wrote {args.out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
