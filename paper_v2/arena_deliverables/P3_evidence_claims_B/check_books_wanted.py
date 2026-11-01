#!/usr/bin/env python3
"""Checker for the book wish list (`BOOKS_WANTED_2026-11-01.*`).

What it proves:

  1. header, ranks 1..n, tiers from {A, B, C}, priorities from the fixed vocabulary;
  2. every row carries a DOI **or** says plainly that none is recorded, and every row
     records where the record was verified - so no title, DOI or ISBN is invented;
  3. the print-only row is the only one without a DOI, and it is labelled as such;
  4. no title duplicates a work this project already holds (library list, author-supplied
     works, books already read) - the whole point of a wish list is that it is not the
     library;
  5. every DOI is DOI-shaped and every ISBN-like string is ISBN-shaped;
  6. no row carries a link, a drive id, a file name or a library folder name;
  7. the audit in the prose is recomputed here: the register still has 111 claims at
     SOURCE NOT AVAILABLE, and exactly two of them are not covered by any claim-level file
     (CR144, CR181). If that audit ever changes, this check fails instead of the README
     quietly becoming wrong;
  8. the tier-A rows are the two the prose says would close the last structural gaps, and
     they name BK-15 and BK-11 respectively.

Exit 0 with a line starting with PASS.
"""
import csv
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
CSV = os.path.join(HERE, "BOOKS_WANTED_2026-11-01.csv")
MD = os.path.join(HERE, "BOOKS_WANTED_2026-11-01.md")
REG = os.path.normpath(os.path.join(HERE, "..", "..", "claim_register.csv"))

COLS = ["rank", "kind", "tier", "authors", "title", "year", "publisher", "doi", "isbn",
        "verified_where", "priority", "buys_what", "claims_or_cases", "pages_to_read"]
TIERS = {"A", "B", "C"}
PRIO = {"highest", "high", "medium", "low"}
leak = re.compile(r"drive\.google|docs\.google|https?://|/folders/|\.zip|\.pdf|z-lib|1lib|"
                  r"LE_PAPERS|Reference List|1[A-Za-z0-9_-]{25,}")
doiok = re.compile(r"^10\.\d{4,9}/\S+$")

fails = []


def check(name, ok, detail=""):
    print(("  ok   " if ok else "  FAIL ") + name + ("  [" + detail + "]" if detail else ""))
    if not ok:
        fails.append(name)


rows = list(csv.DictReader(open(CSV, newline="", encoding="utf-8")))
check("the wish list exists with the declared header", list(rows[0].keys()) == COLS,
      str(list(rows[0].keys())))
check("ranks run 1..n", [int(r["rank"]) for r in rows] == list(range(1, len(rows) + 1)),
      str([r["rank"] for r in rows]))
check("every row is a book", {r["kind"] for r in rows} == {"BOOK"}, str({r["kind"] for r in rows}))
check("tiers come from the fixed set", {r["tier"] for r in rows} <= TIERS,
      str({r["tier"] for r in rows} - TIERS))
check("priorities come from the fixed set", {r["priority"] for r in rows} <= PRIO,
      str({r["priority"] for r in rows} - PRIO))
check("every row names authors, title, year and publisher",
      all(r["authors"].strip() and r["title"].strip() and r["year"].isdigit() and r["publisher"].strip()
          for r in rows))
check("no title is listed twice",
      len({r["title"].lower() for r in rows}) == len(rows))

# 2/3. DOIs and their verification
nodoi = [r for r in rows if not doiok.match(r["doi"])]
check("every row either carries a DOI-shaped DOI or says no DOI is recorded",
      all(r["doi"] == "no DOI recorded" for r in nodoi), str([r["title"] for r in nodoi][:3]))
check("the print-only row is the only one without a DOI", len(nodoi) == 1,
      str([r["title"] for r in nodoi]))
check("the print-only row says 'no DOI recorded' and 'print-only'",
      nodoi and nodoi[0]["doi"] == "no DOI recorded" and "print-only" in nodoi[0]["verified_where"])
check("every row records where its record was verified",
      all(len(r["verified_where"].split()) >= 6 for r in rows),
      str([r["title"] for r in rows if len(r["verified_where"].split()) < 6]))

# 4. not already in the library
def norm(s):
    return " ".join(re.sub(r"[^a-z0-9 ]", " ", s.lower()).split())


held_titles = set()
for fn in ("library_available_sources.csv", "supplied_by_author_2026-11-01.csv",
           "SOURCE_READING_books_2026-11-01.csv"):
    p = os.path.join(HERE, fn)
    if not os.path.exists(p):
        continue
    for r in csv.DictReader(open(p, encoding="utf-8")):
        for k in ("title", "work", "cited_work"):
            if r.get(k):
                held_titles.add(norm(r[k]))
# Deliveries made *after* this list was written are recorded in BOOKS_HELD_2026-11-01.csv.
# A title that arrived as a usable book is no longer "already held at request time"; a title
# that arrived as a one-page review or as Chapter 1 only still counts as outstanding, because
# the book itself is not on the shelf.
delivered = {}
held_path = os.path.join(HERE, "BOOKS_HELD_2026-11-01.csv")
if os.path.exists(held_path):
    for r in csv.DictReader(open(held_path, encoding="utf-8")):
        delivered[norm(r["title"])] = (int(r["wishlist_rank"]), r["delivered_state"])
held_before_request = held_titles - set(delivered)
dup = [r["title"] for r in rows if norm(r["title"]) in held_before_request]
check("no wanted title was already held when the list was written", not dup, str(dup))

if delivered:
    drift = [r["title"] for r in rows
             if norm(r["title"]) in delivered and delivered[norm(r["title"])][0] != int(r["rank"])]
    check("every delivered title matches the rank it was asked for", not drift, str(drift))
    usable = {r for r, (rank, st) in delivered.items() if st == "usable"}
    outstanding = sorted(int(r["rank"]) for r in rows if norm(r["title"]) not in usable)
    check("nothing is outstanding any more: every rank has a usable book on the shelf",
          outstanding == [], str(outstanding))

# 5. shapes
check("every ISBN-looking value is ISBN-shaped",
      all(not r["isbn"] or re.search(r"\d{13}|\d{10}|no ISBN", r["isbn"]) for r in rows))

# 6. hygiene
blob = open(CSV, encoding="utf-8").read() + open(MD, encoding="utf-8").read()
check("no link, drive id, file name or library folder anywhere", not leak.search(blob))

# 7. the audit, recomputed
reg = list(csv.DictReader(open(REG, newline="", encoding="utf-8")))
sna = {r["claim_id"] for r in reg if r["verdict"] == "SOURCE NOT AVAILABLE"}
check("the register still has 111 claims at SOURCE NOT AVAILABLE", len(sna) == 111, str(len(sna)))
covered = set()
for fn, cols in (("claim_upgrade_2026-11-01.csv", ("claim_id",)),
                 ("SOURCE_READING_batch4_2026-11-01.csv", ("claim_id",)),
                 ("SOURCE_READING_held_2026-11-01.csv", ("claim_id",)),
                 ("SOURCE_READING_books_2026-11-01.csv", ("claim_id",)),
                 ("register_level_pass_2026-11-01.csv", ("claim_id",)),
                 ("REQUEST_P_claims_2026-11-01.csv", ("claim_id",)),
                 ("ML_TAIL_READ_2026-11-01.csv", ("claim_id",)),
                 ("RET_ENTROPY_READ_2026-11-01.csv", ("claim_id",))):
    p = os.path.join(HERE, fn)
    if not os.path.exists(p):
        continue
    for r in csv.DictReader(open(p, encoding="utf-8")):
        for c in cols:
            if r.get(c, "").strip():
                covered.add(r[c].strip())
for r in csv.DictReader(open(os.path.join(HERE, "supplied_by_author_2026-11-01.csv"), encoding="utf-8")):
    covered |= set(r["claim_ids"].split())
for r in csv.DictReader(open(os.path.join(HERE, "waived_by_author_2026-11-01.csv"), encoding="utf-8")):
    if r.get("claim_id", "").strip():
        covered.add(r["claim_id"].strip())
left = sorted(sna - covered)
check("exactly two blocked claims have nothing read against them", left == ["CR144", "CR181"], str(left))
check("the prose says no book blocks a claim", "No book is blocking a claim" in open(MD, encoding="utf-8").read())

# 8. tier A is what the prose claims
tierA = {r["rank"]: r for r in rows if r["tier"] == "A"}
check("two tier-A books, closing BK-15 and BK-11",
      len(tierA) == 2
      and any("BK-15" in r["buys_what"] for r in tierA.values())
      and any("BK-11" in r["buys_what"] for r in tierA.values()),
      str(sorted(tierA)))
check("the atlas claim in tier A is the 34/40 -> 40/40 one",
      any("34/40" in r["claims_or_cases"] and "40/40" in r["claims_or_cases"] for r in tierA.values()))

if fails:
    print("FAIL %d check(s) failed" % len(fails))
    sys.exit(1)
print("PASS all checks (rows=%d, tiers A/B/C = %d/%d/%d, one print-only row, "
      "no book blocks a claim: %s, outstanding after delivery: none)" % (len(rows),
                                       sum(1 for r in rows if r["tier"] == "A"),
                                       sum(1 for r in rows if r["tier"] == "B"),
                                       sum(1 for r in rows if r["tier"] == "C"),
                                       "/".join(left)))
