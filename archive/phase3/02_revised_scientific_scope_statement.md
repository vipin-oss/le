# Deliverable 2 — Revised Scientific Scope Statement

**Branch:** arena/40393d9f-le  
**Prepared:** 2026-10-21  
**Supersedes:** Phase 2 provisional domain ("Wave Propagation, Reflection–Transmission, Energy Transport and Coupled-Field Interactions in Generalized Multiphysics Continua")  
**Alignment:** Master Editorial Directive §5, §15

---

## 1. Revised Scope Statement

### 1.1 Working title

**"Wave Propagation, Energy Transport, and Interface Phenomena in Generalized Multiphysics Continua: A Comprehensive Review"**

### 1.2 Scientific domain

The review covers the mathematical modeling, wave propagation, reflection–transmission, energy transport, and dissipation in continuum mechanical systems where multiple physical fields are coupled and/or classical constitutive assumptions are generalized. The domain spans:

| Sub-domain | Physical content | Mathematical character |
|------------|-----------------|----------------------|
| Classical wave mechanics | Elastic waves, P/SV/SH waves, stress waves, dispersion, mode conversion | Hyperbolic PDEs, real wave speeds |
| Thermoelasticity | Classical coupled (Fourier), generalized thermal transport (LS, GL, GN II/III, DPL, TPL, MGT) | Parabolic-to-hyperbolic, finite/infinite propagation speed |
| Generalized constitutive theories | Memory-dependent derivatives, fractional operators, hereditary integrals, nonlocal elasticity, strain-gradient | Integro-differential, nonlocal, fractional |
| Electro-mechanical interactions | Piezoelectricity, piezothermoelasticity, electrostriction | Coupled mechanical-electrical PDEs |
| Porous and microstructured continua | Voids, double porosity, micropolar, micropolar thermoelasticity | Multi-constituent, internal variables |
| Semiconductor and photothermal interactions | Carrier diffusion, recombination, thermal-mechanical coupling | Drift-diffusion coupled to elasticity |
| Wave–interface phenomena | Reflection, transmission, scattering, mode conversion, energy partition at boundaries | Interface conditions, scattering matrices |
| Energy and dissipation | Energy flux, dissipation inequality, thermodynamic admissibility, well-posedness | Clausius-Duhem, Coleman-Noll, energy balances |
| Applications | Smart structures, sensing, energy harvesting, nondestructive evaluation, geophysics | Boundary-value problems, inverse problems |

### 1.3 What is IN scope

- Mathematical formulations of continuum theories with clearly stated assumptions
- Wave propagation characteristics (speeds, dispersion, attenuation, polarization)
- Reflection and transmission at interfaces between dissimilar media
- Energy flux definitions and conservation identities under specified model assumptions
- Thermodynamic admissibility (dissipation inequality, well-posedness, causality)
- Representative analytical and numerical solution methods
- Documented applications with evidence in the peer-reviewed literature
- Existing review coverage and research gaps

### 1.4 What is OUT of scope

- Experimental device design and engineering implementation details
- Numerical method development (finite element, finite difference) as a primary topic — only as applied to continuum problems
- Quantum mechanics, relativistic field theory, or quantum field theory
- Material synthesis, manufacturing, or processing
- Claims of mathematical error in individual published papers (per Master Editorial Directive §1, §12)
- Speculative allegations about author correctness or intentional misrepresentation

### 1.5 Target audience

| Reader type | What they need | How the review serves them |
|-------------|---------------|---------------------------|
| Beginning researcher | Foundational framework, notation, governing equations | Sections 3–4 with notation table, worked derivations |
| Doctoral student | Competing approaches, technical background, reproduction path | Comparative theory sections, benchmark specifications |
| Experienced scientist | Systematic comparisons, limitations, open questions | Synthesis sections, taxonomy, future research roadmap |
| Journal reviewer | Coherent scientific contribution, not a paper collection | Integrative narrative, original taxonomy, evidence map |

### 1.6 Scope boundaries justified by evidence

The scope is bounded by the **24-record deduplicated database** from Phase 2 (11 foundational works + 7 researcher-corpus studies + 6 external discoveries), extended through systematic literature search (Directive §7). Each included topic must have:

- At least 3 peer-reviewed primary sources
- Clearly stated mathematical assumptions
- Documented wave propagation or interface behavior
- Relevance to generalized multiphysics continua

Topics with fewer than 3 sources or only abstract-only accessibility are listed in the **evidence map** but not selected for detailed exposition.

---

## 2. Scope Evolution from Phase 2

| Phase 2 position | Phase 3 revision | Rationale |
|-----------------|-----------------|-----------|
| Focus on identifying mathematical errors in individual papers | Constructive synthesis of established knowledge | Master Editorial Directive §1 |
| Emphasis on "gaps" as errors in specific publications | Emphasis on open questions and future research opportunities | Directive §12, §14 |
| Adversarial gap register (GAP-001 through GAP-012) | Reframed as "research opportunities" with evidence levels | Directive §12 |
| Numerical verification as core contribution | Numerical benchmarks as supporting evidence, not central claim | Directive §13 (originality through synthesis) |
| 24-record corpus as complete | 24-record corpus as seed; expand to hundreds via systematic search | Directive §7 |

---

## 3. Knowledge Products the Review Will Deliver

1. **Historical synthesis**: How continuum wave theory evolved from classical elasticity through generalized thermoelasticity to multiphysics and nonlocal formulations.
2. **Multidimensional taxonomy**: A classification combining constitutive theory, physical coupling, wave behavior, interface structure, and validation evidence.
3. **Mathematical relationship framework**: Assumption-aware account of how models relate (limiting cases, specializations, extensions).
4. **Comparative theory atlas**: Variables, equations, mechanisms, and applications by theory family.
5. **Research evidence map**: Which problems, materials, and methods have been investigated; where evidence is thin.
6. **Future research roadmap**: Evidence-supported directions in theory, computation, and experiment.

---

## 4. What the Review Will NOT Do

| Prohibited action | Directive reference | Alternative approach |
|-------------------|---------------------|---------------------|
| Frame prior publications as containing mathematical errors | §1, §12 | Present differences as assumptions, approximations, model-specific validity |
| Conduct retrospective audit of author correctness | §1 | Organize and synthesize established knowledge |
| Include speculative allegations | §1 | Record only conclusive, transparently sourced findings |
| Present uncertain equations as universal identities | §9 | Use equation verification register; label validity domains |
| Compare non-equivalent numerical quantities | §11 | Include explanatory notes when assumptions differ |
| Inflate length with irrelevant branches | §5 | Include only when evidence demonstrates meaningful connection |
| Set mandatory word count before journal investigation | §16 | Prepare Version A (journal-focused) and Version B (extended) |

---

## 5. Alignment with Reference Model (Abdalla et al. 2022)

| Reference practice | Adoption in this review |
|-------------------|------------------------|
| Executive summary upfront | "Review Scope and Purpose" section |
| Problem-driven hierarchy | Sections organized by physical problem, not paper list |
| Methods before applications | Mathematical foundations before theory-specific sections |
| Sequential equation numbering | All major equations numbered through manuscript |
| Notation/acronym tables | Master symbol table early |
| Comparison figures | Whisker plots for energy ratios; contour plots for dispersion |
| Consistent model template | Each theory: motivation → equations → waves → interfaces → energy → limitations |
| Open questions per section | End each section with topic-specific questions |
| Future research roadmap | Organized by theory/computation/experiment |
| Constructive tone | Differences framed as assumptions, not errors |

---

**Next:** Proceed to Deliverable 3 (Evidence-Supported Article Title Recommendations).
