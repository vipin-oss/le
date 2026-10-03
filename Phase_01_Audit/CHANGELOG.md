# CHANGELOG — Phase 1 (Audit) · 2026-10-03

**Manuscript and data: UNCHANGED by design in this phase** (audit only — no results, tables, figures or
manuscript text were edited). Verified by manifest: `Phase_01_Audit/manifest.txt` records the SHA-256 of the
audited `manuscript_IJHMT.md` (`9bd135c9…`) and of the companion `.tex`, stats, test results and `ANALYSIS_V2.json`.

## Added
- `Phase_01_Audit/REPORT.md` — full scientific audit: headline judgement, 15 class-A, 22 class-B, 6 class-C
  findings (43 total) with file:line evidence, the "already strong, must survive" list, a desk-rejection risk map,
  and six explicitly unresolved items.
- `Phase_01_Audit/FINDINGS.json` — the same 43 findings machine-readable (`id, severity, category, location,
  evidence, action, target_phase, status`), for later phases to close out against.
- `Phase_01_Audit/snapshot/` — copies of the audited manuscript, companion, `.tex`, stats, test results.
- `Phase_01_Audit/verification/static_gates.txt`, `pdf_manuscript.txt`, `pdf_companion.txt` — the six repository
  gates as run at audit time (audit_tex 70 checks, tex-command lint, crossref scan, 26 conversion tests,
  renumbering no-op check, both PDF structural verifications): all green.
- `Phase_01_Audit/manifest.txt`, `Phase_01_Audit/CHANGELOG.md` (this file).
- `SUBMISSION_PROGRAM_STATE.md` / `.json` at the repository root — phase tracker so a later session can resume
  from the latest completed phase without repeating work.

## Findings created (open, to be closed in later phases)
A1 failed-test presentation (V0) · A2 `n/a` in Table 5 · A3 author placeholders (author-owned, cannot be fixed) ·
A4 AI-disclosure placement vs Elsevier policy · A5 Bromwich validity over-claim vs the t_w=2.4 window error ·
A6 duplicated §4.6 prose · A7 internal-development language (20+ hits) · A8 coarse-grid-only attribution evidence ·
A9 "1.4 %" provenance (quasi-static row) · A10 three conflated ellipse/circle ratios incl. one cross-grid ratio ·
A11 figures comparing against superseded internal runs + in-figure "frozen criterion" text · A12 no Limitations
section · A13 uncited Cattaneo/Vernotte/Coleman–Gurtin · A14 stale artifact count in §9 · A15 LaTeX compile
unverifiable in this environment. Plus B1–B22 and C1–C6.

## Evidence gathered in this phase
- Test suite read in source: the V0 criterion is `max(e[1] for e in errs) < 5e-3` (the 96×48 column only) at
  `run_tests.py:207`; χ=2 at 96×48 measures 5.028e-3 (0.56 % over), and the sequence is second-order clean
  (ratios 4.00/4.00/3.90/3.99); a code comment announces an order check that was never implemented.
- Full data-vs-text number audit against `ANALYSIS_V2.json`: circle 0.854 (0.8536), grid-M error 0.03 % (0.031),
  modulation 29.87 %/28.749 %/u_num 1.31 pp, extremes 0.966–1.322, D ≤ 6.4 % (6.38) and 1.6 % for a ≥ 10 nm,
  5δ = 6.56 %, v9d worst 0.08 %, ellipse p = 1.197 with rel. errors 4.4e-3/1.9e-3 — all consistent; the
  inconsistencies found are A8, A9, A10 (grid/provenance, not arithmetic).
- Reference screening: 54 entries, all DOI-verified by the project's own Crossref records
  (`01_Literature/`); coverage adequate with no padding detected; the only genuine citation gaps are A13/B19.
- Elsevier generative-AI author policy text retrieved and recorded (writing-process-only declaration, placed
  before the references; research-process AI described in Methods).
- Compute environment measured: 2 vCPU, 3 GB RAM, ~20 GB free → Phase 2 rerun budgeted at ~22 min for the
  30-run M-grid ablation set (measured 19–20 s/run at the coarse grid, 55 s/run in the cost table at M).

## Known limitation introduced by this phase
None to the artifact. Note `objects.githubusercontent.com` is unreachable here, so no LaTeX engine could be
installed (finding A15); the preprint PDF remains the reportlab-built one.
