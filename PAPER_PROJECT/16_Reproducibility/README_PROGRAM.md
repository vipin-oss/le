# README_PROGRAM

This folder is the runnable program: the solver, the experiment drivers, the verification suite,
the manuscript builders, the QA utilities, the code-freeze manifests and the as-received baseline.
It is a copy of `PAPER_PROJECT/` inside the reproducibility archive; the paths in the tables below
are archive-relative, so every command shown can be run from the extracted archive root.

## Language and version

- Language: Python 3 only (no compilation step, no C/Fortran extensions).
- Interpreter used to verify this archive: `Python 3.11.2` (/usr/bin/python3).
- The project status note `07_DOCUMENTATION/program_control/COMPUTE_STATUS.md` and
  `REPRODUCIBILITY_STATUS.md` record the run environment as "Python 3.13.14, numpy 2.3.5,
  scipy 1.17.1"; `10_Processed_Data/PRODUCTION_PROVENANCE.csv` records the environment of every
  production run as `Python 3.11.2`. 3.13.14 is not a released CPython version, so the
  provenance CSV is taken as authoritative for how the stored results were produced; no claim in
  the paper depends on the distinction, and nothing here was changed to hide it.
- Third-party packages: the pinned set the project shipped with, verbatim from
  `01_PROGRAM/environment/requirements_pinned_from_handoff.txt` (also at
  `work/handoff/PILOT_HUANG_2025_01/requirements.txt`):

```
numpy==2.3.5
scipy==1.17.1
mpmath==1.3.0
matplotlib==3.10.9
PyMuPDF==1.28.2
openpyxl==3.1.5
```

- The manuscript builders additionally import `python-docx`, `Pillow` (via `docbuilder.py`) and
  `reportlab`/`matplotlib` (via `tools/md_to_pdf.py`, `08_Experiments/make_figures.py`). Versions of
  these are NOT DOCUMENTED in the repository: the requirements file above is the handoff's, and the
  submission-programme environment installed them unpinned. `04_REPRODUCTION/ENVIRONMENT_OBSERVED.txt`
  (when present) records what a working environment actually had.

## What each subfolder is

| folder | contents |
|---|---|
| `src/` | the frozen solver: `cg_model` (material), `cg_grid` (mapped grid), `cg_ops` (operators), `cg_solver` (frequency-domain solve), `cg_bromwich` (inversion), `cg_pipeline` (case assembly), `cg_ref1d` (1-D reference solution), `cg_transient` |
| `experiments/` | drivers: `run_convergence.py`, `run_convergence_dirs.py`, `run_production_v2.py heavy|light`, `production_matrix.py` (the case matrix), `analyze_v2.py`, `make_figures.py`, `make_provenance.py`, `reproduce.py`, and the run `logs/` |
| `tests/` | `run_tests.py` (verification suite), `run_tests_supplement.py`, `make_test_report.py`, `diagnostics/`, `logs/`, stored `TEST_RESULTS.json` |
| `builders/` | `build_manuscript.py`, `build_calculations.py`, `build_supplement.py`, `docbuilder.py`, `ms_*.py` - regenerate the manuscript and its companion from the data package |
| `utilities/` | `tools/` (`.md` to `.tex`/`.pdf` converters, LaTeX and connection auditors, reference renumbering) and `bootstrap_paths.sh` |
| `control/` | packaging and phase-state scripts (`make_packages.py`, `make_reproducibility_archive.py`, ...) |
| `freeze/` | `CODE_FREEZE_*.json` manifests (current label `submission_2026_10_03j`) and `make_code_freeze.py`, `DIFF_VS_HANDOFF.txt` |
| `handoff_baseline/` | the as-received 2026-10-01 pilot, committed verbatim; integrity via `MANIFEST_SHA256.json` |

## Installation

```bash
python3 -m venv .venv && . .venv/bin/activate
pip install -r 01_PROGRAM/environment/requirements_pinned_from_handoff.txt
pip install python-docx pillow                 # manuscript builders only
sh bootstrap_paths.sh                          # see "Path convention" below
```

## Path convention (read this before running anything)

Fifteen project scripts refer to the tree as `/home/user/PAPER_PROJECT` because that is where the
project lived when the frozen code was written; changing those lines would alter the SHA-256 of
frozen files and invalidate the code freeze. `bootstrap_paths.sh` therefore creates the symlinks
`/home/user/PAPER_PROJECT -> <repo>/PAPER_PROJECT` and `/home/user/work -> <repo>/work`. On a
machine where you cannot create those links, the alternative is to copy the archive so that the
`PAPER_PROJECT` directory sits at that path, or to set the path in the handful of scripts - in which
case re-run `python3 01_PROGRAM/freeze/make_code_freeze.py <label>` and note that the freeze id
changes. `tools/fix_hardcoded_root.py` exists in the repository for exactly this job; the frozen
files themselves were deliberately left untouched in the archive.

## Entry point and exact execution order

The full order, with expected outputs and runtimes, is `RUN_ORDER.md` in this folder. Shortest
useful path from the shipped data to the shipped results:

```bash
python3 01_PROGRAM/experiments/analyze_v2.py            # data -> ANALYSIS_V2.json + tables
python3 01_PROGRAM/experiments/make_figures.py           # data -> the eight figures
python3 01_PROGRAM/experiments/make_provenance.py        # data -> PRODUCTION_PROVENANCE.csv
python3 01_PROGRAM/tests/run_tests.py                     # verification suite (~20 min)
python3 01_PROGRAM/experiments/reproduce.py                # reproduction test vs stored outputs
python3 01_PROGRAM/builders/build_manuscript.py -c         # rebuild manuscript, self-check only
```
Full recomputation (hours of compute, 150+ runs) starts at `RUN_ORDER.md` step 3 and is optional:
every result in the manuscript is reproducible from the stored raw data with the four commands
above, which is the point of shipping `03_DATA/`.

## Solver settings as written in the source

Extracted by AST from `01_PROGRAM/src/*.py` and `01_PROGRAM/experiments/production_matrix.py`;
values are the literal defaults in the code, not a paraphrase. Machine-readable copy:
`parameter_manifest.json`.

| module | name | line | value as written |
|---|---|---|---|
| cg_model.py | Cij_GPa | `8` | dict(C11=242.8, C22=343.8, C33=347.4, C44=47.8, C55=88.6, C66=104.0,
               C12=128.0, C13=160.0, C23=70.9, C15= |
| cg_model.py | K_ac | `10` | np.array([[12.13, -0.992], [-0.992, 14.09]]) |
| cg_model.py | alpha_crys | `11` | np.array([1.54e-6, 3.37e-6, 3.15e-6]) |
| cg_model.py | rho | `12` | 5880.0 |
| cg_model.py | cp_ESTIMATED | `13` | 560.0 |
| cg_model.py | T0 | `14` | 293.0 |
| cg_model.py | GPa | `16` | 1000000000.0 |
| cg_pipeline.py | A0 | `14` | 1e-08 |
| cg_pipeline.py | DV | `15` | derived() |
| cg_pipeline.py | KAPPA | `16` | DV['kappa'] |
| cg_pipeline.py | C_REF | `17` | DV['c_ref'] |
| cg_pipeline.py | T_QOI | `20` | 6.0 |
| cg_pipeline.py | PHIS | `22` | list(range(0, 180, 15)) |
| cg_pipeline.py | PLAN_DEFAULT | `23` | dict(T=20.0, gamma=0.9) |
| cg_pipeline.py | GAMMA_DEFAULT | `24` | 5.0 |
| cg_pipeline.py | T_STORE | `25` | np.arange(0.0, 12.0 + 1e-9, 0.05) |
| cg_pipeline.py | T_FINE | `26` | np.arange(0.0, T_QOI + 1e-9, 0.01) |
| cg_pipeline.py | ALPHA_SETS | `65` | {
    'baseline_orlandi2015': (1.54e-6, 3.37e-6, 3.15e-6),         # PARAMETER_TABLE (secondary-quoted values of Orlandi |
| 08_Experiments/production_matrix.py | HERE | `11` | os.path.dirname(os.path.abspath(__file__)) |
| 08_Experiments/production_matrix.py | GRIDS | `16` | {'R48': (48, 96), 'T48': (96, 48), 'M': (96, 96), 'R192': (192, 96), 'T144': (96, 144)} |
| 08_Experiments/production_matrix.py | COST | `17` | {'R48': 'light', 'T48': 'light', 'M': 'medium', 'R192': 'heavy', 'T144': 'heavy'} |
| 08_Experiments/production_matrix.py | PHIS6 | `19` | (0, 30, 60, 90, 120, 150) |
| 08_Experiments/production_matrix.py | LAMBDAS_B2 | `20` | (0.05, 0.2, 0.8, 3.2) |
| 08_Experiments/production_matrix.py | E_VARIANTS | `21` | [('E1_alpha_cheng298', dict(alpha='cheng2018_298K_like')), ('E2_alpha_iso', dict(alpha='isotropic_mean')),
              |
| 08_Experiments/production_matrix.py | B_DEF | `24` | [('B_CV_tau1_a10', 'CV', 1.0, 10), ('B_CV_tau5_a10', 'CV', 5.0, 10), ('B_CV_tau20_a10', 'CV', 20.0, 10), ('B_CV_tau20_a5 |
| 08_Experiments/production_matrix.py | F_TW | `28` | (0.3, 0.6, 2.4) |
| 08_Experiments/production_matrix.py | BM_DEF | `29` | [('BM_CV_tau5_a10', 'CV', 5.0, 10), ('BM_CV_tau20_a20', 'CV', 20.0, 20), ('BM_F_tau0_a20', 'FOURIER', 0.0, 20)] |

Production grid/case definitions actually used (`production_matrix.py`): `GRIDS = {'R48': (48, 96), 'T48': (96, 48), 'M': (96, 96), 'R192': (192, 96), 'T144': (96, 144)}`; `COST = {'R48': 'light', 'T48': 'light', 'M': 'medium', 'R192': 'heavy', 'T144': 'heavy'}`.

## Seeds, threads, tolerances

- **Random seeds: none.** No part of the program draws random numbers (`random`, `np.random`,
  `seed` appear nowhere in `src/`, `experiments/` or the builders); the pipeline is deterministic,
  so no seed needs to be recorded.
- **Threading:** every run script sets `OPENBLAS_NUM_THREADS=1` before importing numpy, so BLAS
  threading is not a source of run-to-run variation. Production used exactly two worker processes
  claiming jobs atomically by `mkdir` (`run_production_v2.py`), which makes the run set independent
  of worker interleaving.
- **Solver tolerance:** the Bromwich/solver defaults in the table above (e.g. `eps=1e-10` in the
  contour integrator) are the settings recorded in the code; the per-run residuals stored in
  `03_DATA/processed/PRODUCTION_PROVENANCE.csv` (`backward_err`, `wall_pulse_err`) are the evidence
  that they were met.
- **Comparison tolerances for reproduction:** `reproduce.py` uses 1e-9 for recomputed stress values
  and 1e-12 for tables rebuilt from stored data, and states that a different machine/BLAS would
  need about 1e-6. That sentence is the project's own, quoted from the script docstring.

## Runtime and hardware as recorded

- `07_DOCUMENTATION/program_control/COMPUTE_STATUS.md`: 2 vCPU (Xeon 2.60 GHz), 1,984 MB RAM, no
  GPU; per-run cost 3 s (48x24) to 157 s (192x96); `192x96` solves need 0.7-1.0 GB, one heavy job
  at a time (one run was killed by the OOM killer); cumulative compute about 2.7 CPU-h.
- `03_DATA/processed/PRODUCTION_PROVENANCE.csv` carries `wall_s` and `n_solves` for each of the
  175 production runs, so the cost of any single case can be looked up rather than
  estimated.

## Verification gates run while building this archive

| gate | exit code | tail of output |
|---|---|---|

Transcript with the full tails: `09_ARCHIVE_METADATA/VERIFICATION_GATES.txt`.

Code freeze of the archived code: `submission_2026_10_03j` (27 entries listed in `01_PROGRAM/freeze/`).
