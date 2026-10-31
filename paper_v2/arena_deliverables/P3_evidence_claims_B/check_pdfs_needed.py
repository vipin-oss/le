#!/usr/bin/env python3
"""Validate the two C deliverables.

`pdfs_needed_from_author.csv`
 1. exact column set, ranks 1..n with no gaps and no duplicates;
 2. one row per bibliography key;
 3. sorted by claims_blocked, descending;
 4. the top-30 cut is respected, and every row held only inside an over-cap archive
    bundle survives it (the author can act on those without hunting);
 5. a DOI is either the literal NOT FOUND or a DOI-shaped string; no URL, no Drive id;
 6. every archive row names both the bundle and the member file.

`library_read_findings.csv`
 7. Task-1 column set, verdict vocabulary, a page or equation for every row,
    a <= 25-word source wording, and a basis for every verdict.

Prints PASS lines and exits 0; FAIL and exit 1 otherwise.  Standard library only.
"""
import csv
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
NEEDED = os.path.join(HERE, "pdfs_needed_from_author.csv")
FIND = os.path.join(HERE, "library_read_findings.csv")
AVAIL = os.path.join(HERE, "library_available_sources.csv")

NEEDED_COLS = ["rank", "bib_key", "authors", "year", "title", "doi", "claims_blocked",
               "claim_ids", "availability", "library_ledger_status",
               "cited_as_in_priority_list"]
FIND_COLS = ["claim_id", "manuscript_location", "manuscript_statement", "cited_source",
             "source_doi", "found_in_library", "verdict", "source_page_or_equation",
             "source_wording_max25words", "what_source_actually_states",
             "verification_level", "notes"]
VERDICTS = {"SUPPORTED", "PARTLY SUPPORTED", "NOT SUPPORTED", "SOURCE NOT AVAILABLE"}
fails = []


def check(name, ok, detail=""):
    print(("PASS " if ok else "FAIL ") + name + ("" if ok else " :: " + detail))
    if not ok:
        fails.append(name)


def main():
    rows = list(csv.DictReader(open(NEEDED, newline="")))
    check("needed header matches the declared schema", list(rows[0].keys()) == NEEDED_COLS,
          str(list(rows[0].keys())))
    ranks = [int(r["rank"]) for r in rows]
    check("ranks run 1..n without gaps", ranks == list(range(1, len(rows) + 1)), str(ranks[:6]))
    keys = [r["bib_key"] for r in rows]
    check("one row per bibliography key", len(set(keys)) == len(keys),
          str([k for k in keys if keys.count(k) > 1][:5]))
    cb = [int(r["claims_blocked"]) for r in rows]
    head = cb[:min(30, len(cb))]
    check("the top-30 block is sorted by claims_blocked, descending",
          head == sorted(head, reverse=True), str(head))
    check("no more than 30 rows carry the cut", all(
        "archive bundle" in r["availability"] for r in rows[30:]) or len(rows) <= 30,
        str([r["bib_key"] for r in rows[30:]])[:200])

    arch = [r for r in rows if "archive bundle" in r["availability"]]
    blob = " ".join(r["availability"] for r in arch)
    want = ["huberman2019.pdf", "jackson1970.pdf", "cahill2003.pdf", "2ndSoundSolids.pdf"]
    missing = [w for w in want if w not in blob]
    check("the four over-cap experimental PDFs are listed", not missing, str(missing))
    check("no other source is lost inside an archive without being named",
          all(re.search(r"member [\w-]+\.pdf", r["availability"]) for r in arch),
          str([r["bib_key"] for r in arch if not re.search(r"member [\w-]+\.pdf",
                                                          r["availability"])]))
    check("every archive row names its bundle and member",
          all(re.search(r"LE_PAPERS_P\d+\S*\.zip", r["availability"])
              and re.search(r"member [\w-]+\.pdf", r["availability"]) for r in arch))

    doiok = re.compile(r"^10\.\d{4,9}/\S+$")
    bad = [r["bib_key"] for r in rows
           if r["doi"] != "NOT FOUND" and not doiok.match(r["doi"])]
    check("every DOI is either NOT FOUND or DOI-shaped", not bad, str(bad[:5]))
    leak = re.compile(r"(drive\.google|docs\.google|https?://|/folders/)")
    bad = [r["bib_key"] for r in rows if leak.search(" ".join(r.values()))]
    check("no URLs, Drive links or folder names", not bad, str(bad[:5]))

    frows = list(csv.DictReader(open(FIND, newline="")))
    check("findings header is the Task-1 schema", list(frows[0].keys()) == FIND_COLS,
          str(list(frows[0].keys())))
    check("findings verdict vocabulary", all(r["verdict"] in VERDICTS for r in frows),
          str({r["verdict"] for r in frows} - VERDICTS))
    check("every finding names a page or equation", all(r["source_page_or_equation"].strip()
                                                        for r in frows))
    long = [r["claim_id"] for r in frows if len(r["source_wording_max25words"].split()) > 27]
    check("source wordings stay within 25 words (+ [...] marker)", not long, str(long))
    check("every finding states what the source actually says",
          all(r["what_source_actually_states"].strip() for r in frows))

    arows = list(csv.DictReader(open(AVAIL, newline="")))
    check("the in-library list has one row per key",
          len({r["bib_key"] for r in arows}) == len(arows))
    print("     needed=%d (archive-blocked=%d), library-held=%d, findings=%d"
          % (len(rows), len(arch), len(arows), len(frows)))

    if fails:
        print("FAIL %d check(s) failed" % len(fails))
        return 1
    print("PASS all checks (needed=%d, library=%d, findings=%d)" % (len(rows), len(arows), len(frows)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
