# Applied Mechanics Reviews - Editorial Inquiry Draft

**Status:** Draft only; no submission and no editor contact.<br>
**To:** [EDITOR TO BE VERIFIED]<br>
**Subject:** Scope inquiry for a critical review of coupled wave dynamics<br>
**Proposed working title:** *Coupled Wave Dynamics in Continuous Media: Constitutive Frameworks, Multiphysics Interactions, Model Admissibility, and Reproducible Benchmarks*

Dear [EDITOR TO BE VERIFIED],

I am developing a critical, physics-aware review of coupled wave dynamics in continuous media, with heat conduction as a major organizing theme. It connects constitutive choices to thermoelastic and multiphysics wave behavior, admissibility, and evidence for model selection or validation. It would compare classical and generalized thermoelasticity with memory, nonlocal, porous, viscoelastic, piezoelectric, magnetic, and coupled-field models. Exact delays, truncations, admissibility, causality, and physical validation would remain distinct questions.

The applied-mechanics focus is model choice for a specified medium and geometry. Planned coverage spans bulk, surface, interface, guided, and layered waves, coupled fields, and limits of bulk-dispersion predictions in finite domains. The five batch-002 target papers checked at R3 already cover substantial parts of this area. Shakeriaski et al. (2021, *Journal of Computational Design and Engineering*) review generalized thermoelastic models; Joseph and Preziosi (1989, *Reviews of Modern Physics*) discuss heat-wave propagation and memory kernels; Azhdari et al. (2026, *International Journal of Thermal Sciences*) review phase-lag evidence in bio-heating. El-Karamany and Ezzat (2016, *Applied Mathematical Modelling*) give a unified heat-flux and transport formulation with model-specific thermodynamic restrictions, while Zenkour and El-Mekawy (2020, *International Communications in Heat and Mass Transfer*) analyze a refined phase-lag model with a beam calculation. The earlier R3 staging set also includes Chandrasekharaiah (1998, *Applied Mechanics Reviews*) and Green and Naghdi (1993, *Journal of Elasticity*).

Within those five batch-002 papers, we did not identify a shared, independently verifiable benchmark registry across the model families. The 2020 beam example compares model predictions rather than measured data. The 2016 paper does derive entropy-production restrictions for several Green-Naghdi and related cases; the planned review would incorporate that analysis, compare its assumptions with a wider model set, and avoid presenting admissibility as an unaddressed topic. The proposed focus is a common-convention comparison joined to benchmark protocols, with code verification kept separate from physical validation. These observations are limited to the checked R3 sample, not a claim about the whole literature.

**Current status - EXISTS:** the workspace contains a 134-page `main.pdf`. The available source package includes a review-format 12pt source file and scripts named `bench_schemes.py` and `bench_laplace.py`. File presence alone does not establish that the current results have been independently checked.<br>
**Current status - PLANNED:** a P1 integrity audit and independent script runs; a benchmark registry with reference solutions, parameter domains, tolerances, and inputs; comparative admissibility and parameter-identifiability tables; broader experimental-evidence assessment; and independent specialist reading.

The opened AMR author-information page says the journal is open to unsolicited contributions and recommends an editor proposal with a title, abstract, and likely timeline; it directs authors to the general ASME journal guidelines for format. Would an extended critical review with this scope be suitable for AMR? What length and format do you prefer, and would you advise changing the balance among thermal-wave theory, coupled fields, and verification? The journal-specific page opened for this inquiry does not state a review-article length, so guidance on length would be especially useful.

This document is an editorial-inquiry draft only. No manuscript has been submitted, and no editor has been contacted.

Sincerely,<br>
Vipin Gupta
