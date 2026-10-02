# PROJECT_STATE_PHASE_00 — Project intake (2026-10-01)

MASTER_PROMPT v2.1 · Phase 0 only · **STATUS: PARTIAL** — all four deliverables are written; user-supplied profile and constraint information is still missing and has not been invented (§7).

## 1. Current phase and authorization
- Current phase: 0 (Project Intake), completed by this file. **Next phase: not authorized.**
- The user pasted MASTER_PROMPT v2.1 twice without naming a phase and skipped my phase-choice question. Phase 0 (no compute, no scientific decision) was run on that basis — logged as P0-D001, revocable. Nothing beyond Phase 0 was done.

## 2. What the user asked for
1. "isko aap study kro analysis kro btao isme kya hai aur kya conclusion hai iska" (link to the handoff zip) — DONE (chat analysis + independent code verification).
2. "ab aap isse paper bna skte ho jaise jaise m khu waise" — build a paper from this work, step by step as the user dictates. Then "wait, I'll give a prompt" → the master prompt (2026-10-01).
Working style (handoff D013/D016/D017 + this session): the user dislikes repeated questions and often skips ask_user prompts. Use short copy-pasteable choices; ask only about user-owned decisions (§88).

## 3. Package vs MASTER_PROMPT phases (presence only)
The handoff numbers its own stages "Phases 8–13" (verification → production → analysis → prior-work gate → journal screening → manuscript). In MASTER_PROMPT numbering that content spans Phases 7–13, so the handoff's phase labels cannot be used as-is.

| MP phase | Named deliverables PRESENT | ABSENT (as named) / flags |
|---|---|---|
| 0 Intake | — (created now) | all four Phase-0 files and `RESEARCH_PROFILE.md` were absent. Partly covered by `RESEARCH_READING/`, `PRE_EXECUTION_REVIEW/` |
| 0A-1 / 0A-2 | functional equivalents: `HEAT_MODEL_EXPLORATION/`, `PRE_EXECUTION_REVIEW/`, `BENCHMARK_SOURCE_REVIEW/`, `PRIOR_WORK_COMPARISON_R2.md`, per-folder SEARCH_LOG / EVIDENCE_LOG | CANDIDATE_DIRECTIONS, CANDIDATE_DEEP_ANALYSIS, CLOSEST_FIVE_MATRIX.xlsx, NOVELTY_MATRIX.xlsx, VALIDATION_OPTIONS, COMPUTE_FEASIBILITY, CANDIDATE_RISK_REGISTER. Direction fixed by the user under D013; no §19 shortlist gate recorded |
| 1 Problem definition | PROBLEM_DEFINITION, ASSUMPTIONS, PARAMETER_TABLE, SCIENTIFIC_ACCEPTANCE_PLAN | EQUATION_INVENTORY (folded into MATHEMATICAL_FORMULATION). Stale values (G5); T1 wording ambiguous (G2) |
| 2 V&V design | VERIFICATION_PLAN, PHYSICAL_VALIDATION_PLAN, VALIDATION_STATUS | BENCHMARK_RECONSTRUCTION (pilot folder covers Huang-2025). Physical validation labelled "NOT_AVAILABLE" → should read APPLICABLE — EVIDENCE_UNAVAILABLE (§14) |
| 3 Formulation | MATHEMATICAL_FORMULATION | THERMODYNAMIC_ADMISSIBILITY (one embedded paragraph, no Clausius–Duhem derivation), WELL_POSEDNESS, SYMBOLIC_CHECKS, DIMENSIONAL_AUDIT; EQUATION_TO_CODE_MAP exists only for FEM4 and the pilot |
| 4 Method | NUMERICAL_METHOD_SELECTION | DISCRETIZATION, ALGORITHM, STABILITY_CONSIDERATIONS |
| 5–6 Architecture / implementation | `src/` (5 files) + 3 runner scripts | CODE_ARCHITECTURE. Known defect G1 |
| 7 Basic verification | `run_verify.py` (V0–V7), `data/VERIFY.json`, `logs/` | TEST_REPORT, BASIC_VERIFICATION, UNIT_TESTS/. V3 is blind to G1; no steady-gradient test |
| 8 Validation execution | `PILOT_HUANG_2025_01/` — PILOT, NOT FINAL VALIDATION | VALIDATION_RESULTS. Physical validation unavailable |
| 9 Convergence | V2 (PARTIAL) + 192×96 spot checks in `data/` | CONVERGENCE_REPORT, STABILITY_REPORT, CONVERGENCE_DATA/. No window-length convergence (G3); no ≥3-grid study |
| 10 Baselines / gate | isotropic control (Block D), feedback-off (Block C), Fourier-vs-CV (Block B), `PLAN_FREEZE` | no explicit production-gate document |
| 11 Production | 38 runs (A φ×χ 24, B Λ/size 11, C feedback-off 1, D isotropic 2) + sensitivities, ≈1,039 CPU-s: RUN_SUCCESS as executed | results affected by G1, G3 |
| 12 Analysis | `analyze_production.py`, ANALYSIS.json / _TABLE.md, NUMBERS_AUDIT.csv, SELF_AUDIT_CHECKLIST.md | CENTRAL_STORY. G2, G4 |
| 13 Manuscript | MANUSCRIPT_DRAFT.md v1.0, SUBMISSION_PACKAGE (IJHMT format), fig1–fig5, JOURNAL_SCREENING.md | claims affected (G1–G4); 10 of 11 refs incomplete; abstract ≈234 words |
| §67 packages | — | PACKAGE_PHASE_01…13 none. The recovery zips the handoff cites are not in this package |

## 4. Research problem, type, route
- Problem: transient coupled thermoelastic response around a cavity in monoclinic β-Ga₂O₃ (C2/m), separating (i) material symmetry (13 monoclinic Cij incl. C15, C25, C35, C46; conductivity with off-diagonal K13; anisotropic expansion), (ii) geometric symmetry (circle vs equal-area ellipse, χ = 2), (iii) thermal memory (Fourier vs Cattaneo–Vernotte, τ = 1–20 ps hypothetical; Λ = τκ̄/a², ε = κ̄/(c_ref·a)).
- Setup: plane strain in the a–c plane; Gaussian wall-temperature pulse (t0 = 2.5, tw = 1.2 t_th); traction-free cavity; clamped, cold outer boundary at R = 80a; a = 5–50 nm; stresses reported per kelvin of pulse amplitude.
- Pre-registered in the handoff: H1 circle invariance, H2 ellipse orientation modulation, H3 memory collapse in Λ alone, H4 feedback bound, H5 mode interaction (exploratory); criteria T1–T4 (`SCIENTIFIC_ACCEPTANCE_PLAN.md` item 15).
- Research type: computational scientific study with analytical verification anchors (§15). Novelty/gap: "HOLDS (PROVISIONAL)" per `PRIOR_WORK_COMPARISON_R2.md`.

## 5. Model, assumptions, method (pointers + essentials)
- Equations: `PROJECT_CRYSTAL_GEOMETRY_01/MATHEMATICAL_FORMULATION.md` (linear small-strain coupled thermoelasticity, frequency-domain solver equations, BCs/ICs, nondimensionalization).
- Parameters: Cij from Adachi 2018 and in-plane K = [[12.13, −0.992], [−0.992, 14.09]] W/(m·K) from Klimm 2023 (both match the primary sources); α_a = 1.54e-6, α_c = 3.15e-6 1/K; ρ = 5880 kg/m³; c_p ≈ 560 J/(kg·K) (estimated). Only 9 of the 13 Cij enter the plane-strain problem (C22, C44, C46, C66 do not).
- Method: Python 3.13.14 conservative flux-form finite differences on a mapped grid (96×48; 192×96 spot checks); frequency-domain solves summed by DFT synthesis (26 frequencies over an 8 t_th window); hysteretic damping η_d = 0.05 on dynamic runs. Code freeze: `data/CODE_FREEZE.json` (SHA-256 × 8 files).
- Assumption flags: ASSUMPTIONS.md says MFP 1–2 nm and a continuum limit a ≥ 5 nm — optimistic (`PROJECT_CONSTRAINTS.md` §4).

## 6. Independent findings on the handoff (2026-10-01) — details in `/home/user/work/rerun/REVIEW_FINDINGS.md`
| Handoff claim | Independent re-check | Verdict |
|---|---|---|
| Circle peak hoop stress 0.9666 MPa/K, rotation-invariant | shipped code: peaks 965,440–968,374 Pa/K over φ (0.30% scatter), caused by a sign bug in `rotate_Q_beta`; with the patch: 965,529 Pa/K for every φ (spread 3.2e-10) | bug confirmed (G1); invariance true only after the fix |
| T1 ≤ 1e-8 "PASS (machine class)" | all-φ scatter 3.04e-3; worst 90°-pair 1.58e-3 (`T1_90deg_pair_rel_max`); the reported pair 0°/90° = 4.04e-10 is the one pair where s·c = 0 and the bug is invisible; the status line `… or True` can never fail | FAIL except for that pair (G2) |
| Ellipse modulation 33–37% (36.6% at 96×48, 32.7% at 192×96); σ̂ = 1.125–1.668 MPa/K | patched 96×48: 36.30% (1.1255–1.6646); window 8→64 t_th: modulation proxy 37.9→34.6% | H2 survives qualitatively; the number is unconverged (G3) |
| Absolute stresses (circle 0.9666, ellipse 1.125–1.668 MPa/K; 10 K example 9.67 / 11.25–16.69 MPa) | periodic-DFT synthesis gives the pulse-train steady state. Window 8→64 t_th: circle 967→898 (−7.2%), ellipse φ=90° 1137→1033 (−9.2%), φ=150° 1669→1465 (−12.3%) kPa/K. Isotropic circle: exact single pulse 984.6 vs shipped 1054 (+7%) | inflated ≈7–12% (G3) |
| H3 "not supported"; equal-Λ pair D = 7.36e-3 vs 2.10e-3 → "two-parameter (Λ,ε) map" | inertia off: both 1.9975e-3 (ratio 1.00). D(a = 10 nm) for T = 8, 10, 12, 16, 20, 32 t_th = 7.34, 2.60, 3.68, 4.46, 3.44, 3.24 (×1e-3). Elastic round trip at R = 80a for a = 10 nm = 8.14 t_th ≈ the window | refutation mostly a numerical artifact (G4) |
| Feedback 2.17e-4 ≤ 5δ (δ = 1.078e-3) | consistent with δ ≈ 1e-3 | plausible; NOT re-run |
| V0–V7 PASS (V2 PARTIAL) | 4 production cases re-run reproduce stored values to ≤9e-11; V3 tests only 90°. A steady log-profile gradient test (not in V0–V7) matches the exact −1,234,746 Pa/K with errors −2.90%, −0.87%, −0.24%, +0.006% on 48×24…384×96 (clean 2nd order) | deterministic; solver core sound; V3 blind spot |
| Material data | all 13 Adachi-2018 Cij and Klimm-2023 λ11, λ22, λ33, λ13 match the primary sources; K eigenvalues are 11.72 / 14.50 W/(m·K) (docs: 11.36 / 14.86; axis 22.7°, not 25.5°) | OK; documentation error |

## 7. Gates before manuscript claims (§78, §80)
- **G1 — rotation bug.** `cg_model.py` `rotate_Q_beta`: the `C23p` cross-term `2*s*(-c)*C25` must be `+2*s*c*C25` (β₃ off by up to 0.17% for φ ∉ {0°, 90°}). Patch ready and ANALYTICALLY_CHECKED (agrees with an independent 3-D rotation to 1.6e-16), NOT adopted. Required: document (DECISION_LOG/CHANGELOG), re-run the V-suite (the handoff's own code-freeze rule), add a 45° lattice test (shipped 3.0e-3 vs patched 2e-9).
- **G2 — T1 reporting.** Remove `or True`; state which (φ, φ′) set T1 covers; separate exact grid-aligned rotations from O(h²) continuous rotations (production φ = 0…165° in 15° steps, NT = 48, so all production rotations are grid-aligned and must be exact); retract the "argmax sampling on a flat peak" note (refuted).
- **G3 — synthesis artifact.** Replace the periodic synthesis by an artifact-free single-pulse response (window ≥ 64 t_th with quasi-static elasticity, or a complex-frequency shift with an absorbing or larger outer boundary). **Methodological change → user approval (§88).** Then re-run Blocks A–D, with ≥3-grid and window-length convergence.
- **G4 — H3.** Redo on the corrected synthesis (inertia on/off, damping variants); rewrite the H3 text, abstract, cover letter and highlights — the "two-parameter map" claim is currently unsupported.
- **G5 — documentation.** K eigenvalues; "21 frequencies" vs 26 used; stale values in ASSUMPTIONS / PARAMETER_TABLE (R = 25a, tanh clustering, 48–64 frequencies, δ ≈ 4e-4, c_ref 7676, NOT_STARTED lines); fallback-journal naming; 10 of 11 references incomplete; abstract length vs the IJHMT limit (unverified); Data-availability pointing to an archive that is not in the package; continuum-validity framing.

## 8. Verification and validation status (kept separate, §63)
- Verification: **PARTIAL.** V0–V7 as recorded (V2 PARTIAL); the T1 component FAILED (G1/G2); V3 is blind to the bug; determinism confirmed (≤9e-11); steady-gradient check passes (my test, not part of the handoff suite).
- Physical validation: **APPLICABLE — EVIDENCE_UNAVAILABLE.** Source-case pilot (Huang-2025, CV/MCV3): PILOT — NOT FINAL VALIDATION — 175/177 digitized points within the envelope; Cohen-80 inversion cross-check FAILED (retained); CV refinement 1600→3200 criterion failed, extension 3200→6400 passed (both retained).

## 9. Code status
`PROJECT_CRYSTAL_GEOMETRY_01/src/` + `run_verify.py`, `run_production.py`, `analyze_production.py` (Python 3.13.14, numpy 2.3.5, scipy 1.17.1). Defects: G1 (code), G2 (analysis script). Patch: `/home/user/work/rerun/rotate_Q_beta_fix.diff`; patched file `/home/user/work/rerun/fixed_src/cg_model.py`; unfixed working copy `/home/user/work/rerun/proj/`. Handoff originals are untouched.

## 10. Compute status
Phase 0: no computation. Handoff total ≈0.6 CPU-h (`COMPUTE_STATUS.md`); my review runs not CPU-logged (≈22 min wall-clock span). Sandbox: 2 vCPU / 2 GB / no GPU. Thresholds: 4 CPU-h / 1 GPU-h / 5 GB (§43). Corrected re-run estimate: NOT_RUN (Phase 10 gate).

## 11. Decisions, approvals, rejected ideas
- Handoff history D001–D018 (`/home/user/work/handoff/DECISION_LOG.md`), especially D012, D013, D014, D015, D017.
- This phase: P0-D001…P0-D005 (`DECISION_LOG.md` in this folder).
- Approvals valid now: none for Phase ≥ 1. D013 and D017 are earlier-session approvals awaiting the user's confirmation.
- Rejected / refuted: the handoff's early composed-Laplacian discretization (parity null mode; see handoff `REJECTED_IDEAS.md`); the handoff's explanation of the T1 scatter as "argmax sampling on a flat peak" (cause is G1).

## 12. Unresolved issues
G1–G5 above; the open information requests in `PROJECT_CONSTRAINTS.md` §7; the privacy decision on the public repo; journal reconfirmation (IJHMT primary, fallback naming unclear); JCR verification (no access); expert review (§84).

## 13. Exact next action
Wait for the user's explicit authorization of the next phase. Options offered:
1. `Follow MASTER_PROMPT.md. Continue from Phase 7 only.` → apply the fix, drop `or True`, add the 45° and steady-gradient tests, re-run the V-suite, then STOP (convergence = Phase 9 next).
2. `Follow MASTER_PROMPT.md. Continue Phases 7→13 under D013.` → proceed without repeated questions; stop only at user-owned gates (approval of the synthesis-method change, compute > 4 CPU-h, journal, submission).
3. `Follow MASTER_PROMPT.md. Phase 13 only, shipped numbers.` → conflicts with §78/§89; only on explicit override, with known issues flagged in the text.

## 14. File references
- This phase: `/home/user/PAPER_PROJECT/00_Project_Control/` — MASTER_PROMPT.md (+VERSION, DATE), PROJECT_STATE_PHASE_00.md, INPUT_INVENTORY.md, PROJECT_CONSTRAINTS.md, TOOL_AVAILABILITY.md, DECISION_LOG.md, CHANGELOG.md; `/home/user/PAPER_PROJECT/README.md`.
- Baseline (read-only): `/home/user/work/handoff/` (start at START_HERE.md, `PROJECT_CRYSTAL_GEOMETRY_01/`, root DECISION_LOG / COMPUTE_STATUS / VALIDATION_STATUS / REPRODUCIBILITY_STATUS).
- Review area: `/home/user/work/rerun/` — REVIEW_FINDINGS.md, rotate_Q_beta_fix.diff, fixed_src/, tests, logs.
