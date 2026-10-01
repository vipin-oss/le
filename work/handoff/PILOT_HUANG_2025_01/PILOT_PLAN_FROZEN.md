# Frozen pilot plan v1.0 — before numerical solution

Date:30 September2026. Phase: **bounded Phase0A-2 source-case feasibility/verification pilot ONLY**. Label: **PILOT — NOT FINAL VALIDATION**.

## Authorization

The user's `ok do it` directly follows the single explicit proposal: Huang2025 CV+MCV3 1D reference case, cap0.5CPU-hour/noGPU/50MB. It is interpreted as authorization ONLY for that plan/pilot. It does not approve a final research direction, new material/tensor/ellipse model, production or submission.

## Objective and fixed source inputs

Determine whether the specified coupled source case can be reconstructed with checked equations and quantified numerical/graphical uncertainty. Use sourceTable2/Eqs44–66/Fig5:dimensionless t=.06,tau=.04 and reported copper constants in case_input.json.

- Alpha is documented as1.78e-5 **1/K**, required by the source stress equation; header inconsistency noted, number unchanged.
- Causal zero-prehistory/compatible internal-flux histories are the recorded source-reconstruction assumption.
- Gamma=(3lambda+2mu)alpha; beta2=(lambda+2mu)/mu; b=gamma*T0/mu; g=gamma/(rho*cE). No physical k is invented.
- Source mechanical/thermal coupling is retained; M operates on both strain-rate and temperature-rate energy terms.
- No calibration, coefficient/axis scaling or normalization change to improve agreement.
- Scope is dimensionless mathematical/source verification, not a real copper shock experiment or beta-Ga2O3 prediction.

## Methods / independence

1. Published closed-form two-mode Laplace response, independently coded from Eqs63–66; de Hoog numerical inversion.
2. Same PDE written as a first-order characteristic system and evolved by a time-domain finite-volume solver; this implementation does not evaluate Eq66.
3. Spatial first-order matrix eigenmode solution provides a separate Laplace implementation check.
4. Cohen inversion is an algorithm cross-check, not a fully independent model implementation because it shares the closed transform routine.

For MCV3, the scalar transfer  (1+tau*s)/(1+3tau*s+tau^2*s^2) is implemented in the time solver as two positive-weight CV channels. This is an independently derived equivalent **implementation representation**, not a new source/model law. tau_slow=(3+sqrt5)*tau/2, tau_fast=(3-sqrt5)*tau/2; w_fast=(tau-tau_fast)/(tau_slow-tau_fast), w_slow=1-w_fast. Verify the rational identity before use. Zero internal-channel initial states preserve the assumed source history.

Finite-volume variables:strain,e;velocity,v;temperature increment,theta;heat-flux channel(s),qj. Equations:

```text
e_t=v_x
v_t=e_x-(b/beta2)*theta_x
theta_t=-g*v_x-sum(qj_x)
tauj*qj_t+qj=-wj*theta_x
sigma=beta2*e-b*theta
```

At the heated free end, impose theta=1 and sigma=0 via the two incoming characteristics; outgoing/zero characteristics come from the interior. Right-boundary incoming states are zero. DomainL=1 is outside the causal front duringt=.06; verify its characteristic bound before relying on this finite truncation. Displacement is recovered from strain with zero undisturbed right-end displacement.

Python is chosen because workspace MATLAB/Octave are unavailable and these analytical/PDE checks are method-appropriate; the source equations remain unchanged. User hardware is not inferred from workspace resources. This does not choose the final project method.

## Scales, probes and masks fixed before outputs

Use source-driven nondimensional scales (not observed peaks):

```text
S_theta=1
S_sigma=b
S_u=b*time/beta2.
```

Normalized errors are absolute errors divided by these scales; not percentages of a value approaching zero.

The two coupled front positions are derived from characteristic eigenvalues and source constants before solution. Exclude halfwidth .008 around each front from pointwise acceptance/graphical comparisons. This addresses discontinuity/inversion/plot resolution sensitivity, not permission to hide smooth-domain errors. Show the full curves and report global L1 errors, including front regions, separately. Primary masks/probes/grids are fixed in case_input.json.

## Pre-specified pilot diagnostic criteria

These are feasibility diagnostics, not formal new-project acceptance or universal5percent rules.

### Algebra / implementation

- Normalized Laplace PDE, stress-law and boundary residuals at a fixed deterministic complex-s sample set: <=1e-10.
- Formula versus independent spatial-matrix eigenmode transform: <=1e-9 source-scaled difference.
- MCV3 channel-transfer rational identity: <=1e-12 relative/source-scaled error.
- All transport characteristic speeds real to <=1e-10 relative tolerance; positive tau/weights; decaying half-space roots.

### Numerical inversion

- Off-front probe change, de Hoogdegree48 versus64: <=2e-5 in each source scale.
- Off-front algorithm difference, de Hoog64 versusCohen80: <=5e-5 in each source scale.
- Real finite outputs and non-growing far-field tail; any near-front ringing explicitly reported, not clipped.
- Planned degrees32/48/64 are a single refinement study. If numerical inversion diagnostics fail, one documented extension todegree96/high precision is permitted; do not tune source parameters. Two substantive failed critical correction iterations trigger STOP.

### Independent time-domain check

- Finite-volume resolutions800/1600/3200 cells,CFL=.45; no fitted coefficients.
- Final-grid off-front normalized maximum difference from converged Laplace profiles: <=3e-3 for each QoI.
- Finest-pair off-front maximum change: <=3e-3; require refinement evidence or report unresolved/nonmonotonic behavior.
- Global normalized L1 differences, including fronts, must be reported; front smearing is assessed, not silently omitted from all diagnostics. A useful pilot target is <=3e-3; if larger, flag partial numerical resolution.

The3e-3 load-scaled target is chosen to resolve mechanism-level profile changes while keeping numerical uncertainty below/around the source figure's coarse graphical resolution, not to certify a physical material prediction.

### Published Figure5 comparison

Before new outputs, source plots were digitized by a fixed colour mask from embedded raster images, calibrated axes,4pixel column sampling. Colour mappings were read from the legends. These are **figure-derived reference points**, not experimental measurements/original raw solver arrays.

For each available off-front reference point use the conservative representation envelope:

```text
U_graphic = y_bound + abs(source_local_slope)*x_bound.
```

x/y bounds are at least2pixels; add the demonstrated numerical inversion bound and curve interpolation bound (conservatively the3e-3 source-scale numerical allowance for this pilot). Classify compatibility if computed points lie within the combined envelope. Record point count, coverage and mismatches; do not average an inconsistent field into PASS. Fewer than5 usable points or narrow x coverage yields PARTIAL/UNASSESSED graphical support. Original source solver uncertainty is unknown, so even a compatible graph is not exact/raw-data reproduction.

Reference extraction/frame/mask metadata were saved before numerical model results. Any changed extraction/criterion after viewing results must be logged as post-result; no hidden curve/parameter tuning.

## Budget and records

Hard cap1800 aggregateCPU-seconds, noGPU,50MB newpilotdata; reserve10CPU-seconds for unmetered preflight/document setup. Single-thread numeric libraries. Each stage records CPU/walltime,maxRSS,code hashes,input checksum,source hash,environment,status/output paths. The cap is not an observed runtime estimate.

No source PDF is modified; provided FEM4 code remains unchanged. Recovery excludes protected source image/complete figure-derived reference files pending redistribution review; original input location/hash remains recorded.

## Continue / revise / stop

- Continue source-case feasibility only if core equations/units/causal history and numerical checks are coherent.
- Report source-figure disagreement honestly even if independent solvers agree.
- On critical implementation/diagnostic failure, investigate within approved budget; after two substantive failed corrections stop with evidence/options.
- Budget breach stops computation; no further production or new-material step follows automatically.

At pilot end save actual outputs/report/status/recovery state and STOP. Physical validation, novelty/significance, final research direction/journal and beta/ellipse production remain unapproved/unexecuted.
