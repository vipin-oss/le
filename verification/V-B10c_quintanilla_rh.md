# V-B10c — independent Routh–Hurwitz check of Quintanilla's TPL stability window

**Date 2026-10-22. Branch `arena/04fdf32e-le`. Target claim:** Quintanilla, R. (2009), *Spatial
behaviour of solutions of the three-phase-lag heat equation*, Appl. Math. Comput. **213**:153–162,
DOI `10.1016/j.amc.2009.03.005`, eq (1.2), read in batch B01:

> `(k/k*) τ_q  <  τ*_m  <  2 k τ_T / τ_q`

with the statement (printed in the paper) that under (1.2) solutions are stable and generate a
semigroup, and that violating it produces instability (the paper attributes the counterexample to its
ref. [25], which was **not** opened).

Script: `V-B10c_quintanilla_rh.py` (sympy 1.14.0 + numpy 2.4.6). Transcript:
`V-B10c_quintanilla_rh.out.txt` (full run, exit code 0).

## 1. Task

Decide, independently of the paper, whether eq (1.2) is the correct and complete stability condition
for the equation the paper writes, and by numerical root-finding whether the sign of the growth rate
changes exactly at its two edges. If it does not match, the claim was to be downgraded to
SECONDARY-SOURCE with the discrepancy written down.

## 2. Method

1. **Sub-system isolated.** Only the *rigid heat conductor* (no elastic coupling, no source) — the
   thermal sub-system of the TPL model. Nothing here is a statement about the coupled
   thermoelastic system.
2. **Model.** The T2 truncation as printed in the paper: second order in `τ_q`, first order in `τ_T`
   and `τ_m`, once-time-differentiated form,

   `(1 + τ_q ∂_t + ½τ_q² ∂_t²) T̈ = τ*_m ΔṪ + k τ_T ΔT̈ + C ΔT`

   (`C` = coefficient of `ΔT`; the paper's non-dimensionalisation is not reproducible from the
   garbled equation image, so `C` is kept symbolic and three normalisations are tested).
3. **Dispersion.** Plane wave `T ∝ exp(st + iξ·x)`, `Δ → −λ²`, `λ² = |ξ|² > 0`, gives the quartic
   `a₀s⁴ + a₁s³ + a₂s² + a₃s + a₄ = 0` with
   `a₀ = τ_q²/2`, `a₁ = τ_q`, `a₂ = 1 + λ²kτ_T`, `a₃ = λ²τ*_m`, `a₄ = λ²C`.
4. **Exact symbolic Routh–Hurwitz** on that quartic (sympy, rational arithmetic), keeping the
   first-column expressions in closed form.
5. **Numeric root sweep**: `numpy.roots` over a log-spaced `λ²` grid `10⁻⁴ … 10⁶`, reporting
   `max_λ² max Re(s)`; the grid must extend to `10⁶` because near an edge the unstable wave number
   runs to infinity (see §4).

## 3. Result

**The window is confirmed. Both printed bounds are reproduced from Routh–Hurwitz.**

The two non-trivial Routh conditions (all coefficients are already positive for
`τ_q, τ*_m, C, kτ_T > 0`) reduce to a single statement that must hold **for every** `λ² > 0`:

```
[τ*_m − τ_q·C]  +  λ²·[ τ*_m (k τ_T − ½ τ_q τ*_m) ]  >  0        for all λ² > 0
   ⟺      τ*_m > τ_q · C          (lower bound; scales with the ΔT coefficient)
   ⟺      τ*_m ≤ 2 k τ_T / τ_q     (upper bound; INDEPENDENT of the normalisation)
```

* With `C = k/k*`, this is **exactly** eq (1.2): `(k/k*)τ_q < τ*_m < 2kτ_T/τ_q`. ✔
* With `C = k` the lower bound is `τ*_m > τ_q k`; with `C = k*/k` it is `τ*_m > τ_q k*/k`. Only
  `C = k/k*` reproduces the printed form, which is itself a useful check on the reading of the
  printed equation.

Numeric confirmation (transcript, section 2 and 4), `k = 1`, `k* = 0.4` (`C = 2.5`),
`τ_q = 0.05`, `τ_T = 0.03`, predicted window `(0.125, 1.2)`:

| `τ*_m` | predicted | `max Re(s)` over `λ²` | verdict |
|---|---|---|---|
| 0.1125 | outside (low) | `+5.75e-03` | UNSTABLE |
| 0.12512 | inside | `−6.27e-09` | STABLE |
| 0.6625 | inside | `−2.69e-05` | STABLE |
| 1.1988 | inside | `−5.37e-05` | STABLE |
| 1.26 | outside (high) | `+9.99e-01` | UNSTABLE |

Edge scan (`τ*_m/upper = 0.90 … 1.10`, transcript section 3): every point at or below the edge is
stable, every point above it is unstable, with `argmax λ²` moving to the top of the grid — the
instability is a short-wave instability whose threshold wave number `λ²* ~ P/|Q| → ∞` as
`τ*_m → 2kτ_T/τ_q⁺`. **This is why a finite-wavelength grid that stops early misses the violation**;
the first version of this script (grid to `λ² = 400`) reported a false "stable" at
`τ*_m = 1.001 × upper`. Recorded here because it is exactly the kind of numerical artefact that
produces a wrong verdict.

## 4. Evidence / sources

* Quintanilla (2009) eqs (1.1), (1.2), (2.1), (2.2) — read from the PDF text layer in B01
  (`DRV-0183`, `drive_id` `1O9ciqiS6UN5Cufwe9WT74nbiJCOrRSCZ`). The **operator structure** used here
  (second order in `τ_q`, first order in `τ_T`, `τ_m`, fourth order in time) is what the paper's
  abstract and §1 state in words, so it does not depend on the garbled equation image.
* Execution: `V-B10c_quintanilla_rh.out.txt`, 96 lines, reproduced by
  `/tmp/venv/bin/python verification/V-B10c_quintanilla_rh.py` (sympy 1.14.0, numpy 2.4.6).
* Cross-check against own earlier work: `V-B2p_dpl-truncation-order.md` (DPL, `τ_T > τ_q/2`) and
  `V-B8a_tpl_F6_F9_audit.md` (TPJL form). The TPL window is a **different** inequality from the DPL
  one and the two must not be merged.

## 5. Checks done

* Symbolic result obtained twice, for three normalisations of the constant term (`C = k`, `C = k*/k`,
  `C = k/k*`) — the upper bound is invariant, the lower bound scales exactly as the algebra predicts.
* Sign change of `max Re(s)` located at both predicted edges by root-finding, with the edge
  sharpness resolved by extending the `λ²` grid (see the artefact note in §3).
* The claim tested is the paper's own; **no** part of this check depends on the manuscript.

## 6. Confidence

**HIGH** that (a) the rigid-conductor quartic is the one the paper's equations imply, (b) its exact
stability region (for all `λ² > 0`) is `τ_q C < τ*_m ≤ 2kτ_T/τ_q`, and (c) with `C = k/k*` this is
eq (1.2) verbatim.
**MEDIUM** on the identification `C = k/k*`, because the printed equation image is garbled and the
identification is inferred from which normalisation reproduces the printed window. If a reader finds
the paper's own non-dimensionalisation gives a different `C`, then the *upper* bound stands unchanged
and only the lower-bound constant moves.
**NONE / not claimed:** nothing here supports or refutes the paper's instability *counterexample* for
violating parameters beyond the linear dispersion test (its ref. [25] remains unopened), and nothing
here transfers to the coupled thermoelastic system.

## 7. NOT verified / open issues

1. Quintanilla's ref. [25] (source of the "violation ⇒ instability" statement) — unopened;
   SECONDARY-SOURCE for that half of eq (1.2).
2. The paper's exact non-dimensionalisation of `T`, `k`, `k*` — not recoverable from the text layer;
   hence the `C = k/k*` identification above is MEDIUM confidence.
3. Coupled (thermoelastic) TPL system: not analysed. The excursion to a coupled stability statement
   would need a separate analysis.
4. The quartic here is the **rigid** one. The paper's spatial (Saint-Venant) estimates on a cylinder
   are a different problem and were not re-derived.
