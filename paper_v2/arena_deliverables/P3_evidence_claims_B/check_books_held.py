#!/usr/bin/env python3
"""Checker for the arrival record (`BOOKS_HELD_2026-11-01.*`).

The rule this file exists to enforce is the one that has bitten this project before:
a file name is not an identity.  Every row must carry the evidence that was read off
the copy itself - a title page, a copyright page, an ISBN line - and the states must
be honest about the two arrivals that were not what the wish list asked for.

It checks:

  1. schema, 12 rows, arrival ids 1..12, wishlist ranks unique and inside 1..13;
  2. exactly one rank is missing, and it is rank 12 (Achenbach) - the wish list had 13 rows;
  3. the state vocabulary, and the counts stated in the prose: 10 usable, 1 partial, 1 not-the-book;
  4. the two non-usable rows are the top-ranked item (Eringen and Maugin, rank 1) and Povstenko (rank 4),
     and the prose says in words that BK-15 is still open and coverage stays 34/40;
  5. every usable row is a real book: more than 100 pages, an ISBN (except the 1957 printing, which
     says so), and identity evidence naming a page;
  6. every row's title matches the wish-list title at the same rank - the arrival record cannot drift
     away from the request record;
  7. the two corrections the prose claims (Eringen nonlocal 2002, Muller and Ruggeri print ISBN) are
     present in the row that makes them;
  8. nothing in either file is a link, a drive id, an uploaded file name or a library folder name.

Exit 0 with a line starting with PASS.
"""
import csv
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
CSV = os.path.join(HERE, "BOOKS_HELD_2026-11-01.csv")
MD = os.path.join(HERE, "BOOKS_HELD_2026-11-01.md")
WANT = os.path.join(HERE, "BOOKS_WANTED_2026-11-01.csv")

COLS = ["arrival_id", "wishlist_rank", "title", "authors_printed", "year_printed", "publisher_printed",
        "isbn_printed", "pages", "delivered_state", "identity_evidence", "usable_for", "notes"]
STATES = {"usable", "PARTIAL - Chapter 1 only", "NOT THE BOOK - a one-page review of it"}
leak = re.compile(r"drive\.google|docs\.google|https?://|/folders/|\.zip|\.pdf|z-lib|1lib|"
                  r"LE_PAPERS|Reference List|1[A-Za-z0-9_-]{25,}")

fails = []


def check(name, ok, detail=""):
    print(("  ok   " if ok else "  FAIL ") + name + ("  [" + detail + "]" if detail else ""))
    if not ok:
        fails.append(name)


rows = list(csv.DictReader(open(CSV, newline="", encoding="utf-8")))
md = open(MD, encoding="utf-8").read()
want = {int(r["rank"]): r for r in csv.DictReader(open(WANT, newline="", encoding="utf-8"))}

check("header matches the declared schema", list(rows[0].keys()) == COLS, str(list(rows[0].keys())))
check("12 arrivals, ids 1..12", [int(r["arrival_id"]) for r in rows] == list(range(1, len(rows) + 1)))
ranks = [int(r["wishlist_rank"]) for r in rows]
check("wishlist ranks are unique and inside 1..13",
      len(set(ranks)) == len(ranks) and set(ranks) <= set(range(1, 14)), str(sorted(ranks)))
missing = sorted(set(range(1, 14)) - set(ranks))
check("exactly one wish-list rank is missing, and it is rank 12 (Achenbach)",
      missing == [12] and "Achenbach" in md, str(missing))

states = [r["delivered_state"] for r in rows]
check("states come from the fixed vocabulary", set(states) <= STATES, str(set(states) - STATES))
n_usable = sum(1 for s in states if s == "usable")
n_part = sum(1 for s in states if s.startswith("PARTIAL"))
n_notbook = sum(1 for s in states if s.startswith("NOT THE BOOK"))
check("10 usable / 1 partial / 1 not-the-book, as the prose says",
      (n_usable, n_part, n_notbook) == (10, 1, 1), "%d/%d/%d" % (n_usable, n_part, n_notbook))
check("the prose states the same three numbers",
      "**10**" in md and "**1** - Povstenko" in md and "**1** - Eringen and Maugin" in md)

notbook = [r for r in rows if r["delivered_state"].startswith("NOT THE BOOK")]
part = [r for r in rows if r["delivered_state"].startswith("PARTIAL")]
check("the one-page review is the rank-1 title, Eringen and Maugin",
      notbook and int(notbook[0]["wishlist_rank"]) == 1 and "Electrodynamics of Continua" in notbook[0]["title"])
check("the review is described as a review, with the reviewer and the journal",
      notbook and "review" in notbook[0]["delivered_state"]
      and "Journal of Applied Mechanics" in notbook[0]["identity_evidence"]
      and "Pak" in notbook[0]["identity_evidence"])
check("the partial arrival is Povstenko, chapter 1, and says how many pages",
      part and int(part[0]["wishlist_rank"]) == 4 and part[0]["pages"] == "11")
check("the prose says BK-15 is still open and coverage stays 34/40",
      "BK-15 therefore stays open" in md and "34/40" in md and "not 40/40" in md)

bad_pages = [r["title"] for r in rows if r["delivered_state"] == "usable" and
             not (r["pages"].isdigit() and int(r["pages"]) > 100)]
check("every usable book has more than 100 pages", not bad_pages, str(bad_pages))
check("every row carries identity evidence naming a page",
      all("page" in r["identity_evidence"] or "title page" in r["identity_evidence"] for r in rows),
      str([r["title"] for r in rows if "page" not in r["identity_evidence"]]))
check("every usable book prints an ISBN, except the 1957 printing which says so plainly",
      all(r["isbn_printed"] != "" for r in rows)
      and part and notbook
      and "no ISBN" in [r for r in rows if int(r["wishlist_rank"]) == 13][0]["isbn_printed"])

drift = [r["title"] for r in rows if want.get(int(r["wishlist_rank"]), {}).get("title") != r["title"]]
check("every arrival's title matches the wish list at the same rank", not drift, str(drift))

er = [r for r in rows if int(r["wishlist_rank"]) == 9][0]
check("the Eringen nonlocal year is corrected on the strength of the copyright page",
      "2002" in er["year_printed"] and "2004" in er["notes"])
mr = [r for r in rows if int(r["wishlist_rank"]) == 6][0]
check("Muller and Ruggeri records both the printed and the eBook ISBN",
      "978-1-4612-7460-5" in mr["isbn_printed"] and "978-1-4612-2210-1" in mr["notes"])

check("no link, drive id, file name or library folder in the CSV",
      not leak.search(open(CSV, encoding="utf-8").read()))
check("no link, drive id, file name or library folder in the prose", not leak.search(md))
check("the prose points at the first job that was actually done",
      "ML_TAIL_READ_2026-11-01.md" in md)

if fails:
    print("FAIL %d check(s) failed" % len(fails))
    sys.exit(1)
print("PASS all checks (12 arrivals, %d usable, 1 chapter only, 1 review not the book, "
      "rank 12 outstanding, BK-15 still open, coverage 34/40)" % n_usable)
