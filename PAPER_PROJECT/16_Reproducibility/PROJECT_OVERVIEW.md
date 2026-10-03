# PROJECT_OVERVIEW

**Repository:** `vipin-oss/le`, project directory `PAPER_PROJECT`, run under the project's own
MASTER_PROMPT v2.1 (a copy is at `07_DOCUMENTATION/program_control/MASTER_PROMPT.md`).
**Title as submitted:**

> Orientation-dependent wall stress around circular and elliptical cavities in monoclinic β-Ga₂O₃ under a transient thermal pulse: a verified continuum study with thermal-memory and mechanism ablations

## The one-paragraph version

A transient thermal pulse is applied to the wall of a microscopic cavity (circular, and an equal-area
ellipse with aspect ratio chi = 2) in the a-c plane of monoclinic beta-Ga2O3. Heat conduction is
solved in the frequency domain with Fourier, Lord-Shulman and a two-relaxation-time (MCV3) kernel,
inverted by a Bromwich contour integral, and fed to a coupled thermoelastic solve on a mapped
grid; the reported quantity is the peak compressive hoop stress on the cavity wall as a function of
crystal orientation. The finding is that the anisotropic stiffness and the anisotropic expansion
together modulate that peak by about 30 per cent with orientation, that thermal memory reshapes
rather than rescales it, and that every step is verified against a closed-form solution and an
independent implementation. No experimental comparison is claimed - none exists for this geometry.

## Where the numbers live

| what | where |
|---|---|
| governing equations, constitutive law, nondimensionalization | `05_DERIVATIONS/theory/` |
| numerical method, grid mapping, contour integration, stability | `05_DERIVATIONS/numerical_method/` |
| material and geometry constants as used by the code | `01_PROGRAM/parameter_manifest.json` |
| raw results per run (375 files) | `03_DATA/raw/` |
| aggregates the manuscript quotes | `03_DATA/processed/ANALYSIS_V2.json` |
| figures | `08_FINAL_OUTPUTS/figures/` (raster), `02_OVERLEAF/figures/` (vector) |
| verification suite results | `04_REPRODUCTION/` |
| manuscript sources, rendered PDFs, supplement, cover letter | `08_FINAL_OUTPUTS/manuscript/` |
| why each decision was taken, what was rejected, what was fixed | `07_DOCUMENTATION/program_control/` (DECISION_LOG, REJECTED_IDEAS, CORRECTIONS_LOG, EVIDENCE_LOG) |
| audits of the code, the maths, the literature, the manuscript | `06_VALIDATION/`, `07_DOCUMENTATION/phases/` |

## Scale of what was run

- 175 production runs with provenance rows; 424 files in `03_DATA/raw/`; 35 MB.
- Verification suite: see `04_REPRODUCTION/TEST_REPORT.md` (the paper reports its one failing case).
- The 2026-10-02 freeze in the repository is the scientific freeze date; the submission programme
  that produced this archive ran Phases 1-10 on 2026-10-03 on top of it (branch history in
  `07_DOCUMENTATION/CHANGELOG.md`).
