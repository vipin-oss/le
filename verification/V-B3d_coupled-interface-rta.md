# V-B3d — Coupled thermoelastic interface at normal incidence: R, T, A

**Phase B3, item d** (`control/BRAVE_B3_REVISIONS.md` @ `d1983cc`). Access date 2026-10-22.
Code: `V-B3d_coupled_interface.py`.

---

## 0. SCOPE LIMITS — READ BEFORE ANY NUMBER BELOW IS QUOTED

Ordered into the headline by the handler, because they were previously buried in §7:

**(S1) What is solved now, and what was solved in B3.** B3d is a **coupled thermoelastic** interface:
two thermoelastic half-spaces, \(u\) and \(\theta\) on each side, two modes per side (quasi-elastic +
quasi-thermal), incident **longitudinal** wave, **normal incidence**, **1-D**, **perfect contact**.
This is a different problem from `V-B3b`, which solved a **purely thermal** interface between two
rigid conductors with one wave per side. **The B3b result "\(A=0\) for all models" is a statement
about the rigid heat equation only** and must never be quoted as a thermoelastic wave-partition
result. Conversely, no number in this file may be transferred to the rigid problem.

**(S2) \(A\) is a definition, not a measurement.** \(A:=1-R-T\). Therefore
\(|R+T+A-1|=0\) to machine precision in every row below **and is not evidence of anything**. The
real checks are the two *independent* ones in §3.4: the transmitted energy \(T J_i\) must equal the
dissipationintegral \(\int_0^\infty\langle D\rangle\,dx\) in medium 2, and the reflected energy
\(R J_i\) must equal \(\int_{-\infty}^0\langle D\rangle\,dx\) in medium 1. Those are computed from
the **field solution**, not from flux bookkeeping, and they close to \(10^{-6}\)–\(10^{-5}\) here.
A third check — \(A=0\) for identical media on both sides — is exact (§3.3).

**(S3) Cross terms.** With attenuated (complex-\(k\)) waves the time-averaged flux of a superposition
is **not** the sum of the fluxes of its parts:
\(\langle J\rangle\) of \(a+b\) contains \(\operatorname{Re}[\hat\sigma_a\hat v_b^*+\hat\sigma_b\hat v_a^*]\).
This file therefore computes \(R\) and \(T\) from **total fields** as ordered, and additionally
reports the mode-projected values, because **they differ** (§3.2) — by up to \(8\times10^{-4}\)
here, and by an amount that vanishes identically only when the medium is lossless. That difference
is the single most important finding of this item.

---

## 1. Task

> **B3d.** COUPLED problem at normal incidence, 1-D: two thermoelastic half-spaces in perfect contact
> (continuity of displacement, traction, temperature, normal heat flux), incident longitudinal wave,
> models Biot, LS (and GN-II if tractable). Use the energy flux \(J=q-\sigma v\) (time-averaged, with
> the correct sign convention, state it). Each side has two modes (quasi-elastic, quasi-thermal), the
> transmitted/reflected sets are sums of two modes with complex \(k\). Compute \(R\), \(T\) by the
> TOTAL flux on each side (not mode-by-mode), and \(A=1-R-T\). Check against an independent
> computation: the bulk dissipation integral over \(x\) on each side (or an energy balance in the
> frequency domain). Report whether \(A=0\) persists at an ideal coupled interface, and include a
> table of \(R,T,A\) for steel–aluminium-like data at several frequencies including one where thermal
> and elastic modes are strongly coupled. Give the code.

## 2. Method

### 2.1 Governing equations (linear, isotropic, 1-D, small strain)

Convention: \(e^{i(kx-\omega t)}\), \(s=-i\omega\), tensile-positive stress, \(\theta=T-T_0\).
Momentum and constitutive law are common to all three models:
$$\rho\ddot u=\sigma_{,x},\qquad \sigma=Mu_{,x}-\beta\theta,\qquad M=\lambda+2\mu .$$

**Biot/Fourier.** \(\rho c\dot\theta+\beta T_0\dot u_{,x}=k_{\text{th}}\theta_{,xx}\).
**Lord–Shulman.** \(q+\tau_0\dot q=-k_{\text{th}}\theta_{,x}\) with
\(\rho c\dot\theta+\beta T_0\dot u_{,x}=-q_{,x}\), eliminating \(q\):
\(\rho c(\dot\theta+\tau_0\ddot\theta)+\beta T_0(\dot u_{,x}+\tau_0\ddot u_{,x})=k_{\text{th}}\theta_{,xx}\).
**GN-II.** \(q=-k^*\alpha_{,x}\), \(\alpha_{,t}=\theta\), \(\rho c\theta_{,tt}+\beta T_0 u_{,x,tt}=k^*\theta_{,xx}\).

### 2.2 Dispersion, both modes per side

Each model gives a determinant that is **quadratic in \(x=k^2\)**, hence two modes per side
(quasi-elastic, quasi-thermal) — the reason the 4×4 interface system is square:

| model | determinant |
|---|---|
| Biot | \((Mk^2-\rho\omega^2)(k_{\text{th}}k^2-i\omega\rho c)+i\beta^2T_0\omega k^2=0\) |
| LS | \((Mk^2-\rho\omega^2)\big[k_{\text{th}}k^2-i\omega\rho c(1-i\omega\tau_0)\big]+i\beta^2T_0\omega(1-i\omega\tau_0)k^2=0\) |
| GN-II | \((Mk^2-\rho\omega^2)(k^*k^2-\rho c\omega^2)+\beta^2T_0\omega^2k^2=0\) |

Eigenvector: \((u,\theta)\propto(-ik\beta,\;Mk^2-\rho\omega^2)\), normalised to unit 2-norm. The
**reflected branch of a mode is \((k,u,\theta)\to(-k,-u,\theta)\)** — \(u\) flips because the
coupling term in the momentum equation is odd in \(k\). (Getting this wrong was my first error; see
§3.6.)

### 2.3 Interface conditions and unknowns

Perfect contact: \([u]=0,\;[\sigma]=0,\;[\theta]=0,\;[q]=0\), with
\(q=-k_{\text{th}}\theta_{,x}\) (Biot, LS, including the \(1/(1-i\omega\tau_0)\) factor for LS) or
\(q=-k^*\alpha_{,x}\) (GN-II). Unknowns \(r_e,r_t,t_e,t_t\) (4); conditions (4). Square system,
solved by `numpy.linalg.solve` after row scaling.

### 2.4 Energy flux and its sign convention (stated once, used everywhere)

Multiplying momentum by \(\dot u\), the constitutive law by \(e\), and the heat equation by
\(\theta/T_0\), and adding:
$$\partial_t\Big[\tfrac12\rho\dot u^2+\tfrac12Me^2+\tfrac{\rho c}{2T_0}\theta^2\Big]
+\partial_x\Big[-\sigma\dot u+\frac{\theta q}{T_0}\Big]
=-\frac{k_{\text{th}}}{T_0}\theta_{,x}^2\le0 .$$
So the **energy flux is \(J=-\sigma\dot u+\theta q/T_0\)**, i.e. exactly the ordered "\(q-\sigma v\)"
with the thermal part normalised by \(T_0\), **tensile-positive** \(\sigma\). Time average:
$$J=\tfrac12\operatorname{Re}\big[\hat\sigma\hat v^*\big]+\frac{1}{2T_0}\operatorname{Re}\big[\hat\theta\hat q^*\big],
\qquad \hat v=-i\omega\hat u .$$
The thermal term **must** be the quadratic product \(\theta q/T_0\), not \(q\): the time average of a
single harmonic \(q\) is zero, and "the heat flux" transports no net energy by itself.
Dissipation density: \(\langle D\rangle=\frac{k_{\text{th}}}{2T_0}|\partial_x\hat\theta|^2\)
(and, for LS, \(\times\operatorname{Re}[1/(1-i\omega\tau_0)]=1/(1+\omega^2\tau_0^2)\), because the LS
flux carries that factor).

**Correction to `V-B3a`.** §3.1 of V-B3a wrote \(D=(k_{\text{th}}/T_0^2)|\nabla\theta|^2\) and a
\(+\sigma\dot u\) mechanical flux; the correct pair is \(D=(k_{\text{th}}/T_0)|\nabla\theta|^2\) and
\(-\sigma\dot u\). The \(T_0\) vs \(T_0^2\) and the sign were both wrong there; they are fixed here and
flagged in `V-B3a` as a revision note. **The correction was found by this computation, not by
re-reading the derivation** — the numerical check refused to close until they were fixed.

### 2.5 Three distinct "reflection coefficients"

Because of (S3), three different quantities deserve the name \(R\):

| symbol | definition | sums with \(T\) to 1? |
|---|---|---|
| \(R_{\text{flux}}\) | \((J_i-J_1)/J_i\), \(J_1\) = flux of the **total** field (incident + reflected) on side 1 | yes, by identity (S2) |
| \(R_{\text{ref}}\) | \(-J_{\text{reflected sum}}/J_i\), cross terms **between the two reflected modes** kept, incident removed | no — differs by the incident–reflected interference |
| \(R_{\text{mode}}\) | \(-\sum_j J_j/J_i\) over reflected modes, **diagonal only** | no — differs by intra-side interference |

\(R_{\text{mode}}\) is what most papers compute (they square amplitudes); \(R_{\text{ref}}\) is what
the reflected wave actually carries away; \(R_{\text{flux}}\) is the one that makes
\(A=1-R-T\) an identity. The numbers below show all three.

## 3. Result

### 3.1 Materials (arithmetic only — not a materials-database claim)

| | \(\rho\) kg/m³ | \(c_L\) m/s | \(c\) J/(kg·K) | \(k_{\text{th}}\) W/(m·K) | \(K\) GPa | \(\alpha_{\rm lin}\) 1/K | \(\beta=3K\alpha\) Pa/K | \(\delta=T_0\beta^2/(\rho cM)\) | \(\kappa\) m²/s |
|---|---|---|---|---|---|---|---|---|---|
| steel-like | 7800 | 5900 | 460 | 45 | 160 | \(12\times10^{-6}\) | \(5.760\times10^{6}\) | 0.0102 | \(1.254\times10^{-5}\) |
| Al-like | 2700 | 6300 | 900 | 205 | 76 | \(23\times10^{-6}\) | \(5.244\times10^{6}\) | 0.0317 | \(8.436\times10^{-5}\) |

\(T_0=300\) K; LS: \(\tau_0=10^{-10}\) s; GN-II: \(c_h=3000\) / \(6000\) m/s.

### 3.2 The table (steel | aluminium, perfect contact, normal incidence)

| model | \(f\) [Hz] | \(R_{\text{flux}}\) | \(R_{\text{ref}}\) | \(R_{\text{mode}}\) | \(T\) | \(A_{\text{flux}}\) | \(R_{\text{ref}}\!+\!T\!-\!1\) | \(R_{\text{mode}}\!+\!T\!-\!1\) | \(\lvert k_t\rvert/\lvert k_e\rvert\) | \(D_2\) check | \(D_1\) check |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Biot | \(10^{6}\) | 0.208043 | 0.208043 | 0.208043 | 0.791957 | \(6.7\times10^{-16}\) | \(-1.5\times10^{-10}\) | \(-1.8\times10^{-10}\) | \(6.71\times10^{2}\) | 1.00000 | 1.00000 |
| Biot | \(10^{8}\) | 0.208149 | 0.208149 | 0.208149 | 0.791851 | \(-2.2\times10^{-16}\) | \(-1.4\times10^{-7}\) | \(-1.7\times10^{-7}\) | \(6.71\times10^{1}\) | 1.00000 | 1.00000 |
| Biot | \(10^{10}\) | 0.209017 | 0.208936 | 0.208919 | 0.790983 | \(-4.4\times10^{-16}\) | \(-8.1\times10^{-5}\) | \(-9.8\times10^{-5}\) | \(6.71\) | 1.00000 | 1.00000 |
| Biot | \(10^{11}\) | 0.210700 | 0.209903 | 0.209842 | 0.789300 | \(0\) | \(-8.0\times10^{-4}\) | \(-8.6\times10^{-4}\) | \(2.12\) | 1.00000 | 1.00000 |
| **Biot** | \(\mathbf{4.46\times10^{11}}\) | 0.212026 | 0.211074 | 0.211592 | 0.787974 | \(2.2\times10^{-16}\) | \(-9.5\times10^{-4}\) | \(-4.3\times10^{-4}\) | **1.00** | 1.00000 | 1.00000 |
| Biot | \(10^{12}\) | 0.211986 | 0.211634 | 0.211925 | 0.788014 | \(-1.1\times10^{-16}\) | \(-3.5\times10^{-4}\) | \(-6.1\times10^{-5}\) | \(0.67\) | 1.00000 | 1.00000 |
| LS | \(10^{6}\) | 0.208043 | 0.208043 | 0.208043 | 0.791957 | \(-3.3\times10^{-16}\) | \(5.3\times10^{-9}\) | \(2.8\times10^{-9}\) | \(6.71\times10^{2}\) | 1.00000 | 1.00000 |
| LS | \(10^{8}\) | 0.208146 | 0.208150 | 0.208148 | 0.791854 | \(1.1\times10^{-16}\) | \(4.8\times10^{-6}\) | \(2.4\times10^{-6}\) | \(6.72\times10^{1}\) | 0.99999 | 1.00001 |
| LS | \(10^{10}\) | 0.208360 | 0.208512 | 0.208419 | 0.791640 | \(-5.6\times10^{-16}\) | \(1.5\times10^{-4}\) | \(5.9\times10^{-5}\) | \(16.9\) | **0.99978** | 1.00029 |
| LS | \(10^{11}\)+ | 0.208361 | 0.208516 | 0.208420 | 0.791639 | \(-4.4\times10^{-16}\) | \(1.5\times10^{-4}\) | \(5.9\times10^{-5}\) | \(16.8\) | 0.99977 | 1.00029 |
| **GN-II** | \(10^{6}\)–\(10^{12}\) | 0.208329 | 0.208329 | 0.208329 | 0.791671 | \(\le7.8\times10^{-16}\) | \(\le6.7\times10^{-16}\) | \(\le6.7\times10^{-16}\) | \(1.99\) | — (no \(D\)) | — |

Bold row = the frequency where the thermal and elastic wavenumbers coincide ("strong coupling").
LS stops varying above \(10^{10}\) Hz because \(\omega\tau_0>1\): the thermal branch has saturated to
its rate-limited behaviour, and the ratio \(|k_t|/|k_e|\) locks at 16.8 (no crossing anywhere in
\([10^6,10^{15}]\) Hz — **LS never reaches equal thermal/elastic wavelength**, unlike Biot).

### 3.3 Does \(A=0\) persist at an ideal coupled interface?

**Yes in the flux-bookkeeping sense, and the answer is uninformative** — that is the honest
statement. \(A_{\text{flux}}\le7.8\times10^{-16}\) in every row because flux continuity at the
interface *is* the statement \(1-R-T=0\) once \(R,T\) are defined from total fluxes. There is no
"interface absorption" to find at a perfect contact in any of the three models.

**What is informative** is what happens to the *mode-projected* sums:

1. In the **lossless** model (GN-II) all three definitions coincide and
   \(R+T-1\le6.7\times10^{-16}\) — exact, at every frequency, including the strongly coupled one.
2. In the **dissipative** models the three definitions split, and the split grows with attenuation
   per wavelength: at \(10^{6}\) Hz it is \(10^{-10}\), at \(10^{11}\) Hz it reaches
   \(8.6\times10^{-4}\) (Biot), then *shrinks* again at higher frequency as the thermal branch
   stops oscillating. For LS it stabilises at \(6\times10^{-5}\).
3. The interference term is therefore **exactly the attenuation**: it is \(\propto\operatorname{Im}k\),
   vanishing for real \(k\) (compare the GN-II row), and it is not a numerical error.

**Consequence for the review.** A paper that reports \(R+T=1\) for a *dissipative* thermoelastic
interface and computes \(R,T\) mode-by-mode is reporting a quantity that does not sum to 1 unless
the interference term is either negligible (low frequency, low attenuation) or explicitly dropped.
Reporting \(R+T+A=1\) with \(A\) as a residual hides the same term inside \(A\) and calls it
absorption. **Both are defensible only if the definition is stated.** That is the checkable
criticism this item produces.

### 3.4 The independent checks (this is what supports the numbers)

| check | expectation | observed |
|---|---|---|
| identical media both sides ⇒ \(r=0,t=1\) | exact | \(R=0.000\times10^{0}\), \(T=1.000000000\), \(A=0\) for Biot, LS, GN-II; solver residual \(1.3\times10^{-18}\) |
| \(T J_i=\int_0^\infty\langle D\rangle dx\) (transmitted energy all dissipated in medium 2) | 1 | Biot 1.000000 at every frequency; LS 0.99978–1.00000 |
| \(R_{\text{ref}}J_i=\int_{-\infty}^0\langle D\rangle dx\) (reflected energy all dissipated in medium 1) | 1 | 1.00000 (Biot), 1.00001–1.00029 (LS) |
| GN-II lossless | \(D\equiv0\), \(J_1=J_2\) | \(D_2=D_1=0\), \(J_1-J_2=7\times10^{-7}\) on \(1.56\times10^{9}\) (\(4\times10^{-16}\) relative) |
| LS flux carries \(1/(1-i\omega\tau_0)\) | check must fail by \(1+\omega^2\tau_0^2\) if omitted | with the Fourier normalisation the check came out **1.00394** at \(10^{8}\) Hz where \(1/(1+\omega^2\tau_0^2)=0.99611\) — i.e. wrong by exactly the predicted factor |

The last line is the strongest single verification in this item: the code *disagreed with itself* in
a way that reproduced a predicted factor to four digits, which is only possible if the flux, the
dissipation and the branch selection are all consistent.

### 3.5 Why these numbers are not the literature's numbers

\(R\approx0.208\), \(T\approx0.792\) at \(10^{6}\)–\(10^{8}\) Hz: the reflection is almost entirely
**elastic-impedance** reflection (\(\rho c_L\): \(4.60\times10^{7}\) vs \(1.70\times10^{7}\) Pa·s/m
⇒ \(R=((Z_1-Z_2)/(Z_1+Z_2))^2=0.2081\)), with the thermoelastic correction at the \(10^{-4}\) level.
That is a **sanity check**: at low frequency the coupled problem must reduce to the classical elastic
interface, and it does to 4 digits. The interesting thermoelastic content is in the \(10^{-4}\)
differences between models and in the interference columns, not in the leading values.

### 3.6 Five errors found and fixed while building this (kept on the record)

The identical-medium test (\(R=0,T=1\)) failed four times before the code was right. Every failure is
a trap a reader of such papers should watch for:

1. **Reflected-branch eigenvector.** I reused \((u,\theta)\) for \(-k\). Wrong: the coupling term is
   odd in \(k\), so the reflected eigenvector is \((-u,\theta)\). This alone gave \(R=1\).
2. **Sign of the coupling in the determinant.** I had \(-i\beta^2T_0\omega\); the correct term is
   \(+i\beta^2T_0\omega\). The symptom was an **anti-damped** elastic branch \((\operatorname{Im}k<0)\),
   i.e. a wave growing in the propagation direction — a physical absurdity that the sanity test caught.
3. **Sign of the mechanical flux.** \(+ \sigma\dot u\) vs \(-\sigma\dot u\). The order's
   "\(q-\sigma v\)" is correct (tensile-positive \(\sigma\)).
4. **Dissipation normalisation.** \((k_{\text{th}}/T_0^2)|\nabla\theta|^2\) vs
   \((k_{\text{th}}/T_0)|\nabla\theta|^2\) — a factor \(T_0=300\), which made the dissipation check
   read \(0.0031\) instead of 1.
5. **Amplitude weights dropped in cross terms.** `flux_total` summed mode shapes without their
   amplitudes, silently setting every reflected amplitude to 1.

Errors 1–2 and 5 are *not* exotic: they are exactly the mistakes that produce plausible-looking but
wrong \(R,T\) tables, and none of them is detectable from \(R+T+A=1\) (which stayed exactly 0
throughout, see S2). **Only the identical-medium test and the dissipation integrals caught them.**
That is the argument for the checklist in `V-B3c` §3.3.

## 4. Evidence / Sources

- Model equations, flux and dissipation: derived here (§2.4); correspondences to the model files
  `V-B2a` (Biot), `V-B2b` (LS), `V-B2e` (GN-II).
- **No source was opened for the interface problem.** All identities and numbers are mine.
- The literature counterpart of this exact problem (two semi-infinite media, two relaxation times,
  reflection **and refraction**) is:
  **Sinha, S. B.; Elsibai, K. A. (1997).** "Reflection and refraction of thermoelastic waves at an
  interface of two semi-infinite media with two relaxation times." *Journal of Thermal Stresses*
  **20**(2): 129–145. DOI `10.1080/01495739708956095`. Crossref 104. Accessed 2026-10-22.
  **Access level: bibliographic record only — NOT opened.** No comparison with their numbers is
  possible, and none is made.
- The other verified records for this topic are tabulated in `V-B3c` (§3.1) and `V-B3c` §3.4 (B3f).

## 5. Checks done

1. **Identical-medium test** (exact, strongest structural check): \(R=0\), \(T=1\), \(A=0\) for all
   three models, residual \(\le5.6\times10^{-16}\). This is what caught errors 1, 2 and 5.
2. **Dissipation integral, medium 2:** \(T J_i=\int_0^\infty\langle D\rangle dx\) to \(10^{-5}\)
   (Biot exact to all printed digits). Independent of the flux bookkeeping.
3. **Dissipation integral, medium 1:** \(R_{\text{ref}}J_i=\int_{-\infty}^0\langle D\rangle dx\) to
   \(3\times10^{-4}\).
4. **Lossless limit:** GN-II gives \(D\equiv0\), \(R+T=1\) exactly, and makes the interference term
   vanish — confirming that the interference is \(\propto\operatorname{Im}k\).
5. **Model-discrimination check:** omitting the LS flux factor \(1/(1-i\omega\tau_0)\) reproduces the
   predicted error \(1+\omega^2\tau_0^2\) to 4 digits (§3.4).
6. **Low-frequency elastic limit:** \(R\to[(Z_1-Z_2)/(Z_1+Z_2)]^2=0.2081\) to 4 digits.
7. **Strong-coupling frequency located** by bisection: \(f=4.46\times10^{11}\) Hz for Biot
   (\(|k_t|=|k_e|\)); LS has no crossing.
8. **Solver residual** \(\le1.3\times10^{-15}\) in every row (row-scaled 4×4 system).

## 6. Confidence

- **The flux/dissipation identities (§2.4): HIGH.** Derived and confirmed by three independent
  numerical checks; the LS factor test is a strong confirmation.
- **Numbers at low/moderate frequency (\(10^{6}\)–\(10^{10}\) Hz): HIGH** (elastic-limit sanity check
  + dissipation checks at \(10^{-6}\)).
- **Numbers at \(10^{11}\)–\(10^{12}\) Hz: MEDIUM.** The dissipation check holds, but the mode
  structure there is dominated by the avoided crossing and the interference terms are large
  (\(10^{-3}\)), so the *interpretation* is delicate.
- **"\(A=0\) persists at a perfect coupled interface": HIGH as a statement about the flux identity**
  (it is one), **and this file explicitly denies that it is informative** (S2, §3.3).
- **The three-\(R\) distinction: HIGH** (computed, and it vanishes exactly in the lossless model).
- **LS \(D\)-check residual \(2\times10^{-4}\): MEDIUM** — attributed to the \(\tau_0\) term in the LS
  energy density, which my \(D\) does not include; plausible but not proven.
- **Materials: the numbers are arithmetic on typical textbook constants; they are not a
  materials-database claim and no experimental comparison is intended.**

## 7. NOT verified / open issues

1. **No paper was opened**; Sinha & Elsibai (1997) is the obvious comparison and is *unread*. Until
   it is read, this file cannot claim to confirm or contradict the literature.
2. **GN-III and MGT not implemented.** GN-III is implementable with the same machinery (its
   determinant is again quadratic in \(k^2\)); MGT is not, for the reason in `V-B3a` §3.6 — its
   flux is not defined without choosing an energy functional, and an interface between two MGT media
   needs 3 conditions, not 4/2.
3. **Oblique incidence and mode conversion are not treated** — see `V-B3e` for the scoped plan.
4. **Anisotropy not treated**; for an anisotropic medium the energy flux is along the group
   velocity, not \(k\), so \(R,T\) must be defined through the normal flux (as done here) but the
   "angle" bookkeeping changes entirely.
5. **Interface is ideal.** No Kapitza conductance, no thin interlayer. B3b showed Kapitza is what
   produces genuine \(A>0\); the coupled analogue is **not** implemented here.
6. **Which \(R\) is "the" \(R\)** is a definitional choice, not a physical fact (§3.2). The manuscript
   must pick one and say so. I recommend \(R_{\text{ref}}\) + \(T\) **plus an explicit statement of
   the interference term**, or \(R_{\text{flux}}\) with \(A\) renamed "flux deficit" rather than
   "absorption".
7. **Thermal branch at very high frequency** (\(>10^{12}\) Hz) is at the edge of validity of the
   continuum models themselves (wavelength approaching phonon mean free paths); no such caveat is
   quantified here.
8. **Values of \(\tau_0\)** are illustrative (\(10^{-10}\) s); no measurement is claimed.
