# FIGURE_PROVENANCE

One row per manuscript figure: what the source contains, where it goes, what it reads, the
command, and the shipped files with their sha256. Generated from the scripts and the file tree.

Global plotting settings as written in `08_Experiments/make_figures.py`: `'font.size': 9, 'axes.grid': True, 'grid.alpha': 0.25, 'figure.dpi': 140, 'savefig.dpi': 200,                      'axes.spines.top': False, 'axes.spines.right': False, 'legend.frameon': False`

| manuscript figure | generator | reads | shipped as | sha256 (first 16) |
|---|---|---|---|---|
| `fig1` | `make_figures.py` | `03_DATA/raw/...` + `03_DATA/processed/ANALYSIS_V2.json` | `02_OVERLEAF/figures/fig1_setup.pdf` (vector) and `08_FINAL_OUTPUTS/figures/fig1_setup.png` (raster) | c485b987744740a6 |
| `fig2` | `make_figures.py` | `03_DATA/raw/...` + `03_DATA/processed/ANALYSIS_V2.json` | `02_OVERLEAF/figures/fig2_phi_sweep.pdf` (vector) and `08_FINAL_OUTPUTS/figures/fig2_phi_sweep.png` (raster) | 6d642cad0a71fd0f |
| `fig3` | `make_figures.py` | `03_DATA/raw/...` + `03_DATA/processed/ANALYSIS_V2.json` | `02_OVERLEAF/figures/fig3_wall_profiles.pdf` (vector) and `08_FINAL_OUTPUTS/figures/fig3_wall_profiles.png` (raster) | 4d3067555dc45497 |
| `fig4` | `make_figures.py` | `03_DATA/raw/...` + `03_DATA/processed/ANALYSIS_V2.json`, `07_Tests/TEST_RESULTS.json` | `02_OVERLEAF/figures/fig4_verification.pdf` (vector) and `08_FINAL_OUTPUTS/figures/fig4_verification.png` (raster) | 383fc8f168e058f3 |
| `fig5` | `make_figures.py` | `03_DATA/raw/...` + `03_DATA/processed/ANALYSIS_V2.json` | `02_OVERLEAF/figures/fig5_memory.pdf` (vector) and `08_FINAL_OUTPUTS/figures/fig5_memory.png` (raster) | c1905d40c9abb33c |
| `fig6` | `make_figures.py` | `03_DATA/raw/...` + `03_DATA/processed/ANALYSIS_V2.json` | `02_OVERLEAF/figures/fig6a_mesh.pdf` (vector) and `08_FINAL_OUTPUTS/figures/fig6a_mesh.png` (raster) | c6d3b67eaf91666a |
| `fig7` | `make_figures.py` | `03_DATA/raw/...` + `03_DATA/processed/ANALYSIS_V2.json` | `02_OVERLEAF/figures/fig6b_ablation.pdf` (vector) and `08_FINAL_OUTPUTS/figures/fig6b_ablation.png` (raster) | 3e88449b5463374f |
| `fig8` | `make_figures.py` | `03_DATA/raw/...` + `03_DATA/processed/ANALYSIS_V2.json` | `02_OVERLEAF/figures/fig7_pulse_width.pdf` (vector) and `08_FINAL_OUTPUTS/figures/fig7_pulse_width.png` (raster) | fd98891335469bdc |

Figure-function inventory in the generator script (name -> output file, from the source):

| function | writes |
|---|---|
| `fig1()` | `fig1_setup.png` |
| `fig2()` | `fig2_phi_sweep.png` |
| `fig3()` | `fig3_wall_profiles.png` |
| `fig4()` | `fig4_verification.png` |
| `fig5()` | `fig5_memory.png` |
| `fig6()` | `fig7_pulse_width.png` |

## How each rendition in the archive was produced

```bash
python3 PAPER_PROJECT/08_Experiments/make_figures.py                 # 11_Figures/fig*.png (200 dpi)
python3 Phase_09_Closeout/verification/export_submission_figures.py   # 600-dpi PNG + LZW TIFF, vector PDF, in 11_Figures/submission/
python3 Phase_10_Submission_Package/verification/make_tex_figure_set.py  # the vector set the .tex loads, in 13_Manuscript/figures/
```

- The first call is the frozen figure generator; the second and third are thin wrappers that call
  it with different save settings and then restore the tree (they re-verify the frozen hashes and
  `git checkout --` the PNGs afterwards, so running them cannot leave the working tree modified).
- The exporter wrapper is present in the repository: yes.
- **Raster rendition sizes:** the 600-dpi PNGs and TIFFs are gitignored derived files. They are
  shipped inside this archive when the working copy has them, and when it does not they are exactly
  one command away (the second one above: deterministic, about a minute). How many were packed is
  recorded in `09_ARCHIVE_METADATA/archive_build.json` -> `derived_files.figure_renditions_600dpi`,
  so a reader can tell which case they hold and can verify either way by re-running the exporter and
  diffing the files.
- The 200-dpi PNGs in `08_FINAL_OUTPUTS/figures/` are the tracked ones, so a reader can compare a
  regenerated figure against a shipped one without any network or repository access.

## From figure to number

Each figure is drawn from `03_DATA/` by the function named above; each data file records the code
freeze it came from; `03_DATA/processed/PRODUCTION_PROVENANCE.csv` maps run -> inputs -> output
hash -> wall time -> residuals. The manuscript quotes `03_DATA/processed/ANALYSIS_V2.json` through
the builder modules (`01_PROGRAM/builders/ms_*.py`), which read those files at build time - so a
changed data file changes the manuscript text, and no number is hand-typed anywhere in the chain.
