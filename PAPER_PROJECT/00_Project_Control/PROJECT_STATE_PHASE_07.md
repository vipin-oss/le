# PROJECT_STATE_PHASE_07 — Basic verification (2026-10-01)

## Phase 7 — status PASS (with one reported FAIL)
**Completed:** `rotate_Q_beta` fixed (U0/U1: 1.5e-16 vs independent 3-D rank-4 rotation; shipped 1.7e-3); `inertia_scale` and `refine=2` added to the solver; Bromwich single-pulse module and independent 1-D references (Chebyshev Laplace-domain; Crank–Nicolson time-domain) implemented; verification suite `07_Tests/run_tests.py`: **26 PASS, 1 FAIL** (V0 on the handoff grid family: χ = 2, 96×48 = 5.03e-3 vs 5e-3; V0b on the production grids PASS).
**Key findings:** rotation covariance exact to 6e-14 (θ, u, wall hoop) for every grid-aligned φ; shipped rotation fails at 3.0e-3 and the old V3 was blind (units-mixed normalisation, φ = 90° only); round-off floor 1e-8 removed by iterative refinement.
**Files:** `07_Tests/TEST_REPORT.md`, `TEST_RESULTS.json`, `logs/`, `diagnostics/`; `06_Source_Code/`.
**Next:** Phase 8 (verification against references), Phase 9 (convergence).

## Common context (self-contained recovery summary, MASTER_PROMPT §65)
- **Project:** β-Ga₂O₃ cavity thermoelasticity (circular vs equal-area elliptical cavity, monoclinic crystal, a–c plane, Fourier / Cattaneo–Vernotte / two-relaxation-time conduction) → verified continuum parametric study; target manuscript for IJHMT (journal choice user-owned; D017 working target).
- **Research type / evidence route:** computational scientific study with analytical verification anchors (§15). Verification (Track A): exact + independent 1-D references, grid studies. Physical validation: **APPLICABLE — EVIDENCE_UNAVAILABLE**.
- **Equations / assumptions / method:** `04_Theory/FORMULATION_ADDENDUM.md`, `05_Numerical_Method/NUMERICAL_METHOD_V2.md`; model unchanged from the handoff; time reconstruction by Bromwich inversion (P7-D002, **flag for user**); undamped; grid γ = 5 (P9-D001).
- **Baseline:** `/home/user/work/handoff/` (read-only, 304 files, 303/303 SHA-256). Handoff defects fixed: rotate_Q_beta sign (G1), T1 forced PASS (G2), periodic-synthesis artefact (G3), H3 evaluated on the artefact and on the full window (G4), documentation (G5).
- **Approvals:** D013 blanket authorization for phases 1→13 (user message 2026-10-01 "Continue Phases 7→13 under D013"); user-owned: model changes, compute > 4 CPU-h, journal, submission.
- **Decision / change history:** `DECISION_LOG.md`, `CHANGELOG.md` (this folder); handoff D001–D018 in the handoff.
- **Rejected ideas:** `REJECTED_IDEAS.md` (this folder).
