#!/usr/bin/env python3
"""Checker for the outstanding-books record (`BOOKS_OUTSTANDING_2026-11-01.*`).

Three things have to stay true for this page to be useful rather than harmful:

  1. it asks for exactly what is still missing - ranks 1, 4 and 12 of the earlier wish list, each with one
     primary row and one or two alternatives, and nothing else;
  2. every DOI-bearing row is DOI-shaped, and the row that has no DOI says so in words and explains why
     (Graff 1975 has no Crossref book record) - no chapter DOI borrowed as a book DOI, no invented ISBN;
  3. nothing on it is already on the shelf: no title here repeats a book recorded as usable in
     BOOKS_HELD_2026-11-01.csv, because a list that re-requests a held book wastes the author's time;
  4. the primaries agree with the earlier wish list - same DOI at the same rank - so the two records cannot
     drift apart;
  5. the prose carries no link, drive id, uploaded file name or library folder name.

Exit 0 with a line starting with PASS.
"""
import csv
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
CSV = os.path.join(HERE, "BOOKS_OUTSTANDING_2026-11-01.csv")
MD = os.path.join(HERE, "BOOKS_OUTSTANDING_2026-11-01.md")
HELD = os.path.join(HERE, "BOOKS_HELD_2026-11-01.csv")
WANT = os.path.join(HERE, "BOOKS_WANTED_2026-11-01.csv")

COLS = ["row_id", "need_rank", "role", "authors", "title", "year", "publisher", "doi", "isbn",
        "verified_where", "buys_what", "difference_from_primary", "claims_or_cases"]
NODOI = "no DOI recorded"
leak = re.compile(r"drive\.google|docs\.google|https?://|/folders/|\.zip|\.pdf|z-lib|1lib|"
                  r"LE_PAPERS|Reference List|1[A-Za-z0-9_-]{25,}")
doiok = re.compile(r"^10\.\d{4,9}/\S+$")

fails = []


def check(name, ok, detail=""):
    print(("  ok   " if ok else "  FAIL ") + name + ("  [" + detail + "]" if detail else ""))
    if not ok:
        fails.append(name)


rows = list(csv.DictReader(open(CSV, newline="", encoding="utf-8")))
md = open(MD, encoding="utf-8").read()

check("header matches the declared schema", list(rows[0].keys()) == COLS, str(list(rows[0].keys())))
check("row ids run 1..n", [int(r["row_id"]) for r in rows] == list(range(1, len(rows) + 1)))
check("exactly three needs, ranks 1, 4 and 12",
      sorted({int(r["need_rank"]) for r in rows}) == [1, 4, 12],
      str(sorted({int(r["need_rank"]) for r in rows})))
prim = [int(r["need_rank"]) for r in rows if r["role"] == "primary"]
check("each need has exactly one primary row", sorted(prim) == [1, 4, 12], str(prim))
check("every need has at least one alternative",
      all(sum(1 for r in rows if int(r["need_rank"]) == k and r["role"] == "alternative") >= 1
          for k in (1, 4, 12)))
check("roles come from the fixed pair", {r["role"] for r in rows} == {"primary", "alternative"},
      str({r["role"] for r in rows}))

bad = [r["title"] for r in rows if r["doi"] != NODOI and not doiok.match(r["doi"])]
check("every DOI-bearing row is DOI-shaped", not bad, str(bad))
nodoi = [r for r in rows if r["doi"] == NODOI]
check("exactly one row has no DOI, and it is Graff 1975", len(nodoi) == 1 and "Graff" in nodoi[0]["authors"],
      str([r["title"] for r in nodoi]))
check("the no-DOI row explains itself: no Crossref book record, and a review that must not be borrowed",
      nodoi and "NO Crossref book record" in nodoi[0]["verified_where"]
      and "must not be quoted as one" in nodoi[0]["verified_where"])
check("the print-only row does not assert an ISBN",
      nodoi and nodoi[0]["isbn"].startswith("no ISBN asserted"))
check("every row records where the record was opened",
      all(len(r["verified_where"].split()) >= 8 for r in rows),
      str([r["title"] for r in rows if len(r["verified_where"].split()) < 8]))

held = {r["title"].lower() for r in csv.DictReader(open(HELD, encoding="utf-8"))
        if r["delivered_state"] == "usable"}
clash = [r["title"] for r in rows if r["title"].lower() in held]
check("no row repeats a book already held and usable", not clash, str(clash))

want = {int(r["rank"]): r for r in csv.DictReader(open(WANT, encoding="utf-8"))}
drift = [r["title"] for r in rows if r["role"] == "primary"
         and (want[int(r["need_rank"])]["title"] != r["title"]
              # DOIs are case-insensitive; Crossref returns the Elsevier ones in lower case
              or want[int(r["need_rank"])]["doi"].lower() != r["doi"].lower())]
check("each primary matches the earlier wish list at the same rank, title and DOI", not drift, str(drift))

check("the prose says no other book is needed", "**no**" in md and "nothing else is needed" in md.lower())
check("the prose states why the two earlier deliveries did not count",
      "one-page review" in md and "Chapter 1 only" in md)
check("the prose gives the BK-15 coverage change", "34/40 -> 40/40" in md)
check("no link, drive id, file name or library folder in the CSV",
      not leak.search(open(CSV, encoding="utf-8").read()))
check("no link, drive id, file name or library folder in the prose", not leak.search(md))
check("the prose ends with the reproducing command", "check_books_outstanding.py" in md)

if fails:
    print("FAIL %d check(s) failed" % len(fails))
    sys.exit(1)
print("PASS all checks (9 rows, 3 needs, %d DOIs verified today, 1 print-only, no held title re-requested)"
      % sum(1 for r in rows if r["doi"] != NODOI))
