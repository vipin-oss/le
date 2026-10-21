# Registered Protocol Draft — Phase 1

**Prepared:** 2026-10-21  
**Status:** Milestone B — Review protocol (Completed as draft; NOT preregistered)  
**Protocol ID:** LE-PHASE1-2026-10-21-T1  
**Preregistration status:** NOT preregistered. This is a registration-ready draft only.

---

## 1. Review Questions

**Primary question:**  
How is energy flux defined, partitioned, reflected, transmitted, dissipated, and conserved across
interfaces in coupled multiphysics continuum systems, and can a unified energy-flux formulation be
mathematically established across classical, generalized, nonlocal, fractional, and memory-dependent
theories?

**Sub-questions (RQ1–RQ8):**

| ID | Question |
|----|----------|
| RQ1 | How are energy density, energy flux, mechanical power, thermal transport, and other coupled energy-transfer mechanisms defined in different continuum theories? |
| RQ2 | Under which assumptions can different theoretical energy balances be expressed in a common mathematical framework? |
| RQ3 | How do mechanical, thermal, electric, carrier-diffusion, and porosity-related couplings influence reflected and transmitted wave modes? |
| RQ4 | How do classical, generalized, nonlocal, fractional, and memory-dependent theories differ in their definitions of physically admissible energy transport? |
| RQ5 | How should reflection and transmission coefficients be formulated when wave amplitudes, impedance relations, and propagation constants are complex? |
| RQ6 | What mathematical conditions ensure passivity, thermodynamic admissibility, interface conservation, or appropriate accounting of dissipative losses? |
| RQ7 | Which theoretical results are genuinely comparable across published studies, and which rely on incompatible assumptions, boundary conditions, or normalization procedures? |
| RQ8 | Which unresolved problems could justify new theoretical formulations, numerical benchmarks, or experimental investigations? |

---

## 2. Scope and Boundaries

### 2.1 In scope

- **Physical systems:** Interfaces between two half-spaces, free surfaces, layered waveguides,
  slabs between two media, cylindrical/spherical interfaces in multiphysics continua.
- **Continuum types:** Generalized thermoelastic, piezoelectric/piezothermoelastic, piezomagnetic,
  flexomagnetic, elastic with voids, double-porosity, liquid-saturated porous, semiconductor
  photo-thermo-elastic.
- **Heat-conduction models:** Fourier (classical), Lord–Shulman, Green–Lindsay, Green–Naghdi II/III,
  dual-phase-lag, three-phase-lag, Moore–Gibson–Thompson, memory-dependent derivative, fractional-order.
- **Wave types:** P, SV, SH, Rayleigh, Love, Stoneley, quasi-plane, thermal, plasma.
- **Interface conditions:** Perfect bonding, imperfect (spring-type) bonding, interfacial discontinuity,
  surface irregularity.
- **Dependent variables of interest:** Energy density, energy flux, reflection coefficients,
  transmission coefficients, energy ratios, absorption/loss fractions, dispersion relations,
  attenuation coefficients.

### 2.2 Out of scope

- Bulk wave propagation in a single homogeneous medium without an interface
- Energy harvesting / device engineering / transducer design
- Geophysical reservoir poroelasticity (fluid flow in porous rock)
- Nanobeam / microplate vibration without interface conditions
- Experimental nondestructive evaluation (NDE) as primary subject
- Photothermal therapy / biomedical nanomaterials / photovoltaic devices
- Fractional control theory without thermal-mechanical coupling

### 2.3 Publication period

- **Coverage:** 1956–2026 (from Biot's foundational thermoelasticity paper to present)
- **Rationale:** 1956 marks the beginning of modern coupled thermoelasticity. The corpus of interest
  accelerates from 2022–2026 but foundational theories span 1956–2019.

### 2.4 Language

- English only. Non-English papers excluded (documented as a limitation).

### 2.5 Document type

- Peer-reviewed journal articles, review articles, and conference proceedings with DOI
- Preprints included if they have a DOI and are cited by peer-reviewed work
- Books and book chapters excluded (not systematically searchable)

---

## 3. Eligibility Criteria

### 3.1 Inclusion criteria (all must be met)

1. The paper addresses wave propagation, reflection, transmission, or energy partitioning at an
   interface in a continuum mechanics setting.
2. The paper involves at least one generalized or classical thermoelastic, piezoelectric,
   poroelastic, or multiphysics coupling.
3. The paper presents analytical governing equations, interface conditions, or energy-balance
   formulations (not purely experimental or purely computational without theory).
4. The paper is peer-reviewed or a DOI-registered preprint cited by peer-reviewed work.

### 3.2 Exclusion criteria (any one is sufficient)

1. No interface or boundary condition analysis (bulk-only propagation).
2. Purely geophysical reservoir engineering (fluid flow, CO2 sequestration, shale gas).
3. Purely device/energy-harvesting engineering without wave physics.
4. No energy-related quantity (energy density, flux, ratio, coefficient) discussed.
5. Non-English language.
6. No DOI and not cited by a DOI-registered peer-reviewed work.

### 3.3 Eligibility uncertainty

Papers meeting ≥3 inclusion criteria but unclear on criterion 3 are flagged for full-text review
rather than excluded at title/abstract stage.

---

## 4. Search Sources

| Database | Status | URL | Notes |
|----------|--------|-----|-------|
| OpenAlex | Executed | https://api.openalex.org | Phase 0 searches completed |
| Crossref | Executed | https://api.crossref.org | Exact bibliographic matching |
| ORCID | Executed | https://orcid.org | Author identity verification |
| Scopus | Not accessible | https://www.scopus.com | Search strings prepared (unexecuted) |
| Web of Science | Not accessible | https://webofscience.com | Search strings prepared (unexecuted) |
| Dimensions | Not accessible | https://app.dimensions.ai | Search strings prepared (unexecuted) |
| Semantic Scholar | Not accessed | https://www.semanticscholar.org | API available; not queried |
| arXiv | Not accessed | https://arxiv.org | Preprint server; not queried |
| Google Scholar | Blocked | https://scholar.google.com | reCAPTCHA blocked in Phase 0 |

---

## 5. Search Strategies

### 5.1 Query families

Each query family combines domain terms with interface/energy terms. Database-specific syntax
adapted per source.

**Family A — Generalized thermoelasticity + interface:**
```
("generalized thermoelasticity" OR "Lord-Shulman" OR "Green-Lindsay" OR "Green-Naghdi" OR 
 "dual-phase-lag" OR "three-phase-lag" OR "Moore-Gibson-Thompson" OR "memory-dependent derivative"
 OR "fractional thermoelasticity")
AND
("interface" OR "reflection" OR "transmission" OR "half-space" OR "boundary")
AND
("energy" OR "energy flux" OR "energy ratio" OR "energy partition" OR "dissipation")
```

**Family B — Piezoelectric/piezothermoelastic + wave:**
```
("piezoelectric" OR "piezothermoelastic" OR "piezomagnetic" OR "flexoelectric")
AND
("wave" OR "Rayleigh" OR "surface wave" OR "interface wave")
AND
("reflection" OR "transmission" OR "energy")
```

**Family C — Porous/double-porosity + thermoelastic:**
```
("double porosity" OR "poroelastic" OR "elastic materials with voids" OR "Cowin-Nunziato")
AND
("thermoelastic" OR "thermal")
AND
("interface" OR "reflection" OR "transmission")
```

**Family D — Semiconductor photo-thermo-elastic:**
```
("semiconductor" AND ("photo-thermo-elastic" OR "photothermal" OR "carrier" OR "plasma wave"))
AND
("wave" OR "reflection" OR "transmission" OR "interface")
```

**Family E — Nonlocal/size-dependent + interface:**
```
("nonlocal" OR "strain gradient" OR "size-dependent" OR "Eringen")
AND
("thermoelastic" OR "piezoelectric")
AND
("interface" OR "surface wave" OR "reflection")
```

**Family F — Alternative terminology (novelty confirmation):**
```
("wave energy transport" OR "interface scattering" OR "energy transmission" OR 
 "reflection coefficient" OR "elastic wave energy" OR "coupled-field energy balance" OR
 "acoustic impedance" OR "elastic impedance" OR "dissipative waves")
AND
("thermoelastic" OR "piezoelectric" OR "poroelastic")
AND
("interface" OR "boundary")
```

### 5.2 OpenAlex query syntax (executed in Phase 0)

```
filter=title_and_abstract.search:TERM1,title_and_abstract.search:TERM2
per-page=100
sort=publication_year:desc
```

### 5.3 Crossref query syntax (executed in Phase 0)

```
query.bibliographic=TERMS
rows=10
select=DOI,title,author,issued,container-title,volume,page,is-referenced-by-count
```

### 5.4 Scopus / Web of Science search strings (prepared, unexecuted)

```
TITLE-ABS-KEY ( "generalized thermoelasticity" OR "Lord-Shulman" OR "Green-Lindsay" OR 
  "Green-Naghdi" OR "dual-phase-lag" OR "three-phase-lag" OR "Moore-Gibson-Thompson" OR 
  "memory-dependent derivative" OR "fractional thermoelasticity" )
AND TITLE-ABS-KEY ( "interface" OR "reflection" OR "transmission" OR "half-space" OR "boundary" )
AND TITLE-ABS-KEY ( "energy" OR "energy flux" OR "energy ratio" OR "energy partition" )
AND PUBYEAR > 1955 AND PUBYEAR < 2027
AND ( LIMIT-TO ( LANGUAGE, "English" ) )
```

---

## 6. Study Screening Procedures

### 6.1 Screening stages

| Stage | Input | Output | Method |
|-------|-------|--------|--------|
| S1 | Search results | Title/abstract screening | Two independent reviewers; conflicts resolved by third |
| S2 | S1 included | Full-text eligibility | Full-text retrieval where accessible; metadata-only where not |
| S3 | S2 included | Data extraction | Full data extraction schema (Section 7) |

### 6.2 Screening decisions

Each paper receives one of:
- **INCLUDE** — Meets all inclusion criteria, no exclusion criteria
- **EXCLUDE** — Fails ≥1 inclusion criterion or meets ≥1 exclusion criterion
- **UNCERTAIN** — Insufficient information at title/abstract; proceeds to full-text

### 6.3 Documentation

All screening decisions recorded in `05_screening_decisions.csv` with:
- Study ID
- Decision (INCLUDE/EXCLUDE/UNCERTAIN)
- Reason (specific criterion)
- Reviewer initials
- Date

---

## 7. Data Extraction Schema

Every included study receives a record in `04_literature_master_database.csv` with:

### 7.1 Bibliographic

- study_id, title, authors, year, journal, DOI, publisher, document_type, source_url,
  full_text_access_status, verification_status

### 7.2 Scientific objectives

- research_question, physical_system, main_contribution, originality_claimed, scope_assumptions

### 7.3 Mathematical characteristics

- governing_equations, constitutive_relations, state_variables, differential_operators,
  thermal_model, coupling_mechanisms, dimensionality, geometric_assumptions,
  boundary_interface_conditions, wave_solution_ansatz, secular_equation, dispersion_relation,
  energy_density_formulation, energy_flux_expression, reflection_coefficient_definition

### 7.4 Results and validity

- main_analytical_results, numerical_methods, material_parameters, validation_method,
  limiting_case_checks, energy_balance_checks, sensitivity_analysis, physical_interpretation,
  stated_limitations, identified_limitations, contradictory_evidence, reproducibility_status

### 7.5 Research-gap evidence

- open_questions, missing_validation, incompatible_assumptions, missing_flux_analysis,
  unresolved_interface_conditions, computational_limitations, proposed_future_work

Missing information marked explicitly as `NOT REPORTED` or `UNACCESSIBLE`.

---

## 8. Evidence Synthesis Methods

### 8.1 Synthesis approach

- **Not a meta-analysis:** No pooled effect estimation; literature unsuitable for statistical pooling
- **Critical theoretical synthesis:** Mathematical comparison of governing equations, constitutive
  laws, energy-balance formulations across theories
- **Comparative synthesis:** Structured comparison of methods, interface configurations, wave types,
  models, and results

### 8.2 Handling conflicting findings

- Contradictory results tabulated with source, assumptions, and conditions
- Incompatible assumptions explicitly identified
- No forced consensus where theories are fundamentally different

### 8.3 Treatment of inaccessible full texts

- Metadata-only extraction recorded as `FULL_TEXT_UNACCESSIBLE`
- Abstract-only claims labeled as such
- No inference beyond abstract content

### 8.4 Protocol amendments

- Amendments documented with date, rationale, and scope impact
- No amendment applied retroactively without re-screening affected records

---

## 9. Milestones

| Milestone | Description | Status |
|-----------|-------------|--------|
| A | Foundation audit — validate Phase 0 | COMPLETED AND VERIFIED |
| B | Review protocol — this document | COMPLETED (DRAFT) |
| C | Literature mapping — build deduplicated corpus | NOT STARTED |
| D | Full-text evidence collection — extract and audit | NOT STARTED |
| E | Mathematical foundations — energy-balance framework | NOT STARTED |
| F | Original synthesis — taxonomy and cross-theory relationships | NOT STARTED |
| G | Scientific research architecture — figures, gaps, benchmarks, manuscript | NOT STARTED |
| H | Independent audit — seven-reviewer verification | NOT STARTED |

---

## 10. Limitations

1. Commercial databases (Scopus, Web of Science, Dimensions) not accessible; search strings prepared
   but unexecuted
2. Google Scholar blocked by reCAPTCHA
3. English-language only
4. No full-text systematic review executed in Phase 0; Phase 1 will execute where accessible
5. No claim of preregistration — this is a registration-ready draft only

---

## 11. Next Actions

1. Execute broader literature searches (Milestone C) using Scopus/WoS search strings if access
   becomes available; otherwise extend OpenAlex/Crossref with Family F alternative terminology
2. Build `04_literature_master_database.csv` with screened studies
3. Execute `05_screening_decisions.csv` with explicit reasons
4. Proceed to Milestone D (full-text extraction) for accessible papers