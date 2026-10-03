# README_DATA

The data package is the evidence base of the paper: raw per-run output, the processed results the
manuscript quotes, and the CSV tables behind every figure. Column-by-column detail, including the
array names inside each `.npz`, is in `DATA_DICTIONARY.md` (generated from the files themselves).

## Folders

| folder | what it is | produced by | regenerate with |
|---|---|---|---|
| `raw/convergence/` | grid-refinement family at gamma=5 (mesh-direction and refinement sweeps): 40 files | `08_Experiments/run_convergence.py` | `python3 01_PROGRAM/experiments/run_convergence.py` |
| `raw/convergence_gamma3p5/` | the hand-off grid family (gamma=3.5), partial by design - the paper says so: 34 files | `run_convergence.py` with the gamma=3.5 plan | see `05_DERIVATIONS/numerical_method/CONVERGENCE_REPORT.md` |
| `raw/production/` | the production matrix, one `.json` (scalars + metadata) + one `.npz` (field arrays) per run: 350 files | `08_Experiments/run_production_v2.py` | `python3 01_PROGRAM/experiments/run_production_v2.py heavy` + `... light` |
| `processed/` | the analysis the manuscript quotes (JSON + markdown tables) and the per-run provenance CSV | `08_Experiments/analyze_v2.py`, `make_provenance.py` | `python3 01_PROGRAM/experiments/analyze_v2.py` |
| `tables/` | the six CSVs the figures are drawn from (phi-sweep, convergence, D-vs-lambda, ablations E and E+M, pulse width) | `analyze_v2.py` | same command |

## Conventions that apply to every file

- **Stress** is wall hoop stress, in Pa per K of pulse amplitude (the loading is a unit-temperature
  pulse, so Pa/K is also the physical scaling). **Negative = compression.** Values like
  `-8.53e5` are therefore a compressive peak of 0.85 MPa/K.
- **Times are non-dimensional** in units of the cavity diffusion time `t_th` unless the key name
  says `_s`; `t_th_s` in each `.json` is the dimensional conversion factor in seconds.
- **Geometry** is given by `a_nm` (reference radius in nm), `chi` (ellipse aspect ratio, 1 = circle)
  and `phi` (orientation in degrees, a-axis reference); `Rfac` is the outer radius in units of `a`.
- **Angles on the wall** are reported twice on purpose: `th_star_nodal_deg` (grid node of the peak)
  and `th_star_interp_deg` (the interpolated peak location); they differ by up to one angular cell,
  and the interpolation is what the figures use.
- **Model** is `FOURIER` (`tau_ps = 0`) or `CV`/Maxwell-Cattaneo-Vernotte with `tau_ps` the
  relaxation time in ps; `coupled`/`energy_coupling`/`inertia_scale` are the switches the ablations
  flip. Their meanings are defined in `05_DERIVATIONS/` and in the manuscript section that uses them.
- **Precision:** everything is stored as float64; the `.json` files hold the values at full repr
  precision (not rounded), except where a stored comparison value is quoted to 4 digits by hand in
  a test report - `reproduce.py` documents exactly which of those exist and uses a looser tolerance
  for them.
- **Count:** 175 production runs carry a provenance row with wall time, solve count and
  the two residual measures; each row names the code-freeze sha it was produced with.

## Units and dimensionless groups, in the project's own words

The nondimensionalization is not restated here on purpose: read it in
`05_DERIVATIONS/numerical_method/NUMERICAL_METHOD_V2.md` and `05_DERIVATIONS/theory/FORMULATION_ADDENDUM.md`,
which are the documents the manuscript was written against. The scaling constants actually used at
run time are in `parameter_manifest.json` (`cg_pipeline.derived()`: `kappa_bar`, `c_ref`).
