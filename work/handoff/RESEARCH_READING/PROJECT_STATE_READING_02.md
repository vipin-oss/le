# Project recovery state — literature and existing-code reading 02

Date: 30 September 2026. Latest recovery summary as of the second user-input reading task.

## Scope / authorization

The user first provided a published-paper Excel list and an unpublished-paper ZIP and requested preliminary literature reading. The user then supplied `FEM4_final_package (2).zip` and asked the assistant to obtain an idea of the program from it. Authorized work: download, inspect, understand and document the existing code. No numbered research phase, new topic selection, code modification, numerical regression or production run was authorized/performed.

The user previously supplied FINAL MASTER PROMPT v2.0: correctness and evidence first; separate verification/physical validation; no forced method or thermal physics; user approval of research direction/major changes; traceability/reproducibility and phase stopping. The full master prompt is not stored in this folder; supply/read it separately in a future session.

## Preserved inputs

1. `/home/user/RESEARCH_PROJECT_INPUT/LITERATURE/Vipin_Research_Papers_06-Aug_2026.xlsx`.
2. `/home/user/RESEARCH_PROJECT_INPUT/PREVIOUS_PROJECTS/FEM_Total.zip` and extracted PDFs in `FEM_Total/`.
3. Eight representative published PDFs in `LITERATURE/Accessible_Published_Fulltexts/`.
4. `/home/user/RESEARCH_PROJECT_INPUT/EXISTING_CODE/FEM4_final_package (2).zip`.
5. Extracted FEM4 package at `/home/user/RESEARCH_PROJECT_INPUT/EXISTING_CODE/FEM4_final_package_2/FEM4_final_package/`.

Original files/code were not modified. Downloads/provenance/checksums are in the relevant `SOURCE_MANIFEST.json` files.

## Previous corpus reading completed

- 48 Excel records; 47 distinct supplied DOI strings. This is not 47 independently verified publications.
- IDs 36 and 41 duplicate title and DOI `10.1080/15376494.2024.2440131`.
- ID 47 workbook DOI differs from PDF/publisher; proposed correct DOI `10.1016/j.jppr.2026.02.007`. Raw Excel unchanged.
- Crossref: 12 successful metadata responses, 36 HTTP 429 rate-limit responses. 429 is not evidence of invalid publication.
- Published PDF IDs 1, 2, 25, 29, 35, 38, 45, 47 received section-level first-pass reading; other entries not full-text reviewed. IDs 10 and 21 retrieval unresolved.
- Eight unpublished manuscripts received section-level reading, not exhaustive equation/code audits.
- Main literature notes: `/home/user/RESEARCH_READING/READING_REPORT.md`; statuses in `READING_STATUS.csv`.

## Observed scientific ecosystem

Published work emphasizes coupled wave propagation, generalized thermoelasticity/heat-memory/fractional models, KG/spatial nonlocality, piezoelectric/piezomagnetic/semiconductor coupling, porosity, SH/Rayleigh/interface waves, rotation, gradation and imperfect/impedance boundaries.

Unpublished work includes:

- FEM1/FEM2: ellipsoidal internal-length tensors, anisotropic strain-gradient mechanics and C1 Hermite/BFS frameworks.
- FEM3: total-Lagrangian finite-strain Mindlin/BFS formulation.
- FEM4: reduced piezoelectric–flexoelectric coupling, strain-gradient mechanics and conditioning.
- FEM5: tetragonal BaTiO3 pyro/piezo voltage and thermal-stress reduction; optional flexoelectric contribution not used in quantitative results.
- GK: Fourier-resonance-induced coefficient non-identifiability and synthetic inverse/model-selection analyses.
- QC: inertial/diffusive/telegraph phason dynamics, branch selection, surrogate parameters and configuration-specific electric decoupling.
- Torsional draft: surface elasticity/metamaterial shell and reported thermal decoupling in a specified linear isotropic configuration. Its title page lists Annu Rani and M. S. Barak, not Vipin Gupta; user relationship is unconfirmed.

No novelty of these claims was independently confirmed. Their reported numerical findings were not reproduced. Both published and unpublished work must be considered when assessing overlap in future discovery.

## New code package: actual observations

- Source: https://github.com/vipin-oss/BFS-FEM-MATLAB/blob/main/FEM4_final_package%20(2).zip
- GitHub blob SHA: `6993f8a23f5ce9a3def5ae74875b5d1872f3283d`.
- Archive: 2,282,857 bytes; 226 files; 3,930,102 uncompressed bytes.
- 113 `.m` files total; 89 in `program/MATLAB_COMPLETE_PROGRAM/`; three Python figure scripts.
- Includes TeX/PDF manuscript, master-calculation TeX, CSV/MAT result artifacts, figure-generation code and audit documents.
- Same-title FEM4 manuscript is included, but its PDF hash differs from the earlier `FEM_4_Paper.pdf`; exact revision alignment not certified.

### Core model / discretization

Linear static 2D plane-strain classical + Mindlin Form-II strain-gradient elasticity with reduced piezoelectric/flexoelectric couplings and dielectric electrostatics.

Per-node mechanical order:
`[u,u_x,u_y,u_xy,v,v_x,v_y,v_xy]`.

Mechanical displacement uses C1 bicubic Hermite/BFS; electric potential uses C0 bilinear Lagrange. Four-node element: 32 mechanical plus 4 electrical DOFs = 36. Global unconstrained total: `9*nnode`.

Operators:
- `epsV = [u_x,v_y,u_y+v_x]^T`.
- `etaV = [u_xx,u_xy,v_xy,v_yy,u_xy+v_xx,u_yy+v_xy]^T`.
- `grad(phi) = Bphi*q_phi`; electric field is its negative.

Blocks:
- `Kuu = integral(Be^T C Be + Beta^T D Beta)`.
- `Kup = integral((Be^T eV^T + Beta^T muV^T)*Bphi)`.
- `Kpp = integral(Bphi^T*kappa*Bphi)`.

System:
`[Kuu Kup; Kup^T -Kpp]*[q_u;q_phi] = [F;-Q]`.

Uniform rectangular mesh; constant material per current assembly; sparse blocks, 4x4 Gauss integration, essential-BC elimination, optional symmetric-congruence DOF scaling and linear backslash solve. Some study functions duplicate optimized assembly/solve paths.

### Entry points / outputs

- `main.m`: selected verification and benchmark routines; does not regenerate every study/figure.
- `run_full_scientific_regression.m`: 20 named summary entries in actual source.
- `studies/`: convergence, Lambda/refinement, aspect ratio, hcrit, boundary-condition and field exports.
- `output/`: supplied CSV/MAT artifacts; study execution can overwrite these.
- MATLAB paper-figure layer prefers frozen bundled data; three Python helpers include fixed numerical arrays/absolute build paths.

No thermal field/heat equation, mechanical mass/transient solver, or finite-strain Newton mechanics is implemented in this core. The Legendre-rule Newton routine is not a nonlinear mechanical solver. Arbitrary anisotropic/ellipsoidal tensors, graded integration or distorted meshes are not automatically implemented by this package.

### Evidence boundaries / static concerns

1. No MATLAB/Octave executable found in this workspace; scientific execution is **NOT_RUN**. Do not say the archived PASS claims were observed here.
2. `benchmark_tier1(false)` computes rates from supplied norms; optional FEM uses assumed documented BCs and is not claimed to recreate the source benchmark.
3. `hcrit_study(false)` fits four source-reported roots, not FEM-recovered roots. Referenced `section6_master_dataset.json` is absent.
4. Static algebra finding in optional `hcrit_study.m` branch, lines 96–100: `a4=a5=0.5*D0`, while `constitutive_D` gives `D11=2*(a1+...+a5)`, so this creates `2*D0`, not the commented `D0`. **ANALYTICALLY_CHECKED — STATIC ONLY**. No correction/re-run performed. Default source-root regression is a separate calculation.
5. `verify_limiting_cases.m` skips D=0 solves and conflates exact singularity with numerical ill-conditioning in comments. Its `all_pass` uses decoupling checks, not all solve/energy checks. Independent scoped review needed.
6. BaTiO3 e=0/centrosymmetric interpretation needs a stated phase/idealized benchmark scope, especially relative to separate tetragonal FEM5 work.
7. Absolute plotting paths, fixed arrays, frozen-data precedence and stale documentation references need reproducibility cleanup before claiming full rebuild capability.
8. Eleven same-name solver-output/frozen-figure CSV pairs are byte-identical; this is only a copy-consistency check.
9. Three Python scripts passed AST parsing, not runtime execution.

## Current status

- New research direction/model/method: NOT_SELECTED / NOT_APPROVED.
- Existing mathematical/physical validity: NOT_INDEPENDENTLY_CERTIFIED.
- Code available: MATLAB FEM4 package observed; core architecture inspected.
- Code modification: NONE.
- Scientific verification/validation execution: NOT_RUN.
- Production computation: NONE.
- User hardware, licences, preferred runtime, budget, timeline and experiment access: UNKNOWN.
- Comprehensive novelty/scooping and journal-quartile checks: NOT_STARTED.

## Decisions

- Preserve originals and distinguish supplied artifacts from fresh outputs.
- No forced BFS/FEM/thermal model for future research.
- Use existing code only where the selected problem justifies it.
- Before new execution, preserve archived outputs or run in a versioned working copy.
- Any model/code correction must be logged, tested and revalidated in scope.
- No new topic was proposed/approved and no publication readiness certificate was issued.

## Exact next action

Wait for the user. If code verification is authorized, first choose a MATLAB/Octave execution environment, use a protected working copy, define scoped tests/reference cases, and resolve the static notes without silently altering equations. If discovery is authorized, use this corpus/code capability as evidence of reusable infrastructure but compare both published and unpublished overlap and verify current literature.

## Recovery artifacts

- `READING_REPORT.md`, `PROJECT_STATE_READING_01.md`, this `PROJECT_STATE_READING_02.md`.
- Published/unpublished inventories, `READING_STATUS.csv`, literature search/evidence logs and extracted text under `RESEARCH_READING/`.
- `/home/user/CODE_REVIEW/FEM4_PACKAGE/CODE_OVERVIEW.md` — main code walkthrough.
- `PACKAGE_INVENTORY.csv`, `SOURCE_FUNCTION_INDEX.csv`, `EQUATION_TO_CODE_MAP.csv`.
- `STATIC_INSPECTION_RESULTS.json`, `SOURCE_MANIFEST.json`.

No research-phase cumulative ZIP/final project package was created during these input-reading tasks.
