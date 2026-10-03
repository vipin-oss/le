# NUMERICAL_METHOD

Index into the method documents, plus the settings as the code states them.

## Read these

| topic | document |
|---|---|
| full method write-up | `05_DERIVATIONS/numerical_method/NUMERICAL_METHOD_V2.md` |
| stability analysis | `05_DERIVATIONS/numerical_method/STABILITY_REPORT.md` |
| convergence study and the extrapolation | `05_DERIVATIONS/numerical_method/CONVERGENCE_REPORT.md` |
| how the convergence report is produced | `05_DERIVATIONS/numerical_method/make_convergence_report.py` |
| the same, as the reader sees it | manuscript section 4 and `FINAL_REVISED_CALCULATIONS` |

## Settings extracted from the source

| module | callable / constant | as written |
|---|---|---|
| cg_bromwich | `BromwichPlan.__init__` | `{'T': 20.0, 'gamma': 0.9, 't0': 2.5, 'tw': 1.2, 'eps': 1e-10}` |
| cg_grid | `Grid.__init__` | `{'a': 1.0, 'chi': 1.0, 'R': 80.0, 'Nr': 96, 'Nt': 48, 'gamma': 3.5}` |
| cg_ops | `MappedOps.stress_first` | `{'beta': None}` |
| cg_pipeline | `material_variant` | `{'coupled': True}` |
| cg_pipeline | `material` | `{'iso': False, 'coupled': True, 'variant': None}` |
| cg_pipeline | `build` | `{'iso': False, 'coupled': True, 'energy_coupling': True, 'inertia_scale': 1.0, 'Nr': 96, 'Nt': 48, 'Rfac': 80.0, 'gamma_grid': 'GAMMA_DEFAULT', 'varia` |
| cg_pipeline | `transfer_set` | `{'probe_fracs': (1.5, 2.0, 3.0), 'a': None}` |
| cg_pipeline | `angular_upsample` | `{'factor': 16, 'axis': 0}` |
| cg_pipeline | `qoi_from_series` | `{'t_qoi': 'T_QOI'}` |
| cg_pipeline | `run_config` | `{'outdir': None, 'plan_kw': None, 'iso': False, 'coupled': True, 'energy_coupling': True, 'inertia_scale': 1.0, 'Nr': 96, 'Nt': 48, 'Rfac': 80.0, 'sav` |
| cg_ref1d | `transfer_1d` | `{'model': 'FOURIER', 'tau': 0.0, 'N': 120, 'coupling': True, 'inertia': True}` |
| cg_ref1d | `qs_single_pulse_reference` | `{'t0': 2.5, 'tw': 1.2, 'tstart': -7.0, 'tmax': 9.0, 'dt': 0.002, 'N': 1600}` |
| cg_solver | `HarmonicSolver.__init__` | `{'model': 'CV', 'tau': 0.0, 'outer_theta_value': 0.0, 'energy_coupling': True, 'inertia_scale': 1.0, 'refine': 2}` |
| cg_solver | `HarmonicSolver.stress_wall` | `{'w': None}` |

- Mapped grid: `x = A(rho) cos(eta)`, `y = B(rho) sin(eta)` with `A = ae + (Rout-ae) rho`,
  `B = be + (Rout-be) rho` (quoted from `cg_grid.py` docstring), with radial clustering `gamma`
  (`GAMMA_DEFAULT = 5.0` in `cg_pipeline.py`, changed from the hand-off 3.5 for near-wall
  resolution - the change and its reason are recorded as `P9-D001` in
  `07_DOCUMENTATION/program_control/DECISION_LOG.md`).
- The inversion chooses the number of contour points `K` so that the integrand decays below the
  tolerance stated in `cg_bromwich.py` (quoted in the table above), and the truncated-window choice
  `tw = 2.4` is tied to the pulse width, as the script comment records.
- Determinism: no RNG anywhere; BLAS pinned to a single thread by every driver.
