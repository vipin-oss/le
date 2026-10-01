# Recent heat-conduction models + material symmetry: preliminary paper options

**Search date:** 30 September 2026.  
**Scope:** Initial advice requested by the user; not a completed candidate-gap investigation or approved research project.  
**All proposed novelty claims:** CANDIDATE — GAP NOT CONFIRMED.

## 1. Interpretation requiring confirmation

The user wants a paper using a recent heat-conduction model, analysing materials with a different kind of symmetry. **Clarification received:** the user chose BOTH crystal/material and geometric symmetry and COUPLED THERMOELASTIC RESPONSE. The exact Google Drive paper, if one specific paper is intended as the base, is not identified. The focused follow-up proposal is in `THERMOELASTIC_DIRECTION_NOTE.md`; these initial options remain exploratory, not final selections.

No final model, material, geometry, equations or research direction has been selected.

## 2. Two recent, verified literature anchors

### A. Recent generalized CV/GN formulations — 2025

Huang, Yan, Wu and Yu, **New insights on generalized heat conduction and thermoelastic coupling models**, *Applied Mathematics and Mechanics (English Edition)* 46, 1533–1550 (2025), DOI `10.1007/s10483-025-3280-7`.

The verified abstract describes generalized Cattaneo–Vernotte and Green–Naghdi heat-conduction/thermoelastic formulations constructed through analogy with mechanical viscoelastic models, and a one-dimensional slim-strip thermal-shock study using Laplace transformation and numerical inversion. [1](https://link.springer.com/article/10.1007/s10483-025-3280-7)

**Inspection level:** metadata, abstract and accessible reference/landing-page content. Detailed model equations and coefficient restrictions were NOT inspected: Springer showed subscription content; the official journal landing-page fetch failed. Do not invent the exact 2025 operators from the model names.

**Why relevant to the supplied corpus:** it offers a recent starting point close to the user's semi-analytical thermoelastic background without automatically repeating MGT/MDD/KG combinations.

### B. Viscous Heat Equations (VHE): recent 2026 study, 2020 foundation

Dragašević, Rajkov and Simoncelli, **Viscous Heat Backflow and Temperature Resonances in Extreme Thermal Conductors**, *Physical Review Letters* 136, 186302, published 8 May 2026, DOI `10.1103/nbbn-56hr`.

The paper applies viscous heat equations to graphite and hexagonal boron nitride, treating thermal viscosity, steady heat backflow/vortices and transient temperature-wave resonances. [1](https://journals.aps.org/prl/abstract/10.1103/nbbn-56hr)

VHE itself is not a model invented in 2026: its foundation, **Generalization of Fourier's Law into Viscous Heat Equations**, was published in *Physical Review X* 10, 011019 (2020). It describes coupled temperature and phonon-drift-velocity fields. [2](https://journals.aps.org/prx/abstract/10.1103/PhysRevX.10.011019)

**Inspection level:** 2026 publisher metadata/abstract plus article-text sections on the VHE, steady/transient backflow and resonances (web chunks 0–2). Downloading the version-of-record PDF returned HTTP 403; some mathematical symbols disappear in the text extraction, so exact equations/tensor normalizations must be recovered from a readable authorized source/supplement before formulation.

**Important scope:** graphite/hBN vortices and resonance are already studied in this 2026 paper. Repeating that result with a different plot style is not a new contribution.

## 3. Material choices with evidence—not newly discovered materials

These are possible materials new to the intended study, not claims of their recent discovery.

### Monoclinic beta-Ga2O3

A 2025 *Physical Review B* study, **Anisotropic anharmonicity dictates the thermal conductivity of beta-Ga2O3**, identifies its monoclinic structure and four independent conductivity-tensor components, and analyses the role of phonon renormalization in conductivity predictions. [1](https://par.nsf.gov/servlets/purl/10617360)

A direct experimental anchor is **Three-dimensional anisotropic thermal conductivity tensor of single crystalline beta-Ga2O3**, *Applied Physics Letters* 113, 232105 (2018). It reports a measured conductivity tensor, orientation dependence and uncertainty. [3](https://pubs.aip.org/aip/apl/article/113/23/232105/36409/Three-dimensional-anisotropic-thermal-conductivity)

**Useful feature:** lower symmetry with off-diagonal conductivity permitted in an appropriate coordinate convention. **Caution:** published axes/Miller directions must be mapped into an orthonormal Cartesian frame; non-orthogonal lattice axes must not be treated as Cartesian axes.

**Evidence limitation:** measured conductivity is not a measured generalized-model relaxation time and does not validate ultrafast non-Fourier predictions.

### Orthorhombic black phosphorus (BP)

BP is a possible in-plane anisotropic comparison material. Measurements of suspended few-layer BP distinguish armchair and zigzag heat conduction and its thickness dependence. [1](https://www.nature.com/articles/ncomms9572)

For a hydrodynamic route, **Observation of Poiseuille flow of phonons in black phosphorus**, *Science Advances* 4, eaat3374 (2018), reports heat-flow measurements over 0.1–80 K and Poiseuille signatures in a low-temperature window, including faster-than-cubic conductivity behavior between 5 and 12 K. [1](https://pmc.ncbi.nlm.nih.gov/articles/PMC6014719/)

**Evidence limitation:** do not mix room-temperature thin-film conductivity with cryogenic bulk hydrodynamic coefficients. Thickness, temperature, sample quality and transport regime must be declared consistently. BP thermal-viscosity/collision parameters for a quantitative VHE model are not established by this initial search.

### Cubic gamma / monoclinic beta Ga2O3 comparison

**Thermal conductivity of double polymorph Ga2O3 structures**, *APL Materials* 12, 081108 (2024), DOI `10.1063/5.0213985`, already studies gamma/beta interfaces using TDTR and simulations. The measured gamma-phase response is associated with a cubic spinel structure, while beta-phase transport is anisotropic. [1](https://pubs.aip.org/aip/apm/article/12/8/081108/3307887/Thermal-conductivity-of-double-polymorph-Ga2O3)

**Useful feature:** same chemical composition but different phases/symmetries. **Caution:** phase changes also change defects, density, heat capacity, scattering and interface properties; observed differences cannot automatically be attributed exclusively to symmetry. The existing thermal-interface study is a competing/reference paper, not a confirmed gap. Gamma-phase material-data completeness must be investigated.

## 4. Three focused candidate directions

### Option A — Generalized heat-memory response in a monoclinic crystal

**Proposed working title:** *Symmetry-constrained generalized heat conduction in monoclinic beta-Ga2O3: directional transient response and model discrimination.*

**Possible 2025 base:** generalized CV/GN paper above, after full-text model reconstruction.

**Main question:** can an admissible recent model predict directional, time/frequency-dependent thermal response that cannot be explained by ordinary anisotropic Fourier conduction at the same conductivity tensor?

**Possible decisive outputs:** orientation-resolved pulse response; amplitude/phase response; flux-direction response; stability/admissibility bounds; a criterion for when non-Fourier effects are resolvable rather than merely fitted.

**Evidence route:** reconstruct the source paper's one-dimensional case for code verification; verify the anisotropic Fourier limit against an independent method; use published Ga2O3 conductivity data within their scope. Non-Fourier material coefficients require separate evidence or explicit hypothetical/dimensionless-study labels.

**Feasibility:** likely compatible with MATLAB and semi-analytical/spectral/numerical methods; no runtime estimate has yet been profiled. Main blockers are full-model access, coefficient restrictions and justified dynamic parameters.

**Overlap boundary:** not merely another MGT/MDD/KG parameter study. The recent formulation, symmetry constraints and decisive model-discrimination question must provide the difference.

### Option B — Symmetry-aware diagnostics of hydrodynamic heat flow

**Proposed working title:** *Distinguishing anisotropic Fourier transport from viscous heat backflow in low-symmetry crystals.*

**Possible base:** VHE with the 2026 PRL study as a recent verification/reference anchor. BP is a candidate anisotropic target; graphite/hBN can be reference cases already studied in the literature.

**Main question:** which observable signatures distinguish genuine non-Fourier transport from geometric/orientation effects of ordinary anisotropic conduction?

**Analytical starting observation, not a novelty claim:** for constant diagonal conductivity in 2D,

```text
qx = -kx*T_x, qy = -ky*T_y
(curl q)_z = (kx-ky)*T_xy.
```

Thus a nonzero curl of heat flux is possible even under anisotropic Fourier's law. Vorticity alone is not a universal hydrodynamic diagnostic. For symmetric positive-definite local conductivity, however,

```text
q dot grad(T) = -grad(T)^T K grad(T) <= 0.
```

These elementary identities must not be presented as newly discovered mathematics. A possible contribution would be a scoped, robust diagnostic/design framework with controlled simulations and material-consistent transport coefficients. Departure from local Fourier behavior is not, by itself, unique proof of hydrodynamics; competing ballistic explanations also require consideration.

**Evidence route:** reproduce an isotropic reference case; verify tensor rotations and Fourier limits; establish BP hydrodynamic parameter provenance and applicable regime. Existing BP measurements do not automatically validate every proposed transient/vortex prediction.

**Main blocker:** full thermal-viscosity/momentum-dissipation/coupling tensor data. Conductivity alone is insufficient. First-principles calculations would add a substantially different computational burden; do not assume the current FEM4 code provides those coefficients.

### Option C — Same-composition, different-symmetry thermal interfaces

**Proposed working title:** *Non-Fourier transient heat transfer across cubic–monoclinic Ga2O3 interfaces: orientation, thermal memory and contact resistance.*

**Main question:** can independently supported thermal-memory effects be distinguished from ordinary interface resistance and phase-specific conductivity in gamma/beta structures?

**Possible base:** the 2025 generalized CV/GN family, subject to admissible tensor/interface extension and full source inspection.

**Evidence route:** use the 2024 gamma/beta study as an existing physical reference, not a new idea; reconstruct its experimental/model scope; compare Fourier/interface-only and generalized-model predictions without reusing calibration data as independent validation.

**Main blockers:** complete phase-specific heat capacity/dynamic parameters, interface conditions, and possible parameter non-identifiability. This option must also be distinguished from the user's existing GK inverse manuscript, not simply repeat its estimation story.

## 5. Recommendation is conditional, not a final selection

- For continuity with the user's analytical thermoelastic research and a recent generalized constitutive family: investigate **Option A** first, but obtain/read the 2025 full equations before proceeding.
- For a pure heat-conduction paper focused on microscopic transport mechanisms and observable signatures: investigate **Option B**, conditional on the required tensor data being obtainable.
- For a phase/symmetry-interface study: **Option C** is plausible but has substantial data and existing-literature overlap risks.

No arbitrary candidate score, novelty confirmation, Q1 guarantee or journal-quartile claim is made. None of the proposals has undergone a closest-five-paper matrix or full scooping search.

## 6. Numerical infrastructure boundary

The provided FEM4 MATLAB package is static electromechanics, not an existing heat solver. Its mesh/assembly/scaling/testing/output organization may be reusable, but thermal equations, boundary/initial conditions and time/frequency solution need dedicated implementation. FEM/BFS will not be forced; method selection follows the chosen equations.

## 7. Clarifications needed before a precise paper plan

1. **Resolved:** user chose both crystal/material and geometric symmetry.
2. **Resolved:** user chose coupled thermoelastic response.
3. **Pending:** if a specific previously shared Google Drive paper is intended as the model base, provide its title or workbook Sr. No.
4. **Pending:** explicit user shortlisting of the focused recommendation in THERMOELASTIC_DIRECTION_NOTE.md.

**Next action:** wait for exact-direction shortlisting and any intended source-paper identification. No final problem selection, model derivation, scientific simulation or production run has been undertaken.
