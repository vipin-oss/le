# B23b — OCL-513 check (manuscript Eq. (4.2) vs Biot 1956)

Head inspected: `d9bf722` (working tree `/home/user/b23b_src`, extracted read-only).
Claim row: `OPEN_CLAIMS_LEDGER.csv` → `OCL-513`, resolved_by "Biot (1956), printed p. 242,
Eqs. (3.3)–(3.4); manuscript Eq. (3.22); `phase5/verification/verify_classical_thermoelastic.py`".

## 1. What the manuscript says

`phase5/master/sections/sec04_thermoelastic.tex`, Eq. (4.2):

    rho c_v \dot{T} = k \nabla^2 T - beta T_0 \dot{u}_{i,i}

Scope words present in the same section: linear isotropic thermoelasticity, constant
coefficients, uniform reference temperature, Fourier heat flux, zero body force and zero
heat supply, first-order perturbations. Entropy relation used upstream is Eq. (3.22):

    s = s_0 + (beta/rho) eps_kk + (c_v/T_0) T

## 2. What the printed source says

Biot, *J. Appl. Phys.* **27** (1956) 240, file `1.1722351.pdf`, 15 pp. Page footers checked,
so printed page numbers are not inferred from PDF offsets.

| printed page | equation | content actually seen |
|---|---|---|
| 241 | (2.2) | `sigma_xx = 2 mu e_xx + lambda e - beta theta` (negative temperature-increment term) |
| 241 | (2.12)–(2.14) | `ds = c dT/T + beta de`; `s = (c theta/T) + beta e`; `c` is defined on the same page as *the specific heat of the unit volume* |
| 241 | (2.15) | `h = c theta + T beta e`, i.e. `T s` equals the heat absorbed per unit volume |
| 242 | (3.3) | `dh/dt = k div grad theta = k lap(theta)` |
| 242 | (3.4) | `k lap(theta) = c dtheta/dt + T beta de/dt` |

## 3. Comparison

Rearranging (3.4): `c theta_dot = k lap(theta) - T beta e_dot`. With the identifications

* `theta` → `T` (Biot's `theta` is the increment above the reference temperature `T`; p. 241),
* `c` → `rho c_v` (Biot's `c` is per unit volume; `c_v` per unit mass),
* `e` → `u_{i,i}`,

this is Eq. (4.2) exactly, with the source term absent. So **the anchor supports the
equation: CONFIRMED**, and the only freedom is notation (symbol and per-volume vs
per-mass normalisation of entropy and heat capacity), not physics or sign.

Two consistency remarks that matter for the ledger's "*resolved_by* (3.3)–(3.4)" wording:

1. Eq. (4.2) does **not** need (3.3); (3.3) is the intermediate step (`dh/dt = k∇²θ`) that
   produces (3.4) once (2.15) is inserted. Citing (3.3)–(3.4) together is accurate.
2. The entropy route in Eq. (3.22) and Biot's heat route (2.14)–(2.15) agree identically at
   first order (`T_0 rho s = c theta + T_0 beta e`), so the manuscript is not mixing two
   incompatible conventions.

## 4. Independent symbolic check

`verification/B23b_verify_biot.py` (imports nothing from phase5; `sympy` only), run:

    $ python3 verification/B23b_verify_biot.py    # rc = 0

1. residual of `(Biot 3.4) − (Eq. 4.2)` under the map `c = rho c_v`, `T_abs = T_0`, `e = u_{i,i}` → **0**;
2. Biot (2.2) minus a `+beta T` stress convention → **0** (the printed sign is the negative one);
3. `T_abs*rho*s − h` → **0**, so the two routes coincide;
4. expanding `rho Theta s_dot = k lap + rho r` with `Theta = T_0 + theta` and `s` from (3.22):
   `full − linear − remainder == 0` and `deg_eps(remainder) == 2` with vanishing `eps^1`
   coefficient → the discarded terms really are second order;
5. negative controls: `beta = 0` gives pure Fourier diffusion; `k = 0` retains the coupling term;
6. SI dimensions: `rho c_v Tdot`, `beta T_0 epsdot` and `k lap(T)` are all `M L^-1 T^-3`.

## 5. Audit of the ledger's other cited support: `verify_classical_thermoelastic.py`

Read in full, and executed at `d9bf722`:

    $ python3 phase5/verification/verify_classical_thermoelastic.py    # rc = 0

* The symbolic part is substantive: it reproduces steps 3–6 above independently of my script.
* Its **last block is not science**: it asserts two LaTeX *substrings* of
  `sec04_thermoelastic.tex`. Mutation-wise this block is load-bearing only as a
  transcription guard, and it works — flipping the sign inside that string kills the script
  (`verification/B23b_mutation_test.py`, mutant 3: KILLED).
* Deleting the quadratic-remainder assertion makes the script still pass (mutant 4:
  SURVIVED). That is expected — removing a check cannot fail a script — and is reported only
  so the surviving-mutant count is not mistaken for a defect.
* Consequence for the ledger: the row's evidence mode is fair, but the script alone cannot
  substitute for the page check. Here the page check was done (Section 2), so the combination
  is adequate.

## 6. Residual risk

* Biot's `c` per unit volume is mapped to `rho c_v`; if the manuscript ever writes `c` for
  the *per-mass* specific heat in one place and `rho c_v` in another, a dimensional
  inconsistency would follow. A one-line notation gloss in Section 3 would close this.
* Eq. (4.2) assumes constant coefficients and no source; the ledger already forbids extending
  it to anisotropic / generalized / source-bearing models. Nothing in Section 2 of this note
  weakens that restriction.

**Verdict: OCL-513 CONFIRMED at the printed anchor; no change requested.**
