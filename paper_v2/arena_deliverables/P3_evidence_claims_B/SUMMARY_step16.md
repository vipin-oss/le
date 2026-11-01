# Step 16 — the fourth batch: 26 files, 25 matched, list down to 13 works

Date: 2026-11-01. Scope: evidence and inventory only, no `.tex`, no `scripts/`.

The author added one more collection to Drive and said the remaining papers could not be found. Every
file in it was downloaded, opened, and identified from the page itself — the printed journal, volume,
page or DOI — never from the file name. Twenty-five of the twenty-six turned out to be works on the
request list; one did not.

## Result

* **25 works closed**, and with them 25 blocked claims. The list falls from 38 works to **13 works
  (14 claims)**.
* **One file did not match its row**: a two-page Journal of Thermal Stresses item
  (DOI 10.1080/01495738808961927) was sent for the **Nowacki (1975)** book. That row stays on the list,
  unchanged and unexplained by the batch.
* Verdicts across the 25: **23 SUPPORTED, 2 PARTLY SUPPORTED**, none unsupported, none unreadable.

The two PARTLY rows are worth the author's eye:

1. **Askes and Aifantis 2006** — the sentence credits the pair (2006, 2011) with a gradient of inertia as
   well as of strain. The 2011 paper says it outright ("higher-order spatial derivatives of strains,
   stresses and/or accelerations"); the 2006 paper is a unification of gradient formats and contains
   neither the word "inertia" nor "acceleration" anywhere in its eight pages. The wording is safe if it
   is carried by the pair, not by the 2006 paper alone.
2. **Biswas 2020** — the sentence says the Stroh formalism is the route taken for piezothermoelastic
   layers and half-spaces. This paper does treat that geometry, but it derives a secular equation from
   potential functions and its own reference list credits "Stroh analysis" to a different paper by the
   same author. So the geometry is supported, the method attribution is not.

## What is left

13 works / 14 claims, of which two are books and the rest are pre-DOI or hard-to-locate papers:
Podlubny 1999, Boley and Weiner 1960, Born and von Karman 1912, Carlson 1972, Cattaneo 1948,
Danilovskaya 1950, Kumar and Tomar 2024, Kumar/Gupta/Pathania/Barak 2025, Nowacki 1975,
Singh/Sarkar/Pal 2020, Tzou 1997, Vernotte 1958, Wang and Li 2025. Plus the one replacement copy:
Polizzotto (2001), whose held copy has no extractable text.

## Files touched

| file | what it is |
|---|---|
| `batch4_2026-11-01.csv` | 26 rows: what each file's page printed, and whether it matched |
| `SOURCE_READING_batch4_2026-11-01.csv` | 25 rows: claim, verdict, page, quote, what the source states, action for the author |
| `sources_still_needed_full.csv` / `.md` | re-cut to 13 works, ranks renumbered |
| `REFERENCE_LIST_still_needed_2026-11-01.pdf` | rebuilt: one page, 13 rows, author + title + DOI |
| `LEDGER_2026-11-01.md` | 103 files read, 92 works identified, 66 claims closed, 111 = 66 + 14 + 12 + 19 |
| `check_pdfs_needed.py` | 11 new checks for the batch, its reading, the re-cut list and the ledger |

Checker: `PASS all checks (needed=1, library=34, findings=3)`, exit 0.
