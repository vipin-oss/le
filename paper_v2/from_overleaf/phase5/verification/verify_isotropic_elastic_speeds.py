#!/usr/bin/env python3
"""Verify uncoupled isotropic elastic reference speeds from Sec. 4 Eq. 4.1.

The test sets beta=0 and uses plane waves in a homogeneous isotropic solid.
It does not give the coupled thermoelastic longitudinal dispersion relation.
"""
import sympy as sp

rho, lam, mu, beta, k, omega, A, T_hat = sp.symbols(
    "rho lambda mu beta k omega A T_hat", positive=True
)
I = sp.I
# Longitudinal displacement parallel to the wave vector (x direction).
x, t = sp.symbols("x t", real=True)
uL = A * sp.exp(I * (k * x - omega * t))
div_uL = sp.diff(uL, x)
navier_L = rho * sp.diff(uL, t, 2) - (lam + 2 * mu) * sp.diff(div_uL, x)
assert sp.simplify(navier_L / uL + rho * omega**2 - (lam + 2 * mu) * k**2) == 0
cp2 = sp.solve(rho * omega**2 - (lam + 2 * mu) * k**2, omega**2)[0] / k**2
assert sp.simplify(cp2 - (lam + 2 * mu) / rho) == 0

# Wave vector along x and displacement along y: divergence is zero, leaving
# only the shear term in the vector Navier equation.
y, z = sp.symbols("y z", real=True)
uS = A * sp.exp(I * (k * x - omega * t))
uS_vec = sp.Matrix([0, uS, 0])
div_uS = sp.diff(uS_vec[0], x) + sp.diff(uS_vec[1], y) + sp.diff(uS_vec[2], z)
assert sp.simplify(div_uS) == 0
lap_uS_y = sp.diff(uS_vec[1], x, 2) + sp.diff(uS_vec[1], y, 2) + sp.diff(uS_vec[1], z, 2)
navier_S = rho * sp.diff(uS, t, 2) - mu * lap_uS_y
assert sp.simplify(navier_S / uS + rho * omega**2 - mu * k**2) == 0
cs2 = sp.solve(rho * omega**2 - mu * k**2, omega**2)[0] / k**2
assert sp.simplify(cs2 - mu / rho) == 0

# Negative control: nonzero thermoelastic coupling leaves the temperature-gradient term.
thermal_longitudinal_residual = sp.simplify(navier_L + beta * sp.diff(T_hat * sp.exp(I * (k * x - omega * t)), x))
assert sp.simplify(thermal_longitudinal_residual.subs(beta, 0) - navier_L) == 0
assert sp.simplify(thermal_longitudinal_residual.subs(beta, 1) - navier_L) != 0

print("PASS: beta=0 longitudinal reference speed is sqrt((lambda+2 mu)/rho)")
print("PASS: beta=0 shear speed is sqrt(mu/rho)")
print("PASS: nonzero beta retains thermal coupling, so these are not coupled thermoelastic mode speeds")
