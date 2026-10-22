# R3a status — Sections 4.1–4.12

## Outcome

R3a added mapped citations and Crossref-backed bibliography metadata for **21 technical-claim-eligible, VERIFIED sources**. Eighteen bibliography keys were newly added; three existing entries (`Lord1967`, `Quintanilla2019`, `RoyChoudhuri2007`) were refreshed from the saved Crossref metadata. No MISMATCH or NOT-FOUND row was cited. The verified source keys are used only for the scoped, model-specific claims identified in the manuscript; CONDITIONAL and SECONDARY-SOURCE labels are retained where applicable.

The saved Crossref responses were fetched once by Actions run `39799109343` (successful; Crossref/build preflight took 4m17s). After correcting title/venue normalization and comparing the base year against all Crossref published/issued date fields, the same 81 saved responses were re-evaluated offline with `--reuse-raw`; no new DOI requests were made. The original comparison yielded 43 VERIFIED / 37 MISMATCH / 1 NOT-FOUND; the final corrected comparison below is authoritative.

## Crossref verification

- Scoped plan rows: **81**
- DOI requests in the saved Actions snapshot: **81**
- Final results: **58 VERIFIED, 22 MISMATCH, 1 NOT-FOUND**
- `technical_claim_eligible=YES`: **21 VERIFIED and bibliography-ready; 1 NOT-FOUND; 0 MISMATCH**
- All **22 MISMATCH** rows are metadata-only/ineligible for technical claims. Their detailed field-level reasons are in `CROSSREF_VERIFY.csv`.

## Added and mapped evidence by plan section

Counts below are Crossref-VERIFIED, bibliography-ready sources, grouped by the read-only `REFERENCE_PLAN.plan_section` value. The TPL section's existing MGT citation `Quintanilla2019` is placed in manuscript subsection 4.9, where the MGT discussion appears, although its plan row is labelled s.4.10.

| Plan section | Ready sources | Status / gap |
|---|---:|---|
| 4.1 | 0 | No eligible verified source in scope |
| 4.2 | 0 | No eligible verified source in scope |
| 4.3 | 2 | Lord–Shulman; model-specific fractional/nonlocal LS variant |
| 4.4 | 1 | Rate-dependent two-temperature comparison |
| 4.5 | 1 | Rheological network comparison; no admissibility claim inferred |
| 4.6 | 1 | Nonlocal GN-III variant |
| 4.7 | 2 | Distinct second-order DPL truncations; no universal ordering inferred |
| 4.8 | **8** | Only section meeting the ≥6-source threshold; multiple distinct TPL/DPL variants, not a single universal law |
| 4.9 | 0 | No plan row labelled 4.9; MGT source is mapped at plan s.4.10 and cited in the MGT subsection |
| 4.10 | 2 | MGT and memory-dependent/fractional comparison |
| 4.11 | 0 | No eligible verified source in scope |
| 4.12 | 4 | Comparative two-temperature examples; Youssef2018 is NOT-FOUND and remains uncited |

Thus, **section 4.8 is the only section with at least six evidence-ready sources**. The sections with no eligible verified source are 4.1, 4.2, 4.9, and 4.11. Other underfilled areas remain gaps rather than being padded with unverified sources.

## MISMATCH and NOT-FOUND — unresolved and uncited

**MISMATCH (22):**

- LIT-0006 `Dhaliwal1980`
- LIT-0023 `Iesan2013`
- LIT-0039 `Chandrasekharaiah1998`
- LIT-0040 `Shakeriaski2021`
- LIT-0051 `Hughes1980`
- LIT-0143 `FractionalHeat2025`
- LIT-0035 `Caputo1967`
- LIT-0056 `Kumar2010`
- LIT-0053 `Suh1998`
- LIT-0060 `Tiwari2022`
- LIT-0061 `Baksi2004`
- LIT-0116 `SizeDependent2022`
- LIT-0148 `SomeBasic2024`
- LIT-0004 `Green1991`
- LIT-0086 `Zenkour2016`
- LIT-0092 `Masui2025`
- LIT-0093 `Shi2025`
- LIT-0094 `Li2026`
- LIT-0095 `Bazarra2019`
- LIT-0097 `Li2025`
- LIT-0096 `Shi2021`
- LIT-0098 `Mondal2019`

**NOT-FOUND (1):** LIT-0467 `Youssef2018` — DOI `10.18720/MPM.4022018_4`, Crossref HTTP 404. It remains unresolved and uncited.

The row-level DOI, comparison fields, reason, eligibility, and raw-response path are recorded in `CROSSREF_VERIFY.csv`.

## No-DOI printed-source leads

These remain separately identified as **“NO DOI - printed source”** and were not sent through Crossref or assigned invented DOI matches: Cattaneo (1948), Vernotte (1958), Achenbach (1973), Nowacki (1975), and Tzou (1997 book).

## Final strict build

The final strict-build workflow fills the following fields after all build gates pass and publishes this report with the PDF/contact sheets:

- Content/source commit: `02dd3cf9ac9371c56b5bb6ea14e0a33cd3edbc93`
- Strict CI run ID: `39801616881`
- Strict build-step time: `10` seconds
- PDF pages: `151`
- Undefined references/citations: `0`

MISMATCH and NOT-FOUND literature rows are intentionally unresolved; the undefined-reference count above is the separate LaTeX strict-build metric.
