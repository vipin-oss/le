# PHASE 1 — Repository Audit (final)

Date: 2026-10-01 · branch `arena/01a0f67f-le` · source: `le.zip` from `vipin-oss/le@main`

---

## 0. How `le.zip` was obtained

The repository was empty (single 5-byte `README.md`, commit `10a9e2f`) when this session
started. The user then pushed `le.zip` to `main` (commit `7409c7d`).

| Item | Value |
|---|---|
| File | `le.zip`, `main`, blob `297f5dcb0f91a2ded1b7a03592637d363db627b2` |
| Size | 52,189,612 bytes (985 entries, 2 top-level dirs) |
| sha256 | `5e780e1fd6292690c1b56ad378dc35c9737e52cd873e4f18e610cfdf45bb0363` |
| Fetch | `git cat-file -p 297f5dcb > /tmp/le.zip` (`raw.githubusercontent.com` unreachable from the sandbox: TLS error 35) |
| Integrity | re-hashed with `git hash-object` → identical to the blob id ⇒ byte-exact |
| Extracted to | repo root: `PAPER_PROJECT/` (32 MB) + `work/` (21 MB) |

The local copy of `le.zip` was deleted after extraction (it stays on GitHub `main`);
`work/handoff.zip` (6.9 MB) is git-ignored because `work/handoff/` is the verified copy.

---

## 1. What the project is

**`PAPER_PROJECT`** — *"verified continuum study of cavity thermoelasticity in monoclinic
β-Ga₂O₃"* (`PAPER_PROJECT/README.md`), built under **MASTER_PROMPT v2.1**
(`00_Project_Control/MASTER_PROMPT.md`, 1,838 lines, 90 numbered sections).

- **Physics.** Linear small-strain coupled thermoelasticity, plane strain in the a–c plane of
  monoclinic β-Ga₂O₃ (C2/m). Circular cavity vs equal-area ellipse (axis ratio χ = 2),
  crystal rotated by φ. Gaussian wall-temperature pulse (t₀ = 2.5 t_th, t_w = 1.2 t_th),
  traction-free cavity wall, clamped + cold outer boundary at R = 80a, a = 5–50 nm.
  Fourier / Cattaneo–Vernotte (Lord–Shulman) / two-relaxation-time conduction (τ hypothetical).
- **Numbers.** κ̄ = 3.959e-6 m²/s; t_th = a²/κ̄; Λ = τκ̄/a²; ε = κ̄/(c_ref·a), c_ref = 7686 m/s;
  δ = 1.078e-3; Cij (Adachi 2018), K = [[12.13, −0.992], [−0.992, 14.09]] W/(m·K) (Klimm 2023),
  α_a = 1.54e-6, α_c = 3.15e-6 1/K, ρ = 5880 kg/m³, c_p ≈ 560 J/(kg·K).
- **Method.** Conservative flux-form finite differences on a mapped polar grid; frequency-domain
  solves at complex s on Re s = 0.9/t_th; **single-pulse time response by Bromwich inversion**
  (replaces the handoff's periodic-DFT synthesis, P7-D002); production grid 96×96, radial
  clustering γ = 5, outer radius 80a, `refine = 2` iterative refinement.
- **Evidence route** (MP §15): computational study with analytical verification anchors.
  Verification Track A (exact + independent 1-D references, grid studies).
  **Physical validation: APPLICABLE — EVIDENCE_UNAVAILABLE** (no experimental data exist).
- **Target journal:** IJHMT (user-owned decision, handoff D017).

`work/` is **not** project output — it is the read-only **input baseline** (`work/handoff/`,
the 2026-09-30 handoff) plus the previous session's review area (`work/rerun/`).

---

## 2. Directory inventory (985 files)

| Path | Files | Content |
|---|---|---|
| `PAPER_PROJECT/00_Project_Control` | 22 | MASTER_PROMPT v2.1 (+VERSION/DATE), CENTRAL_STORY, DECISION_LOG, CHANGELOG, EVIDENCE_LOG, INPUT_INVENTORY, PROJECT_CONSTRAINTS, TOOL_AVAILABILITY, REJECTED_IDEAS, VALIDATION/COMPUTE/REPRODUCIBILITY_STATUS, `PROJECT_STATE_PHASE_00` and `_07…_13`, and 4 generator scripts |
| `01_Literature` | 7 | REFERENCES_VERIFIED (.md/.json), 2 Crossref verification outputs, SEARCH_LOG, 3 scripts |
| `02_Problem_Definition` | 1 | ACCEPTANCE_CRITERIA_V2_FROZEN.md |
| `03_Validation` | 2 | VALIDATION_RESULTS.md (R1–R9) + generator |
| `04_Theory` | 1 | FORMULATION_ADDENDUM.md |
| `05_Numerical_Method` | 4 | NUMERICAL_METHOD_V2.md, CONVERGENCE_REPORT.md, STABILITY_REPORT.md, generator |
| `06_Source_Code` | 13 | `src/cg_{bromwich,grid,model,ops,pipeline,ref1d,solver,transient}.py`, CODE_FREEZE_v2_gate.json, CODE_FREEZE_v2_blockF.json, DIFF_VS_HANDOFF.txt, generator |
| `07_Tests` | 12 | run_tests.py, supplement, TEST_RESULTS.json, TEST_REPORT.md, BASIC_VERIFICATION.md, REPRODUCTION_TEST_REPORT.md, 4 logs, 1 diagnostic |
| `08_Experiments` | 15 | production_matrix.py, run_production_v2.py, run_convergence{,_dirs}.py, analyze_v2.py, make_figures.py, make_provenance.py, reproduce.py, 5 logs |
| `09_Raw_Data` | 300+70 | `production/` 150 json + 150 npz; `convergence/` 18 json + 18 npz; `convergence_gamma3p5/` 17 json + 17 npz |
| `10_Processed_Data` | 4 | ANALYSIS_V2.json (29 kB), ANALYSIS_V2_TABLES.md, CONVERGENCE_RESULTS.json, CONVERGENCE_DIRS.json, PRODUCTION_PROVENANCE.csv |
| `11_Figures` | 8 | fig1_setup … fig7_pulse_width (png) |
| `12_Tables` | 5 | phi_sweep_ellipse.csv, D_lambda_eps.csv, ablations_E.csv, convergence_ellipse_6phi.csv, pulse_width_F.csv |
| `13_Manuscript` | 12 | manuscript_IJHMT.docx/.md, SUPPLEMENTARY_TABLES.xlsx, cover_letter.md, highlights.txt, JOURNAL_FIT.md, MANUSCRIPT_STATS.json, equations/eq01–03.png, 4 builders |
| `14_Documentation` | 2 | CORRECTIONS_LOG.md + generator |
| `15_Audits` | 4 | AUDIT_PRE_PRODUCTION, AUDIT_PRE_MANUSCRIPT, AUDIT_FULL_PROJECT, AUDIT_FINAL_ADVERSARIAL |
| `work/handoff` | 304 | **pristine input baseline** (303 files + MANIFEST_SHA256.json) |
| `work/rerun` | 187 | previous session's review area (REVIEW_FINDINGS.md, rotate_Q_beta_fix.diff, fixed_src/, tests, logs, unfixed `proj/`) |

---

## 3. What has already been completed

Per `README.md`, `CHANGELOG.md`, `DECISION_LOG.md` and the phase states (all dated 2026-10-01):

| Phase | Status | Deliverables present |
|---|---|---|
| 0 Intake | PARTIAL | PHASE_00 state, INPUT_INVENTORY, PROJECT_CONSTRAINTS, TOOL_AVAILABILITY (user profile information still missing, deliberately not invented) |
| 1–6 | **not re-opened** (superseded) | corrected in `04_Theory/FORMULATION_ADDENDUM.md` + `05_Numerical_Method/NUMERICAL_METHOD_V2.md` |
| 7 Basic verification | PASS (1 reported FAIL) | rotation bug G1 fixed & tested, `refine`/`inertia_scale`, Bromwich module + 1-D references, 26 PASS / 1 FAIL |
| 8 Validation execution | PASS (verification) | R1–R9; physical validation = APPLICABLE — EVIDENCE_UNAVAILABLE |
| 9 Convergence | PASS | C4 mesh-direction study (γ 3.5 → 5), C2/C3, Richardson families R48/T48/M/R192/T144 |
| 10 Baselines + gate | PASS | criteria frozen, code frozen (`CODE_FREEZE_v2_gate.json`), production matrix 141 runs, pre-production audit |
| 11 Production | PASS | **150** runs (141 gate + 9 block F) json+npz, PRODUCTION_PROVENANCE.csv |
| 12 Analysis | PASS (honest negative) | ANALYSIS_V2.json / _TABLES.md, CENTRAL_STORY, T1 PASS, T3 PASS, T4 RESOLVABLE, T2 quasi-static SUPPORTED / dynamic NOT-SUPPORTED |
| 13 Manuscript | PARTIAL | manuscript_IJHMT.docx/.md (4,305 body words, abstract 231), highlights, cover letter, supplementary xlsx, JOURNAL_FIT, 4 audits, reproduction test **11 PASS / 0 FAIL** |

Cross-checks performed during this audit (all against the files as delivered):

| Check | Expected (docs) | Found | Result |
|---|---|---|---|
| Handoff baseline integrity | 303/303 SHA-256 | 303 OK, 0 missing, 0 mismatch; 304 files = 303 + manifest | **PASS** |
| Production runs | 150 | 150 json + 150 npz | **PASS** |
| Test suite | 26 PASS / 1 FAIL | `TEST_RESULTS.json`: n_pass 26, n_fail 1, 28 cases, CPU 1209.7 s | **PASS** |
| Reproduction test | 11 PASS | 11 PASS / 0 FAIL | **PASS** |
| Abstract length | ≤ 250 words | 231 (`MANUSCRIPT_STATS.json`) | **PASS** |
| Highlights | ≤ 85 chars | 78/84/70/76/77 | **PASS** |
| Ellipse modulation | 28.7% extrapolated | `amp_best` = 0.2874949857952955 | **PASS** |
| Figures / tables | 8 / 5 | 8 png / 5 csv | **PASS** |
| Abstract "0.08% at the finest grid" | V9d worst-law 192×96 = 0.08% (V11 = 0.07%) | matches §4 table (line 133) | **consistent** (abstract wording is that of the dynamic coupled case) |

---

## 4. What is still pending

**A. Phase 13 tail / final delivery — nothing of this exists yet:**

1. **`PAPER_PROJECT/packages/PACKAGE_PHASE_07…13.zip`** (MP §67/§68) — directory `packages/`
   is absent; `00_Project_Control/make_packages.py` exists and is ready to build them
   (with a `MANIFEST.json` holding SHA-256 per file). `DECISION_LOG` P13-D001 records that they
   were to be "reconstructed at the end of the session" — that step never ran.
2. **`00_Project_Control/PROJECT_STATE_FINAL.md`** (MP §74) — referenced three times
   (`README.md` start-here list, `PROJECT_STATE_PHASE_13.md`, `AUDIT_FINAL_ADVERSARIAL.md`
   reproducibility row) but **not present**.
3. **`packages/RESEARCH_PROJECT_FINAL.zip`** (MP §74) — the final archive;
   `make_packages.py final` builds it. MP §74: "Only claim it exists if actually created."

**B. Known gaps inherited from Phases 0–2 (not re-opened; §74 would want them):**
`RESEARCH_PROFILE.md`, `SCIENTIFIC_ACCEPTANCE_PLAN.md` (exists only in
`work/handoff/PROJECT_CRYSTAL_GEOMETRY_01/`), `NOVELTY_MATRIX.xlsx`.
These belong to phases the project deliberately did **not** re-open; creating them now would
mean fabricating content → flag to user, do not invent.

**C. User-owned gates still open** (`AUDIT_PRE_MANUSCRIPT.md` §"Open items"):
authors/affiliations/CRediT/funding/conflicts, AI-use declaration, repository DOI + licence,
final journal decision, JCR verification, **confirmation of P7-D002** (the Bromwich-inversion
synthesis change is explicitly "FLAGGED FOR USER CONFIRMATION"), independent expert review.

**D. Consistency items found during the audit to be resolved in Phase 2:**
- `CODE_FREEZE_v2_blockF.json` (latest freeze, 07:39:17): **3 mismatches** —
  `13_Manuscript/build_manuscript.py`, `ms_results.py`, `ms_static.py` were edited *after* the
  last freeze, with no addendum recorded. (The 5 mismatches vs `CODE_FREEZE_v2_gate.json` are
  the documented, expected block-F + P12-D001 additive changes.)
- 15 scripts hard-code `/home/user/PAPER_PROJECT` and `/home/user/work/handoff`
  (17 occurrences), which do not exist in this checkout → nothing runs until the paths resolve.

---

## 5. Environment (this sandbox) vs the recorded environment

| | Recorded (`COMPUTE_STATUS.md`, code freezes) | This sandbox |
|---|---|---|
| Python | 3.13.14 | 3.11.2 |
| numpy / scipy / matplotlib | 2.3.5 / 1.17.1 / 1.16… (2.3.5/1.17.1/3.10.9) | **not installed** (PyPI reachable) |
| python-docx / openpyxl | 1.1.2 / 3.1.5 | **not installed** |
| CPU / RAM | 2 vCPU, 1,984 MB | 2 vCPU, ~3 GB |
| MATLAB / Octave / LaTeX | not used | not installed |

Consequence: any re-run needs `pip install numpy scipy matplotlib python-docx openpyxl` first,
and MP §75 explicitly allows non-bitwise-identical reproduction across environments.
