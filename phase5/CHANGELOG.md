# Changelog — phase5 v1.1 working copy

This records substantive phase5 changes relative to the preserved phase4/v1.0 source. It is not a claim that all changes are correct or fully validated. See `reports/equation-audit.csv`, `reports/scientific-audit.md`, and `reports/build-status.md` for evidence status.

## v1.1 source-audit (in progress)

### Added

- Versioned `phase5/master/` working copy and explicit source/PDF provenance record; preserved phase4 source and baseline PDF unchanged.
- Portable local table and figure directories, 18 generated vector PDF renditions from inherited editable SVGs, vector conversion and structural validation scripts.
- Fail-fast `latexmk` build configuration, log checker, static label/citation/asset inventory script, strict CI workflow, and baseline PDF thumbnail generator.
- Equation, figure/source/licence, literature evidence, build, provenance, quality-gate, and scientific audit registers.
- Generic article and separate supplement wrappers, explicitly not journal-specific or compiled.

### Corrected or narrowed

- Classical total energy now distinguishes specific internal energy from volumetric energy density.
- Classical outward-positive Cauchy flux is stated with consistent indices and sign: `J_i = q_i - sigma_ij v_j`; the harmonic mechanical average uses `-1/2 Re[sigma_hat_ij v_hat_j*]`, with heat flux separate and convention stated. Corrected product-rule/divergence contractions in the mechanical-energy derivation to avoid free/dummy-index mismatches.
- Lord–Shulman, Green–Lindsay, piezoelectric quasi-electrostatic modes, piezoelectric effective stiffness, nonlocal dispersion, evanescent-wave flux, and fully dynamic thermoelasticity descriptions were revised or narrowed; see the evidence register for limits.
- Universal generalized/nonlocal flux and family-wide dissipation/admissibility assertions were withdrawn where no model-specific derivation was available.
- TPL formula was withheld rather than replaced with an unverified form; MGT and MDD equations are labelled source leads with assumptions/checks open.
- Fractional scalar equation coefficient changed to `a_alpha`, with dimensions stated for the shown equation; wording now distinguishes the scalar diffusion-wave model from a complete coupled thermoelastic theory.
- Clarified notation collisions between Green–Naghdi thermal displacement and fractional order, and between the MDD time horizon and angular frequency.
- Recast the spring-interface relation using an explicitly named stiffness tensor and its compliance, correcting the limiting-condition interpretation; passivity/source validation remains open.
- Withheld placeholder nonlocal-correction and candidate piezoelectric electrical-flux equations from the generalized energy appendix; both remain OPEN pending model-specific derivation.

### Not completed

- No phase5 LaTeX build, final PDF, final text extraction, final-page visual inspection, font/overfull-box report, or clean compile log.
- No complete primary-source equation verification, literature claim/citation relevance audit, theorem attribution audit, independent benchmark, table-by-table transcription review, or journal-specific adaptation.
- Several inherited appendices, tables, equations, and legacy evidence labels remain to be reconciled.
- The repository baseline is 161 pages; the separately described 170-page/pdfTeX-1.40.29 PDF is unavailable.
