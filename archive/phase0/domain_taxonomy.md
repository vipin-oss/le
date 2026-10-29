# Domain Taxonomy — Wave Propagation in Multiphysics Continua

**Prepared:** 2026-10-21 · **Evidence cut-off:** 2026-10-21
**Evidence standard:** `VERIFIED` / `SNAPSHOT` / `INFERRED` / `HYPOTHESIS`
**Scope discipline:** this taxonomy describes the researcher's verified programme. Peripheral papers
(bioremediation, mathematics education, bio-electrochemical systems) are excluded.

---

## 1. Top-level definition (five-axis taxonomy)

Each work in the corpus sits at an intersection of five independent axes. This five-dimensional
classification is the organising principle for the review topics in [`five_candidate_topics.md`](five_candidate_topics.md).

| Axis | Dimension | Levels (verified from corpus) |
|---|---|---|
| **A** | Thermal law (heat-conduction model) | Fourier (classical); Lord–Shulman (single-phase-lag, hyperbolic); Green–Lindsay (two-temperature / temperature-rate); Green–Naghdi II & III; dual-phase-lag (DPL); three-phase-lag (TPL); Moore–Gibson–Thompson (MGT); memory-dependent derivative (MDD); fractional-order |
| **B** | Coupling field | Purely elastic; thermoelastic; piezoelectric / piezothermoelastic; piezomagnetic / flexomagnetic; photo-thermo-piezo-elastic; photo-piezoelectric-semiconductor; magneto-thermo-elastic |
| **C** | Pore structure | Solid (no pores); voids (single porosity); double porosity; saturated with inviscid liquid; micropolar |
| **D** | Scale / size | Local (continuum); nonlocal (Eringen / strain gradient); size-dependent; microstructured; nanobeam / microplate; spherical/cylindrical cavity |
| **E** | Geometry / boundary | Half-space; interface between two half-spaces; free surface; layered waveguide; slab between two media; beam / plate / microplate; cylindrical tunnel / spherical cavity; parabolic interfacial discontinuity |

Every paper in the programme decomposes as an (A–E) tuple. For example:

- [`10.1007/s12648-022-02568-w`](https://doi.org/10.1007/s12648-022-02568-w): A=Lord–Shulman-type generalized thermoelasticity, B=piezothermoelastic, C=solid, D=local, E=interface between elastic and piezothermoelastic half-spaces → **energy analysis**
- [`10.1088/1402-4896/acfced`](https://doi.org/10.1088/1402-4896/acfced): A=thermoelastic, B=thermoelastic, C=double porosity, D=nonlocal, E=interface with fluid
- [`10.1108/hff-10-2023-0615`](https://doi.org/10.1108/hff-10-2023-0615): A=MGT memory-dependent, B=piezothermoelastic with voids, C=voids, D=nonlocal, E=Rayleigh surface wave

`INFERRED`: this tuple structure is my own classification; no source states it explicitly.

---

## 2. Field theory (historical development)

| Epoch | Landmark contribution | Verified source | Core idea |
|---|---|---|---|
| 1850s | Duhamel–Neumann / classical coupled thermoelasticity | [historical context] | Quasi-static thermal stress; infinite heat speed (parabolic Fourier law) |
| 1956 | Biot, *Thermoelasticity and Irreversible Thermodynamics*, J. Appl. Phys. 27, 240–253 | Crossref `10.1063/1.1722351`, VERIFIED | Coupled thermoelasticity via irreversible thermodynamics |
| 1967 | Lord & Shulman, *A generalized dynamical theory of thermoelasticity*, J. Mech. Phys. Solids 15, 299–309 | Crossref `10.1016/0022-5096(67)90024-5`, VERIFIED | First hyperbolic (single-relaxation-time) model — finite heat-wave speed |
| 1972 | Green & Lindsay, *Thermoelasticity*, J. Elasticity 2, 1–7 | Crossref `10.1007/bf00045689`, VERIFIED | Temperature-rate (two-temperature) theory |
| 1991 | Green & Naghdi, *A re-examination of the basic postulates of thermomechanics*, Proc. R. Soc. A 432, 171–194 | Crossref `10.1098/rspa.1991.0012`, VERIFIED | Types II & III: no energy dissipation; wave-type heat propagation |
| 1995 | Tzou, *A unified field approach for heat conduction from macro- to micro-scales*, J. Heat Transfer 117, 8–16 | Crossref `10.1115/1.2822329`, VERIFIED | Dual-phase-lag model |
| 2007 | Roy Choudhuri, *On a thermoelastic three-phase-lag model*, J. Thermal Stresses 30, 231–238 | Crossref `10.1080/01495730601130919`, VERIFIED | Three-phase-lag extension |
| 2011 | *Concept of the memory-dependent derivative*, Comp. Appl. Math. (verified citation count 459) | OpenAlex `10.1016/j.camwa.2011.04.028`, VERIFIED | MDD operator generalizes fractional derivatives |
| 2014 | *Generalized thermoelasticity model based on memory-dependent derivative*, Int. J. Eng. Sci. (295 citations) | OpenAlex `10.1016/j.ijengsci.2014.04.014`, VERIFIED | MDD introduced into thermoelasticity |
| 2019 | Quintanilla, *Moore–Gibson–Thompson thermoelasticity*, Math. Mech. Solids (409 citations) | Crossref `10.1177/1081286519862007`, VERIFIED (abstract + cited-by count) | Third-order-in-time hyperbolic thermoelasticity; MGT equation |

The corpus inherits this lineage: every paper in the researcher's set uses at least one of LS,
GL, GN, DPL, TPL, MGT, MDD, or fractional operators. This is `VERIFIED` at the title/abstract level
and `INFERRED` as a family-level claim.

---

## 3. Governing equations (mathematical depth)

The corpus uses a consistent linearized continuum-mechanics formalism. The equations below represent
the *shape* of the model family, not any single paper's exact system.

### 3.1 Elasticity (balance of linear momentum)

```
ρ ü_i = σ_ji,j + ρ f_i
```

For anisotropic media: `σ_ij = c_ijkl ε_kl − β_ij (T − T0) − e_kij E_k − ...`
- `c_ijkl`: elastic stiffness
- `β_ij`: thermal-stress coefficient
- `e_kij`: piezoelectric coefficient
- `E_k`: electric field

### 3.2 Heat conduction (the variable axis)

| Model | Equation (schematic) | Verified source |
|---|---|---|
| Fourier | `q_i = −k T_,i` | Classical; basis of all papers |
| Lord–Shulman | `q_i + τ q_i˙ = −k T_,i` | [`10.1016/0022-5096(67)90024-5`](https://doi.org/10.1016/0022-5096(67)90024-5), VERIFIED |
| Green–Lindsay | Two temperatures; `q_i + ...` coupled to `T˙` | [`10.1007/bf00045689`](https://doi.org/10.1007/bf00045689), VERIFIED |
| Green–Naghdi II/III | No dissipation; `τ₀² T¨ + τ₁ T˙ + ...` | [`10.1098/rspa.1991.0012`](https://doi.org/10.1098/rspa.1991.0012), VERIFIED |
| Dual-phase-lag | `q_i(t+τ_q) = −k T_,i(t+τ_T)` | [`10.1115/1.2822329`](https://doi.org/10.1115/1.2822329), VERIFIED |
| Three-phase-lag | Adds phase-lag of temperature gradient | [`10.1080/01495730601130919`](https://doi.org/10.1080/01495730601130919), VERIFIED |
| Moore–Gibson–Thompson | `τ q¨ + q˙ = −k ∇²T − ...` | [`10.1177/1081286519862007`](https://doi.org/10.1177/1081286519862007), VERIFIED |

### 3.3 Electric field (piezoelectric coupling)

```
D_i = e_ijk ε_jk + κ_ij E_j,   E_i = −φ_,i,   D_i,i = 0 (no free charge)
```
`κ_ij`: dielectric permittivity; `φ`: electric potential.

### 3.4 Porosity / voids

- Single porosity (voids): volume fraction `φ` with its own balance equation (Cowin & Nunziato,
  [`10.1007/bf00249363`](https://doi.org/10.1007/bf00249363), VERIFIED)
- Double porosity: two interacting pore networks (no double source in Crossref for the exact
  foundational double-porosity paper; the corpus title `10.1007/s00419-023-02364-w` invokes it).

### 3.5 Nonlocal elasticity

```
σ_ij(x) − (e₀a)² ∇²σ_ij(x) = C_ijkl ε_kl(x)
```
`e₀a`: nonlocal length scale. Eringen [`10.1016/0020-7225(72)90050-x`](https://doi.org/10.1016/0020-7225(72)90050-x), VERIFIED.

### 3.6 Memory-dependent derivative

```
D^α_MDD f(t) = ∫_{0}^{t} M(ξ) f^(α)(t−ξ) dξ
```
Kernel `M` (memory kernel). [`10.1016/j.camwa.2011.04.028`](https://doi.org/10.1016/j.camwa.2011.04.028), VERIFIED.

`INFERRED`: the mathematical difficulty in this family is that the dispersion relation is generally
a high-degree polynomial in complex slowness, so closed-form interface solutions are possible only
for simplified geometries (half-space, free surface, two-media interface). Layered or irregular
geometries require numerical root-finding or transform methods.

---

## 4. Major methodological families

| Family | What it does | Strength | Limitation |
|---|---|---|---|
| Harmonic plane-wave ansatz + Christoffel-type secular equation | Dispersion, mode speeds, attenuation | Closed form; physical transparency | Homogeneous, infinite domains only |
| Displacement potentials / state-vector reduction | Decouples coupled field equations | Handles anisotropy and coupling | Algebraic complexity grows with fields |
| Interface conditions (continuity of displacement/traction/temperature/flux/potential) | Reflection–transmission coefficients | Direct link to measurable energy ratios | Perfect bonding assumed; imperfect bond needs extra parameters |
| Energy-ratio computation from stress/flux fields | Partitioning of incident energy | Connects to conservation | No shared definition across dissipative/nonlocal media |
| Parametric sweeps (frequency × angle × memory × fractional order × porosity × nonlocal length) | Sensitivity maps | Empirical model discrimination | Computationally repetitive; no analytical synthesis |
| Limiting-case checks (Fourier limit, no-coupling limit, static limit) | Model validation | Guards against algebra errors | Does not validate against experiment |

`INFERRED` from corpus structure; no source states this as a "methodology family" list.

---

## 5. Competing scientific perspectives

| Debate | Position A | Position B | Corpus status |
|---|---|---|---|
| Heat-wave speed | Fourier: infinite speed (parabolic) | Generalized theories: finite speed (hyperbolic) | Corpus firmly on side B |
| Dissipation | GN II/III: no energy dissipation | LS/DPL/MGT: dissipative | Both used; corpus explores both |
| MDD vs fractional | MDD: kernel-based, flexible memory | Fractional: power-law memory, non-local in time | Both used; often presented as alternatives |
| Nonlocal | Stress-based (Eringen) | Strain-gradient / couple-stress | Mixed usage |
| Energy at interface | Local flux `q·n + σ·u˙ + D·E˙` | Nonlocal/integral flux required | **Unresolved** — papers compute ratios but do not agree on the flux functional |

The energy-flux definition is the **live theoretical debate** in this corner of the field. This is
the `INFERRED` central opportunity for a synthesis review.

---

## 6. Research maturity

| Dimension | Assessment | Basis |
|---|---|---|
| Theory | Mature (classical); emerging (fractional, MGT, nonlocal-coupled) | 1956–2019 lineage is established; 2020–2026 corpus applies it |
| Experiment | Weak to absent | Corpus is analytical/computational; no experimental paper identified in the 49-record set |
| Numerical | Moderate | Some finite-element / transform work, but dominated by closed-form secular equations |
| Review saturation | Low for the specific intersection | No verified review covers "energy ratios at multiphysics interfaces with memory/fractional/nonlocal effects" (see [`existing_review_analysis.md`](existing_review_analysis.md)) |
| Community | Small, coherent | ~49 works in 5 years, dense co-authorship, recurring venues |

`INFERRED`: The field is **mature in its constituent theories but immature in their synthesis**.
This is the classic condition for a high-value review: enough primary work to ground it, enough
disagreement to motivate it, and no existing authoritative synthesis.

---

## 7. How this taxonomy supports the five candidate topics

Each candidate topic in [`five_candidate_topics.md`](five_candidate_topics.md) is defined as a
slice of this five-axis space:

| Topic | Axes emphasised | Gap targeted |
|---|---|---|
| T1: Energy-flux partitioning at multiphysics interfaces | A, B, E (all) | No shared flux definition/conservation statement |
| T2: Memory & fractional operators in generalized thermoelastic waves | A | MDD vs fractional never systematically compared |
| T3: Reflection & transmission at double-porosity interfaces | B, C, E | Double-porosity interfaces underexplored vs single |
| T4: Nonlocal/size-dependent surface waves in piezo-thermo-elastic media | D, B | Size effects reviewed for beams, not for surface/interface waves |
| T5: Semiconductor photo-thermo-elastic & plasma waves | B | Carrier transport + waves never reviewed together |
