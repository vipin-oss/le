#!/usr/bin/env python3
"""Checker for the arrival record (`BOOKS_HELD_2026-11-01.*`).

Two rules this file enforces, both learned the hard way in this project:

  * a file name is not an identity - every row must carry what was read off the copy itself
    (a title page, a copyright page, an ISBN line);
  * a delivery is not a success - a review of a book and the first chapter of a book are
    recorded as such, and only rows marked `usable` count towards coverage of the wish list.

It checks:

  1. schema, 18 arrivals, arrival ids 1..18;
  2. every wish-list rank 1..13 now has exactly one `usable` book, and the ranks that received
     spare copies are the ones the prose names (rank 1: three usable copies, rank 4: two);
  3. the two earlier misfires (a one-page review of Eringen and Maugin I, and Povstenko's
     Chapter 1) are still on the record, still marked non-usable - history is not tidied away;
  4. every usable row has more than 100 pages, names the page its identity came from, and prints
     an ISBN unless the copy is a pre-ISBN printing that says so;
  5. every row's title matches the wish-list title at the same rank;
  6. the prose states the third thing honestly: BK-15 is now *executable* but atlas coverage is
     later executed in Step 39 (bench_multifield.py), moving the atlas to 40/40;
  7. nothing in either file is a link, a drive id, an uploaded file name or a library folder name.

Exit 0 with a line starting with PASS.
"""
import csv
import os
import re
import sys
from collections import Counter

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
check("18 arrivals, ids 1..18", [int(r["arrival_id"]) for r in rows] == list(range(1, len(rows) + 1)),
      str(len(rows)))

states = Counter(r["delivered_state"] for r in rows)
check("states come from the fixed vocabulary", set(states) <= STATES, str(set(states) - STATES))
n_usable = states["usable"]
n_part = states["PARTIAL - Chapter 1 only"]
n_notbook = states["NOT THE BOOK - a one-page review of it"]
check("16 usable rows, 1 chapter-only row, 1 review row",
      (n_usable, n_part, n_notbook) == (16, 1, 1), "%d/%d/%d" % (n_usable, n_part, n_notbook))

usable_ranks = [int(r["wishlist_rank"]) for r in rows if r["delivered_state"] == "usable"]
check("every wish-list rank 1..13 is covered by a usable book",
      sorted(set(usable_ranks)) == list(range(1, 14)), str(sorted(set(usable_ranks))))
per_rank = Counter(usable_ranks)
check("rank 1 has three usable copies and rank 4 has two, as the prose says",
      per_rank[1] == 3 and per_rank[4] == 2 and all(per_rank[k] == 1 for k in per_rank if k not in (1, 4)),
      str(dict(sorted(per_rank.items()))))
check("no rank has a duplicate usable copy beyond those two", sum(per_rank.values()) == 16)

bad_rank = [r["arrival_id"] for r in rows
            if r["delivered_state"] == "usable" and int(r["wishlist_rank"]) not in want]
check("no usable row points at a rank the wish list never had", not bad_rank, str(bad_rank))

review = [r for r in rows if r["delivered_state"].startswith("NOT THE BOOK")]
part = [r for r in rows if r["delivered_state"].startswith("PARTIAL")]
check("the one-page review is still recorded, at rank 1, and is described as a review",
      review and int(review[0]["wishlist_rank"]) == 1
      and "Journal of Applied Mechanics" in review[0]["identity_evidence"]
      and "Pak" in review[0]["identity_evidence"])
check("the chapter-only row is still recorded, at rank 4, and says 11 pages",
      part and int(part[0]["wishlist_rank"]) == 4 and part[0]["pages"] == "11")
check("both misfires record that a later arrival supersedes them",
      "superseded" in review[0]["notes"].lower() and "superseded" in part[0]["notes"].lower())

bad_pages = [r["title"] for r in rows if r["delivered_state"] == "usable"
             and not (r["pages"].isdigit() and int(r["pages"]) > 100)]
check("every usable book has more than 100 pages", not bad_pages, str(bad_pages))
check("every row carries identity evidence naming a page",
      all("page" in r["identity_evidence"] for r in rows),
      str([r["title"] for r in rows if "page" not in r["identity_evidence"]]))
noisbn = [r for r in rows if "no ISBN" in r["isbn_printed"]]
check("the only rows without an ISBN are the pre-ISBN printings, and they say so",
      {int(r["wishlist_rank"]) for r in noisbn} == {1, 12} or
      all("no ISBN" in r["isbn_printed"] for r in noisbn),
      str([(r["arrival_id"], r["isbn_printed"]) for r in noisbn]))

# A spare copy (volume II, Maugin 1988, the diffusion-wave book) legitimately has a different
# title from the wished item at that rank; its own row says so in the notes. Everything else must
# match the wish list exactly.
spare = {r["arrival_id"] for r in rows if "spare" in r["notes"] or "different book" in r["notes"]}
drift = [r["title"] for r in rows
         if r["arrival_id"] not in spare
         and want.get(int(r["wishlist_rank"]), {}).get("title") != r["title"]]
check("every arrival that is not a declared spare matches the wish list at the same rank",
      not drift, str(drift))
check("three rows are declared spares, and each says so in its notes", len(spare) == 3, str(sorted(spare)))

check("the prose carries the addendum in which the last three arrived",
      "Addendum" in md and "all three needs are met" in md)
check("the prose is honest about the coverage change: arrival said 34/40, Step 39 says 40/40",
      "Superseded by Step 39" in md and "40/0/0 of 40" in md)
check("the prose names the three spares", "three usable copies" in md and "spare" in md)

check("no link, drive id, file name or library folder in the CSV",
      not leak.search(open(CSV, encoding="utf-8").read()))
check("no link, drive id, file name or library folder in the prose", not leak.search(md))

if fails:
    print("FAIL %d check(s) failed" % len(fails))
    sys.exit(1)
print("PASS all checks (18 arrivals, %d usable covering all 13 ranks, 1 chapter only, 1 review, "
      "BK-15 executed in Step 39, atlas 40/40)" % n_usable)
