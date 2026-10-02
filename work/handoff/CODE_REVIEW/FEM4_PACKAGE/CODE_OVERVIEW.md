# FEM4 program — architecture aur equation-to-code walkthrough

**Inspection date:** 30 September 2026  
**Authorization:** User asked to understand the program from the supplied ZIP.  
**Status:** Core source walkthrough and artifact inventory completed. Scientific MATLAB/Octave execution: **NOT_RUN**.

> Yeh source-level understanding hai, independent verification/physical validation certificate nahi. Archived PASS reports, CSV values and manuscript results are supplied artifacts—not newly observed solver outputs in this session. Original code/package was not modified.

## 1. Package and version

Source: https://github.com/vipin-oss/BFS-FEM-MATLAB/blob/main/FEM4_final_package%20(2).zip

- Archive: 2,282,857 bytes; 226 files; 3,930,102 uncompressed bytes.
- 113 MATLAB `.m` files in the whole package; **89** inside `program/MATLAB_COMPLETE_PROGRAM/`.
- Three Python scripts support final figure generation; Python is not the supplied primary FEM solver.
- Manuscript LaTeX/PDF, a master-calculation TeX document, 49 CSV files, 11 MAT files, figure assets and audit/readme documents are included.
- GitHub blob SHA and local SHA-256 are in `SOURCE_MANIFEST.json`.
- The package includes the same-title coupled piezoelectric–flexoelectric FEM4 manuscript. Its `main_final.pdf` is not byte-identical to the previously supplied `FEM_4_Paper.pdf`; exact revision/scientific-content alignment has not been certified.

Local immutable input:
`/home/user/RESEARCH_PROJECT_INPUT/EXISTING_CODE/FEM4_final_package (2).zip`

Extracted root:
`/home/user/RESEARCH_PROJECT_INPUT/EXISTING_CODE/FEM4_final_package_2/FEM4_final_package/`

The mathematical 'master' is an author-supplied derivation source. Calling it frozen/authoritative in the package does not independently establish its scientific correctness.

## 2. Actual model implemented

### Physics and scope

- Linear, static, two-dimensional plane-strain electromechanics.
- Classical elasticity plus Mindlin Form-II strain-gradient elasticity.
- Reduced piezoelectric and flexoelectric couplings.
- Dielectric electrostatics.
- Rectangular uniform structured mesh with constant supplied material coefficients.

**No thermal field/heat equation, mechanical mass matrix, transient integration, or finite-strain Newton solver was found in this core walkthrough.** A Newton iteration used to construct Gauss rules is not a nonlinear mechanical solver.

The material helpers include idealized BaTiO3, PZT-5H and a Shekarchizadeh strain-gradient benchmark set. The classical elastic matrix has equal first/second normal diagonal entries and is not an arbitrary full anisotropic elastic tensor. The five-constant gradient matrix is the supplied isotropic Mindlin reduction, not the ellipsoidal anisotropy implementation from the user's other manuscripts.

### Unknown fields and DOFs

Mechanical unknowns are `u(x,y)` and `v(x,y)`; electric potential is `phi(x,y)`.

At each node, the mechanical DOFs are:

```text
[u, u_x, u_y, u_xy, v, v_x, v_y, v_xy]
```

- Mechanical displacement: tensor-product bicubic Hermite/BFS, **C1** conforming on the implemented rectangular mesh.
- Electric potential: bilinear Lagrange, **C0**, one `phi` DOF per node.
- Four-node element: **32 mechanical + 4 electrical = 36 element DOFs**.
- Before constraints, global total is `9*nnode`; shared-node DOFs are not counted separately for every element.

C1 continuity of displacement does not mean every second derivative is globally continuous.

## 3. Variational structure visible in the code

Let `g = grad(phi)` and `E = -g`.

```text
epsV = [u_x, v_y, u_y + v_x]^T
etaV = [u_xx, u_xy, v_xy, v_yy,
        u_xy + v_xx, u_yy + v_xy]^T
```

The implemented enthalpy structure, also written in `verify_energy_balance.m`, is:

```text
H = 1/2 epsV^T C epsV
  + 1/2 etaV^T D etaV
  - 1/2 g^T kappa g
  + g^T eV epsV
  + g^T muV etaV
```

Engineering-shear factors and the declared component order matter. The electric-field minus sign is carried through the enthalpy/system convention; `B_phi_matrix` returns the potential gradient, not the electric field itself.

Element blocks:

```text
Kuu = integral(Be^T C Be + Beta^T D Beta) dOmega      [32 x 32]
Kup = integral((Be^T eV^T + Beta^T muV^T) Bphi) dOmega [32 x 4]
Kpp = integral(Bphi^T kappa Bphi) dOmega              [4 x 4]
```

Global system:

```text
[ Kuu   Kup ] [q_u  ] = [ F ]
[ Kup^T -Kpp] [q_phi]   [-Q ]
```

It is a symmetric saddle system, not a positive-definite coupled stiffness matrix. These expressions were traced to source files; signs/admissibility and independent derivations have not been fully audited here.

## 4. Program flow

```text
Material parameters + geometry + study settings
                 |
                 v
generate_mesh + DOF numbering
                 |
                 v
Hermite/BFS basis and physical derivatives
                 |
                 v
Be, Beta and bilinear Bphi operators
                 |
                 v
C, D, eV, muV and kappa matrices
                 |
                 v
4 x 4 Gauss integration of element blocks
                 |
                 v
Sparse global assembly
                 |
                 v
Essential BC elimination + potential reference
                 |
                 v
Optional symmetric-congruence DOF scaling
                 |
                 v
Linear backslash solve and recovery of physical DOFs
                 |
                 v
Displacement/potential/energy/conditioning observables
                 |
                 v
CSV and MAT exports -> plotting scripts -> manuscript figures
```

### Key files

| Layer | Source files | Observed responsibility |
|---|---|---|
| Entry points | `main.m`, `run_full_scientific_regression.m` | Selected checks/benchmarks; full regression summary contains 20 named entries. |
| Inputs | `config/material_*.m`, `simulation_parameters.m` | Material sets, reference scales and some numerical defaults. Individual studies also specify their own meshes/ranges. |
| Constitutive | `constitutive_C.m`, `constitutive_D.m`, `piezoelectric_e.m`, `flexoelectric_mu.m`, `dielectric_kappa.m` | Reduced matrix construction. |
| Basis/kinematics | `hermite_cubic.m`, `bfs_shape_functions.m`, `bfs_shape_derivatives.m`, `B_*_matrix.m` | Values, first/second physical derivatives, strain/gradient/electric operators. |
| Element/global assembly | `element_stiffness.m`, `element_coupling.m`, `element_electrical.m`, `assembly.m` | Element integrals and sparse shared-node assembly. |
| Loads/BCs | `apply_tip_load.m`, `make_cantilever_bc.m`, `apply_boundary_conditions.m` | End resultant distributed equally over free-edge nodes; clamp and gauge reference; symmetric reduction. |
| Solver/scaling | `solve_system.m`, `dof_scaling_vector.m` | Assemble, constrain, scale, solve and undo the scaling. |
| Studies | `studies/` | Convergence, Lambda sweep/refinement, aspect ratio, critical thickness, BC comparisons and field exports. |
| Checks | `verification/` | Basis/derivative, constitutive, symmetry, quadrature, energy, limiting-case and conditioning routines. |
| Figures | `plotting/`, `paper_figures/` | Numerical-data visualization; supplied Python scripts generate revised final figures. |

`main.m` does not regenerate every production study/figure. Those have separate entry points. Study functions may write/overwrite their own `output/*.csv` and `.mat` files when executed.

## 5. Scaling, loads and observables

### Scaling

`dof_scaling_vector.m` constructs per-field factors consistent with:

```text
q = T .* qbar
Kbar = diag(T) K diag(T)
fbar = diag(T) f
```

Mechanical value/slope/twist factors are `[u0, u0/L0, u0/L0, u0/L0^2]`; the electrical factor is `phi0 = u0*sqrt(C0/kappa0)`. Prescribed BC values are scaled too, and the recovered solution is transformed back to physical DOFs.

The purpose is to handle representation/unit-scale disparities; condition-number improvement alone is not physical validation.

### Boundary/load model

The default cantilever helper fixes all eight mechanical DOFs at left-edge nodes and grounds one electric node. In open-circuit studies, no external nodal charge is supplied. This is a specific electrical boundary problem, not automatically an electroded-device voltage measurement model.

`apply_tip_load.m` distributes a specified force resultant equally over right-edge **value** DOFs. This is not a general consistent Hermite traction/double-traction integration routine.

Several studies report `max(abs(q_phi))`, a potential magnitude relative to the chosen ground. It must not silently be renamed an arbitrary electrode-to-electrode measured voltage.

### Energy conventions

The code distinguishes:

```text
P = F^T q_u                 dead-load product (open circuit)
W_qs = P/2                  proportional quasi-static loading work
U_mech = 1/2 q_u^T Kuu q_u
U_elec = 1/2 q_phi^T Kpp q_phi
U_coup = q_u^T Kup q_phi
```

`aspect_ratio_study.m` defines its main ratio on the dead-load product and also exports a quasi-static-work ratio. Older/auxiliary CSV headings must be interpreted through their producer, not assumed identical because the column is called `W_ext`.

## 6. Tests, supplied data and what was not executed

### Observed test architecture

The regression source has **20 named summary entries**. They are heterogeneous:

- Actual FEM/constitutive/basis/quadrature/energy routines when run.
- Checks of algebraic identities.
- Recalculation of rates from supplied benchmark norms.
- Regression on four source-reported critical-thickness roots.

Therefore '20 PASS' is not equivalent to 20 independent physical validations or 20 newly reconstructed literature benchmarks.

### Evidence/provenance distinctions

1. `benchmark_tier1(false)` calculates convergence rates from explicitly entered source-reported norms; it does not execute a FEM error-norm study.
2. Optional Tier-1 FEM uses documented assumed BCs and a point observable; it expressly does not claim to reconstruct the literature benchmark setup.
3. `hcrit_study(false)` fits supplied roots; it does not recover those roots from the current FEM model.
4. `section6_master_dataset.json` is referenced but absent. The loader reports this instead of constructing missing reference data. This limits those reference comparisons; it does not mean all core studies are unavailable.
5. The paper-figure MATLAB layer preferentially reads its bundled frozen data. Re-running the solver does not automatically make every figure use the new `output/` data.
6. Eleven same-name CSV pairs in `output/` versus bundled paper-figure `data/` were byte-identical in this inspection. This checks copies, not their numerical truth or full figure provenance.

**Current execution status:** neither a MATLAB nor an Octave executable was found in this workspace. No installation, translation, solver run, regression run or production sweep was undertaken. The three Python figure scripts passed AST parsing only; they were not executed.

## 7. Bounded static concerns to check before reuse

This is not a full bug audit. The following observations arose during the walkthrough:

### S01 — Optional critical-thickness branch: factor-of-two mismatch

In `studies/hcrit_study.m`, lines 96–100:

```matlab
mat.a1 = 0; mat.a2 = 0; mat.a3 = 0;
mat.a4 = 0.5*D0; mat.a5 = 0.5*D0;   % 2(a4+a5) = D0
```

But `constitutive_D.m` defines `D11 = 2*(a1+a2+a3+a4+a5)`. The assignments above produce **D11 = 2*D0**, not the commented target `D0`.

**Status: ANALYTICALLY_CHECKED — STATIC ALGEBRA.** The optional FEM branch was not run. This observation does not invalidate or reproduce the separate fit to four source-reported roots. No code was changed. Any correction/re-run needs its own documented change and result provenance.

### S02 — Limiting-case claims need a sharper numerical/mathematical distinction

`verify_limiting_cases.m` skips its D=0 solves. Its comments mix thin-mesh numerical ill-conditioning with an assertion of exact singularity. Those are not equivalent and should be independently checked in a suitable scaled representation. The aggregate `all_pass` is based on decoupling checks, not completion of every limiting-case solve/energy residual.

### S03 — Material-phase interpretation

The BaTiO3 helper deliberately sets piezoelectric coefficients to zero and labels the material centrosymmetric. Reuse should identify the assumed phase/temperature or idealized benchmark specialization; do not generalize that comment to every BaTiO3 state, especially when comparing with the user's separate tetragonal pyroelectric manuscript.

### S04 — Reproducibility wiring

- Python figure scripts contain build-machine absolute paths; they will need controlled path configuration for a new environment.
- Some figures embed numerical arrays rather than reading the named CSVs directly; numerical source-to-figure checks should therefore be explicit.
- Bundled figure data can take precedence over freshly generated results.
- README/traceability references to `FINAL_CALCULATION_REFERENCES.bib`, `MASTER_CALCULATION_AUDIT.md`, and `assembly_Kuu.m` were not found in the archive. These are documentation/package-completeness observations, not proof of solver failure.
- Some studies duplicate an optimized assembly/solve path rather than calling `solve_system.m`; future core changes must be propagated and regression-checked across those paths.

## 8. What can potentially be reused

Reusable candidates, subject to independent checks and fit to the new problem:

- Rectangular Hermite/BFS basis and derivative operators.
- Engineering-Voigt conventions and higher-order weak-form organization.
- Sparse block assembly and essential-BC elimination.
- Electromechanical saddle-system structure.
- Congruence scaling and recovery of physical DOFs.
- Data exports, parameter-study patterns and test organization.

Not automatically already available:

- General unstructured/distorted/curvilinear mesh treatment.
- Arbitrary anisotropic material tensors or spatially graded coefficients.
- Full general flexoelectric tensor.
- Thermal transport/thermoelastic dynamics.
- Mechanical inertia, wave dispersion, time integration or nonlinear finite strain.
- A validated physical material/device model.

The research problem still determines whether this code should be extended, used only for a benchmark, or not used at all.

## 9. Supporting review artifacts

- `PACKAGE_INVENTORY.csv` — all 226 files.
- `SOURCE_FUNCTION_INDEX.csv` — MATLAB source/function index and checksums.
- `EQUATION_TO_CODE_MAP.csv` — observed core equation/function map.
- `STATIC_INSPECTION_RESULTS.json` — actual inventory, environment, copy checks and static notes.
- `SOURCE_MANIFEST.json` — downloaded archive version/provenance.
- `/home/user/RESEARCH_READING/PROJECT_STATE_READING_02.md` — cumulative recovery state.

**Bottom line:** program ka actual architecture, DOF scheme, constitutive blocks, assembly/solver flow aur result-generation structure samajh aa gaya hai. Numerical correctness, physical validity aur every-paper-number reproduction remain separate, pending tasks. No new research direction or major code change was selected.
