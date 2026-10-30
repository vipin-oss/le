# Paper B (Neha): sign and unit audit

Same method as Paper A: every pair of terms that shares a constant is checked for reciprocity, and every
term is checked for dimensions.

## 1. Phonon-phason coupling

    sigma_ij = C_ijkl eps_kl + R_ijkl w_kl - e E_k - beta_ij theta
    H_ij     = R_klij eps_kl + K_ijkl w_kl - beta^w_ij theta

Reciprocity: the energy density contains `R_ijkl eps_ij w_kl`. For the energy to be a function of state and
not of the path, the coupling seen from either side must be the same, that is `R_ijkl = R_klij`. The two
equations satisfy this by construction: one carries `R_ijkl` acting on `w`, the other `R_klij` acting on
`eps`. A scholar transcribing a table must not symmetrise `R` by hand; it is already symmetric in its two
index pairs.

Dimensions: `R eps` and `R w` are both Pa, since `w_kl = dw_k/dx_l` is dimensionless. `K w` is Pa.
`H_zj,j` is Pa/m = N/m3, matching `rho_p w_ddot` (kg/m3)(m/s2) = N/m3 and `gamma w_dot`
(kg m^-3 s^-1)(m/s) = kg m^-2 s^-2 = N/m3.

Signs: both couplings enter with plus signs. A minus in front of `R w` would mean a positive phason strain
relieves the phonon stress, which is not what the modulus tables mean. Keep plus.

## 2. Phason friction: sign of the dissipation

Multiply the phason balance by `w_dot` and integrate over the volume. The friction term gives
`-gamma w_dot^2`, so the rate of mechanical energy loss is `gamma w_dot^2` per unit volume. This is
non-negative only for `gamma > 0`. The model must therefore state `gamma` positive, and every sweep must
stop at zero from above. A negative `gamma` would be a pump. `rho_p` is positive by definition.

The two limits: `gamma = 0` gives a wave equation with speed of order `sqrt(K/rho_p)` in the pure phason
case; `rho_p = 0` gives `gamma w_dot = H_zj,j`, a diffusion equation with diffusivity of order `K/gamma`.
Both are the limits quoted by Agiasofitou and Lazar (2014), and the crossover sits near `gamma/rho_p` up to
the modulus.

## 3. Thermo-phason pair

Bracket of the heat equation:

    (1 + tau_q d/dt)[ rho c_p dtheta/dt + T0 beta_ij d eps_ij/dt + T0 beta^w_ij d w_ij/dt + T0 p_i dE_i/dt ]

The reciprocal partner of `H_ij = ... - beta^w_ij theta` is `+T0 beta^w_ij d w_ij/dt`, on the same reasoning
as the classical thermoelastic pair: the bracket carries the negative of the source, and the source is
`-T0 beta^w d w/dt`. Same constant, factor T0, opposite sign. Dimensions: K (Pa/K)(1/s) = W/m3.

Status: the thermo-phason constant has no published source that I found. It is labelled a proposed
extension in the plan and in the source log, and the paper must say so where it is used. Reciprocity and
dimensions can be checked even when the citation is missing, and they are checked above.

## 4. Piezoelectric pair

`-e E` in the stress and `+e eps` in `D_i`: same tensor, opposite signs, energy `-eE eps`. Dimensions: `eE`
= Pa, `e eps` = C/m2.

## 5. Pyroelectric pair

`+p theta` in `D_i` and `+T0 p dE/dt` in the bracket. Same constant, factor T0, bracket sign as in section 3.
Dimensions C/m2 and W/m3.

## 6. MGT operator

`(1 + tau_q d/dt)` applied term by term to the bracket. No reciprocity between entries is broken, because it
acts on a sum. Dimensions: dimensionless on W/m3.

## 7. Unit audit, every term

Phason balance: N/m3 on both sides. Heat equation: W/m3 for each of the four bracket entries and for the
conduction term. Momentum with the size effect: `(1 - l_nl^2 lap) rho u_ddot` is (1)(kg/m3)(m/s2) = N/m3, and
`sigma_ij,j` is N/m3; the operator is dimensionless because `l^2 lap` is a length squared times an inverse
length squared.

## 8. One residual worry

The phason inertia and the phason friction are both taken isotropic in the plane, while the literature
carries a friction tensor. The audit above holds for the scalar case only. If the scholar moves to the
tensor case, the dissipation becomes `-D_ij w_dot_i w_dot_j`, non-negative only if the tensor is positive
semi-definite, and that condition must be stated.
