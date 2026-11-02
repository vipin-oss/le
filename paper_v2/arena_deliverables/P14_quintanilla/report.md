# P14 — Quintanilla 2003, the delay-parameter condition, and the DPL stability sentence

Evidence only: no `.tex` was edited, no script outside this folder was edited, no PDF and no library
location is written here. Every quote is at most 15 words and carries an equation or theorem number
plus the **printed** page. A DOI is recorded only where the article prints one.

Deliverables: `report.md`, `evidence.csv` (55 rows, 7 papers), `refs_P14.bib`, `check_p14.py`.

## 0. First, a correction: the file the brief named is not Quintanilla 2003

The brief pointed at a file it expected to be Quintanilla's *Journal of Thermal Stresses* paper. It is
not. That file is **18 pages** and its own title page reads:

> Quintanilla, R. and Racke, R., "Stability in thermoelasticity of type III", *Discrete and Continuous
> Dynamical Systems — Series B* **3**(3) (2003) 383–400.

So it is a different 2003 paper by the same first author, about Green–Naghdi **type III** thermoelasticity
(exponential stability in one space dimension by energy methods and by spectral methods, plus
equipartition of energy), not about dual-phase lag. It is not used for the delay-parameter claim. It is
recorded under its own key `QuintanillaRacke2003DCDS` because it is worth citing elsewhere (see §6).

**The right paper was in the library after all**, under a plain author-year name: *Journal of Thermal
Stresses* **26**(7) (2003) 713–721, DOI 10.1080/713855996, 9 printed pages. It was identified from its
own cover page and article page, not from the file name.

## 1. What Quintanilla 2003 actually contains

Model and Taylor order (p. 714):

* the model is one-dimensional homogeneous isotropic thermoelasticity with the Chandrasekharaiah–Tzou
  dual-phase-lag flux, eqs. (2)–(3), p. 715;
* the expansion is taken on both sides of Tzou's lag equation and, in the paper's words, "up to the
  second order in tq but only to the first order in ty" (p. 714) — i.e. **second order in τ_q, first
  order in τ_T**, exactly the variant the review sentence names;
* the two lagged operators are written θ̂ = θ + τ_T θ̇ and θ̃ = θ + τ_q θ̇ + ½τ_q²θ̈, eq. (4), p. 715,
  so the heat equation is third order in time.

The argument (pp. 714–718):

* eigenfunctions of the form (12), p. 716, which give a homogeneous 2×2 system (13)–(14), p. 717;
* setting the determinant to zero gives a **fifth-order characteristic polynomial** in ω, eq. (15),
  p. 717;
* the spectrum is pushed to the left of the line Re z = −ε by the shift (16), p. 717, and the sign of
  the real parts is decided by the **Hurwitz theorem**, (17)–(19), p. 717 ("In this second step we use
  the Hurwitz theorem", p. 714);
* the Hurwitz determinants carry the condition explicitly:
  `L2 = 2n²(2τ_T − τ_q) + 4 + E Q2(n²)τ_q³`, eq. (23), p. 718, and likewise (24) with
  `4n⁴(2τ_T − τ_q)(1 + τ_qγ)`. **The factor (2τ_T − τ_q) is where the "one half" comes from**;
* the condition itself is eq. (11), p. 716: **τ_T > τ_q/2**.

Results:

* **Theorem 1, p. 718**: "Then the solutions decay exponentially to zero" — for the problem with
  eqs. (5)–(6), initial conditions (8) and boundary conditions (9), under the integral condition (10);
* instability, p. 719: when (11) fails, an eigenvalue with positive real part exists; the conclusions
  of §4 state that "there exist unstable solutions" (p. 720);
* conclusions, p. 720: (i) for τ_T > τ_q/2 the solutions of the one-dimensional thermoelastic problem
  are exponentially stable; (ii) for τ_T < τ_q/2 there exist unstable solutions.

**Which stability notion?** The paper claims **exponential stability**, and its method is
**spectral** (eigenvalue polynomials + Hurwitz). One caveat matters if the sentence is to survive a
referee: the step from "spectrum left of Re z = −ε" to "exponentially stable" needs the solutions to
live in a C₀-semigroup, and the paper imports that — "we can obtain the solutions by means of a
semigroup" (p. 714), referring to the 2002 companion paper, where the decay is proved with **energy
functionals**, eqs. (4.2)–(4.4), p. 221. So: spectral argument for the condition, energy/semigroup
argument for the exponential rate. Both are the same author's, and the review sentence's word
"spectral" describes the 2003 step correctly.

## 2. Verdict on the s06_lags sentence

The sentence: *"Quintanilla derived the condition τ_T > τ_q/2 (exponential stability, with instability
for τ_T < τ_q/2) by a spectral argument, for the version where the flux is expanded to second order in
τ_q and the gradient to first order in τ_T."*

| clause | evidence | page |
|---|---|---|
| condition τ_T > τ_q/2 | eq. (11) | 716 |
| exponential stability | Theorem 1, conclusions (i) | 718, 720 |
| instability for τ_T < τ_q/2 | §4, conclusions (ii) | 719, 720 |
| by a spectral argument | polynomial family (15) + Hurwitz (17)–(19) | 714, 717 |
| second order in τ_q, first order in τ_T | text + operators (4) | 714, 715 |

**Verdict (s06_lags sentence): SUPPORTED.** Every clause maps to a printed page, and the variant name
in the sentence is the paper's own description. The single refinement worth adding is one clause long:
*the exponential conclusion rests on the semigroup established in the companion 2002 paper, p. 714;
the 2003 paper supplies the spectral bound.*

## 3. S5, re-judged

P13 judged S5 — the claim "Quintanilla 2003: stability iff τT > τq/2 for dual-phase-lag" — as
**NOT SUPPORTED**, and it was right to, because the two books in that batch contain neither the
inequality nor a citation of it, and both put the character change at τT = τq. P13 also wrote down the
correct remedy: re-derive the sentence from the primary paper, which it did not have. That paper is now
read. Re-judged:

| id | wording | verdict |
|---|---|---|
| S5 (P13, as written) | "Quintanilla 2003: stability iff τT > τq/2 for dual-phase-lag" | **NOT SUPPORTED** — stands. Unqualified it is false for the first-order-in-both model and it conflates two different thresholds (§4). |
| S5 (variant-qualified) | the s06_lags sentence quoted in §2 | **SUPPORTED** — every clause maps to a printed page. |

Everything in P13 that made S5 look unsupported is still true and is now explained rather than
contradicted:

* Tzou never cites Quintanilla and states no DPL stability theorem; his number is `B = τ_T/(2τ_q)` with
  the critical point at `B = 1/2`, i.e. **τ_T = τ_q**, and that is a *wave-character* boundary, not a
  stability boundary (P13 evidence, pp. 81–86).
* Ignaczak's **Theorem 1.1, p. 18** says the first-order-in-both DPL temperature field is hyperbolic iff
  `τ_q − τ_T > 0` — again **τ_T = τ_q**, again a type boundary.
* Ignaczak lists Quintanilla 2003 only in the bibliography (p. 399) and never reproduces its condition.

## 4. Why 1, ½ and 2−√3 are all correct: three Taylor variants, three thresholds

The literature contains three distinct time-differential DPL models, and each has its own threshold.
This table is the reconciliation the review needs.

| variant | Taylor orders | threshold on ω = τ_T/τ_q | source (page) | what the number means |
|---|---|---|---|---|
| (i) | first order in both | **ω = 1** | Tzou `B = τ_T/(2τ_q)`, `B = 1/2`, pp. 81–86; Ignaczak Theorem 1.1, p. 18 | change of *type*: wave-like vs overdamped; hyperbolic vs parabolic |
| (ii) | second in τ_q, first in τ_T | **ω = 1/2** | Quintanilla 2002 eq. (4.1), p. 221; Quintanilla 2003 eq. (11), p. 716 and Theorem 1, p. 718; Quintanilla–Racke 2006 eq. (1.5), p. 1210 | *stability*: exponential decay above, instability below |
| (iii) | second order in both | **ω = 2 − √3 ≈ 0.268** | Quintanilla–Racke 2006 eq. (3.12), p. 1212 (sufficient form eq. (3.3), p. 1211: ω ≥ √2 − 1); Fabrizio & Lazzari 2014 eq. (4), p. 485 | first-model stability, and the Second Law then narrows it to a two-sided band |

Two consequences worth stating in the paper:

1. **The qualifier is load-bearing.** Quintanilla–Racke 2006 exist precisely to show that variants (ii)
   and (iii) have different stability regions: "there is an open set of parameter values for which"
   one is stable and the other is not (p. 1210), namely `2 − √3 < ω < 1/2` (their (4.1), p. 1212). A
   sentence that drops the variant would be wrong by a factor of about 1.9 in the threshold.
2. **The "½" is a property of variant (ii), visible in the algebra.** In Quintanilla 2003 the Hurwitz
   determinant is proportional to `(2τ_T − τ_q)`, eq. (23), p. 718 — that factor *is* the half. In the
   first-order-in-both model the corresponding factor is `(τ_q − τ_T)`, which is why Tzou and Ignaczak
   land on 1.
3. Tzou himself is quoted by Quintanilla–Racke (p. 1210) as saying that second-order expansions in
   *both* lags "should also involve a second-order time derivative … resulting in an equation of
   parabolic type" — the reason variant (iii) is a separate model and not a refinement of (i).

## 5. The other five sources: one-line verdicts

| key | paper | Taylor variant | stability notion | verdict in one line |
|---|---|---|---|---|
| Quintanilla2002JNET | *Exponential Stability in the Dual-Phase-Lag Heat Conduction Theory*, J. Non-Equilib. Thermodyn. **27** (2002) 217–227 | (ii) — same third-order-in-time equation, (2.1) p. 218 | **exponential stability in time** by energy functionals under (4.1) `τ_T > τ_q/2`, p. 221; **instability** by exact solutions, p. 222; also **spatial** decay, p. 218 | this is where the ½ first appears, and it is an energy argument, not a spectral one |
| QuintanillaRacke2006IJHMT | *A note on stability in dual-phase-lag heat conduction*, IJHMT **49** (2006) 1209–1213 | (ii) and (iii) side by side: (1.4)–(1.5) p. 1210 vs (1.8) p. 1210 | (exponential) stability vs non-stability of the two models, by characteristic polynomials; explicit caution that "the supremum of the spectrum does not describe" the semigroup type, p. 1211 | the paper that proves the variant distinction; cite it whenever the qualifier is used |
| FabrizioLazzari2014 | *Stability and Second Law of Thermodynamics in dual-phase-lag heat conduction*, IJHMT **74** (2014) 484–489 | (ii) as model (2), p. 484, and (iii) as model (3), p. 485, both as fading-memory materials | **exponential decay** by Laplace/Fourier estimates, Theorem 4.1, p. 488, compared against the Second Law: for (ii) the two coincide, for (iii) stability is wider than the thermodynamic band (4), p. 485 | the thermodynamic-admissibility counterpart; useful for the "which restrictions are physical" paragraph |
| ChiritaDApiceZampoli2016 | *The time differential three-phase-lag heat conduction model: Thermodynamic compatibility and continuous dependence*, IJHMT **102** (2016) 226–232 | **three**-phase-lag, second order in τ_q and first order in τ_T and τ_α, eq. (3), p. 227 | **continuous dependence** on data and supply, not exponential stability; the relaxed estimate deliberately "allows the solutions to grow exponentially in time", p. 226 | the TPL analogue; do not cite it for exponential stability |
| ChiritaCiarlettaTibullo2017 | *On the thermomechanical consistency of the time differential dual-phase-lag models of heat conduction*, IJHMT **114** (2017) 277–285 | **all** order pairs (n in τ_q, m in τ_T) | algebraic: for n ≥ 5 the constitutive characteristic equation has a root with positive real part, i.e. instability, p. 279; for n, m ≤ 4 the roots are in the left half-plane, p. 279, and thermodynamic consistency is then checked, p. 284 | the "how far can you truncate" paper; supports any statement that the order is a modelling choice with consequences |

None of the six asked for is missing. Two of them (the 2002 heat-conduction paper and the 2016
three-phase-lag paper) live inside archive files in the library rather than as loose documents; they
were identified from their own title pages and are cited here under their own keys. Archive names are
deliberately not written into this repository.

## 6. Knock-on for other statements

* **S4 (P13) gains a witness.** `QuintanillaRacke2003DCDS` (DCDS-B **3** (2003) 383–400) proves
  exponential stability of Green–Naghdi **type III** in one space dimension by both energy and spectral
  methods, and states on p. 383 that type II "does not allow the dissipation of the energy". That is a
  clean, citable separation of types II and III, which is exactly what S4 needs when it says the
  Green–Naghdi family behaves differently from the lagged models.
* **The "spectral vs exponential" distinction is worth one sentence** wherever the review uses the
  word "spectral": Quintanilla–Racke 2006, p. 1211, state explicitly that a spectral bound does not by
  itself give the semigroup type, and then prove what they need.

## 7. Recommended wording for s06_lags

> Quintanilla [Quintanilla2003JTS] derived the condition τ_T > τ_q/2 — exponential stability above it,
> instability below (Theorem 1, p. 718; §4, p. 720) — by a spectral argument (a fifth-order
> characteristic polynomial, eq. (15), p. 717, resolved with the Hurwitz criterion), for the variant in
> which the flux is expanded to second order in τ_q and the temperature gradient to first order in τ_T
> (p. 714); the exponential rate itself uses the semigroup established in the companion
> heat-conduction paper [Quintanilla2002JNET], p. 714. The threshold is ½ only for this variant: with
> first-order expansions in both lags it is τ_T = τ_q [Tzou2015 pp. 81–86; Ignaczak2010 Thm 1.1, p. 18],
> and with second-order expansions in both it becomes τ_T = (2 − √3)τ_q [QuintanillaRacke2006IJHMT
> eq. (3.12), p. 1212].

## 8. Gates and hygiene

`check_p14.py` (this folder), `check_p8.py`, `check_p9.py`, `check_p10.py`, `check_p11.py`,
`check_p13.py` and `check_readme_paths.py` all print PASS and exit 0. No PDF, no `.tex`, no link, no
library location and no archive name is in this folder; no key here collides with the 81 keys already
carried by `P8_coverage` (72), `P10_verification` (3) and `P13_books` (6). The gate also asserts the
column count of every `evidence.csv` row, the check whose absence let a column shift through in P13.

## 9. Limitations

* The "spectral, not energy" wording is a description of the 2003 *method*; the *conclusion* of
  exponential decay also leans on the 2002 semigroup. Both papers are in the library and both are
  cited, so the review can state this precisely instead of choosing.
* Quintanilla 2003 proves the result for one space dimension with boundary conditions (9) and the
  integral condition (10); no claim is made here about higher dimensions.
* The five one-line verdicts in §5 rest on the abstract, the model equations and the sections that
  state the conditions — not on every proof in those papers.
