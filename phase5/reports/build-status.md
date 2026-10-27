# Current build status — phase5 v1.1

**Current engineering state: PASS.** The latest content-bearing manuscript validation is successful CI run [40456561663](https://github.com/vipin-oss/le/actions/runs/40456561663), source commit `519a21a` (2026-10-27). The workflow-published 130-page PDF and contact sheets are in output commit `11a5aa5`.

| Check | Result |
|---|---:|
| PDF pages | 130 |
| Undefined references/citations | 0 |
| Overfull boxes above 1 pt (strict build gate) | 0; gate passed |
| Near-overfull boxes above 0.5 pt (summary metric) | 0 |
| Forbidden process-tag occurrences under the case-sensitive workflow pattern | 0 |
| Privacy-token occurrences in extracted PDF text | 0 |
| Figure PDFs generated / included | 18 / 18 generated; 16 active master includes |
| Install utilities + TeX build time | 16 s + 8 s = 24 s |
| Whole job duration | 2m 40s |

The current PDF and four contact sheets are under `phase5/build_outputs/`; the output commit is `11a5aa5`. The 100-dpi sheets are overview checks, not full-size proofing. Section 9 was visually checked on PDF pp. 62–65 (printed pp. 61–64): interface equations, determinant/energy-ratio layout, the revised interface schematic, and T6 all render without apparent overlap or clipping. Section 10's new derivations compile; final-size visual inspection of those pages remains pending. The schematic was simplified after review because its flux annotations overlapped the interface and conservation panels; the updated drawing includes the electrical matching condition and separates the wave geometry from the lower panels. CI run `40440483768` first exposed one 14.8-pt overfull line in T6; the cell wording was shortened without changing its scope, and the strict gate passed in the later runs. The build establishes engineering reproducibility and gate results; it does **not** certify every scientific claim.

## Scientific and editorial state

- The classical local energy density and outward-positive flux were derived from the displayed local balances and symbolically checked under their stated assumptions.
- WP2 source-backing: Sections 5, 7, 8, 9, 10, and 12 are complete at the documented targeted scope; the Section 10 additions are a Class V-scoped control-volume split and welded 1D benchmark, not generalized-family flux laws. Section 4 has a targeted Tzou pass but remains open; Sections 11, 13, and 14–17 also remain. Q1 is active: equation-level checks OCL-470–OCL-473 cover a limited set of displayed-form substitutions; unified notation, source-by-source reductions, GL/GN-I coverage, and the comparison table remain open. Then Q2–Q5 proceed in order before the remaining WP3/WP4/WP6/WP7/WP8 work. The current ledger has 477 rows (A=29, B=126, C=313, V=9; A+V=38); `MISSING_SOURCES.csv` has 23 bounded records. The Kumar bibliography-key reconciliation is recorded at OCL-477; all 19 dependent rows (OCL-076 and OCL-278–OCL-295) remain B/C. Section 9 made no Class A promotions; OCL-291 is Class C and marked `CONTRADICTION-FIXED`. Consult `OPEN_CLAIMS_LEDGER.csv` and `R4B_SOURCE_FINDINGS.md` for scope and evidence limits.
- `R4A_DELETION_AUDIT.csv` records 593 removed-text entries and has zero `NONE` identifiers. Deleted claims are not thereby verified and should not be restored as established results.
- Figure source/licensing provenance, individual final-size legibility, complete claim-level primary-source verification, and journal/submission readiness remain open.

## Historical build reports

Older page counts and CI identifiers in `quality-gates.md`, `phase-status.md`, `page-count-reconciliation.md`, `page-by-page-reconciliation.md`, and `version-provenance.md` describe earlier snapshots. They are retained as history; use this file and the linked current CI run for the current build state. The v1.0 baseline remains in `phase4/` and `phase5/master/v1.0-baseline.pdf` for comparison, not as the current manuscript.
