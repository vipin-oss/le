# Published-journal and benchmark screen — before execution

**Date:** 30 September 2026  
**Current master:** user-supplied `FINAL MASTER PROMPT v2.1`, saved at `/home/user/MASTER_PROMPT.md` with all sections 0–90.  
**Task authorized:** inspect credible published sources/journals and realistic verification/validation routes before execution.  
**Overall status:** **PARTIAL — evidence routes identified, execution readiness not established.**

This is a bounded pre-execution screen, not a completed formal Phase 0A-2, Phase 2, numerical validation or final journal selection. No scientific solver, numerical benchmark, pilot or production run was executed.

## 1. Main answer

**Haan, published literature mein limiting-case / analytical comparison routes milte hain.** But the route must be reconstructed before claiming it is executable or that agreement will occur.

The useful separation is:

1. **Recent-model source case:** reproduce the exact source model and its stated case.
2. **Coupled thermoelastic limit:** compare an explicitly derived common limit with a cylinder/sphere reference.
3. **Heat-only Fourier limit:** compare a controlled thermal subsystem with a cavity solution.
4. **Independent mathematical controls:** rotation covariance, isotropic/circular limits, conservation and manufactured solutions where appropriate.
5. **Physical evidence:** assess real material/sample measurements separately and restrict any validation claim to the actual compared quantity/conditions.

Passing items 1–4 does not make the full new model physically validated. A paper's own section titled 'validation' may contain only a comparison with another theoretical calculation.

## 2. Three plausible journal families — no overall ranking

The following 2025 SCImago category quartiles were directly inspected on 30 September 2026. These are **SJR/SCImago (Scopus-based) quartiles, not automatically JCR quartiles**.

| Journal | SCImago 2025 categories inspected | Quartile | Indexing evidence | Possible scientific fit |
|---|---|---|---|---|
| Applied Mathematics and Mechanics — English Edition | Applied Mathematics; Mechanical Engineering; Mechanics of Materials | Q1 in these categories | Springer publisher page lists SCIE and Scopus | Analytical/generalized thermoelastic modelling with a sound derivation and a meaningful mechanics finding. |
| International Journal of Heat and Mass Transfer | Fluid Flow and Transfer Processes; Mechanical Engineering; Condensed Matter Physics | Q1 in these categories | Elsevier publisher Insights page lists SCIE and Scopus | Heat-transport mechanisms, credible thermal-model comparisons and transfer-process understanding. |
| International Journal of Mechanical Sciences | Mechanical Engineering; Mechanics of Materials (other categories not required for this screen) | Q1 in these categories | Elsevier publisher Insights page lists SCIE and Scopus | Coupled mechanical/material understanding and an engineering-relevant scientific contribution. |

Quartile sources: [2](https://www.scimagojr.com/journalsearch.php?q=25178&tip=sid&clean=0), [1](https://www.scimagojr.com/journalsearch.php?q=20448&tip=sid), [1](https://www.scimagojr.com/journalsearch.php?q=50170&tip=sid).

Publisher scope/indexing sources inspected:
- https://link.springer.com/journal/10483
- https://www.sciencedirect.com/journal/international-journal-of-heat-and-mass-transfer/about/aims-and-scope
- https://www.sciencedirect.com/journal/international-journal-of-heat-and-mass-transfer/about/insights
- https://www.sciencedirect.com/journal/international-journal-of-mechanical-sciences/about/insights

**Limits of this journal check:** independent Clarivate Master Journal List verification and current category-specific JCR quartiles were not obtained. Publisher-reported indexing is the evidence used here. Full submission-fit review—recent competing articles, article length/type, data/code/AI policies and final publication model—remains pending. No final journal is selected and no acceptance probability is claimed.

Important scope nuance: IJMS explicitly discourages purely descriptive work or generic mathematical/computational techniques without a specific engineering application, and encourages validation against tests. The existing 2007 reference in that journal is not proof that a new parameter-sweep paper would fit its present scope. [1](https://www.scimagojr.com/journalsearch.php?q=50170&tip=sid)

Also, **Applied Mathematics and Mechanics (English Edition)** must not be confused with the separately indexed Chinese-title journal or *Advances in Applied Mathematics and Mechanics*.

## 3. Published references and their actual roles

### B01 — Recent-model source case: Huang et al., 2025

**New insights on generalized heat conduction and thermoelastic coupling models**  
*Applied Mathematics and Mechanics*, 46, 1533–1550.  
DOI: `10.1007/s10483-025-3280-7`.

The publisher abstract identifies generalized CV/GN formulations and a one-dimensional slim-strip thermal-shock calculation using Laplace transformation and numerical inversion. [1](https://link.springer.com/article/10.1007/s10483-025-3280-7)

- **Possible role:** recent-model verification anchor, before a two-dimensional anisotropic extension.
- **Inspected:** metadata, abstract, accessible reference/preview material.
- **Not inspected:** full model equations, full parameter set, exact BCs/ICs, complete reference curves and coefficient restrictions.
- **Access:** Springer subscription preview; official journal alternate URL fetch failed; OpenAlex did not resolve an OA PDF in this attempt.
- **Reconstruction status:** **BLOCKED — FULL TEXT REQUIRED**.
- **Project comparison status:** **NOT_RUN**.

Do not assume its exact operators or LS/Fourier limit from the words 'generalized CV/GN'. The explicit limiting map and compatible initial data must be derived after reading the equations.

### B02 — Coupled cylinder/sphere reference: Bagri & Eslami, 2007

**A unified generalized thermoelasticity; solution for cylinders and spheres**  
*International Journal of Mechanical Sciences*, 49(12), 1325–1335.  
DOI: `10.1016/j.ijmecsci.2007.04.004`.

Publisher preview: https://www.sciencedirect.com/science/article/abs/pii/S0020740307000665

The abstract describes LS/GL/GN coupled formulations, reduction to homogeneous isotropic material, and Laplace-domain solutions for hollow cylinders and spheres under inner-surface thermal shock. This makes it a relevant **candidate coupled limiting-case reference**, not automatically a physically validated dataset.

- **Possible role:** compare a common, explicitly derived coupled limit of the selected new model.
- **Inspected:** publisher metadata/abstract/introduction preview, with DOI corroborated in published reference lists.
- **Not inspected:** full equations, exact source-specific numerical cases, complete parameters/BCs/ICs and plots.
- **Reconstruction status:** **BLOCKED — FULL TEXT / CASE DETAILS REQUIRED**.
- **Project comparison status:** **NOT_RUN**.

A finite hollow cylinder is not automatically the same problem as an infinite solid with a cylindrical cavity. Plane strain/stress, outer boundary, source and normalization must match. An axisymmetric reference must not be used as though it directly represents a fixed-Cartesian monoclinic single crystal; use a justified isotropic/common limit.

### B03 — Thermal cavity reference: Gordeliy, Crouch & Mogilevskaya, 2008

**Transient heat conduction in a medium with two circular cavities: Semi-analytical solution**  
*International Journal of Heat and Mass Transfer*, 51(13–14), 3556–3570.  
DOI: `10.1016/j.ijheatmasstransfer.2007.10.021`.

The publisher preview describes an infinite medium, two non-overlapping circular cavities, suddenly applied steady Dirichlet conditions and a Laplace/Fourier-series solution. [2](https://www.sciencedirect.com/science/article/abs/pii/S0017931007006618)

- **Possible role:** temperature-field verification for an appropriately matched classical heat-diffusion subsystem/common limit.
- **Inspected:** metadata, abstract and introduction/selected section preview.
- **Not inspected:** complete series coefficients, truncation/inversion settings and numerical examples.
- **Reconstruction status:** **BLOCKED — FULL TEXT / REFERENCE CASE REQUIRED**.
- **Project comparison status:** **NOT_RUN**.

This reference is not coupled thermoelasticity and cannot validate the new stress/displacement response. Its Dirichlet loading is not the same as a prescribed finite heat-flux pulse. If a single-cavity limit or different boundary experiment is used for verification, document that as an explicit separate case; do not silently change the proposed production problem.

### B04 — Actual material measurements: Klimm et al., issue 2023 / online 2022

**The Thermal Conductivity Tensor of beta-Ga2O3 from 300 to 1275 K**  
*Crystal Research and Technology*, 58(2), 2200204.  
DOI: `10.1002/crat.202200204`.

**Full five-page publisher-format PDF obtained and read locally**, including tensor/coordinate equations and experimental-method sections. Pages 2 and 3 were also inspected as rendered pages. Public PDF source: [3](https://d-nb.info/1274779782/34). Publisher page: [2](https://onlinelibrary.wiley.com/doi/full/10.1002/crat.202200204).

The source reports laser-flash measurements of diffusivity and derives conductivity using:

```text
conductivity(T) = diffusivity(T) * density(T) * specific_heat(T).
```

Specific heat is taken from FactSage databases; graphite-coated samples remained partly transparent, so the authors used Mehling's semitransparent-material model for the detector-signal analysis. These are material-characterization data with a measurement/analysis model, not direct measurements of every new generalized thermoelastic parameter.

**Source-reported room-temperature tensor**, in the article's orthonormal crystal-physical basis `e2 || b`, `e3 || c`:

```text
K(300 K) = [12.13       0    -0.992
                0   24.26        0
           -0.992       0    14.09] W/(m K).
```

These are REFERENCE INPUT VALUES—not numerical outputs produced in this project, not independently remeasured values and not yet approved project parameters.

Relevant source scope:
- nominally undoped Czochralski-grown crystal slices;
- thickness 0.82–0.85 mm, diameter approximately 10–15 mm;
- crystallographic miscut/orientation uncertainty approximately ±1 degree;
- Nd:YAG flash duration 1 microsecond;
- temperature response detected on the opposite face;
- temperature-dependent study above room temperature, with detailed supporting tables not obtained in this session;
- Figure 2 shows a 2-sigma error bar for one reported curve; do not assign that same uncertainty to every reconstructed tensor component.

**Supporting Information:** publisher metadata says it exists, but the attempted URLs did not yield the PDF. Python requests returned 403; one alternate fetch returned a 404/error page. This is not evidence that the official supplement does not exist. Tables S1/S2 and the detailed detector-curve figure S3 are **NOT INSPECTED**.

**What this provides now:** source-backed conductivity/coordinate/measurement information for parameter provenance and a possible experimental reconstruction route.

**What it does NOT provide now:** independent validation of ultrafast non-Fourier temperature waves, relaxation coefficients or coupled thermal stresses around a cavity. Copying measured K into the model and then reporting that the model has the same K is not independent physical validation.

### B05/B06 — Original TDTR paper plus mandatory correction

Jiang et al., **Three-dimensional anisotropic thermal conductivity tensor of single crystalline beta-Ga2O3**, *Applied Physics Letters* 113, 232105 (2018), DOI `10.1063/1.5054573`.

The publisher links a correction: **Erratum**, *Applied Physics Letters* 114, 049902 (2019), DOI **`10.1063/1.5088513`**. The correction metadata and its main text were inspected. It explicitly corrects a sign in Equation (4), updates the related heat-flux interpretation and Figure 2(b).

Original and correction:
- [1](https://pubs.aip.org/aip/apl/article/113/23/232105/36409/Three-dimensional-anisotropic-thermal-conductivity)
- https://pubs.aip.org/aip/apl/article/114/4/049902/1022980/Erratum-Three-dimensional-anisotropic-thermal

**Consequence:** do not copy the uncorrected tensor or mix it with Klimm's differently defined Cartesian basis. Exact corrected-data import/rotation remains to be checked before use. Correction/retraction screening is source-specific: the linked APL correction was checked; a comprehensive update/retraction check for B01–B04 was not performed. No blanket absence-of-corrections claim is made.

Klimm et al. additionally question a representation-surface ellipse fit in that earlier study. That is a published criticism, not an independent adjudication performed here. A plotted conductivity representation surface is not automatically an ellipsoid. The thermodynamic/coordinate meaning of the chosen representation needs to be stated.

## 4. Recommended evidence ladder — proposed, not executed

| Layer | What would be compared | What it could establish | Current readiness |
|---|---|---|---|
| Exact recent-model source case | same equations, source material, BCs/ICs and output definitions | implementation/source-case verification | BLOCKED by B01 full text |
| Common coupled limit | matched cylinder/sphere temperature/displacement/stress case | coupled limiting-case verification | BLOCKED by explicit new-model reduction and B02 case reconstruction |
| Heat-only classical limit | matched cavity temperature/flux case | thermal subsystem/geometry verification | BLOCKED by full B03 case; independent analytical controls remain possible after authorization |
| Independent mathematical checks | rotations, isotropic/circular limits, source balance, residuals, manufactured case where useful | correctness and robustness | PLANNED, not executed |
| Material characterization | conductivity/diffusivity in a declared sample/temperature/frame | parameter provenance; possible scoped experimental comparison | main B04 source available; supplement and full reconstruction pending |
| New generalized transient prediction | measured T(t) and/or stress/displacement under a matched experiment | physical validation of those quantities within that scope | APPLICABLE — EVIDENCE_UNAVAILABLE in this bounded screen |

The last status means relevant matched evidence was not established here—not proof that no experiment exists anywhere. A theoretically meaningful project may remain legitimate, with restricted claims and an approved theoretical/computational evidence route.

## 5. Execution gates still open

Before any new-model implementation or pilot:

1. Confirm the exact research shortlist and authorized next phase.
2. Obtain/read the model source and derive its assumptions, admissible coefficients and common limits.
3. Reconstruct at least one complete reference case: equations, constitutive conventions, geometry, material, units, BCs, ICs, compared quantity and available reference data.
4. Choose a method appropriate to the actual equations, not simply existing BFS code.
5. Define the pilot's objective, diagnostic criteria and small compute budget if a pilot is explicitly authorized.

Before confirmatory/production interpretation:

- approve the precise research type/problem and formal scientific acceptance plan;
- define quantity-specific errors, reference/digitization uncertainty and numerical accuracy criteria;
- verify admissibility, source-case agreement and relevant numerical uncertainty;
- distinguish calibration from validation;
- state which predictions remain hypothetical/extrapolative;
- obtain production approval if ANY threshold exceeds 4 CPU-hours, 1 GPU-hour or 5 GB generated data.

No universal 'less than 5 percent means PASS' rule is adopted.

## 6. Updated recommendation

**Keep beta-Ga2O3 and the 2025 family provisional rather than frozen.** Reconstructable evidence should inform the final material/model choice. The previous crystal–geometry symmetry idea remains a candidate, not an approved scientific project.

The practical first priority is **B01 full model + B02 coupled reference**, or a clearly approved alternative with accessible full equations. Do not silently replace the recent model by an older one merely because the older benchmark is easier to match.

The two most useful PDFs to supply, if the user has legitimate access, are:

1. Huang et al. (2025), DOI `10.1007/s10483-025-3280-7`.
2. Bagri & Eslami (2007), DOI `10.1016/j.ijmecsci.2007.04.004`.

B03 is useful additionally for a heat-only cavity comparison. If a specific previously shared Google Drive paper was intended as the base, give its title/Excel Sr. No.; it has not been identified.

## 7. Completion record / stop

**PHASE / TASK:** user-authorized published-journal and benchmark/evidence screen; not full numbered-phase completion.  
**STATUS:** PARTIAL.

**COMPLETED:** v2.1 persisted; three journal-family metadata checks; published verification candidates identified; one full material-measurement paper read; relevant erratum inspected; source/access/evidence boundaries recorded.

**SCIENTIFIC ACCEPTANCE:** not established; no formal acceptance plan yet because Phase 1/final direction are unapproved.

**DECISIONS:** evidence-first selection; no guaranteed benchmark matching; corrected source versions and coordinates required.

**REJECTED / HELD:** uncorrected 2018 tensor as a ready input; treating measured conductivity as full-model validation; treating publication in a Q1 venue as proof of correctness; treating snippets as reconstructed equations. Papers themselves are not rejected wholesale.

**VERIFICATION:** NOT_STARTED for the new project.  
**PHYSICAL VALIDATION:** NOT_STARTED; matched new transient/stress evidence not established.  
**CODE:** no new scientific implementation; provided FEM4 original unchanged.  
**COMPUTE:** zero new scientific solver/pilot/production runs.

**OPEN QUESTIONS:** full model/reference access; exact common limits; complete coupled material data; approved evidence route; user hardware/software/compute constraints; final shortlist and journal.

**IMPACT ON PREVIOUS WORK:** no numerical results changed because none were produced. Earlier beta-Ga2O3 reference suggestions now carry a correction/coordinate warning. Older v2.0 control assumptions are superseded by user-supplied v2.1.

**FILES:** this report; `PRE_EXECUTION_SCREEN.xlsx`; search/evidence logs; reference/journal/source-status records; root control/state files; canonical master/version/date files.

**RECOVERY PACKAGE:** `RECOVERY_PRE_EXECUTION_REVIEW_01.zip` is a notes/control checkpoint, NOT a final research package. It excludes third-party PDFs/images and original code/manuscript inputs; accessible input paths/URLs/manifests remain recorded. It is not an offline-complete source/input archive.

**EXACT NEXT ACTION:** wait for source PDFs and/or explicit approval of the next source-reconstruction/shortlisting task. Do not start simulations automatically.
