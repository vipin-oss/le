# PHYSICAL_VALIDATION_PLAN — Phase 2 (scientific non-applicability record)
Date: 30 September 2026.

## Status: NOT_AVAILABLE — with scientific reason (not convenience)
1. No experimental transient thermoelastic dataset for β-Ga2O3 (or any monoclinic crystal) around a cavity was located in the bounded live search (SEARCH_LOG.md). The measured literature provides constitutive inputs only (elastic tensor, conductivity, expansion) — these are used as MODEL INPUTS, not as validation targets (validating a solver against its own inputs is not validation).
2. No author code or benchmark package for the target problem exists in the supplied corpus (user corpus = heat-model papers, FEM4 electromechanical code, Huang/Bagri/Gordeliy sources — none is a 2D anisotropic cavity benchmark).
3. Retrospective physical validation via the pilot source case (Huang-2025 Fig.5) is verified code-family evidence, but a DIFFERENT problem (1D slab, Cu, nondimensional) — cannot validate the cavity geometry claims.

## Consequence (recorded, per §13)
- Claims will say "verified computation within a documented model", never "physically validated".
- Material parameters use real measured data where verified; the study's conclusions about orientation/shape/memory interactions are model-conditional.
- A physical-validation pathway for the FUTURE: measured thermal-shock stress/curvature on a β-Ga2O3 single-crystal plate with lithographed circular vs elliptical holes (e.g., by Raman/thermoelastic stress analysis) — described in manuscript as recommended future validation, not performed.

## Where validation WAS achieved (documented, different scope)
- Huang-2025 source-case reproduction (PILOT_HUANG_2025_01): source-figure comparison 175/177 points within envelope — mathematical source-case reproduction of the heat-model family, retained as code-family precedent.
