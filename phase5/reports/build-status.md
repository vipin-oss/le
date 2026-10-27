# Current build status — phase5 v1.1

**Current engineering state: PASS.** The latest content-bearing manuscript/workflow validation was successful CI run [40434775391](https://github.com/vipin-oss/le/actions/runs/40434775391), source commit `debf937` (2026-10-27). The workflow-published PDF and contact sheets are in output commit `c76bc25`.

| Check | Result |
|---|---:|
| PDF pages | 130 |
| Undefined references/citations | 0 |
| Overfull boxes above 1 pt (strict build gate) | 0; gate passed |
| Near-overfull boxes above 0.5 pt (summary metric) | 0 |
| Forbidden process-tag occurrences under the case-sensitive workflow pattern | 0 |
| Privacy-token occurrences in extracted PDF text | 0 |
| Figure PDFs generated / included | 18 / 18 generated; 16 active master includes |
| Install utilities + TeX build time | 19 s + 10 s = 29 s |
| Whole job duration | 2m 57s |

The build published the current PDF and four contact sheets under `phase5/build_outputs/`; the output commit is `c76bc25`. The 100-dpi sheets are overview checks, not full-size proofing. The build establishes engineering reproducibility and gate results; it does **not** certify every scientific claim.

## Scientific and editorial state

- The classical local energy density and outward-positive flux were derived from the displayed local balances and symbolically checked under their stated assumptions.
- WP2 Section 4 has a targeted Tzou pass (OCL-166–OCL-168 Class A); Section 5 now has fresh Mindlin, Biot, Barak, and Kumar page checks. OCL-195, -207, -404, and -405 are Class A; OCL-205/-206 were removed from active text. Other Section 5 sources and claims remain open. Consult `OPEN_CLAIMS_LEDGER.csv` (445 entries: A=20, B=129, C=296), `R4B_SOURCE_FINDINGS.md`, and `MISSING_SOURCES.csv`.
- `R4A_DELETION_AUDIT.csv` records 593 removed-text entries and has zero `NONE` identifiers. Deleted claims are not thereby verified and should not be restored as established results.
- Figure source/licensing provenance, individual final-size legibility, complete claim-level primary-source verification, and journal/submission readiness remain open.

## Historical build reports

Older page counts and CI identifiers in `quality-gates.md`, `phase-status.md`, `page-count-reconciliation.md`, `page-by-page-reconciliation.md`, and `version-provenance.md` describe earlier snapshots. They are retained as history; use this file and the linked current CI run for the current build state. The v1.0 baseline remains in `phase4/` and `phase5/master/v1.0-baseline.pdf` for comparison, not as the current manuscript.
