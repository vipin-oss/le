# Deliverable 4 — Comprehensive Chapter-by-Chapter Outline

**Branch:** arena/40393d9f-le  
**Prepared:** 2026-10-21  
**Alignment:** Master Editorial Directive §15 (proposed manuscript architecture), §17 (scientific writing standards)  
**Reference model:** Abdalla et al. (2022) — executive summary, problem-driven hierarchy, methods before applications, constructive tone

---

## 0. Front Matter

- Title page
- Abstract (structured: background, scope, method, key findings, future directions)
- Keywords (6–8)
- Notation table (master symbol table with units and physical meaning) — **new, inspired by reference model Table 1**
- Acronym table — **new**

---

## 1. Review Scope and Purpose (Executive Summary)

**~3 pages**

1.1 What this review covers  
1.2 Why it matters (application landscape: smart structures, sensing, energy harvesting, NDE)  
1.3 How it is organized (section-by-section preview)  
1.4 Who it serves (beginning researcher, doctoral student, experienced scientist, journal reviewer)  
1.5 What it does NOT do (no adversarial fault-finding; no error audit of individual papers)  
1.6 Key open questions addressed (~8 bulleted questions, each mapped to a section)

---

## 2. Literature Strategy and Review Organization

**~5 pages**

2.1 Search strategy (databases, citation chaining, landmark tracing)  
2.2 Inclusion/exclusion criteria (Directive §3: relevance, clarity, provenance, history, reproducibility)  
2.3 Screening decisions (included/excluded/undecided counts)  
2.4 Full-text access status (open access vs. abstract-only)  
2.5 Equation selection policy (Directive §8–§9: verification register, validity domains)  
2.6 How to read this review (paths for different reader types)  
2.7 Limitations of the evidence base (abstract-only papers, paywalled journals, language restrictions)

---

## 3. Foundations of Continuum Wave Mechanics

**~15 pages** — Layer I of Directive §8 mathematical exposition

3.1 Kinematics: displacement, strain, rotation  
3.2 Conservation laws: linear momentum, angular momentum (symmetric stress)  
3.3 Mechanical power and internal energy (first law of thermodynamics)  
3.4 Entropy and dissipation inequality (Clausius-Duhem; Coleman-Noll restrictions)  
3.5 Constitutive principles: free energy potential, linear constitutive relations  
3.6 Classical elasticity: Navier equations, P-wave and SV-wave speeds  
3.7 Plane wave assumptions and harmonic wave form  
3.8 Energy flux in classical elasticity: Jᵢ = σⱼᵢvᵢ  
3.9 Interface conditions: perfect bonding (displacement and traction continuity)  
3.9.1 Imperfect bonding: spring-type conditions  
3.10 Notation summary for this section

**Open questions:** What is the most general form of energy flux that remains valid across all generalized theories?

---

## 4. Classical and Generalized Thermoelastic Theories

**~20 pages** — Layer II of Directive §8

4.1 Historical evolution: Biot (1956) → Lord–Shulman (1967) → Green–Lindsay (1972) → Green–Naghdi (1991)  
4.2 Classical coupled thermoelasticity (Fourier heat conduction)  
4.2.1 Governing equations  
4.2.2 Wave speeds: coupled longitudinal and thermal waves  
4.2.3 Infinite propagation speed paradox  
4.3 Lord–Shulman (1967): single relaxation time  
4.3.1 Modified heat equation: qᵢ + τ₀q̇ᵢ = −kT,ᵢ  
4.3.2 Finite wave speed; well-posedness condition τ₀ > 0  
4.3.3 Dissipation structure  
4.4 Green–Lindsay (1972): two temperatures  
4.4.1 Conductivity and thermodynamic temperatures  
4.4.2 Dissipationless wave propagation  
4.5 Green–Naghdi Type II (1991): dissipationless  
4.5.1 Thermal displacement gradient formulation  
4.5.2 Energy conservation (no dissipation)  
4.6 Green–Naghdi Type III (1991): dissipative  
4.6.1 Mixed character  
4.7 Dual-phase-lag (Tzou, 1995): two relaxation times  
4.7.1 τ_q ≥ τ_T condition for thermodynamic admissibility  
4.8 Three-phase-lag: three relaxation times  
4.9 Memory-dependent derivative models: integral-form relaxation  
4.10 Comparative table: theory × relaxation parameters × dissipation × wave speed  
4.11 Limiting cases (parameter substitutions → classical or other theories)  
4.12 Notation summary for this section

**Open questions:** What is the complete energy flux for LS, DPL, TPL, and MGT theories? How do limiting procedures behave under rigorous mathematical limits (not just parameter substitution)?

---

## 5. Coupled Multiphysics Continua

**~18 pages** — Layer III of Directive §8

5.1 Piezoelectricity: constitutive relations, coupling coefficients  
5.2 Piezothermoelasticity: three-field coupling (mechanical–thermal–electrical)  
5.3 Electrical boundary conditions: perfect contact, insulated (D₃ = 0), spring-type  
5.4 Porous media: voids, double porosity, pore-fluid coupling  
5.5 Micropolar and micromorphic continua: micro-rotation, couple stresses  
5.6 Semiconductor photo-thermo-elasticity: carrier diffusion, recombination  
5.7 Magneto-thermo-elasticity: magnetic field coupling  
5.8 Comparative table: theory × coupled fields × governing equations × interface conditions  
5.9 Notation summary for this section

**Open questions:** What is the electrical energy flux channel at piezoelectric interfaces? How do imperfect bonding conditions affect energy partition?

---

## 6. Generalized Transport and Memory Effects

**~15 pages** — Layer IV of Directive §8

6.1 Relaxation mechanisms: physical origin, mathematical representation  
6.2 Fractional operators: Caputo, Riemann–Liouville derivatives  
6.3 Hereditary integrals: convolution kernels, memory kernels  
6.4 Memory-dependent derivative: MDD operator and kernel function  
6.5 Energy flux in memory-dependent media: hereditary flux formulation  
6.6 Well-posedness and causality for memory-dependent models  
6.7 Comparative table: transport model × mathematical structure × dissipation × well-posedness  
6.8 Notation summary for this section

**Open questions:** What is the instantaneous energy flux in media with convolution-type memory? How is energy partitioned between storage and dissipation in hereditary media?

---

## 7. Nonlocal and Scale-Dependent Continuum Models

**~12 pages** — Layer VII of Directive §8

7.1 Nonlocal elasticity (Eringen): integral constitutive relations  
7.2 Strain-gradient theory: higher-order gradients  
7.3 Size-dependent wave behavior: dispersion from nonlocality  
7.4 Energy flux in nonlocal media: integral-form flux (divergence theorem modification)  
7.5 Interface conditions for nonlocal media  
7.6 Comparative table: nonlocal model × length scale × wave dispersion × energy flux form  
7.7 Notation summary for this section

**Open questions:** What is the correct energy flux at nonlocal interfaces? How do nonlocal boundary conditions differ from classical ones?

---

## 8. Mathematical Methods for Wave Propagation

**~12 pages** — Layer IV/V of Directive §8

8.1 Plane wave ansatz and harmonic time dependence  
8.2 Christoffel-type equations and wave speeds  
8.3 Secular equations and characteristic polynomials  
8.4 Complex wave numbers: propagating, evanescent, attenuating modes  
8.5 Modal normalization for energy flux computation  
8.6 Transform methods: Fourier, Laplace  
8.7 Spectral methods and numerical approaches  
8.8 Notation summary for this section

**Open questions:** How are complex modes consistently normalized for energy flux computation across theories?

---

## 9. Reflection, Transmission, and Interface Phenomena

**~18 pages** — Layer V of Directive §8

9.1 Interface geometry: two half-spaces, bonded or imperfectly bonded  
9.2 Wave decomposition: incident, reflected, transmitted modes  
9.3 Interface conditions: displacement, traction, temperature, heat flux, electric potential, displacement  
9.4 Scattering matrix formulation: ΔX = Q  
9.5 Secular equation and mode classification  
9.6 Number of boundary conditions vs. unknown amplitudes  
9.7 Energy ratios: reflected, transmitted, absorbed fractions  
9.8 Complex mode handling: evanescent and attenuating modes  
9.9 Reciprocity and symmetry of scattering matrix  
9.10 Notation summary for this section

**Open questions:** What is the correct number of interface conditions for each theory family? How do imperfect bonding conditions modify the scattering matrix?

---

## 10. Energy Transport and Dissipation

**~15 pages** — Layer VI of Directive §8

10.1 General energy balance: ∂ₜℰ + ∇·J = 𝒫 − 𝒟  
10.2 Classical energy flux: Jᵢ = σⱼᵢvᵢ + qᵢ  
10.3 Energy flux in generalized theories: model-specific formulations  
10.4 Interface energy balance: jump conditions, energy storage at interface  
10.5 Conservation identity: ΣR + ΣT + A = 1 (conditions for validity)  
10.6 Dissipation mechanisms: thermal relaxation, viscous, electrical, interface  
10.7 Thermodynamic admissibility: well-posedness, causality, positivity  
10.8 Comparative table: theory × energy flux form × dissipation mechanism × conservation validity  
10.9 Notation summary for this section

**Open questions:** Does ΣR + ΣT + A = 1 hold for generalized theories with symmetric flux definitions? What is the complete energy flux at multiphysics interfaces?

---

## 11. Advanced Theoretical Developments

**~10 pages** — Layer VII of Directive §8

11.1 Fractional-order continuum models  
11.2 Strain-gradient and couple-stress theories  
11.3 Emerging formulations with mathematical significance  
11.4 Limitations and open problems  
11.5 Notation summary for this section

---

## 12. Comparative Synthesis of Existing Research

**~20 pages** — Synthesis layer

12.1 Cross-theory comparison table (12 criteria × 9 theory families)  
12.2 Evidence trends by theory family  
12.3 Mathematical relationships: limiting cases and specializations  
12.4 Contradiction mapping: where studies disagree and why  
12.5 Model comparability: conditions under which theories can be compared  
12.6 Notation summary for this section

---

## 13. Applications of Multiphysics Wave Mechanics

**~10 pages**

13.1 Smart structures and adaptive materials  
13.2 Nondestructive evaluation and sensing  
13.3 Energy harvesting and conversion  
13.4 Geophysics and seismology  
13.5 Biomedical applications (ultrasound, thermal therapy)  
13.6 Evidence map: which applications have peer-reviewed support  
13.7 Notation summary for this section

---

## 14. Original Multidimensional Research Taxonomy

**~12 pages**

14.1 Five-axis taxonomy (physical, mathematical, wave, energy, validation)  
14.2 Application to the evidence base (24+ records classified)  
14.3 Empty cells: research gaps identified by taxonomy  
14.4 Contradiction mapping: pairs of studies with contradictory approaches  
14.5 Advantages over single-axis classifications  
14.6 Limitations (analyst-constructed, abstract-only classifications)

---

## 15. Major Scientific Challenges

**~10 pages** — Constructively framed (Directive §12)

15.1 Energy flux formulation across theory families  
15.2 Conservation verification at multiphysics interfaces  
15.3 Numerical benchmarks and validation  
15.4 Experimental validation  
15.5 Complex mode handling  
15.6 Nonlocal interface energetics  
15.7 Memory-dependent energy flux  
15.8 Each challenge: existing foundation → why important → what achieved → what remains open → approaches → obstacles

---

## 16. Future Research Opportunities

**~12 pages**

16.1 Coupled-field modeling in emerging materials  
16.2 Mathematically consistent generalized transport  
16.3 Multiscale wave phenomena  
16.4 Nonlocal and hereditary continuum interactions  
16.5 Advanced interface conditions  
16.6 Multiphysics mode conversion  
16.7 Reproducible numerical benchmarks  
16.8 Experimental validation  
16.9 Inverse material characterization  
16.10 For each direction: foundation → importance → achieved → open → approaches → relevance → obstacles

---

## 17. Conclusions and Scientific Outlook

**~5 pages**

17.1 Synthesis of major established insights  
17.2 What is well established vs. what remains open  
17.3 The role of constructive synthesis vs. adversarial criticism  
17.4 Final outlook: next decade of research in multiphysics continuum mechanics

---

## 18. References

---

## 19. Appendices (supplementary material)

- Appendix A: Equation verification register  
- Appendix B: Detailed derivation of classical balance laws  
- Appendix C: Benchmark specifications (BM-1 through BM-5)  
- Appendix D: Figure specifications  
- Appendix E: Table specifications  
- Appendix F: Reproducibility statement (scripts, data)

---

## Estimated Page Count

| Section | Pages |
|---------|-------|
| Front matter + notation | 4 |
| 1. Scope and purpose | 3 |
| 2. Literature strategy | 5 |
| 3. Foundations | 15 |
| 4. Thermoelastic theories | 20 |
| 5. Multiphysics continua | 18 |
| 6. Transport and memory | 15 |
| 7. Nonlocal models | 12 |
| 8. Mathematical methods | 12 |
| 9. Interface phenomena | 18 |
| 10. Energy and dissipation | 15 |
| 11. Advanced developments | 10 |
| 12. Comparative synthesis | 20 |
| 13. Applications | 10 |
| 14. Taxonomy | 12 |
| 15. Challenges | 10 |
| 16. Future opportunities | 12 |
| 17. Conclusions | 5 |
| References | 10 |
| Appendices | 15 |
| **Total** | **~215 pages** |

**Note:** This is Version B (extended authoritative review). Version A (journal-focused) would target 60–90 pages by condensing sections 4–10 and moving appendices to supplementary material.

---

## Reader Paths

| Reader type | Recommended path |
|-------------|-----------------|
| Beginning researcher | Sections 1–3, notation table, Section 17 |
| Doctoral student | Sections 3–10, Appendix A–C, Section 16 |
| Experienced scientist | Sections 12–16, taxonomy, future roadmap |
| Journal reviewer | Sections 1–2, 12, 16–17, equation register |

---

**Next:** Proceed to Deliverable 5 (Subsection-Level Mathematical Content Plan).
