# CR046: the heavy tail is located, in the book the claim cites

*2026-11-01, step 35. Gorenflo, Kilbas, Mainardi and Rogosin (2014), read on printed pages 25-27, 47, 208
and 219 as page images. `ML_TAIL_READ_2026-11-01.csv` is the row-by-row record;
`check_ml_tail.py` recomputes every number below from scratch.*

---

## What the register said, and what the book says

The register's CR046 note was: *"The Mittag-Leffler provenance is supported, but the specific asymptotic
statement (power-law/heavy tails for alpha < 1) was not located in the front matter read; a page-level check
of the asymptotic chapters is needed."* That check is now done, and the statement is not merely located - it
is printed twice, once for the special function and once for the solution.

**1. The algebra - Proposition 3.6, eq. (3.4.15), p. 26.** For 0 < alpha < 2 and pi*alpha/2 < theta <
min{pi, alpha*pi}:

> E_alpha(z) = - sum_{k=1}^{p} z^(-k)/Gamma(1-alpha k) + O(|z|^(-1-p)),  |z| -> inf,  theta <= |arg z| <= pi.

Because theta < alpha*pi < pi when alpha < 1, the negative real axis is inside that sector, so with
z = -t^alpha:

> E_alpha(-t^alpha) = sum_{k=1}^{p} (-1)^(k+1) / (Gamma(1-alpha k) t^(alpha k)) + O(t^(-alpha(1+p))),

whose first term is **1/(Gamma(1-alpha) t^alpha)**. That is a power law of exponent alpha - a heavy tail -
and the *exponential* term of the companion eq. (3.4.14) is exactly what has disappeared in this sector. The
remainder is not hand-waving either: p. 27 bounds it explicitly (eq. (3.4.25)).

**2. The word "decay" - Proposition 3.23 (Pollard), p. 47.**

> "The Mittag-Leffler function of negative argument E_alpha(-x) is completely monotonic for all 0 <= alpha <= 1."

Completely monotonic means positive and decreasing, with a non-negative spectral measure. A solution built
on E_alpha(-x) can only fall; it cannot oscillate its way out of the tail.

**3. The solution, not just the function - p. 208.** Eq. (8.1.31) prints the same expansion for the
fractional relaxation solution itself, f_alpha(t) = sum_{n=1}^{N} (-1)^(n-1) t^(-n alpha)/Gamma(1-n alpha) +
O(t^(-(N+1) alpha)), and the sentence above it is the claim's own subject:

> "in both cases (a) and (b) ... i.e. for fractional relaxation and fractional oscillation, all the
> fundamental and impulse-response solutions exhibit an *algebraic decay* as t -> inf."

**4. The constants - eq. (8.1.80), p. 219**, for the three solution families: a t^(-alpha)/Gamma(1-alpha),
-a t^(-alpha-1)/Gamma(-alpha) and a t^(1-alpha)/Gamma(2-alpha), followed by the sentence that the solution
shows "a finite number of damped oscillations followed by a monotonic algebraic decay as t -> inf".

---

## The numbers, recomputed

The checker does not trust the book either. It evaluates E_alpha(-x) two ways - a spectral integral and the
defining series - and first validates the fast one against the book's own closed form, eq. (8.1.30),
E_{1/2}(-sqrt t) = e^t erfc(sqrt t): **worst relative error 3.8e-38**. The two evaluators agree to 2.8e-26
where both are usable. Then, against eqs. (3.4.15) and (8.1.31):

| test | result |
|---|---|
| tail constant, x*E_a(-x) -> 1/Gamma(1-a) at t = 1e5 | a=0.3: 1.8e-2 · a=0.5: 5.0e-6 · a=0.7: 2.5e-4 · a=0.9: 5.2e-5 (all inside 3 t^(-a), all improving by the predicted factor) |
| remainder with p = 2 decays like t^(-3a) | measured ratio 8.5 / 123.4 / 503.7 against 10^(3a) = 7.9 / 125.9 / 501.2 for a = 0.3 / 0.7 / 0.9 |
| complete monotonicity on x in [1, 1000] | positive and strictly decreasing for a = 0.25, 0.50, 0.75, 0.90; a = 1 reproduces exp(-x) exactly |
| no exponential cut-off | E_a(-x)/exp(-x) goes 1.6e+01 -> 5.9e+19 (a = 0.5) and 5.1e+00 -> 1.1e+19 (a = 0.9) between x = 5 and x = 50 |

The second row is the sharp one: it tests the *order of the remainder the book prints*, not just "the tail is
small". A wrong exponent in (3.4.15) would miss 10^(3a) by a wide margin; it lands within 7%.

---

## Verdict proposal - and what is not covered

**Proposal: CR046 PARTLY SUPPORTED -> SUPPORTED**, citing Gorenflo et al. (2014), **Prop. 3.6, eq. (3.4.15),
p. 26** for the tail and **Prop. 3.23, p. 47** for the decay, with **eq. (8.1.31), p. 208** as the
solution-level statement. As always, the proposal is not written into the register: the checker re-reads
`claim_register.csv` and asserts CR046 is still PARTLY SUPPORTED there.

Two honest limits:

- **"Heavy tails" is the manuscript's word, not the book's.** The book's phrase is *algebraic decay*
  (pp. 208, 219); "heavy tails" appears on the book's pages only inside a bibliography entry, p. 399.
  Neither word is wrong - they are synonyms here - but if the sentence is to read as a quotation, the
  wording should be "algebraic (power-law) decay" with (8.1.31) beside it. Recommended fix, no more than
  that: cite the equation, keep whichever adjective the author prefers.
- **Luchko 2010, the claim's second bibkey, is not this book.** Nothing here verifies it, and the proposal
  covers the Gorenflo et al. half only. It is a paper, so it stays where papers have been put: at the back.

```bash
python3 check_ml_tail.py    # PASS all checks (pages 25-27, 47, 208, 219; register CR046 untouched)
```
