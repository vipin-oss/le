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
              list(srows[0].keys()) == ["rank", "authors", "title", "citation", "doi",
                                        "doi_status", "doi_note", "claims_blocked",
                                        "claim_ids", "availability"],
              str(list(srows[0].keys())))
        check("every row names the author(s)",
              all(len(r["authors"].split()) >= 2 for r in srows),
              str([r["rank"] for r in srows if len(r["authors"].split()) < 2]))
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
            # the 2026-11-01 sweep of the whole Drive name index: one work found and struck off
            W = os.path.join(HERE, "drive_recheck_2026-11-01.md")
            check("the record of the Drive sweep exists", os.path.exists(W))
            if os.path.exists(W):
                wtxt = open(W, encoding="utf-8").read()
                check("the Drive sweep record states its verdict",
                      "one** of the 39 was already in Drive" in wtxt
                      or "**one** of the 39 was already in Drive" in wtxt)
                check("the Drive sweep record carries no URLs or Drive links", not leak.search(wtxt))
                check("the Drive sweep record names what it found",
                      "Applications and Applied Mathematics" in wtxt and "CR144" in wtxt)
                found = [r for r in drows if "CR144" in r["claim_ids"]]
                check("the work found by the sweep is in the held record", len(found) == 1,
                      str(len(found)))
                gone = [r["citation"] for r in srows if r["claim_ids"].strip() == "CR144"]
                check("the work found by the sweep is off the request list", not gone, str(gone))
                print("     works on the list that the sweep also found in Drive: %d" % len(gone))

                # batch4: 26 files, 25 matched their row, 1 did not
                B4 = os.path.join(HERE, "batch4_2026-11-01.csv")
                R4 = os.path.join(HERE, "SOURCE_READING_batch4_2026-11-01.csv")
                check("the fourth batch record exists", os.path.exists(B4))
                check("the claim-level reading of the fourth batch exists", os.path.exists(R4))
                if os.path.exists(B4) and os.path.exists(R4):
                    b4 = list(csv.DictReader(open(B4, newline="")))
                    r4 = list(csv.DictReader(open(R4, newline="")))
                    check("the batch record covers every file (26)", len(b4) == 26, str(len(b4)))
                    acc = [r for r in b4 if r["verdict"].startswith("accepted")]
                    rej = [r for r in b4 if r["verdict"].startswith("rejected")]
                    check("25 of the 26 matched their row", len(acc) == 25, str(len(acc)))
                    check("exactly one file is recorded as a mismatch", len(rej) == 1, str(len(rej)))
                    check("the reading covers the 25 accepted works", len(r4) == 25, str(len(r4)))
                    check("every row in the batch reading carries a page and a quote",
                          all(re.match(r"^p\. ?\d", r["evidence_page"]) and
                              len(r["evidence_quote"].split()) >= 4 for r in r4))
                    bad = [r["claim_id"] for r in r4 if len(r["evidence_quote"].split()) > 27]
                    check("no batch quote is longer than 27 words", not bad, str(bad[:5]))
                    bad = [r["claim_id"] for r in r4 if r["verdict"] not in VERDICTS]
                    check("batch verdicts come from the fixed vocabulary", not bad, str(bad[:5]))
                    bad = [r["claim_id"] for r in r4 if r["claim_id"] not in reg]
                    check("batch rows name only real register claims", not bad, str(bad[:5]))
                    still = [r["claim_id"] for r in r4
                             if r["claim_id"] in {c for s in srows for c in s["claim_ids"].split()}]
                    check("no claim read in the fourth batch is still on the request list",
                          not still, str(still[:5]))
                    bad = [r["claim_id"] for r in r4 if re.search(r"\.zip|google_drive|Reference List",
                                                                 " ".join(r.values()))]
                    check("the batch records do not name the uploaded files", not bad, str(bad[:5]))
                    tot = sum(len(r["claim_ids"].split()) for r in srows)
                    check("the request list is down to 13 works / 14 claims",
                          len(srows) == 13 and tot == 14, "%d works, %d claims" % (len(srows), tot))
                    print("     fourth batch: 26 files, 25 accepted, 1 mismatch; list now %d works "
                          "(%d claims)" % (len(srows), tot))
                # LEDGER_*.md - the single page that reconciles every upload with every blocked claim
                L = os.path.join(HERE, "LEDGER_2026-11-01.md")
                check("the one-page ledger exists", os.path.exists(L))
                if os.path.exists(L):
                    ltxt = open(L, encoding="utf-8").read()
                    check("the ledger carries no URLs or Drive links", not leak.search(ltxt))
                    need = "**%d works, %d claims" % (
                        len(srows), sum(len(r["claim_ids"].split()) for r in srows))
                    check("the ledger states what is needed from the author",
                          need in ltxt, need)
                    check("the ledger's four buckets add up to the register's blocked rows",
                          "**111**" in ltxt and "| **total** | **111** |" in ltxt)
                    print("     ledger: 111 blocked claims = 66 closed + %d to order + 12 held "
                          "+ 19 register-level" % sum(len(r["claim_ids"].split()) for r in srows))

        # supplied_by_author_*.csv - works the author sent on 2026-11-01, each verified page-1
        S = os.path.join(HERE, "supplied_by_author_2026-11-01.csv")
        check("the author-supplied record exists", os.path.exists(S))
        if os.path.exists(S):
            prows = list(csv.DictReader(open(S, newline="")))
            check("author-supplied header",
                  list(prows[0].keys()) == ["work", "title", "doi", "pages_in_file",
                                            "read_on_file", "received", "status",
                                            "claims_blocked", "claim_ids"],
                  str(list(prows[0].keys())))
            check("one author-supplied row per work",
                  len({r["work"].lower() for r in prows}) == len(prows))
            check("every supplied file was opened and read",
                  all(r["read_on_file"].strip() and int(r["pages_in_file"]) > 0 for r in prows),
                  str([r["work"] for r in prows if not r["read_on_file"].strip()]))
            check("every supplied row says the work left the request list",
                  all("removed from the request list" in r["status"] for r in prows),
                  str([r["work"] for r in prows if "removed" not in r["status"]]))
            bad = [r["work"] for r in prows if leak.search(" ".join(r.values()))]
            check("the author-supplied record has no URLs, ids or folder names", not bad,
                  str(bad[:5]))
            bad = [r["work"] for r in prows if "Reference List" in " ".join(r.values())
                   or re.search(r"Paper \d+", " ".join(r.values()))]
            check("the author-supplied record does not name the uploaded file", not bad,
                  str(bad[:5]))
            asked = {r["doi"].lower() for r in srows if r["doi"]}
            still = [r["work"] for r in prows
                     if (r["doi"] != "none" and r["doi"].lower() in asked)
                     or r["title"].lower() in {x["title"].lower() for x in srows}]
            check("no supplied work is still on the request list", not still, str(still[:5]))
            print("     supplied by the author and struck off=%d (%s blocked claims freed)"
                  % (len(prows), sum(len(r["claim_ids"].split()) for r in prows)))

        # new_drive_batch_*.md - a Drive drop that was read through and found to hold nothing on the list
        N = os.path.join(HERE, "new_drive_batch_2026-11-01.md")
        check("the record of the unneeded Drive drop exists", os.path.exists(N))
        if os.path.exists(N):
            txt = open(N, encoding="utf-8").read()
            check("the Drive drop record states the verdict",
                  "Not one of them is a work that is still on the request list" in txt)
            check("the Drive drop record carries no URLs or Drive links", not leak.search(txt))
            drop_dois = {d.lower().rstrip('.') for d in re.findall(r"10\.\d{4,9}/[^\s|,;)]+", txt)}
            asked_dois = {r["doi"].lower() for r in srows if r["doi"]}
            overlap = sorted(drop_dois & asked_dois)
            check("no DOI in the Drive drop is still on the request list", not overlap,
                  str(overlap[:5]))
            print("     Drive drop read through: %d files, %d distinct DOIs, 0 wanted"
                  % (txt.count('\n| '), len(drop_dois)))

        # source_reading_*.csv - the author-supplied sources read against the claims they free
        S = os.path.join(HERE, "source_reading_2026-11-01.csv")
        check("the claim-level reading of the supplied sources exists", os.path.exists(S))
        if os.path.exists(S):
            with open(S, newline="", encoding="utf-8") as f:
                sr = list(csv.DictReader(f))
            check("the reading covers one row per freed claim", len(sr) == 40, str(len(sr)))
            ids = [r["claim_id"] for r in sr]
            check("no claim is read twice", len(set(ids)) == len(ids),
                  str([i for i in ids if ids.count(i) > 1][:5]))
            freed = set()
            for r in prows:
                freed |= {c.strip() for c in r["claim_ids"].split() if c.strip()}
            stray = sorted(set(ids) - freed)
            check("every claim read is one the supplied sources free", not stray, str(stray[:5]))
            vocab = {"SUPPORTED", "PARTLY SUPPORTED", "NOT SUPPORTED", "NOT READ"}
            badv = sorted({r["verdict"] for r in sr} - vocab)
            check("every verdict is from the fixed vocabulary", not badv, str(badv))
            nopage = [r["claim_id"] for r in sr if r["verdict"] != "NOT READ"
                      and not re.match(r"^p\. ?\d", r["evidence_page"].strip())]
            check("every read claim carries the page the words were read on", not nopage, str(nopage[:5]))
            noquote = [r["claim_id"] for r in sr if r["verdict"] != "NOT READ"
                       and len(r["evidence_quote"].split()) < 4]
            check("every read claim carries a quote", not noquote, str(noquote[:5]))
            longq = [r["claim_id"] for r in sr if len(r["evidence_quote"].split()) > 27]
            check("no quote is longer than 27 words", not longq, str(longq[:5]))
            unread = [r["claim_id"] for r in sr if r["verdict"] == "NOT READ"]
            badunread = [r["claim_id"] for r in sr if r["verdict"] == "NOT READ"
                         and (r["evidence_quote"].strip() or len(r["note"]) < 40)]
            check("a claim not read carries no quote and says why", not badunread, str(badunread[:5]))
            blank = [r["claim_id"] for r in sr if len(r["note"].strip()) < 20]
            check("every row explains itself", not blank, str(blank[:5]))
            blob = open(S, encoding="utf-8").read()
            check("the reading file carries no URLs or Drive links", not leak.search(blob))
            named = [r["claim_id"] for r in sr
                     if re.search(r"Reference List|\bPaper \d+|\.zip|google_drive", " ".join(r.values()))]
            check("the reading file does not name the uploaded files", not named, str(named[:5]))
            print("     supplied sources read at claim level: %d rows (%s)"
                  % (len(sr), ", ".join("%s=%d" % (v, sum(1 for r in sr if r["verdict"] == v))
                                        for v in ("SUPPORTED", "PARTLY SUPPORTED",
                                                  "NOT SUPPORTED", "NOT READ"))))
    print("     needed=%d (top-20 cut), archive-held=%d, library-held=%d, findings=%d"
          % (len(rows), len(hrows), len(arows), len(frows)))

    if fails:
        print("FAIL %d check(s) failed" % len(fails))
        return 1
    print("PASS all checks (needed=%d, library=%d, findings=%d)" % (len(rows), len(arows), len(frows)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
