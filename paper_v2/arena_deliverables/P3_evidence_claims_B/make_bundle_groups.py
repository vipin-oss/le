#!/usr/bin/env python3
"""Sort the 34 author-request rows by where the PDF has to come from.

Four groups:
  * P01 - LE_PAPERS_P01.zip
  * P02 - LE_PAPERS_P02__was_R3.zip
  * P03 - LE_PAPERS_P03__was_R4.zip
  * separate - not inside any bundle; a fresh download is needed

A row is put in a bundle group only where there is positive evidence that the bundle
really holds *that* paper: the member name is recorded in the library ledger (or in this
project's own archive index) and the ledger's note about that member refers to the same
work.  Where the ledger recorded a member that turned out to be a different paper, the
work is NOT put in that bundle - the bundle does not contain it.

`file_name` is the member to extract (only where known).  `suggested_save_as` is a name to
save a fresh download under, so that it can be matched to the bibliography key later; it is
a suggestion, not something read out of the library.

Usage: python3 make_bundle_groups.py
"""
import csv
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "pdfs_needed_from_author.csv")
OUT = os.path.join(HERE, "pdfs_needed_by_bundle.csv")

BUNDLES = {
    "P01": "LE_PAPERS_P01.zip",
    "P02": "LE_PAPERS_P02__was_R3.zip",
    "P03": "LE_PAPERS_P03__was_R4.zip",
}

# key -> (group, member file inside the bundle)
IN_BUNDLE = {
    "Quintanilla2008a": ("P01", "quintanilla2008.pdf"),
    "Cahill2003": ("P02", "cahill2003.pdf"),
    "SecondSound1970review": ("P02", "2ndSoundSolids.pdf"),
    "Jackson1970": ("P03", "jackson1970.pdf"),
    "Huberman2019": ("P03", "huberman2019.pdf"),
}

# cases where the ledger looked inside a bundle and the member turned out to be a
# different paper - worth saying out loud, because extracting that member does not help
LOOKED_IN = {
    "ChenGurtin1968": ("the ledger tried P03 member gurtin1968.pdf, but that file is Gurtin & "
                       "Pipkin (1968) 'A general theory of heat conduction with finite wave "
                       "speeds' - a different paper, so the bundle does not hold this work"),
    "vanDerMerwe2021": ("the ledger tried P01 member quintanilla2008.pdf, but that file is "
                        "Quintanilla & Racke (2008) on three-phase-lag stability - a different "
                        "paper"),
    "Quintanilla2008": ("do not confuse this with the P01 member also called "
                        "quintanilla2008.pdf: that member is Quintanilla & Racke 2008 "
                        "(Quintanilla2008a). This row is the Applicable Analysis paper with "
                        "DOI 10.1080/00036810802428938"),
}

NOTES = {
    "P01": "extract this member from the bundle (the bundle is 15.5 MB, under the extraction cap)",
    "P02": "extract this member from the bundle (51.8 MB, over the extraction cap here)",
    "P03": "extract this member from the bundle (62.3 MB, over the extraction cap here)",
    "separate": ("not inside any bundle according to the library ledger; a fresh download is "
                 "needed - the name below is only a suggestion for saving it"),
}


def main():
    rows = list(csv.DictReader(open(SRC, newline="")))
    out = []
    for r in rows:
        key = r["bib_key"]
        if key in IN_BUNDLE:
            group, member = IN_BUNDLE[key]
            out.append(dict(group=group, bundle=BUNDLES[group], file_name=member,
                            bib_key=key, claims_blocked=r["claims_blocked"],
                            suggested_save_as="", note=NOTES[group]))
        else:
            out.append(dict(group="separate", bundle="", file_name="",
                            bib_key=key, claims_blocked=r["claims_blocked"],
                            suggested_save_as=key.lower() + ".pdf",
                            note=(LOOKED_IN[key] + " :: " if key in LOOKED_IN else "") +
                                 NOTES["separate"]))

    order = {"P01": 0, "P02": 1, "P03": 2, "separate": 3}
    out.sort(key=lambda r: (order[r["group"]], -int(r["claims_blocked"]), r["bib_key"]))
    for i, r in enumerate(out, 1):
        r["n"] = i

    cols = ["n", "group", "bundle", "file_name", "bib_key", "claims_blocked",
            "suggested_save_as", "note"]
    with open(OUT, "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=cols)
        w.writeheader()
        for r in out:
            w.writerow(r)

    counts = {}
    for r in out:
        counts[r["group"]] = counts.get(r["group"], 0) + 1
    print("wrote pdfs_needed_by_bundle.csv (%d rows): %s" % (
        len(out), ", ".join("%s=%d" % (g, counts.get(g, 0)) for g in ("P01", "P02", "P03", "separate"))))
    return 0


if __name__ == "__main__":
    sys.exit(main())
