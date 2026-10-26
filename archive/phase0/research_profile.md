# Research Profile — Vipin Gupta

**Prepared:** 2026-10-21 · **Evidence cut-off:** 2026-10-21
**Evidence standard:** every factual claim below carries one of four tags —
`VERIFIED` (field returned by a registry/API or quoted from a retrieved publisher page),
`SNAPSHOT` (a database value that will drift, with access date),
`INFERRED` (reasoned from verified data, not directly stated by a source),
`UNVERIFIED` (could not be confirmed in this session).

---

## 1. Identity resolution (do this before any bibliometrics)

Name-based author search is unsafe for this name. An OpenAlex search for `Vipin Gupta` returns a
top hit with **74 works, 47,861 citations and an h-index of 22**, affiliated with the University of
Delhi, the National Institutes of Health, Deakin, QUT, Bristol and LSHTM. That profile is a
**biomedical/epidemiology researcher with ORCID 0000-0002-0607-5543** and is **not** the author of
the wave-propagation corpus. Any bibliometric analysis keyed on the name alone would be wrong by
roughly two orders of magnitude.

### 1.1 Correct identity

| Field | Value | Status | Evidence |
|---|---|---|---|
| Name | Vipin Gupta | `VERIFIED` | ORCID public record |
| ORCID | [0000-0002-5238-1963](https://orcid.org/0000-0002-5238-1963) | `VERIFIED` | ORCID record; OpenAlex author `A5013823819` |
| OpenAlex author ID | [A5013823819](https://openalex.org/A5013823819) | `VERIFIED` | OpenAlex `/authors` response |
| Current position | Assistant Professor (Mathematics), Department of Mathematics, Gurugram University, Gurugram, India | `VERIFIED` | ORCID employment entry, start date 2024-06-28 |
| Previous affiliation | Department of Mathematics, Indira Gandhi University, Meerpur (Rewari), Haryana, India | `VERIFIED` | Author affiliations on 2022–2025 articles (Springer, Emerald, IOP, Taylor & Francis pages); OpenAlex affiliation years 2022–2025 |
| Verified e-mail domain | `gurugramuniversity.ac.in` | `VERIFIED` | ORCID "verified email domains" |
| Field | Applied Mathematics; mechanics of materials; wave propagation | `VERIFIED` | ORCID; OpenAlex topics; article titles |
| CSIR funding (doctoral-era) | CSIR, New Delhi, File No. `09/1293(0003)/2019-EMR-I` | `VERIFIED` (publisher acknowledgement) | Acknowledgement text on Taylor & Francis and Emerald article pages |

### 1.2 Excluded homonyms and duplicate records

| Entity | Why excluded / flagged |
|---|---|
| OpenAlex `A5024011528`, ORCID `0000-0002-0607-5543` | Biomedical/global-health researcher; 74 works, 47,861 citations. **Different person.** |
| OpenAlex `A5128895995` (6 works) and `A5137960888` (2 works) | Additional split profiles for the same Vipin Gupta; records also carry ORCID 0000-0002-5238-1963. Cause of count inflation between the author profile and the ORCID filter. |
| Google Scholar profile `o014_b0AAAAJ` | Profile page itself was **blocked by reCAPTCHA** in this session. A search-engine index snippet identifies it as "Vipin Gupta — Gurugram University — Verified email at gurugramuniversity.ac.in — Applied Mathematics" and lists the 2024 *Mechanics of Advanced Materials and Structures* paper, which is consistent with the correct identity. **Profile metrics are therefore not quoted as verified.** |

> **Consequence:** all bibliometrics below use the **ORCID-linked** record set, not the name-linked set.

---

## 2. Publication record

### 2.1 Counts

| Metric | Value | Source / date | Status |
|---|---|---|---|
| Works attributed to OpenAlex author `A5013823819` | **41** | OpenAlex author record, updated 2026-10-19 | `SNAPSHOT` |
| Works carrying ORCID `0000-0002-5238-1963` | **49** | OpenAlex `/works?filter=author.orcid:...`, 2026-10-21 | `SNAPSHOT` |
| Citations (author profile) | **827** | OpenAlex author record, updated 2026-10-19 | `SNAPSHOT` |
| h-index (author profile) | **19** | OpenAlex | `SNAPSHOT` |
| i10-index (author profile) | **28** | OpenAlex | `SNAPSHOT` |
| 2-year mean citedness | **16.26** | OpenAlex | `SNAPSHOT` |
| Works listed on ORCID | **13** | ORCID public record | `VERIFIED` |
| Peer reviews recorded on ORCID | **13 reviews for 7 publications/grants** | ORCID public record | `VERIFIED` |

The 41 vs 49 discrepancy is a **record-linkage artifact** (split author profiles, preprints, book
chapter, and duplicate DOI deposits), not evidence of 49 distinct peer-reviewed articles. The
author-level citation total (827) should not be recomputed by summing work-level counts, because
deduplicated and split records would double-count.

### 2.2 Year distribution (attributed profile)

| Year | Works | Citations accrued |
|---|---|---|
| 2022 | 3 | 52 |
| 2023 | 15 | 401 |
| 2024 | 9 | 206 |
| 2025 | 9 | 155 |
| 2026 | 5 | 13 |

`SNAPSHOT` — OpenAlex `counts_by_year`, retrieved 2026-10-21.

Interpretation (`INFERRED`): the corpus is **young and front-loaded**. Roughly 83% of the works were
published in 2023–2026, and the citation peak lags publication by about one year, consistent with a
rapidly accumulating but still early-career record. The 2026 citation figure is necessarily partial.
Several records carry 2026 or 2027 *issue* years because of online-first publication; these are not
evidence of future work.

### 2.3 Most-cited works (OpenAlex work-level counts, 2026-10-21)

| # | Work | Venue (vol/issue) | Year | Citations |
|---|---|---|---|---|
| 1 | Vibrational analysis of size-dependent thermo-piezo-photo-electric semiconductor medium under memory-dependent MGT photo-thermoelasticity | Mech. Adv. Mater. Struct. 31(28) | 2024 | 68 |
| 2 | Impact of memory-dependent heat transfer on Rayleigh waves in nonlocal piezo-thermo-elastic medium with voids | Int. J. Numer. Methods Heat Fluid Flow 34(4) | 2024 | 55 |
| 3 | Size-dependent effect on surface waves in micropolar thermoelastic medium with dual pore connectivity | Physica Scripta 99(6) | 2024 | 50 |
| 4 | Fractional and memory effects on wave reflection in pre-stressed microstructured solids with dual porosity | Eur. J. Mech. A/Solids 111 | 2025 | 44 |
| 5 | Photo-thermo-piezo-elastic waves in semiconductor medium with two-temperature models and higher-order memory | Int. J. Numer. Methods Heat Fluid Flow 34(1) | 2024 | 41 |
| 6 | Memory-dependent and fractional order analysis of the initially stressed piezo-thermoelastic medium | Mech. Adv. Mater. Struct. 31(20) | 2024 | 36 |
| 7 | Hydro-thermo-electromechanical response in a size-dependent porous piezoelectric medium under memory-dependent MGT | Mech. Adv. Mater. Struct. 33(1) | 2025 | 33 |
| 8 | Reflection at the free surface of the orthotropic piezo-hygro-thermo-elastic medium | Int. J. Numer. Methods Heat Fluid Flow 33(10) | 2023 | 33 |
| 9 | Reflection of quasi-plasma wave in photo-piezo semiconductor medium with fractional two-temperature models | Physica Scripta 99(2) | 2024 | 32 |
| 10 | Fractional and MDD analysis of piezo-photo-thermo-elastic waves in semiconductor medium | Mech. Adv. Mater. Struct. 31(25) | 2024 | 30 |
| 11 | Double porous thermoelastic waves in a homogeneous isotropic solid with inviscid liquid | Arch. Appl. Mech. 93(5) | 2023 | 28 |
| 12 | Reflection/transmission of plane waves at an ideal fluid / nonlocal piezothermoelastic interface | Int. J. Numer. Methods Heat Fluid Flow 33(2) | 2023 | 28 |
| 13 | Comparative analysis of double and single porosity effects on SH-wave vibrations in periodic porous lattices | Soil Dyn. Earthq. Eng. 186 | 2024 | 27 |
| 14 | Rayleigh wave in nonlocal piezo-thermo-electric semiconductor medium with fractional MGT model | Waves Random Complex Media 36(5) | 2024 | 27 |
| 15 | Generalized plane waves in a rotating thermoelastic double porous solid | Int. J. Appl. Mech. Eng. 27(4) | 2022 | 24 |

Full machine-readable record: [`data/publications_verified.csv`](data/publications_verified.csv).

### 2.4 Venue profile

Counted from the 49 ORCID-linked records retrieved on 2026-10-21 (`INFERRED`; ±1 record because of
linkage). Venues with ≥2 records:

| Venue | Publisher | Records | Character |
|---|---|---|---|
| Int. J. Numerical Methods for Heat & Fluid Flow | Emerald | ~10 | Numerical heat/fluid mechanics; fast, application-oriented |
| Mechanics of Advanced Materials and Structures | Taylor & Francis | 6 | Advanced materials, coupled mechanics |
| Physica Scripta | IOP | ~5 | Physics; broad-scope, high-volume |
| Scientific Reports | Nature Portfolio | 4 | Broad-scope, open access |
| European Journal of Mechanics — A/Solids | Elsevier | 3 | Solid mechanics |
| Journal of Thermal Stresses | Taylor & Francis | 2 | Thermal-stress specialty journal |
| Applied Mathematical Modelling | Elsevier | 2 | Applied mechanics modelling |

The modal venue set is **specialist applied-mechanics and heat-transfer journals**, not general
science or pure mathematics. This matters for the review strategy: the natural audience is the
thermoelasticity/poroelasticity/wave-propagation community, and the natural review venue is a
mechanics review journal rather than a general-science outlet.

---

## 3. Research programme: themes, questions, and method

### 3.1 Thematic composition (title-level keyword incidence)

`INFERRED` from the 49 titles; this is a **title-level** count, not full-text coding, and themes overlap.

| Theme | Approx. records | Representative evidence |
|---|---|---|
| Interface / reflection / transmission / energy ratios | ~18 | `10.1007/s12648-022-02568-w`; `10.1088/1402-4896/acfced`; `10.1007/s40010-023-00850-y` |
| Memory-dependent derivatives & fractional calculus | ~14 | `10.1016/j.ijengsci.2014.04.014` (cited as foundation); `10.1080/15376494.2023.2211065` |
| Piezoelectric / piezomagnetic / flexoelectric coupling | ~20 | `10.1088/1402-4896/ad4829`; `10.1016/j.compstruct.2025.118997` |
| Porosity: voids, single/double porosity, liquid saturation | ~10 | `10.1007/s00419-023-02364-w`; `10.1088/1402-4896/ad6ae7` |
| Semiconductor / photo-thermo-elastic / plasma waves | ~8 | `10.1108/hff-07-2023-0380`; `10.1038/s41598-026-59340-x` |
| Nonlocal / size-dependent / gradient theories | ~7 | `10.1108/hff-10-2023-0615`; `10.1016/j.apm.2026.116904` |
| Rotating, initially stressed, functionally graded media | ~8 | `10.2478/ijame-2022-0055`; `10.1016/j.compstruct.2025.118997` |
| Structural elements (beams, plates, cavities, tunnels, layered shells) | ~7 | `10.1142/s0219455426420150`; `10.1016/j.apm.2026.116904` |

### 3.2 Recurring research questions

These are the questions the corpus returns to, stated in the corpus's own vocabulary:

- **RQ-A — Model sensitivity.** How does replacing Fourier conduction with a generalized law
  (Lord–Shulman, Green–Lindsay, Green–Naghdi, dual-phase-lag, three-phase-lag, Moore–Gibson–Thompson)
  change the number, speed, dispersion, and attenuation of wave modes?
- **RQ-B — Interface bookkeeping.** At a boundary between two different multiphysics media, how is
  incident energy distributed among reflected and transmitted modes, and is that distribution
  consistent with energy conservation?
- **RQ-C — Memory and fractionality.** How do memory kernels and fractional orders reshape amplitude,
  phase, and dispersion relative to integer-order models?
- **RQ-D — Scale.** How do nonlocal, gradient, couple-stress, and flexoelectric parameters shift
  dispersion and surface-wave speed at micro/nanoscale?
- **RQ-E — Porosity.** How do voids, single porosity, and double porosity (with or without a
  pore-fluid) add modes and alter interface conditions?
- **RQ-F — Environment.** How do rotation, initial stress, gravity, functional grading, and imperfect
  bonding modulate the above?
- **RQ-G — Closed form.** Can a secular equation be obtained in closed form and physically interpreted
  in its limiting cases?

### 3.3 Methodological signature

The corpus follows a remarkably stable analytical pipeline (`INFERRED` from titles, abstracts, and
the structure of the articles):

1. **Select a medium and a constitutive package** (e.g., orthotropic piezo-thermo-elastic solid with voids).
2. **Linearize** the balance laws about a reference state, retaining initial stress/rotation where relevant.
3. **Reduce** the coupled field equations using displacement potentials, Helmholtz decomposition, or a
   state-vector formulation.
4. **Substitute a harmonic plane-wave (or Rayleigh) ansatz** with complex slowness.
5. **Derive the secular equation** as the determinant of a coupled algebraic system (Christoffel-type matrix).
6. **Apply interface conditions** — continuity of displacement/traction, temperature/heat flux,
   potential/electric displacement, carrier density/flux; or spring-like imperfect-bond conditions.
7. **Compute amplitude ratios and then energy ratios** from the stress and flux fields.
8. **Perform parametric sensitivity analysis** in frequency, incidence angle, memory parameter,
   fractional order, porosity, nonlocal length, and rotation.
9. **Check limiting cases** against classical elasticity/thermoelasticity.

The methodological repertoire is therefore **analytical continuum mechanics + complex dispersion
analysis + parametric computation**, with occasional numerical (finite-element / transform-inversion)
work. It is not an experimental programme, and it is not a numerical-methods programme despite
appearances in numerically titled journals.

### 3.4 The pivot: step 7 is the unexplored theoretical core

Steps 1–6 and 8–9 are highly standardized across the literature. Step 7 — the *definition and
conservation of energy flux* in a coupled, dissipative, memory-dependent medium — is where the
corpus is most active and least theorized. Papers compute "energy ratios", but there is no shared
statement of what the energy flux functional is when:
- heat conduction is hyperbolic, so the thermal flux is not `q·n` alone;
- the medium is piezoelectric, so electrical energy flux must be included;
- the medium is nonlocal, so the divergence theorem argument behind a local flux breaks down;
- the interface is imperfect, so the interface itself can store or dissipate energy;
- the constitutive law is a convolution, so "instantaneous" flux is not the physically relevant object.

This is the single most defensible theoretical gap in the programme. It motivates topic **T1**.

---

## 4. Collaboration network

`VERIFIED` via OpenAlex `group_by=authorships.author.id` on the ORCID filter (counts are lower
bounds because several collaborators have duplicate author IDs).

| Collaborator | Joint records | Role in the programme |
|---|---|---|
| Mahabir Singh Barak (Indira Gandhi University / Gurugram University) | 29 | Senior co-author; co-supervisor figure; thermoelasticity and memory modelling |
| Soumik Das (Amrita Vishwa Vidyapeetham) | 23 | Size-dependent, porous, flexoelectric and MGT modelling |
| Rachaita Dutta | 9 | Porous/flexoelectric wave mechanics |
| Abhik Sur | 9 | Nonlocal thermoelasticity, fractional/MGT, cavities |
| Hijaz Ahmad | 9 | Applied mathematics, fractional models |
| Vijayata Pathania | 8 | Double-porosity thermoelasticity, interfaces |
| Rajesh Kumar | 8 | Double porosity, rotation, interface energy |
| Murat Yaylacı | 7 | Solid mechanics, contact/loading problems |
| Rajneesh Kumar | 4 (+3 duplicate ID) | Classical thermoelasticity; Kurukshetra University |
| Bandar Almohsen | 4 | Fractional/nonlocal modelling |
| Abhinav Singhal | 3 (+3) | Wave propagation, composite structures |
| Eduard-Marius Craciun | 3 | Continuum mechanics (Romania) |
| Sandeep Kumar | 3 | Visco-thermoelasticity |
| Meghana A. R. | 3 | Porous seabed, moving loads |

`INFERRED`: the network is **two clusters bridged by the researcher** — a Haryana thermoelasticity
cluster (Barak, Rajesh Kumar, Rajneesh Kumar, Pathania, Sandeep Kumar, Kumari) and a West Bengal /
South India applied-mathematics cluster (Das, Dutta, Sur, Singhal). This is an asset for a review:
it gives access to both the analytical-thermoelasticity and the size-dependent/porous communities.

The network is **domestic-plus-diaspora**, with international co-authors from Turkey, Saudi Arabia,
Romania, Italy/Egypt and Pakistan. There is no evidence of a sustained experimental collaboration.

---

## 5. Interdisciplinary reach

`INFERRED` from topic classification and venue choice:

- **Core:** applied mathematics, continuum mechanics, thermal stresses.
- **Adjacent (strong):** acoustics and ultrasonic nondestructive evaluation; piezoelectric smart
  materials and SAW devices; geophysics/poroelasticity (wave-induced fluid flow, seabed response);
  semiconductor optoelectronics and photothermal metrology.
- **Peripheral (weak, single papers):** biomechanics/thermal therapy, bioremediation and
  bio-electrochemical systems, digital-twin mathematics education.

The peripheral papers (`10.22207/jpam.20.2.63`, `10.1007/978-3-032-31204-4_13`,
`10.1142/s0219581x26400247`) are outliers relative to the core programme and should not be used to
define the review's domain.

---

## 6. Influence pattern (what is actually cited, and why)

`INFERRED` from the citation ranking and titles:

1. **The most-cited papers combine three ingredients**: a canonical generalized theory (usually MGT
   or memory-dependent derivatives), a multiphysics coupling (piezo + photo + thermal), and a
   canonical geometry (Rayleigh surface wave or vibrational analysis). Purely theoretical or purely
   parametric papers rank lower.
2. **Size-dependent + porous + surface-wave papers** form the second citation tier. This reflects
   demand from the micro/nano and geotechnical communities, not from the thermoelasticity community alone.
3. **The energy-ratio series is coherent but moderately cited** (8–22 citations each). Its value is
   *programmatic* — seven or more papers on one concept — rather than *bibliometric*. This is exactly
   the profile that supports an authoritative synthesis: enough primary work to ground it, not
   enough competition to pre-empt it.
4. **Citation counts are young.** A 2023–2024 paper with 30–60 citations is performing well relative
   to the field's median, but the absolute numbers are small. No claim about "highly cited" status is made.

---

## 7. What could not be verified

Listed explicitly, as required:

| Item | Status | Note |
|---|---|---|
| Google Scholar total citations, h-index, i10 | `UNVERIFIED` | Profile blocked by reCAPTCHA; search-index snippet only |
| Scopus Author ID and Scopus metrics | `UNVERIFIED` | No Scopus API access in this session |
| Web of Science ResearcherID / metrics | `UNVERIFIED` | Not retrieved |
| PhD year, institution, thesis title | `UNVERIFIED` | Not present on the ORCID public record; not asserted anywhere in this workspace |
| Postdoctoral history | `UNVERIFIED` | No evidence found |
| Editorial board memberships | `UNVERIFIED` | None confirmed |
| Awards and honours | `UNVERIFIED` | None confirmed |
| Grant portfolio beyond CSIR File No. 09/1293(0003)/2019-EMR-I | `UNVERIFIED` | One acknowledgement verified; no funder database query executed |
| Exact CRediT contribution on every paper | `UNVERIFIED` | CRediT statements retrieved for only a few articles |
| Whether all 49 ORCID-linked records are correctly attributed | `PARTIAL` | Split/duplicate OpenAlex profiles exist; a few records may be mislinked |
| Full-text reading of the corpus | **Not claimed** | Analysis is based on titles, abstracts, metadata, and publisher landing pages |
| Language of instruction / teaching profile | `UNVERIFIED` | Irrelevant to the review and not pursued |

---

## 8. Implications for a landmark review

`INFERRED`, stated as strategic reasoning rather than fact:

1. **Authorship credibility is highest in the interface/energy sub-domain.** The researcher has a
   multi-paper, multi-year series on energy ratios spanning elastic/piezo/thermo/porous/viscoelastic
   media. A review in this area would be read as an authoritative synthesis by the person who helped
   build the sub-field, not as an outsider's survey.
2. **The programme is broad enough to support a unifying framework but narrow enough to be coherent.**
   Five constitutive axes (thermal lag, memory/fraction, piezoelectricity, porosity, nonlocality) all
   appear repeatedly, which is precisely the raw material for an original taxonomy.
3. **The citation base is young**, so the review must earn authority through *methodological rigour*
   (explicit definitions, conservation proofs, reproducibility tables), not through the author's
   citation record.
4. **The natural language of the review is mathematical.** The audience will expect explicit governing
   equations, interface conditions, and energy identities — not a narrative survey. This favours a
   review venue with a mathematical-mechanics readership.
5. **The main risk is self-referentiality.** A synthesis that draws mainly on the author's own series
   will be dismissed. The review must be built on an independently sampled corpus, with the author's
   work treated as one contribution among many. This is the single most important design constraint
   for Phase 1.

---

## 9. One-paragraph profile

Vipin Gupta is an Assistant Professor of Mathematics at Gurugram University (since June 2024),
previously at Indira Gandhi University, Meerpur. His ORCID-linked record contains 49 works
(2022–2026), of which 41 are attributed to a single OpenAlex author profile with 827 citations,
h-index 19, and i10-index 28 as of 2026-10-19. The programme is a tightly coherent body of analytical
continuum mechanics on **wave propagation and reflection–transmission in multiphysics continua**:
generalized thermoelasticity, piezoelectric and piezothermoelastic coupling, voids and double
porosity, semiconductor photo-thermo-elasticity, nonlocal/size effects, and memory-dependent or
fractional heat transport. Its methodological signature is the harmonic-plane-wave → secular-equation
→ interface-condition → energy-ratio pipeline. Its most distinctive and least theorized component is
the **energy-flux bookkeeping at interfaces**, which is the basis of the recommended review direction.
