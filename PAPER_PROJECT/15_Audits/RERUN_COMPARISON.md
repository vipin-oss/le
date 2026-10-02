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
