#!/usr/bin/env python3
"""Derive the 1D nonlocal-bar dispersion relation from Eq. 7.2."""
import sympy as sp

x, t = sp.symbols("x t", real=True)
rho, C, xi, k, omega, A = sp.symbols("rho C xi k omega A", positive=True)
u = A * sp.exp(sp.I * (k * x - omega * t))
strain = sp.diff(u, x)
# (1 - xi^2 d_xx) sigma = C epsilon for the displayed Helmholtz form.
sigma = C * strain / (1 + xi**2 * k**2)
momentum_residual = sp.simplify(rho * sp.diff(u, t, 2) - sp.diff(sigma, x))
dispersion_residual = rho * omega**2 - C * k**2 / (1 + xi**2 * k**2)
assert sp.simplify(momentum_residual / u + dispersion_residual) == 0
omega2 = sp.solve(dispersion_residual, omega**2)[0]
phase_speed_squared = sp.simplify(omega2 / k**2)
assert sp.simplify(phase_speed_squared - C / (rho * (1 + xi**2 * k**2))) == 0

# Local limit, finite-wavenumber negative control, and derived high-wavenumber behavior.
assert sp.simplify(phase_speed_squared.subs(xi, 0) - C / rho) == 0
assert sp.simplify(phase_speed_squared - C / rho) != 0
c0 = sp.sqrt(C / rho)
omega_expr = c0 * k / sp.sqrt(1 + xi**2 * k**2)
phase_speed = omega_expr / k
group_velocity = sp.diff(omega_expr, k)
assert sp.simplify(phase_speed**2 - phase_speed_squared) == 0
assert sp.simplify(group_velocity - c0 / (1 + xi**2 * k**2)**sp.Rational(3, 2)) == 0
assert sp.limit(phase_speed, k, sp.oo) == 0
assert sp.limit(omega_expr, k, sp.oo) == c0 / xi
assert sp.limit(group_velocity, k, sp.oo) == 0

print("PASS: the Helmholtz nonlocal bar gives omega^2=(C/rho) k^2/(1+xi^2 k^2)")
print("PASS: phase speed is c0/sqrt(1+xi^2 k^2), frequency saturates at c0/xi, and group speed tends to zero")
print("Scope: one-dimensional homogeneous bar and the displayed Helmholtz operator only")
