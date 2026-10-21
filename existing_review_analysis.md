# Existing Review Analysis — Saturation Map

**Prepared:** 2026-10-21 · **Evidence cut-off:** 2026-10-21
**Evidence standard:** `VERIFIED` / `SNAPSHOT` / `INFERRED` / `HYPOTHESIS`

---

## 1. Method and its limits

I searched OpenAlex (title/abstract + `type:review`) and Crossref (exact bibliographic match) for
review articles across seven slices of the corpus. Full results are in
[`search_log/queries.csv`](search_log/queries.csv) and [`data/review_inventory.csv`](data/review_inventory.csv).

**Limits (stated plainly):**
- OpenAlex's `type:review` classification is incomplete and noisy — several items in the inventory
  have no DOI and no verified venue.
- Absence of a review in these searches is **absence of evidence in those databases**, not proof
  that no review exists anywhere.
- I did not execute a full-text systematic review; no PRISMA flow is claimed.

---

## 2. Verified review inventory

The table below is the complete set of review-type works located, grouped by relevance to the
corpus. Machine-readable copy: [`data/review_inventory.csv`](data/review_inventory.csv).

### 2.1 Directly relevant / foundational (verified)

| DOI | Title | Year | Journal | Citations | Role |
|---|---|---|---|---|---|
| 10.1115/1.3098984 | Hyperbolic Thermoelasticity: A Review of Recent Literature | 1998 | Applied Mechanics Reviews | 1284 | Landmark; defines second-sound thermoelasticity |
| 10.1115/1.3143705 | Thermoelasticity with Second Sound: A Review | 1986 | Applied Mechanics Reviews | 834 | Landmark; predecessor to 1998 review |
| 10.1080/014957399280832 | GENERALIZED THERMOELASTICITY | 1999 | Journal of Thermal Stresses | 602 | Crossref-verified review-length treatise |
| 10.1093/jcde/qwaa082 | Recent advances in generalized thermoelasticity theory and the modified models: a review | 2021 | J. Comput. Des. Eng. | 54 | Most recent generalized-thermoelasticity review; 146 references |

### 2.2 Adjacent but not on-target (verified)

| DOI | Title | Year | Journal | Citations | Why not on-target |
|---|---|---|---|---|---|
| null | A Review On Two-Temperature Theory Of Generalized Thermoelasticity | 2019 | No DOI/venue | 0 | Title-level match only; no verifiable record |
| null | Fractional order generalized thermoelasticity theories: A review | 2016 | No DOI/venue | 6 | Only fractional-thermoelasticity review; unverified venue |
| 10.22059/jcamech.2021.331410.653 | A review on stress-driven nonlocal elasticity theory | 2021 | J. Comput. Applied Mech. | 35 | Nonlocal elasticity only; no thermoelastic coupling |
| 10.12989/sem.2020.74.5.611 | A comprehensive review on the modeling of smart piezoelectric nanostructures | 2020 | Struct. Eng. Mech. | 21 | Nanostructure modelling; not interface waves |
| 10.1190/1.3474602 | Computational poroelasticity — A review | 2010 | Geophysics | 213 | Geophysical; not multiphysics interface waves |
| 10.1190/1.3463417 | Seismic wave attenuation ... wave-induced flow in porous rocks — A review | 2010 | Geophysics | 921 | Geophysical poroelasticity |

### 2.3 Negative searches — zero relevant reviews located

These searches returned works, but **none is on-target** for a review of wave reflection /
transmission at multiphysics interfaces:

| Search (OpenAlex, 2026-10-21) | Matching works | On-target reviews |
|---|---|---|
| `type:review` + `"piezo-thermoelastic"` | 0 | 0 |
| `title:"review"` + `"memory-dependent"` | 77 | 0 (none on thermoelastic wave interfaces) |
| `title:"review"` + `"fractional thermoelastic"` | 1 | 0 (the one match is unverified) |
| `title:"review"` + `piezoelectric` + `wave` | 163 | 0 (all energy-harvesting / SHM) |
| `title:"review"` + `"surface waves"` | 270 | 0 (all ocean / geophysical / metasurface) |
| `title:"review"` + `"reflection and transmission"` | 40 | 0 (none on elastic/piezoelectric interfaces) |
| `title:"review"` + `"poroelastic"` | 95 | 0 (all geotechnical / CO2 / seismic) |
| `title:"review"` + `flexoelectric` | 23 | 0 (all materials / applications) |
| `title:"review"` + `photothermal` + `semiconductor` | 30 | 0 (all biomedical / therapy) |

`VERIFIED` for counts; `INFERRED` for "none on-target" (based on title inspection of returned
results).

---

## 3. Saturation assessment by topic axis

| Axis | Saturation | Evidence | Gap |
|---|---|---|---|
| Generalized thermoelasticity (theories LS/GL/GN/DPL/TPL) | **High** | Chandrasekharaiah 1986 (834 cites), 1998 (1284); Shakeriaski 2021 (54) | Well covered; no gap |
| Memory-dependent derivatives / fractional thermoelasticity | **Low** | One unverified 2016 review (6 cites); no MDD review | Gap — but theory-only, not interface-focused |
| Nonlocal elasticity | **Medium** | Two reviews (35, 21 cites); neither thermoelastic-coupled | Partial gap |
| Poroelasticity / double porosity | **Medium** | Geophysical reviews exist; no solid-mechanics interface review | Gap |
| Piezoelectric / piezothermoelastic waves | **Low** | Zero reviews with piezo-thermoelastic in title/abstract | Significant gap |
| Reflection–transmission at multiphysics interfaces | **Low** | Zero reviews located | **Primary gap** |
| Energy ratios / energy flux at interfaces | **Low** | Zero reviews located; phrase "energy ratios" = 10,997 works globally (broad) | **Primary gap** |
| Surface waves in piezo-thermo-elastic media | **Low** | Zero reviews located | Gap |
| Semiconductor photo-thermo-elastic / plasma waves | **Low** | Zero reviews located | Gap |

`INFERRED` saturation ratings; based on located review counts, not on a full-text census.

---

## 4. Differentiation logic (why a new review is defensible)

A new review must not merely re-title an existing one. The differentiation is structural:

1. **Scope.** Existing reviews cover *theories* (Chandrasekharaiah; Shakeriaski) or *materials*
   (piezoelectric nanostructures; poroelasticity geophysics). None synthesizes *interface energy
   partitioning* across thermal lag × piezoelectricity × porosity × nonlocality × memory.
2. **Dependent variable.** Existing work computes reflection coefficients and (in the corpus)
   energy ratios case-by-case. No review derives or compares a *general energy-flux identity* for
   dissipative, memory-dependent, nonlocal multiphysics media.
3. **Population.** The corpus population (49 works, 2022–2026, dense co-authorship, recurring
   venues) is large enough to review but not so large that a synthesis is impossible.
4. **Timing.** The MDD/fractional/nonlocal wave-interface literature is still accumulating (peak
   2023–2025). A review now captures the field before it fragments further.

---

## 5. Gap statements (one per candidate topic)

These feed directly into [`five_candidate_topics.md`](five_candidate_topics.md).

| # | Gap | Verification basis |
|---|---|---|
| G1 | No review synthesizes energy-flux definitions and conservation across dissipative / nonlocal / multiphysics interfaces | Zero reviews located for "piezo-thermoelastic" + interface; "energy ratios" broad phrase only |
| G2 | No review systematically compares MDD vs fractional-order operators in generalized thermoelastic waves | One unverified 2016 fractional review; no MDD review |
| G3 | No review covers reflection–transmission at double-porosity / liquid-saturated interfaces | Poroelastic reviews are geophysical; solid-mechanics interface absent |
| G4 | No review covers nonlocal/size-dependent surface and interface waves in piezo-thermo-elastic media | Nonlocal reviews are beam/nanostructure focused |
| G5 | No review unites semiconductor carrier transport with thermo-elastic wave propagation | Photothermal-semiconductor reviews are biomedical |
