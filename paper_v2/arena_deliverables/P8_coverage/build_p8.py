#!/usr/bin/env python3
"""Build refs_P8.bib and refs_P8.csv for the P8 coverage extension.

Metadata comes from /home/user/work/p8_data.py, where every record was transcribed from a
Crossref `query.bibliographic` response on 2026-11-02. This script only formats; it invents
nothing. It also asserts that no key collides with the paper's existing bibliography.

    python3 build_p8.py
"""
import csv
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, "/home/user/work")
import p8_data  # noqa: E402

EXISTING = set(open("/home/user/work/p8_existing_keys.txt", encoding="utf8").read().split())

ACCENTS = {"à": r"{\`a}", "á": r"{\'a}", "è": r"{\`e}", "é": r"{\'e}", "ù": r"{\`u}", "ú": r"{\'u}",
           "ö": r"{\"o}", "ü": r"{\"u}", "ä": r"{\"a}", "ñ": r"{\~n}", "ç": r"{\c c}", "ø": r"{\o}"}


def ascii_safe(s):
    for a, b in ACCENTS.items():
        s = s.replace(a, b)
    return s.replace("–", "--").replace("—", "---")


def bib_entry(e):
    authors = " and ".join("%s, %s" % (f, g) for f, g in e["authors"])
    fields = [
        ("author", ascii_safe(authors)),
        ("title", ascii_safe(e["title"])),
        ("journal", ascii_safe(e["journal"])),
        ("volume", e["volume"]),
        ("pages", e["pages"]),
        ("year", e["year"]),
    ]
    if e.get("doi"):
        fields.append(("doi", e["doi"]))
    body = ",\n  ".join("%s = {%s}" % (k, v) for k, v in fields if v)
    return "@%s{%s,\n  %s\n}\n" % (e.get("kind", "article"), e["key"], body)


def main():
    entries = p8_data.AREA_A + p8_data.AREA_B + p8_data.AREA_C + p8_data.AREA_D
    keys = [e["key"] for e in entries]
    assert len(keys) == len(set(keys)), "duplicate keys inside refs_P8"
    clash = sorted(set(keys) & EXISTING)
    assert not clash, "keys clash with the paper's refs.bib: %s" % clash
    for e in entries:
        assert e["doi"].startswith("10."), e["key"]
        assert e["ver"], e["key"]

    bib = os.path.join(HERE, "refs_P8.bib")
    with open(bib, "w", encoding="utf8") as f:
        f.write("% refs_P8.bib — new references proposed for P8 (coverage extension).\n")
        f.write("% Every DOI below was returned by a Crossref query on 2026-11-02; nothing is from memory.\n")
        f.write("% Keys are prefixed-free and checked against paper_v2/overleaf_package.zip refs*.bib (362 keys).\n\n")
        for area, name in ((p8_data.AREA_A, "A"), (p8_data.AREA_B, "B"),
                           (p8_data.AREA_C, "C"), (p8_data.AREA_D, "D")):
            f.write("%% ==================== Area %s ====================\n\n" % name)
            for e in area:
                f.write(bib_entry(e))

    csv_path = os.path.join(HERE, "refs_P8.csv")
    with open(csv_path, "w", newline="", encoding="utf8") as f:
        w = csv.writer(f)
        w.writerow(["key", "area", "authors", "year", "title", "venue", "volume", "pages", "doi",
                    "verification", "fits_section", "inside_or_outside_template",
                    "what_it_shows", "notes"])
        for e in entries:
            w.writerow([
                e["key"], e["area"],
                "; ".join("%s %s" % (f.split()[-1], g) for f, g in e["authors"]),
                e["year"], e["title"], e["journal"], e["volume"], e["pages"], e["doi"],
                e["ver"], e["fits"], e["inout"], e["shows"], e.get("note", ""),
            ])

    from collections import Counter
    by_area = Counter(e["area"] for e in entries)
    by_ver = Counter(e["ver"] for e in entries)
    print("wrote", bib)
    print("wrote", csv_path)
    print("total %d references:" % len(entries), dict(sorted(by_area.items())))
    print("by verification level:", dict(sorted(by_ver.items())))
    print("keys checked against %d existing keys, no clash" % len(EXISTING))


if __name__ == "__main__":
    main()
