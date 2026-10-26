# Existing Review Saturation — Phase 1

**Prepared:** 2026-10-21  
**Status:** Partially completed (Phase 0 audit imported; broader search pending)  
**Evidence standard:** `VERIFIED` / `SNAPSHOT` / `INFERRED` / `UNCONFIRMED`

---

## 1. Phase 0 Review Inventory (Imported)

Complete set of review-type works located in OpenAlex/Crossref searches:

| DOI | Title | Year | Journal | Citations | Relevance |
|-----|-------|------|---------|-----------|-----------|
| 10.1115/1.3098984 | Hyperbolic Thermoelasticity: A Review of Recent Literature | 1998 | Applied Mechanics Reviews | 1284 | Foundational; bulk-medium focus |
| 10.1115/1.3143705 | Thermoelasticity with Second Sound: A Review | 1986 | Applied Mechanics Reviews | 834 | Foundational; bulk-medium focus |
| 10.1080/014957399280832 | GENERALIZED THERMOELASTICITY | 1999 | Journal of Thermal Stresses | 602 | Review-length treatise; bulk-medium focus |
| 10.1093/jcde/qwaa082 | Recent advances in generalized thermoelasticity theory and the modified models: a review | 2021 | J. Comput. Des. Eng. | 54 | Most recent; 146 references; bulk-medium focus |
| null | A Review On Two-Temperature Theory Of Generalized Thermoelasticity | 2019 | No DOI/venue | 0 | Unverified; no venue |
| null | Fractional order generalized thermoelasticity theories: A review | 2016 | No DOI/venue | 6 | Unverified; no venue |
| 10.22059/jcamech.2021.331410.653 | A review on stress-driven nonlocal elasticity theory | 2021 | J. Comput. Applied Mech. | 35 | Nonlocal only; no thermoelastic coupling |
| 10.12989/sem.2020.74.5.611 | A comprehensive review on the modeling of smart piezoelectric nanostructures | 2020 | Struct. Eng. Mech. | 21 | Nanostructures; not interface waves |
| 10.1190/1.3474602 | Computational poroelasticity — A review | 2010 | Geophysics | 213 | Geophysical; not multiphysics interfaces |
| 10.1190/1.3463417 | Seismic wave attenuation ... wave-induced flow in porous rocks — A review | 2010 | Geophysics | 921 | Geophysical poroelasticity |

**Zero on-target reviews located** for:
- piezo-thermoelastic + interface (OpenAlex count = 0)
- memory-dependent + thermoelastic interfaces (77 works, 0 on-target)
- fractional thermoelastic interfaces (1 work, unverified)
- piezoelectric + wave + interface (163 works, all energy-harvesting/SHM)
- surface waves + thermoelastic/piezoelectric interfaces (270 works, 0 on-target)
- reflection and transmission + elastic/piezoelectric interfaces (40 works, 0 on-target)
- poroelastic + double-porosity interface waves (95 works, all geotechnical)
- flexoelectric wave propagation (23 works, all materials/applications)
- photothermal + semiconductor wave physics (30 works, all biomedical/therapy)

---

## 2. Limitations of Phase 0 Saturation Analysis

| Limitation | Impact | Phase 1 mitigation |
|------------|--------|-------------------|
| OpenAlex `type:review` classification incomplete | Reviews may be missed | Search Scopus/WoS/Dimensions if accessible |
| Title/abstract keyword only | Reviews with different terminology missed | Family F alternative terminology searches |
| No backward/forward citation chasing | Review citing foundational works missed | Citation chasing from Chandrasekharaiah/Shakeriaski |
| No full-text reading | Review scope may be broader than title suggests | Full-text extraction where accessible |
| English only | Non-English reviews missed | Documented limitation |

---

## 3. Phase 1 Saturation Verification Plan

### 3.1 Family F searches (alternative terminology)

Execute OpenAlex searches for:
- "wave energy transport" + thermoelastic/piezoelectric/poroelastic
- "interface scattering" + thermoelastic/piezoelectric
- "energy transmission" + elastic wave
- "reflection coefficient" + thermoelastic interface
- "coupled-field energy balance" + interface
- "elastic wave energy" + interface
- "dissipative waves" + thermoelastic

### 3.2 Citation chasing

**Backward:** From Chandrasekharaiah 1986/1998 and Shakeriaski 2021, extract references to identify earlier interface/energy papers.

**Forward:** From Biot 1956, Lord & Shulman 1967, Eringen 1972, Quintanilla 2019, identify citing papers that may be reviews.

### 3.3 Scopus/Web of Science (if access becomes available)

Execute prepared search strings (documented in `02_search_strategy.md`) to confirm or refute the gap claim.

---

## 4. Saturation Assessment (Conservative)

| Topic area | Located reviews | On-target reviews | Saturation level | Confidence |
|------------|-----------------|-------------------|------------------|------------|
| Generalized thermoelasticity theory | 4 | 0 (bulk only) | HIGH | VERIFIED |
| Interface energy flux (multiphysics) | 0 | 0 | LOW | UNCONFIRMED |
| MDD/fractional thermoelastic waves | 1 (unverified) | 0 | LOW | PARTIAL |
| Nonlocal elasticity | 2 | 0 (thermoelastic-coupled) | MEDIUM | VERIFIED |
| Poroelasticity | 2 | 0 (solid-mechanics interface) | MEDIUM | VERIFIED |
| Piezoelectric waves | 0 | 0 | LOW | UNCONFIRMED |

**Key finding:** No review located that synthesizes energy-flux definitions and conservation across dissipative/nonlocal/multiphysics interfaces. This is the primary gap supporting Topic T1, but the claim is **UNCONFIRMED** pending broader database searches.

---

## 5. Differentiation from Existing Reviews

| Existing review | Scope | What T1 would add |
|----------------|-------|-------------------|
| Chandrasekharaiah 1986/1998 | Hyperbolic thermoelasticity theory | Interface energy flux; piezoelectric + porous media |
| Shakeriaski et al. 2021 | Generalized thermoelasticity + modified models | Conservation-law proof; multi-channel energy partitioning |
| Nonlocal elasticity reviews (2020, 2021) | Beam/nanostructure modelling | Interface reflection–transmission; energy flux |
| Piezoelectric nanostructure review (2020) | Smart materials modelling | Wave physics at interfaces; not device engineering |

**T1 is NOT a retitle:** It shifts from theory review (existing) to interface conservation law (new).
