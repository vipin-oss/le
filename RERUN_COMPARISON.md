# RERUN COMPARISON — recomputed (this session) vs delivered (le.zip)
tolerance 1e-09 · production tolerance 1e-10

### TEST_RESULTS.json
compared 156 scalar/array leaves; 2 exceed tol=1e-09

| key | delivered | recomputed | rel.diff |
|---|---|---|---|
| `cpu_seconds` | 1.209718e+03 | 1.177748e+03 | 2.643e-02 |
| `wall_seconds` | 1.210410e+03 | 1.179598e+03 | 2.546e-02 |

### CONVERGENCE_RESULTS.json
compared 49 scalar/array leaves; 2 exceed tol=1e-09

| key | delivered | recomputed | rel.diff |
|---|---|---|---|
| `cpu_seconds` | 2.828019e+02 | 2.955139e+02 | 4.302e-02 |
| `wall_seconds` | 2.856858e+02 | 2.967990e+02 | 3.744e-02 |

### CONVERGENCE_DIRS.json
compared 45 scalar/array leaves; 9 exceed tol=1e-09

| key | delivered | recomputed | rel.diff |
|---|---|---|---|
| `144x72_gam5.wall_s` | 6.645972e+01 | 6.574988e+01 | 1.068e-02 |
| `192x48_gam3.5.wall_s` | 4.178719e+01 | 4.107341e+01 | 1.708e-02 |
| `192x96_gam3.5.wall_s` | 1.704243e+02 | 1.568882e+02 | 7.943e-02 |
| `96x144_gam3.5.wall_s` | 1.367772e+02 | 1.261042e+02 | 7.803e-02 |
| `96x48_gam3.5.wall_s` | 1.933509e+01 | 1.953430e+01 | 1.020e-02 |
| `96x48_gam5.wall_s` | 1.971728e+01 | 1.812478e+01 | 8.077e-02 |
| `96x48_gam6.5.wall_s` | 1.944007e+01 | 1.817537e+01 | 6.506e-02 |
| `96x96_gam3.5.wall_s` | 6.869338e+01 | 6.562577e+01 | 4.466e-02 |
| `96x96_gam5.wall_s` | 7.036963e+01 | 6.566595e+01 | 6.684e-02 |

### ANALYSIS_V2.json
compared 669 scalar/array leaves; 0 exceed tol=1e-09

All compared values agree within tolerance.

### production runs
150 common tags, 1200 QoI values compared; 0 differ by more than 1e-10

max relative difference over all QoIs: 0.000e+00 (F_tw2.4_ell_phi150/wall_pulse_err)

### stored wall-stress series (npz)
150 common runs; worst max-relative difference of the hoop series:

- A_chi2_phi060_T144: 0.000e+00
- A_chi2_phi060_R48: 0.000e+00
- A_chi2_phi060_R192: 0.000e+00
- A_chi2_phi060_M: 0.000e+00
- A_chi2_phi045_T48: 0.000e+00
- A_chi2_phi045_R48: 0.000e+00
- A_chi2_phi045_M: 0.000e+00
- A_chi2_phi030_T48: 0.000e+00
- A_chi2_phi030_T144: 0.000e+00
- A_chi2_phi030_R48: 0.000e+00

### figures / tables / manuscript
- `11_Figures/fig1_setup.png`: identical
- `11_Figures/fig2_phi_sweep.png`: identical
- `11_Figures/fig3_wall_profiles.png`: identical
- `11_Figures/fig4_verification.png`: identical
- `11_Figures/fig5_memory.png`: identical
- `11_Figures/fig6a_mesh.png`: identical
- `11_Figures/fig6b_ablation.png`: identical
- `11_Figures/fig7_pulse_width.png`: identical
- `12_Tables/D_lambda_eps.csv`: identical
- `12_Tables/ablations_E.csv`: identical
- `12_Tables/convergence_ellipse_6phi.csv`: identical
- `12_Tables/phi_sweep_ellipse.csv`: identical
- `12_Tables/pulse_width_F.csv`: identical
- `13_Manuscript/JOURNAL_FIT.md`: identical
- `13_Manuscript/MANUSCRIPT_STATS.json`: identical
- `13_Manuscript/SUPPLEMENTARY_TABLES.xlsx`: REGENERATED (differs)
- `13_Manuscript/build_manuscript.py`: identical
- `13_Manuscript/build_supplement.py`: identical
- `13_Manuscript/cover_letter.md`: identical
- `13_Manuscript/docbuilder.py`: identical
- `13_Manuscript/highlights.txt`: identical
- `13_Manuscript/manuscript_IJHMT.docx`: REGENERATED (differs)
- `13_Manuscript/manuscript_IJHMT.md`: identical
- `13_Manuscript/ms_results.py`: REGENERATED (differs)
- `13_Manuscript/ms_static.py`: identical

---

## Container-format artifacts

`SUPPLEMENTARY_TABLES.xlsx` and `manuscript_IJHMT.docx` differ at the byte level because
OOXML/ZIP containers embed creation timestamps. Their **content** was checked directly:

| artifact | check | result |
|---|---|---|
| `SUPPLEMENTARY_TABLES.xlsx` | all 8 sheets × all cells compared with openpyxl (`data_only=True`) | **CONTENT IDENTICAL** |
| `manuscript_IJHMT.docx` | all 159 body blocks compared with python-docx | **BODY TEXT IDENTICAL** |

`13_Manuscript/ms_results.py` differs because of the one-line portability edit documented as
R-D002 in `DECISION_LOG.md`; the manuscript regenerated with the edited file is byte-identical
(md5 `590301281df9ca130a6ec9ae5fecb2c8`) to the delivered one, so the edit changes no output.

## Non-scientific differences only

`cpu_seconds` / `wall_seconds` in `TEST_RESULTS.json` and `CONVERGENCE_RESULTS.json`, and the
per-run `wall_s` timings in `CONVERGENCE_DIRS.json`, differ by 1–8%. These are timings on a
different machine, not results (MASTER_PROMPT §75: different hardware/software environments do
NOT need bitwise-identical outputs).

## Verdict

Full re-run on different hardware (Python 3.11.2 vs 3.13.14; identical numpy/scipy/matplotlib
versions) reproduced **every** scientific quantity:

- verification suite 26 PASS / 1 FAIL / 1 exploratory — same statuses, same metrics
- 150/150 production runs — max relative difference of any QoI **0.0**
- 150/150 stored hoop-stress series (npz) — max relative difference **0.0**
- C2/C3/C4 convergence — 9/9 mesh-direction cases identical (rel = 0.00e+00)
- `ANALYSIS_V2.json` — 669 compared leaves, **0** outside 1e-9
- 8 figures, 5 tables — byte-identical
- manuscript (.md and .docx body) and supplementary workbook — identical

Physical validation status is unchanged: **APPLICABLE — EVIDENCE_UNAVAILABLE** (no experimental
data exist); nothing in this re-run changes that.

## Why the raw `.npz` files are not byte-identical (they are data-identical)

150/150 runs: all 1350 stored arrays (`t, hoop, wall, probe, H_hoop, H_wall, H_probe, s, r`)
are **exactly equal** (`np.array_equal`). The container bytes differ in 99 bytes out of ~219 kB
(0.002 %): only the ZIP `create_version`/`extract_version` fields, 45 (Python 3.13) vs
20 (Python 3.11). All member CRCs, sizes and compressed streams are equal.

Similarly, the production `.json` sidecars differ in exactly two fields:
- `wall_s` — per-run wall-clock time (machine speed);
- `pulse_t0_tw` — the delivered 141 gate runs predate the additive `pulse` argument of
  `cg_pipeline.run_config` (P11-D001), so they store `null`, while the re-run stores `[2.5, 1.2]`.
  The value is the pre-registered baseline pulse in both cases; no result changes.

`PRODUCTION_PROVENANCE.csv` changes for the same reason (it dumps `wall_s`).
