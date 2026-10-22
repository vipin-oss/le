# V-B4 — independent audit of the manuscript (Round 2, math truth)

**Task.** Audit every displayed constitutive law, governing PDE, dispersion relation, wave-speed
formula, energy density/flux/dissipation expression and interface condition in
`phase5/master/{sections/sec03,sec04,sec06,sec07,sec09,sec10,appendices/appA,appB,energy_flux_derivations}.tex`
of branch `arena/40393d9f-le`, plus every sentence in those files asserting finite speed,
dissipativity, energy conservation, stability, well-posedness or thermodynamic consistency.
Deliverables: `verification/EQUATION_LEDGER.csv`, `verification/CLAIM_LEDGER.csv`, this summary.

**Method.** Manuscript read only (checked out into `/tmp`, never edited; no file outside
`verification/` touched). Each display was re-derived or limit-checked on paper; two results needed
computation and are scripted: `V-B4_secular_degree.py` (sympy, degree of the 2-D P–SV–T determinant)
and `V-B4_energy_flux_convention.py` (numeric, reuses the `V-B3d` interface solver). Judgements were
made against my own reference sheets (`V-B1*`, `V-B2a`…`V-B2z`, `V-B3a`…`V-B3e`), which were written
before the manuscript was opened; no manuscript wording was adopted.

## 1. Result — counts

| ledger | rows | CORRECT | CORRECT-CONDITIONAL | WRONG | UNCLEAR | UNVERIFIED | NOT-CHECKABLE |
|---|---|---|---|---|---|---|---|
| equations | **130** | 105 | 19 | **3** | 2 | 1 | — |
| claims | **29** | 18 | 5 | **3** | 1 | — | 2 |

Coverage: all 132 display environments in the assigned files (130 rows; two pairs are the same
equation printed twice and are merged explicitly). The manuscript's own register (`appA`) has **no
rows at all** for Sections 6, 7 and 9 — see §3.8.

The headline number is not "3 wrong". It is that **the paper is wrong in the two places where it
stops hedging and states a result** (the GL energy equation, the degree of the secular polynomial),
and **hedges in the two places where a real result exists** (the GL parameter restriction, and the
Clausius–Duhem/Coleman–Noll pair that it actually derives). Both failure modes are fixed by the same
habits: derive it, then state it.

## 2. The three WRONG equations

**W1 — `sec04:101`, eq. (4.9), the Green–Lindsay energy equation.** Printed as

    rho c_v (Tdot + tau_0 Tddot) = k lap T - beta T_0 (div udot + tau_0 div uddot)

which is a **verbatim copy of the LS equation (4.5)** directly above it, while the GL stress
(4.10) two lines later carries the *other* relaxation time:

    sigma_ij = lambda eps_kk delta_ij + 2 mu eps_ij - beta (T + tau_1 Tdot) delta_ij

In GL the same time multiplies the temperature-rate terms in the stress and in the energy equation,
because both descend from one free energy `psi(eps, T, Tdot)`. Four lines, which is why I am
confident without the 1972 paper (paywalled, not opened):

    s = -dpsi/dT = (beta/rho) eps_kk + (c_v/T_0)(T + tau_1 Tdot)
    rho T_0 sdot = -q_{i,i}   =>   rho c_v (Tdot + tau_1 Tddot) = k lap T - beta T_0 (div udot + tau_1 div uddot)
    q_i + tau_0 qdot_i = -k T_{,i}      with      tau_0 > tau_1 > 0

So the corrected (4.9) carries **tau_1**, not tau_0, and the flux law (4.4) has tau_0. As printed,
(4.9) and (4.10) are inconsistent unless tau_0 = tau_1 — in which case the model is LS with a shifted
stress, i.e. not GL. Confidence MEDIUM only because the primary text is unopened; the inconsistency
itself is internal and does not depend on the primary text.

**W2 — `sec09:117`, eq. (9.9), "an eighth-order polynomial in q for coupled thermo-piezoelastic
media".** Computed (`V-B4_secular_degree.py`, sympy, exact determinant of the 3×3 (u₁, u₃, T) system):

| theory | degree in q | in q² |
|---|---|---|
| Biot (Fourier) | **6** | 3 |
| Lord–Shulman | **6** | 3 |
| Green–Naghdi III | **6** | 3 |

Degree 8 requires **four** branches per medium. Every single-temperature theory in Sections 4 and 6
has **three** (qP, qSV, qT); a quasi-static electric potential adds none, because `div D = 0` slaves
it to (u, T). Correct statement: *cubic in q² (degree 6) for the three-mode theories; quartic in q²
only when a second thermal branch exists* (a fourth-order-in-space heat operator, or a
carrier/plasma mode in a semiconductor — not the "thermo-piezoelastic" case in the caption).
This one propagates: §9.6's condition-counting sentence points at this polynomial.

**W3 — `energy_flux_derivations.tex:270`, the Fourier transform of the finite-horizon derivative.**

    D_omega f(t)  <->  [(1 - e^{-i w_f omega}) / (i w_f omega)] (-i w_f) fhat    "(simplified)"

Correct only for `kappa == 1` (a moving average of the derivative). With the inherited kernel (6.8),
`kappa(t) != 1`, so the finite-horizon operator is a **convolution** and has no multiplicative
symbol; no such factor exists. "Simplified" does not make it defined. Either state `kappa == 1` or
delete the line — it is the only place in the paper where a transform is asserted without a caveat,
in a section that is otherwise scrupulous about it.

## 3. The rest of the ranked list (4–15)

**4. `sec09:151`, eq. (9.10): `A = D/|J_inc|` with `D` never scoped.** Computed
(`V-B4_energy_flux_convention.py`, steel|Al, normal incidence, 3 models × 5 frequencies):
`D_tot/J_inc` equals `R + T` to within **1.5e-3** — because in an attenuating medium everything that
crosses is eventually dissipated. Substituting into (9.12) therefore gives `R+T+A ≈ 2`, i.e. the
identity fails by ~1 for every dissipative case. It holds only if `D` is **interface-local**. One
word fixes it, and without the word the sentence at `sec09:178` ("any inconsistency … shows up
immediately") is pointing at the paper's own definition.

**5. `sec09:151`, per-mode numerators.** `J_ref` read as the reflected *mode* rather than the
reflected *field* is not the same quantity once the medium is attenuating or carries two branches.
Measured, with the paper's own flux in (10.3): `sum R + sum T = 0.667226` for **GN-II**, which is
lossless and must give exactly 1.000000. Total-field accounting repairs it to 1.000000 for all three
models. The caveat is in §10.5 in prose; it is not in (9.10), where the reader will implement it.

**6. `sec09:187,190` — attributing a closed balance to specific papers** ("the conservation identity
remains satisfied", "the energy balance closed"). NOT-CHECKABLE here (full texts not opened), and
**flagged rather than accepted**, because items 4–5 show the identity does not close automatically
for a piezothermoelastic interface with per-mode numerators. An assertion that someone else's
identity closed is a strong claim; it needs the paper's flux convention quoted, not paraphrased.

**7. `appA` EQ-005 and EQ-006 marked UNVERIFIED** (Clausius–Duhem, Coleman–Noll) although `sec03:182`
and `sec03:207` **derive both**, and I re-derived them. The register contradicts the body: it
hedges a proof it has and asserts a result it has not got (see 8).

**8. `appA` coverage.** The register's layers stop at Sections 3, 4, 5, 10. Sections 6 (memory
fluxes), 7 (nonlocal dispersion) and 9 (the energy partition, i.e. the paper's own headline
mechanism) have no register rows. It reads as a complete audit; it is not one.

**9. `sec07:41`, eq. (7.3).** Strain-gradient elasticity `sigma = C eps - ell^2 C lap eps` is given,
but only the **nonlocal** dispersion (7.4) follows. (7.3) behaves oppositely:
`omega^2 = c_0^2 k^2 (1 + ell^2 k^2)`, phase speed growing without bound as k → ∞. A subsection
titled "size-dependent wave behavior" that shows the band-limited case and omits the stiffening case
inverts the physical message of the section, and `ell^2 > 0` is never stated.

**10. `sec03:199,207`.** `psi = psi(eps, T)` is presented as the general route from the dissipation
inequality. It is the *classical* route: it excludes `Tdot`-dependence (GL), thermal displacement
(GN-II/III), memory (DPL/MDD) — i.e. every model the review is about. The label is missing, so §3
appears to license §4 while in fact contradicting it.

**11. `sec04:43` and `sec03:264`: `c_p = sqrt((lambda+2mu)/rho)` with the isothermal λ of (3.21).**
That is the **isothermal** P speed. The ultrasonic (adiabatic) speed is
`sqrt((lambda+2mu+beta^2 T_0/(rho c_v))/rho)`; for steel `beta^2T_0/(rho c_v) = 2.77e6 Pa` against
`2.72e11 Pa` (5e-6 relative — 0.03 m/s, negligible), but for soft or high-expansion materials it is
not, and no reader can tell from the paper which one is tabulated. Also `c_p` is the universal
symbol for specific heat at constant pressure in a paper that uses `c_v` throughout.

**12. `sec06:95`, kernel `kappa = 1 - 2 beta (t-xi)/omega + alpha^2 (t-xi)^2/omega^2`**: `alpha` is
the fractional order two displays earlier, `beta` is the thermal-stress coefficient everywhere else,
`omega` is the angular frequency everywhere else. Three collisions in one line.

**13. `sec03:92` / `appB:60`: σ symmetry derived with no couple stress**, in a review that devotes
§5 to micropolar continua where σ is not symmetric. `appA` marks it CONDITIONAL; the body does not.
One clause suffices, and it is the kind of thing a critical review is expected to catch.

**14. Equation-number inflation.** (4.5) ≡ (4.9) (same symbols, one of them wrong); (4.19) ≡ (6.4);
(6.11) ≡ (6.12) ≡ (A.x) ≡ (A.y); `q_i - sigma_ij v_j` is numbered at least five times across
§3.8, §6.5, §10.2 and Appendix. For a 148-page AMR submission this is a reviewing risk, not a
cosmetic one.

**15. Table T6, "Thermal interface" row**: lists `T` continuity *and* "temperature jump" *and*
"interfacial thermal resistance" as one configuration. They are three different interfaces: perfect
contact has no jump; a Kapitza contact replaces `[q_n] = 0` by `q_n = h (T_1 - T_2)`. This is the
one table row where the summarised physics is wrong rather than merely unchecked.

## 4. Safe vs unsafe

**Safe (I would not challenge these).** §3.1–3.4 kinematics and stress power (EQ-001…016);
§3.6–3.7 free energy, stress, entropy, Fourier restriction (EQ-020…022, 019); classical speeds
(EQ-023, 025); conventions (EQ-026, 027) — stated once, correctly, and used consistently;
§4.2 Biot pair (EQ-036, 037); §4.3 LS (EQ-039…041) — exact operator, no truncation caveat needed;
§4.5 GN-II and §4.6 GN-III (EQ-044, 045, 047); §6.2–6.4 Caputo/RL/hereditary definitions;
§7.1–7.2 nonlocal integral and differential forms (correctly scoped to the Helmholtz kernel);
§9.3–9.4 matching conditions; §10.1–10.3 flux, mean flux and the pillbox jump (EQ-080…085); the
whole of Appendix B (reproduction of §3, no new error).

**Unsafe.** §4.4 GL (W1 + CL-006); §9.5 secular equation (W2); §9.7 energy ratios (items 4–5) and
the literature attribution (item 6); the MDD transform (W3); §7.3 by omission (item 9); the
register (`appA`) as an audit record (items 7–8); Table T6's thermal row (item 15).

## 5. Checks done

1. Re-derivation of every display in §3, §4, §6, §7, §9, §10 and Appendix B (130 rows).
2. Symbolic degree of the 2-D (P,SV,T) determinant for three theories — `V-B4_secular_degree.py`.
3. Numeric flux-convention test: three models × five frequencies, per-mode vs total-field vs
   quadratic flux, `A = D/J_inc` — `V-B4_energy_flux_convention.py`.
4. Dimensional and notation-collision scan across all nine files (`c_p`, `alpha`, `beta`, `omega`).
5. Cross-check of every ledger verdict against my pre-existing V-files (column "compared with").
6. Consistency between body and register (`appA`): 2 contradictions found.

## 6. Confidence

HIGH for the 130 equation verdicts (all re-derived; the two computed ones are exact/numeric with
explicit code). MEDIUM for W1's attribution to Green–Lindsay 1972 (primary text unopened; the
internal inconsistency is HIGH confidence). LOW for the two §9.7 literature attributions (I did not
open those papers — flagged, not judged).

## 7. NOT verified / open issues

- Green–Lindsay 1972, Tzou's DPL papers, the Quintanilla–Racke series and the five interface papers
  named in §9.7 were **not opened** (paywalls; see `V-B3c` §3.4 search log). Nothing in this file
  depends on their content except where marked MEDIUM/LOW.
- Sections 5, 8, 11–17, the bibliography (beyond Crossref existence checks), T1–T5, T8, the figures
  and the 148-page PDF build were **not** audited — outside the B4 scope as ordered.
- I did not check that the labels/`\eqref`s point to the equations I read by line number; I audited
  the equations as they appear at `file:line`.
- The manuscript is in a state where 8 of 9 rows of Table T7 say "OPEN". That is honest but it is a
  compendium of audit tasks, not a review; the fix is the same three or four model-specific
  derivations that `V-B3a`…`V-B3d` show are tractable in a day each.
