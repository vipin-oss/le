# V-B2p — DPL: Taylor-truncation order, well-posedness, finite propagation speed

**Revision task R1** (`control/BRAVE_B2_REVISIONS.md`). Supersedes the DPL row of
`V-B2z_comparison_table.md` and the finite-speed discussion in `V-B2g_dpl.md`.

---

## 1. Task

R1 as written:

> **R1 (DPL):** table currently says "τ_T ≠ 0: finite speed NOT established". Strengthen with
> literature, not memory. Handler's recollection (UNVERIFIED): second order in τ_q + first order
> in τ_T needs τ_q > τ_T/2; first order in both gives a strongly-damped, infinite-speed equation.
> Find primary papers (Quintanilla & Racke and related; Dreher–Quintanilla–Racke), verify or
> refute, add `V-B2p`. State clearly which truncation each statement refers to.
> **Correct the table cell accordingly.**

Two separate questions are entangled in the task and are kept separate below:

- **(Q1) Stability / well-posedness:** for which $(\tau_q,\tau_\theta)$ is each truncated model
  stable, and which truncations are ill-posed?
- **(Q2) Finite speed:** does the truncated model predict a *bounded* propagation speed, and if so
  what is it?

The handler's recollection mixes the two: the inequality it recalls is a *stability* condition,
the "infinite speed" part is a *kinematic* statement, and they apply to *different* truncations.

## 2. Method

1. Fix the truncation. The DPL law is the delay relation
   $q(t+\tau_q)=-\kappa\,\nabla\theta(t+\tau_\theta)$; every "DPL equation" in the literature is a
   Taylor truncation of it, and the properties depend on the truncation. I use the numbering of
   Dreher, Quintanilla & Racke (2009), eqs. (1.12)–(1.15), which is the only source I found that
   lists all four side by side:

   | Tag | Truncation of the constitutive law | Time order $n$ | $\Delta$-order $m$ | $n-m$ |
   |---|---|---|---|---|
   | T1 | $q+\tau_q\dot q=-\kappa\nabla\theta-\kappa\tau_\theta\nabla\dot\theta$ (Jeffreys) | 2 | 1 | 1 |
   | T2 | $q+\tau_q\dot q+\tfrac{\tau_q^2}{2}\ddot q=-\kappa\nabla\theta-\kappa\tau_\theta\nabla\dot\theta$ | 3 | 1 | 2 |
   | T3 | $q+\tau_q\dot q=-\kappa\nabla\theta-\kappa\tau_\theta\nabla\dot\theta-\kappa\tfrac{\tau_\theta^2}{2}\nabla\ddot\theta$ | 2 | 2 | 0 |
   | T4 | both second order | 3 | 2 | 1 |

   T2 is the model normally meant by "the DPL thermoelastic model" (it is eq. (1.3)/(1.4) of
   Quintanilla & Racke 2006, IJHMT). T1 is also frequently used and is often *called* "DPL" in the
   engineering literature.

2. Combine with the energy equation $\theta_{,t}+\gamma\,\mathrm{div}\,q=0$, eliminate $q$, and
   write the plane-wave ansatz $\theta\propto e^{\,i(kx-\omega t)}$, i.e. $s=-i\omega$ with
   $e^{st}$. **Time convention: $e^{i(kx-\omega t)}$, hence $s=-i\omega$.** Length: 1-D.
   $\kappa:=\gamma k_{\text{cond}}=\kappa_{\text{cond}}/(\rho c_v)$ is the diffusivity.

   Characteristic polynomials (all in $s$, for fixed $k$):
   - T1: $\tau_q s^2+(1+\kappa k^2\tau_\theta)s+\kappa k^2=0$
   - T2: $\tfrac{\tau_q^2}{2}s^3+\tau_q s^2+(1+\kappa k^2\tau_\theta)s+\kappa k^2=0$
   - T4: $\tfrac{\tau_q^2}{2}s^3+\big(\tau_q+\tfrac{\kappa k^2\tau_\theta^2}{2}\big)s^2+(1+\kappa k^2\tau_\theta)s+\kappa k^2=0$

3. Three independent routes to each answer:
   (a) **Literature statement** (what the paper asserts);
   (b) **Routh–Hurwitz / dominant-balance algebra** done here from the polynomial;
   (c) **numerical root-finding** in `V-B2p_dpl_truncation_check.py`.

4. For the finite speed, dominant balance for $k\to\infty$ with $\omega=ck$; the test is whether
   a *real positive* $c$ solves the leading-order balance.

## 3. Result

### 3.1 Q1 — stability: the recalled inequality has the wrong direction

**Verified from the source.** Quintanilla & Racke (2006, IJHMT), citing their own [7]
(= Quintanilla 2002) and restating it in their own Conclusion:

> "For Eq. (1.4) … the system is (even exponentially) stable if $x:=\tau_\theta/\tau_q>\tfrac12$
> holds, and … it is not (exponentially) stable if $x<\tfrac12$ holds."
> — Quintanilla & Racke, IJHMT **49** (2006), §1

and, restated as their own conclusion list:

> 1. When we approximate until first-order in $\tau_q$ and until first or second-order in
>    $\tau_\theta$, the system is always stable.
> 2. When we approximate until second-order in $\tau_q$ and only until first-order in
>    $\tau_\theta$, the system is stable if $\tau_\theta/\tau_q>1/2$ and unstable if
>    $\tau_\theta/\tau_q<1/2$.

Eq. (1.4) there **is** T2. So the condition is

$$\boxed{\ \tau_\theta>\tau_q/2\ }\qquad\text{(stability, T2)}$$

i.e. **$\tau_T>\tau_q/2$ — not $\tau_q>\tau_T/2$.** The handler's recollection inverts the
inequality. The two are opposite: $ \tau_q>\tau_T/2 \iff \tau_\theta/\tau_q<2$, which is
compatible with instability for any $\tau_\theta/\tau_q\in(0,\tfrac12)$.

**Routh–Hurwitz confirms it independently.** For T2 with $a_3=\tau_q^2/2$, $a_2=\tau_q$,
$a_1=1+\kappa k^2\tau_\theta>0$, $a_0=\kappa k^2>0$, the criterion $a_2a_1>a_3a_0$ is

$$1+\kappa k^2\tau_\theta>\tfrac{\tau_q}{2}\kappa k^2
\iff 1>\kappa k^2\Big(\tfrac{\tau_q}{2}-\tau_\theta\Big).$$

Row 1 and row 2 of the Routh table are automatically positive, so this *single* inequality is
necessary and sufficient. It holds for all $k$ **iff** $\tau_\theta\ge\tau_q/2$, with equality
marginal (the $k\to\infty$ limit is approached but the condition $1>0$ still holds at finite $k$).
When $\tau_\theta<\tau_q/2$ the model is stable for $k<k_c$ and unstable for $k>k_c$ with the
**closed form**

$$k_c=\Big[\kappa\big(\tfrac{\tau_q}{2}-\tau_\theta\big)\Big]^{-1/2}.$$

Numerical check (reference material, see §4): at $\tau_\theta/\tau_q=0.3$ the swept model goes
unstable from $k=7.47\times10^{7}\,\mathrm{m^{-1}}$; predicted
$k_c=[1.254\times10^{-5}\cdot2\times10^{-11}]^{-1/2}=6.31\times10^{7}$. Agreement to the grid
resolution of the sweep. At ratios 0.5 and 0.7 no unstable $k$ exists in $[10^2,10^{10}]$.

**T1, T3 are always stable** — matches conclusion 1 above and my sweep at ratios 0.3, 1.0, 3.0
(all stable). Their truncation order is too low to produce the pathology.

### 3.2 Q1 — well-posedness: the standard truncations are *not* the ill-posed ones

Dreher, Quintanilla & Racke (2009), **Theorem 1.3** (full text read): for
$b_0u_t+\dots+b_j u_t^{(j+1)}=c_0Au+\dots+c_mAu_t^{(m)}$ with $n:=j+1\ge m$ and
$\kappa_{\text{DQR}}:=n-m$, the problem is **ill-posed if $\kappa_{\text{DQR}}\ge3$**. They add
that for Fourier, Cattaneo, Jeffreys and the four DPL truncations (1.12)–(1.15) "we have
$0\le\kappa_{\text{DQR}}\le2$ in each case", and therefore "Theorem 1.3 is sharp". All four DPL
truncations above have $n-m\in\{0,1,2\}$ — inside the well-posed class.

What *is* ill-posed per that paper is the **delay equation itself**:

> "Single-phase-lag and dual-phase-lag heat conduction models can be interpreted as formal
> expansions of delay equations. The delay equations are shown to be ill-posed, as are the formal
> expansions of higher order — in contrast to lower-order expansions leading to Fourier's or
> Cattaneo's law."
> — Dreher, Quintanilla & Racke, AML **22** (2009), Abstract

This is a stronger and more useful statement for the review than "DPL is ill-posed": the stable,
exponentially-decaying truncated models are *not* approximations of the object they claim to
approximate, because that object (the delay equation) has no continuous dependence on the data.
The truncated models' stability is therefore a property of the truncation, not evidence of
soundness of the underlying lag picture. I flag this as a review-relevant remark, not as a
statement of the original authors about DPL as such.

### 3.3 Q2 — finite speed: **yes for T2**, with an explicit speed

This is the substantive correction to my own table. Dominant balance for T2, $k\to\infty$,
$s=-i\omega$, $\omega=ck$:

$$\underbrace{\tfrac{\tau_q^2}{2}s^3}_{i\tfrac{\tau_q^2}{2}c^3k^3}
+\underbrace{\tau_q s^2}_{-\tau_qc^2k^2}
+\underbrace{(1+\kappa k^2\tau_\theta)s}_{-i\kappa\tau_\theta ck^3}
+\underbrace{\kappa k^2}_{\kappa k^2}=0 .$$

The $O(k^3)$ terms must cancel (there is no other term of that order), giving

$$\tfrac{\tau_q^2}{2}c^3=\kappa\tau_\theta c\quad\Longrightarrow\quad
\boxed{\,c_\infty=\frac{\sqrt{2\kappa\tau_\theta}}{\tau_q}\,}$$

real and positive for $\tau_\theta>0$: **T2 has a genuine finite propagation speed.** At the
stability boundary $\tau_\theta=\tau_q/2$ this collapses to $c_\infty=\sqrt{\kappa/\tau_q}$.

Dimensional check: $\sqrt{(\mathrm{m^2/s})\cdot\mathrm{s}}/\mathrm{s}=\mathrm{m/s}$ ✓.

Numerical confirmation, three parameter sets deliberately chosen so that the decoy expression
$\sqrt{\kappa/\tau_\theta}$ **disagrees** with the correct one:

| $\tau_\theta$ | numeric $v_{ph}$ at $k=10^{13}$ | $\sqrt{2\kappa\tau_\theta}/\tau_q$ | decoy $\sqrt{\kappa/\tau_\theta}$ |
|---|---|---|---|
| $1.0\times10^{-10}$ | **500.84** | **500.84** | 354.14 |
| $0.7\times10^{-10}$ | **419.03** | **419.03** | 423.28 |
| $0.5\times10^{-10}$ | **354.14** | **354.14** | 500.84 |

(units m/s; $\kappa=1.254181\times10^{-5}\,\mathrm{m^2/s}$, $\tau_q=10^{-10}\,\mathrm{s}$.)

The first row is the discriminator: at $\tau_\theta=\tau_q$ the two candidate formulas differ by
41 % and the numeric value picks the correct one exactly. **My earlier arithmetic in this
session had picked $\sqrt{\kappa/\tau_\theta}$, which agrees to 1 % at $\tau_\theta=0.7\tau_q$ and
is therefore a trap**; it is refuted here.

Because $c_\infty$ exists, T2 is hyperbolic in the sense relevant to the review: a sharp thermal
wave front propagates. A thermal wave speed is thus available in DPL **provided the second-order
term in $\tau_q$ is retained** and $\tau_\theta>0$.

### 3.4 Q2 — no finite speed for T1, T3, T4

- **T1 (first order in both).** With real frequency, $k^2$ follows from
  $(1+\kappa k^2\tau_\theta)s+\kappa k^2=-(\tau_q s^2+s)$; numerically $v_{ph}=356.65$,
  $3310.5$, $33214$ m/s at $10^9,10^{11},10^{13}$ Hz, i.e. $v_{ph}\propto\sqrt{\omega}$
  ($v_{ph}/\sqrt{\omega}=4.50,4.18,4.19\times10^{-3}$). **Unbounded — no finite speed.**
  At fixed real $k$ the two roots are real and *negative* for this material
  ($k=10^5$: $-9.99996\times10^{9},-1.254\times10^{5}$; $k=10^{9}$:
  $-8.77\times10^{12},-1.429\times10^{10}$) — i.e. **overdamped, no oscillation at all**.
  So the recollection's "strongly damped, infinite-speed equation" is **confirmed** for T1, and
  Q&R's "always stable" is consistent with it (monotone decay of every mode).
- **T3 (first order $\tau_q$, second order $\tau_\theta$).** $n-m=0$; same overdamped character as
  T1. Not separately re-derived here — see §7.
- **T4 (second order in both).** Numerically band-limited: $\omega\to1/\tau_\theta$ exactly
  ($1.4286\times10^{10}\,\mathrm{rad/s}$ for $\tau_\theta=0.7\times10^{-10}$, reproduced at
  $k=10^{9},10^{11},10^{13},10^{15}$ to 4 digits) while $v_{ph}=\omega/k\to0$. This is neither a
  wave nor a diffusion: short waves are frozen, and there is no front. It matches Tzou's own
  reservation, quoted verbatim by Quintanilla & Racke (2006, §1) from Tzou [12, p. 3237]:
  second-order expansion in both lags "should also involve a second-order time derivative in
  $\tau_\theta^2$ … resulting in an equation of parabolic type".

### 3.5 Corrected table cell for `V-B2z` (replaces the old DPL finite-speed entry)

> **DPL — finite speed is truncation-dependent; replace the old "τ_T ≠ 0: not established".**
> T2 (2nd order in $\tau_q$, 1st in $\tau_\theta$; the model usually meant by "DPL"):
> **finite speed $c_\infty=\sqrt{2\kappa\tau_\theta}/\tau_q$**, stable iff
> $\tau_\theta>\tau_q/2$ [Q&R 2006; re-derived here via Routh–Hurwitz and checked numerically].
> T1 (1st order in both): **no finite speed** ($v_{ph}\propto\sqrt{\omega}$), always stable,
> overdamped. T4 (2nd order in both): **band-limited**, $\omega\le1/\tau_\theta$, $v_{ph}\to0$.
> Truncations with $n-m\ge3$ are ill-posed [DQR 2009, Thm 1.3]; the four standard truncations
> have $n-m\le2$ and are not.

### 3.6 Verdict on the recollection (R1 asks for verify *or refute*)

| Recollection | Status | Basis |
|---|---|---|
| "second order in $\tau_q$ + first order in $\tau_T$" is the relevant truncation | **CONFIRMED** | Q&R 2006 eq. (1.4) is exactly T2 |
| "needs $\tau_q>\tau_T/2$" | **REFUTED — wrong direction** | Q&R 2006 §1 and Conclusion 2: $\tau_\theta/\tau_q>1/2$; Routh–Hurwitz gives $k_c=[\kappa(\tau_q/2-\tau_\theta)]^{-1/2}$, unstable for $\tau_\theta<\tau_q/2$ |
| "first order in both gives a strongly damped, infinite-speed equation" | **CONFIRMED** | sweep: overdamped real negative roots, $v_{ph}\propto\sqrt{\omega}$; Q&R Conclusion 1: always stable |
| (implicit) DPL has no finite speed | **REFUTED for T2** | $c_\infty=\sqrt{2\kappa\tau_\theta}/\tau_q$, two independent routes |

## 4. Evidence / Sources

1. **Quintanilla, R.; Racke, R. (2006).** "A note on stability in dual-phase-lag heat conduction."
   *International Journal of Heat and Mass Transfer* **49**(7–8): 1209–1213.
   DOI: `10.1016/j.ijheatmasstransfer.2005.10.016`. Accessed 2026-10-22.
   **Access level: abstract + §1 (Introduction) + section snippets + Conclusion, from the
   publisher-rendered article-preview page.** Not the typeset PDF. The quoted Conclusion list and
   the $\tau_\theta/\tau_q>1/2$ statement are from that preview and are first-hand statements by
   the authors, but I have not seen the proofs.
2. **Dreher, M.; Quintanilla, R.; Racke, R. (2009).** "Ill-posed problems in thermomechanics."
   *Applied Mathematics Letters* **22**(9): 1374–1379. DOI: `10.1016/j.aml.2009.03.010`.
   Accessed 2026-10-22. **Access level: FULL TEXT** (Elsevier open archive; abstract, §1 with
   Theorem 1.1–1.3 and the statements about expansion order, §2–3 proofs, references).
   **This is the first primary full text opened in this verification set.**
3. **Quintanilla, R.; Racke, R. (2007).** "Qualitative aspects in dual-phase-lag heat conduction."
   *Proceedings of the Royal Society A* **463**(2079): 659–674. DOI: `10.1098/rspa.2006.1784`.
   Accessed 2026-10-22. **Access level: abstract only** (paywalled). Abstract states: both
   parameters positive ⇒ well posed, spatial decay exponential in distance; "when the phase lag of
   the gradient of the temperature is bigger than the phase lag of the heat flux" ⇒ exponentially
   stable with spatial decay exponential in the *square* of the distance. Note this paper writes
   the threshold as $\tau_\theta>\tau_q$, not $\tau_q/2$ — **two different thresholds in two papers
   by the same authors; do not merge them.**
4. **Quintanilla, R. (2002).** "Exponential stability in the dual-phase-lag heat conduction
   theory." *Journal of Non-Equilibrium Thermodynamics* **27**: 17–? (pages incomplete).
   DOI: `10.1515/jnetdy.2002.012`. Accessed 2026-10-22. **Access level: bibliographic record
   only** (via Crossref and as reference [7] of source 1). Original source of the $1/2$ threshold
   as attributed by Q&R 2006; not read.
5. **Quintanilla, R.; Racke, R. (2008).** "A note on stability in three-phase-lag heat
   conduction." *IJHMT* **51**(1–2): 24–29. DOI: `10.1016/j.ijheatmasstransfer.2007.04.045`.
   **Access level: bibliographic only.** Relevant to TPL, not used for any claim here.

Reference material for all numbers (same as `V-B2_wave_speeds.py`): $k_{\text{cond}}=45$ W/(m·K),
$\rho=7800$ kg/m³, $c_v=460$ J/(kg·K) ⇒ $\kappa=1.254181\times10^{-5}$ m²/s; $\tau_q=10^{-10}$ s.

## 5. Checks done

1. **Routh–Hurwitz vs literature** (T2): the algebraic condition $a_2a_1>a_3a_0$ reduces to
   $\tau_\theta\ge\tau_q/2$ and reproduces Q&R's $1/2$ independently, including the closed-form
   $k_c$ that matches the swept instability onset. Two routes, same threshold.
2. **Finite speed, analytic vs numeric** at three parameter sets, one of which separates the two
   candidate formulas by 41 %; numeric matches the dominant-balance result to 5 significant
   figures in all three (500.84 / 419.03 / 354.14 m/s).
3. **Dimensional analysis** of $c_\infty$: m/s ✓.
4. **Limit check:** $c_\infty(\tau_\theta\to\tau_q/2)=\sqrt{\kappa/\tau_q}$ — the value a
   Cattaneo model with $\tau=\tau_q$ would give, consistent.
5. **Scaling check on the ill-posedness invariant:** $\max|s|$ grows like $k^{2/(n-m)}$ — measured
   $k^2$ for $n-m=1$ (T1, T4) and $k^1$ for $n-m=2$ (T2), matching Theorem 1.3's exponent and
   independently confirming the finite-speed/non-finite-speed split.
6. **Overdamped check (T1):** fixed-$k$ roots are real and negative at three decades of $k$,
   confirming "strongly damped" rather than oscillatory.
7. **Self-correction recorded:** an earlier hand computation in this session used
   $\sqrt{\kappa/\tau_\theta}$ for $c_\infty$; check 2 refutes it. Logged here rather than deleted.
8. Script: `V-B2p_dpl_truncation_check.py`, run under Python 3 with numpy; all six check blocks
   execute without error.

## 6. Confidence

- **Q1 stability threshold $\tau_\theta>\tau_q/2$ (T2): HIGH.** Author statement + independent
  Routh–Hurwitz + numerics.
- **Q2 $c_\infty=\sqrt{2\kappa\tau_\theta}/\tau_q$ (T2): HIGH.** Dominant balance + numerics on a
  discriminating parameter set + dimensional analysis.
- **T1 infinite speed / overdamped: HIGH.**
- **T4 band-limited $\omega_c=1/\tau_\theta$: MEDIUM–HIGH.** Numerics clear (4 digits); analytic
  leading-order balance of the $k^2$ terms gives $(\tau_\theta^2/2)\omega^2+i\omega\tau_\theta-1=0$
  consistent with the measured $\omega\to1/\tau_\theta$, but I did not carry the full asymptotic
  expansion.
- **Ill-posedness attribution to $n-m\ge3$: HIGH** as a reading of Theorem 1.3 (full text),
  **MEDIUM** as a statement that it covers every model called "DPL" in the literature, since
  authors use different truncations under the same name.
- **Quoted threshold "x = 1" in Q&R §1: MEDIUM** — the HTML rendering drops fractions; I read
  "the case x = 1" as "x = ½". Does not affect any conclusion (the two-sided statement around it
  is unambiguous).

## 7. NOT verified / open issues

1. **Quintanilla (2002), J. Non-Equilib. Thermodyn. 27** — not opened. The $1/2$ threshold is
   attributed to it by Q&R 2006 and restated by them; I did not see the original proof, nor the
   full page range.
2. **Q&R 2006 IJHMT typeset PDF** — not seen. Stability conclusions read from the publisher
   preview; the *proofs* (§2–3) and the exact hypotheses on the domain/boundary conditions are
   unverified. My Routh–Hurwitz check is for the 1-D symbol, i.e. it tests the *pointwise*
   (frozen-coefficient) condition, not the operator-theoretic statement on a bounded domain.
3. **The third conclusion of Q&R 2006** (on T4 / second order in both) is **truncated in the
   accessible preview** — the list stops after item 2. In the §"The model (1.8)" snippet the
   sufficient condition prints as $\tau_\theta/\tau_q\ge\sqrt2-1$ and a non-stability window as
   "$\sqrt3-2<x<1/2$" (rendered by the HTML-to-text conversion as "2-3<x<12"). **I read those as
   $\sqrt2-1$ and $(\sqrt3-2,\,1/2)$ but the rendering is corrupt; treat both intervals as
   UNVERIFIED** and do not print them without the PDF. For the same reason I did **not** test my
   T4 numerics against their predicted non-stability window; my T4 sweep at
   $\tau_\theta/\tau_q=0.3,0.5,0.7$ found no instability, which is not a contradiction (the window
   sits below 0.5) but also not a confirmation.
4. **T3 not analysed numerically.** Its polynomial needs care (the $\Delta\ddot\theta$ term raises
   the $\Delta$-order to 2 with time order 2) and I did not verify the $n-m=0$ bookkeeping by hand
   beyond reading Dreher et al.'s own list. Flagged rather than guessed.
5. **Coupling to elasticity is not treated here.** Everything above is the rigid heat conductor.
   Whether the $\tau_\theta>\tau_q/2$ threshold survives when the heat equation is coupled to the
   momentum equation (the case of actual interest for the review) is **not** established by these
   sources for T2; Q&R mention 1-D DPL thermoelasticity results in their refs [8],[9] but I have
   not read them. **Do not extend the rigid-conductor threshold to the coupled system without a
   source.**
6. **Tzou's quoted remark** is reproduced from Q&R's quotation of Tzou (1995), p. 3237; I did not
   open Tzou (1995) itself, so the page number is second-hand.
7. **Symbol collision warning for the manuscript:** Q&R and Dreher et al. write the
   temperature-gradient lag as $\tau_\theta$; my `V-B2g`/`V-B2z` write $\tau_T$. Also, Dreher
   et al. use $\kappa$ both for thermal conductivity and (in Theorem 1.3) for the integer
   $n-m$; I have renamed their integer to $\kappa_{\text{DQR}}$ above. Any manuscript sentence must
   fix one notation.
