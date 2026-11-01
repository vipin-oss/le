#!/usr/bin/env python3
"""Check the Section 5 quasi-electrostatic statement (no propagating EM branch).

Scope: uniform isotropic dielectric closure D = eps E with E = -grad(phi) and
free-charge-free Gauss law div(D) = 0, as displayed in the Section 5 piezoelectric
discussion. Coupled piezoelectric mechanical terms are NOT included here; the
check concerns only the electric-potential branch.
"""
import sympy as sp

x, t = sp.symbols("x t", real=True)
eps, mu, k, omega, A = sp.symbols("epsilon mu k omega A", positive=True)

# Quasi-electrostatic branch: E_x = -d(phi)/dx, D_x = eps E_x, div D = 0.
phi = A * sp.exp(sp.I * (k * x - omega * t))
E_x = -sp.diff(phi, x)
D_x = eps * E_x
gauss_residual = sp.simplify(sp.diff(D_x, x) / phi)
assert sp.simplify(gauss_residual - eps * k**2) == 0
# The residual contains no frequency: no time derivative enters Gauss's law here.
assert not gauss_residual.has(omega)
# For k > 0 (k != 0) there is no root; nontrivial solutions require k = 0.
assert sp.solve(sp.Eq(gauss_residual, 0), k) == []

# Negative control: transverse Maxwell with displacement current (no free charge).
# Faraday: d_x E_y = -d_t B_z ; Ampere-Maxwell: -d_x (B_z/mu) = eps d_t E_y.
Ey = A * sp.exp(sp.I * (k * x - omega * t))
B = sp.symbols("B", positive=True)
Bz = B * sp.exp(sp.I * (k * x - omega * t))
faraday = sp.simplify(sp.diff(Ey, x) + sp.diff(Bz, t))
ampere = sp.simplify(-sp.diff(Bz, x) / mu - eps * sp.diff(Ey, t))
sol = sp.solve([sp.simplify(faraday / sp.exp(sp.I * (k * x - omega * t))),
                sp.simplify(ampere / sp.exp(sp.I * (k * x - omega * t)))], [B, omega], dict=True)
speeds = {sp.simplify(s[omega]) for s in sol if omega in s and s[omega] != 0}
# omega is declared positive, so only the positive-frequency root omega = k/sqrt(mu eps) is returned.
assert speeds == {k / sp.sqrt(mu * eps)}, speeds

print("PASS: quasi-electrostatic Gauss law gives eps k^2 phi = 0 with no frequency dependence")
print("PASS: nontrivial plane-wave potential solutions require k = 0 in this closure")
print("PASS: negative control: displacement current gives omega^2 = k^2/(mu eps), a propagating EM branch")
print("Scope: uniform isotropic dielectric closure only; coupled piezoelectric mechanical terms excluded")
