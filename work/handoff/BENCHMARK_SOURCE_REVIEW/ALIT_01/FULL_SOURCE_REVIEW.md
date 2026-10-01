# Full-source benchmark review — alit.zip

**Date:** 30 September 2026  
**Master:** FINAL MASTER PROMPT v2.1.  
**Authorized scope:** receive/read the requested papers and inspect source equations, cases and evidence routes before execution.  
**Status:** source-access blocker **RESOLVED**; benchmark specifications identified; overall implementation/validation readiness **PARTIAL**.  
**Scientific solver/pilot/production:** **NOT_RUN**.

## 1. Files received and matched

The supplied archive contains exactly three PDFs, not code or raw simulation/experimental datasets.

| ID | Paper | DOI | PDF pages |
|---|---|---|---:|
| B01 | Huang et al., *New insights on generalized heat conduction and thermoelastic coupling models* (2025) | 10.1007/s10483-025-3280-7 | 18 |
| B02 | Bagri & Eslami, *A unified generalized thermoelasticity; solution for cylinders and spheres* (2007) | 10.1016/j.ijmecsci.2007.04.004 | 11 |
| B03 | Gordeliy et al., *Transient heat conduction in a medium with two circular cavities: Semi-analytical solution* (2008) | 10.1016/j.ijheatmasstransfer.2007.10.021 | 15 |

Titles/DOIs match the requested sources. The 44 pages are document sizes, not a claim that every equation/proof has been independently audited. Full texts were available and their relevant formulation, BC/IC, method, parameter, result/benchmark and conclusion sections were inspected. Key equations/tables were also read as rendered pages, not inferred from snippets.

Raw files are preserved under:
`/home/user/RESEARCH_PROJECT_INPUT/LITERATURE/USER_SUPPLIED_BENCHMARKS/ALIT_01/`.

Provenance, file hashes and Git blob are in `SOURCE_MANIFEST.json` and `PDF_MANIFEST.json`. The older pre-execution report's full-text BLOCKED labels are historical; this review supersedes those access statuses, not the unexecuted scientific-validation status.

## 2. Concrete benchmark route selected for proposal

**First:** B01's 1D source case, using CV as the parent and MCV3 as a candidate modified law.  
**Second:** B02's explicitly stated LS hollow-cylinder case, to check the curved coupled limit under its own BCs and normalization.  
**Third:** B03's printed tables as independent heat-only geometry references.

This is a source-case recommendation, not final approval of beta-Ga2O3, an elliptical cavity, a new research direction or a journal. No agreement is guaranteed. The source models/parameter conventions must be reproduced faithfully; matched-conductivity mechanism controls belong to a separate, explicitly labelled analysis.

## 3. B01 — recent-model 1D coupled source case

### What the paper actually implements

The source uses **CV + six MCV laws + GN + four MGN laws** (12 Table-1 rows). They are not all independent kernels under its equal-component-parameter restriction.

The original mechanical model is classical linear elasticity. Modified laws add **time derivatives** of heat flux/temperature gradient; they do not introduce Mindlin mechanical strain-gradient stiffness or prove that a C1 BFS discretization is required. Eliminating one field produces a fourth-order spatial ODE, but the original coupled u/theta formulation is different from a physical strain-gradient elastic model.

### Equations inspected

B01 PDF pp. 8–11, Eqs. (44)–(66):

```text
rho*u_tt = (lambda+2*mu)*u_xx - gamma*theta_x
sigma = (lambda+2*mu)*u_x - gamma*theta
k*N(D)*theta_xx = M(D)*(gamma*T0*u_xt + rho*cE*theta_t)
gamma = (3*lambda+2*mu)*alpha_theta
```

`theta=T-T0`, `D=d/dt`. **M acts on both the temperature and the thermoelastic strain-rate coupling**, not only on theta_t.

### Geometry, loading, BCs and initial-history scope

- One-dimensional **semi-infinite** longitudinal strip/continuum, `x >= 0`; not a finite cantilever beam.
- Heated free end: `sigma(0,t)=0`, `theta(0,t)=T0*H(t)`.
- Undisturbed far field: `u,theta -> 0` as `x -> infinity`.
- Dimensionless boundary temperature: `theta*(0,t*)=H(t*)`.
- The Laplace equations omit initial-history terms. The relevant source section does not explicitly list every IC for each higher-order heat law. A **causal zero-prehistory/equilibrium interpretation** must therefore be documented as a reconstruction assumption, including compatible heat-flux/memory histories, rather than presented as an explicit author-supplied complete IC list.

### Reported inputs and target

Source Table 2, PDF p. 11:

| Property | Source-reported value |
|---|---:|
| lambda | 77.6 GPa |
| mu | 38.6 GPa |
| alpha_theta | 1.78e-5; see unit issue below |
| rho | **8945 kg/m3** |
| cE | **381 J/(kg K)** |
| T0 | 293 K |

Do not silently substitute the different copper values often used in other papers.

**Figure-5 case:** dimensionless `t*=0.06`, `tau*=0.04`; temperature, normal stress and displacement versus dimensionless position. CV and MCV3 form a useful first source-case pair. Table 1 gives MCV3:

```text
q + 3*tau*q_t + tau^2*q_tt = -k*grad(theta) - k*tau*grad(theta_t).
```

The source gives closed Laplace-domain decay modes and amplitudes in Eqs. (63)–(66). Root branches must be chosen to decay in the half-space. The code/inversion settings are not supplied: the paper refers to Brancik (1999), Ref. [51], for a MATLAB numerical-inversion algorithm.

**Reference curves:** Figs. 5–8 are available, but raw numerical arrays and digitization uncertainty are not provided. No figure has been digitized or reproduced here.

### Useful analytical checks, not executed solver tests

- Eq. (66) amplitudes give `theta_hat(0,s)=1/s` and `sigma_hat(0,s)=0`, provided the roots/amplitudes are used consistently.
- In the source normalization, `n2=rho*cE/k` and `g=gamma/(k*n2)`, hence **g=gamma/(rho*cE)**. The missing physical k in Table 2 does **not** prevent a dimensionless Figure-5 reconstruction. Physical x/time/relaxation conversion still requires justified k.
- Stress is normalized by **mu**, while x/u/t/tau use the source's n1/n2 scaling. Do not mix this with B02/B03 normalizations.

The source chooses a normalized mathematical step with dimensional theta amplitude T0. It is not an experimental operating-point validation or permission to impose a large temperature jump on a different material while retaining constant room-temperature coefficients.

### Figure 4 is not a self-contained experimental validation case

The paper compares MCV1 temperature with Yu & Zhao (2020), Ref. [52]. It is a **theoretical literature comparison**, not an experiment. The Figure-4 paragraph/caption does not state all time/relaxation settings needed for an exact independent reconstruction. Ref. [52] is useful if that specific comparison is audited, but it is **not needed to begin the explicitly stated Figure-5 CV/MCV3 source-case assessment**.

Ref. [52] metadata: *Fractional thermoelasticity revisited with new definitions of fractional derivative*, DOI `10.1016/j.euromechsol.2020.104043`; full text not inspected in this task.

## 4. B02 — coupled curved reference: use the LS cylinder first

Relevant source: PDF pp. 3–6, Eqs. (15)–(56), especially Sec. 4.1.

### Explicit published case

- Homogeneous isotropic long hollow cylinder, **plane strain**, radial symmetry (`m=1`).
- Dimensionless radii `a=1`, `b=2`.
- Source parameters: `c1=1`, `c2=0.535`, coupling `epsilon=0.02`.
- LS thermal parameters: `tau0=4`, `cK=1`.
- Smoothed step `f(t)=1-(1+100*t)*exp(-100*t)`; it rises toward one and is not a pulse returning to zero.
- Inner boundary: `q_r(a,t)=f(t)`, **u(a,t)=0** (fixed).
- Outer boundary: **theta(b,t)=0**, `sigma_rr(b,t)=0` (traction-free).
- Eq. (27) explicitly gives zero initial u, u_t, theta, theta_t and q.
- Eq. (56) gives `f_hat(s)=10000/[s*(s+100)^2]`.
- Targets: Figs. 2–4, temperature/radial-stress/hoop-stress profiles; closed Laplace expressions in Eqs. (43)–(53).

The paper uses dimensionless illustrative wave/coupling constants. Do not call this a measured copper cylinder or replace them with B01's copper parameters.

### What this can and cannot check

B01 CV and B02 LS share the same classical-stress/entropy + Cattaneo heat-law structure in the common isotropic setting. That relationship was checked analytically from their constitutive/energy equations. **Their plotted cases are not identical:** geometry, loading, boundary restraint and normalization differ. Each source case needs its own configuration.

The inner boundary is not traction-free, unlike the provisional proposed cavity problem. The thermal normal on the inner wall points opposite to increasing r, so a weak-form flux implementation must handle the sign consistently.

B02's displayed GN plots use **type II** (`cK=0`), whereas B01's GN law contains a dissipative k term and corresponds to the type-III structure with `k*=k/tau`. Do not directly claim that B02's GN-II curves validate unmodified B01 GN/MGN predictions. The GL case also changes stress/entropy constitutive terms that are absent from B01's native classical-stress model.

No numerical error or reproduced profile is reported. Published front-speed interpretations are source descriptions; a quantitative check must use the coupled equations/actual characteristic roots and appropriate uncertainty, not force an uncoupled speed to be exact.

## 5. B03 — source tables give quantitative heat-only targets

Source Eq. (2): classical dimensionless diffusion `T_t=laplacian(T)` in the infinite exterior of two circles; initial temperature increment zero. Boundary L2 is zero. Boundary L1 is either one (Table 1) or `cos(phi1)` (Table 2).

- Centre distance rho is the length scale; `Rk=radius_k/rho` and `t=kappa_diffusivity*time_physical/rho^2`.
- `R2=0.3`, with `R1=0.2,0.3,0.5,0.6`.
- Points A/B are specified in local polar coordinates. A consistent derived Cartesian convention places centres at (0,0)/(1,0), giving A=(-1.5,0), B=(2.5,0).
- Reported transient times: `t=1,10,100`; steady values are also tabulated.
- **64 printed reference values** (two tables, four radii, two points, three transient times plus steady value) were transcribed locally and visually checked against rendered PDF pp. 10–11.

Example, **source-reported numerical reference**, not our computation:

```text
Table 1, R1=0.2, R2=0.3, point A, t=1: T_reference = 0.15440.
```

The authors compare their results with COMSOL/steady analytical solutions. That is published mathematical/numerical evidence, not a new physical experiment. Their epsilon=1e-6 (or 1e-5 near the closest cavities) is principally a specified **boundary-approximation diagnostic**, not a universal experimental/project tolerance. Tables print five decimals; printed precision, method error and our future numerical uncertainty must all be considered.

**Important geometry/far-field caution:** the source requires boundedness at infinity. Do not impose a finite cold outer boundary and assume its late-time/steady solution is identical. The two-dimensional long-time behavior and large-domain limit need care. Likewise, negative Table-2 values are relative temperature increments under sign-changing cosine loading—not negative absolute Kelvin temperatures.

This is a thermal-subsystem benchmark, not validation of coupled stress/displacement. No new simulation was performed, and no paper table was independently recomputed.

## 6. Source-quality findings before implementation

### A. Some Table-1 labels reduce to simpler kernels

Under the source's equal-unit parameters and compatible causal histories:

- **MCV5:** `k*N/M = 2k/(1+tau*s)` — CV with effective conductivity 2k.
- **MGN3:** `k*N/M = (k/2)*(1+tau*s)/(tau*s)` — the GN structure with k/2.
- MCV1/MCV2 are the same restricted first-order relaxation family under an appropriate k/tau rescaling, with consistent dimensional/non-dimensional conversion.

These are source-specific algebraic checks, not claims of first discovery or unconditional equivalence for arbitrary extra ICs/unequal component parameters.

MCV2/4/5 have DC conductivity **2k**, while CV/MCV1/3/6 have **k**. Comparing all models at the same component k does not hold total measured static conductivity fixed. Reproduce source comparisons faithfully first, then label matched-conductivity controls separately. GN/MGN laws have a zero-frequency pole, so a measured steady conductivity alone does not identify their full constitutive response.

### B. MGN2 Eq. (36) does not reduce to Eq. (37)

Rendered source PDF p. 7 confirms the mismatch. Setting `k1=k2=k`, `tau1=tau2=tau` in printed Eq. (36) gives the MCV3-like expression, **not** Eq. (37)/MGN2's Table-1 row. Eq. (35) can be independently eliminated to obtain the equal-parameter Eq. (37); see `ANALYTICAL_SOURCE_CHECKS.md`.

**Status: ACTION REQUIRED if MGN2 is chosen.** No source PDF was changed and no correction was silently implemented. This is a source internal-consistency observation, not a claim that a formal publisher erratum exists or that every result is wrong. The focused correction search did not locate a verified relevant correction; absence is not proved. CV/MCV3 source-case planning does not require implementing this ambiguous branch.

### C. Thermal-expansion unit header

Table 2 prints an m/K-style alpha heading, but the source's `gamma=(3*lambda+2*mu)*alpha_theta` stress coupling requires a linear strain-expansion coefficient in **1/K**. The proposed reconstruction interpretation is the same reported value 1.78e-5 with units 1/K, explicitly documented. No input file/model implementation was changed. The unit disposition must be recorded before coding; do not claim a new measured value.

These findings demonstrate why publication/Q1 status cannot substitute for equation/unit checks. This review is not an exhaustive proof/thermodynamic audit of all 12 variants.

## 7. New material/tensor extension is still unapproved

The three numerical source cases are homogeneous/isotropic or heat-only. They do not physically validate a monoclinic beta-Ga2O3 transient-stress prediction. The proposed tensor/material/ellipse problem requires its own derivation, complete C/alpha/capacity/density/conductivity/dynamic inputs, applicability limits and meaningful baselines.

Do not turn scalar conductivity ratios into tensor divisions or assume noncommuting relaxation/conductivity tensors are admissible. No anisotropic modified model was derived/approved here. Recent naming, extra formal time derivatives or a material substitution is not confirmed novelty/significance.

## 8. Proposed next step — not yet authorized

A bounded **Phase-0A-2 feasibility pilot, reference cases only**, could first assess the dimensionless B01 CV and MCV3 case at t*=0.06/tau*=0.04 using source equations/inputs. Its short plan would freeze the source/IC/unit interpretation, diagnostics, reference/digitization route and numerical refinement approach before execution.

**Proposed cap:** 0.5 CPU-hour, no GPU, at most 50 MB newly generated pilot data. This is a proposed maximum budget, not an observed/estimated solver runtime. No pilot has been approved/run. No beta-Ga2O3/elliptical-cavity production is included.

Label any future pilot **PILOT — NOT FINAL VALIDATION**. Full new-project direction/acceptance/method/production approvals still follow v2.1.

## 9. Completion and recovery

**Task:** requested full-source receipt, reading and benchmark compatibility screen.  
**Overall status:** PARTIAL; source identification/access completed, specifications/analytical source checks available, numerical reconstruction/validation unexecuted.

- **Verification:** numerical NOT_STARTED; limited source algebra checks ANALYTICALLY_CHECKED with stated conditions.
- **Physical validation:** NOT_STARTED; these PDFs do not add matched new-material experimental T/stress evidence.
- **Code:** no scientific solver implemented; document/data-handling only.
- **Compute:** zero scientific solver/pilot/production runs.
- **New questions:** initial-history/inversion/reference-uncertainty details; source-issue disposition; exact research/phase approval and full new-material evidence route.
- **Impact:** source-access BLOCKED statuses are resolved; prior source reports retained as history. No numerical results/equations/code in original inputs changed.

Deliverables: this report, `ANALYTICAL_SOURCE_CHECKS.md`, `SOURCE_BENCHMARK_READINESS.xlsx`, `BENCHMARK_CASES.json`, `MODEL_OPERATORS.csv`, local source reference-table transcriptions, source manifests, logs and latest root recovery state.

`RECOVERY_FULL_SOURCE_REVIEW_01.zip` is a cumulative notes/control checkpoint, NOT a final or offline-complete research package. Original PDFs/text/images and complete source-table extractions are excluded pending redistribution-rights review; local paths/identities remain recorded.

**Exact next action:** STOP and wait for explicit authorization of the next scoped plan/pilot task. No additional PDF is required for the first dimensionless Figure-5 reference assessment. Do not execute automatically.
