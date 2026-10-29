# Deliverable 1 — Reference Review Structural Analysis: Abdalla et al. (2022)

**Source:** Abdalla et al., "Cosmology Intertwined: A Review of the Particle Physics, Astrophysics, and Cosmology Associated with the Cosmological Tensions and Anomalies," J. High En. Astrophys. 2204, 002 (2022); arXiv:2203.06142v3 (224 pages, 27 figures, ~100+ tables/equations, 203+ authors).

**Prepared:** 2026-10-21  
**Branch:** arena/40393d9f-le  
**Purpose:** Analyze the scholarly structure of the reference review to identify transferable practices for a continuum mechanics review.

---

## 1. Introduction Strategy (Section I–II)

### 1.1 How the introduction motivates a large interdisciplinary field

- **Executive Summary first** (Section I): A standalone ~1-page summary states the paper's purpose (SNOWMASS 2021 white paper), its scope (cosmological tensions), its method (community-organized, section-by-section), and its audience (funding agencies, researchers, policymakers).
- **Introduction** (Section II): Opens with the accelerating expansion discovery, then presents the standard ΛCDM model's successes, then its failures (dark energy, dark matter, inflation unexplained). The narrative arc is: **standard model works → but cracks appear → tensions emerge → new physics may be needed**.
- **Key questions are listed explicitly** (bulleted, ~15 questions), giving the reader a roadmap of what the review will address.
- **Scale:** The introduction is substantive (~15 pages), not a brief preamble. It establishes why the field matters before diving into details.

### Transferable practice

Open with a standalone "Executive Summary" or "Scope and Purpose" that states: what the review covers, why it matters, who it serves, and how it is organized. Then use the Introduction to trace the field's historical arc from classical success to contemporary anomalies.

---

## 2. Section Hierarchy (Sections I–X)

### 2.1 Top-level structure

| Section | Title | Function |
|---------|-------|----------|
| I | Executive Summary | Standalone purpose, scope, method, audience |
| II | Introduction | Motivation, historical context, key questions |
| III | Quantification of "Tensions" and Model Comparison | Statistical framework — how to measure disagreement |
| IV | The H₀ Tension | Deep dive: one specific tension, all measurement methods |
| V | The S₈ Tension | Deep dive: second tension, all measurement methods |
| VI | Other Measurements and Systematics | BAO, age, GW standard sirens, redshift drift, etc. |
| VII | Cosmological Models Proposed to Solve the Tensions | Early-universe, late-time, modified gravity models |
| VIII | Challenges for ΛCDM Beyond H₀ and S₈ | Closed universe, anomalies, dipoles, etc. |
| IX | Stepping Up to the New Challenges | Future experiments, facilities, road ahead |
| X | Conclusions | Synthesis and outlook |

### 2.2 Subsection depth

Sections go up to 4 levels deep (e.g., VII.5.10 → "VII.5 Late-Time Alternative Proposed Models → VII.5.10 Quintessence Models and their Various Extensions"). Each section has **coordinators and contributors listed**, making authorship transparent.

Each subsection follows a pattern:
1. **Physical setup** — what is being measured/modeled
2. **Mathematical formulation** — key equations with equation numbers
3. **Empirical results** — values, uncertainties, significance levels
4. **Systematics** — what could go wrong
5. **Comparison** — how different methods agree/disagree
6. **Figures** — whisker plots, constraint contours, comparison diagrams

### Transferable practice

Use a **problem-driven hierarchy**: each major section addresses a specific open question or tension, not just a list of papers. Within each section, move from measurement → theory → comparison → systematics → future. Number equations sequentially within the manuscript (not per section).

---

## 3. Background → Advanced Transition

### 3.1 How theory transitions into advanced problems

- **Section III** (Quantification) provides the mathematical tools (Bayesian evidence, tension metrics, χ², information criteria) **before** the deep dives. This is "methods first, applications second."
- **Sections IV–VI** apply these tools to specific tensions, showing how different measurement techniques (distance ladder, CMB, BAO, GW, etc.) produce conflicting values.
- **Section VII** then presents **proposed solutions** — alternative models that could resolve the tensions. Each model gets: physical motivation, mathematical formulation, empirical assessment, limitations.
- **Section VIII** presents **remaining challenges** — anomalies that no proposed model fully explains.
- **Section IX** looks **forward** — what facilities and methods will resolve these questions.

### Transferable practice

Structure the continuum mechanics review as: **foundations → measurement/modeling methods → specific problems (interfaces, wave types, couplings) → proposed theoretical solutions → remaining challenges → future directions.** Do not present theories in isolation; present them as responses to specific physical problems.

---

## 4. Mathematical Equation Usage

### 4.1 How equations are used

- Equations are **numbered sequentially** across the whole manuscript (Eq. 1, Eq. 2, ..., Eq. 141).
- Each equation is **introduced with physical context**, stated, then **interpreted** (what the terms mean, what the result implies).
- Key equations are **referenced back to** throughout (e.g., Eq. 4 for look-back time is cited in multiple sections).
- **Tables of notation** (Table 1) and **acronyms** (Table 2) appear early, giving readers a reference.
- **Model equations are presented comparatively** — e.g., different dark energy models each get their own equation showing how they modify the background evolution.

### Transferable practice

- Number all major equations sequentially through the manuscript.
- Provide a **notation table** early (symbols, units, physical meaning).
- Each equation: context → statement → interpretation → citation.
- Present competing model equations side by side to highlight structural differences.

---

## 5. Figure Strategy

### 5.1 How figures contribute to understanding

- **27 figures** across 224 pages (~1 figure per 8 pages).
- Figure types:
  - **Whisker plots** (Fig. 2): H₀ values from different probes with error bars — immediate visual comparison.
  - **Constraint contours** (Fig. 5): tensor-to-scalar ratio vs. spectral index, showing model exclusion regions.
  - **Systematic effect plots** (Fig. 3): δH₀/H₀ vs. redshift and scale.
  - **Reference figures** (Fig. 1): posterior odds vs. tension significance.
- Every figure has a **detailed caption** explaining what is shown, what data source, what it means.
- Figures are **referenced in text** at the point of discussion ("see Fig. 2").
- Figures are **original** (not copied from other papers) or clearly attributed.

### Transferable practice

- Target ~1 figure per 8–10 pages of content.
- Each figure must answer a specific scientific question (comparison, constraint, systematic effect).
- Use whisker plots for parameter comparison across methods/studies.
- Use contour plots for model exclusion/inclusion regions.
- Captions must be self-contained (understandable without reading main text).

---

## 6. Literature Integration

### 6.1 How literature is integrated into explanatory arguments

- **Inline citation numbers** ([23], [24], etc.) — not parenthetical author-year.
- Citations are **woven into the narrative**: "The latest SH0ES measurement gives H₀ = 73.04 ± 1.04 [45], a 5σ disagreement with the CMB one."
- **Reference list is comprehensive** (~2300+ references) — the paper is a Snowmass white paper with massive community input.
- **Comparative language**: "both surveys find values that are ~2–3σ smaller," "results are similar across various analysis choices."
- **No adversarial language**: models are presented as "proposed solutions," "alternative formulations," "extensions" — never as "wrong" or "erroneous."

### Transferable practice

- Use inline numeric citations for readability.
- Integrate citations into explanatory sentences, not just as end-of-sentence drops.
- Use comparative language throughout ("under assumption X, model Y predicts Z").
- Never frame individual papers as erroneous; frame differences as assumptions, approximations, or model-specific validities.

---

## 7. Complementary and Competing Theories

### 7.1 How competing models are presented

- **Section VII** presents ~15 different model families (early dark energy, NEDE, bulk viscosity, chameleon, modified gravity, varying G, vacuum metamorphosis, etc.).
- Each model subsection follows the same template: motivation → equations → empirical assessment → limitations → references.
- **Comparative language dominates**: "Model X reduces the tension but worsens the fit to low-redshift data," "Model Y has fewer parameters but does not ease both tensions."
- **No model is declared the winner**: the conclusion states that the resolution "will likely require a coordinated effort from theory and data."

### Transferable practice

- Present each continuum mechanics theory with a consistent template: physical motivation → governing equations → wave propagation characteristics → interface behavior → energy flux → limitations.
- Compare theories explicitly: "LS theory gives finite wave speed but requires τ₀ > 0 for well-posedness," "GN II is dissipationless but does not model attenuation."
- Never declare one theory superior; present applicability domains.

---

## 8. Organization Without Losing Coherence

### 8.1 Structural coherence mechanisms

- **Executive Summary** (Section I) gives the big picture upfront.
- **Key questions** (Section II) are listed and then each is addressed by a specific later section.
- **Methods section** (Section III) comes before applications, so readers have tools to evaluate the results.
- **Cross-references** between sections are explicit ("see Sec. VII.8," "as discussed in Sec. III.2").
- **Notation table** (Table 1) and **acronym table** (Table 2) ensure consistent symbols.
- **Experiment table** (Table 3) and **science-facility matrix** (Table 4) organize the future-looking material.

### Transferable practice

- Start with an executive summary that previews the whole review.
- List key open questions early; map each to a section that addresses it.
- Use cross-references liberally to connect related material.
- Maintain a master notation table and acronym list.
- Use synthesis tables (theory × property, method × application) to organize comparative material.

---

## 9. Open Questions and Future Research

### 9.1 How open questions are identified

- **Section II** lists ~15 key questions (nature of dark matter, nature of dark energy, inflation, gravity at horizon scale, etc.).
- **Section IX** ("Stepping Up to the New Challenges") presents future investigations organized by science topic and facility (Table 4 maps science to experiments).
- **Section X** (Conclusions) synthesizes: what would resolve the tensions, what experiments will decide, what theoretical work remains.
- Each open question includes: why it matters, what has been tried, what remains, what approach could work.

### Transferable practice

- End each major section with "Open questions" specific to that topic.
- End the review with a "Future research roadmap" organized by approach (theory, computation, experiment) and timeline.
- Map research directions to specific methods (analytical derivation, numerical benchmark, experimental validation).

---

## 10. Transferable vs. Non-Transferable Practices

| Practice | Transferable? | Adaptation for Continuum Mechanics |
|----------|---------------|------------------------------------|
| Executive summary | YES | 1-page scope, purpose, audience statement |
| Problem-driven hierarchy | YES | Sections organized by physical problem (interface, wave type, coupling) |
| Methods before applications | YES | Mathematical foundations (balance laws, energy flux) before specific models |
| Sequential equation numbering | YES | Number all major equations through manuscript |
| Notation/acronym tables | YES | Master symbol table with units and physical meaning |
| Whisker/comparison figures | YES | Energy ratio comparison across theories and incidence angles |
| Consistent model template | YES | Each theory: motivation → equations → waves → interfaces → energy → limitations |
| Coordinators/contributors listed | N/A | Single-author or small-team review; not applicable |
| ~2300 references | NO | Target ~150–300 carefully selected references |
| 224 pages | NO | Target 40–80 pages depending on journal |
| Snowmass white paper format | NO | Adapt to standard journal review article format |
| Community brainstorming | N/A | Not applicable; use literature synthesis instead |

---

## 11. Summary of Structural Practices to Adopt

1. **Executive Summary** → "Review Scope and Purpose" (standalone, ~1 page)
2. **Introduction with key questions** → Historical arc from classical elasticity to generalized multiphysics continua; list ~10 open questions
3. **Methods section** → Mathematical foundations (balance laws, energy flux, interface conditions)
4. **Problem-specific deep dives** → Each major physical problem gets its own section (thermoelastic interfaces, piezoelectric coupling, porous media, etc.)
5. **Model comparison sections** → Each theory family presented with consistent template
6. **Notation and acronym tables** → Master symbol table early in manuscript
7. **Comparison figures** → Whisker plots for energy ratios, contour plots for wave speeds/dispersion
8. **Open questions per section** → End each section with topic-specific open questions
9. **Future research roadmap** → Organized by theory/computation/experiment
10. **Constructive, non-adversarial tone** → Differences framed as assumptions, not errors

---

**Next:** Proceed to Deliverable 2 (Revised Scientific Scope Statement).
