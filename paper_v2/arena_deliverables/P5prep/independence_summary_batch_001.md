# P5-prep Independence Audit - Batch 001 Summary

Scope: metadata triage only of the 74 rows in `paper_v2/atlas_targets.csv` against the
Google Drive PDF library matched by `pdf_filename`. No manuscript was edited. No
scientific findings were extracted; only what was actually opened on the first page
(title block, author list, journal/year/DOI imprint) is recorded. This triage is not a
finding. Companion file: `independence_audit_batch_001.csv` (74 data rows, exact 14-column
header, ASCII only).

## Row-level counts (74 rows)

- pdf_found = yes: 68; pdf_found = no: 6
- readable = yes: 68; readable = no: 6 (same 6 not-found rows; nothing was opened for them)
- own_group: 47
- independent_by_authors: 21
- unknown: 6 (all six are the not-found rows; author list could not be read)

Notes on duplicates in the source file:
- Barak2023IJP appears on two identical rows; the file was opened once and the record is
  repeated with a duplicate note (own_group on both rows).
- Guo2018 appears on two identical rows; same treatment (independent_by_authors on both rows).
- Lim2015 appears on two rows with different filenames. The first file
  (`1-s2.0-S0022509615000320-main.pdf`) was found and read (independent_by_authors).
  The second (`lim2015.pdf`) was not found; that row is recorded as unknown/not-found.
- Wang2021 appears on two rows with different filenames; both files were found, opened and
  read (both independent_by_authors). See caveat below.

Unique-bibkey view: 70 unique bibkeys; 46 own_group, 19 independent_by_authors,
5 with no readable copy at all (Lim2015 is covered by its other file).

## Problem-type triage among independent rows (21 rows, by first opened row per bibkey)

- reflection_transmission: 3 (AboDahab2020, Singh2020c, Yadav2022)
- review_or_theory: 7 (Biot1956, Chen2004, Gao2007, Lim2015, Szekeres2012, Wang2021 rows)
- bulk_wave: 1 (Mondal2020)
- other (statics, vibration, diffusion, fracture, FE, bio-heat - no propagating-wave
  boundary-value problem on first page): 10 (Guo2018, Ke2014, Li2019, Li2021, Ma2020,
  Raja2004, Vinyas2017, Zhang2021, Zhao2018, plus Wang2021 second file counted under
  review_or_theory above)

## Independent bibkeys (19)

AboDahab2020, Biot1956, Chen2004, Gao2007, Guo2018, Ke2014, Li2019, Li2021, Lim2015,
Ma2020, Mondal2020, Raja2004, Singh2020c, Szekeres2012, Vinyas2017, Wang2021, Yadav2022,
Zhang2021, Zhao2018

Own-group author list used for matching (abbreviations such as "V. Gupta" count as
matches): Vipin Gupta, M. S. Barak, Soumik Das, Vijayata Pathania, Rajesh Kumar,
Rachaita Dutta, Meghana A. R., Abhik Sur.

## Not found in the Drive library (6 rows; searched by filename, then by title and DOI)

- DellOroPata2016Viscoelasticity - `10.1007@s00245-016-9365-1.pdf`
- Fabrizio2014 - `fabrizio2014.pdf`
- Lim2015 (second row) - `lim2015.pdf`
- Povstenko2011Cattaneo - `povstenko2011.pdf`
- Quintanilla2003DPL - `quintanilla2003.pdf`
- Quintanilla2008a - `quintanilla2008.pdf`

These rows are recorded with own_group_status = unknown, readable = no, and empty content
columns; no inference was made about them. They are also the complete unreadable list.

## Caveats

- Wang2021 row with filename `AppliedMathematicsandComputation3912021125627.pdf`: the
  opened PDF carries a ResearchGate cover sheet printing the Part I title and the target
  DOI (10.1016/j.cam.2020.112923), but the article pages are Part II in Applied
  Mathematics and Computation 391 (2021) 125627. The other Wang2021 file
  (`mdd vs fract.pdf`) is Part I in Journal of Computational and Applied Mathematics 384
  (2021) 112923 and matches the target DOI. Mismatch noted in the CSV row.
- Emerald early-cite prints (HFF, MTDM, JIOS rows): DOI is printed on page 1 but the
  volume/year block is not always present; where no year imprint was visible, year is
  recorded as "-" with a note, never guessed.
- Authors printed with diacritics were ASCII-transliterated (for example Murat Yaylaci,
  Eduard-Marius Craciun, Szechenyi/Gyor in one affiliation); "diacritics removed" is
  noted in the affected rows.
- Singh2020c authors are Baljeet Singh and Geetika Gupta; Geetika Gupta is not the
  own-group Vipin Gupta, so the row is independent_by_authors.
- No Google Drive IDs, links, or folder names appear in any deliverable; files are
  identified only by the `pdf_filename` values from `atlas_targets.csv`.
- Both deliverables are pure ASCII with no control characters (verified byte scan).
- All 74 source rows fit in this single batch; no batch 002 is required.
