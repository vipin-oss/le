#!/usr/bin/env python3
"""Check exact reductions of the explicitly displayed constitutive equations.

These are algebraic checks of the equations as written in Sections 4, 6, and 7;
they do not verify source transcription, solution convergence, thermodynamic
admissibility, or equivalence of complete initial-boundary-value problems.
"""
from __future__ import annotations

from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]

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
# Positive DPL -> LS check: remove the temperature-gradient lag but retain
# the heat-flux relaxation with the LS time constant.
dpl_to_ls = sp.simplify(dpl.subs({tau_T: 0, tau_q: tau0}) - ls)
assert dpl_to_ls == 0

# Negative check: sending tau_q to zero does not give LS for independent,
# nonzero tau0, tau_T, and qdot. It also does not remove the gradient-lag term.
dpl_tau_q_zero_minus_ls = sp.expand(dpl.subs(tau_q, 0) - ls)
assert dpl_tau_q_zero_minus_ls == -tau0 * qdot + k * tau_T * grad_T_dot
assert dpl_tau_q_zero_minus_ls != 0

# Removing both DPL lags gives Fourier, a distinct reduction from LS.
assert sp.simplify(dpl.subs({tau_T: 0, tau_q: 0}) - fourier) == 0
assert sp.simplify(tpl.subs(k_star, 0) - dpl) == 0

# Keep the active comparison table synchronized with the checked reduction.
comparison = (ROOT / "master/sections/sec12_comparative.tex").read_text(encoding="utf-8")
assert r"$\tau_T \to 0$, with $\tau_q=\tau_0$" in comparison
assert r"$\tau_q \to 0$" not in comparison
assert "Model-dependent" in comparison
assert "do not classify the critical case" in comparison
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

# For the displayed scalar Caputo PDE, integer-order endpoints have the
# differential form of the heat equation (alpha=1) and wave equation (alpha=2).
x_cap = sp.symbols("x_cap", real=True)
T_cap = sp.Function("T_cap")(x_cap, t_cap)
a1, a2 = sp.symbols("a1 a2", positive=True)
lap_T_cap = sp.diff(T_cap, x_cap, 2)
caputo_d1, caputo_d2 = sp.symbols("caputo_d1 caputo_d2")
alpha1_residual = caputo_d1 - a1 * lap_T_cap
alpha2_residual = caputo_d2 - a2 * lap_T_cap
heat_endpoint = sp.diff(T_cap, t_cap) - a1 * lap_T_cap
wave_endpoint = sp.diff(T_cap, t_cap, 2) - a2 * lap_T_cap
assert sp.simplify(alpha1_residual.subs(caputo_d1, sp.diff(T_cap, t_cap)) - heat_endpoint) == 0
assert sp.simplify(alpha2_residual.subs(caputo_d2, sp.diff(T_cap, t_cap, 2)) - wave_endpoint) == 0
print("PASS: scalar Caputo endpoints have heat-equation and wave-equation differential forms")

# The local limit is checked only for the displayed Helmholtz differential form
# and the displayed one-dimensional dispersion relation.
xi, wave_number, c0 = sp.symbols("xi wave_number c0", nonnegative=True)
sigma, sigma_local = sp.symbols("sigma sigma_local")
helmholtz_residual = sigma - xi**2 * sp.Symbol("lap_sigma") - sigma_local
assert sp.simplify(helmholtz_residual.subs(xi, 0) - (sigma - sigma_local)) == 0
c_nonlocal = c0 / sp.sqrt(1 + xi**2 * wave_number**2)
assert sp.simplify(c_nonlocal.subs(xi, 0) - c0) == 0
print("PASS: displayed Helmholtz differential law and 1D dispersion expression have their xi=0 local limits")

# The reduction map must cover the requested families while explicitly leaving
# GL and GN-I equation-level reductions open. These text checks do not establish
# source transcription or any solution-level limiting result.
reduction_map = (ROOT / "master/tables/source/T2_reduction_map.tex").read_text(encoding="utf-8")
for family in (
    "Classical coupled", "LS", "GL", "GN-I", "GN-II / GN-III", "DPL",
    "TPL", "MGT", "Fractional scalar", "Spatially nonlocal", "MDD",
):
    assert family in reduction_map, f"reduction map is missing {family}"
assert "No equation-level reduction asserted" in reduction_map
assert r"\alpha=1" in reduction_map and r"\alpha=2" in reduction_map
assert r"\tau_0=0" in reduction_map and r"\xi=0" in reduction_map
assert "Derivative-level compatibility only" in reduction_map
assert "no shared stability or thermodynamic condition follows" in reduction_map

# Confirm that the shared scaffold is explicitly a local Cauchy balance pair
# plus non-universal constitutive placeholders.
section4 = (ROOT / "master/sections/sec04_thermoelastic.tex").read_text(encoding="utf-8")
assert r"\label{eq:4.21}" in section4 and r"\label{eq:4.22}" in section4
assert "not common constitutive functions" in section4
assert "do not cover higher-gradient, micropolar, or nonlocal boundary-power terms" in section4
print("PASS: reduction map covers LS, GL, GN-I/II/III, DPL, TPL, MGT, fractional, nonlocal, and MDD with explicit open rows")
print("PASS: shared balance scaffold is scoped to local Cauchy continua and non-universal closures")

print("Scope: equation-level substitutions only; no claim of source transcription, convergence, stability, or family-wide equivalence")
