# Current build status — phase5 v1.1

**Current engineering state: PASS.** The latest content-bearing manuscript/workflow validation was successful CI run [40437606245](https://github.com/vipin-oss/le/actions/runs/40437606245), source commit `101ec95` (2026-10-27). The workflow-published PDF and contact sheets are in output commit `2520052`.

| Check | Result |
|---|---:|
| PDF pages | 129 |
| Undefined references/citations | 0 |
| Overfull boxes above 1 pt (strict build gate) | 0; gate passed |
| Near-overfull boxes above 0.5 pt (summary metric) | 0 |
| Forbidden process-tag occurrences under the case-sensitive workflow pattern | 0 |
| Privacy-token occurrences in extracted PDF text | 0 |
| Figure PDFs generated / included | 18 / 18 generated; 16 active master includes |
| Underfull hbox warnings | 258 |
| Install utilities + TeX build time | 18 s + 9 s = 27 s |
| Whole job duration | 3m 0s |

The build published the current PDF and four contact sheets under `phase5/build_outputs/`; the output commit is `2520052`. The 100-dpi sheets are overview checks, not full-size proofing. Section 7 was visually checked on PDF pp. 55–56; Section 8 prose, equations, and technique tables were inspected on PDF pp. 56–60 (printed pp. 55–59), with no apparent clipping. The solution-workflow figure’s lower connectors should receive a closer figure-audit review in WP5. The build establishes engineering reproducibility and gate results; it does **not** certify every scientific claim.

## Scientific and editorial state

- The classical local energy density and outward-positive flux were derived from the displayed local balances and symbolically checked under their stated assumptions.
- WP2 source-backing: Section 4 has a targeted Tzou pass; Section 5 has fresh Mindlin, Biot, Barak, and Kumar checks; Section 7 has fresh Lata–Singh, Gupta, Li–He, Tung, and Zang checks; Section 8 has a fresh Biswas GN-III Eq. (3) check and narrowed method claims; Section 12 has a targeted Tzou/Quintanilla pass. OCL-256, -257, -258, -260, -261, and -075 are Class A, with OCL-260 recording a `CONTRADICTION-FIXED` correction. Chadwick–Sneddon, Marotti, and Hughes full texts were not located in the inspected set; source identity remains distinct from claim verification. Consult `OPEN_CLAIMS_LEDGER.csv` (457 entries: A=26, B=127, C=304), `R4B_SOURCE_FINDINGS.md`, and `MISSING_SOURCES.csv` (21 records).
- `R4A_DELETION_AUDIT.csv` records 593 removed-text entries and has zero `NONE` identifiers. Deleted claims are not thereby verified and should not be restored as established results.
- Figure source/licensing provenance, individual final-size legibility, complete claim-level primary-source verification, and journal/submission readiness remain open.

## Historical build reports

Older page counts and CI identifiers in `quality-gates.md`, `phase-status.md`, `page-count-reconciliation.md`, `page-by-page-reconciliation.md`, and `version-provenance.md` describe earlier snapshots. They are retained as history; use this file and the linked current CI run for the current build state. The v1.0 baseline remains in `phase4/` and `phase5/master/v1.0-baseline.pdf` for comparison, not as the current manuscript.
