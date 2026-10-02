# Project recovery state — user-corpus reading 01

Date: 30 September 2026.

## Authorization and scope

The user provided a published-paper Excel list and an unpublished-manuscript ZIP and asked the assistant to read some literature first. This authorized corpus reading, not candidate discovery, research-direction selection, formulation of a new project, code execution or production simulations. No numbered research phase has been explicitly authorized.

The user previously supplied FINAL MASTER PROMPT v2.0. Its key constraints include scientific correctness, evidence-supported novelty, separate verification/physical validation, method determined by problem, no forced thermal coupling, explicit user decisions, reproducibility and stopping between authorized phases. The complete master prompt is not stored in this reading folder; it should be supplied/read separately in a future session.

## Inputs and provenance

- Original published list: `/home/user/RESEARCH_PROJECT_INPUT/LITERATURE/Vipin_Research_Papers_06-Aug_2026.xlsx`.
- Original unpublished archive: `/home/user/RESEARCH_PROJECT_INPUT/PREVIOUS_PROJECTS/FEM_Total.zip`.
- Extracted manuscripts: `/home/user/RESEARCH_PROJECT_INPUT/PREVIOUS_PROJECTS/FEM_Total/`.
- Retrieved representative published PDFs: `/home/user/RESEARCH_PROJECT_INPUT/LITERATURE/Accessible_Published_Fulltexts/`.
- Source URLs, checksums and Git blob identifiers: `SOURCE_MANIFEST.json`.

Raw inputs were not modified. Unpublished text was not used in external searches or uploaded to another service. The linked repository is public; public exposure of unpublished drafts should be considered by the user.

## What was completed

1. Excel cells, hyperlinks and metadata inventoried: 48 records, 47 distinct DOI strings.
2. Duplicate identified: records 36 and 41 share title and DOI `10.1080/15376494.2024.2440131`.
3. DOI correction proposed for record 47: source Excel gives `10.1016/j.jppr.2026.116904`; retrieved PDF/publisher give `10.1016/j.jppr.2026.02.007`.
4. Crossref retrieval: 12 metadata records succeeded; 36 requests rate limited (429). Do not infer invalid papers from 429.
5. Published PDF IDs 1, 2, 25, 29, 35, 38, 45, 47 retrieved and read at section level. IDs 10 and 21 attempted but PDF retrieval unresolved. Remaining published entries are inventoried, not full-text reviewed.
6. Eight manuscript PDFs extracted and read at section level. The ZIP contains no code/data files.
7. Initial reading report, search log, evidence log and per-entry status files created.

## Reading depth

Selected abstracts/front matter, method/comparison passages, conclusions and limitations were inspected. This is not an exhaustive equation-by-equation audit or systematic novelty search. Accessible samples contain 148 published PDF pages and 265 unpublished PDF pages; these counts do not mean all 413 pages were individually audited. PDF text extraction can distort tensor notation and two-column order; rendered pages must be inspected for later equation-level audits.

## Observed research ecosystem

- Published corpus: coupled wave propagation; thermoelastic/thermal-memory/fractional models; nonlocality; piezoelectric/piezomagnetic/semiconductor coupling; porosity; SH/Rayleigh/interface waves; rotation; gradation; imperfect/impedance boundaries.
- Unpublished FEM family: ellipsoidal characteristic-length tensors; C1 Hermite/BFS strain-gradient mechanics; total-Lagrangian finite strain; flexoelectric/piezoelectric and pyroelectric coupling; higher-order BCs; conditioning and energy bookkeeping.
- Further unpublished work: GK parameter identifiability and model selection; quasicrystal phason dynamic-class/branch discrimination; torsional metamaterial/surface-elasticity waveguide.

## Manuscript inventory and scientific boundaries

- `FEM_!_Paper.pdf` (41 pages): ellipsoidal internal-length framework and 1D/2D/3D C1 computation; calibration protocol proposed, not executed evidence.
- `FEM_2_Paper.pdf` (24): anisotropic Mindlin/BFS simple-shear boundary layers; benchmark claims unreproduced; continuous-second-derivative wording flagged for checking.
- `FEM_3_Paper.pdf` (31): finite-strain total-Lagrangian Mindlin/BFS; small-strain verification and nonlinear claims have separate scopes.
- `FEM_4_Paper.pdf` (41): reduced flexoelectric/strain-gradient coupling; some reported benchmark rates derived from source-reported norms, not fresh solver error reconstruction.
- `FEM_5_Paper.pdf` (26): BaTiO3 pyro/piezo voltage and thermal-stress reduction; optional flexoelectric extension excluded from numerical results; no direct device experiment.
- `GK_heat_Paper.pdf` (44): Fourier-resonance-induced non-identifiability; synthetic inverse experiments; published analytical reference comparisons do not establish physical validation.
- `Quasi_crystal_Paper.pdf` (30): inertial/diffusive/telegraph phasons; configuration-specific electric decoupling; surrogate parameter set; numerical-floor bounds; administrative placeholders remain.
- `paper_springer.pdf` (28): torsional metamaterial waveguide, surface elasticity, interface springs and reported thermal decoupling in a linear isotropic configuration. Title page lists Annu Rani and M. S. Barak, not Vipin Gupta. User's relationship to this document is unconfirmed; do not silently attribute authorship.

## Research/model/code status

- New research direction: NOT_SELECTED / NOT_APPROVED.
- New equations/method: NOT_DEFINED.
- Existing manuscript claims: READ, NOT INDEPENDENTLY CERTIFIED.
- Scientific code/tests/simulations: NOT_RUN.
- Physical validation: NOT_ASSESSED for an approved project.
- Full literature novelty/scooping: NOT_STARTED.
- Current journal indexing/quartiles: NOT_VERIFIED; Excel metrics remain user-supplied.
- Reproduction: NOT_ATTEMPTED; code archives were not downloaded/inspected.
- Hardware, local software availability, timeline and experiment access: UNKNOWN, not inferred from papers or repository name.

## Decisions and risks

- Preserve originals; record corrections separately.
- Use both published and unpublished work as the future overlap baseline.
- Do not force BFS/FEM or thermal coupling.
- Distinguish source-reported calculations from executed results.
- Do not label analytical/limiting-case comparisons as physical validation.
- No candidate was proposed, shortlisted, ranked, rejected or approved.

## Exact next action

Wait for the user. If deeper reading is authorized, expand a paper-by-paper equation/BC/method/benchmark/overlap matrix and inspect current matching code archives with clear attribution and versions. If a numbered phase is authorized, first read the complete master prompt and this state/report; do not repeat the completed inventory unnecessarily.

## Recovery file inventory

- `READING_REPORT.md` — main deliverable.
- `PUBLISHED_PAPERS_INVENTORY.csv`, `.json`.
- `PUBLISHED_WORKBOOK_CONTENTS.json`.
- `UNPUBLISHED_PACKAGE_INVENTORY.csv`.
- `READING_STATUS.csv`.
- `SOURCE_MANIFEST.json`.
- `CROSSREF_METADATA_VERIFICATION.json`.
- `PUBLISHED_FULLTEXT_RETRIEVAL.json`.
- `PUBLISHED_READING_EXTRACTS.json`, `UNPUBLISHED_READING_EXTRACTS.json`.
- `EXTRACTED_PUBLISHED/`, `EXTRACTED_PUBLISHED_NATIVE/`, `EXTRACTED_UNPUBLISHED/`.
- `SEARCH_LOG.md`, `EVIDENCE_LOG.md`.
- `inspect_published_sources.py` — retrieval helper; beware API limits if rerunning.

No cumulative research-phase ZIP or final research package was created, because the authorized task was preliminary reading only.
