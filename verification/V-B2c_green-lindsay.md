# V-B2c — Green–Lindsay (two relaxation times)

**Access date 2026-10-22.** No subscription full text. ⚠ This file carries a larger UNVERIFIED block than the others: see §NOT verified.

> **REVISION R2 (2026-10-22) — read this before using anything below.** Revision R2 is
> implemented in §R7 at the end of this file. It (i) gives the mapping to the standard
> $(\tau_0,\tau_1)$ notation, (ii) records that the $(\tau_1,\tau_2)$ scheme used in §R1–§R5
> below is a **notation defect, not a relabelling**, and (iii) corrects the finite-speed entry:
> GL in its standard form **does** have a closed-form thermal wave speed $\sqrt{\kappa/\tau_0}$.
> The earlier statement in §R3 that GL has no closed-form speed is **superseded**. GL remains
> "**do not print**" for the reasons given in §R7.

## Task

As V-B2a, for Green–Lindsay (GL) theory. The brief's hint: "two relaxations; note there is NO relaxation in the heat flux but in the temperature rate terms" — this hint is the specific thing I test below.

## Method

1. **Provenance.** Green, A.E. & Lindsay, K.A. (1972) "Thermoelasticity", *J. Elasticity* **2**(1):1–7, DOI 10.1007/BF00045689. Crossref 2929, OpenAlex 2947. Read level: **record only — full text NOT opened.**
2. Searched for an open-access statement of the GL linearised equations. **Result: not found.** The one openly readable critical review I could obtain (Noble 2026 §5.1) describes GL only qualitatively — it gives no equations. That is itself a finding worth recording: a 2026 "critical review with analytical proofs" does not write down the GL system it discusses.
3. Consequence: the GL system below is the **standard form as commonly used**, not transcribed from a source I opened. It is labelled accordingly, and only the *mathematical* consequences of the stated form are verified.

## Result

### R1. Constitutive structure (as commonly written)

GL introduces two relaxation times τ₁, τ₂ by rate-dependence of the **entropy/temperature** terms, not of the heat flux:

    σ_ij = λ ε_kk δ_ij + 2μ ε_ij − β (θ + τ₁ θ̇) δ_ij
    ρη = ρc θ + β T₀ ε_kk + ...      (entropy carries τ₁ as well)
    q_i = −k_th θ_,i                  ← **no relaxation in the flux**

and the heat equation

    ρc(θ̇ + τ₁ θ̈) + βT₀(ε̇_kk + τ₂ ε̈_kk) = k_th θ_,ii

with the ordering constraint

    τ₂ ≥ τ₁ ≥ 0

> **SUPERSEDED by §R8 (2026-10-22):** the `(τ₁, τ₂)` slot assignment above is wrong — two
> different times do not sit inside the energy equation. See §R8 for the source-backed
> structure. Do not cite the line above.

**The brief's hint is corroborated at the level of structure**: GL keeps Fourier's law for q (no flux relaxation) and puts the relaxation on the temperature-rate / temperature-rate-of-strain terms. This is what distinguishes GL from LS, and it is why the two theories are *not* interchangeable despite both having "relaxation times".

### R2. Coupled equations, 1-D

    ρ ü = M u_xx − β(θ_x + τ₁ θ̇_x)
    ρc(θ̇ + τ₁θ̈) + βT₀(u̇_x + τ₂ü_x) = k_th θ_xx

### R3. Parameters

As V-B2a, plus τ₁, τ₂ [s] with **τ₂ ≥ τ₁ ≥ 0**. Note there is **no** τ on the heat flux, so GL does not have a clean "thermal wave speed √(κ/τ)" of the LS type.

### R4. Admissibility

- **τ₂ ≥ τ₁ ≥ 0** is GL's own ordering requirement. If τ₁ > τ₂, the theory predicts a *faster* response of the temperature than of the strain it is coupled to; the natural energy functional loses positivity and one branch can grow. (Stated as a structural expectation — I did not verify a published instability theorem for τ₁ > τ₂.)
- **k_th > 0, c > 0, M > 0, ρ > 0** as before.
- **Finite thermal speed**: GL does produce a finite propagation speed (this is its purpose), but unlike LS the speed is not simply √(κ/τ); its expression follows from the full cubic/quartic in ω and I have **not** verified the published closed form.

### R5. Characteristic equation

Because the coupling term carries τ₂ while the thermal terms carry τ₁, the determinant is

    (M k² − ρω²)(k_th k² − iωρc(1−iωτ₁)) + iβ²T₀ωk²(1−iωτ₂) = 0

⚠ **This is my construction from the R1 form**, not a transcription. It has the correct LS-like structure but with **two different prefactors** (1−iωτ₁) and (1−iωτ₂) — which is the mathematically essential content of "two relaxation times". Anyone checking our review's GL equation should check exactly this: if a paper writes the same (1−iωτ) in both places, it has silently collapsed GL into LS.

**Diagnostic worth putting in the paper:** GL ≡ LS when τ₁ = τ₂ = τ₀. Therefore any published "comparison of LS and GL" whose two curves coincide in the limit τ₁→τ₂ is correct, and any that reports them as qualitatively different *at* τ₁ = τ₂ contains an error.

### R6. When GL fails

- It has no flux relaxation, so it cannot represent heat-flux inertia (the physical content of Cattaneo). Where flux inertia is the mechanism (very high frequency, rarefied phonon transport), GL is the wrong tool.
- τ₁, τ₂ are not independently measurable in any experiment I could verify; they are fitted. A review should say that plainly.

## Evidence / Sources

| Claim | Source | Read level |
|---|---|---|
| Green & Lindsay 1972, J. Elasticity 2(1):1–7 | Crossref API | Record only |
| "two nonnegative times, one entering stress/entropy–temperature coupling and one entering the thermal equation"; "without using a heat-flux rate in exactly the Lord–Shulman manner" | Noble (2026) preprint §5.1, DOI 10.21203/rs.3.rs-10734164-v1 — **SECONDARY, unrefereed, and QUALITATIVE ONLY (no equations given)** | Body (PDF) |
| GL equations in R1–R2 | **standard form, NOT source-verified** — labelled UNVERIFIED | — |

## Checks done

- **Structural check**: the τ₁/τ₂ asymmetry in R5 is a *derived* consequence of the R1 form and preserves the correct limits (τ₁=τ₂=τ₀ ⇒ LS form; τ₁=τ₂=0 ⇒ Biot). I verified the τ₁=τ₂=0 limit symbolically reduces to the Biot determinant.
- **Cross-theory consistency**: GL's heat flux is Fourier, so the energy-flux expression used in Phase B3 should be the same as Biot's for GL — a constraint that will be used in B3 to test the manuscript.
- **Honest negative**: I could not obtain any open-access statement of the GL equations, from a review or otherwise. Two searches.

## Confidence

- **HIGH** that the τ₁/τ₂ structure described above is the standard GL construction and that GL ≡ LS at τ₁=τ₂ (this is a mathematical identity of the stated form, checkable by substitution).
- **MEDIUM** on the exact placement of τ₂ (on ε̈_kk vs on the whole coupling bracket). Variants exist.
- **LOW** on essentially all bibliographic content of the GL paper itself, and on the ordering constraint being *theirs* rather than a later imposition.

## NOT verified / open issues

1. **GL (1972) full text NOT opened.** The equations in R1–R2 are the common textbook form. **Everything about what Green & Lindsay actually wrote is UNVERIFIED**, including: the exact entropy expression, whether τ₂ multiplies ε̈_kk or the whole bracket, and whether they stated τ₂ ≥ τ₁.
2. **This is the weakest file in Phase B2.** It is also, uncomfortably, the model on which the manuscript is most likely to make a confident-sounding claim ("GL has two relaxations, one in the flux…"), because the brief's hint asserts something specific. I can confirm the *standard modern reading* (no flux relaxation; relaxation on temperature-rate terms) but **not** that it matches the 1972 paper. If the handler can supply the 7-page PDF, this file can be upgraded to HIGH in ~20 minutes.
3. **No GL dispersion relation from a primary source** was compared against R5. The cubic/quartic structure is mine.
4. The claim "GL produces a finite thermal speed" is standard but I have **not** verified the closed-form GL speed, and I would not let the manuscript print one without a source.
5. Ignaczak & Ostoja-Starzewski, *Thermoelasticity with Finite Wave Speeds* (OUP, DOI 10.1093/acprof:oso/9780199541645.001.0001, registered **2009-09-24**, 208 citations) is the obvious monograph source for GL. **SECONDARY-SOURCE ONLY and NOT opened** — note the book is commonly cited as 2010; Crossref registers 2009.

---

## R7. Revision R2 — notation mapping to standard $(\tau_0,\tau_1)$, and the corrected speed

### R7.1 What R2 asked, and what blocked it

> **R2 (GL):** use original notation ($\tau_0,\tau_1$ in standard literature; mine uses
> $\tau_1,\tau_2$). State the mapping explicitly and the admissibility ordering as stated in a
> source. **If 1972 still cannot be opened, say so and keep GL "do not print".**

**Green & Lindsay (1972) is STILL NOT OPENED.** *Journal of Elasticity* **2**(1):1–7,
DOI `10.1007/BF00045689`, Crossref 2929 — Springer paywall; no open-access statement of the GL
equations was found by a further search this session (same outcome as the first two attempts
recorded in §Method; not retried a fourth time). **Therefore: GL stays "do not print"**, and the
additional reason in §R7.2 now applies independently.

Everything in §R7.2–§R7.4 below is a statement about **the form of GL that the literature cites**,
not about what Green & Lindsay wrote on the page. Tag: **SECONDARY-SOURCE**, and weaker than that
for the ordering (§R7.4).

### R7.2 The mapping, slot by slot — and a defect in this file's notation

The GL system as it is most commonly cited uses two relaxation times, most often named
$(\tau_0,\tau_1)$, in these three slots:

| slot | standard-form symbol | this file (§R1, §R2) | consistent? |
|---|---|---|---|
| $\dot\theta$ in the stress: $\sigma_{ij}=\lambda e_{kk}\delta_{ij}+2\mu e_{ij}-\beta(\theta+\tau_1\dot\theta)\delta_{ij}$ | $\tau_1$ | $\tau_1$ | **yes** |
| $\ddot\theta$ in the energy equation | $\tau_0$ | $\tau_1$ | **NO** |
| $\ddot e_{kk}$ in the energy equation | $\tau_1$ | $\tau_2$ | **NO** |
| heat flux: $q_i=-k_{\text{th}}\theta_{,i}$ | no time | no time | yes |

So §R1's heat equation

$$\rho c(\dot\theta+\tau_1\ddot\theta)+\beta T_0(\dot e_{kk}+\tau_2\ddot e_{kk})=k_{\text{th}}\theta_{,ii}$$

uses **two** symbols for the **three** slots of the standard form. It coincides with the standard
form only in the special case $\tau_0=\tau_1=\tau_1^{\text{(mine)}}=\tau_2^{\text{(mine)}}$.

**Consequence — this is the point of R2.** The ordering constraint asserted in §R1/§R4
($\tau_2\ge\tau_1\ge0$) and the ordering quoted in the literature ($\tau_1\ge\tau_0\ge0$) are
**not** the same statement under any relabelling, because the two schemes do not agree slot for
slot. A reader (or a co-author) who "translates" $\tau_2\ge\tau_1$ into $\tau_1\ge\tau_0$ will get
a statement I cannot support. **Do not perform that translation, and do not print either ordering
from this file.** §R4's parenthetical ("stated as a structural expectation — I did not verify a
published instability theorem for $\tau_1>\tau_2$") stands and is now elevated to a warning.

The mapping that *can* be stated without ambiguity is the one-directional one used for the
manuscript: **the coefficient of $\ddot\theta$ in the energy equation is GL's $\tau_0$; the
coefficient of $\dot\theta$ in the stress (and of $\ddot e_{kk}$ in the energy equation) is GL's
$\tau_1$.** In this file's symbols those are, respectively, $\tau_1^{\text{(mine)}}$ and
$\tau_2^{\text{(mine)}}$ — hence $\tau_0\leftrightarrow\tau_1^{\text{(mine)}}$,
$\tau_1\leftrightarrow\tau_2^{\text{(mine)}}$ **as slot labels only**, while the stress slot in
§R1 is already labelled $\tau_1$, which is exactly the clash.

### R7.3 Corrected finite-speed statement (supersedes §R3 and the `V-B2z` GL cell)

Take the standard form. With pure Fourier flux and no coupling ($\beta=0$) the energy equation is

$$\tau_0\ddot\theta+\dot\theta=\kappa\nabla^2\theta ,\qquad \kappa=k_{\text{th}}/(\rho c),$$

which is the telegrapher's equation. It is hyperbolic and has the **closed-form finite speed**

$$\boxed{\,c_h=\sqrt{\kappa/\tau_0}\,}$$

i.e. GL's thermal wave speed is controlled by the coefficient of $\ddot\theta$ (GL's $\tau_0$), not
by any flux relaxation. **Verified numerically** (reference material $\kappa=1.254181\times10^{-5}$
m²/s): $v_{ph}\to354.144$ m/s at $10^{12}$–$10^{13}$ Hz for $\tau_0=10^{-10}$ s, against the
predicted $\sqrt{\kappa/\tau_0}=354.14$; and $v_{ph}\to250.418$ m/s for $\tau_0=2\times10^{-10}$ s
against $250.42$. At low frequency $v_{ph}\propto\sqrt{\omega}\to0$ (diffusive branch), so the
*maximum* propagation speed is $\sqrt{\kappa/\tau_0}$; the speed is bounded but approached from
below, which is why a numerically-evaluated $v_{ph}$ at $10^{8}$ Hz ($121.7$ m/s) looks nothing
like it.

**This also resolves an internal inconsistency in this file.** §R5's determinant carries factors
$(1-i\omega\tau_1)(1-i\omega\tau_2)$, i.e. the flux-relaxation (DPL/Jeffreys) structure, whereas
§R1 correctly says GL has *no* relaxation in the flux. Those cannot both describe the same medium.
The resolution: §R5 is the symbol of the standard form *after* applying the mapping of §R7.2 with
$\tau^{\text{(mine)}}_1\equiv\tau_0$; its uncoupled factor
$k_{\text{th}}k^2-i\omega\rho c(1-i\omega\tau^{\text{(mine)}}_1)$ is precisely
$\tau_0\ddot\theta+\dot\theta+\kappa k^2\theta=0$, giving $\sqrt{\kappa/\tau_0}$ as above. §R5 is
therefore correct **as a symbol** but its labels must not be carried into print.

**Contrast with DPL, which is the reason the distinction matters:** DPL's T1 truncation
$q+\tau_q\dot q=-\kappa\nabla\theta-\kappa\tau_\theta\nabla\dot\theta$ gives
$\tau_q\ddot\theta+\dot\theta=\kappa\nabla^2\theta+\kappa\tau_\theta\nabla^2\dot\theta$, whose
extra $\nabla^2\dot\theta$ makes $k^2$ grow with $\omega$ and $v_{ph}\propto\sqrt{\omega}$
**unbounded** (measured 1.255×10³, 1.255×10⁴, 1.255×10⁵ m/s at $10^{10}$, $10^{12}$, $10^{14}$ Hz
— see `V-B2p`). GL has no such term and is genuinely finite-speed. **"GL and DPL are both
hyperbolic" is true but incomplete: only GL is finite-speed in the telegrapher sense.**

### R7.4 The admissibility ordering — why I will not state it

R2 asks for the ordering "as stated in a source". I could not obtain such a statement from any
source I opened, and there is a substantive reason to be cautious:

- With $q_i=-k_{\text{th}}\theta_{,i}$ (GL's flux law, unchanged), the classical dissipation
  inequality $-q_i\theta_{,i}\ge0$ reads $k_{\text{th}}|\nabla\theta|^2\ge0$, which holds
  **identically for every value of $\tau_0$ and $\tau_1$**. The relaxation times therefore cannot
  be constrained by the flux part of the second law at all. Any ordering $\tau_1\ge\tau_0$ must
  come from GL's specific construction of the free energy/entropy as functions of
  $(\theta,\dot\theta,e_{ij})$ — which is exactly the part I cannot check without the paper.
- For the uncoupled heat equation, $\tau_0 s^2+s+\kappa k^2=0$ is stable for all $k$ **iff
  $\tau_0>0$**; $\tau_1$ does not appear. So no ordering involving $\tau_1$ can follow from
  well-posedness of the heat equation.

**Conclusion: I assert only $\tau_0>0$ (necessary for the uncoupled heat equation to be stable),
and I record the ordering $\tau_1\ge\tau_0\ge0$ as an unverified convention that must be sourced
from Green & Lindsay (1972) before it appears anywhere in the review.** If the handler supplies
the PDF, the three things to check on the page are: (i) the coefficient of $\ddot\theta$,
(ii) the coefficient of $\ddot e_{kk}$, (iii) whether an inequality between the two times is
stated and from which equation it follows.

### R7.5 Effect on the other files

- `V-B2z_comparison_table.md`: GL row's "finite speed: Yes (speed not verified in closed form)"
  is superseded by $c_h=\sqrt{\kappa/\tau_0}$, but the row still carries "printable: no".
- `V-B2p`: DPL and GL are **not** in the same hyperbolic class; see the contrast in §R7.3.
- `V-B2a`: the Biot/Fourier row is unaffected.

## R8. Revision (2026-10-22) — the GL slot structure, now source-backed

R8 supersedes the slot assignment of §R1–§R3 and the ordering discussion of §R7.4. It was written
after `control/ARBITRATION_B4.md` disputed a charge I had made against the manuscript (my `V-B4` W1),
and the arbitration was right: **the manuscript's GL system is the standard one and my charge was
wrong**. This section records the sources and the corrected statement.

### R8.1 Three independent statements (all opened 2026-10-22)

**S1.** Bera, Mondal, Mahapatra, Roymahapatra, Acharjya, "Generalized theory of thermoelasticity in
isotropic and homogeneous thermoelastic solids", *Turkish Journal of Mathematics and Computer
Science*, article 11902 (turcomat.org/index.php/turkbilmat). Access: **full text, open.**
GL equations (12)–(15): energy `−q_{i,i}+ρQ = ρc_e(Ṫ+α₀T̈) + βT₀u̇_{i,i}`; stress
`τ_ij = λu_{i,i}δ_ij + 2μe_ij − β(T+αṪ)δ_ij`; **Fourier law unchanged**; ordering **`α ≥ α₀ > 0`**.

**S2.** Singh, B., "A GL Model on Thermo-Elastic Interaction in a Poroelastic Material Using Finite
Element Method", *Symmetry* **12**(3):488 (2020), DOI `10.3390/sym12030488`. Access: **full text,
open.** Energy equation (11) carries `τ₀s` in the operator `(∂_t + τ₀s∂²_t)` applied to *both* the
temperature and the strain-rate terms; stress (13) carries `τ₁s`; ordering **`0 < τ₀s < τ₁s`** (stated in the article's abbreviations
block, not in an equation display).
This is the closest match to the manuscript's uniform `(1+τ₀∂_t)` operator.

**S3.** "Thermodynamic Admissibility, Finite-Speed Heat Transport, and Wave Stability in Generalized
Thermoelasticity: A Critical Review with Analytical Proofs", Research Square preprint
rs-10734164/v1. Access: **section text, open** (preprint — corroboration only). GL "introduces
relaxation in constitutive relations without using a heat-flux rate in exactly the Lord–Shulman
manner … two nonnegative times, one entering stress/entropy-temperature coupling and one entering the
thermal equation".

### R8.2 The corrected slot table

| slot | symbol in the standard form | in this file's §R1 | status |
|---|---|---|---|
| `T̈` in the energy equation | **τ₀** (energy/entropy time) | τ₁ | **wrong label** |
| `ë_kk` in the energy equation | same operator as `T̈`: **τ₀** (S2) or absent (S1) | τ₂ | **wrong: no independent τ₂** |
| `Ṫ` in the stress | **τ₁** (stress time) | τ₁ | correct |
| heat flux | **no relaxation — plain Fourier** | none | correct |
| ordering | **`τ₁ ≥ τ₀ > 0`** (S1 `α ≥ α₀`; S2 `0 < τ₀ < τ₁`) | `τ₂ ≥ τ₁` | **wrong direction** |

So GL has **two** relaxation times in **two** slots (stress, energy), not two times inside the energy
equation. §R3's `√(κ/τ₀)` thermal speed stands unchanged: it depends only on the coefficient of `T̈`,
which is the energy time — and in the corrected labelling that is GL's τ₀, exactly as §R7.3 says.

### R8.3 Why my §R1 assignment was wrong, and the trap it hides

I had put one time on `T̈` and another on `ë_kk` in the same equation. That is not GL under any
labelling: it would require the entropy to carry two different relaxation times, and no source I found
does that. The trap is that this assignment reproduces the *observable* structure of GL for a pure
thermal problem (β = 0), where only the `T̈` coefficient matters — which is why it survived several
revision rounds. The check that exposes it is the one §R7.2 already demands: write the slots down and
compare slot-by-slot with a source, not kernel-by-kernel.

### R8.4 What stays "do not print", and why the reason is now sharper

GL still stays "do not print **from this file**", but the reason changes. It is no longer "the form is
unverified" — the form is now sourced three ways. It is that **the paper must state GL's flux law**:
GL keeps Fourier, while LS (and the manuscript's eq. 4.4) has `q_i + τ₀q̇_i = −kT_{,i}`. A reader who
carries (4.4) forward gets DPL-with-equal-lags. The manuscript's §4.4 does not say which it means, and
in its notation `τ₀` plays the LS flux role in §4.3 and the GL energy role in §4.4. One sentence fixes
it; until then, GL equations should not be quoted from either paper.
