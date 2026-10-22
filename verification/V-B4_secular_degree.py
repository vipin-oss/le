#!/usr/bin/env python3
"""V-B4 — what degree in q does the coupled thermoelastic secular equation really have?

Manuscript claim (sec09_interfaces.tex:117):  G1 q^8 + G2 q^6 + ... + G5 = 0
    "which is an eighth-order polynomial in q for coupled thermo-piezoelastic media"

Setup: plane wave exp(i(k x1 + q x3 - w t)) in ONE medium; eliminate the amplitudes of
(u1, u3, T) for the 2-D P-SV-T problem and take the determinant.  The degree in q is
2 x (number of spatial branches in that medium).
"""
import sympy as sp

w, k, q = sp.symbols("omega k q", real=False)
lam, mu, rho, beta, T0, cv, kth, tau0, cE, kstar, th0 = sp.symbols(
    "lambda mu rho beta T0 c_v k_th tau0 c_e k_star theta0", positive=True)


def deg(expr, var=q):
    p = sp.Poly(sp.expand(expr), var)
    return p.degree()


def ls_det():
    """Lord-Shulman: momentum + (1+tau0 d/dt) energy equation."""
    i = sp.I
    # displacement amplitudes U1, U3 ; temperature amplitude TH
    U1, U3, TH = sp.symbols("U1 U3 TH")
    div = i * k * U1 + i * q * U3
    eq1 = -rho * w**2 * U1 - ((lam + mu) * i * k * div + mu * (-(k**2 + q**2)) * U1 - beta * i * k * TH)
    eq2 = -rho * w**2 * U3 - ((lam + mu) * i * q * div + mu * (-(k**2 + q**2)) * U3 - beta * i * q * TH)
    # LS energy: rho cv (Tdot + tau0 Tddot) = kth lap T - beta T0 (d/dt + tau0 d2/dt2) div u
    opT = (-i * w) + tau0 * (-w**2)
    eq3 = rho * cv * opT * TH - kth * (-(k**2 + q**2)) * TH + beta * T0 * opT * div
    M = sp.Matrix([[sp.expand(eq1.coeff(v)) for v in (U1, U3, TH)],
                   [sp.expand(eq2.coeff(v)) for v in (U1, U3, TH)],
                   [sp.expand(eq3.coeff(v)) for v in (U1, U3, TH)]])
    return sp.expand(M.det()), "LS (tau0 heat flux, 3 modes expected)"


def gn3_det():
    """Green-Naghdi III: kth lap Tdot + k* lap T - rho ce Tddot = beta T0 div uddot."""
    i = sp.I
    U1, U3, TH = sp.symbols("U1 U3 TH")
    div = i * k * U1 + i * q * U3
    eq1 = -rho * w**2 * U1 - ((lam + mu) * i * k * div + mu * (-(k**2 + q**2)) * U1 - beta * i * k * TH)
    eq2 = -rho * w**2 * U3 - ((lam + mu) * i * q * div + mu * (-(k**2 + q**2)) * U3 - beta * i * q * TH)
    lap = -(k**2 + q**2)
    eq3 = kth * (-i * w) * lap * TH + kstar * lap * TH - rho * cE * (-w**2) * TH \
          - beta * T0 * (-w**2) * div
    M = sp.Matrix([[sp.expand(eq1.coeff(v)) for v in (U1, U3, TH)],
                   [sp.expand(eq2.coeff(v)) for v in (U1, U3, TH)],
                   [sp.expand(eq3.coeff(v)) for v in (U1, U3, TH)]])
    return sp.expand(M.det()), "GN-III (2 thermal symbols, 3 modes expected)"


def biot_det():
    """Classical Biot: rho cv Tdot = kth lap T - beta T0 div udot."""
    i = sp.I
    U1, U3, TH = sp.symbols("U1 U3 TH")
    div = i * k * U1 + i * q * U3
    eq1 = -rho * w**2 * U1 - ((lam + mu) * i * k * div + mu * (-(k**2 + q**2)) * U1 - beta * i * k * TH)
    eq2 = -rho * w**2 * U3 - ((lam + mu) * i * q * div + mu * (-(k**2 + q**2)) * U3 - beta * i * q * TH)
    eq3 = rho * cv * (-i * w) * TH - kth * (-(k**2 + q**2)) * TH + beta * T0 * (-i * w) * div
    M = sp.Matrix([[sp.expand(eq1.coeff(v)) for v in (U1, U3, TH)],
                   [sp.expand(eq2.coeff(v)) for v in (U1, U3, TH)],
                   [sp.expand(eq3.coeff(v)) for v in (U1, U3, TH)]])
    return sp.expand(M.det()), "Biot (Fourier, 3 modes expected)"


print("=" * 78)
print("V-B4  degree of the 2-D (P-SV-T) secular determinant in the vertical wavenumber q")
print("=" * 78)
for fn in (biot_det, ls_det, gn3_det):
    D, label = fn()
    d = deg(D)
    print(f"{label:52s} degree in q = {d}   (in q^2: {d//2})")
print()
print("Manuscript eq. (9.9) asserts degree 8 (quartic in q^2) 'for coupled thermo-piezoelastic")
print("media'.  Degree 8 requires FOUR spatial branches per medium.  Every single-temperature")
print("theory in Sections 4 and 6 -- Biot, LS, GL, GN-II, GN-III, DPL, MDD kernel models --")
print("gives THREE (qP, qSV, qT), because the quasi-static electric potential is slaved to")
print("(u, T) by div D = 0 and contributes no branch of its own.")
print()
print("Corrected statement: the secular equation is a CUBIC in q^2 (degree 6 in q) for the")
print("three-mode single-temperature theories; it becomes quartic in q^2 only for a theory")
print("with a second thermal branch (e.g. a fourth-order-in-space heat operator, or a")
print("carrier/plasma mode in a semiconductor), none of which is the 'thermo-piezoelastic'")
print("case named in the caption.")
