# PROJECT_PROGRESS — `vipin-oss/le`

Branch: `arena/01a0f67f-le` · updated 2026-10-01 · source: `le.zip` (52,189,612 B,
sha256 `5e780e1fd6292690c1b56ad378dc35c9737e52cd873e4f18e610cfdf45bb0363`)

- Repository audit: **[`docs/PHASE1_AUDIT.md`](docs/PHASE1_AUDIT.md)**
- Re-run comparison: `RERUN_COMPARISON.md` (written after the re-run completes)

---

## What this project is

`PAPER_PROJECT` — *"verified continuum study of cavity thermoelasticity in monoclinic β-Ga₂O₃"*
under **MASTER_PROMPT v2.1** (90 sections). Transient coupled thermoelasticity around a circular vs
equal-area elliptical cavity (χ = 2) in the a–c plane of monoclinic β-Ga₂O₃; Fourier /
Lord–Shulman / two-relaxation-time conduction; frequency-domain mapped-grid FD solver +
**Bromwich inversion** for the single-pulse response; target journal IJHMT (user-owned).
`work/handoff/` = read-only input baseline (303 files, SHA-256 303/303 verified),
`work/rerun/` = prior review area.

---

## Phase status

| Phase | Status |
|---|---|
| PHASE 1 — repository audit | **COMPLETE** |
| PHASE 2 — consistency check | **COMPLETE** (findings below) |
| PHASE 3 — continue pending work | in progress: full re-run, then final delivery |
| PHASE 4 — validation of re-run | **in progress** (verification suite done; production running) |
| PHASE 5 — persistence | ongoing (committed each stage) |
| PHASE 6 — final delivery | pending (three missing deliverables) |

---

## PHASE 2 — consistency check (findings)

### Code vs documented formulation — all consistent
Read `06_Source_Code/src/*.py` against `04_Theory/FORMULATION_ADDENDUM.md`,
`05_Numerical_Method/NUMERICAL_METHOD_V2.md` and `13_Manuscript/manuscript_IJHMT.md`:

| Item | Checked | Result |
|---|---|---|
| Constitutive law | σ = Qε − βθ; Q = plane-strain block (C11,C13,C15,C33,C35,C55); β = Cα incl. C12,C23,C25 via α_b | ✅ matches §2.1 |
| Momentum | div σ + ρω²u = 0 (exp(+iωt), so ω² term), `inertia_scale` switches it off | ✅ |
| Heat equation | div(K g ∇θ) = iω(ρc_pθ + T₀β:ε); g = 1 / 1/(1+iωτ) / ½/(1+½iωτ)+½/(1+2iωτ) | ✅ matches §2.1 and `gfac()` |
| BCs | cavity: θ = 1 (unit transfer), traction-free rows from n·σ; outer R = 80a: θ = 0, u = 0 | ✅ matches §2.1 |
| ICs | quiescent medium: two-sided Laplace Gaussian P(s) = √π t_w exp((s t_w/2)² − s t₀) | ✅ derived independently, matches `cg_bromwich.py` |
| Bromwich inversion | y(t) = e^{γt}/T [Y(γ) + 2Re Σ_{k≥1} Y(s_k)e^{iω_k t}], conjugate symmetry | ✅ derived independently, matches |
| Solver ↔ Laplace map | w = −i s/t_th so iω = s/t_th, ω² = −s²/t_th² | ✅ |
| Rotation fix (G1) | C12′ = c²C12+s²C23−2sc C25; C23′ = s²C12+c²C23+**+2sc**C25; C25′ = sc(C12−C23)+(c²−s²)C25 | ✅ all three derived independently from C′=RCRCᵀ |
| κ̄, δ, c_ref | √(det K)/(ρc_p) = 3.958e-6 m²/s; T₀β·β/(ρc_pC̄) = 1.0782e-3; √(C33/ρ) = 7686.6 m/s | ✅ matches manuscript §2.2 (3.959e-6, 1.078e-3, 7686) |
| Pulse / QoI | t₀ = 2.5, t_w = 1.2 t_th; QoI window t ≤ 6; 12 orientations 0…165° | ✅ matches pre-registration |
| Grid | γ_grid = 5 (P9-D001), R = 80a, `refine = 2`, T = 20, γ_B = 0.9 → K = 26, 27 solves | ✅ matches P9-D001 / P11 and CORRECTIONS_LOG #8 |
| Ablation α sets | baseline (1.54, 3.37, 3.15)e-6; cheng298-like (0.10, 0.20, 0.20)e-6 (labelled sensitivity-only) | ✅ |

### Manuscript claims vs `10_Processed_Data/ANALYSIS_V2.json` — all consistent
| Claim | Delivered data |
|---|---|
| Circle peak 0.854 MPa/K | `circle_peak.radial_interp.f_ext` = 853,900 Pa/K = 0.8539 MPa/K |
| Circle orientation-invariant, spread 4.6e-15 | `T1_H1.M_sig_nodal.spread_rel` = 4.64e-15 |
| Ellipse modulation 28.7% (M, 12φ: 29.9%; u_num 1.31 pp) | 0.28749 / 0.29870 / 0.013111 |
| D ≤ 6.4% (≤1.6% for a ≥ 10 nm), peak shift ≤ 1.4% | max D = 0.06380 (a=5 nm); max_{a≥10} = 0.01569; max \|peak shift\| = 0.0096 |
| T2 quasi-static SUPPORTED (residual 0.0%), dynamic NOT-SUPPORTED (51.6%) | `pair_QS.residual` = 0.0; `pair_dynamic.residual` = 0.51584 |
| T3 feedback WITHIN-BOUND | 6.19e-4 vs 5δ = 5.39e-3 |
| Ablation amplitude ratios K 0.94 / C 1.57 / α_iso 0.72 / α_cheng 1.03 | 0.938 / 1.572 / 0.717 / 1.031 |
| Pulse-width A₂ = 24.8, 27.7, 30.0, 32.0 % | 0.2483, 0.2767, 0.3001, 0.3198 |
| Isotropic ellipse ≈ 1.5× isotropic circle | `ellipse_M_over_circle_T48` = 1.531 |
| Closed-form reference 0.985 MPa/K | 985,689.45 Pa/K — equals the V11 reference peak 985689.4485743708 |
| Abstract "0.08% at the finest grid" | V9d worst-law 192×96 = 0.0755% ≈ 0.08% (V11 = 0.0666%); §4 table states both |

### Issues found (documented, not silently changed)
1. **Stale code freeze.** `CODE_FREEZE_v2_blockF.json` (07:39:17) has 3 mismatches:
   `13_Manuscript/{build_manuscript,ms_results,ms_static}.py` were edited after the freeze
   (they implement the CORRECTIONS_LOG corrections) — no addendum recorded.
   The 5 mismatches vs `CODE_FREEZE_v2_gate.json` are the documented block-F + P12-D001 changes.
2. **Hard-coded absolute paths.** 15 scripts use `/home/user/PAPER_PROJECT` and
   `/home/user/work/handoff`; three of them are frozen files, so they were **not** patched.
   `bootstrap_paths.sh` (repo root) recreates the expected paths with symlinks; all freeze
   hashes still verify (e.g. `cg_pipeline.py` = `50ae282c…`).
3. §74 items belonging to non-re-opened phases 0–2 are absent (`RESEARCH_PROFILE.md`,
   `SCIENTIFIC_ACCEPTANCE_PLAN.md`, `NOVELTY_MATRIX.xlsx`) — user decision, not to be invented.

---

## PHASE 4 — re-run (user chose "full re-run"; P7-D002 confirmed by the user)

Environment installed to match the recorded one: numpy 2.3.5, scipy 1.17.1, matplotlib 3.10.9,
python-docx 1.1.2, openpyxl 3.1.5 (Python is 3.11.2, recorded 3.13.14 — MP §75 permits
non-bitwise reproduction across environments).

### Verification suite — **DONE, reproduces**
```
python3 07_Tests/run_tests.py            -> 25 PASS, 1 FAIL   (cpu 1178 s, wall 1180 s)
python3 07_Tests/run_tests_supplement.py -> appends V0b: PASS -> 26 PASS, 1 FAIL, 1 INFO
```
Delivered: 26 PASS / 1 FAIL / 1 exploratory — **identical** (V0b is in the supplement script,
so it is absent until that script is run — this is a script-layout fact, not a discrepancy).
Bit-identical examples: V11 `reference_peak_Pa_per_K` = 985689.4485743708;
V9a `worst_192` = 0.0008712698489962431; V9e `worst_rel_err_192` = 0.012998607775645632;
V0 χ=2 @96×48 = 5.0279e-3 (the documented failing criterion); V0b `worst_production_grids`
= 0.003575961642985348.

### Production — running
Delivered outputs were snapshotted to `baseline_provided/` (405 files) **before** clearing
`09_Raw_Data/production/` (300 files) and `09_Raw_Data/convergence/` (36 files) so that
nothing cached is reused. `09_Raw_Data/convergence_gamma3p5/` (34 files) was **kept**: it is a
partial study with no regenerator script in the package.
Two workers started exactly as the README prescribes:
```
python3 08_Experiments/run_production_v2.py heavy    # 14 heavy + helps with the rest
python3 08_Experiments/run_production_v2.py light    # medium + light only
```
150 jobs (A 68, B 11, BQS 12, BM 3, B2 14, B2QS 4, C 1, D 4, E 24, F 9).
Logs: `08_Experiments/logs/production_{heavy,light}_RERUN_arena_2026-10-01.log`.

---

## Files created / modified this session

| File | Action |
|---|---|
| `docs/PHASE1_AUDIT.md` | created — full Phase-1 audit |
| `PROJECT_PROGRESS.md` | created/updated — this record |
| `bootstrap_paths.sh` | created — idempotent symlink bootstrap (does not touch frozen files) |
| `tools/compare_rerun.py` | created — delivered-vs-recomputed comparison harness |
| `.gitignore` | created — `work/handoff.zip`, `PAPER_PROJECT/packages/`, `__pycache__/` |
| `PAPER_PROJECT/**`, `work/**` | added unmodified (extracted from `le.zip`) |
| `baseline_provided/` | created — safety snapshot of delivered outputs (git-ignored) |
| `07_Tests/TEST_RESULTS.json` | **regenerated** by the re-run |
| `09_Raw_Data/{production,convergence}/` | **regenerated** by the re-run |

## Tests performed
- `le.zip` integrity (git blob hash) — PASS
- handoff baseline 303/303 SHA-256 — PASS
- verification suite re-run — 26 PASS / 1 FAIL / 1 INFO, matches delivered
- supplement (V0b) — PASS, bit-identical
- production re-run — running

## Unresolved issues
- Post-freeze edits to 3 manuscript builder scripts need a freeze addendum (pending, Phase 3).
- `baseline_provided/` and `PAPER_PROJECT/packages/` are git-ignored (see `.gitignore`).
- User-owned open items: authors/affiliations/CRediT/funding/conflicts, AI-use declaration,
  repository DOI + licence, final journal, JCR verification, independent expert review.

## Exact next action
1. Wait for both production workers; then run
   `run_convergence.py` and `run_convergence_dirs.py 30`.
2. Run `analyze_v2.py`, `make_figures.py`, `13_Manuscript/build_manuscript.py`, `reproduce.py`.
3. Run `tools/compare_rerun.py` → `RERUN_COMPARISON.md`; record P7-D002 confirmation and the
   new code-freeze addendum in `DECISION_LOG.md` / `CHANGELOG.md`.
4. Build the three missing deliverables: `00_Project_Control/PROJECT_STATE_FINAL.md`,
   `packages/PACKAGE_PHASE_07…13.zip`, `packages/RESEARCH_PROJECT_FINAL.zip`;
   update `README.md` / `CHANGELOG.md`.
