# Physics Reports - Preliminary Review Proposal Draft

**Editor:** [EDITOR TO BE VERIFIED]<br>
**Working title:** *Coupled Wave Dynamics in Continuous Media: Constitutive Frameworks, Multiphysics Interactions, Model Admissibility, and Reproducible Benchmarks*<br>
**Status:** Preliminary draft only; not sent.

The Physics Reports author guide describes invited articles and says that editors welcome suggestions. It asks for a review proposal of approximately 500-1,000 words and requires the intended editor to be specified. The guide distinguishes regular reports, generally more than 50 journal pages, from Rapid Reviews, which target about 20 journal pages. The editor field remains a placeholder; the 134-page custom-format manuscript is not equated with journal pages.

## Scope and motivation

The proposed review would examine how heat transport, mechanical deformation, and additional material fields combine to support or alter wave propagation in continua. Finite-speed heat transport and second sound motivate the organizing thread; relaxation kernels and memory effects connect constitutive choices to transient response. The physics motivation is fundamental as well as applied: transport and memory assumptions shape the balance and constitutive structure, dispersion, attenuation, and interpretation of predicted modes. Piezoelectric, magnetic, porous, viscoelastic, micropolar, semiconductor, and nonlocal settings would be included where they address the planned questions about admissibility, model selection, and verification. The purpose is to distinguish physically supported behavior from consequences of a chosen constitutive law, approximation, boundary condition, or numerical procedure.

## Existing literature and intended focus

The R3 papers staged for this task include Joseph and Preziosi (1989, *Reviews of Modern Physics*) on heat-wave transmission and memory kernels; Green and Naghdi (1993, *Journal of Elasticity*) on thermoelasticity without energy dissipation; Chandrasekharaiah (1998, *Applied Mechanics Reviews*) on hyperbolic thermoelasticity; Shakeriaski et al. (2021, *Journal of Computational Design and Engineering*) on generalized thermoelastic models; Azhdari et al. (2026, *International Journal of Thermal Sciences*) on phase-lag evidence in bio-heating; El-Karamany and Ezzat (2016, *Applied Mathematical Modelling*) on phase-lag Green-Naghdi formulations and restrictions; and Zenkour and El-Mekawy (2020, *International Communications in Heat and Mass Transfer*) on a refined multi-phase-lag model.

Within the five batch-002 target papers, combined constitutive formulations and limiting cases are already present. El-Karamany and Ezzat derive model-specific entropy-production restrictions for Green-Naghdi and related cases, so the planned synthesis would incorporate that work rather than imply that admissibility analysis is absent. The checked five do not identify a shared, independently verifiable benchmark registry spanning their model families; the Zenkour and El-Mekawy beam example is a comparison among model predictions, not measured validation. The proposed focus is to place existing restrictions beside their stated assumptions and to connect each future comparison to a benchmark with traceable inputs and a stated reference. These observations are restricted to the R3 papers checked for P0-a and are not a claim about all prior work.

## Planned structure

The review would follow the eight parts in the frozen blueprint:

1. **Part I - Scope and questions:** research questions, comparison with checked reviews, and search method.
2. **Part II - Fundamental theory:** balance and constitutive descriptions, thermodynamics, causality, dimensional analysis, and an admissibility matrix.
3. **Part III - Thermal-wave models:** classical, Lord-Shulman, Green-Lindsay, Green-Naghdi, Cattaneo, dual- and three-phase-lag, Moore-Gibson-Thompson, Guyer-Krumhansl, fractional, and memory models.
4. **Part IV - Mathematical wave framework:** operators, validity conditions, branches, attenuation, stability, boundaries, and interfaces.
5. **Part V - Wave geometries:** bulk, surface, interface, guided, layered, periodic, and scattering problems.
6. **Part VI - Coupled material physics:** piezoelectric, magnetic, porous, viscoelastic, micropolar, nonlocal, and semiconductor settings.
7. **Part VII - Verification and evidence:** analytic checks, numerical convergence, experiments, parameter identification, uncertainty, and inverse problems.
8. **Part VIII - Critical synthesis:** model-selection guidance, a problem atlas, benchmark registry, controversy table, and open questions.

## Mathematical, experimental, and reproducibility plan

The analysis would distinguish constitutive laws from balance laws; exact delays and hereditary kernels from truncated expansions; bulk dispersion from surface or interface conditions; and thermodynamic admissibility from causality, stability, and well-posedness. Experimental reports would be classified by evidence type and regime. Phase-lag values would be treated as quantities requiring identifiability and uncertainty assessment, not as universal constants.

A benchmark registry is planned, not yet assembled. Each record would identify the tested quantity, reference solution, parameter domain, error measure, precision, tolerance rationale, inputs, and computational environment. Candidate cases would be retained only when a reference and assumptions can be checked. Code verification would be reported separately from physical validation; the presence of scripts alone would not count as either.

## Status, readership, and assessment

**EXISTS:** the workspace contains a 134-page `main.pdf`; the available source archive includes a review-format 12pt source file and scripts such as `bench_schemes.py` and `bench_laplace.py`. The P1 integrity audit and independent script runs have not yet been performed. P0-a batches 001 and 002 are being used as staging evidence, and this proposal relies only on their R3 rows.<br>
**PLANNED:** expansion of the admissibility comparison, benchmark registry, evidence review, and problem atlas.

The intended readership includes researchers in continuum mechanics, thermal and condensed-matter physics, wave physics, applied mathematics, numerical methods, and experimental thermal transport. After the integrity audit, the plan is to seek two or three independent expert readings spanning continuum thermodynamics, elastic or guided waves, and numerical or experimental wave research. Names remain to be identified by the author; this draft makes no contact with an editor or reviewer.

This is a preliminary proposal draft only. It has not been sent to the journal.

**Word count:** 885 words for the draft text above, including headings and editor placeholder; excludes this count line.
