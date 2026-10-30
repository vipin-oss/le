# Paper A (Sumit): sign and unit audit

Requested after the v4 review. Every cross-coupling pair is checked twice: once for reciprocity (does the
same constant appear on both sides, with a sign that conserves energy?) and once for dimensions.

## 1. The thermodiffusion coefficient, from the flux

Take the electron particle flux (number per area per second) for an n-type material, charge of the electron
`-q`:

    j_i = -n b_n E_i + n b_n S_n theta_,i                              (1)

First term: drift, velocity `-b_n E_i` for an electron, so the particle flux is `n(-b_n E_i)`. Correct sign.
Second term: thermodiffusion; with `S_n < 0` it points along `-grad(theta)`, that is from hot to cold, which
is what electrons do. Correct sign.

Charge conservation with no recombination, `dn/dt + div j = 0`, linearised about `n0`:

    d(Dn)/dt = -div j = D_n lap(Dn) + b_n n0 div E - b_n S_n lap(theta) + ...

Compare with the model equation, `d(Dn)/dt = D_n lap(Dn) + b_n n0 div E + beta_th lap(theta)`:

    beta_th = -b_n n0 S_n ,        [beta_th] = m^-1 s^-1 K^-1                  (2)

With `S_n < 0` for electrons, `beta_th > 0`. Consequence: at a hot spot theta has a maximum, so
`lap(theta) < 0`, so the thermodiffusion term is negative, so the excess density falls there and the carriers
gather where it is cold. That is the sentence the text now carries. The earlier version had
`beta_th = +b_n n0 S_n`, which with `S_n < 0` made carriers pile up at the hot spot and contradicted its own
sentence. Fixed.

## 2. The Peltier term, from the energy balance of the carrier stream

Electric current is `J_i = -q j_i`. The heat carried by that current is `Pi_th J_i` (Peltier coefficient in
volts, so volts times amperes per area is watts per area). What the lattice receives per unit volume is the
convergence of that flux with a minus sign, because the carriers lose what the lattice gains:

    source = -div(Pi_th J_i) = -Pi_th div J_i   (Pi_th uniform)
           = +q Pi_th div j_i
           = -q Pi_th d(Dn)/dt                                                (3)

Sign test: carriers accumulate, `d(Dn)/dt > 0`, the lattice must heat. With `Pi_th < 0` for electrons, (3)
is positive. Correct.

## 3. Placing the term in the heat equation

The heat equation is written as

    (1 + tau_q d/dt) [ rho c_p dtheta/dt + T0 beta_ij d eps_ij/dt + T0 p_i dE_i/dt + X ] = k_th lap(theta)

The bracket holds the negative of each heat source, because the classical thermoelastic entry is
`+T0 beta_ij d eps/dt` while its source is `-T0 beta_ij d eps/dt` (compression heats, expansion cools). So
`X = -(Peltier source) = +q Pi_th d(Dn)/dt`. This is the sign now in (A6). With `Pi_th < 0` and
accumulation, the bracket entry is negative, which raises the right-hand side, that is, heats the lattice.

The earlier draft had `X = -q Pi_th d(Dn)/dt`, which is the source itself put into the bracket without the
extra minus. Two sign errors cancelled in my head and left one in the file. The reviewer's version is right
and the equations now agree with it.

## 4. Onsager ratio

    Pi_th = T0 S_n ,  beta_th = -b_n n0 S_n  =>  Pi_th / beta_th = -T0 / (b_n n0)          (4)

The magnitude is Kelvin's relation in the form every thermoelectric text uses; the minus sign follows from
beta_th carrying a minus for electrons. It is stated with the sign in the paper so that a reader cannot take
the two coefficients for independent fitting parameters.

## 5. Other cross-coupling pairs

| pair | appears as | reciprocity test | dimensions |
|---|---|---|---|
| piezoelectric | `-e E` in sigma; `+e eps` in D | same tensor, opposite sign, energy `-eE eps` | `eE` = Pa; `e eps` = C/m2 |
| pyroelectric / electrocaloric | `+p theta` in D; `+T0 p dE/dt` in the bracket | same `p`, factor T0, bracket sign as in section 3 | C/m2 and W/m3 |
| thermal stress | `-beta theta` in sigma; `+T0 beta d eps/dt` in the bracket | same `beta`, factor T0, opposite sign as required | Pa and W/m3 |
| MGT operator | `(1 + tau_q d/dt)` on the whole bracket | applies to every entry, so no reciprocity is broken between them | dimensionless on W/m3 |
| carrier drift | `b_n n0 div E` in (A5) | with Gauss, `div D = -q Dn`, closes on itself, no new constant | m^-3 s^-1 |
| recombination option | `-Dn/tau_R` in (A5); `+E_g Dn/tau_R` in the bracket | a pair only; energy per event `E_g`, sign positive in the bracket because heat is released | W/m3 |

## 6. Unit audit, every term

(A5): `d(Dn)/dt` m^-3 s^-1; `D_n lap` m^2/s x m^-3/m^2 = m^-3 s^-1; `b_n n0 div E` (m2/Vs)(m^-3)(V/m2) =
m^-3 s^-1; `v_d dDn/dx` (m/s)(m^-3/m) = m^-3 s^-1; `beta_th lap(theta)` (m^-1 s^-1 K^-1)(K/m2) = m^-3 s^-1;
`Dn/tau_R` m^-3 s^-1.

(A6): `rho c_p dtheta/dt` W/m3; `T0 beta d eps/dt` W/m3; `T0 p dE/dt` W/m3; `q Pi_th d(Dn)/dt`
(C)(V)(m^-3 s^-1) = W/m3; `E_g Dn/tau_R` W/m3; `k_th lap(theta)` W/m3.

All six terms of each equation agree. The tables in the model document and in the plan carry the same result.
