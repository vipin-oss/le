# Recovery state — heat-model exploratory advice 03

Date: 30 September 2026. Previous cumulative state: `PROJECT_STATE_READING_02.md`; detailed literature and code reading reports remain accessible.

## New user objective

User wants one paper on a recent heat-conduction model, analysed for materials with a different type of symmetry. The user refers to a previously shared Google link, but no exact base-paper title/Sr. No. is identified. In the clarification UI the user explicitly chose BOTH crystal/material and geometric symmetry, and COUPLED THERMOELASTIC RESPONSE. This establishes the desired scope, not final approval of a specific model/material/geometry.

Authorization: initial suggestions and current literature checking. No final direction, detailed model, numerical execution or submission is approved. This is not a completed formal 8–10-direction Phase 0A-1 or closest-five Phase 0A-2.

## Background retained

- User's Excel contains 48 entries / 47 distinct supplied DOI strings; duplicate IDs 36/41 and proposed DOI correction for ID47 are recorded in earlier reports.
- Eight representative published PDFs and all eight supplied unpublished PDFs had section-level initial reading, not exhaustive audits.
- Corpus already covers MGT/MDD/KG, coupled wave mechanics, strain-gradient/BFS, nonlinear/electromechanical topics, GK inverse identifiability and QC phason model discrimination. Future novelty must compare against both published and unpublished work.
- FEM4 MATLAB package has a static 2D electromechanical/strain-gradient solver: C1 BFS mechanical fields, C0 potential, 36 element DOFs. It does not already implement thermal transport/dynamics. Core source was inspected, not executed; neither MATLAB nor Octave was found in the workspace.
- Original inputs/code are unchanged. Static hcrit factor-of-two note and other scoped concerns are in `CODE_REVIEW/FEM4_PACKAGE/CODE_OVERVIEW.md`.
- User hardware, licences, compute budget, timeline and experimental access remain unknown.

## New literature anchors

1. Huang et al. (2025), *New insights on generalized heat conduction and thermoelastic coupling models*, DOI 10.1007/s10483-025-3280-7: recent generalized CV/GN formulations; metadata/abstract inspected, full equations unavailable in this attempt (subscription preview/journal fetch failure). Do not invent the model operators.
2. Dragasevic/Rajkov/Simoncelli (2026), PRL 136,186302, DOI 10.1103/nbbn-56hr: VHE applied to graphite/hBN backflow, vortices and temperature resonances. Publisher text chunks0–2 read. PDF download403, math extraction incomplete. VHE framework itself dates to PRX10,011019 (2020), not invented in2026.
3. Monoclinic beta-Ga2O3: 2025 PRB111,094308 and 2018 APL113,232105 provide current physical context/measured conductivity tensor. Conductivity does not determine generalized-model relaxation parameters.
4. BP: 2015 few-layer directional-conductivity measurements and 2018 Science Advances eaat3374 low-temperature Poiseuille observations. Avoid mixing incompatible temperature/sample regimes. Required VHE viscosity/collision tensor data not established.
5. Gamma/beta Ga2O3: 2024 APL Materials12,081108, DOI10.1063/5.0213985 already studies polymorph/interface transport. Not a new gap by itself; phase differences include more than symmetry, and complete material/dynamic inputs require investigation.

## Preliminary options — all GAP NOT CONFIRMED

A. Recent generalized CV/GN model in monoclinic beta-Ga2O3: symmetry-constrained directional transient response and model discrimination.
B. VHE in a low-symmetry candidate such as BP: distinguish anisotropic Fourier signatures from non-Fourier/hydrodynamic backflow, with graphite/hBN only as already-studied reference cases.
C. Generalized non-Fourier response at cubic–monoclinic gamma/beta Ga2O3 interfaces: distinguish memory from interface resistance, subject to data/overlap blockers.

None is selected or approved. No arbitrary scores, novelty guarantees or Q1 claims are made.

## Important analytical planning observation

For constant diagonal 2D conductivity, qx=-kx*T_x and qy=-ky*T_y imply (curl q)_z=(kx-ky)*T_xy. Therefore vorticity alone is not a universal hydrodynamic diagnostic. For symmetric positive-definite local K, q dot grad(T)=-grad(T)^T K grad(T)<=0. These elementary identities are not claimed as novel results; quantitative diagnostic novelty would require investigation. Non-Fourier behavior is not uniquely proof of hydrodynamics; ballistic alternatives must be considered.

## Current evidence/execution status

- Search: preliminary live search completed; exact queries and retained/excluded sources logged.
- Full source-equation reconstruction: pending.
- Closest-five/scooping/gap confirmation: not completed.
- Parameter provenance/calibration and physical validation: not established for a new project.
- Model derivation/code/tests/production: NOT_RUN / NOT_STARTED.
- Journal status: not checked.

## Exact next action

Clarifications are resolved: BOTH material/crystal and geometric symmetry, COUPLED THERMOELASTIC RESPONSE. Agent provisionally recommends shortlisting the 2025 generalized CV/GN family + monoclinic beta-Ga2O3 + circular/elliptical cavity symmetry-mismatch problem; user has not approved that exact direction. Wait for explicit shortlist approval and/or the intended Google Drive paper title/Sr. No. Obtain readable exact equations, broaden literature/closest-paper comparison and inspect full material/benchmark availability before final problem approval. Do not execute simulations automatically.

## Recovery artifacts

- `/home/user/HEAT_MODEL_EXPLORATION/HEAT_MODEL_OPTIONS.md` — initial options and evidence boundaries.
- `/home/user/HEAT_MODEL_EXPLORATION/THERMOELASTIC_DIRECTION_NOTE.md` — current focused provisional recommendation, user scope and approval/evidence gates.
- `/home/user/HEAT_MODEL_EXPLORATION/SEARCH_LOG.md` — twelve exact searches, inspection depth and exclusions.
- `/home/user/RESEARCH_READING/PROJECT_STATE_READING_02.md`, `READING_REPORT.md`, `READING_STATUS.csv` — prior corpus/context.
- `/home/user/CODE_REVIEW/FEM4_PACKAGE/CODE_OVERVIEW.md` and associated source/traceability inventory — existing code context.

No new numerical outputs, approved scientific direction or cumulative final-research package exists.
