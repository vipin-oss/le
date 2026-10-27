#!/usr/bin/env python3
"""Verify a one-dimensional lossless interface and control-volume bookkeeping.

Scope: normal-incidence longitudinal waves in two real, positive-impedance
half-spaces, a welded interface, and passive, source-free, steady time-averaged
energy balances.
This does not prove a generalized-multiphysics flux or a multidimensional
interface theorem.
"""
from __future__ import annotations

from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]

# Unknown reflected/transmitted displacement amplitudes; incident amplitude is known.
Z1, Z2, Ai = sp.symbols("Z1 Z2 Ai", positive=True, real=True)
M = sp.Matrix([[1, -1], [-Z1, -Z2]])
b = sp.Matrix([-Ai, -Z1 * Ai])
assert M.shape == (2, 2)  # two scalar continuity conditions, two unknown amplitudes
assert sp.simplify(M.det() + Z1 + Z2) == 0
assert sp.simplify(M.det()) != 0  # Z1,Z2 are assumed positive
Ar, At = M.inv() * b
r = sp.factor(Ar / Ai)
t = sp.factor(At / Ai)
assert sp.simplify(r - (Z1 - Z2) / (Z1 + Z2)) == 0
assert sp.simplify(t - 2 * Z1 / (Z1 + Z2)) == 0

# For real positive impedances, the power ratios are |r|^2 and (Z2/Z1)|t|^2.
R = sp.simplify(r**2)
T = sp.simplify((Z2 / Z1) * t**2)
assert sp.simplify(R + T - 1) == 0

# For real positive impedances, the harmonic mechanical fluxes are +/- Z*omega^2*|A|^2/2.
# The same-medium incident/reflected cross term is purely imaginary in -Re(sigma*v*)/2.
omega = sp.symbols("omega", positive=True, real=True)
Ai2, Ar2, At2 = sp.symbols("Ai2 Ar2 At2", positive=True, real=True)
J_inc = Z1 * omega**2 * Ai2 / 2
J_ref = -Z1 * omega**2 * Ar2 / 2
J_trans = Z2 * omega**2 * At2 / 2
R_flux = sp.simplify((-J_ref / J_inc).subs(Ar2, r**2 * Ai2))
T_flux = sp.simplify((J_trans / J_inc).subs(At2, t**2 * Ai2))
assert sp.simplify(R_flux - R) == 0
assert sp.simplify(T_flux - T) == 0
z = sp.symbols("z", complex=True)
assert sp.simplify(sp.re(z - sp.conjugate(z))) == 0

# Steady control-volume balances: bulk losses lie between remote planes and
# interface faces; the local residual uses only the two interface-face fluxes.
I, R_far, T_far, J_left, J_right = sp.symbols(
    "I R_far T_far J_left J_right", real=True
)
A_interface = J_left - J_right
# Balance of the two bulk regions identifies their dissipations.
D_left = I - R_far - J_left
D_right = J_right - T_far
closure = sp.simplify(R_far + T_far + A_interface + D_left + D_right - I)
assert closure == 0
R_remote = R_far / I
T_remote = T_far / I
A_bulk_left = D_left / I
A_int = A_interface / I
A_bulk_right = D_right / I
remote_balance = sp.simplify(
    R_remote + T_remote + A_bulk_left + A_int + A_bulk_right - 1
)
assert remote_balance == 0
# The remote-plane residual already contains both bulk and interface losses.
A_remote = I - R_far - T_far
assert sp.simplify(A_remote - (D_left + A_interface + D_right)) == 0
# Adding bulk losses to that remote residual increases the balance by exactly them again.
double_count_excess = sp.simplify(R_far + T_far + A_remote + D_left + D_right - I)
assert sp.simplify(double_count_excess - D_left - D_right) == 0

# The total-field interface identity is algebraic under its definitions.
J_inc, J1_total, J2_total = sp.symbols("J_inc J1_total J2_total", nonzero=True, real=True)
R_sigma = (J_inc - J1_total) / J_inc
T_sigma = J2_total / J_inc
A_sigma = (J1_total - J2_total) / J_inc
assert sp.simplify(R_sigma + T_sigma + A_sigma - 1) == 0

# Keep the manuscript's plane labels and remote-plane balance synchronized.
section9 = (ROOT / "master/sections/sec09_interfaces.tex").read_text(encoding="utf-8")
section10 = (ROOT / "master/sections/sec10_energy.tex").read_text(encoding="utf-8")
assert r"R_{\Sigma}" in section9 and r"T_{\Sigma}" in section9
assert "remote-plane reflectance and transmittance" in section9
assert r"R_{\mathrm{rem}} + T_{\mathrm{rem}}" in section10
assert r"A_{\mathrm{bulk},L}" in section10 and r"A_{\mathrm{bulk},R}" in section10
assert "interface-plane bookkeeping identity" in section10
assert r"R = \frac{J_{\mathrm{inc},n}" not in section9

print("PASS: welded 1D interface gives a 2x2 system from two conditions/two amplitudes")
print("PASS: det(M)=-(Z1+Z2); positive impedances give unique amplitudes")
print(f"PASS: r={r}, t={t}; real-impedance power ratios satisfy R+T=1")
print("PASS: same-medium harmonic incident/reflected cross term has zero mean normal flux")
print("PASS: remote-plane loss equals bulk-left + interface + bulk-right losses")
print("PASS: local interface-plane ratios R_sigma/T_sigma and remote-plane ratios remain distinct")
print("PASS: R_sigma + T_sigma + A_sigma is an identity under the stated interface-plane definitions")
print("Scope: 1D welded, lossless, positive-real-impedance example; not a generalized or multidimensional proof")
