# Phase 3 — Mathematical audit

Scope: re-derive the constitutive algebra, every printed analytical identity, and the conventions of the
discretisation, the kernel and the inversion against the shipped code; correct what is wrong; keep the record
of what is merely uncomfortable. No experimental or physical validation is claimed anywhere in this phase:
everything below is algebra, arithmetic or a numerical consistency check of the model as written.

Status: **complete for the audit itself** (harness green, document corrections applied, rebuilt and gated).
Two items are carried forward: the verification-suite re-run (in flight, §8) and one unresolved model input
(§9, author-owned).

Sandbox note: this directory was deleted by a sandbox reset during the phase and has been rebuilt from the
committed state (`6d62242` on `arena/01a10176-le`). The audit harness that exists here
(`verification/audit_phase3.py`) is therefore the re-created one, and the numbers in this report are the
numbers it prints. Findings that the re-created harness does not reproduce are listed in its own
`not_reproduced` field and named in §7, rather than being quoted from a run whose script no longer exists.

## 1. What was checked, and how

`verification/audit_phase3.py` runs 25 checks: 22 PASS, 3 INFO, 0 FAIL. It imports the shipped modules
(`cg_model`, `cg_grid`, `cg_ops`, `cg_bromwich`) and, for the printed conventions, the manuscript builder
itself (`ms_static`), so a check that passes proves the document and the code say the same thing. Symbolic
checks use sympy. It writes `verification/AUDIT_phase3.json` and `verification/audit_phase3.log` and is
read-only with respect to everything else.

The structure follows the audit's four parts: **A** constitutive algebra and material scales, **B** analytic
identities, **C** conventions of the numerics and the inversion, **D** provenance of what the documents print.

## 2. Part A — constitutive algebra

- **A1** The 3×3 plane-strain block `Q` and the thermal vector `beta` are exactly the stated combinations of
  the thirteen constants: assembled independently, `max|assembled − used| = 0` for both; `Q` is symmetric to
  0 and its eigenvalues are 8.8507e+10 / 1.2686e+11 / 4.6343e+11 Pa, all positive.
- **A2** The four odd constants (C15 = −1.62, C25 = 0.36, C35 = 0.97, C46 = 5.59 GPa) are present and
  nonzero, so the block is not orthotropic: the shear couples to the normals through C15 and C35. That
  coupling is what the 2φ orientation dependence in Section 2.1 of the manuscript rests on, and the audit
  confirms the dependence is genuine rather than an artefact of the reduction.
- **A3** `alpha_5 = 0` is the only shear assumption inside `beta`; with it, `beta_13` = 1.7739e+03 Pa/K. A
  value of `alpha_5` of the size of `alpha_1` would add 1.4e+05 Pa/K, i.e. 8.6 % of the largest component of
  `beta`. The documents keep this as a stated limitation (§9), not as a result.
- **A4** The scales in Section 2.3 reproduce: c_ref = √(C33/ρ) = 7686.5 m/s, κ̄ = √det K_ac/(ρ c_p) =
  3.958828e−06 m²/s, which gives t_th = a²/κ̄ = 25.26 ps at a = 10 nm and 631.5 ps at 50 nm, |β| =
  2.0517 MPa/K, and δ = T₀ β:β/(ρ c_p C̄) = 1.078201e−03 — the printed 1.078e−03.
- **A5** Over the 72-orientation lattice the reduced block is π-periodic to 3.36e−17 relative and positive
  definite everywhere, with smallest eigenvalue 6.4021e+10 Pa at 45°. This is what licenses keeping half the
  lattice in the production sweep, and the periodicity is now stated where the lattice is defined.
- **A6** (INFO) δ: the builder's weighted triple — the contraction with the engineering-shear entry counted
  twice — has relative spread 2.0e−15 over the lattice, i.e. it is the invariant; the 1-norm instance is what
  the text prints, and the β:β form is a factor 1.59 larger. Section 2.2 now states the convention instead of
  leaving the reader to guess which contraction a number came from. The harness recomputes both from
  `cg_model` and agrees with the builder to machine precision.
- **A7** (isotropic control) The control is matched by construction: K_ac eigenvalues 11.716 / 14.504 W/mK,
  mean 13.110 = the control's isotropic value, √det = 13.036. The conductivity block's own anisotropy is
  23.8 %, so "matched modulus" means matched mean, and the ablation label in the document says CONTROL rather
  than a material claim — unchanged, confirmed.
- **A8** (INFO) C̄ = C33 = 347.4 GPa is 89.3 % above the Voigt bulk average of the full 6×6 (183.53 GPa). The
  text uses C33 as a reference modulus for nondimensionalisation and does not call it the bulk modulus; the
  audit checked that no sentence implies otherwise. None does.
- **A9** The rotation is covariant only with the 2026-10-01 cross-term sign fix: the rotated C′23 at 45°
  differs by 0.72 % of its own value between the two conventions (9.9810e+10 against 9.9090e+10 Pa), and the
  suite's covariance test is what pins the fixed form. The sign error and its correction remain in the
  record, in the body of the manuscript, not in a footnote.

## 3. Part B — analytic identities

All PASS, computed rather than transcribed: the kernel low-frequency expansions (CV = 1 − sτ + (sτ)²,
MCV3 = 1 − 5/4 sτ + 5/2 (sτ)², whence τ_eff = 1.25 τ); Re g on the Laplace line for both kernels
(1/(1+x) and (3x+2)/(2(4x+1)) with x = (ωτ)², both strictly positive); the orientation map as an orthogonal
involution (TᵀT = I, T² = I), which is why the response carries 2φ and is π-periodic; the central staggered
first-derivative symbol (sin z = z − z³/6, second order); the one-sided three-point stencils at both ends of
the radial direction (the weights −3/2, 2, −1/2 divided by h are the unique set exact on 1, u, u², with error
−2h² = (h²/3)f‴ on u³); and the grid map (ρ(0) = 0, ρ(1) = 1, monotone, dρ/dξ = 0.0339 at ξ = 0 and
increasing: the clustering is at the cavity, min J = 1.885 > 0).

**New finding carried to Phase 4 (B1 detail).** The two kernels are matched at first order only: their
second-order coefficients differ (1 for CV against 5/2 for MCV3). Any sentence that reads as though the
three-pole form reproduces the single-pole kernel beyond the leading term must say which order it means.

## 4. Part C — conventions of the numerics and the inversion

- **C1** The Bromwich plan as shipped: T = 20, γ_B = 0.9, t₀ = 2.5, t_w = 1.2, ε = 1e−10 give
  w_max = 8.0480 1/t_th, K = 26, i.e. 27 solves of the harmonic system per run, with periodisation alias
  exp(−γ_B T) = 1.5230e−08. These are the numbers the method section prints.
- **C2** The validity window was a hard-coded `T − 5.5`. It is now the formula that number instantiates,
  `t_valid_max = T − (t₀ + 2.5 t_w)`: 14.5 t_th at the baseline t_w = 1.2 — the value already printed, so no
  stored run and no reported value moves — and 11.5 t_th at t_w = 2.4, the wide-pulse case used in the
  locality test, which the hard-coded bound over-allowed by 3 t_th. The documents state the rule and both
  numbers.
- **C3** The bound is a bound, not a convenience: exp(+γ_B T) times the Gaussian pre-history at the read
  limit is 1.06e−14 at t_w = 1.2 and 9.22e−09 at t_w = 2.4, while the reconstruction's own growth is
  exp(γ_B t) = 221.4 at t = 6 and 4.9e4 at t = 12.
- **C4** With unit transfer the inversion returns the prescribed pulse to 3.6e−11 on 1 ≤ t ≤ 6 t_th and
  6.9e−08 over the whole valid window. The text's "better than 1e−8, and 1e−10 for t ≤ 6" is accurate on the
  core window; the far tails are limited by the truncation of the evaluation line, and the wording now
  reflects that.
- **C5** The operators' finite-difference metrics against the grid's analytic ones: 4.4e−04 over the whole
  grid, 2.1e−04 over the interior rows, 1.4e−05 on the wall row. This is the distinction behind the one INFO
  finding (§7): an O(1) first row in a refinement probe is the probe's own one-sided derivative, not the
  scheme's order.
- **C6** (INFO) A uniform temperature gives exactly zero discrete body force by construction, because the
  thermal load is kept outside the flux as β·∇θ. Recorded as the reason the patch test cannot fail, and
  therefore as a reason not to cite it as evidence of accuracy.
- **C7** Document state: the computed train mean t_w√π/T = 0.1063 (printed 0.106) appears where the DFT
  comparison is made in both documents, and the strings `0.27 of the peak`, `frozen criterion`,
  `frozen threshold`, `frozen bound`, `earlier internal analysis`, `MASTER_PROMPT`, `pre-registered` and the
  placeholder `n/a` appear in neither.

## 5. Part D — provenance

- **D1** 54 bibliography entries, all keys distinct, and the reference count printed by the builder agrees
  with the file. Key-by-key linkage is the cross-reference gate's job and it passes.
- **D2** All eight figure files the manuscript references exist at the paths printed in it.
- **D3** The builder's structure counts for the manuscript: 84 equations, 8 figures, 11 tables, 9 sections,
  41 subsections, 54 references, abstract 249 words (limit 250), body ≈10 437 words, highlight lengths
  [78, 70, 69, 74, 69] (limit 85).

## 6. What changed in the deliverables

Manuscript and companion are both generated, so every correction went into a builder
(`ms_static.py`, `ms_derivation.py`, `ms_numerics.py`, `ms_results.py`, `build_manuscript.py`,
`build_calculations.py`) and the documents were regenerated; nothing was hand-edited into a `.md`.

1. Section 2.1 gained the plane-strain-class paragraph; Section 2.2 gained the δ norm sentence (§2, A6).
2. Eq. (33) prints `\Vert … \Vert` (the mathtext subset has no `\lVert`), and a `c_ref` typo was corrected.
3. The DFT comparison prints the computed 0.106 instead of the typed 0.27, in both documents.
4. Section 4.4/4.6 and companion §4.1 state the validity bound as a formula (§4, C2).
5. Internal designations removed throughout (Table 4 provenance and caption, the criterion and threshold
   wording, the ablation caption, the Section 9.1 file list, which is now computed from the manifests).
6. The AI disclosure was split the way the journal requires: writing use in the declaration before the
   references, code and simulation use in the numerical-methods section, with an explicit statement that no
   AI tool produced or selected a reported number and that AI is not an author or a cited source. The hand
   maintained cover letter was aligned with it.
7. `build_manuscript.py` aborts if the abstract or a highlight contains `n/a`; §7 explains the one real
   incident where that guard was the difference between a stale build and a wrong one.
8. `cg_bromwich.py`: the computed `t_valid_max`, and the module header states the pulse-width dependence.
9. `CODE_FREEZE_submission_2026_10_03c.json` (27 files, all verified byte-identical) is quoted by both
   documents; the three earlier manifests are unchanged on disk, as history.

## 7. Negative and uncomfortable results, kept

- **C1b, one-sided metric probe (INFO, deliberately not "fixed").** A refinement probe at the wall rows
  shows O(1) convergence in the first row while the interior is clean second order (order 2 across the
  interior rows). The cause is the probe: the metric derivatives at χ = 0 and η = 0 are one-sided, and B5
  above proves those stencils are themselves second order on a quadratic. The finding stays in the record
  because a reader reproducing the probe will see the same first row.
- **A6, the δ ambiguity was introduced by the documents, not by the code.** Before this phase the printed
  value could be read as either of two contractions that differ by a factor 1.59. The number was always
  correct for the convention the builder uses; what was missing was the convention.
- **The `n/a` incident.** A build performed while `07_Tests/run_tests.py` was rewriting
  `TEST_RESULTS.json` propagated `n/a` into a table, and once the guard existed, later builds correctly
  refused to overwrite. Diagnosis first, then the guard: the fix was the build ordering rule (never build
  while the suite is writing), not the table logic; the table logic was already right, and the earlier
  suspicion that the builder's path resolution was at fault was wrong and is recorded as wrong here.
- **Nothing was re-tuned.** No reported value was changed to improve an appearance; the only numerical
  change in the code path (C2) leaves the baseline identical by construction.

## 8. Verification status

`PAPER_PROJECT/07_Tests/run_tests.py` (28 cases) is being re-run with the Phase-3 code change present, in the
sandbox, as `verification/suite_rerun_20261003b.log`. Two earlier attempts — one before the first sandbox
reset, one after — were interrupted; the completed run of the same code before the resets ended
27 PASS, 0 FAIL, 1 INFO (the exploratory non-aligned case), which is what §7 reports. This phase does not
claim the suite passed until its own log says so; the outcome and its timing belong to the freeze record
that Phase 8 closes.

## 9. Open, author-owned

`alpha_5 = 0`: one thermal expansion component is unresolved in the source literature as far as this work
could establish. A3 above quantifies what a value of the size of `alpha_1` would do to `beta_13` (8.6 % of
the largest component). This is not closable by computing: it needs the authors to decide whether to keep the
limitation as stated, or to add a sensitivity run at a bounded `alpha_5`, or to soften one sentence.

## 10. Reproducing this phase

From the repository root, with the project environment (numpy, scipy, matplotlib):
`python3 Phase_03_Mathematical_Audit/verification/audit_phase3.py` re-runs all 25 checks and rewrites
`AUDIT_phase3.json`; `sh bootstrap_paths.sh` first, if the `PAPER_PROJECT` symlink is absent. The document
edits are replayable with `verification/patch_phase3_batch1.py` and `patch_phase3_batch2.py`, both
idempotent; after any builder edit, regenerate the code freeze last, then rebuild — and never rebuild while
the suite is writing its results (§7).
