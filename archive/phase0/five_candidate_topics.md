# Five Candidate Review Topics

**Prepared:** 2026-10-21 · **Evidence cut-off:** 2026-10-21
**Evidence standard:** `VERIFIED` / `SNAPSHOT` / `INFERRED` / `HYPOTHESIS`

Each topic includes the 13 required elements. Saturation claims are based on the searches recorded in
[`search_log/queries.csv`](search_log/queries.csv) — they describe what was located in OpenAlex /
Crossref, not proof that nothing exists elsewhere.

---

## Topic T1 — Energy-flux partitioning at multiphysics interfaces (RECOMMENDED)

### Precise proposed title
**"Energy flux and energy-ratio partitioning at interfaces of generalized thermoelastic, piezoelectric and poroelastic media: a unified review of definitions, conservation laws and wave-mode coupling"**

### Scope and boundaries
- **In scope:** reflection–transmission and energy-ratio analysis at interfaces between two
  half-spaces or at a free surface, where at least one medium is generalized thermoelastic,
  piezoelectric/piezothermoelastic, piezomagnetic, or porous (voids, single/double porosity,
  liquid-saturated). Heat-conduction models: Lord–Shulman, Green–Lindsay, Green–Naghdi II/III,
  dual-phase-lag, three-phase-lag, Moore–Gibson–Thompson, memory-dependent derivative, fractional.
  Wave types: P, SV, SH, Rayleigh, quasi-plane, plasma, thermal. Interface conditions: perfect and
  imperfect (spring-type) bonding.
- **Out of scope:** bulk wave propagation in a single homogeneous medium without an interface;
  energy harvesting / device engineering; geophysical poroelasticity; nanobeam / microplate
  vibration without interface conditions; experimental NDE.

### Central scientific research questions
1. What is the correct energy-flux functional for a dissipative, memory-dependent, nonlocal
   multiphysics medium at an interface — and how do thermal, electrical, mechanical and pore-fluid
   channels contribute?
2. Do the published "energy ratios" sum to unity across all cases, or only under restrictive
   assumptions (local, elastic, perfect bonding)?
3. How do memory kernels, fractional orders, nonlocal length scales, and porosity each shift the
   partitioning among reflected and transmitted modes?
4. What interface conditions (imperfect bonding, interfacial discontinuity, surface irregularity)
   make energy conservation fail, and where does the missing energy go (interface storage vs
   dissipation)?

### Foundational theoretical concepts
- Balance of linear momentum, energy, charge, and mass in linearized continua
- Christoffel-type secular equation from harmonic plane-wave ansatz
- Heat-conduction hierarchy: Fourier → LS → GL → GN II/III → DPL → TPL → MGT → MDD → fractional
- Piezoelectric coupling: `D = e·ε + κ·E`; piezomagnetic/flexomagnetic analogues
- Porosity: Cowin–Nunziato void theory; double-porosity interaction
- Nonlocal elasticity: Eringen stress-based and strain-gradient forms
- Memory-dependent derivative: convolution kernel operator

### Mathematical depth
`HIGH`. The review would carry explicit governing equations, dispersion determinants, amplitude
matrices, interface condition matrices, and energy identities. Target reader: continuum mechanics
researcher comfortable with complex slowness and tensorial notation. Equations are the deliverable,
not optional illustration.

### Existing review saturation
`LOW` (verified absence in searched databases).
- Zero reviews located with "piezo-thermoelastic" + interface in title/abstract (OpenAlex,
  `type:review` filter, count = 0).
- Zero reviews on energy ratios at multiphysics interfaces; the phrase "energy returns" 10,997
  works globally but none specific to this setting (OpenAlex, 2026-10-21).
- Chandrasekharaiah 1986/1998 and Shakeriaski 2021 review *theories*, not interfaces or energy
  partitioning.
`INFERRED`: saturation is low because every located review stops at the bulk-medium level.

### Specific differentiation from published reviews
| Published review | What it covers | What T1 adds |
|---|---|---|
| Chandrasekharaiah 1986 / 1998 | Hyperbolic thermoelasticity theory | Energy-flux definition at *interfaces*; piezoelectric + porous media |
| Shakeriaski et al. 2021 | Generalized thermoelasticity + modified models | Conservation-law proof; multi-channel energy partitioning |
| Nonlocal elasticity reviews (2020, 2021) | Beam / nanostructure modelling | Interface reflection–transmission, not bulk vibration |
| Piezoelectric nanostructure review (2020) | Smart materials modelling | Wave physics, not device engineering |

### Potential for an original scientific taxonomy
`HIGH`. Original 4-way taxonomy of interface energy partitioning:
- **E1** Mechanical-to-mechanical (elastic ↔ elastic)
- **E2** Mechanical-to-thermal (elastic ↔ thermoelastic)
- **E3** Electro-mechanical (piezoelectric ↔ elastic / piezo ↔ piezo)
- **E4** Poro-fluid (double-porosity ↔ liquid-saturated)
Crossed with dissipation class (conservative GN II/III vs dissipative LS/DPL/MGT/MDD) and bonding
class (perfect vs imperfect). Each cell gets a defining energy identity and a conservation check.

### Opportunities for original diagrams and synthesis
- Figure: energy-flow Sankey at a two-medium interface (incident → reflected P/SV/thermal +
  transmitted modes)
- Figure: decision tree selecting the correct flux functional by (dissipation × coupling ×
  nonlocality × bonding)
- Figure: heat map of energy-ratio deviation from unity across parameter space
- Table: conservation audit of the ~7 corpus energy-ratio papers (do ratios sum to 1?)
- Table: interface-condition catalogue (perfect / spring-type / irregular / discontinuous)

### Availability of primary literature
`HIGH`. The researcher's own corpus provides ≥7 energy-ratio papers (verified titles), plus a broad
primary field (686 works matching reflection + thermoelastic; 1,036 nonlocal + thermoelastic;
121 double-porosity + thermoelastic — OpenAlex counts, 2026-10-21). Primary literature is ample
and accessible via DOI.

### Major unresolved problems
1. No consensus on energy flux in nonlocal media (divergence theorem needs nonlocal flux).
2. No consensus on energy flux with hyperbolic heat conduction (thermal flux is not `q·n` alone).
3. No unified treatment of imperfect bonding energy storage/dissipation.
4. Fractional/MDD energy: convolution kernels make "instantaneous" flux ill-defined.

### Suitable high-ranking journals (scope verified where pages retrieved)

| Journal | Publisher | Scope fit | Verification status | Notes |
|---|---|---|---|---|
| Applied Mechanics Reviews | ASME | "Review Articles that reflect upon active areas of research… organize, summarize, and clarify knowledge"; solid mechanics, heat transfer | `VERIFIED` (ASME page retrieved) | Top-tier mechanics review journal; h-index 206 (OpenAlex) |
| Continuum Mechanics and Thermodynamics | Springer | "invited review articles"; continuum + thermodynamic closure; micro/macro bridging | `VERIFIED` (Springer page retrieved) | JIF 3.0 (2025); hybrid; natural fit for thermodynamic flux |
| International Journal of Numerical Methods for Heat & Fluid Flow | Emerald | Numerical heat/fluid flow; corpus's modal venue | `PARTIAL` (page retrieved; review policy not confirmed) | h-index 89; corpus home venue |
| Journal of Thermal Stresses | Taylor & Francis | Thermal-stress specialty | `PARTIAL` | h-index 86; several corpus papers |
| Mathematics and Mechanics of Solids | SAGE | Continuum mechanics; Quintanilla MGT paper published here | `PARTIAL` | h-index unknown in this session |
| European Journal of Mechanics — A/Solids | Elsevier | Solid mechanics | `PARTIAL` | h-index 124 |

`PARTIAL` = publisher page retrieved but explicit review-scope statement not confirmed. Scope
statements quoted only where the page was actually retrieved.

### Long-term scientific relevance
`HIGH`. Energy conservation at interfaces is a foundational, time-independent problem in continuum
mechanics. As generalized theories (fractional, nonlocal, MGT) become standard, a unified flux
framework becomes more necessary, not less.

### Realistic limitations and risks
- **Self-referentiality risk:** The researcher's own series dominates the energy-ratio literature.
  Mitigation: build on independently sampled corpus; treat own work as one contribution.
- **Definition risk:** If no consensus flux exists, the review may conclude with a *proposal* rather
  than a *settled* answer — acceptable for a theory review, but must be framed honestly.
- **Mathematical barrier:** High equation density limits readership; mitigated by targeting
  mechanics-thermodynamics venues.
- **Verification risk:** Absence of located reviews is not proof of nonexistence; must be
  phrase-checked against Scopus/Web of Science in Phase 1.

---

## Topic T2 — Memory-dependent and fractional operators in generalized thermoelastic waves

### Precise proposed title
**"Memory-dependent derivatives versus fractional-order operators in generalized thermoelastic wave propagation: a comparative review of models, dispersion and interface response"**

### Scope and boundaries
- **In scope:** MDD and fractional calculus applied to thermoelasticity (LS, GL, GN, DPL, TPL, MGT
  bases); wave dispersion, attenuation, reflection; semiconductor and piezoelectric media.
- **Out of scope:** fractional control theory, fractional viscoelasticity without thermal coupling,
  fractional diffusion without waves.

### Central scientific research questions
1. Do MDD and fractional operators produce distinguishable dispersion signatures, or are they
   reparameterizations of the same memory physics?
2. How do kernel choice (MDD) vs power-law (fractional) affect attenuation vs phase velocity?
3. What are the well-posedness and stability limits of each operator in wave problems?

### Foundational theoretical concepts
- Memory-dependent derivative: convolution with kernel M(ξ) [`10.1016/j.camwa.2011.04.028`, 459 cites]
- Fractional derivative: Caputo, Riemann–Liouville, Atangana–Baleanu
- Non-Fourier heat conduction; relaxation time
- Dispersion and attenuation in complex slowness plane

### Mathematical depth
`MEDIUM-HIGH`. Integral operators, Laplace/Fourier transforms, stability analysis. Less tensorial
than T1; more functional-analysis.

### Existing review saturation
`LOW`. One unverified 2016 fractional-thermoelasticity review (6 citations); zero MDD reviews.
`INFERRED`: gap is real but the topic is theory-heavy with limited interface content.

### Specific differentiation from published reviews
Existing fractional reviews (where located) cover *applications* (EV energy storage, avian flu) or
*control*, not thermoelastic wave physics. T2 would be the first mechanics-focused MDD-vs-fractional
comparison.

### Potential for an original scientific taxonomy
`MEDIUM`. Taxonomy by operator class (MDD kernel families vs fractional derivative types) × base
theory (LS/GL/GN/DPL/TPL/MGT) × wave type.

### Opportunities for original diagrams and synthesis
- Dispersion curves: MDD vs fractional vs integer-order, overlaid
- Attenuation coefficient maps vs frequency and order
- Table: well-posedness conditions per operator

### Availability of primary literature
`HIGH`. 373 works match "memory-dependent derivative" in title/abstract (OpenAlex, 2026-10-21);
foundation papers 2011 (459 cites) and 2014 (295 cites) verified.

### Major unresolved problems
1. MDD vs fractional equivalence is unproven for wave problems.
2. Stability boundaries for higher-order MDD in coupled media are unmapped.

### Suitable high-ranking journals
Mechanics of Advanced Materials and Structures (h82, T&F), Journal of Thermal Stresses (h86,
T&F), Continuum Mechanics and Thermodynamics (JIF 3.0, Springer).

### Long-term scientific relevance
`MEDIUM-HIGH`. Memory/fractional modelling is active but the wave-specific literature is younger
than classical thermoelasticity; relevance depends on whether MDD becomes standard.

### Realistic limitations and risks
- **Narrow audience:** more mathematical than T1; smaller readership.
- **Overlap risk:** foundation papers (2011, 2014) are not by the researcher; less author
  credibility advantage than T1.

---

## Topic T3 — Reflection and transmission at double-porosity and liquid-saturated interfaces

### Precise proposed title
**"Reflection, transmission and energy partitioning at double-porosity and liquid-saturated thermoelastic interfaces: a review of wave-mode coupling and pore-fluid effects"**

### Scope and boundaries
- **In scope:** single vs double porosity, voids, inviscid liquid saturation; P/SV/thermal/2nd
  sound modes at interfaces; rotation and initial stress where combined with porosity.
- **Out of scope:** geophysical reservoir poroelasticity; shale gas transport; CO2 sequestration.

### Central scientific research questions
1. How many additional wave modes does double porosity introduce, and how do they partition at an
   interface?
2. How does pore-fluid (inviscid liquid) coupling change reflection coefficients vs dry voids?
3. How do rotation, initial stress, and memory modify double-porosity interface response?

### Foundational theoretical concepts
- Cowin–Nunziato elastic materials with voids [`10.1007/bf00249363`, 790 cites]
- Double-porosity interaction; Biot-style fluid coupling
- Interface conditions with pore pressure and fluid flux

### Mathematical depth
`MEDIUM`. Additional field variable (porosity volume fraction) → larger secular determinant;
interface conditions include pore variables.

### Existing review saturation
`MEDIUM`. Poroelastic reviews exist (geophysical, 213–921 cites) but none on solid-mechanics
double-porosity interface waves. `INFERRED`: gap in the mechanics sub-domain.

### Specific differentiation from published reviews
Geophysical poroelasticity reviews (2010, 213/921 cites) cover reservoir flow, not wave reflection
at solid interfaces. T3 would be mechanics-specific.

### Potential for an original scientific taxonomy
`MEDIUM`. Taxonomy by porosity class (void / single / double / liquid-saturated) × coupling
(thermo / piezo / none) × interface (perfect / imperfect).

### Opportunities for original diagrams and synthesis
- Mode-conversion diagram at double-porosity interface
- Porosity-parameter sensitivity maps
- Table: double-porosity vs single-porosity interface conditions

### Availability of primary literature
`MEDIUM-HIGH`. 121 works match "double porosity" + thermoelastic (OpenAlex, 2026-10-21); corpus has
≥5 double-porosity papers.

### Major unresolved problems
1. Double-porosity interface conditions not standardized.
2. Liquid-saturated interface energy partitioning unstudied.

### Suitable high-ranking journals
Journal of Thermal Stresses (h86), Mechanics of Advanced Materials and Structures (h82), European
Journal of Mechanics—A/Solids (h124).

### Long-term scientific relevance
`MEDIUM`. Relevant to geomechanics and poroelastic devices, but narrower than T1.

### Realistic limitations and risks
- **Domain boundary:** risk of drifting into geophysics where reviews already exist.
- **Smaller corpus** than T1 (121 vs 686+ works).

---

## Topic T4 — Nonlocal and size-dependent surface waves in piezo-thermo-elastic media

### Precise proposed title
**"Nonlocal and size-dependent surface and interface waves in piezoelectric, piezomagnetic and flexoelectric media: a review of scale effects, dispersion and surface-mode localization"**

### Scope and boundaries
- **In scope:** Eringen nonlocal, strain-gradient, couple-stress; size-dependent Rayleigh / surface /
  interface waves; piezoelectric, piezomagnetic, flexoelectric coupling; micro/nanobeams and
  microplates where surface waves are the focus.
- **Out of scope:** bulk nonlocal elasticity without waves; beam/plate vibration without surface
  wave content; energy-harvesting devices.

### Central scientific research questions
1. How does the nonlocal length scale shift surface-wave speed and attenuation vs local theory?
2. How do piezoelectric/flexoelectric surface charges modify nonlocal dispersion?
3. At what length scale do nonlocal effects dominate over classical size effects?

### Foundational theoretical concepts
- Eringen nonlocal elasticity [`10.1016/0020-7225(72)90050-x`, 1272 cites]
- Strain-gradient / couple-stress elasticity
- Surface-wave (Rayleigh, Love, Stoneley) secular equations
- Flexoelectricity: polarization gradient coupling

### Mathematical depth
`MEDIUM-HIGH`. Nonlocal operators → integro-differential equations; surface-wave determinants.

### Existing review saturation
`MEDIUM`. Nonlocal elasticity reviews exist (2021, 35 cites; nanostructures 2020, 21 cites) but none
on surface/interface waves in piezo-thermo-elastic media. `INFERRED`: partial gap.

### Specific differentiation from published reviews
Existing nonlocal reviews cover beams/nanostructures; T4 would focus on *surface and interface
waves* with *piezoelectric coupling*.

### Potential for an original scientific taxonomy
`MEDIUM`. Taxonomy by nonlocal model × coupling type × wave type × dimensionality.

### Opportunities for original diagrams and synthesis
- Dispersion: local vs nonlocal surface waves, multiple length scales
- Surface-mode localization depth vs nonlocal parameter
- Table: nonlocal model comparison for surface waves

### Availability of primary literature
`HIGH`. 1,036 works match nonlocal + thermoelastic (OpenAlex, 2026-10-21); corpus has ≥5 nonlocal
papers.

### Major unresolved problems
1. Stress-based vs strain-gradient nonlocal: which is appropriate for surface waves?
2. Flexoelectric surface-wave coupling is weakly modelled.

### Suitable high-ranking journals
Mechanics of Advanced Materials and Structures (h82), European Journal of Mechanics—A/Solids (h124),
Continuum Mechanics and Thermodynamics (JIF 3.0).

### Long-term scientific relevance
`MEDIUM-HIGH`. Nonlocal/size effects are growing with nano-device design, but surface-wave niche is
smaller than interface energy.

### Realistic limitations and risks
- **Review competition:** nonlocal elasticity already has reviews; differentiation must be sharp
  (surface + piezo + thermo).
- **Narrower than T1.**

---

## Topic T5 — Semiconductor photo-thermo-elastic and plasma waves

### Precise proposed title
**"Photo-thermo-elastic and plasma wave propagation in semiconductor media under memory-dependent and nonlocal theories: a review of carrier–lattice–field coupling"**

### Scope and boundaries
- **In scope:** semiconductor photo-thermo-elasticity; quasi-plasma waves; carrier density and
  temperature fields; two-temperature models; memory-dependent and fractional heat flux; nonlocal
  effects.
- **Out of scope:** photothermal therapy, biomedical nanomaterials, photovoltaic devices.

### Central scientific research questions
1. How do carrier density waves couple to elastic and thermal waves in semiconductors?
2. How do memory-dependent and two-temperature models alter plasma-wave dispersion?
3. What is the role of nonlocality in semiconductor surface/interface wave modes?

### Foundational theoretical concepts
- Semiconductor equations: carrier continuity, energy, Poisson
- Photo-thermo-elastic coupling: deformation potential, photo-generated carriers
- Quasi-plasma wave modes
- Two-temperature model (electron/lattice temperatures)

### Mathematical depth
`MEDIUM-HIGH`. Coupled carrier–lattice–thermal system; larger state vector; complex dispersion.

### Existing review saturation
`LOW`. Photothermal-semiconductor reviews are biomedical (30 works, none on wave physics).
`INFERRED`: essentially no mechanics-review competition.

### Specific differentiation from published reviews
All located photothermal-semiconductor reviews are biomedical/therapy. T5 would be the first
wave-mechanics review of semiconductor photo-thermo-elasticity.

### Potential for an original scientific taxonomy
`MEDIUM`. Taxonomy by semiconductor model (single/double temperature) × coupling (photo / piezo /
none) × memory model × wave type.

### Opportunities for original diagrams and synthesis
- Carrier–lattice–thermal wave coupling diagram
- Dispersion: plasma wave vs thermoelastic wave in semiconductor
- Table: semiconductor vs elastic medium parameter comparison

### Availability of primary literature
`MEDIUM`. 620 works match elastic + photothermal (OpenAlex, 2026-10-21); corpus has ≥4
photo-thermo-piezo papers. Smaller than T1/T4.

### Major unresolved problems
1. Carrier–lattice two-temperature coupling at interfaces is under-modelled.
2. Plasma-wave / elastic-wave conversion at semiconductor boundaries.

### Suitable high-ranking journals
International Journal of Numerical Methods for Heat & Fluid Flow (h89, corpus venue),
Waves in Random and Complex Media (T&F), Continuum Mechanics and Thermodynamics (JIF 3.0).

### Long-term scientific relevance
`MEDIUM`. Semiconductor thermal management and photothermal sensing are applied growth areas, but
the pure wave-mechanics sub-topic is niche.

### Realistic limitations and risks
- **Smallest primary corpus** of the five topics.
- **Applied drift risk:** easy to slide into photothermal device literature where reviews exist.

---

## Summary table

| Topic | Core gap | Saturation | Mathematical depth | Primary lit. | Author-fit |
|---|---|---|---|---|---|
| T1 Energy-flux at interfaces | No unified flux/conservation | LOW | HIGH | HIGH | HIGH |
| T2 MDD vs fractional operators | No mechanics comparison | LOW | MED-HIGH | HIGH | MED |
| T3 Double-porosity interfaces | No mechanics interface review | MED | MED | MED-HIGH | MED-HIGH |
| T4 Nonlocal surface waves | Surface+piezo not reviewed | MED | MED-HIGH | HIGH | MED |
| T5 Semiconductor plasma waves | No mechanics review | LOW | MED-HIGH | MED | MED |
