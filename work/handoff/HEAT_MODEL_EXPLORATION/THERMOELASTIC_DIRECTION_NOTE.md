# Focused proposal after user clarification: coupled thermoelasticity + material/geometry symmetry

Date: 30 September 2026.

## Confirmed user scope versus unapproved choices

**User confirmed:** both crystal/material symmetry and geometric symmetry; coupled thermoelastic response.

**Not approved/confirmed:** exact recent model branch, material, geometry, final research direction, novelty, parameter set, computation or journal. This note is a provisional recommendation, not a completed gap investigation or scientific acceptance plan.

## 1. Recommended first shortlist

**Working title:**

> Crystal–geometry symmetry mismatch in monoclinic beta-Ga2O3: transient thermoelasticity with generalized heat conduction

**Recent starting literature:** Huang et al. (2025), *New insights on generalized heat conduction and thermoelastic coupling models*, DOI `10.1007/s10483-025-3280-7`. Its verified abstract treats generalized CV/GN formulations and coupled slim-strip thermal shock using Laplace transformation and numerical inversion. [1](https://link.springer.com/article/10.1007/s10483-025-3280-7)

This is closer to the user's confirmed coupled-thermoelastic aim than directly importing the 2026 VHE work, which treats temperature/phonon drift and would require a justified elastic coupling. The exact 2025 model operators, constitutive assumptions and parameter restrictions remain unread because full-text access was not obtained. Choose ONE justified recent branch after inspecting the full equations; do not construct a CV/GN/MGT/fractional hybrid by name.

**Primary material candidate:** monoclinic beta-Ga2O3. A 2025 PRB study discusses its anisotropic conductivity and monoclinic tensor structure; a 2018 experiment provides measured 3D conductivity with uncertainty. [1](https://par.nsf.gov/servlets/purl/10617360) [3](https://pubs.aip.org/aip/apl/article/113/23/232105/36409/Three-dimensional-anisotropic-thermal-conductivity)

**Important limitation:** these conductivity sources do not provide every elastic/thermal-expansion/dynamic parameter needed for the proposed coupled model. Material-complete data and generalized-model relaxation coefficients must be investigated separately.

## 2. Why both kinds of symmetry should interact in the same problem

Proposed question:

> How does a mismatch between geometric and crystal symmetries change the angular structure, timing and concentration of thermal stresses—and can those effects be separated from the effects of a non-Fourier heat-conduction law?

Uniform heating of a geometrically circular cavity does not generally justify an axisymmetric solution when the material tensors are anisotropic. Conversely, an observed angular pattern or peak change is not automatically a new heat-wave effect: ordinary anisotropic Fourier thermoelasticity must be a matched baseline.

The contribution cannot be only 'new material + different heat model + more plots'. A defensible candidate contribution is a symmetry/rotation-consistent explanation of angular-mode coupling and a testable criterion distinguishing geometry/crystal effects from generalized thermal-memory effects.

Neither this contribution nor its novelty has been established yet.

## 3. Proposed geometry and loading — not final assumptions

A controlled starting problem could be a **2D plane-strain cross-section of a long solid with a heated internal cavity**:

- Circular, rotationally symmetric outer boundary.
- Centered inner cavity changed from circle to ellipse.
- Crystal orientation varied relative to the ellipse axes.
- Spatially uniform, finite-duration inward heat-flux pulse on the cavity wall.
- Traction-free cavity wall.
- Outer thermal/mechanical conditions chosen to be rotationally covariant (for example, a uniform thermal reservoir and a prescribed zero outer displacement, if that physical configuration is selected).

Plane strain, outer restraint and thermal reservoir are proposed configuration choices, not user-confirmed physical conditions. A thin plane-stress plate is a different reduction and must not be substituted without revisiting the model.

### Fair controls

- Preserve cavity area when comparing circle and ellipse, unless an explicitly different experimental/design question is selected.
- Preserve total deposited heat per unit depth, not merely the local flux value when perimeter changes.
- Compare each generalized-model run with Fourier thermoelasticity using the SAME material tensors, geometry, source and BCs.
- Check outer-boundary dependence or explicitly interpret the problem as a finite body; do not call a finite-domain result an infinite-body solution without evidence.
- Use a finite pulse bandwidth compatible with local-equilibrium/continuum assumptions. Do not treat a mathematical instantaneous thermal shock as physically valid at arbitrarily high frequencies.

## 4. Essential symmetry check: circle versus ellipse

For an entirely circular configuration with rotationally covariant loading and BCs, rigidly rotating all crystal tensors must rotate the solution. It must not spuriously change rotation-invariant quantities, such as the global maximum principal stress, solely because of the chosen laboratory angle.

A geometrically circular specimen can still have a non-axisymmetric FIELD in an anisotropic crystal; rotation covariance and axisymmetry are different properties.

For an elliptical cavity, orientation relative to the ellipse is physically meaningful. Whether, how strongly and in which parameter regime peak stress, peak location or phase changes occur is a hypothesis to test, not an observed result.

This check should be included before interpreting orientation-dependent plots. It guards against coordinate-rotation or loading errors masquerading as physics.

## 5. Material and constitutive scope

A focused manuscript should initially use one primary material and at most one well-supported comparator, rather than six unrelated materials.

Possible choices, subject to complete parameter/overlap checks:

- **Primary:** monoclinic beta-Ga2O3.
- **Comparator:** orthorhombic black phosphorus, if a consistent coupled elastic/thermal dataset and temperature regime can be established. Its directional conductivity is experimentally supported, but bulk/few-layer and cryogenic/room-temperature datasets must not be mixed. [1](https://www.nature.com/articles/ncomms9572) [1](https://pmc.ncbi.nlm.nih.gov/articles/PMC6014719/)
- **Verification/control:** an isotropic constitutive limit; optionally a real cubic crystal only if the full coupled dataset is appropriate. Cubic thermal conductivity does not imply a fully isotropic fourth-rank elastic tensor.

### Tensor treatment required

- Rotate conductivity, elasticity and thermal expansion consistently; do not rotate only conductivity.
- Define an orthonormal Cartesian frame and the material-cut plane. Monoclinic lattice directions are not automatically orthogonal Cartesian axes.
- Check whether the chosen material/cut permits in-plane/anti-plane decoupling. Do not force a two-field mechanical reduction if the transformed full tensor couples the excluded displacement.
- Perform the full 3D thermal-stress contraction before a plane-strain/plane-stress reduction. Omitting the out-of-plane expansion contribution can change the effective thermal loading.
- Separate measured/literature, fitted, assumed and sensitivity-only parameters.
- Do not add piezoelectricity, flexoelectricity, porosity, magnetic fields or strain-gradient mechanics merely because the existing FEM4 package has some of those features.

## 6. Possible decisive analyses

These are proposed analyses, not results:

1. **Symmetry-selected angular structure:** derive which angular components are permitted by the material, geometry and source symmetries; compare field/mode content under circle and ellipse.
2. **Thermal-stress concentration and location:** use a declared principal-stress or other justified failure-related observable, rather than relying only on Cartesian-component peaks.
3. **Generalized-model discrimination:** determine whether timing, amplitude/phase or attenuation changes survive matched Fourier controls and numerical uncertainty.
4. **Mechanism isolation:** separate conductivity anisotropy, elastic anisotropy and anisotropic thermal expansion through meaningful mathematical controls. Artificial isotropizations must be labeled model controls, not different measured specimens.
5. **Limits, stability and robustness:** thermodynamic admissibility, time/spatial resolution, finite-pulse bandwidth, constitutive scaling, rotation covariance and parameter sensitivity.

If the non-Fourier effect is below a documented numerical/experimental resolution floor, report that limitation or null result. Do not tune relaxation parameters merely to create a visually strong effect.

## 7. Method and code boundary

The exact model order and geometry determine the method:

- Laplace-domain and angular/spectral formulations may be useful for reference/circular cases.
- FEM, finite-volume, spectral or boundary-based formulations may be used for the ellipse after inspecting the actual equations and natural conditions.
- An independent implementation/method for at least one key benchmark is preferable to checking the same algebra twice.

No method is selected yet. BFS is not mandatory. The existing FEM4 MATLAB package does not already solve transient thermal transport or curved-cavity geometry. Its program organization, material/configuration patterns, sparse block handling, scaling, exports and tests may be reused only after adaptation and rechecking.

No solver was implemented or run in this exploration. No production-compute estimate is claimed.

## 8. Novelty and evidence gates before development

The preliminary additional searches were:

- `"Ga2O3" "thermoelastic" "cavity"`
- `"generalized" "heat conduction" "elliptical cavity" anisotropic`

Their sparse/noisy results do NOT establish absence of prior work. Anisotropic generalized thermoelasticity and anisotropic heat transfer are established fields. A broader title/DOI/database and closest-paper comparison is required.

Before approving a final problem:

1. Obtain/read the exact 2025 heat-model equations and reconstruct their assumptions/limits.
2. Search the chosen model with monoclinic/orthorhombic materials, cavities, noncircular domains, angular modes and thermal-stress concentration; compare at least five closest papers, with additional coverage as needed.
3. Compare against the user's published and unpublished work, including GK identifiability and existing cavity/KG studies.
4. Build a source-backed material ledger: elasticity, thermal expansion, density, heat capacity, conductivity, dynamic coefficients and scope.
5. Define an evidence route: source-case reconstruction is verification; conductivity agreement alone is not physical validation of generalized transient thermoelasticity.
6. Set a scientific acceptance plan with admissibility, baseline, observables, errors/uncertainty and continue/revise/reject criteria before detailed development.

## 9. Current recommendation and next user decision

**Recommendation:** shortlist the 2025 generalized CV/GN family + monoclinic beta-Ga2O3 + circular/elliptical cavity symmetry-mismatch question for deeper investigation.

This is a recommended shortlist, not final scientific/journal approval. The user must approve the exact direction. If a specific Google Drive paper was intended as the base, supply its title/workbook Sr. No. or full PDF so this recommendation can be aligned with it.

**No new research results, verified novelty or Q1 guarantee are claimed.**
