# START_HERE — Project orientation (read this first)

**For: any AI model / researcher picking up this project cold.**
Built: 2026-09-30. Language of working notes: mixed English/Hinglish. All scientific
content below is in English.

## 1. What this project is (30 seconds)

A verified computational study of **transient coupled thermoelasticity around a cavity
in a low-symmetry crystal** — specifically monoclinic **β-Ga₂O₃** (plane strain, a-c
crystal plane). The study cleanly separates three effects that the literature entangles:

1. **Material symmetry** (monoclinic elastic tensor C_ij incl. C15, C25, C35, C46;
   anisotropic conductivity with off-diagonal K13; anisotropic thermal expansion).
2. **Geometric symmetry** (circular vs equal-area elliptical cavity, χ=2).
3. **Thermal memory** (Fourier vs Cattaneo–Vernotte vs a 3-phase-lag-type kernel,
   relaxation time τ, dimensionless thermal number Λ = τκ̄/a², size number
   ε = κ̄/(c_ref·a)).

Loading: wall-temperature Gaussian pulse on the cavity (t0=2.5 t_th, tw=1.2 t_th),
traction-free cavity, fixed cold outer boundary at R=80a. All stresses reported **per
unit pulse amplitude** (MPa/K); multiply by θ_amp in kelvin.

## 2. Headline results (all from data/ANALYSIS.json + data/VERIFY.json)

| Claim | Status | Key number |
|---|---|---|
| Circle peak hoop stress is **rotation-invariant** (discrete-rotation identity) | PASS (machine-class) | 0°/90° pair rel. 4.04e-10; field covariance 6.26e-14 |
| Circle field is nonetheless **non-axisymmetric** (anisotropy pattern) | measured (exploratory) | m2/m0 = 0.085 (isotropic circle = 5.2e-11) |
| Ellipse converts crystal orientation φ into **peak-stress modulation** | RESOLVABLE (robust) | 33–37% amplitude (32.7% at 192×96 grid), σ̂ = 1.13–1.67 MPa/K over φ |
| Thermal-memory deviation D(Λ,ε) **collapses in Λ alone** (pre-registered H3) | NOT-SUPPORTED (honest negative) | collapse residual 78%; equal-Λ pair splits 3.5×; post-hoc scalings also fail (D/Λ 3.7×, D/(Λε) 2.5×, D/(Λε²) 10× spread) → **two-parameter (Λ,ε) map is the finding** |
| Thermoelastic feedback on temperature bounded | WITHIN-BOUND | 2.17e-4 ≤ 5δ (δ = 1.08e-3) — ≈0.2δ, negligible |
| Verification suite V0–V7 | mostly PASS | V2 PARTIAL (grid convergence 2.35% circle / 6.8% ellipse vs ≤2% — handled via documented per-quantity uncertainty + 192×96 spot checks); V3 rotation covariance 6.26e-14; V6 log-law 9.5e-6; V7 closed form 0.68% |

Worked dimensional example (a=10 nm, τ=20 ps, c_p≈560 J/kgK): t_th≈25.3 ps, Λ≈0.79,
ε≈0.052; at θ_amp=10 K: circle peak 9.67 MPa (orientation-invariant), ellipse
11.25–16.69 MPa over φ. Full worked table: data/SUPP_cp_worked_example.csv.

## 3. What was NOT claimed (important)

- **No physical validation**: no transient cavity experiments exist for β-Ga₂O₃
  (recorded). Verification ≠ validation. τ values are HYPOTHETICAL (ps-scale sweep).
- α5 (shear expansion) unmeasured → set 0 (LIMITATION). c_p estimated ≈560 J/kgK with
  sensitivity band {500,560,700}.
- Continuum continuum flag: cavity a ≥ 5 nm. Linear small-strain theory.
- The H3 negative result is reported as-is; no post-hoc rescue was dressed as a law.

## 4. How the work was governed (protocol)

- `MASTER_PROMPT.md` = the phase protocol (§0–90) the work followed.
- `DECISION_LOG.md` (D001–D018) = every consequential decision + deviation, timestamped
  **before** results were seen where it mattered (D015: R=80a deviation pre-registered).
- Frozen acceptance criteria (`PROJECT_CRYSTAL_GEOMETRY_01/SCIENTIFIC_ACCEPTANCE_PLAN.md`
  + `logs/PLAN_FREEZE.json`): T1 ≤1e-8 circle covariance; T2 collapse ≤25%;
  T3 feedback ≤5δ; T4 ellipse ≥max(5×noise, 2%); V-criteria in VERIFICATION_PLAN.md.
  **Never changed after results.**
- Confirmatory vs exploratory strictly labelled (fig5 collapse tests = EXPLORATORY).
- Failed attempts preserved (`CHANGELOG.md`, `REJECTED_IDEAS.md`): an early Laplacian
  implementation had a parity null mode — all its results were discarded and re-earned.
- No fabrication of evidence/references/numbers; unknown reference fields are marked
  TODO in the submission package rather than invented.

## 5. Directory map (this archive)

```
START_HERE.md                  ← you are here
MASTER_PROMPT.md (+VERSION/DATE, PROJECT_CONTROL/)   protocol
DECISION_LOG.md  CHANGELOG.md  VALIDATION_STATUS.md  COMPUTE_STATUS.md
REPRODUCIBILITY_STATUS.md  REJECTED_IDEAS.md  CURRENT_PROJECT_STATE.md
PROJECT_STATE_PHASE_XX.md                          historical phase records
PROJECT_CRYSTAL_GEOMETRY_01/                       ★ THE ACTIVE PROJECT
  PROBLEM_DEFINITION.md  MATHEMATICAL_FORMULATION.md  PARAMETER_TABLE.md
  ASSUMPTIONS.md  NUMERICAL_METHOD_SELECTION.md  SCIENTIFIC_ACCEPTANCE_PLAN.md
  VERIFICATION_PLAN.md  PHYSICAL_VALIDATION_PLAN.md  PRIOR_WORK_COMPARISON_R2.md
  JOURNAL_SCREENING.md  SEARCH_LOG.md
  src/            cg_model.py (materials/rotation), cg_grid.py (mapped grid),
                  cg_ops.py (conservative flux-form operators — core numerics),
                  cg_solver.py (harmonic solves, row equilibration),
                  cg_transient.py (spectral time synthesis)
  run_verify.py   V0–V7 verification suite  (→ data/VERIFY.json)
  run_production.py  38-run confirmatory matrix (→ data/PROD/)
  analyze_production.py  pre-registered criteria + diagnostics (→ data/ANALYSIS.json)
  data/           VERIFY.json  ANALYSIS.json  ANALYSIS_TABLE.md
                  ANALYSIS_EXPLORATORY_SCALING.json  NUMBERS_AUDIT.csv
                  SUPP_*.csv (4)  ENVIRONMENT.json  CODE_FREEZE.json  PROD/ (per-run)
  figures/        fig1_sigma_phi  fig2_D_lambda  fig3_series  fig4_angular
                  fig5_scaling (exploratory) + FIGURE_CAPTIONS.md
  MANUSCRIPT_DRAFT.md          ★ journal-agnostic manuscript (canonical record)
  SUBMISSION_PACKAGE/          IJHMT format pass: manuscript_IJHMT.md (numbered refs),
                               cover_letter.md, title_page.md, declarations.md, README
  SELF_AUDIT_CHECKLIST.md  PROJECT_STATE_PHASE_08..13.md
  logs/           PLAN_FREEZE.json  verify_rerun_v3.log  production_v2.log
PILOT_HUANG_2025_01/           benchmark pilot: reconstruction of a published
                               generalized-thermoelasticity cylinder problem
                               (Huang-2025, DOI 10.1007/s10483-025-3280-7) used to
                               validate the operator family. Start: PILOT_REPORT_FINAL.md
PRE_EXECUTION_REVIEW/          source-verification + environment evidence (pre-execution)
BENCHMARK_SOURCE_REVIEW/ALIT_01/  benchmark source reconstruction (equations/BCs level)
CODE_REVIEW/FEM4_PACKAGE/      static review of a separate FEM package (context only)
HEAT_MODEL_EXPLORATION/        early model-option exploration (decision context)
RESEARCH_READING/              source-verification evidence log (paper extracts omitted —
                               copyright; see note §8)
```

## 6. Reproduce (3 commands, Python 3.13 + numpy/scipy/matplotlib — see data/ENVIRONMENT.json)

```bash
cd PROJECT_CRYSTAL_GEOMETRY_01
python run_verify.py          # V0–V7 → data/VERIFY.json   (~7 min CPU)
python run_production.py      # 38 runs → data/PROD/       (~17 min CPU)
python analyze_production.py  # → data/ANALYSIS.json (byte-identical on re-run)
```

Total compute ≈ 0.7 CPU-h. Code-freeze hashes: data/CODE_FREEZE.json.
Numbers in the manuscript trace to sources via data/NUMBERS_AUDIT.csv.

## 7. Current status & what remains (user-owned)

COMPLETE: literature/gap (bounded search, 2026-09-30), source reconstruction, model +
conservative solver, verification, production, analysis, manuscript v1.0, supplements,
figures, reproducibility close-out, journal screening, IJHMT format pass.
PENDING (only the human author can do): author names/affiliations, completing TODO
reference fields (never fabricated), JCR verification at submission, expert review,
AI-use disclosure confirmation, final submission. Suggested targets: IJHMT (primary),
MDSM (fallback) — see JOURNAL_SCREENING.md + SUBMISSION_PACKAGE/README.md.

## 8. Note on excluded materials

Third-party publisher PDFs and their full-text extracts are NOT in this archive
(copyright). Their identity is preserved via DOIs in PRIOR_WORK_COMPARISON_R2.md /
PARAMETER_TABLE.md and SHA-256 hashes in the workspace EXCLUDED_FILES record. All
quoted equations/BCs needed for verification are recorded inside the review documents.

## 9. If you continue this work, read in this order

1. MANUSCRIPT_DRAFT.md (the science) → 2. data/ANALYSIS.json (the numbers) →
3. DECISION_LOG.md (why the design is what it is) → 4. src/cg_ops.py (the numerics) →
5. SCIENTIFIC_ACCEPTANCE_PLAN.md (the frozen criteria) → 6. SUBMISSION_PACKAGE/README.md
(the remaining human steps).
