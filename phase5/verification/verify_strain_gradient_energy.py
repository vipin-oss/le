#!/usr/bin/env python3
"""Verify the scoped strain-gradient law in Sec. 7.2 from a chosen energy.

The vector form represents six independent small-strain components and three
spatial directions. The algebra is variational and model-specific; it is not a
source-transcription, calibration, or family-wide gradient-theory proof.
"""
import sympy as sp

x, y, z, t = sp.symbols("x y z t", real=True)
coords = (x, y, z)
ell = sp.symbols("ell", positive=True)

# Symmetric stiffness matrix in the six-component representation of C_ijkl.
C_symbols = {}
for i in range(6):
    for j in range(i, 6):
        C_symbols[i, j] = sp.symbols(f"C{i}{j}")
C = sp.Matrix(6, 6, lambda i, j: C_symbols[min(i, j), max(i, j)])
eps = sp.Matrix([sp.Function(f"eps{i}")(x, y, z) for i in range(6)])
energy = sp.Rational(1, 2) * (eps.T * C * eps)[0]
for coord in coords:
    eps_grad = eps.applyfunc(lambda f: sp.diff(f, coord))
    energy += sp.Rational(1, 2) * ell**2 * (eps_grad.T * C * eps_grad)[0]

# Euler-Lagrange bulk stress vector and higher-order microstress.
stress = []
for a in range(6):
    component = sp.diff(energy, eps[a])
    for coord in coords:
        component -= sp.diff(sp.diff(energy, sp.diff(eps[a], coord)), coord)
    stress.append(sp.simplify(component))
for a in range(6):
    for coord in coords:
        microstress = sp.diff(energy, sp.diff(eps[a], coord))
        expected_microstress = ell**2 * sum(C[a, b] * sp.diff(eps[b], coord) for b in range(6))
        assert sp.simplify(microstress - expected_microstress) == 0
expected = C * sp.Matrix([
    eps[a] - ell**2 * sum(sp.diff(eps[a], coord, 2) for coord in coords)
    for a in range(6)
])
assert all(sp.simplify(stress[a] - expected[a]) == 0 for a in range(6))

# Local limit and a negative control against the wrong gradient sign in a 1D bar.
C1, rho = sp.symbols("C1 rho", positive=True)
x1 = sp.symbols("x1", real=True)
e = sp.Function("e")(x1)
local_energy = sp.Rational(1, 2) * C1 * e**2 + sp.Rational(1, 2) * C1 * ell**2 * sp.diff(e, x1)**2
sigma = sp.diff(local_energy, e) - sp.diff(sp.diff(local_energy, sp.diff(e, x1)), x1)
expected_1d = C1 * e - C1 * ell**2 * sp.diff(e, x1, 2)
assert sp.simplify(sigma - expected_1d) == 0
assert sp.simplify(expected_1d.subs(ell, 0) - C1 * e) == 0
wrong_sign = C1 * e + C1 * ell**2 * sp.diff(e, x1, 2)
wrong_residual = sp.simplify((wrong_sign - expected_1d).subs(e, x1**2))
assert sp.simplify(wrong_residual - 4 * C1 * ell**2) == 0

# For u=A exp(i(kx-omega t)), verify the one-dimensional dispersion relation.
A, k, omega = sp.symbols("A k omega", real=True, nonzero=True)
u = A * sp.exp(sp.I * (k * x1 - omega * t))
strain = sp.diff(u, x1)
sigma_wave = C1 * strain - C1 * ell**2 * sp.diff(strain, x1, 2)
residual = sp.simplify(rho * sp.diff(u, t, 2) - sp.diff(sigma_wave, x1))
coefficient = sp.simplify(residual / u)
expected_dispersion_residual = rho * omega**2 - C1 * k**2 * (1 + ell**2 * k**2)
assert sp.simplify(coefficient + expected_dispersion_residual) == 0
omega_squared = sp.solve(expected_dispersion_residual, omega**2)[0]
assert sp.simplify(omega_squared - C1 * k**2 * (1 + ell**2 * k**2) / rho) == 0
phase_speed_squared = sp.simplify(omega_squared / k**2)
assert sp.simplify(phase_speed_squared - C1 * (1 + ell**2 * k**2) / rho) == 0
assert sp.simplify(omega_squared.subs(ell, 0) - C1 * k**2 / rho) == 0

print("PASS: 3D six-component Euler-Lagrange derivative gives the scoped bulk stress in Eq. 7.3")
print("PASS: ell=0 recovers local Hooke elasticity; wrong-sign gradient fails the negative control")
print("PASS: 1D bar dispersion is omega^2=(C1/rho) k^2 (1+ell^2 k^2)")
print("Scope: one quadratic gradient energy with constant symmetric positive-definite C; higher-order boundary data are separate")
