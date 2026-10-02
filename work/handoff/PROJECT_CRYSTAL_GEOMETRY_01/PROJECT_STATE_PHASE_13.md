# PROJECT_STATE_PHASE_13 — Manuscript package complete (30 Sep 2026)

## Outcome
Manuscript draft v1.0 (numbers-polished, MANUSCRIPT_DRAFT.md) + supplementary tables +
final figures with captions + reproducibility package complete. Journal choice and
submission REMAIN USER-OWNED (shortlist in JOURNAL_SCREENING.md; draft is journal-agnostic).

## Completed this phase (previous-task loose ends)
1. c_p worked example (PARAMETER_TABLE §D promise): data/SUPP_cp_worked_example.csv —
   c_p∈{500,560,700} → t_th∈{22.6,25.3,31.6} ps, Λ∈{0.887,0.792,0.633},
   ε∈{0.0577,0.0515,0.0412} at (a=10nm, τ=20ps); folded into manuscript §4.2b.
2. θ_amp=10 K dimensional example: circle 9.67 MPa, ellipse 11.25–16.69 MPa,
   iso controls 10.54/17.63 MPa (manuscript Table 3 block).
3. Supplementary CSVs: SUPP_phi_sweep.csv, SUPP_D_lambda.csv, SUPP_verification.csv.
4. Environment captured: data/ENVIRONMENT.json (Python 3.13.14, numpy 2.3.5,
   scipy 1.17.1, matplotlib 3.10.9, Linux x86_64).
5. Code freeze: data/CODE_FREEZE.json (sha256 × 8 code files; change ⇒ CHANGELOG +
   V-suite re-run rule stated).
6. Determinism: analyze_production.py addendum folded in (single-script reproduction);
   double-run comparison IDENTICAL (data/ANALYSIS.json keys complete).
7. Figures regenerated at 160 dpi + figures/FIGURE_CAPTIONS.md (fig1–fig4 final).
8. RECOVERY_CRYSTAL_GEOMETRY_01.zip refreshed (see manifest for final file list).

## Evidence map (submission package)
- Science: MANUSCRIPT_DRAFT.md, figures/fig1–4 + FIGURE_CAPTIONS.md,
  data/SUPP_*.csv, data/ANALYSIS.json.
- Verification: data/VERIFY.json, logs/verify_rerun_v3.log, PRIOR_WORK_COMPARISON_R2.md.
- Reproducibility: RECOVERY zip + manifest (sha256), data/ENVIRONMENT.json,
  data/CODE_FREEZE.json, run_verify/run_production/analyze_production.
- Honest history: root CHANGELOG + DECISION_LOG (D013–D016), REJECTED_IDEAS.md.

## Limitations (carried, unchanged)
Physical validation NOT_AVAILABLE; τ hypothetical; α5=0; c_p estimated (worked example
now provided); V2 PARTIAL (grid uncertainty carried); η_d=0.05 regularization
(≤0.2% sensitivity); JCR direct records UNVERIFIED (submission-time check).

## Exact next action (user-owned)
1. Journal decision (shortlist ready) → 2. format pass per target + JCR verification +
cover letter → 3. expert review recommended → 4. submission.
