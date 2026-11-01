# Step 14 — the request list re-cut with author names, and Drive swept again

Date: 2026-11-01. Scope: evidence and inventory only, no `.tex`, no `scripts/`.

The question this step answers is the one the author asked: the list is only worth sending if nothing on
it is already in Drive. So the whole list was swept against Drive again, and the list is now printed with
**author names** next to every DOI so each row can be recognised at a glance.

## Result

* **One** of the 39 works was already in Drive: **Kumar, Devi and Sharma 2017**,
  "Damping in microscale modified couple stress thermoelastic circular Kirchhoff plate resonators",
  Applications and Applied Mathematics 12(2), Article 19. It carries **no DOI**, which is why the earlier
  name-and-DOI passes walked past it. It is struck off, recorded in `drive_held_sources_2026-11-01.csv`,
  and it frees claim **CR144**.
* The list therefore stands at **38 works, 39 blocked claims** (Tzou 1997 blocks two).
* 38 rows carry an author field, 35 carry a title (3 say plainly that no title is asserted), 29 carry a
  verified DOI and 9 have none.

## What was searched

Nine name-index query groups over the whole Drive, covering every surname on the list and the distinctive
title words of the works a surname could miss (a book, a paper filed under its subject). About 190 file
hits came back; every file that could plausibly have been one of the 39 was then named exactly and its
first page read — eleven distinct files, two of them duplicate copies. Every hit is listed in
`drive_recheck_2026-11-01.md` with what the page actually says, so a rejection can be checked as easily as
an acceptance.

The one limit is stated in that record too: a file named only by a publisher's PII number or an internal
code cannot be caught by a name search. Those files are covered by the archive inventory, which was built
by opening every file in the bundles, and by the three uploads of the day, each read page by page.

## Files touched

| file | what changed |
|---|---|
| `sources_still_needed_full.csv` | 39 rows -> 38, renumbered, new `authors` column |
| `sources_still_needed_full.md` | mirror of the same list, with authors |
| `drive_held_sources_2026-11-01.csv` | 7 rows -> 8; the Kumar/Devi/Sharma find added |
| `drive_recheck_2026-11-01.md` | new: the sweep, every hit, every rejection, the residual limit |
| `REFERENCE_LIST_still_needed_2026-11-01.pdf` | rebuilt: 3 pages, 38 rows, author column added |
| `check_pdfs_needed.py` | 8 new checks for the authors column, the found work and the sweep record |

Checker: `PASS all checks (needed=1, library=34, findings=3)`, exit 0 — with
`works on the list that the sweep also found in Drive: 0`.

## For the author

The three rows worth sending first, in this order: **Tzou 1997** (the one book left; two claims hang on
it), **Singh, Sarkar and Pal 2020** (J. Heat Transfer 142, DOI 10.1115/1.4047510) and
**Chirita, Ciarletta and Tibullo 2017** (DOI 10.1016/j.ijheatmasstransfer.2017.06.071). One work remains
unreadable rather than missing: the Polizzotto (2001) copy already held has no extractable text, so a
text-readable copy would close CR195 as well.
