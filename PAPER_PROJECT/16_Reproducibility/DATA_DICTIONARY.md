# DATA_DICTIONARY

Generated from the files themselves at build time - the key lists, types and array shapes below
are read out of the shipped data, so they cannot disagree with it.

## `03_DATA/raw/convergence/`

20 `.json` result records + 20 `.npz` field files, 2.9 MB total. File name pattern: `<BLOCK>_chi<CHI>_phi<PHI>[_<GRID>].(json|npz)` for production, `C<N>_(...)` for the convergence families; the tag inside each file matches its name.

### Result record (`.json`) - keys, types, example values

| key | type(s) | present in | example value (as stored) |
|---|---|---|---|
| `Lambda` | float | 20/20 | `0.0` |
| `Nr` | int | 20/20 | `96` |
| `Nt` | int | 20/20 | `48` |
| `Rfac` | float | 20/20 | `80.0` |
| `a_nm` | float | 20/20 | `10.0` |
| `ang_modes` | list | 20/20 | `list[9] first=731076.7311687997` |
| `back_max` | float | 20/20 | `6.85049861922754e-25` |
| `chi` | float | 20/20 | `2.0` |
| `coupled` | bool | 20/20 | `True` |
| `energy_coupling` | bool | 20/20 | `True` |
| `epsilon` | float | 20/20 | `0.05150393493736088` |
| `gamma_grid` | float | 20/20 | `5.0` |
| `inertia_scale` | float | 20/20 | `1.0` |
| `iso` | bool | 20/20 | `False` |
| `model` | str | 20/20 | `FOURIER` |
| `n_solves` | int | 20/20 | `22` |
| `phi` | float, int | 20/20 | `90` |
| `plan` | dict | 20/20 | container - see source |
| `probe_r_over_a` | list | 20/20 | `list[3] first=1.505396347596303` |
| `profile_at_peak` | list | 20/20 | `list[48] first=-824949.8778893489` |
| `pulse_t0_tw` | list | 20/20 | `list[2] first=2.5` |
| `sig_abs_max` | float | 20/20 | `959287.0612903115` |
| `sig_interp` | float | 20/20 | `-961654.3306622012` |
| `sig_nodal` | float | 20/20 | `-959287.0612903115` |
| `t_star` | float | 20/20 | `2.5100000000000002` |
| `t_star_interp` | float | 20/20 | `2.5100000000000002` |
| `t_th_s` | float | 20/20 | `2.5259999944530252e-11` |
| `tag` | str | 20/20 | `C2_ell_phi090_T16_g1.1` |
| `tau_ps` | float | 20/20 | `0.0` |
| `th_star_interp_deg` | float | 20/20 | `159.375` |
| `th_star_nodal_deg` | float | 20/20 | `157.5` |
| `variant` | NoneType | 20/20 | container - see source |
| `wall_pulse_err` | float | 20/20 | `7.948244164719383e-06` |
| `wall_s` | float | 20/20 | `16.293014764785767` |

### Field arrays (`.npz`) - from `PAPER_PROJECT/09_Raw_Data/convergence/C2_ell_phi090_T16_g1.1.npz` (all 20 files in the folder share this layout)

| array | shape | dtype | compressed B | uncompressed B |
|---|---|---|---|---|
| t | (241,) | <f8 | 612 | 2056 |
| hoop | (48, 241) | <f8 | 89184 | 92672 |
| wall | (48, 241) | <f8 | 2482 | 92672 |
| probe | (3, 241) | <f8 | 5565 | 5912 |
| H_hoop | (22, 48) | <c16 | 11246 | 17024 |
| H_wall | (22, 48) | <c16 | 144 | 17024 |
| H_probe | (22, 3) | <c16 | 1124 | 1184 |
| s | (22,) | <c16 | 217 | 480 |
| r | (96,) | <f8 | 856 | 896 |

## `03_DATA/raw/convergence_gamma3p5/`

17 `.json` result records + 17 `.npz` field files, 2.1 MB total. File name pattern: `<BLOCK>_chi<CHI>_phi<PHI>[_<GRID>].(json|npz)` for production, `C<N>_(...)` for the convergence families; the tag inside each file matches its name.

### Result record (`.json`) - keys, types, example values

| key | type(s) | present in | example value (as stored) |
|---|---|---|---|
| `Lambda` | float | 17/17 | `0.19794140977750438` |
| `Nr` | int | 17/17 | `48` |
| `Nt` | int | 17/17 | `24` |
| `Rfac` | float | 17/17 | `80.0` |
| `a_nm` | float | 17/17 | `10.0` |
| `ang_modes` | list | 17/17 | `list[9] first=765903.6854769336` |
| `back_max` | float | 17/17 | `6.596097872674245e-26` |
| `chi` | float | 17/17 | `1.0` |
| `coupled` | bool | 17/17 | `True` |
| `energy_coupling` | bool | 17/17 | `True` |
| `epsilon` | float | 17/17 | `0.05150393493736088` |
| `inertia_scale` | float | 17/17 | `1.0` |
| `iso` | bool | 17/17 | `False` |
| `model` | str | 17/17 | `CV` |
| `n_solves` | int | 17/17 | `27` |
| `phi` | int | 17/17 | `0` |
| `plan` | dict | 17/17 | container - see source |
| `probe_r_over_a` | list | 17/17 | `list[3] first=1.3950532471203136` |
| `profile_at_peak` | list | 17/17 | `list[24] first=-749520.0219099703` |
| `sig_abs_max` | float | 17/17 | `923361.3779291752` |
| `sig_interp` | float | 17/17 | `-944616.450801658` |
| `sig_nodal` | float | 17/17 | `-923361.3779291752` |
| `t_star` | float | 17/17 | `2.45` |
| `t_star_interp` | float | 17/17 | `2.45` |
| `t_th_s` | float | 17/17 | `2.5259999944530252e-11` |
| `tag` | str | 17/17 | `C1_circ_phi000_CV5_g48` |
| `tau_ps` | float | 17/17 | `5.0` |
| `th_star_interp_deg` | float | 17/17 | `218.4375` |
| `th_star_nodal_deg` | float | 17/17 | `225.0` |
| `wall_pulse_err` | float | 17/17 | `6.337471067996692e-09` |
| `wall_s` | float | 17/17 | `2.8165993690490723` |

### Field arrays (`.npz`) - from `PAPER_PROJECT/09_Raw_Data/convergence_gamma3p5/C1_circ_phi000_CV5_g48.npz` (all 17 files in the folder share this layout)

| array | shape | dtype | compressed B | uncompressed B |
|---|---|---|---|---|
| t | (241,) | <f8 | 612 | 2056 |
| hoop | (24, 241) | <f8 | 35227 | 46400 |
| wall | (24, 241) | <f8 | 2200 | 46400 |
| probe | (3, 241) | <f8 | 5568 | 5912 |
| H_hoop | (27, 24) | <c16 | 6662 | 10496 |
| H_wall | (27, 24) | <c16 | 133 | 10496 |
| H_probe | (27, 3) | <c16 | 1350 | 1424 |
| s | (27,) | <c16 | 245 | 560 |
| r | (48,) | <f8 | 471 | 512 |

## `03_DATA/raw/production/`

175 `.json` result records + 175 `.npz` field files, 30.1 MB total. File name pattern: `<BLOCK>_chi<CHI>_phi<PHI>[_<GRID>].(json|npz)` for production, `C<N>_(...)` for the convergence families; the tag inside each file matches its name.

### Result record (`.json`) - keys, types, example values

| key | type(s) | present in | example value (as stored) |
|---|---|---|---|
| `Lambda` | float | 175/175 | `0.0` |
| `Nr` | int | 175/175 | `96` |
| `Nt` | int | 175/175 | `96` |
| `Rfac` | float | 175/175 | `80.0` |
| `a_nm` | float | 175/175 | `10.0` |
| `ang_modes` | list | 175/175 | `list[9] first=722778.7006601975` |
| `back_max` | float | 175/175 | `7.279680242636356e-25` |
| `block` | str | 175/175 | `A` |
| `chi` | float | 175/175 | `1.0` |
| `coupled` | bool | 175/175 | `True` |
| `energy_coupling` | bool | 175/175 | `True` |
| `epsilon` | float | 175/175 | `0.05150393493736088` |
| `gamma_grid` | float | 175/175 | `5.0` |
| `grid` | str | 175/175 | `M` |
| `inertia_scale` | float | 175/175 | `1.0` |
| `iso` | bool | 175/175 | `False` |
| `model` | str | 175/175 | `FOURIER` |
| `n_solves` | int | 175/175 | `27` |
| `phi` | float | 175/175 | `0.0` |
| `plan` | dict | 175/175 | container - see source |
| `probe_r_over_a` | list | 175/175 | `list[3] first=1.526372947900705` |
| `profile_at_peak` | list | 175/175 | `list[96] first=-740907.5934568855` |
| `pulse_t0_tw` | list | 175/175 | `list[2] first=2.5` |
| `sig_abs_max` | float | 175/175 | `853483.9779698204` |
| `sig_interp` | float | 175/175 | `-853638.7276150119` |
| `sig_nodal` | float | 175/175 | `-853483.9779698204` |
| `t_star` | float | 175/175 | `2.48` |
| `t_star_interp` | float | 175/175 | `2.48` |
| `t_th_s` | float | 175/175 | `2.5259999944530252e-11` |
| `tag` | str | 175/175 | `A_chi1_phi000_M` |
| `tau_ps` | float | 175/175 | `0.0` |
| `th_star_interp_deg` | float | 175/175 | `36.796875` |
| `th_star_nodal_deg` | float | 175/175 | `217.5` |
| `variant` | NoneType, dict | 175/175 | container - see source |
| `wall_pulse_err` | float | 175/175 | `6.337471067996692e-09` |
| `wall_s` | float | 175/175 | `65.3912034034729` |

### Field arrays (`.npz`) - from `PAPER_PROJECT/09_Raw_Data/production/A_chi1_phi000_M.npz` (all 175 files in the folder share this layout)

| array | shape | dtype | compressed B | uncompressed B |
|---|---|---|---|---|
| t | (241,) | <f8 | 612 | 2056 |
| hoop | (96, 241) | <f8 | 178198 | 185216 |
| wall | (96, 241) | <f8 | 3037 | 185216 |
| probe | (3, 241) | <f8 | 5568 | 5912 |
| H_hoop | (27, 96) | <c16 | 27766 | 41600 |
| H_wall | (27, 96) | <c16 | 191 | 41600 |
| H_probe | (27, 3) | <c16 | 1352 | 1424 |
| s | (27,) | <c16 | 245 | 560 |
| r | (96,) | <f8 | 858 | 896 |

## `03_DATA/processed/`

| file | what it is | produced by |
|---|---|---|
| `ANALYSIS_V2.json` | the aggregated analysis the manuscript quotes (peak/extreme tables, the T1-T5 frozen-criterion verdicts, ablations) | `01_PROGRAM/experiments/analyze_v2.py` |
| `ANALYSIS_V2_TABLES.md` | the same, rendered as the markdown tables the builders embed | same script |
| `CONVERGENCE_RESULTS.json`, `CONVERGENCE_RESULTS_gamma3p5_partial.json`, `CONVERGENCE_DIRS.json` | the convergence studies as processed tables | `analyze_v2.py` / the convergence drivers |
| `PRODUCTION_PROVENANCE.csv` | the per-run audit trail, 13 columns | `01_PROGRAM/experiments/make_provenance.py` |

### `PRODUCTION_PROVENANCE.csv` columns

| column | meaning |
|---|---|
| `RUN_ID` | the case tag; matches `<TAG>.json`/`.npz` under `03_DATA/raw/production/` |
| `block` | which block of the matrix (A, B, D, E, F, BM, ...) - see `production_matrix.py` |
| `status` | `RUN_SUCCESS` or the recorded failure |
| `CODE_VERSION(freeze sha256[:16])` | first 16 hex of the code-freeze manifest that described the code as it ran |
| `INPUT_CHECKSUM` | sha256[:16] of the inputs that defined the case |
| `REFERENCE_DATA_VERSION(cg_model sha256[:16])` | the material-constants module the run used |
| `ENVIRONMENT_VERSION` | interpreter, library and kernel string captured at run time |
| `OUTPUT_LOCATION` | path of the `.npz` (archive-relative reading = project-relative writing) |
| `OUTPUT_SHA256[:16]` | first 16 hex of the output file |
| `wall_s`, `n_solves` | cost of that run (see COMPUTE_STATUS.md for the hardware) |
| `backward_err`, `wall_pulse_err` | the two internal consistency residuals per run (Bromwich round-trip; wall-temperature recovery) |

Example row, verbatim:

```
RUN_ID,block,status,CODE_VERSION(freeze sha256[:16]),INPUT_CHECKSUM,REFERENCE_DATA_VERSION(cg_model sha256[:16]),ENVIRONMENT_VERSION,OUTPUT_LOCATION,OUTPUT_SHA256[:16],wall_s,n_solves,backward_err,wall_pulse_err
A_chi1_phi000_M,A,RUN_SUCCESS,feab48880c3c1359,ea861aea886db5f8,f15578152b6374c1,Python 3.11.2; numpy/scipy as in CODE_FREEZE; Linux-6.1.158+-x86_64-with-glibc2.36,09_Raw_Data/production/A_chi1_phi000_M.npz,8a7cb347374d3b39,65,27,7.279680242636356e-25,6.337471067996692e-09
A_chi1_phi000_R192,A,RUN_SUCCESS,feab48880c3c1359,174c9ab3ff15a1fd,f15578152b6374c1,Python 3.11.2; numpy/scipy as in CODE_FREEZE; Linux-6.1.158+-x86_64-with-glibc2.36,09_Raw_Data/production/A_chi1_phi000_R192.npz,5d4a861c93939161,154,27,1.4537939209478578e-24,6.337471067996692e-09
```

## `03_DATA/tables/`

| csv | rows | used by |
|---|---|---|
| D_lambda_eps.csv | 32 | figure/table source (see `FIGURE_PROVENANCE.md`) |
| ablations_E.csv | 5 | figure/table source (see `FIGURE_PROVENANCE.md`) |
| ablations_E_M.csv | 5 | figure/table source (see `FIGURE_PROVENANCE.md`) |
| convergence_ellipse_6phi.csv | 6 | figure/table source (see `FIGURE_PROVENANCE.md`) |
| phi_sweep_ellipse.csv | 12 | figure/table source (see `FIGURE_PROVENANCE.md`) |
| pulse_width_F.csv | 4 | figure/table source (see `FIGURE_PROVENANCE.md`) |

## What is NOT in the data folders

- `09_Raw_Data/production/_claims/` - the job-claiming directories the two workers used; transient
  by design, and the packager skips them (`packages/`, `__pycache__` likewise).
- Any experimental measurement: the study is a continuum computation and the paper says no physical
  validation data exists (`06_VALIDATION/PHYSICAL_VALIDATION.md`).
- Third-party PDFs of the cited literature: not redistributable, so the archive ships the Crossref
  verification records in `06_VALIDATION/literature_verification/` instead.
