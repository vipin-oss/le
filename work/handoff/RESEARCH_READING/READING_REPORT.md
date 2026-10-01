# Aapke Research Corpus ka Initial Reading Report

**Reading date:** 30 September 2026  
**Scope:** User-authorized literature/corpus reading, before new research discovery.  
**Status:** Inventory completed; representative section-level reading completed; exhaustive paper-by-paper review and numerical audit NOT completed.

> Yeh report papers ko samajhne ka first pass hai. Isse unke equations, numerical values, novelty, physical validation ya publication readiness independently certified nahi hote. Manuscript mein reported results aur is session mein independently reproduced results alag hain. Is session mein koi scientific simulation/test execute nahi kiya gaya.

## 1. Kya retrieve aur inspect kiya gaya

| Input | Observed contents | Reading/verification status |
|---|---|---|
| `Vipin_Research_Papers_06-Aug_2026.xlsx` | 48 nonempty paper records; 2022–2026 according to supplied entries | All records and hyperlinks inventoried. Bibliography is not full text. |
| Published DOI entries | 47 distinct DOI strings, because records 36 and 41 duplicate the same title/DOI | These are not being claimed as 47 independently verified publications. |
| Crossref checks | 12 successful metadata responses; 36 HTTP 429 rate-limit responses | Successful records matched listed titles. Rate-limited records remain incompletely verified, not invalid. |
| Representative published PDFs | 8 PDFs retrieved, for Sr. Nos. 1, 2, 25, 29, 35, 38, 45, 47 | Section-level first pass: abstracts/front matter, selected formulation/comparison passages, conclusions and limitations as available. |
| `FEM_Total.zip` | 8 PDFs; no source-code/data files within this supplied archive | All 8 manuscripts received a section-level first pass. Publication status is as supplied by the user. |
| Code / result reproduction | Not performed | NOT_RUN. Claims of executed code inside papers were read, not independently re-executed. |

The available published sample PDFs total **148 PDF pages**; the eight supplied unpublished PDFs total **265 PDF pages**. These totals describe accessible documents, **not pages individually audited**.

Two additional selected published full-text links, Sr. Nos. **10 and 21**, did not yield a PDF in this retrieval attempt. No full-text reading is claimed for them. The other unsampled published entries were inventoried, not fully read.

Original inputs are preserved unchanged. Download URLs, retrieval timestamps, SHA-256 checksums and the GitHub blob identifiers are recorded in `SOURCE_MANIFEST.json`.

### Metadata corrections / cautions

1. **Duplicate:** Sr. Nos. **36 and 41** contain the same title, *Size-dependent analysis of surface wave in irregular fractured porous seabed subjected to fractional-order derivative*, and DOI `10.1080/15376494.2024.2440131`. Treat them as one DOI record unless the user explains a separate bibliographic purpose. Online publication and final issue dates must be distinguished; a date difference alone is not an error.
2. **DOI mismatch, Sr. No. 47:** The workbook gives `10.1016/j.jppr.2026.116904`. The retrieved article PDF, page 1, and the publisher record give **`10.1016/j.jppr.2026.02.007`**, *Propulsion and Power Research* 15(1), 179–196. Publisher evidence: [1](https://www.sciencedirect.com/science/article/pii/S2212540X26000210). This is a proposed metadata correction; the original workbook was not edited.
3. **Link classification:** Sr. No. 2's “Link to Article” points to a journal-indexing search page rather than article full text. Its actual DOI resolves to the Scientific Reports article, also indexed in PMC: [2](https://pmc.ncbi.nlm.nih.gov/articles/PMC10567774/).
4. Spreadsheet indexing and impact-factor columns remain **USER-SUPPLIED — NOT CURRENTLY VERIFIED**. No current journal-quartile conclusion is made here.

## 2. Aapka observed research ecosystem

This profile is inferred from supplied titles and inspected sections, not from assumptions about personal expertise, available hardware, software licences or individual contributions to every coauthored paper.

### Stream A — Analytical/semi-analytical coupled wave mechanics

The publication list and inspected sample emphasize:

- Plane-wave, Rayleigh/surface-wave and SH-wave propagation.
- Reflection/transmission and energy partition at boundaries/interfaces.
- Thermoelasticity, generalized heat conduction, fractional and memory-dependent operators.
- Piezoelectric/piezomagnetic/semiconductor coupling.
- Single/double porosity, fluid interaction, material gradation and imperfect interfaces.
- Spatial/spatiotemporal nonlocality, size effects, rotation and viscoelasticity.
- Secular/determinant formulations, modal solutions, variable separation and Laplace-domain methods.

Thermal physics is important, but it is **not universal**: the supplied corpus also includes mechanically/electrically driven SH-wave work without thermal coupling.

### Stream B — Variational higher-order continuum computation

The five FEM manuscripts emphasize:

- Mindlin Form-II and simplified/anisotropic strain-gradient elasticity.
- Ellipsoidal averaging domains and orientation-dependent characteristic-length tensors.
- C1 Hermite / Bogner–Fox–Schmit discretization.
- Weak forms, higher-order boundary conditions and boundary-layer mechanics.
- Total-Lagrangian finite-strain formulations and consistent Newton tangents.
- Coupled piezoelectric–flexoelectric and piezoelectric–pyroelectric problems.
- Conditioning, non-dimensionalization, energy bookkeeping and material-parameter provenance.

BFS is therefore an observed computational framework in this corpus, **not a compulsory method for future work**.

### Stream C — Identifiability, model discrimination and observability

The GK, quasicrystal and later electromechanical manuscripts introduce questions beyond parameter curves:

- Are fitted coefficients separately recoverable?
- Can different dynamic models be distinguished above numerical resolution?
- Which physical couplings are active, weak or exactly decoupled in a specified configuration?
- Does a constitutive reduction change the sign of a predicted device observable?

These are descriptions of the manuscripts' stated scientific questions—not independently verified novelty claims.

## 3. Published sample: what was actually read

| Sr. No. | Paper / family | Inspected focus and observed approach |
|---|---|---|
| 1 | Generalized plane waves in a rotating thermoelastic double porous solid | Lord–Shulman thermal model; coupled displacement, temperature and two void fields; plane-wave ansatz, characteristic roots, surface conditions and reported rotation-dependent responses. |
| 2 | Behavior of higher-order MDD on energy ratios at the interface of thermoelastic and piezothermoelastic mediums | Higher-order memory-dependent three-phase-lag interface problem; reflected/transmitted mode amplitudes and energy ratios; reported energy balance. |
| 25 | Comparative analysis of double and single porosity effects on SH-wave induced vibrations in periodic porous lattices | Corrugated layered geometry; variable separation; complex dispersion/attenuation equations; single/double-porosity comparisons; reduced cases including Love-wave relation. |
| 29 | Effects of layer imperfections and material gradation on circumferential SH waves in cylindrical piezoelectric composite structure | Three concentric layers, imperfect interfaces, gradation and initial stress; phase velocity and layer fields; explicitly stated theoretical/computational scope and missing experimental validation. |
| 35 | Coupled thermo-mechanical dynamics of rotating nano-beams with spatiotemporal nonlocality and higher-order memory-driven heat transfer | Euler–Bernoulli beam; KG-type spatiotemporal nonlocality; MGT heat transport with higher-order MDD; Laplace/eigenvalue approach and Zakian inversion; reduced-model comparison table. |
| 38 | Acoustic wave behavior in rotating functionally graded piezomagnetic media with impedance boundaries | Flexomagnetic/strain-gradient/micro-inertia formulation; reflected-mode energy partition; gradation, rotation and impedance comparisons. |
| 45 | Heat map analysis of wave dynamics in nonlocal Kelvin–Voigt piezo-semiconductors under memory-dependent heat flux | KG nonlocality, Kelvin–Voigt viscosity, three-phase-lag/MDD conduction and semiconductor fields; normal-mode solution; CdSe reference inputs; limiting-case comparisons and stated lack of experimental validation. |
| 47 | Fractal geometry-based KG model for heat and mass transfer in a cylindrical cavity with variable thermal conductivity | Non-integer-dimensional operators; thermoelastic diffusion; Kirchhoff transformation; Laplace/Zakian solution; reduced-model checks and radial-field analysis. DOI correction recorded above. |

### Evidence-label observation

In several inspected papers, sections named “validation” primarily discuss agreement with reduced established models, analytical relations or prior theoretical results. In the v2 master-prompt framework, those passages should be assessed primarily as **verification / model-consistency / theoretical comparison**, unless they actually compare with empirical physical evidence. Publication or the section heading does not automatically determine the evidence category.

## 4. Supplied unpublished manuscripts

All quantities below are descriptions of what the manuscripts **claim/report**. No numerical values or convergence claims have been independently reproduced in this session.

| File | PDF pages | Main question/contribution reported | Evidence boundary observed |
|---|---:|---|---|
| `FEM_!_Paper.pdf` | 41 | Ellipsoidal averaging-based anisotropic characteristic lengths; C1 Hermite/BFS/tricubic formulations; orientation-dependent static and vibration response. | Experimental calibration appears as a proposed protocol, not completed independent material calibration. |
| `FEM_2_Paper.pdf` | 24 | Mindlin Form-II BFS framework; anisotropic ellipsoidal microstructures; simple-shear boundary layers, double stresses and energy partition. | Analytical Shekarchizadeh benchmark is reported; solver and anisotropic production results remain unreproduced here. |
| `FEM_3_Paper.pdf` | 31 | Total-Lagrangian, finite-strain Mindlin Form-II mechanics; displacement-only C1 BFS and consistent tangent. | Reported small-strain benchmark plus finite-deformation numerical studies; those support different scopes and must not be conflated. |
| `FEM_4_Paper.pdf` | 41 | Coupled piezoelectric–flexoelectric/strain-gradient formulation; reduced flexoelectric specialization; scaling and conditioning. | Some benchmark convergence rates are calculated from **source-reported error norms**, explicitly not a fresh reconstruction of those errors. |
| `FEM_5_Paper.pdf` | 26 | Plane-strain tetragonal BaTiO3 microcantilever; correct 3D thermal-stress contraction, primary pyroelectric coefficient and voltage polarity. | Material uncertainties and no direct full-device experimental voltage comparison are stated. Flexoelectric extension is excluded from quantitative results. |
| `GK_heat_Paper.pdf` | 44 | Fourier-resonance-induced structural/practical non-identifiability of GK coefficients; inverse analysis, Fisher information and model selection. | Inverse experiments are synthetic. Published analytical forward-reference comparisons are not experimental validation of inverse conclusions. |
| `Quasi_crystal_Paper.pdf` | 30 | Inertial, diffusive and telegraph phason dynamics; semi-analytical surface-wave matrix/root formulation; branch identity and resolvability. | Surrogate/composite parameters; configuration-specific electric decoupling; no experimental validation claimed. |
| `paper_springer.pdf` | 28 | Torsional waves with metamaterial shell, imperfect interfaces and Gurtin–Murdoch surface elasticity; reported exact thermal decoupling and localization/sensing analysis. | Supplied reduced-model literature comparison is a verification pathway. Title page names **Annu Rani and M. S. Barak**, not Vipin Gupta; relationship to the user's authored work is unconfirmed. |

## 5. Detailed first-pass observations for future work

### U01 — Ellipsoidal characteristic-length framework

`FEM_!_Paper.pdf` explicitly links microstructural-domain geometry to an anisotropic tensor, with an energy-based gradient penalty and static/dynamic finite-element applications. Its experimental-calibration section proposes size-effect tests, orientation tests, dispersion measurements and RVE procedures. These are possible future evidence routes; their presence in the manuscript is not evidence that they were executed.

**Novelty boundary for later discovery:** ellipsoidal internal lengths, orientation tuning and the associated Hermite/BFS framework already belong to the supplied unpublished corpus. Do not propose them as a fresh direction without comparing the exact scientific difference.

### U02 — Anisotropic simple-shear/boundary-layer study

`FEM_2_Paper.pdf` reports displacement-profile agreement with the Shekarchizadeh benchmark and then studies an anisotropic ellipsoidal model. Later review should check the benchmark-to-production constitutive mapping and which terms each test exercises.

A terminology issue is flagged for checking: the conclusion refers to “continuous second-order derivatives.” C1 conformity gives continuous first derivatives; global continuity of all second derivatives is not generally a BFS property or the conformity requirement. This is a preliminary wording concern, not a completed numerical audit.

### U03 — Nonlinear strain-gradient mechanics

`FEM_3_Paper.pdf` separates Green–Lagrange/material-gradient kinematics, free energy, virtual work, element residual and consistent tangent. Its small-strain analytical comparison checks linear-limit recovery; the finite-strain claims additionally need tangent/objectivity/nonlinear checks. No implementation was examined here.

### U04 — Reduced flexoelectric model and source-reported benchmarks

`FEM_4_Paper.pdf` explicitly identifies a reduced/shear-free flexoelectric specialization. Its reported slenderness behavior is interpreted through that specialization, not simply numerical convergence. It also clearly labels source-reported benchmark norms and roots.

**Traceability requirement:** recomputing a rate from another source's errors must remain distinct from demonstrating the present solver's convergence against an independently reconstructed reference. Actual coupled-problem mesh studies and analytical checks should be tracked separately.

### U05 — Thermal-stress reduction and voltage polarity

`FEM_5_Paper.pdf` has a comparatively specific central question: how the constitutive plane-strain reduction and parameter definitions affect a device-level observable. It distinguishes primary versus total pyroelectric coefficients and identifies material-data incompatibilities/uncertainties.

The optional flexoelectric extension is not used for the reported quantitative results. Future proposals must not treat this manuscript as a completed full flexoelectric thermoelectromechanical validation. Its stated repository/test/environment details are documentary claims pending artifact inspection.

### U06 — GK inverse-problem study

`GK_heat_Paper.pdf` distinguishes the known Fourier-resonance cancellation from the proposed inverse-identifiability consequence. Its universal structural statement and configuration-dependent finite-noise band must be kept separate. The three reproduced reference figures belong to one analytical reference paper, as the manuscript itself states.

The manuscript calls those comparisons “external validation.” Under the master prompt's physical-validation definition they are **external analytical verification/comparison**, not physical validation. No experimental test of the inverse conclusions is claimed.

### U07 — Quasicrystal dynamic-model discrimination

`Quasi_crystal_Paper.pdf` treats phason dynamics as a model-class/branch-selection question. It explicitly reports weak or unresolved effects relative to a numerical floor, rather than insisting that every coupling produce a strong change.

Its electric decoupling is configuration-specific; its parameter set is not a fully characterized single specimen. Future interpretation must preserve both boundaries. Declarations also contain placeholders, so this supplied version is not administratively submission-final.

### U08 — Torsional-wave draft

`paper_springer.pdf` reports thermal decoupling for pure axisymmetric torsion in the specified linear isotropic setting. This does not imply that temperature-dependent properties, thermal prestress or other configurations have no effect. Its claimed reduced-model agreement and branch tracking remain unreproduced here.

**Attribution:** keep this document as supplied collaborator/reference material pending the user's clarification. Do not silently attribute its authorship to Vipin Gupta.

## 6. Implications for the next research project—not a topic selection

1. Compare a future candidate with **both published and unpublished** supplied work; otherwise an apparently new idea may simply repeat an existing draft.
2. Do not assume the publication list establishes the user's individual mastery of every coauthored method. Confirm reusable code and responsibilities when relevant.
3. Do not force BFS/FEM. The corpus already contains multiple semi-analytical solution routes.
4. Do not force thermal coupling. The supplied drafts themselves identify exact or configuration-specific decoupling.
5. Prefer an explicit, testable limitation/mechanism over merely increasing the number of coupled ingredients. Identifiability, model distinguishability and constitutive-reduction questions are already visible in this corpus.
6. Independently inspect equations, references and code before accepting any benchmark/validation statement as verified project evidence.

No broad candidate discovery, final direction selection, new novelty confirmation, production run, journal-quartile verification or manuscript rewrite was performed.

## 7. Unknowns retained—not guessed

- Which exact code package corresponds to each manuscript and whether it is the current version.
- Which results the user wishes to extend versus avoid overlapping.
- User's available languages/software licences, hardware, compute budget and timeline.
- Access to experiments/measurement collaborators or benchmark datasets.
- Relationship of `paper_springer.pdf` to the user's authored/collaborative work.
- Remaining published full texts and current correction/retraction status for the entire list.

## 8. Confidentiality / licensing note

The provided GitHub repository was publicly accessible during retrieval. The supplied unpublished ZIP is therefore accessible through its public URL; this review did not upload it or its text to another service or use unpublished passages in web-search queries. The user may wish to review public exposure of unpublished drafts. Public availability is not itself a licence to redistribute third-party PDFs/code.

## 9. Recovery files

Main reading report: `READING_REPORT.md`.

Supporting files:

- `PROJECT_STATE_READING_01.md` — recovery state and exact pending actions.
- `PUBLISHED_PAPERS_INVENTORY.csv` / `.json` — all 48 source entries, preserving original metadata.
- `UNPUBLISHED_PACKAGE_INVENTORY.csv` — actual archive contents.
- `READING_STATUS.csv` — per-entry reading scope/status.
- `SOURCE_MANIFEST.json` — source/version/checksum provenance.
- `CROSSREF_METADATA_VERIFICATION.json` — actual responses/statuses.
- `PUBLISHED_FULLTEXT_RETRIEVAL.json` — successful and unsuccessful selected PDF retrievals.
- `SEARCH_LOG.md` — exact published-literature queries used.
- `EVIDENCE_LOG.md` — key first-pass claims and evidence boundaries.
- `EXTRACTED_UNPUBLISHED/` and `EXTRACTED_PUBLISHED_NATIVE/` — PDF text extracts for follow-up, not substitutes for rendered equation inspection.

**Next action:** wait for user authorization. If deeper reading is requested, expand the paper-by-paper equation/BC/method/benchmark/overlap matrix and inspect the relevant current code archives. No research direction is approved.
