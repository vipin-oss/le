#!/usr/bin/env python3
"""Validate gurtin_pipkin_1968.csv.

The paper is not in the library, so nothing about its contents may be asserted.  This
validator makes that limitation structural:

 1. header is the landmark schema plus the two placement columns;
 2. exactly one row, id GP-1968;
 3. DOI is well formed but its status says it was NOT verified on a DOI page;
 4. `verified_from` says SOURCE NOT AVAILABLE (no first page was read);
 5. `in_paper_status` says the manuscript does not cite it - and that is checked
    against the sources themselves: GurtinPipkin1968 must really appear in no .tex file
    of paper_sources.zip;
 6. the placement column names four anchors, each with a real .tex file that exists in
    the source bundle, a line number and a manuscript page number;
 7. no Drive identifier, link or source-library folder name anywhere.

Prints PASS lines and exits 0.
"""
import csv
import re
import sys
import zipfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
CSV = HERE / "gurtin_pipkin_1968.csv"
ZIP = HERE.parents[1] / "paper_sources.zip"

HEADER = ["landmark_id", "Authors", "Title", "Journal_or_publisher", "Volume", "Pages", "Year",
          "DOI", "doi_status", "relevance_one_line", "belongs_in_section", "in_paper_status",
          "verified_from", "suggested_citation_anchors", "anchor_reason"]
fails = []


def check(cond, msg):
    if not cond:
        fails.append(msg)


def main():
    with CSV.open(newline="", encoding="utf-8") as fh:
        rdr = csv.reader(fh)
        header = next(rdr)
        rows = [dict(zip(header, r)) for r in rdr]
    check(header == HEADER, f"header mismatch: {header}")
    print(f"PASS header: {len(header)} columns")

    check(len(rows) == 1, f"expected 1 row, found {len(rows)}")
    r = rows[0]
    check(r["landmark_id"] == "GP-1968", f"unexpected landmark id {r['landmark_id']}")
    print("PASS rows: a single landmark row")

    check(re.match(r"^10\.\d{4,9}/\S+$", r["DOI"]) is not None, f"malformed DOI {r['DOI']!r}")
    check("NOT VERIFIED" in r["doi_status"].upper(), "doi_status does not flag the DOI as unverified")
    print("PASS DOI: well formed and explicitly marked unverified")

    check(r["verified_from"].upper().startswith("SOURCE NOT AVAILABLE"),
          "verified_from does not state that the source is unavailable")
    check("113-126" == r["Pages"] and r["Volume"] == "31" and r["Year"] == "1968",
          "bibliographic values drifted from the bibliography entries")
    print("PASS honesty: the paper was not read, and the row says so")

    with zipfile.ZipFile(ZIP) as z:
        tex = {n: z.read(n).decode("utf-8", "replace") for n in z.namelist()
               if n.endswith(".tex") and n.startswith("sections/")}
        if not tex:
            tex = {n: z.read(n).decode("utf-8", "replace") for n in z.namelist() if n.endswith(".tex")}
    hits = [n for n, t in tex.items() if "GurtinPipkin1968" in t]
    check(not hits, f"the manuscript does cite GurtinPipkin1968 in {hits}, so in_paper_status is wrong")
    check("not cited" in r["in_paper_status"], "in_paper_status does not say the manuscript omits the citation")
    print("PASS citation status: no .tex file in the bundle cites GurtinPipkin1968")

    anchors = re.findall(r"(s[0-9a-z_]+\.tex), line (\d+) \(manuscript p\. (\d+)\)", r["suggested_citation_anchors"])
    check(len(anchors) == 4, f"expected 4 anchors, parsed {len(anchors)}")
    known = set(tex) | {f"sections/{n}" for n in tex} | {n.split("/")[-1] for n in tex}
    for fname, line, page in anchors:
        check(any(fname == k or k.endswith("/" + fname) for k in known), f"anchor file {fname} not in the bundle")
        check(int(line) > 0, f"anchor {fname}: bad line {line}")
        check(int(page) > 0, f"anchor {fname}: bad page {page}")
        # the named line must exist and the file must be the one meant
        real = next((t for n, t in tex.items() if n.endswith("/" + fname) or n == fname), None)
        if real is not None:
            check(int(line) <= real.count("\n") + 1, f"anchor {fname}: line {line} beyond end of file")
    print(f"PASS placement: {len(anchors)} anchors, each with a real file, line and page")

    for field in r.values():
        check(not re.search(r"https?://|drive\.google|docs\.google|\b1[A-Za-z0-9_-]{32}\b", field),
              "link or Drive id leaked into the CSV")
        check("LE_" not in field and "Extracted ZIPs" not in field,
              "source-library folder name leaked into the CSV")
    print("PASS no leaked library identifiers")

    if fails:
        for f in fails:
            print("FAIL", f)
        return 1
    print(f"PASS all checks (rows={len(rows)}, anchors={len(anchors)}, values_read=0)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
