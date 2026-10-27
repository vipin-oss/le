#!/usr/bin/env python3
"""Check exact reductions of the explicitly displayed constitutive equations.

These are algebraic checks of the equations as written in Sections 4, 6, and 7;
they do not verify source transcription, solution convergence, thermodynamic
admissibility, or equivalence of complete initial-boundary-value problems.
"""
from __future__ import annotations

import sympy as sp

# Abstract heat-flux law components corresponding to the displayed LS law
# (Sec. 4, Eq. 4.4), first-order DPL/TPL forms (Eq. 4.16 and the stated TPL
# expansion), and the MGT heat-flux law (Eq. 4.18). Each residual is written
# with all terms on the left, so equality is tested by subtracting residuals.
tau0, tau_q, tau_T, tau_v, tau_m = sp.symbols(
    "tau0 tau_q tau_T tau_v tau_m", real=True
)
k, k_star = sp.symbols("k k_star", real=True)
q, qdot, grad_T, grad_T_dot, grad_v, grad_v_dot = sp.symbols(
    "q qdot grad_T grad_T_dot grad_v grad_v_dot"
)

fourier = q + k * grad_T
ls = q + tau0 * qdot + k * grad_T
dpl = q + tau_q * qdot + k * (grad_T + tau_T * grad_T_dot)
tpl = dpl + k_star * (grad_v + tau_v * grad_v_dot)
mgt = q + tau_m * qdot + k * grad_T + k_star * grad_v

assert sp.simplify(ls.subs(tau0, 0) - fourier) == 0
assert sp.simplify(dpl.subs({tau_T: 0, tau_q: tau0}) - ls) == 0
assert sp.simplify(dpl.subs({tau_T: 0, tau_q: 0}) - fourier) == 0
assert sp.simplify(tpl.subs(k_star, 0) - dpl) == 0
assert sp.simplify(mgt.subs({tau_m: 0, k_star: 0}) - fourier) == 0
print("PASS: LS -> Fourier; first-order DPL -> LS/Fourier; TPL -> DPL; displayed MGT heat-flux law -> Fourier")

# GN-III with kappa=0 is the time derivative of the stated, time-integrated
# GN-II equation when T = alpha_GN_dot. This is derivative-level
# compatibility only; a solution reduction additionally needs an integration
# constant and compatible initial data.
x, t = sp.symbols("x t", real=True)
alpha_gn = sp.Function("alpha_gn")(x, t)
u = sp.Function("u")(x, t)
T = sp.Function("T")(x, t)
rho_ce, beta_T0, kappa, kappa_star = sp.symbols(
    "rho_ce beta_T0 kappa kappa_star", real=True
)

gn2_residual = (
    kappa_star * sp.diff(alpha_gn, x, 2)
    - rho_ce * sp.diff(alpha_gn, t, 2)
    - beta_T0 * sp.diff(u, x, t)
)
gn3_residual = (
    rho_ce * sp.diff(T, t, 2)
    + beta_T0 * sp.diff(u, x, t, 2)
    - kappa * sp.diff(T, x, 2, t)
    - kappa_star * sp.diff(T, x, 2)
)
gn3_kappa_zero = gn3_residual.subs(kappa, 0).subs(T, sp.diff(alpha_gn, t))
assert sp.simplify(gn3_kappa_zero + sp.diff(gn2_residual, t)) == 0
print("PASS: GN-III with kappa=0 equals the time derivative of displayed GN-II under T=alpha_GN_dot")

# Caputo derivatives of integer-order monomials reduce to ordinary derivatives
# at integer orders for the selected smooth test functions.
t_cap = sp.symbols("t_cap", positive=True)
for degree in range(2, 7):
    for order in (1, 2):
        caputo_monomial = (
            sp.gamma(degree + 1)
            / sp.gamma(degree + 1 - order)
            * t_cap ** (degree - order)
        )
        assert sp.simplify(
            caputo_monomial - sp.diff(t_cap**degree, t_cap, order)
        ) == 0
print("PASS: Caputo monomial identities at orders 1 and 2 for degrees 2 through 6")

# The local limit is checked only for the displayed Helmholtz differential form
# and the displayed one-dimensional dispersion relation.
xi, wave_number, c0 = sp.symbols("xi wave_number c0", nonnegative=True)
sigma, sigma_local = sp.symbols("sigma sigma_local")
helmholtz_residual = sigma - xi**2 * sp.Symbol("lap_sigma") - sigma_local
assert sp.simplify(helmholtz_residual.subs(xi, 0) - (sigma - sigma_local)) == 0
c_nonlocal = c0 / sp.sqrt(1 + xi**2 * wave_number**2)
assert sp.simplify(c_nonlocal.subs(xi, 0) - c0) == 0
print("PASS: displayed Helmholtz differential law and 1D dispersion expression have their xi=0 local limits")

print("Scope: equation-level substitutions only; no claim of source transcription, convergence, stability, or family-wide equivalence")
