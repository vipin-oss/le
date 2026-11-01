#!/usr/bin/env python3
"""Check coefficient/variable mapping of GN-III source equations to Sec. 4.

This verifies an algebraic correspondence only. The primary-source equations
are anchored by OCL-494 and the targeted page-image review documented in
Q3_PRIMARY_SOURCE_CHECKS.md; this script does not verify transcription,
solutions, admissibility, stability, or an energy/flux theorem.
"""

import sympy as sp

lam, mu = sp.symbols("lambda mu")
rho0, rho = sp.symbols("rho_0 rho", positive=True)
E, beta_star, nu = sp.symbols("E beta_star nu")
beta_gn, beta = sp.symbols("beta_GN beta")

# Distinct placeholders make the source-to-manuscript operator/field map explicit.
div_grad_u_s, lap_u_s, grad_theta_s, uddot_u_s = sp.symbols(
    "div_grad_u_source lap_u_source grad_theta_source uddot_u_source"
)
div_grad_u_m, lap_u_m, grad_T_m, uddot_u_m = sp.symbols(
    "div_grad_u_ms lap_u_ms grad_T_ms uddot_u_ms"
)
source_mechanical = (
    (lam + mu) * div_grad_u_s
    + mu * lap_u_s
    - beta_gn * grad_theta_s
    - rho0 * uddot_u_s
)
manuscript_mechanical = (
    (lam + mu) * div_grad_u_m
    + mu * lap_u_m
    - beta * grad_T_m
    - rho * uddot_u_m
)
mechanical_map = {
    beta_gn: E * beta_star / (3 * (1 - 2 * nu)),
    beta: E * beta_star / (3 * (1 - 2 * nu)),
    rho: rho0,
    div_grad_u_m: div_grad_u_s,
    lap_u_m: lap_u_s,
    grad_T_m: grad_theta_s,
    uddot_u_m: uddot_u_s,
}
assert sp.simplify(
    source_mechanical.subs(mechanical_map) - manuscript_mechanical.subs(mechanical_map)
) == 0

# Source Eq. (3.20) with r=0, compared to manuscript Eq. (4.14).
c_source, c_e = sp.symbols("c_source c_e")
theta0, T0 = sp.symbols("theta_0 T_0")
kappa_source, kappa_star_source = sp.symbols("kappa_source kappa_star_source")
kappa, kappa_star = sp.symbols("kappa kappa_star")
theta_ddot, T_ddot = sp.symbols("theta_ddot T_ddot")
div_u_ddot = sp.symbols("div_u_ddot")
lap_theta_dot, lap_theta = sp.symbols("lap_theta_dot lap_theta")
lap_T_dot, lap_T = sp.symbols("lap_T_dot lap_T")
source_heat = (
    rho0 * c_source * theta_ddot
    + beta_gn * theta0 * div_u_ddot
    - kappa_source * lap_theta_dot
    - kappa_star_source * lap_theta
)
manuscript_heat = (
    rho * c_e * T_ddot
    + beta * T0 * div_u_ddot
    - kappa * lap_T_dot
    - kappa_star * lap_T
)
thermal_map = {
    **mechanical_map,
    c_e: c_source,
    T0: theta0,
    kappa: kappa_source,
    kappa_star: kappa_star_source,
    T_ddot: theta_ddot,
    lap_T_dot: lap_theta_dot,
    lap_T: lap_theta,
}
assert sp.simplify(source_heat.subs(thermal_map) - manuscript_heat.subs(thermal_map)) == 0

print("PASS: source Eq. (3.19) maps to manuscript Eq. (4.1) for b=0 and beta=E beta*/[3(1-2 nu)]")
print("PASS: source Eq. (3.20) maps to manuscript Eq. (4.14) for r=0 and the explicit variable/coefficient map")
print("Scope: symbolic coefficient/variable substitution only; no transcription, solution, admissibility, stability, or energy/flux proof")
