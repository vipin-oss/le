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

Pending the R3b Crossref Actions run.

## Final strict build

The strict CI run fills the following markers only after the build and publication gates pass:

- Content/source commit: `__R3_SOURCE_COMMIT__`
- Strict CI run ID: `__R3_CI_RUN_ID__`
- Strict build-step time: `__R3_BUILD_SECONDS__` seconds
- PDF pages: `__R3_PDF_PAGES__`
- Undefined references/citations: `__R3_UNRESOLVED_REFS__`

The preserved R1/R2 baseline remains commit `0be9322`, CI run `39781561017`, 149 pages, and zero undefined references. MISMATCH, NOT-FOUND, and out-of-scope literature records are intentionally not promoted to citations; the undefined-reference count is a separate LaTeX build metric.
