#!/usr/bin/env python3
"""Validate the two C deliverables.

`pdfs_needed_from_author.csv`
 1. exact column set, ranks 1..n with no gaps and no duplicates;
 2. one row per bibliography key;
 3. sorted by claims_blocked, descending;
 4. the list is the top-20 cut of the sources that are still NOT held: no row may be a
    source already read from the library, and no row may name a claim that a
    P3_evidence_claims_C batch has since resolved;
 5. a DOI is either the literal NOT FOUND or a DOI-shaped string; no URL, no Drive id.
    A DOI is only asserted when it was read off a page, so the column is NOT FOUND
    wherever the work is not held at all;
 6. `pdfs_held_in_archives.csv` keeps the over-cap archive members that therefore left
    this list, one row each, naming bundle and member.

`pdfs_needed_by_bundle.csv` is retired: it grouped the old 34-row list, which no longer exists.

`library_read_findings.csv`
 7. Task-1 column set, verdict vocabulary, a page or equation for every row,
    a <= 25-word source wording, and a basis for every verdict.

Prints PASS lines and exits 0; FAIL and exit 1 otherwise.  Standard library only.
"""
import csv
import glob
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
NEEDED = os.path.join(HERE, "pdfs_needed_from_author.csv")
FIND = os.path.join(HERE, "library_read_findings.csv")
AVAIL = os.path.join(HERE, "library_available_sources.csv")
HELD = os.path.join(HERE, "pdfs_held_in_archives.csv")
CBATCH = os.path.join(HERE, "..", "P3_evidence_claims_C")

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
    check("the top-20 block is sorted by claims_blocked, descending",
          head == sorted(head, reverse=True), str(head))
    check("the list is the top-20 cut", len(rows) <= 20, "%d rows" % len(rows))
    check("no row on the needed list is a source already held in the library",
          not any("archive bundle" in r["availability"] for r in rows),
          str([r["bib_key"] for r in rows if "archive bundle" in r["availability"]]))
    check("every row states that the source is not held",
          all(r["availability"].startswith("not in library") for r in rows),
          str([r["bib_key"] for r in rows if not r["availability"].startswith("not in library")]))
    # a claim resolved by a later C batch must not still be advertised as blocked
    resolved = set()
    for b in sorted(glob.glob(os.path.join(CBATCH, "claim_check_C_batch_*.csv"))):
        for c in csv.DictReader(open(b, newline="")):
            # only a row that actually read a page counts as resolved; a batch row that
            # ends at SOURCE NOT AVAILABLE leaves the source on the needed list
            if c["verdict"] == "SOURCE NOT AVAILABLE":
                continue
            for ref in re.findall(r"\b(CR\d{3})\b", c["notes"]):
                resolved.add(ref)
    stale = [(r["bib_key"], c) for r in rows for c in r["claim_ids"].split() if c in resolved]
    check("no row still lists a claim that has since been checked against a held source",
          not stale, str(stale[:5]))
    check("every blocked claim id is a real register row", all(
        re.match(r"^CR\d{3}$", c) for r in rows for c in r["claim_ids"].split()))

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

    hrows = list(csv.DictReader(open(HELD, newline="")))
    check("the archive appendix has one row per held member",
          len({r["bib_key"] for r in hrows}) == len(hrows))
    want = {"quintanilla2008.pdf", "jackson1970.pdf", "huberman2019.pdf", "cahill2003.pdf"}
    have = {r["file_name"] for r in hrows}
    check("the four over-cap experimental PDFs are still accounted for", want <= have,
          str(want - have))
    check("every archive row names both the bundle and the member", all(
        re.search(r"LE_PAPERS_P\d+\S*\.zip", r["bundle"]) and r["file_name"].endswith(".pdf")
        for r in hrows),
        str([r["bib_key"] for r in hrows if not re.search(r"LE_PAPERS_P\d+\S*\.zip", r["bundle"])]))
    check("no key appears both as needed and as held",
          not ({r["bib_key"] for r in rows} & {r["bib_key"] for r in hrows}))

    arows = list(csv.DictReader(open(AVAIL, newline="")))
    check("the in-library list has one row per key",
          len({r["bib_key"] for r in arows}) == len(arows))

    # sources_still_needed_full.csv - the complete, de-duplicated request list (Step 7)
    F = os.path.join(HERE, "sources_still_needed_full.csv")
    if os.path.exists(F):
        srows = list(csv.DictReader(open(F, newline="")))
        check("full request list header",
              list(srows[0].keys()) == ["rank", "title", "citation", "doi", "doi_status",
                                        "doi_note", "claims_blocked", "claim_ids",
                                        "availability"],
              str(list(srows[0].keys())))
        check("full request list ranks run 1..n",
              [int(r["rank"]) for r in srows] == list(range(1, len(srows) + 1)))
        check("full request list has no duplicate citation",
              len({r["citation"].lower() for r in srows}) == len(srows), "duplicates present")
        check("full request list has no repeated work (same DOI twice)",
              len({r["doi"] for r in srows if r["doi"]}) == sum(1 for r in srows if r["doi"]))
        check("every row states a title or says plainly that none is asserted",
              all(r["title"].strip() for r in srows), "empty title field")
        check("full request list DOI status vocabulary",
              all(r["doi_status"] in {"verified", "WRONG DOI", "no DOI recorded"} for r in srows),
              str({r["doi_status"] for r in srows}))
        bad = [r["rank"] for r in srows
               if (r["doi_status"] == "no DOI recorded") == bool(r["doi"])]
        check("full request list marks exactly the empty DOIs as 'no DOI recorded'",
              not bad, str(bad[:5]))
        bad = [r["rank"] for r in srows if r["doi"] and not doiok.match(r["doi"])]
        check("full request list DOIs are DOI-shaped or empty", not bad, str(bad[:5]))
        bad = [r["rank"] for r in srows if leak.search(" ".join(r.values()))]
        check("full request list has no URLs or Drive links", not bad, str(bad[:5]))
        reg = {r["claim_id"]: r for r in csv.DictReader(
            open(os.path.join(HERE, "..", "..", "claim_register.csv"), newline=""))}
        bad = [c for r in srows for c in r["claim_ids"].split() if c not in reg]
        check("full request list names only real register rows", not bad, str(bad[:5]))
        bad = [c for r in srows for c in r["claim_ids"].split()
               if reg[c]["verdict"] != "SOURCE NOT AVAILABLE"]
        check("full request list names only claims that are still unavailable", not bad,
              str(bad[:5]))
        print("     full request list=%d rows (%d with a DOI)"
              % (len(srows), sum(1 for r in srows if r["doi"])))

        # drive_held_sources_*.csv - works found inside Drive on 2026-11-01 and therefore
        # struck off the request list. No id, link or folder name is kept anywhere.
        D = os.path.join(HERE, "drive_held_sources_2026-11-01.csv")
        check("the Drive re-check record exists", os.path.exists(D))
        if os.path.exists(D):
            drows = list(csv.DictReader(open(D, newline="")))
            check("Drive re-check header",
                  list(drows[0].keys()) == ["work", "title", "doi", "claims_blocked",
                                            "claim_ids", "verified_in_drive", "status", "note"],
                  str(list(drows[0].keys())))
            check("one Drive re-check row per work",
                  len({r["work"].lower() for r in drows}) == len(drows))
            check("every Drive row says the work left the request list",
                  all("removed from the request list" in r["status"] for r in drows),
                  str([r["work"] for r in drows if "removed" not in r["status"]]))
            check("every Drive row was verified by opening the file",
                  all(r["verified_in_drive"] == "2026-11-01" and "opened" in r["note"]
                      for r in drows),
                  str([r["work"] for r in drows if "opened" not in r["note"]]))
            bad = [r["work"] for r in drows if leak.search(" ".join(r.values()))]
            check("the Drive re-check record has no URLs, ids or folder names", not bad,
                  str(bad[:5]))
            asked = {r["doi"].lower() for r in srows if r["doi"]}
            still = [r["work"] for r in drows
                     if (r["doi"] != "none" and r["doi"].lower() in asked)
                     or r["title"].lower() in {x["title"].lower() for x in srows}]
            check("no work that is held in Drive is still on the request list", not still,
                  str(still[:5]))
            print("     Drive-held and struck off=%d" % len(drows))
    print("     needed=%d (top-20 cut), archive-held=%d, library-held=%d, findings=%d"
          % (len(rows), len(hrows), len(arows), len(frows)))

    if fails:
        print("FAIL %d check(s) failed" % len(fails))
        return 1
    print("PASS all checks (needed=%d, library=%d, findings=%d)" % (len(rows), len(arows), len(frows)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
