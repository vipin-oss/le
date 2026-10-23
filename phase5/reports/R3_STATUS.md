# R3 evidence-verification and build status

**Current R3a result:** 81 rows; **77 VERIFIED / 3 MISMATCH / 1 NOT-FOUND**. The R3a comparison was regenerated only from the 81 saved Crossref JSON responses; no new R3a requests were made. R3b is verified dynamically by the single strict CI run associated with the `[R3B-CROSSREF]` content commit.

## R3a verification — Sections 4.1–4.12

The same saved JSON was re-evaluated under the documented relaxed title, venue, and date comparison rules. **Nineteen** rows record `reclassified_from=MISMATCH`. Final R3a result: **77 VERIFIED / 3 MISMATCH / 1 NOT-FOUND**. Among technically eligible rows, **21 are VERIFIED and bibliography-ready, 0 are MISMATCH, and 1 is NOT-FOUND**. The 21 eligible sources are cited only for their mapped, model-specific claims; conditional and secondary-source labels remain in force. `Chandrasekharaiah1998` is the one additional BibTeX-ready Crossref record, cited only as `SECONDARY-SOURCE` historical background, never as equation-level evidence.

The three unresolved Crossref metadata mismatches are `Iesan2013` (venue mismatch), `Zenkour2016` (venue mismatch), and `Masui2025` (venue mismatch). `Youssef2018` is NOT-FOUND (Crossref HTTP 404) and remains uncited. The R3a title-overlap human-check list has **zero candidates**; the 404 is not a title-match human-check case. See `CROSSREF_VERIFY.csv`, `CROSSREF_METHOD.md`, and `CROSSREF_HUMAN_CHECK.md` for the full comparison and provenance.

### R3a evidence-ready counts by plan section

| Plan section | Verified, technically eligible and bibliography-ready sources | Status / gap |
|---|---:|---|
| 4.1 | 0 | No eligible verified source in scope |
| 4.2 | 0 | No eligible verified source in scope |
| 4.3 | 2 | Lord–Shulman; model-specific fractional/nonlocal LS variant |
| 4.4 | 1 | Rate-dependent two-temperature comparison |
| 4.5 | 1 | Rheological network comparison; no admissibility claim inferred |
| 4.6 | 1 | Nonlocal GN-III variant |
| 4.7 | 2 | Distinct second-order DPL truncations; no universal ordering inferred |
| 4.8 | **8** | Multiple distinct TPL/DPL variants; not a single universal law |
| 4.9 | 0 | No plan row labelled 4.9; MGT source is mapped at plan s.4.10 and cited in the MGT subsection |
| 4.10 | 2 | MGT and memory-dependent/fractional comparison |
| 4.11 | 0 | No eligible verified source in scope |
| 4.12 | 4 | Comparative two-temperature examples; `Youssef2018` is NOT-FOUND and uncited |

Only section 4.8 reaches six evidence-ready R3a sources. Gaps are not padded with unverified records.

### No-DOI printed-source leads

Cattaneo (1948), Vernotte (1958), Achenbach (1973), Nowacki (1975), and Tzou (1997 book) remain separately identified as **“NO DOI - printed source”**. No DOI was invented or assigned to these leads.

## R3b verification and evidence

- Scope: 90 REFERENCE_PLAN rows from sections 5–9 and 11–13; 47 technically eligible DOI rows queried; 47 unique Crossref requests.
- R3b Crossref results: 40 VERIFIED, 5 MISMATCH, 2 NOT-FOUND, 4 NO-DOI; 39 metadata-only rows INELIGIBLE and not queried.
- Technical-eligible R3b rows: 39 VERIFIED and bibliography-ready; 1 VERIFIED but not bibliography-ready; 4 NO-DOI; 5 MISMATCH; 2 NOT-FOUND.
- R3b mapped citations inserted: 39 unique verified eligible keys; new BibTeX keys added in this build: 35. No metadata-only or unverified row is inserted as technical evidence.
- Sections meeting ≥6 evidence-ready sources across R3a/R3b: 4.8 (8), 6 (7), 7 (6), 9 (19).
- R3b human-check list: `CROSSREF_R3B_HUMAN_CHECK.md`.
- R3a final counts after cached-response reclassification: 77 VERIFIED / 3 MISMATCH / 1 NOT-FOUND; 19 rows record `reclassified_from=MISMATCH`; 21 technical-eligible bibliography-ready keys; 1 background-only review key.
- R3a title human-check list: `CROSSREF_HUMAN_CHECK.md`.
- Frozen `CITATION_MAP.csv` exact-key matches in the R3b candidate set: 0. Section-specific additions are mapped in `R3B_CITATION_MAP.csv` from the eligible plan rows and their documented source claims.
- Remaining gaps: Section 10 is reserved for R3c; Section 11 GAP-09 remains open; R3b MISMATCH, NOT-FOUND, and NO-DOI rows remain uncited. R3b rows with a title overlap below 0.60 are in `CROSSREF_R3B_HUMAN_CHECK.md`.

### R3b unresolved identifiers (not cited)

- LIT-0439 `Guo2019` — MISMATCH: normalized venue does not match Crossref container-title/short-container-title
- LIT-0442 `Deswal2015` — MISMATCH: normalized venue does not match Crossref container-title/short-container-title
- LIT-0443 `Ezzat2012` — MISMATCH: normalized venue does not match Crossref container-title/short-container-title
- LIT-0029 `Wang2011` — MISMATCH: normalized venue does not match Crossref container-title/short-container-title
- LIT-0438 `Quintanilla2009` — MISMATCH: normalized venue does not match Crossref container-title/short-container-title
- LIT-0457 `Faleh2020` — NOT-FOUND: Crossref returned HTTP 404
- LIT-0440 `Kumar2017a` — NOT-FOUND: Crossref returned HTTP 404
- LIT-0499 `Hu2000` — NO-DOI: no DOI recorded; not Crossref-verifiable; keep uncited under this phase
- LIT-0437 `Eringen1978` — NO-DOI: no DOI recorded; not Crossref-verifiable; keep uncited under this phase
- LIT-0484 `Singh2021` — NO-DOI: no DOI recorded; not Crossref-verifiable; keep uncited under this phase
- LIT-0485 `Kumar2020` — NO-DOI: no DOI recorded; not Crossref-verifiable; keep uncited under this phase
- LIT-0471 `Bassiouny2021` — VERIFIED: Crossref author metadata is empty; do not emit BibTeX

## Final strict build

The strict CI run fills the following markers only after the build and publication gates pass:

- Content/source commit: `f03dd97517e127bb05e54bce4da63df457459d40`
- Strict CI run ID: `39875147113`
- Strict build-step time: `10` seconds
- PDF pages: `155`
- Undefined references/citations: `0`

The preserved R1/R2 baseline remains commit `0be9322`, CI run `39781561017`, 149 pages, and zero undefined references. MISMATCH, NOT-FOUND, and out-of-scope literature records are intentionally not promoted to citations; the undefined-reference count is a separate LaTeX build metric.
