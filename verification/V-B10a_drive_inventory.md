# V-B10a — Drive inventory of the paper library (370 files, 24 folders)

**Order:** `control/BRAVE_B10.md` (B10a), read at `origin/claude/control` `a0ace86` on 2026-10-22.
**Deliverable:** `verification/DRIVE_INVENTORY.csv` — 370 rows, 14 columns.
**Branch:** `arena/04fdf32e-le`.

---

## 1. Task

Build an inventory of the handler's Drive paper library: title, Drive id, first author, year,
journal, DOI if printed, matched `LITERATURE_BASE` key or `NEW`, `read_level = NONE` — without reading
bodies beyond title page.

**Scope constraint applied this turn (handler's instruction of 2026-10-22):** the inventory is built
**only** by `'<folderId>' in parents` listings of the papers folders. No Drive-wide query was issued.
Nothing outside the papers tree was listed or opened, and the private/personal folder is **not named in
this file or anywhere in the repo**; it was not opened, not listed and its contents are unknown to me.

## 2. Method

1. Three roots were used as the papers tree, all reached by parent-id listing only:
   `1_My_Published_Papers`, `2_Others_Papers`, and a third folder named `Papers` (recorded as
   `Papers_root`) whose own parent I did **not** resolve — it was already known by id from the previous
   turn's listing and contains only papers, so I listed its children by id and stopped there.
2. Every subfolder of `2_Others_Papers` was then listed by id: `Collected`, `Collected from Drafts`,
   `Collected from My Folders`, `Mendeley`, `Beam`, `Flexo`, `Nonlocal`, `Energy`, `Two temp`,
   `Three phase lag`, `TPL`, `Piezo+MDD`, `New piezo`, `reflection+piezo`, `reflection piezo`,
   `Imperfact boundary`, `R Poonia Sir`, `Used in P07/P10/P11/P17/P31`. Twenty-four folders in total,
   all leaf-level listing calls.
3. `read_level = NONE` for every row: no body was read. The only file openings were **title-page
   extractions** (10 attempted, 8 succeeded), used to fill title/author/year/journal/DOI for files whose
   names carry no bibliographic information.
4. Matching to `LITERATURE_BASE` (430 rows) was done mechanically, in three tiers, and the tier is
   recorded per row in `match_basis`:
   * `DOI_in_filename` — a DOI suffix from the base appears verbatim in the file name;
   * `TITLE_TOKEN_MATCH` — ≥4 shared non-stopword tokens and ratio ≥0.75, accepted only if the match is
     unique and beats the runner-up by ≥0.10, then de-duplicated so that no LIT id is claimed twice;
   * `AUTHOR_YEAR_ONLY` — surname+year parsed from the file name, exactly one base row matches; kept as
     **unconfirmed** (id suffixed `?`).
   An earlier looser pass (3 tokens, 0.55) produced multi-file collisions on one LIT id and was
   discarded, not shipped.
5. Folder labels in the CSV are structural (`2_Others_Papers_/Mendeley` etc.), not Drive display names,
   so the file carries no personal or non-paper information.

## 3. Result

| quantity | value |
|---|---|
| files inventoried | **370** |
| folders traversed | **24** |
| PDFs | 368 |
| `.doc` (own drafts, not papers) | 2 |
| unique Drive ids | 370 (0 duplicates) |
| confirmed match to `LITERATURE_BASE` | **14** (11 title-token, 3 DOI-in-filename) |
| unconfirmed author+year match | 1 |
| **`NEW`** (not in the 430-record base) | **355** |
| rows with a DOI string | 8 |
| rows with first author filled | 8 (all from title pages) |
| title pages opened | 8 of 10 attempted |

Per folder: My-Folders 74, My-Published-Papers 53, from-Drafts 49, Mendeley 30, Nonlocal 20, Beam 15,
Flexo 15, Used-in-P10 13, Reflection-piezo 11, Others-root 10, New-piezo 10, Used-in-P17 10,
Used-in-P31 10, Energy 8, Two-temp 8, Three-phase-lag 8, Used-in-P07 8, Reflection+piezo 6, Papers_root 3,
Imperfect-Boundary 2, Piezo+MDD 2, R-Poonia-Sir 2, Used-in-P11 2, TPL 1.

### 3.1 The two findings that matter for B10

**(a) The library and the reference base barely overlap.** 355 of 370 files are `NEW`; only 14 carry a
confirmed `LITERATURE_BASE` id. The base of 430 records is therefore mostly **not backed by a PDF in this
library**, and the library is mostly **not used by the manuscript**. Both directions matter: B10c cannot
"verify the base from the PDFs" for most keys, and the library is a separate corpus of candidate
references. This is a scoping fact, not an error in either artefact — but the B10 plan should not assume
one-to-one.

**(b) 15 rows are internal duplicates.** Seven filename groups repeat (15 files): `LAg_Nonlocal_WM-6`
×3, and `2019Amodifiedfractional…`, `arefi2016`, `Kaur,Lata,Singh 2020 Reflection and refra`,
`wang2020`, `zhang2020`, `MAIN PAPER` ×2 each. So the distinct-paper count is **≈355**, and any
"~400 papers" figure is an upper bound on files, not on papers.

### 3.2 A correction that falls out of the inventory (B11 carry-over)

Title page of `P05_2023_SciRep_…` prints **`Scientific Reports (2023) 13:17170`**, DOI
`10.1038/s41598-023-44339-5`, authors Barak, Ahmad, Kumar, Kumar, Gupta, Awwad, Ismail. B11 recorded
"article number not captured — do not cite 17421". The number is now read off the publisher PDF:
**13, 17170**. `LITERATURE_BASE` LIT-0042 venue and author list were updated from that page and
`literature_base.bib` was regenerated (430 entries, still 0 duplicate DOIs, still **308** records without
authors — LIT-0042 was not one of the blank ones, so the B10d baseline is unchanged).

## 4. Evidence / sources

* Listing calls: `list_files` with `'<id>' in parents` for each of the 25 folder ids (24 folders + the
  roots), 2026-10-22. Total items returned: 370; every response carried `next_page_token: null`, so no
  page was silently dropped.
* Folder ids are recorded in the CSV only as folder labels, not as drive ids, to keep the file free of
  structural identifiers beyond what is needed.
* Title pages read (8, all `extraction_status: success`): `093.pdf` (Shekarchizadeh, *Math. Mech.
  Solids* 27(10) 2218, DOI `10.1177/10812865221114336`), `Full.pdf` (Wierzbicki, *Structural Mechanics*,
  LibreTexts OER), `1a10900e-….pdf` (Sun & Zhang, *Adv. Math. Phys.* submission PDF), `fileserve.pdf`
  (S. Kumar, Kumari, Barak, *Change Management* 22(1)), `P40` (Aldandani et al., *HFF*, DOI
  `10.1108/HFF-11-2025-0930`), `P05` (Barak et al., *Sci. Rep.* 13, 17170), `P19` (Gupta & Barak,
  *MAMS*, DOI `10.15376494.2023.2217420`), `Inhomogeneous waves in porous piezo-thermoelast.pdf`
  (Vashishth & Sukhija, *Acta Mech.* 2017, DOI `10.1007/s00707-017-1805-8`), `lord1967.pdf` (Lord &
  Shulman, *J. Mech. Phys. Solids* 15, 299–309), `MACS-2502-1808-1-2.pdf` (Seth & Kashim, MGT + MDD
  state-space).
* `LITERATURE_BASE.csv` (430 rows) as the matching target; `make_bibtex.py` re-run after the LIT-0042 edit.

## 5. Checks done

1. **Completeness of the traversal.** Every subfolder returned by the parent listings was itself listed;
   the recursion terminates with 24 leaf folders and no folder was listed twice.
2. **Uniqueness.** 370 rows, 370 distinct Drive ids, 0 duplicates (`sort | uniq -d` on the id column).
3. **Arithmetic.** Per-folder counts sum to 370 (checked against the sum of the individual listing
   totals: 53+10+138+49+74+43+3).
4. **No silent over-claim in matching.** The first matching pass produced 5 collisions (several files
   mapping to one LIT id) and was discarded; the shipped pass enforces uniqueness plus a 0.10 margin and
   demotes the rest to `NEW`. Two spot-checks were run by hand: `lord1967.pdf` → LIT-0002 (correct, Lord
   & Shulman 1967) and the earlier collision `P06`/`P03` → LIT-0185 (correctly demoted).
5. **PDF vs paper.** The two `.doc` files are the handler's own manuscript drafts; they are flagged
   `is_pdf = no` and excluded from any "papers" count.
6. **Duplicate detection.** Normalised filename comparison found 7 repeated groups / 15 files; reported,
   not silently collapsed.
7. **Privacy.** The private/personal folder's name appears in no committed file; nothing outside the
   papers tree was listed or opened.

## 6. Confidence

* File count, folder structure, ids: **HIGH** (direct listings, no pagination remainder).
* The 14 confirmed matches: **HIGH** for the 3 DOI matches (string identity), **MEDIUM-HIGH** for the 11
  title matches (token match inspected, uniqueness enforced, two hand-checked).
* `NEW` for the remaining 355: **HIGH as "not in the base by these criteria"**, not as "not in the base"
  — a file whose name is opaque (`FullText2019.pdf`, `093.pdf`, `MACS-2502-1808-1-2.pdf`) can match a base
  row once its title page is read. `093.pdf` is exactly such a case: it is now identified, and it is
  `NEW`.
* First author / year / journal for the 355 unopened rows: **UNVERIFIED**.

## 7. NOT verified / open issues

* **Metadata is blank or filename-derived for 362 of 370 rows.** `first_author` and `journal` are empty
  for all but the 8 title-page rows; `year` and `title` are filename-derived and often truncated
  mid-word (`…Subject` for `…Subject to higher order…`). Nothing in this CSV may be cited as
  bibliographic fact until the title page is read in B10c.
* **Two files could not be opened at all:** `abo el nour abd alla.pdf` (3.7 MB, extraction *failed* —
  reported as possibly corrupt, not size) and `slaughter2002.pdf` (71.5 MB, above the 25 MB extraction
  cap; also 71 MB suggests a book, not a paper). Both stay `read_level = NONE`, no metadata invented.
* **`Papers_root` parent unresolved.** I did not walk upward to check where that folder lives; its 3
  files are inventoried, its position in the tree is not. If it is not a papers folder, three rows
  (2 drafts + `fileserve.pdf`) come out — no other row depends on it.
* **One folder in the papers tree was skipped as not-a-paper-folder:** `AK Notes (Elasticity)` (notes,
  not publications). Say-so here, per the "if unsure, skip and say so" rule.
* **No PDF was opened beyond page 1 and no full text, figure or page image entered the repo.** No PDF
  bytes were downloaded.
* **Duplicate papers across folders are counted, not merged.** The distinct-paper count (≈355) is an
  estimate from filenames only.
* **No separate B10 addendum file exists** on `origin/claude/control` @ `a0ace86` (checked the tree and
  grepped `ADDENDUM`/`308` across all `control/*.md`). The operative amendments to B10 are B11's three
  conditions — in particular the **308** blank-author baseline, which is unchanged by this turn. If an
  addendum was meant to be a separate file, it did not reach the branch.
