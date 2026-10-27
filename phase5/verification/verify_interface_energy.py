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

# SUBSTANTIVE FIELD DERIVATION: construct the actual incident, reflected, and
# transmitted harmonic displacement fields, then derive velocity and stress.
# The impedance relation Z=E*k/omega is used only to express the elastic modulus;
# no power-flux weight is assumed.
omega = sp.symbols("omega", positive=True, real=True)
k1, k2, x = sp.symbols("k1 k2 x", positive=True, real=True)
E1 = Z1 * omega / k1
E2 = Z2 * omega / k2
u_inc_hat = Ai * sp.exp(sp.I * k1 * x)
u_ref_hat = Ar * sp.exp(-sp.I * k1 * x)
u_trans_hat = At * sp.exp(sp.I * k2 * x)
v_inc_hat = -sp.I * omega * u_inc_hat
v_ref_hat = -sp.I * omega * u_ref_hat
v_trans_hat = -sp.I * omega * u_trans_hat
sigma_inc_hat = sp.I * k1 * E1 * u_inc_hat
sigma_ref_hat = -sp.I * k1 * E1 * u_ref_hat
sigma_trans_hat = sp.I * k2 * E2 * u_trans_hat

# Derive each time-averaged mechanical flux from -Re(sigma*v*)/2.
J_inc_field = sp.simplify(-sp.Rational(1, 2) * sp.re(sigma_inc_hat * sp.conjugate(v_inc_hat)))
J_ref_field = sp.simplify(-sp.Rational(1, 2) * sp.re(sigma_ref_hat * sp.conjugate(v_ref_hat)))
J_trans_field = sp.simplify(-sp.Rational(1, 2) * sp.re(sigma_trans_hat * sp.conjugate(v_trans_hat)))
assert sp.simplify(J_inc_field - Z1 * omega**2 * Ai**2 / 2) == 0
assert sp.simplify(J_ref_field + Z1 * omega**2 * Ar**2 / 2) == 0
assert sp.simplify(J_trans_field - Z2 * omega**2 * At**2 / 2) == 0

# General complex-amplitude cross term, shown before taking its real part
# (equivalently, before the harmonic time average).
Ai_complex, Ar_complex = sp.symbols("Ai_complex Ar_complex", complex=True)
u_inc_complex = Ai_complex * sp.exp(sp.I * k1 * x)
u_ref_complex = Ar_complex * sp.exp(-sp.I * k1 * x)
v_inc_complex = -sp.I * omega * u_inc_complex
v_ref_complex = -sp.I * omega * u_ref_complex
sigma_inc_complex = sp.I * k1 * E1 * u_inc_complex
sigma_ref_complex = -sp.I * k1 * E1 * u_ref_complex
cross_phasor_general = sp.simplify(
    sigma_inc_complex * sp.conjugate(v_ref_complex)
    + sigma_ref_complex * sp.conjugate(v_inc_complex)
)
cross_general_expected = E1 * k1 * omega * (
    -Ai_complex * sp.conjugate(Ar_complex) * sp.exp(2 * sp.I * k1 * x)
    + Ar_complex * sp.conjugate(Ai_complex) * sp.exp(-2 * sp.I * k1 * x)
)
assert sp.simplify(cross_phasor_general - cross_general_expected) == 0
assert sp.simplify(sp.re(sp.expand_complex(cross_phasor_general))) == 0

# The actual lossless-interface solution has real amplitude ratio Ar/Ai, so
# its pre-average cross term has this explicit nonzero-in-general form.
cross_phasor = sp.simplify(
    sigma_inc_hat * sp.conjugate(v_ref_hat)
    + sigma_ref_hat * sp.conjugate(v_inc_hat)
)
cross_expected = -2 * sp.I * E1 * k1 * omega * Ai * Ar * sp.sin(2 * k1 * x)
assert sp.simplify(cross_phasor - cross_expected) == 0
cross_flux_mean = sp.simplify(-sp.Rational(1, 2) * sp.re(cross_phasor))
assert cross_flux_mean == 0

# The interface power ratios now use the fluxes derived above, not postulated weights.
R_flux = sp.simplify(-J_ref_field / J_inc_field)
T_flux = sp.simplify(J_trans_field / J_inc_field)
assert sp.simplify(R_flux - R) == 0
assert sp.simplify(T_flux - T) == 0

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
figure_paths = (
    ROOT / "figures/source/fig13-interface-reflection.svg",
    ROOT / "master/figures/source/fig13-interface-reflection.svg",
    ROOT / "master/figures/rendered/fig13-interface-reflection.svg",
)
for figure_path in figure_paths:
    figure_text = figure_path.read_text(encoding="utf-8")
    assert "Interface-plane accounting:" in figure_text
    assert "RΣ + TΣ + A_int = 1" in figure_text
    assert "R + T + A_int = 1" not in figure_text
assert r"R_{\Sigma}" in section9 and r"T_{\Sigma}" in section9
assert r"\shortstack{$R_{\Sigma},T_{\Sigma},$\\$A_{\mathrm{int}}$}" in section9
assert "saved audit summary does not specify reference planes" in section9
assert r"J_{\mathrm{inc},n}\equiv P_{i,\Sigma}>0" in section9
assert r"A_{\mathrm{int}}=\mathcal{D}_{\Sigma}/P_{i,\Sigma}" in section9
assert "does not identify" in section9 and "remote-plane incident power" in section9
assert "remote-plane reflectance and transmittance" in section9
assert r"R_{\mathrm{rem}} + T_{\mathrm{rem}}" in section10
assert r"A_{\mathrm{bulk},L}" in section10 and r"A_{\mathrm{bulk},R}" in section10
assert "interface-plane bookkeeping identity" in section10
assert r"R = \frac{J_{\mathrm{inc},n}" not in section9
equation_register = (ROOT / "master/appendices/appA_equation_register.tex").read_text(encoding="utf-8")
for equation_id in ("EQ-10.13", "EQ-10.14", "EQ-10.15", "EQ-10.16"):
    assert equation_id + " &" in equation_register
assert "EQ-10.GEN & Generalized-theory energy fluxes & OPEN" in equation_register
assert "EQ-10.13 & Generalized-theory energy fluxes" not in equation_register

print("PASS: welded 1D interface gives a 2x2 system from two conditions/two amplitudes")
print("PASS: det(M)=-(Z1+Z2); positive impedances give unique amplitudes")
print(f"PASS: r={r}, t={t}; real-impedance power ratios satisfy R+T=1")
print("PASS: stress/velocity fields derive incident, reflected, and transmitted harmonic fluxes")
print(f"PASS: incident/reflected cross term before averaging = {cross_phasor}; its time-mean flux is zero")
print("PASS: remote-plane loss equals bulk-left + interface + bulk-right losses")
print("PASS: local interface-plane ratios R_sigma/T_sigma and remote-plane ratios remain distinct")
print("DEFINITIONAL CHECK: R_sigma + T_sigma + A_sigma is an identity under the stated interface-plane definitions; this is not a field-derived conservation theorem")
print("Scope: 1D welded, lossless, positive-real-impedance example; not a generalized or multidimensional proof")
