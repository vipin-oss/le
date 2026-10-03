# MODEL_DESCRIPTION

Pointers, not a paraphrase: the equations are in the two documents named below and in the
manuscript sections; the constants are quoted straight out of the source.

## Authoritative descriptions, in this archive

| aspect | read this |
|---|---|
| physics and constitutive law | `05_DERIVATIONS/theory/FORMULATION_ADDENDUM.md` |
| what was frozen as the acceptance criteria | `05_DERIVATIONS/acceptance_criteria/ACCEPTANCE_CRITERIA_V2_FROZEN.md` |
| discretisation, mapping, contour integration, stability | `05_DERIVATIONS/numerical_method/NUMERICAL_METHOD_V2.md`, `STABILITY_REPORT.md`, `CONVERGENCE_REPORT.md` |
| how it is stated to a reader | manuscript sections 2-4 (`08_FINAL_OUTPUTS/manuscript/manuscript_IJHMT.md`) |
| every equation, with derivations, as its own document | `05_DERIVATIONS/manuscript_derivation_source/calculations_IJHMT.md` and `02_OVERLEAF/FINAL_REVISED_CALCULATIONS.tex` |

## The model in eight bullet points (each is a claim the source code or a document supports)

- A cylindrical cavity of radius `a` sits in an infinite monoclinic medium; the outer boundary is a
  clamped cold circle at `R = 1e-08`-scaled 80a (`Rfac` in the data).
- A transient thermal pulse of non-dimensional width `tw` and centre `t0` is imposed on the wall
  (default `t0=2.5`, `tw=1.2` in `cg_bromwich`/`cg_solver` signatures).
- Conduction is generalised: Fourier (`tau = 0`), Lord-Shulman/Maxwell-Cattaneo-Vernotte (one `tau`),
  and a two-relaxation-time kernel used as an **exploratory** sensitivity, never as a prediction.
- Elasticity is the full monoclinic law: nine independent `Cij` (the model uses `C15`, `C25`, `C35`,
  `C46` as well as the diagonal block), so the shear-extension coupling is retained rather than
  assumed away.
- Thermal expansion is the crystal tensor `alpha_crys`, with `alpha_5` unresolved in the literature
  and set to 0 - stated in the paper, and the ablation E-series quantifies what the choice does.
- The problem is solved in the frequency domain on a radial-clustered mapped grid, and inverted with a
  Bromwich contour; the round-trip residual `back_max`/`backward_err` per run is in the provenance CSV.
- Quantities of interest are the peak wall hoop stress (nodal and interpolated) inside the frozen
  window `t <= 6.0 t_th`, its angular location, and the orientation
  modulation across `phi = 0..165 deg` in 15-degree steps.
- Uncertainty is grid-based: the reported envelope comes from the convergence families and the
  extrapolated refinement, not from a measurement-error model.

## Material and geometry constants, exactly as written in `01_PROGRAM/src/cg_model.py`

| name | line | value |
|---|---|---|
| `Cij_GPa` | `8` | `dict(C11=242.8, C22=343.8, C33=347.4, C44=47.8, C55=88.6, C66=104.0,
               C12=128.0, C13=160.0, C23=` |
| `K_ac` | `10` | `np.array([[12.13, -0.992], [-0.992, 14.09]])` |
| `alpha_crys` | `11` | `np.array([1.54e-6, 3.37e-6, 3.15e-6])` |
| `rho` | `12` | `5880.0` |
| `cp_ESTIMATED` | `13` | `560.0` |
| `T0` | `14` | `293.0` |
| `GPa` | `16` | `1000000000.0` |

## Scaling and case-level constants, from `cg_pipeline.py`

| name | line | value |
|---|---|---|
| `A0` | `14` | `1e-08` |
| `DV` | `15` | `derived()` |
| `KAPPA` | `16` | `DV['kappa']` |
| `C_REF` | `17` | `DV['c_ref']` |
| `T_QOI` | `20` | `6.0` |
| `PHIS` | `22` | `list(range(0, 180, 15))` |
| `PLAN_DEFAULT` | `23` | `dict(T=20.0, gamma=0.9)` |
| `GAMMA_DEFAULT` | `24` | `5.0` |
| `T_STORE` | `25` | `np.arange(0.0, 12.0 + 1e-9, 0.05)` |
| `T_FINE` | `26` | `np.arange(0.0, T_QOI + 1e-9, 0.01)` |
| `ALPHA_SETS` | `65` | `{
    'baseline_orlandi2015': (1.54e-6, 3.37e-6, 3.15e-6),         # PARAMETER_TABLE (secondary-quoted values ` |

## Fisher information / CRLB

Requirement asks for sensitivity, FIM and CRLB derivations. **No Fisher-information or Cramer-Rao
analysis exists in this project** - the strings `FIM`, `Fisher` and `CRLB` appear nowhere in the
repository, and none is claimed by the manuscript. Sensitivity is instead characterised by (i) the
grid-refinement and extrapolation study, (ii) the ablation matrix E/E+M, (iii) the `D_lambda_eps`
and pulse-width sweeps, all of which are shipped as CSVs in `03_DATA/tables/`. Recording a method
the project did not use would be the kind of invention this archive forbids.
