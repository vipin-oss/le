# CR127: the entropy does depend on the heat flux - printed, not inferred

*2026-11-01, step 36. Muller and Ruggeri (1998), read on printed p. 24 (and p. 5 for the tour
d'horizon). `RET_ENTROPY_READ_2026-11-01.csv` is the row record; `check_ret_entropy.py` re-tests the
structure claimed below.*

---

## The claim that could never be judged

CR127 said: *"In extended irreversible thermodynamics (Jou et al. 2010; Muller and Ruggeri 1998; Muller
1967) the entropy depends also on the heat flux q_i, which must enter the state space."* The register's note
was blunt: **"not read; the source is not in the library, so no verdict is possible"**. The book is now on
the shelf, and the claim is on one page - §3.5, *Entropy and Entropy Flux in Grad's 13-Moment Theory*.

**The equations.** Eq. (3.27) writes the Grad distribution as the Maxwellian times a bracket carrying a
traceless stress and a heat flux - the thirteen moments *are* the state. Eq. (3.28) defines the entropy and
its flux as functionals of that distribution. Eq. (3.29) then prints the entropy itself:

> s = (k/m) ln(T^(3/2)/rho) + varsigma - t_<ij> t_<ij>/(4 rho p^2 T) - q_i q_i/(5 p^2 T)

and eq. (3.30) the entropy flux, which is **not** q_i/T:

> phi_i = q_i/T + (2/(5 p^2 T)) t_<ij> q_j

**The sentence.** Immediately after, p. 24:

> "Thus indeed, the specific entropy of the kinetic theory in the Grad approximation depends on t_<ij> and
> q_i. Also the entropy flux is not simply equal to q_i/T but it contains a term proportional to t_<ij>q_j.
> **These facts confirm the conjectures of extended TIP.**"

That is the claim, in the cited authors' own words, with the mechanism attached: because the entropy is a
functional of f and f depends on q, the dependence of s on q is a *consequence* in this reading, not a
postulate. The coefficient list of eq. (3.31) then names a, b, c, K and L, so the manuscript could cite an
equation instead of a general "depends on the fluxes".

---

## What was verified, and what was deliberately not

**Verified - the structure of (3.29).** The checker evaluates the printed bracket of (3.27) against a
Gaussian equilibrium and tests the three properties that (3.29) asserts:

| property | result |
|---|---|
| the correction is negative for every non-zero (t, q) | yes, for the tested traceless stress and flux |
| it is **even in q** - reversing the heat flux changes nothing | |s(q) - s(-q)| <= 1e-30 relative |
| there is **no t-q cross term** | the joint correction equals the sum of the two separate ones to 1e-25 |

Those three are what the claim actually needs: an entropy that cannot be built without q, and that cannot
be built with q to the first power either - the dependence is on q_i q_i.

**Not verified - the coefficients 1/4 and 1/5.** A naive Gaussian evaluation of (3.27) does **not** reproduce
both coefficients with a single normalisation, because the page does not fix the normalisation of t_<ij> and
q_i in the book's moment convention. Rather than fit the normalisation until the numbers agree - which would
be a manufactured result - the coefficients are **quoted as printed and not claimed as reproduced**, and the
readout says so in words. This is recorded as its own row in the CSV (row 7), not hidden.

---

## Verdict proposal

**Proposal: CR127 SOURCE NOT AVAILABLE -> SUPPORTED**, citing Muller and Ruggeri (1998), **§3.5, eq. (3.29)
and the sentence on p. 24** (with eqs. (3.27), (3.28), (3.30), (3.31) as support). The register is not
touched; the checker re-reads it and asserts CR127 is still SOURCE NOT AVAILABLE there.

One scope note: the claim names **three** sources - Jou et al. (2010), Muller and Ruggeri (1998) and Muller
(1967). This job verifies the second. Jou et al. (4th ed., 2010) is also on the shelf now and has not been
read yet; Muller (1967) is a paper and is not held. So the proposal covers one of three citations, and says
so.

```bash
python3 check_ret_entropy.py    # PASS all checks (p. 24, structure confirmed, register CR127 untouched)
```
