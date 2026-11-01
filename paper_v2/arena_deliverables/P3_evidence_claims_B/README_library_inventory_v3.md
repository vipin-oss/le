# Library inventory v3 — the whole library re-scanned, one status per file

`library_inventory_v3.csv` replaces the two earlier file-level passes (v2, 37 files, and
part 2, 79 files) with a single table of **117 files**, each carrying an explicit status
from a closed set. It is generated, not retyped: every row is the corresponding row of v2
or part 2, plus one new file, plus a status derived mechanically from what was actually
read on the page.

| status | rows | meaning |
|---|---|---|
| `match` | 63 | a bibliography key was matched from the page (title and/or the DOI printed on it) |
| `no key` | 33 | the first page was read, but no key in the bibliography corresponds to it |
| `mismatch` | 20 | the file holds a different work from the one its name suggests (the reason is in the row) |
| `NOT READ` | 1 | not even the first page has been seen |

## What this re-scan found

* The article folder holds **100 files**. Ninety-nine were already inventoried; **one is
  new**: `nonlocal-continuum-field-theories-2004.pdf`, **29.7 MB**, i.e. over the 25 MB
  in-place read cap. Its title page therefore has **not** been seen and the row says
  `NOT READ`; it must not be identified from its file name alone. (It is the second
  over-cap book in the library; the other is the 30.2 MB `10.1007@978-1-4612-2210-1.pdf`,
  which was already row-less for the same reason.)
* Seventeen inventoried files are **not** in the article folder: they are the withdrawn
  placeholder chapters of *Wave Propagation in Elastic Solids*. They stay in the table,
  because they are files the library really holds, and they stay `mismatch`, because a
  withdrawal notice is not the article.
* No file that existed on 2026-10-26 has disappeared: the folder was re-saved on
  2026-10-31 (every file now carries a 17:39–17:41 timestamp), but the name set is the
  same 99 plus the new book.
* The two corrections of the previous pass are carried forward: `2ndSoundSolids.pdf` is
  keyed to `Chester1963` (it is Chester's *Second Sound in Solids*, not an X-ray paper and
  not a review), and `ezzat2011.pdf` remains a `mismatch` (it is not `Ezzat2011`).

## Why `no key` is not a defect

The 33 key-less files are mostly classical papers that the manuscript's bibliography does
not contain — Mindlin 1965 and 1968, Eringen 1966 and 1972, Puri 1972, Nayfeh 1971, Liu
1972, Achenbach 1968, Crump 1976, Compte 1997, Deresiewicz 1957, Coleman 1964, Dafermos
1968, Sinha 1996/1997, Weideman 2007, Zhang 2003, Majumdar 1993, and the two books that
are only partly readable. They are usable as sources if a claim needs them; they simply do
not correspond to a `\bibitem` yet, and inventing a key for them would be a guess.

Run `python3 check_library_inventory_v3.py`: it fails the build if a `match` row lacks a
key, if any other row carries one, if a status is outside the closed set, if a `mismatch`
or `NOT READ` row states no reason, if the counts drift, or if a link, a Drive id or a
source-library folder name appears anywhere in the table.
