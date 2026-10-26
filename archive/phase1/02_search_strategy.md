# Search Strategy — Phase 1

**Prepared:** 2026-10-21  
**Status:** Partially completed (OpenAlex/Crossref executed; Scopus/WoS/Dimensions prepared but unexecuted)  
**Protocol reference:** LE-PHASE1-2026-10-21-T1

---

## 1. Search Philosophy

Phase 0 demonstrated that OpenAlex and Crossref searches can identify the researcher's corpus and
locate foundational reviews. However, the novelty claim ("zero reviews on interface energy flux")
must be tested against:

1. **Alternative terminology** — reviews may use different words (e.g., "wave energy transport"
   instead of "energy flux partitioning")
2. **Broader databases** — Scopus, Web of Science, Dimensions index different journal sets
3. **Backward/forward citation chasing** — foundational works' reference lists and citing papers

This document defines the complete search strategy for Phase 1.

---

## 2. Query Families

Six query families (A–F) defined in [`01_registered_protocol_draft.md`](01_registered_protocol_draft.md).
Each family is executed against each accessible database with database-specific syntax.

### Family A — Generalized thermoelasticity + interface + energy

Core concept: Does any review synthesize energy flux at interfaces across generalized thermoelastic
theories?

| Component | Terms |
|-----------|-------|
| Thermal models | "Lord-Shulman", "Green-Lindsay", "Green-Naghdi", "dual-phase-lag", "three-phase-lag", "Moore-Gibson-Thompson", "memory-dependent derivative", "fractional thermoelasticity", "generalized thermoelasticity" |
| Interface/boundary | "interface", "reflection", "transmission", "half-space", "boundary", "surface" |
| Energy | "energy flux", "energy ratio", "energy partition", "energy balance", "dissipation", "conservation" |

### Family B — Piezoelectric/piezothermoelastic + wave + energy

Core concept: Is there a review of wave energy in piezoelectric multiphysics interfaces?

| Component | Terms |
|-----------|-------|
| Coupling | "piezoelectric", "piezothermoelastic", "piezomagnetic", "flexoelectric", "magnetoelectric" |
| Waves | "wave", "Rayleigh", "surface wave", "interface wave", "bulk wave" |
| Interface/energy | "reflection", "transmission", "energy", "energy flux", "impedance" |

### Family C — Porous/double-porosity + thermoelastic + interface

Core concept: Is there a mechanics-specific review of double-porosity interface waves?

| Component | Terms |
|-----------|-------|
| Porosity | "double porosity", "poroelastic", "elastic materials with voids", "Cowin-Nunziato", "single porosity" |
| Thermal | "thermoelastic", "thermal", "heat conduction" |
| Interface | "interface", "reflection", "transmission", "boundary condition" |

### Family D — Semiconductor photo-thermo-elastic + wave

Core concept: Is there a mechanics review of semiconductor carrier-thermal-elastic wave coupling?

| Component | Terms |
|-----------|-------|
| Medium | "semiconductor", "photo-thermo-elastic", "photothermal" |
| Physics | "carrier", "plasma wave", "deformation potential", "two-temperature" |
| Waves/interface | "wave", "reflection", "transmission", "interface" |

### Family E — Nonlocal/size-dependent + interface

Core concept: Is there a review of nonlocal surface/interface waves in multiphysics media?

| Component | Terms |
|-----------|-------|
| Scale | "nonlocal", "strain gradient", "size-dependent", "Eringen", "couple stress" |
| Medium | "thermoelastic", "piezoelectric", "poroelastic" |
| Geometry | "interface", "surface wave", "reflection", "half-space" |

### Family F — Alternative terminology (novelty confirmation)

Core concept: Do functionally equivalent reviews exist under different names?

| Component | Terms |
|-----------|-------|
| Energy/wave | "wave energy transport", "interface scattering", "energy transmission", "reflection coefficient", "elastic wave energy", "coupled-field energy balance", "acoustic impedance", "elastic impedance", "dissipative waves" |
| Medium | "thermoelastic", "piezoelectric", "poroelastic", "generalized continuum" |
| Geometry | "interface", "boundary" |

---

## 3. Database-Specific Execution

### 3.1 OpenAlex (EXECUTED in Phase 0)

**Syntax:** `filter=title_and_abstract.search:TERM1,title_and_abstract.search:TERM2&per-page=100`

**Executed searches (Phase 0, 2026-10-21):**

| Query | Works | On-target reviews |
|-------|-------|-------------------|
| type:review + thermoelastic | 10 | 0 on interfaces |
| type:review + "nonlocal elasticity" | 2 | 0 on thermoelastic interfaces |
| title:review + thermoelastic | 112 | Chandrasekharaiah 1986/1998; Shakeriaski 2021 |
| type:review + "piezo-thermoelastic" | 0 | 0 |
| title:review + "memory-dependent" | 77 | 0 on thermoelastic interfaces |
| title:review + "fractional thermoelastic" | 1 | 0 (unverified venue) |
| title:review + piezoelectric + wave | 163 | 0 (all energy-harvesting/SHM) |
| title:review + "surface waves" | 270 | 0 (all ocean/geophysical/metasurface) |
| title:review + "reflection and transmission" | 40 | 0 (none on elastic/piezoelectric) |
| title:review + "poroelastic" | 95 | 0 (all geotechnical) |
| title:review + flexoelectric | 23 | 0 (all materials/applications) |
| title:review + photothermal + semiconductor | 30 | 0 (all biomedical/therapy) |

**Remaining OpenAlex executions (Phase 1):**
- Family F alternative terminology searches
- Backward/forward citation from Chandrasekharaiah 1986/1998 and Shakeriaski 2021

### 3.2 Crossref (EXECUTED in Phase 0)

**Syntax:** `query.bibliographic=TERMS&rows=10&select=DOI,title,author,issued,container-title,volume,page,is-referenced-by-count`

**Executed searches (Phase 0, 2026-10-21):**
- Foundational works: Biot 1956, Lord & Shulman 1967, Green & Lindsay 1972, Green & Naghdi 1991,
  Tzou 1995, Roy Choudhuri 2007, Eringen 1972, Nunziato & Cowin 1979, Quintanilla 2019,
  Hetnarski & Ignaczak 1999, Chandrasekharaiah 1986/1998, Shakeriaski 2021

**Remaining Crossref executions (Phase 1):**
- Family A–F searches with bibliographic terms
- Citation count verification for key foundational works

### 3.3 Scopus (PREPARED, UNEXECUTED)

**Search string (Family A):**
```
TITLE-ABS-KEY ( "generalized thermoelasticity" OR "Lord-Shulman" OR "Green-Lindsay" OR 
  "Green-Naghdi" OR "dual-phase-lag" OR "three-phase-lag" OR "Moore-Gibson-Thompson" OR 
  "memory-dependent derivative" OR "fractional thermoelasticity" )
AND TITLE-ABS-KEY ( "interface" OR "reflection" OR "transmission" OR "half-space" OR "boundary" )
AND TITLE-ABS-KEY ( "energy" OR "energy flux" OR "energy ratio" OR "energy partition" )
AND PUBYEAR > 1955 AND PUBYEAR < 2027
AND ( LIMIT-TO ( LANGUAGE, "English" ) )
```

**Status:** Not accessible in this sandbox. Search string documented for future execution.

### 3.4 Web of Science (PREPARED, UNEXECUTED)

**Search string (Family A):**
```
TS = ( ("generalized thermoelasticity" OR "Lord-Shulman" OR "Green-Lindsay" OR "Green-Naghdi" 
  OR "dual-phase-lag" OR "three-phase-lag" OR "Moore-Gibson-Thompson" OR "memory-dependent 
  derivative" OR "fractional thermoelasticity") )
AND TS = ( ("interface" OR "reflection" OR "transmission" OR "half-space" OR "boundary") )
AND TS = ( ("energy" OR "energy flux" OR "energy ratio" OR "energy partition") )
AND PY > 1955 AND PY < 2027
AND LA = (English)
```

**Status:** Not accessible in this sandbox. Search string documented for future execution.

### 3.5 Dimensions (PREPARED, UNEXECUTED)

Same query families adapted to Dimensions search syntax. Status: not accessible.

### 3.6 Semantic Scholar (NOT YET ACCESSED)

API available at https://api.semanticscholar.org/graph/v1. Not yet queried in Phase 0 or Phase 1.

### 3.7 arXiv (NOT YET ACCESSED)

Preprint server at https://arxiv.org. Not yet queried.

### 3.8 Google Scholar (BLOCKED)

reCAPTCHA blocked in Phase 0. Not retried in Phase 1.

---

## 4. Citation Chasing

### 4.1 Backward citation chasing

From each foundational review, extract references to identify:
- Earlier theoretical works not captured by keyword searches
- Foundational interface/energy papers predating 1956

**Seed reviews:**
- Chandrasekharaiah 1986 (DOI: 10.1115/1.3143705)
- Chandrasekharaiah 1998 (DOI: 10.1115/1.3098984)
- Shakeriaski et al. 2021 (DOI: 10.1093/jcde/qwaa082)

### 4.2 Forward citation chasing

From each foundational work, identify citing papers to capture:
- Later interface/energy applications
- Reviews citing the foundational works

**Seed works:**
- Biot 1956 (DOI: 10.1063/1.1722351)
- Lord & Shulman 1967 (DOI: 10.1016/0022-5096(67)90024-5)
- Eringen 1972 (DOI: 10.1016/0020-7225(72)90050-x)
- Quintanilla 2019 (DOI: 10.1177/1081286519862007)

**Status:** Not yet executed. OpenAlex `referenced_works` and `cited_by` APIs support this.

---

## 5. Deduplication Method

1. Primary key: DOI (where available)
2. Secondary key: title + year + first author (where DOI missing)
3. Tertiary key: title similarity (for preprints vs. published versions)
4. Duplicates flagged with `duplicate_of` field referencing the canonical study_id

---

## 6. Search Execution Log

All searches logged in `03_search_execution_log.csv` with:
- Database, exact query, date executed, filters, result count, records exported, limitations

Phase 0 searches are imported as baseline records.

---

## 7. Next Actions

1. Import Phase 0 search log into `03_search_execution_log.csv`
2. Execute Family F alternative terminology searches on OpenAlex
3. Execute backward/forward citation chasing on seed reviews
4. If Scopus/WoS access becomes available, execute prepared search strings
5. Build `04_literature_master_database.csv` from deduplicated results