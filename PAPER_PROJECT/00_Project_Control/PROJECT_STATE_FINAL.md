# PROJECT_STATE_FINAL — PAPER_PROJECT (MASTER_PROMPT §74)

**2026-10-01** · MASTER_PROMPT v2.1 · repository `vipin-oss/le`, branch `arena/01a0f67f-le`
Recovery summary for a reader who starts here.

---

## 1. Project

*Orientation-dependent wall stress around circular and elliptical cavities in monoclinic β-Ga₂O₃
under a transient thermal pulse: a verified continuum study with thermal-memory and mechanism
ablations.*

Linear small-strain coupled thermoelasticity, plane strain in the a–c plane of monoclinic β-Ga₂O₃
(C2/m): circular cavity vs equal-area ellipse (χ = 2), crystal rotated by φ ∈ [0°, 165°]; Gaussian
wall-temperature pulse (t₀ = 2.5 t_th, t_w = 1.2 t_th), traction-free cavity wall, clamped + cold
outer boundary at R = 80a, a = 5–50 nm; Fourier, Cattaneo–Vernotte (Lord–Shulman) and a
two-relaxation-time conduction law (τ hypothetical). Frequency-domain conservative flux-form
finite differences on a body-fitted mapped grid, single-pulse time response obtained by Bromwich
inversion on Re s = 0.9/t_th.

**Research type** (§15): computational scientific study with analytical verification anchors.
**Physical validation: APPLICABLE — EVIDENCE_UNAVAILABLE** — no transient measurements around
cavities in β-Ga₂O₃ (or any monoclinic crystal) exist; every claim is restricted accordingly.

## 2. Phase status

| Phase | Status | Evidence |
|---|---|---|
| 0 Intake | PARTIAL | `PROJECT_STATE_PHASE_00.md`; user profile information deliberately not invented |
| 1–6 | NOT RE-OPENED | superseded; corrected in `04_Theory/FORMULATION_ADDENDUM.md`, `05_Numerical_Method/NUMERICAL_METHOD_V2.md` |
| 7 Basic verification | PASS (1 reported FAIL) | 26 PASS / 1 FAIL / 1 exploratory; `07_Tests/TEST_REPORT.md` |
| 8 Validation execution | PASS (verification) | R1–R9, `03_Validation/VALIDATION_RESULTS.md` |
| 9 Convergence | PASS | C2/C3/C4, `05_Numerical_Method/CONVERGENCE_REPORT.md`, `STABILITY_REPORT.md` |
| 10 Baselines + gate | PASS | `02_Problem_Definition/ACCEPTANCE_CRITERIA_V2_FROZEN.md`, `CODE_FREEZE_v2_gate.json` |
| 11 Production | PASS | 150 runs (141 gate + 9 block F), `10_Processed_Data/PRODUCTION_PROVENANCE.csv` |
| 12 Analysis | PASS with an honest negative | `10_Processed_Data/ANALYSIS_V2.json`, `ANALYSIS_V2_TABLES.md` |
| 13 Manuscript | PARTIAL (draft complete) | `13_Manuscript/manuscript_IJHMT.docx/.md`; user-owned items open |

## 3. Principal results (all recomputed 2026-10-01, `RERUN_COMPARISON.md`)

| Result | Value |
|---|---|
| Verification of the single-pulse Bromwich route | peak error 0.08 % at 192×96 vs an independent time-domain solution, order ≈ 2 |
| Circle peak wall stress | **0.854 MPa/K** (3-grid extrapolation; grid M error −0.03 %) |
| Circle orientation invariance (T1) | spread 4.6e-15 → PASS |
| Ellipse orientation modulation (T4) | **28.7 %** extrapolated (29.9 % on grid M), u_num = 1.31 pp → RESOLVABLE |
| Thermal memory (T2) | D ≤ **6.4 %** (≤ 1.6 % for a ≥ 10 nm), peak shift ≤ 1.4 %; quasi-static collapse in Λ exact (residual 0.0 %), dynamic residual 51.6 % → NOT-SUPPORTED as pre-registered, explained by an O(ε²) inertia correction |
| Thermoelastic feedback (T3) | 6.2e-4 vs bound 5δ = 5.4e-3 → WITHIN-BOUND |
| Ablations (exploratory) | amplitude ratios K_iso 0.94, C_iso 1.57, α_iso 0.72, α_cheng298-like 1.03 |
| Pulse-width test | A₂ = 24.8 / 27.7 / 30.0 / 32.0 % for t_w = 0.3 / 0.6 / 1.2 / 2.4 — the local (thin-layer) interpretation is **not** supported |
| Stress scale | uncertain by a factor ≈ 16 between two literature-based expansion sets |

## 4. Reproducibility

Environment of record: Python 3.13.14, numpy 2.3.5, scipy 1.17.1, matplotlib 3.10.9,
python-docx 1.1.2, openpyxl 3.1.5, Linux x86_64, 2 vCPU / 2 GB.
Re-run performed 2026-10-01 on **Python 3.11.2** with the same library versions: every scientific
quantity reproduced **bit-identically** (150/150 runs, max QoI relative difference 0.0; 669
analysis leaves within 1e-9; 8 figures and 5 tables byte-identical; manuscript byte-identical).
Only CPU/wall timings differ.

```sh
sh bootstrap_paths.sh                       # recreate /home/user/{PAPER_PROJECT,work} (see R-D004)
python3 07_Tests/run_tests.py               # ≈ 20 min
python3 07_Tests/run_tests_supplement.py    # appends V0b
python3 08_Experiments/run_production_v2.py heavy &  python3 08_Experiments/run_production_v2.py light
python3 08_Experiments/run_convergence.py ; python3 08_Experiments/run_convergence_dirs.py 30
python3 08_Experiments/analyze_v2.py && python3 08_Experiments/make_figures.py && python3 13_Manuscript/build_manuscript.py
python3 08_Experiments/reproduce.py         # 11 PASS / 0 FAIL
python3 tools/compare_rerun.py              # delivered vs recomputed
python3 06_Source_Code/make_code_freeze.py <label>
python3 00_Project_Control/make_packages.py final
```
Run one heavy (192×96 / 96×144) job at a time — they need ≈ 0.7–1.0 GB.

## 5. Deviations and decisions

`DECISION_LOG.md`: handoff D001–D018; this project P0-D001…P0-D005, P7-D001…P7-D004,
P9-D001/D002, P10-D001, P11-D001, P12-D001, P13-D001; continuation session
**P7-D002 user-confirmed**, **R-D001** (full re-run), **R-D002** (one-line portability edit in
`13_Manuscript/ms_results.py`, output-identical), **R-D003** (`CODE_FREEZE_v2_final.json`
addendum), **R-D004** (`bootstrap_paths.sh` instead of patching frozen files).

## 6. Known limitations

- No physical validation; τ hypothetical; continuum validity at 5–50 nm not established;
  c_p estimated; α uncertain by > 10×; plane strain; Dirichlet wall temperature; α₅ = 0.
- Thermal-memory runs exist for the circular cavity only; block E ablations are exploratory
  and were run on grid T48 (96×48).
- `09_Raw_Data/convergence_gamma3p5/` is a partial γ = 3.5 study with no regenerator script.
- §74 items belonging to phases 0–2 (`RESEARCH_PROFILE.md`, `SCIENTIFIC_ACCEPTANCE_PLAN.md`,
  `NOVELTY_MATRIX.xlsx`) are absent; those phases were not re-opened and nothing was invented.

## 7. Open items — user-owned

Authors, affiliations, CRediT, funding, competing interests; confirmation/editing of the AI-use
declaration template; public repository, licence and DOI; final journal decision (working target
IJHMT, `13_Manuscript/JOURNAL_FIT.md`); JCR verification; independent expert review (§84);
privacy decision about a public repository holding an unpublished manuscript.

## 8. Archives

`packages/PACKAGE_PHASE_07…13.zip` (cumulative, reconstructed at the end of the session, each with
a `MANIFEST.json` of SHA-256 per file) and `packages/RESEARCH_PROJECT_FINAL.zip` (whole
`PAPER_PROJECT`, excluding `packages/`). Built by `00_Project_Control/make_packages.py [final]`.
