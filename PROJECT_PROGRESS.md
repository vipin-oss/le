# PROJECT_PROGRESS — `vipin-oss/le`

Branch: `arena/01a0f67f-le` · 2026-10-01 · source: `le.zip` (52,189,612 B,
sha256 `5e780e1fd6292690c1b56ad378dc35c9737e52cd873e4f18e610cfdf45bb0363`)

- Repository audit: **[`docs/PHASE1_AUDIT.md`](docs/PHASE1_AUDIT.md)**
- Re-run comparison: **[`RERUN_COMPARISON.md`](RERUN_COMPARISON.md)**
- Recovery summary: `PAPER_PROJECT/00_Project_Control/PROJECT_STATE_FINAL.md`

---

## Project

`PAPER_PROJECT` — *"verified continuum study of cavity thermoelasticity in monoclinic β-Ga₂O₃"*
under **MASTER_PROMPT v2.1**. Transient coupled thermoelasticity around a circular vs equal-area
elliptical cavity (χ = 2) in the a–c plane of monoclinic β-Ga₂O₃; Fourier / Lord–Shulman /
two-relaxation-time conduction; frequency-domain mapped-grid FD solver + **Bromwich inversion**;
150-run production; target journal IJHMT (user-owned).

---

## FINAL STATUS

| Phase | Status |
|---|---|
| **PHASE 1** — repository audit | **COMPLETE** |
| **PHASE 2** — consistency check | **COMPLETE** (all checks pass; 4 issues documented, none scientific) |
| **PHASE 3** — continue pending work | **COMPLETE** (re-run + Phase 13 final delivery built) |
| **PHASE 4** — validation | **COMPLETE** — everything reproduced bit-identically; reproduction test 11 PASS |
| **PHASE 5** — persistence | committed each stage (**see push caveat below**) |
| **PHASE 6** — final delivery | **COMPLETE** — `PROJECT_STATE_FINAL.md` + 8 archives |

---

## Phase 1 — what was found

The repository was empty when the session began (`# le`, 1 commit); the user then pushed `le.zip`
to `main`. Audit of the extracted workspace: `PAPER_PROJECT/` (493 files, phases 00–15),
`work/handoff/` (304 files = pristine input baseline), `work/rerun/` (187 files, prior review).
Phases 0 and 7→13 had been executed upstream; Phases 1–6 deliberately not re-opened.
**Pending:** `packages/PACKAGE_PHASE_07…13.zip`, `PROJECT_STATE_FINAL.md`,
`RESEARCH_PROJECT_FINAL.zip` — none existed.

## Phase 2 — consistency check

**Code vs documented formulation: consistent.** Independently re-derived and matched against
`cg_model.py` / `cg_solver.py` / `cg_bromwich.py`: constitutive law σ = Qε − βθ; momentum and
heat equations (incl. g(s) for Fourier/CV/MCV3); BCs (θ = 1 unit transfer, traction-free wall;
θ = 0, u = 0 at R = 80a); the two-sided Laplace transform of the Gaussian pulse; the trapezoidal
Bromwich sum; the solver↔Laplace map w = −i s/t_th; the rotation fix (all three C′ components);
κ̄ = 3.958e-6, δ = 1.0782e-3, c_ref = 7686.6 m/s; pulse, QoI window, grid, plan settings.

**Manuscript claims vs `ANALYSIS_V2.json`: all 11 headline claims verified** (0.854 MPa/K;
spread 4.6e-15; 28.7 % modulation, u_num 1.31 pp; D ≤ 6.4 %, ≤ 1.6 % for a ≥ 10 nm; T2 quasi-static
0.0 % / dynamic 51.6 %; T3 6.2e-4 vs 5.4e-3; ablation ratios 0.94/1.57/0.72/1.03; A₂ =
24.8/27.7/30.0/32.0 %; iso-ellipse/iso-circle 1.53; closed form 985,689.45 Pa/K).

**Issues found — documented, not silently changed**
1. `CODE_FREEZE_v2_blockF.json` stale (3 manuscript scripts edited after it) → fixed by addendum
   `CODE_FREEZE_v2_final.json` (R-D003).
2. 15 scripts hard-code `/home/user/…`; three are frozen files → solved with `bootstrap_paths.sh`
   symlinks instead of patching (R-D004); all frozen hashes still verify.
3. `ms_results.py` used PEP 701 f-string syntax (Python ≥ 3.12 only) → one-line portability edit
   (R-D002), proven output-identical.
4. §74 items from phases 0–2 absent → flagged to user, nothing invented.

## Phase 3/4 — full re-run (user choice; P7-D002 confirmed by the user)

Delivered outputs were snapshotted to `baseline_provided/` before anything was overwritten.
Environment installed to match the record: numpy 2.3.5, scipy 1.17.1, matplotlib 3.10.9,
python-docx 1.1.2, openpyxl 3.1.5 (Python 3.11.2 vs recorded 3.13.14).

| Step | Result |
|---|---|
| `run_tests.py` + `run_tests_supplement.py` | 26 PASS / 1 FAIL / 1 exploratory — **identical** to delivered |
| `run_production_v2.py` heavy + light | **150/150** runs, ~51 min wall |
| all stored arrays (150 runs × 9 arrays = 1350) | **exactly equal**; max rel. diff 0.0 |
| QoIs (1200 values) | max rel. diff **0.0** |
| C2/C3/C4 convergence | 9/9 mesh-direction cases identical (rel = 0.00e+00) |
| `ANALYSIS_V2.json` | 669 compared leaves, **0** outside 1e-9 |
| figures (8) / tables (5) | **byte-identical** |
| manuscript `.md` | **byte-identical** (md5 `590301281df9ca130a6ec9ae5fecb2c8`) |
| `.docx` body (159 blocks) / `.xlsx` (8 sheets, all cells) | **content identical** |
| `reproduce.py` | **11 PASS / 0 FAIL** |

Only non-scientific differences: CPU/wall timings; `.npz` ZIP version metadata (all CRCs equal);
`pulse_t0_tw` field (absent in the delivered pre-block-F runs). Full detail: `RERUN_COMPARISON.md`.

**Validation status (unchanged):** verification VERIFIED for the listed quantities and grids;
physical validation **APPLICABLE — EVIDENCE_UNAVAILABLE** — no experimental data exist.

## Phase 6 — deliverables built

- `PAPER_PROJECT/00_Project_Control/PROJECT_STATE_FINAL.md`
- `PAPER_PROJECT/packages/PACKAGE_PHASE_07…13.zip` (69 → 502 files; `MANIFEST.json` with SHA-256
  per file, verified: 0 mismatches)
- `PAPER_PROJECT/packages/RESEARCH_PROJECT_FINAL.zip` (506 files = whole `PAPER_PROJECT`
  excluding `packages/`; 31.7 MB)
- `06_Source_Code/CODE_FREEZE_v2_final.json` (24 files)
- Updated: `README.md`, `DECISION_LOG.md`, `CHANGELOG.md`

---

## Files created / modified

| File | Action |
|---|---|
| `docs/PHASE1_AUDIT.md` | created — Phase-1 audit |
| `PROJECT_PROGRESS.md` | created/updated — this record |
| `RERUN_COMPARISON.md` | created — delivered vs recomputed |
| `bootstrap_paths.sh` | created — path bootstrap (frozen files untouched) |
| `tools/compare_rerun.py` | created — comparison harness |
| `.gitignore` | created — `work/handoff.zip`, `PAPER_PROJECT/packages/`, `baseline_provided/`, `__pycache__/` |
| `PAPER_PROJECT/00_Project_Control/PROJECT_STATE_FINAL.md` | **created (was missing)** |
| `PAPER_PROJECT/packages/*.zip` (8) | **created (was missing)**; git-ignored |
| `PAPER_PROJECT/06_Source_Code/CODE_FREEZE_v2_final.json` | created |
| `PAPER_PROJECT/13_Manuscript/ms_results.py` | 1-line portability edit (R-D002) |
| `PAPER_PROJECT/README.md`, `DECISION_LOG.md`, `CHANGELOG.md` | updated |
| regenerated data/docs | TEST_RESULTS.json, TEST_REPORT.md, 09_Raw_Data (production 300, convergence 40), ANALYSIS_V2.json, ANALYSIS_V2_TABLES.md, PRODUCTION_PROVENANCE.csv, CONVERGENCE_*.json, VALIDATION_RESULTS.md, CONVERGENCE_REPORT.md, STABILITY_REPORT.md, 11_Figures, 12_Tables, 13_Manuscript, CENTRAL_STORY.md, CORRECTIONS_LOG.md, phase states 07–13 |

## Remaining limitations

- No physical validation (evidence does not exist); τ hypothetical; continuum validity at 5–50 nm
  not established; c_p estimated; α uncertain by > 10×; α₅ = 0; plane strain.
- `09_Raw_Data/convergence_gamma3p5/` not re-run (partial study, no regenerator script in package).
- §74 items from phases 0–2 still absent (user decision).
- User-owned: authors/affiliations/CRediT/funding/conflicts, AI-use declaration, repository
  DOI + licence, final journal, JCR verification, independent expert review.

## Push status — **PUSHED**

`origin/arena/01a0f67f-le` = `5648946` = local `HEAD`, working tree clean.
(The token expired mid-session; after the user reconnected GitHub the branch was pushed as
`b482751..5648946`.)

## Restoring this workspace after a snapshot reset — learned the hard way

A workspace restore rolls `.git` back to the clone state and drops git-ignored directories and
system-installed Python packages. The file contents survive. Recovery procedure:

```sh
cd /home/user/le
# 1. Python packages (installed outside /home/user, so they are not snapshotted):
pip3 install --break-system-packages numpy==2.3.5 scipy==1.17.1 matplotlib==3.10.9 \
                                     python-docx==1.1.2 openpyxl==3.1.5
# 2. Paths the frozen scripts expect (symlinks are not snapshotted either):
sh bootstrap_paths.sh
# 3. Re-linearise onto the remote branch and commit the restored working tree:
git fetch origin && git add -A && git reset --soft origin/arena/01a0f67f-le
git commit -m "<message>" && git push origin arena/01a0f67f-le
# 4. Regenerate the two git-ignored directories (dropped by the restore):
cd PAPER_PROJECT && python3 00_Project_Control/make_packages.py final      # packages/ (≈3 s)
#    baseline_provided/ (snapshot of the delivered outputs, needed only by tools/compare_rerun.py):
cd /home/user/le && mkdir -p /tmp/lz && git cat-file -p origin/main:le.zip > /tmp/lz/le.zip \
  && unzip -q -o /tmp/lz/le.zip -d /tmp/lz/x && mkdir -p baseline_provided \
  && cp -a /tmp/lz/x/PAPER_PROJECT/{09_Raw_Data,10_Processed_Data,11_Figures,12_Tables,13_Manuscript} baseline_provided/ \
  && cp -a /tmp/lz/x/PAPER_PROJECT/07_Tests/TEST_RESULTS.json baseline_provided/
```

`packages/` and `baseline_provided/` are **git-ignored on purpose** (63 MB of regenerable
archives; 32 MB already published in `le.zip` on `main`) — both are rebuilt by the commands above.

## Next action

None outstanding from the task list. Remaining items are user-owned (authors, declarations,
repository DOI/licence, final journal, JCR check, independent expert review).
