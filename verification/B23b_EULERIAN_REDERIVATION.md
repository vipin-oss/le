# B23b — independent re-derivation of the Eulerian energy flux, and what it does to B23 P1-1

Head inspected: `d9bf722`. Script: `verification/B23b_verify_eulerian.py` (sympy only, imports
nothing from `phase5/`), `rc = 0`. Mutation harness:
`verification/B23b_mutation_test.py <phase5-root>`, `rc = 0` (3 killed, 1 deliberate survivor).

## 1. The identity, derived by Reynolds transport, not asserted

Starting from the *material* balances only — mass `rho_dot + div(rho v) = 0`, momentum
`rho Dv_i/Dt = sigma_ij,j + rho f_i`, internal energy
`rho De/Dt = sigma_ij eps_dot_ij - q_j,j + rho r` with `sigma` symmetric — with `E = rho(1/2|v|^2 + e)`:

| step | check | result |
|---|---|---|
| A1 | `rho D(1/2|v|^2+e)/Dt + div(q - sigma·v) - (f·v + rho r)` minus `v·(momentum) + (internal energy)` | **0** |
| A2 | `dE/dt + div(q - sigma·v + E v) - source` minus `material balance + h * mass residual` | **0** |
| A3 | reduced flux `q - sigma·v` alone, minus the exact Eulerian balance | **-div(E v)** |

So the exact fixed-volume flux is

    F_i = q_i - sigma_ij v_j + E v_i,    E = rho(1/2 |v|^2 + e)

and the advective term is not a correction to a convention — it is the difference between a
material-derivative balance and a fixed-volume one.

## 2. A counterexample, so this is not algebra about nothing

A genuine steady solution of all three balances with `rho = 1`, `v = 1` (uniform, continuity
exact), `sigma = 2` (constant, momentum exact with `f = 0`), `e = x^2`, `q = 0`, and the heat
supply `rho r = v e' = 2x` that the internal-energy balance then requires:

* exact Eulerian residual at `x = 2`: **0**
* reduced-flux (`q - sigma·v`) residual at `x = 2`: **-4**
* predicted `-div(E v)` at `x = 2`: **-4**

A finite, easily reproduced failure, not an infinitesimal one. (An earlier draft of my script
used a linear velocity field and a zero heat supply; that combination is *not* a solution of the
internal-energy balance, and the assertion failed honestly. The counterexample above is the
corrected one; the failure is recorded here so the record is auditable.)

## 3. The case that actually matters for this manuscript: cycle means

Section 10 does not use the instantaneous flux; it uses time averages. Two results:

* Lossless elastic wave `u = A cos(kx - omega t)`: `e - e_0` is quadratic in `A`, so
  `<rho (e-e_0) v> = 0` **identically** over a period.
* Adiabatic (isentropic) thermoelastic wave: `s` constant forces
  `e - e_0 = (beta T_0/rho) eps + c_v T` with `T = -(beta T_0/(rho c_v)) eps`, so the linear
  part of `e - e_0` cancels exactly and the mean advective flux is again **0**.
* General (phase-lagged) thermoelastic field: with `T` lagging the strain by `varphi`,
  `<rho (e-e_0) v> = -(A^2 T_0 beta omega/2)(B c_v sin varphi + k)` — **nonzero in general**.

This is exactly the shape of the caveat now printed in Section 10.2: the welded-interface
example is safe because its fields are lossless/adiabatic, and a second-order cycle-averaged
claim in a lossy or generally coupled medium would need the advective mean evaluated. The order
argument alone (`advection = O(eps^2)`) does not remove it, because the retained terms
`-sigma·v` and `q` are *also* `O(eps^2)` after averaging. The manuscript says this in as many
words, which is why I regard the point as closed rather than open.

## 4. Verdict on B23 P1-1 (the "tautological script / missing advective flux" finding)

B23 was written against the pre-remediation head, where `sec03_foundations.tex`
Eqs. (3.28)–(3.30) displayed the flux without `E v_i`. At `d9bf722`:

* Eq. (3.28) is the exact balance with `q_j - sigma_ji v_i + E v_j`, derived from the material
  balances and mass conservation (line 320: "Using mass conservation to convert the material
  derivative to an Eulerian balance");
* Eq. (3.29) restates `F_i = q_i - sigma_ij v_j + E v_i` and the text immediately adds that
  omitting `E v_i` "is not an exact identity";
* Eq. (3.30) integrates it over a *fixed* volume;
* Section 10.2 introduces the reduced `J_i = q_i - sigma_ij v_j` only as a first-order convention
  and states twice that it is not the exact flux, plus the cycle-average caveat quoted above.

`phase5/scripts/verify_classical_flux.py` at the same head, run by me: `rc = 0`. It performs the
A1/A2/A3 chain symbolically and then adds a **negative control** — the short flux leaves exactly
`-div(E v)` behind — so the "tautology" objection no longer sticks. Mutation evidence:

| mutation | outcome |
|---|---|
| drop `E v` from the exact flux | KILLED (`AssertionError`, line 87) |
| flip the sign of `E v` | KILLED (`AssertionError`, line 87) |
| flip the sign of `beta T_0 du/dt` in the Section 4 string assertion | KILLED |
| delete the quadratic-remainder degree assertion | SURVIVED (expected: removing a check cannot fail a script) |

**B23 P1-1 is UPHELD for the head it was written against and FIXED at `d9bf722`.** No open P1.

## 5. Residual risk

* The reduced flux is legitimate only under "first-order wave balance" wording. Any place in the
  manuscript that computes an energy ratio from `J_i` while claiming a second-order total-energy
  statement would inherit the error; Section 10 is explicit about this, so the risk is editorial
  rather than technical.
* `E` uses the total energy density including kinetic energy; if a later section defines `E` as
  internal energy only, the advective term changes. A notation gloss would remove the ambiguity.
