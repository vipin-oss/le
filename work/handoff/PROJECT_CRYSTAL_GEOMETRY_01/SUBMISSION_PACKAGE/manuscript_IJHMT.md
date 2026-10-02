# MANUSCRIPT DRAFT v1.0 — numbers-polished (30 Sep 2026)
Journal-agnostic IMRaD (targets per JOURNAL_SCREENING.md; journal choice USER-OWNED,
open). All numbers verified-pipeline outputs (data/VERIFY.json, data/PROD/, data/
ANALYSIS.json). Stresses are per unit wall-pulse amplitude θ_amp (linear theory);
multiply by θ_amp in kelvin (worked example θ_amp = 10 K).

---

## Title
Crystal orientation versus cavity shape in transient thermoelasticity of monoclinic
β-Ga₂O₃: a covariance-verified computational study with thermal-memory sensitivity

## Abstract
Coupled transient thermoelasticity around cavities in low-symmetry crystals entangles
crystal anisotropy, cavity shape, and thermal memory. We separate these effects with a
verified conservative flux-form harmonic solver for monoclinic β-Ga₂O₃ (plane strain,
a-c plane; full 13-component Cij and off-diagonal conductivity K13) around circular and
equal-area elliptical (χ=2) cavities under a wall-temperature Gaussian pulse (t0=2.5 t_th,
tw=1.2 t_th). Verification: discrete rotation covariance 6.3×10⁻¹⁴ (machine class),
steady log-law 9.5×10⁻⁶, static thermoelastic annulus closed form 0.68% (V0–V7 suite).
Results for unit pulse amplitude: (i) the circular cavity peak hoop stress is
rotation-invariant (0°/90° identity 4×10⁻¹⁰; pattern non-axisymmetric, m2/m0=0.085);
(ii) the elliptical cavity converts crystal orientation into a 33–37% peak-stress
modulation (1.13–1.67 MPa/K over φ∈[0°,165°]; robust to grid (192×96) and to numerical
damping η_d∈[0.02,0.1]); (iii) thermal-memory deviation D grows with Λ=τκ/a² from
3×10⁻⁴ (Λ=0.03) to 0.10 (Λ=3.2) but does NOT collapse in Λ alone — equal-Λ pairs
differing in ε=κ/(c_ref a) split by 3.5×, refuting the pre-registered strong-similarity
hypothesis at the 25% level; a two-parameter (Λ,ε) validity map is required;
(iv) thermoelastic feedback on the temperature field is 2.2×10⁻⁴ (≈0.2δ, δ=1.1×10⁻³),
within the pre-registered 5δ bound. Relaxation times are hypothetical (dimensionless
study); physical validation data do not exist for this system.

## Keywords

thermoelasticity; thermal shock; anisotropic crystals; cavity; thermal waves; generalized thermoelasticity

## 1. Introduction
Thermal stress concentration around holes is classical [1,2].
Extensions cover anisotropic solids with elliptic boundaries by analytic methods
[3], generalized-thermoelastic cavity problems with
circular geometry ([4]; orthotropic cylindrical cavity family; [5]), and hole-shape effects on
thermal SCF in composites [6]. Within a bounded literature search (log
2026-09-30) no study was located combining: low-symmetry (monoclinic) crystal tensors,
a circle-vs-ellipse comparative design, transient wall-thermal loading, and generalized
(thermal-memory) conduction with a size/validity map. We study exactly this combination
for β-Ga₂O₃, a wide-gap semiconductor of current device interest, whose monoclinic
elastic tensor includes the shear–normal couplings C15, C25, C35, C46 and whose a-c
plane conductivity has a measurable off-diagonal term K13.

Claims are restricted to verified computation: no experimental transient cavity data
for β-Ga₂O₃ exist (recorded), so this is not a physically validated study.

## 2. Problem statement and materials
Plane strain along the crystal b-axis; cross-section = a-c crystal plane; central
circular cavity (radius a) or equal-area ellipse (semi-axes a√χ, a/√χ, χ=2); outer
boundary circle R=80a (elastic round trips 8.1 t_th longitudinal / 14.9 t_th shear
exceed the analysis window t≤6 t_th); wall-temperature Gaussian pulse θ_w(t)=exp(−((t−
t0)/tw)²), t0=2.5 t_th, tw=1.2 t_th, t_th=a²/κ̄; traction-free cavity; u=0, θ=0 outer;
zero ICs. Crystal orientation φ∈{0°,15°,…,165°}: all of K, C, β rotated together.

Governing equations (harmonic, e^{iωt}):
  (C:ε(u) − βθ)_,j + ρω²u_i = 0,
  ∇·(K g(ω) ∇θ) = iω[ρc_E θ + T0 β:ε(u)],
with g(ω)=1 (Fourier), (1+iωτ)⁻¹ (Cattaneo–Vernotte), ½(1+iωτ/2)⁻¹+½(1+iω2τ)⁻¹
(MCV3-type; models reviewed in [9]); τ HYPOTHETICAL ({1,5,20} ps sweep).

Materials (β-Ga₂O₃, sourced/estimated per PARAMETER_TABLE.md): 13 Cij from Adachi et al. [7] (JAP 124, 085102; full-text VoR; e.g. C11=242.8, C22=343.8, C33=347.4,
C44=47.8, C55=88.6, C66=104.0 GPa; C15=−1.62, C46=5.59 GPa); K(a-c)= [[12.13,−0.992],
[−0.992,14.09]] W/mK [8]; α_a=1.54, α_c=3.15×10⁻⁶ K⁻¹ (powder XRD, 2015 [10];
α5 unmeasured → 0, LIMITATION); ρ=5880 kg/m³; c_p ESTIMATED ≈560 J/kgK (Debye Θ_D=685 K [11];
sensitivity 500/560/700 recorded); T0=293 K. Derived: c_ref=7686 m/s, κ̄=3.959×10⁻⁶
m²/s, δ=T0|β|²/(ρc_p C̄)=1.08×10⁻³, ε=κ̄/(c_ref a), Λ=τκ̄/a². Isotropic control:
K_iso=13.11·I, λ=128, μ=104 GPa, β_iso=(3λ+2μ)α.

## 3. Numerical method and verification
Body-fitted algebraic grid (γ=3.5 exponential radial clustering; 96×48 production).
Spatial operators are conservative flux forms on the mapped grid (contravariant thermal
operator; Thompson identity for the displacement divergence) assembled from central
differences of the coordinate arrays so that mixed partials commute exactly (patch
identity). Harmonic solves (SuperLU) with row equilibration; time series by Gaussian-
spectrum synthesis (21 frequencies, ω≤20/t_th, 128 time points, window 8 t_th). A
hysteretic damping η_d=0.05 on Q regularizes undamped finite-domain resonances in
dynamic runs (statics undamped); QoIs shift ≤0.2% for η_d∈[0.02,0.1]. The cavity wall
value being Dirichlet-prescribed, the feedback probe uses the interior field (r≈2a).

Verification suite (pre-registered V0–V7, 403 CPU-s): V0 metric consistency 0.41% (2nd-
order mapped FD); V1 stencil dispersion 1.3% at kh=0.4; V2 grid convergence PARTIAL —
96 vs 192 med-fine 2.35% (circle) / 6.80% (ellipse), handled per plan with per-quantity
uncertainty + 192×96 confirmatory spot checks; V3 rotation covariance (90° circle
automorphism) 6.26×10⁻¹⁴; V3b 37° covariance (interp) 0.26%; V4 uncoupled null exact 0;
V5 τ→0 limit 1.09×10⁻⁷; V6 steady log-law max err 9.5×10⁻⁶; V7 static uniform-θ
annulus vs closed form 0.68% (traction residual 2.6×10⁻¹⁵). Honest history: an earlier
composed first-derivative Laplacian carried a parity null mode; all results of that
phase were discarded and re-earned (project CHANGELOG 2026-09-30; see Reproducibility).

## 4. Results
### 4.1 Orientation × shape (Figs. 1, 4; Table 1)
Circle: |σ̂(φ)| = 0.9654–0.9684 MPa/K (mean 0.9666, scatter 0.30% = peak-sampling on a
flat maximum; the 0°/90° discrete-rotation identity holds to 4.0×10⁻¹⁰ and the field
covariance to 6.3×10⁻¹⁴). The field is nonetheless non-axisymmetric (m2/m0=0.085).
Ellipse: σ̂(φ) spans 1.125–1.668 MPa/K — amplitude 36.6% of the mean at 96×48, 32.7% at
192×96 (RESOLVABLE ≫ pre-registered max(5×noise, 2%)=2% threshold; robust to η_d,
spread ≤0.2%). Peak angles θ* rotate with the pattern for the circle; for the ellipse
θ*(φ) is steered by the crystal–shape interplay (Table 1). Isotropic control: circle
1.054, ellipse 1.763 MPa/K (χ=2 amplifies without any crystal anisotropy).

Table 1 — peak |σ̂| (MPa/K) vs φ (96×48):
φ°  | circle | ellipse
0   | 0.9655 | 1.3973
15  | 0.9654 | 1.5525
30  | 0.9662 | 1.6227
45  | 0.9668 | 1.5314
60  | 0.9667 | 1.4566
75  | 0.9659 | 1.2647
90  | 0.9655 | 1.1255
105 | 0.9662 | 1.3705
120 | 0.9675 | 1.5826
135 | 0.9684 | 1.6644
150 | 0.9680 | 1.6685
165 | 0.9667 | 1.5883

### 4.2 Thermal memory (Fig. 2; Table 2)
D(Λ)=max_t|σ̂_CV−σ̂_F|/σ̂_F (circle, φ=0):
Λ     | τ (ps) | a (nm) | D
0.0317| 20     | 50     | 3.39×10⁻⁴
0.0396| 1      | 10     | 1.54×10⁻³
0.1979| 5      | 10     | 7.36×10⁻³
0.1979| 20     | 20     | 2.10×10⁻³
0.7918| 20     | 10     | 2.06×10⁻²
3.167 | 20     | 5      | 0.1031
Within each size family D increases monotonically with Λ (span 3×10⁻⁴→0.10). The two
equal-Λ (Λ=0.198) points differ 3.5× because ε=κ̄/(c_ref a) differs — the pre-registered
strong-similarity hypothesis (collapse vs Λ alone, ≤25% residual) is REFUTED; the data
require a two-parameter (Λ,ε) description. This is a negative confirmatory result,
reported as registered. MCV3-type vs CV at equal τ differ by ≤0.2% in σ̂ in this
parameter window (τ=20 ps: −0.9692 vs −0.9709 MPa/K).

### 4.2b Worked dimensional examples (Table 3)
All response quantities are reported per unit pulse amplitude and vs (Λ,ε); the map
applies for any c_p since (Λ,ε) absorb it. Worked example (circle, φ=0, a=10 nm,
τ=20 ps): c_p∈{500,560,700} J/kgK (sensitivity band) gives t_th∈{22.6, 25.3, 31.6} ps,
Λ∈{0.887, 0.792, 0.633}, ε∈{0.0577, 0.0515, 0.0412} (exact algebra on sourced k̄, ρ;
data/SUPP_cp_worked_example.csv). Peak hoop stresses scale linearly with pulse
amplitude: at θ_amp=10 K the circle peak is 9.67 MPa (orientation-invariant), the
ellipse spans 11.25–16.69 MPa over φ (isotropic control: circle 10.54, ellipse 17.63
MPa). Full per-run values: data/SUPP_phi_sweep.csv, data/SUPP_D_lambda.csv.

### 4.3 Coupling feedback (Fig. 3-left)
|θ_on−θ_off|(r≈2a)/|θ| = 2.17×10⁻⁴ ≤ 5δ = 5.39×10⁻³ (δ=1.08×10⁻³) — WITHIN the
pre-registered bound; feedback is ≈0.2δ, i.e. physically negligible in this regime
(pre-registered null-type claim H4, confirmed).

### 4.4 Angular content (Fig. 4; H5 exploratory)
m2/m0 of the wall hoop at peak: isotropic circle 5.2×10⁻¹¹ (exact null), anisotropic
circle 0.085, isotropic ellipse 0.204, anisotropic ellipse 0.309 — the
anisotropy×shape interaction raises the leading non-axisymmetric mode beyond each
single factor (exploratory trend, consistent with H5).

## 5. Discussion
Verification ≠ physical validation: no transient/cavity experimental data for β-Ga₂O₃
were located; the elastic/transport inputs are measured, the response predictions are
verified-computation only. Other limits: τ_q hypothetical (dimensionless study label);
α5=0 (unmeasured shear expansion); c_p estimated (sensitivity recorded; Λ,ε axes are
c_p-aware); continuum flag a≥5 nm; linear small-strain, ΔT/T0≪1; V2 PARTIAL grid
uncertainty (ellipse ±6.8% on σ̂) carried into T4 as a robustness check (conclusion
unchanged at 192×96); η_d=0.05 damping is a documented regularization (≤0.2% effect);
R=80a replaces the pre-registered 25a whose causal claim fails (D015, logged before
production outputs). The circle's 0.30% peak scatter is argmax sampling on a flat
maximum, not covariance failure (field-level identity is machine-class).

## 6. Conclusions
(1) For a circular cavity in a monoclinic crystal the peak thermoelastic hoop stress is
orientation-invariant by a discrete-rotation identity, while the field is
non-axisymmetric — an exact, machine-checked symmetry statement. (2) Equal-area
ellipticity breaks this: peak stress varies 33–37% with crystal orientation, robust to
grid and regularization — a resolvable shape×crystal symmetry mismatch effect.
(3) Thermal-memory deviations grow monotonically with Λ within size families but obey a
two-parameter (Λ,ε) law, not a single-parameter collapse (pre-registered strong form
refuted). (4) Thermoelastic feedback on temperature is bounded by ≈0.2δ and negligible.

## Reproducibility
Code, inputs, per-run series, scripts, logs, and sha256 manifest: RECOVERY_CRYSTAL_
GEOMETRY_01.zip (121 files; no third-party PDFs). Environment: Python 3.13, numpy/
scipy/matplotlib (exact versions to record at submission). AI-assisted self-audit ≠
peer review — expert review recommended before submission (recorded).

## References

[1] Florence, A.L., Goodier, J.N. (1959). [TITLE to be completed from source record].
J. Appl. Mech. 26, 293-294. (verification level: metadata; see project
PRIOR_WORK_COMPARISON_R2.md).

[2] Florence, A.L., Goodier, J.N. (1960). [TITLE and pages to be completed from source
record]. J. Appl. Mech. (1960 follow-on; verification level: citation-trail).

[3] Chao, [initials], Gao, [initials] (2001). [TITLE to be completed from source
record]. Int. J. Solids Struct. 38, 5975-5994.
DOI: 10.1016/S0020-7683(00)00403-0. (verification level: abstract).

[4] [AUTHOR NAMES to be completed from source record] (2015). [TITLE to be completed] -
dual-phase-lag thermoelastic response of a fiber-reinforced medium with a circular hole.
Mech. Adv. Mater. Struct. 43(4). DOI: 10.1080/15397734.2015.1029589.
(verification level: abstract+keywords).

[5] Karmakar, S., Sur, A., Kanoria, M. (2016). [TITLE to be completed] - DPL spherical
cavity problem. DOI: 10.1134/S002189441604009X. (verification level: abstract).

[6] Jafari, [initials] (2019). [TITLE to be completed] - perforated composite plate,
hole-geometry effect on thermal stress concentration. J. Compos. Mater.
DOI: 10.1177/0021998318795279. (verification level: metadata+snippet).

[7] Adachi, [full author list to complete] (2018). [TITLE to complete] - complete
second-order elastic tensor of monoclinic beta-Ga2O3. J. Appl. Phys. 124, 085102.
DOI: 10.1063/1.5047017. (verification level: full text).

[8] Klimm, G. et al. (2023). [TITLE to complete] - thermal-conductivity tensor of
beta-Ga2O3 including K13. Cryst. Res. Technol. DOI: 10.1002/crat.202200204.
(verification level: full text).

[9] Tzou, D.Y. (1995). Macro- to Microscale Heat Transfer: The Lagging Behavior.
Taylor & Francis. (canonical multi-phase-lag/DPL reference).

[10] [Powder XRD thermal-expansion study of beta-Ga2O3, 2015 - reference to be
completed from project provenance record, PARAMETER_TABLE.md.]

[11] [beta-Ga2O3 heat-capacity/Debye-temperature study, ACS Omega, 2021 - reference to
be completed from project provenance record.]


## Appendix A. Nomenclature

| Symbol | Meaning | Units |
|---|---|---|
| a | cavity semi-axis (radius for the circle) | m |
| C, C_ij | elasticity tensor and its components | Pa |
| c_E | specific heat at constant strain | J/(kg K) |
| c_ref | reference speed, sqrt(C/rho) | m/s |
| D(Lambda,eps) | memory deviation of sigma-hat from its tau=0 baseline | - |
| g(omega) | thermal kernel (Fourier / CV / MCV3-type) | - |
| K, k-bar | conductivity tensor (W/m K); scalar level | W/m K |
| m0, m2 | even angular modes of the temperature field | K |
| R | outer-domain radius | m |
| t, t_th | time; thermal time a^2/kappa | s |
| u, traction | displacement; traction | m; Pa |
| beta | thermal-stress coupling tensor | Pa/K |
| delta | coupling parameter T0|beta|^2/(rho c_p C-bar) ~ 1.1e-3 | - |
| eps | size number kappa/(c_ref a) | - |
| theta, theta_amp | temperature rise; pulse amplitude | K |
| kappa | scalar thermal diffusivity | m^2/s |
| lambda, mu | isotropic Lame constants | Pa |
| rho | mass density | kg/m^3 |
| sigma, sigma-hat | stress; peak hoop stress per unit theta_amp | Pa/K |
| tau | relaxation time (hypothetical sweep) | s |
| phi | crystal/cavity orientation angle | deg |
| chi | material set (0 = anisotropic, 1 = isotropic) | - |
| omega | angular frequency | rad/s |
| Lambda | thermal number tau*kappa/a^2 | - |
| eta_d | hysteretic damping regularization parameter | - |

## Declarations

**CRediT authorship statement:** [AUTHOR LIST AND CONTRIBUTION ROLES - to be completed
by the authors]

**Data availability:** All computational inputs, code (Python/NumPy/SciPy), per-run
outputs and analysis scripts underlying this work are archived in the project
reproducibility package (RECOVERY_CRYSTAL_GEOMETRY_01.zip with SHA-256 manifest).
[AUTHORS TO CONFIRM public deposition + insert repository DOI.]

**Conflicts of interest:** [AUTHORS TO DECLARE - currently: none known]

**Funding:** [AUTHORS TO DECLARE - currently: none]

**AI-use disclosure (TEMPLATE - authors must review, edit and confirm; journal policy
governs):** During the preparation of this work the author(s) used AI assistance
(agentic coding and drafting tools) in order to develop and verify the numerical
implementation, perform the data analysis, and draft figures and manuscript text. The
author(s) have reviewed and edited the content and take full responsibility for the
content of the publication. [NOTE: IJHMT (Elsevier) requires disclosure of AI use in
the writing process - check the current Guide for Authors at submission.]

**Supplementary material:** SUPP1-SUPP4 (Tables S1-S3, worked example) cited in the text.

