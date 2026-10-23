# V-B2o — Guyer–Krumhansl (nonlocal / phonon-hydrodynamic heat conduction)

**Revision task R4 (first of two).** Access date 2026-10-22.

> **DEPTH MARKER — READ FIRST.** This file is a **short source-verified overview**, as R4
> requires. It is **not** a full-depth file of the `V-B2a`…`V-B2m` kind: there is **no opened
> primary source** for the Guyer–Krumhansl equation, no verification of its coefficient structure
> against the original paper, and no literature survey of its applications. What it does contain,
> and what is checked, is the **mathematical content of the equation as commonly written** —
> which is enough to answer the review's question ("finite speed? dissipative? what breaks?") but
> **not** enough to print the model's derivation or coefficients as sourced.

---

## 1. Task

Part of R4: add `V-B2o` Guyer–Krumhansl (nonlocal heat conduction), "only a short source-verified
overview with governing-equation structure" and "mark depth honestly".

## 2. Method

1. Verify the bibliographic anchors (done: §4).
2. Write the equation structure as it is commonly used, and **derive the 1-D dispersion myself**,
   since that is the part the review actually needs.
3. Check the consequences numerically, including the reduction to Cattaneo.
4. Mark every unverified point (§7).

**Conventions:** 1-D, $e^{i(kx-\omega t)}$, $s=-i\omega$; $\theta$ = temperature difference;
$\kappa=k_{\text{th}}/(\rho c_v)$; $\tau$ = single flux relaxation time; $\ell$ = nonlocal length.

## 3. Result

### 3.1 Equation structure

GK-type constitutive law (heat flux with a Laplacian/nonlocal term):

$$q_i+\tau\dot q_i=-k_{\text{th}}\theta_{,i}+\ell^2\big(\Delta q_i+2\,\partial_i\partial_jq_j\big)$$

With the energy equation $\dot\theta=-\partial_iq_i$ and the **1-D** reduction
$\Delta q+2\partial_x^2q=3q_{,xx}$, this gives

$$\boxed{\ \tau\ddot\theta+\dot\theta=\kappa\,\theta_{,xx}+3\ell^2\dot\theta_{,xx}\ }$$

**Note the factor 3.** It comes from $\Delta q+2\nabla(\nabla\!\cdot\!q)$ in the 1-D reduction, and
**different papers absorb it differently** (some write $\ell^2\theta_{,xxt}$ with no 3, having
defined $\ell$ with the factor inside). Any comparison of nonlocal lengths across papers must
first fix this convention — the same pitfall already recorded for TPL's $\tfrac12\tau_v^2$ in
`V-B2z`.

Structure, in words: it is **Cattaneo (damped wave) plus a spatial-gradient correction to the
damping**. The $\tau\ddot\theta$ term gives wave character; the $3\ell^2\dot\theta_{,xx}$ term
makes the damping stronger at short wavelength.

### 3.2 Dispersion and the answer to "finite speed?"

Plane wave: $\tau s^2+(1+3\ell^2k^2)s+\kappa k^2=0$. Discriminant
$$\Delta=(1+3\ell^2k^2)^2-4\tau\kappa k^2 .$$

- **$\ell=0$:** $\Delta=1-4\tau\kappa k^2<0$ for $k>k_1=1/(2\sqrt{\tau\kappa})$ ⇒ oscillatory modes
  above $k_1$, and $v_{ph}\to\sqrt{\kappa/\tau}$ — **finite speed** (this is just Cattaneo).
- **$\ell>0$:** for large $k$ the $(3\ell^2k^2)^2$ term dominates and $\Delta>0$ again ⇒ the modes
  become **overdamped** at short wavelength. The oscillatory band is
  $$k_1<k<k_2,\qquad k_1=\frac{1}{2\sqrt{\tau\kappa}},\qquad
  k_2=\sqrt{\frac{4\tau\kappa}{9\ell^4}} .$$
  As $k\to\infty$ one root $\to-\kappa/(3\ell^2)$ (a finite rate) and the other $\to-\infty$
  (rate $\propto k^2$): no oscillation, hence **no wave front**.

**So: Guyer–Krumhansl as commonly written does *not* have a finite propagation speed for
$\ell>0$; its "second sound" is a band-limited resonance, not a wave.** For $\ell=0$ it collapses to
Cattaneo, which does.

Numerical (reference material $\kappa=1.254181\times10^{-5}$ m²/s, $\tau=10^{-10}$ s,
$\sqrt{\kappa/\tau}=354.14$ m/s):

| $\ell$ | $k=10^{7}$ | $k=10^{9}$ | $k=10^{10}$ | $k=10^{11}$ | $k=10^{13}$ |
|---|---|---|---|---|---|
| 0 | overdamped | osc., $v_{ph}$=354.11 | 354.14 | 354.14 | 354.14 |
| 1 nm | overdamped | osc., 353.58 | osc., 320.57 | **overdamped** | overdamped |
| 10 nm | overdamped | **overdamped** | overdamped | overdamped | overdamped |

Predicted transition $k_2=\sqrt{4\tau\kappa/(9\ell^4)}$: $2.36\times10^{10}$ m⁻¹ for $\ell=1$ nm,
$2.36\times10^{8}$ m⁻¹ for $\ell=10$ nm — both consistent with the table (1 nm: oscillatory at
$10^{10}$, dead at $10^{11}$; 10 nm: dead already at $10^{9}$). The surviving slow rate is
$\kappa/(3\ell^2)=4.18\times10^{12}$ s⁻¹ for $\ell=1$ nm, matching the computed root
$4.181\times10^{12}$.

### 3.3 Where it sits among the other models

- **Class:** a **nonlocal-in-space**, single-time-relaxation heat law. It is *not* a higher-order
  time truncation (unlike DPL/TPL), so it is **not** exposed to Dreher–Quintanilla–Racke's
  ill-posedness theorem, which counts time orders (`V-B2p`).
- **Relationship to the review's list:** distinct from Eringen nonlocal elasticity (`V-B2m`), which
  regularises the *momentum* equation, not the heat equation. GK regularises the **flux**; the two
  are not interchangeable and are often confused because both introduce a length $\ell$.
- **Dissipation:** the equation has a $-\kappa\theta_{,xx}$ term, so it is dissipative; the
  $\ell$-term is a *stabilising* correction to the damping at short wavelength, not a source of
  finite speed.
- **Known physical motivation (reported, not verified here):** phonon hydrodynamics / Poiseuille
  flow of phonons in dielectric crystals at low temperature; the $\ell^2$ term is the
  nonlocal (Burnett-order) correction to the linearised phonon Boltzmann equation. **This sentence
  is the standard motivation and is NOT sourced in this file beyond the 1966 paper's existence.**

### 3.4 Coupled thermoelastic form

Adding the usual thermoelastic coupling replaces $\dot\theta$ by
$\dot\theta+\beta T_0\dot e_{kk}/(\rho c_v)$ in the same operator; speeds then hybridise with the
elastic branches exactly as in `V-B2a`. **This is not derived here** (it is the obvious substitution
and nothing depends on it in this file) — flagged in §7.

## 4. Evidence / Sources

1. **Guyer, R. A.; Krumhansl, J. A. (1966).** "Solution of the linearized phonon Boltzmann
   equation." *Physical Review* **148**(2): 766–778. DOI `10.1103/PhysRev.148.766`. Crossref 856.
   Accessed 2026-10-22. **Access level: bibliographic record only (Crossref). Full text not
   opened.** Note: the 1966 *Phys. Rev.* paper is the usual citation for the nonlocal ("Guyer–
   Krumhansl") heat equation; **there is also a 1966 *Phys. Rev. Lett.* companion**? — not verified,
   not cited.
2. **Horie, C.; Krumhansl, J. A. (1964).** "Boltzmann equation in a phonon system." *Physical
   Review* **136**(5A): A1397–A1407. DOI `10.1103/PhysRev.136.A1397`. Crossref 35.
   **Access level: record only.** Cited since it is the immediate precursor found in the same
   Crossref query.

**The equation in §3.1 is not transcribed from either source.** It is the form in common use. The
$\tau\ddot\theta$ and $3\ell^2\dot\theta_{,xx}$ structures and the reduction are verified only as
mathematics (§5).

## 5. Checks done

1. **1-D reduction of the nonlocal operator:** $\Delta q_i+2\partial_i\partial_jq_j$ in 1-D equals
   $q_{,xx}+2q_{,xx}=3q_{,xx}$ — this is the origin of the factor 3 and is checked by hand and in
   the script.
2. **$\ell\to0$ limit returns Cattaneo:** $v_{ph}\to\sqrt{\kappa/\tau}=354.14$ m/s numerically and
   the oscillatory band becomes $k>k_1$ with no upper cutoff ✓.
3. **Discriminant analysis vs numerics:** predicted $k_2$ vs observed oscillatory/overdamped
   transition, for two values of $\ell$ — agrees (see table).
4. **Residual root check:** computed slow rate $4.181\times10^{12}$ s⁻¹ vs
   $\kappa/(3\ell^2)=4.181\times10^{12}$ s⁻¹ for $\ell=1$ nm ✓.
5. **No instability at any tested $k$ or $\ell$** — all roots have negative real part over
   $k\in[10^6,10^{13}]$, $\ell\in\{0,1,10\}$ nm; so, as written, GK is stable (contrast with the
   DPL danger case in `V-B2p`).
6. **Dimensional analysis:** $[\tau\ddot\theta]=[\dot\theta]$, $[3\ell^2\dot\theta_{,xx}]=[\dot\theta]$ ✓.

## 6. Confidence

- **The mathematics of §3.2–§3.3: HIGH** (discriminant + numerics + limit check agree), *given* the
  equation as written.
- **The equation as *the* GK equation: MEDIUM.** It is the widely used form, but not checked
  against the 1966 paper; the factor 3 and the placement of $\ell^2$ are exactly the sort of thing
  that varies.
- **The physical motivation sentence in §3.3: LOW/SECONDARY** — reported as standard, not sourced.
- **Overall depth: deliberately shallow.** Do not upgrade this file's status by copy-editing.

## 7. NOT verified / open issues

1. **Guyer & Krumhansl (1966) not opened.** No statement in this file should be attributed to that
   paper except its existence and coordinates.
2. **Coefficient structure unverified:** whether the original law has $+2\partial_i\partial_jq_j$,
   $+\tfrac13$, or a different combination; whether the 1-D coefficient is 3 (convention), and
   whether $\ell$ is defined with or without that factor. **A review must not compare GK lengths
   across papers without resolving this.**
3. **No coupled thermoelastic GK treatment** derived or sourced (§3.4).
4. **No literature survey** of GK applications (nanoscale heat transport, graphene, etc.) — out of
   scope for R4's "short overview", and no sources were gathered.
5. **No assessment** of whether GK is compatible with the second law in the form stated; with a
   purely diffusive-looking principal part one expects it to be, but this is not checked.
6. **Crossref counts are snapshots** (856, 35) taken 2026-10-22 and are not significance claims.
