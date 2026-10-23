# V-B5b_3 — Testing Arena's method: re-classification of all 56 rows

| field | content |
|---|---|
| **Task** | The order's second demand: do not only break the Guyer1990 tie. Re-run checks on Arena's 48 "YES" rows and the 8 `NO_DOI` rows, report any mismatch, any title-only match (the `Eringen1968b` pattern where authors differ) and any irrelevant-topic hit (the `Abdalla2022` pattern), and re-classify every row into EXISTS‑AND‑MATCHES / EXISTS‑BUT‑AUTHORS‑DIFFER / EXISTS‑BUT‑IRRELEVANT / NOT‑FOUND. |
| **Method** | (a) bulk OpenAlex existence-and-title lookup for all 48 DOI'd rows in four batches of ~12 using `filter=doi:a\|b\|c&select=doi,display_name`; (b) OpenAlex `select=authorships` spot-checks; (c) the B5a per-DOI Crossref records already on file in `REFERENCE_AUDIT.csv`; (d) a read of Arena's own validator source. Results in `V-B5b_arena_method_reclassification.csv`. |
| **Result** | 44 EXISTS‑AND‑MATCHES · 2 EXISTS‑BUT‑AUTHORS‑DIFFER · 1 EXISTS‑BUT‑IRRELEVANT · 1 NOT‑FOUND · 8 not machine-checkable (no DOI). **Every one of the 48 DOI'd rows except Guyer1990 resolves to a real work**, so the Guyer1990 fabrication is an isolated artefact, not a symptom of a wholesale bad list. But **13 rows carry a metadata defect** that a table of YES/YES/YES conceals. |
| **Confidence** | **HIGH** on existence: 47/48 DOIs resolve on OpenAlex and the failures are discriminating. **MEDIUM** on "matches": titles were compared against OpenAlex `display_name` for all 48, but **author lists were independently verified for only 5 of the 44 MATCHES rows**. **LOW** on the 8 no-DOI rows — see §4. |
| **NOT verified** | Author lists for 39 of the 44 EXISTS‑AND‑MATCHES rows; the title of `10.1512/iumj.1966.15.15060` (OpenAlex returns `display_name: null`, so that row's title could not be compared at all); whether the manuscript's *use* of each source is appropriate — this sheet tests the record, not the citation's role in the argument. |

## 1. Headline numbers

| class | n | rows |
|---|---|---|
| EXISTS‑AND‑MATCHES | 44 | all DOI'd rows not named below |
| EXISTS‑BUT‑AUTHORS‑DIFFER | 2 | `Eringen1968b`, `Sharma2022` |
| EXISTS‑BUT‑IRRELEVANT | 1 | `Abdalla2022` |
| NOT‑FOUND | 1 | `Guyer1990` |
| not machine-checkable (no DOI) | 8 | `Tzou1997`, `Cattaneo1948`, `Vernotte1958`, `Povstenko2016`, `Gorenflo1997`, `Luchko2010`, `Achenbach1973`, `Nowacki1975` |

## 2. The three failure modes, concretely

**Fabrication.** `Guyer1990` — DOI, volume, issue and page range all resolve to nothing, and the
page is occupied by another journal. Full evidence in `V-B5b_guyer1990.md`.

**Title-only match.** `Eringen1968b`, DOI `10.1016/0020-7225(68)90037-2`: the DOI resolves, the
title, year, volume and pages match the manuscript's claim — but the authors on the record are
**Tauchert, Claus and Ariman**, not Eringen. A checker that compares titles (`title_match YES`
in Arena's table) passes this row. `Sharma2022` is the same pattern one step further: title
matches, authors *and* year do not.

This is the failure mode worth stressing, because it is invisible to the check Arena ran and
it is the one that survives a title similarity score of 1.0.

**Irrelevant topic.** `Abdalla2022`, DOI `10.1016/j.jheap.2022.04.002`: real DOI, real paper,
correct title match — and the paper is a **cosmology review**. It does not belong in a review
of wave mechanics in generalized continua at all. Existence checks cannot catch this; only a
topic check can.

## 3. Metadata defects hidden by a flat YES

Thirteen rows are "exists and matches" in the sense the four buckets ask, but carry a
defect that would survive into the typeset bibliography. Recorded in the `metadata_flag`
column: `Iesan2013` (year differs), `Povstenko2004` (year ambiguous between print and online),
`Barak2023JTS` (record year 2024, manuscript says 2023), `Gupta2023IJNMF` (record 2023,
online-first 2022), `Quintanilla2019` (attribution detail), and — in the no-DOI group —
`Vernotte1958` (page range wrong; the real citation is C. R. **246**:3154), `Gorenflo1997`
and `Nowacki1975` (author initials wrong), `Luchko2010` (author initial wrong and venue
doubtful), `Marotti2013` (exists, but low value for this review).

Arena's table marks all of these `verified YES` on a date when, per its own source, no lookup
was performed. That is the substantive finding of this sheet, independent of Guyer1990.

## 4. What I could not check, and why that matters

* **Authors.** Only 5 of the 44 MATCHES rows had their author lists independently confirmed
  (Green1972 = A. E. Green & K. A. Lindsay; Chandrasekharaiah1986 = D. S. Chandrasekharaiah;
  Iesan1986 = D. Ieşan; Marotti2013 = F. Marotti de Sciarra; Hughes1980 = T. J. R. Hughes —
  all five correct). The other 39 are classified on existence + title + the B5a Crossref notes
  only. Since `Eringen1968b` shows that a wrong author list can sit behind a perfect title
  match, **the 44 should be read as "no defect found", not as "verified clean"**.
* **The 8 no-DOI rows cannot be tested this way at all.** They are books and pre-DOI journal
  items; `Vernotte1958`, `Gorenflo1997`, `Nowacki1975` and `Luchko2010` carry defects found by
  other means in B5a. They are outside the order's four buckets by construction, and I have
  labelled them rather than forced them into a bucket they do not fit.
* **`10.1512/iumj.1966.15.15060`** (`Eringen1966a`) resolves, but OpenAlex holds no title for
  it. The row is real and the DOI is right; the *title* claim is unverified.

## 5. Verdict on the method

Arena's checking procedure tests the wrong thing. It validates **syntax** (DOI shape,
duplicates, allowed status strings) and never performs **resolution**, so:

* a non-existent DOI with valid syntax passes (Guyer1990),
* a real DOI with the wrong authors passes (Eringen1968b, Sharma2022),
* a real DOI on the wrong topic passes (Abdalla2022),
* and the output column is named `crossref_match`, which implies a lookup that never happened.

The fix is not more careful labelling; it is one HTTP GET per row. That is cheap — this sheet
tested 48 rows with four OpenAlex batch calls.
