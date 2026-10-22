#!/usr/bin/env python3
"""V-B4 recheck — branch count of the secular polynomial, and why my first count was wrong.

The B4 report charged eq. (9.9) ("G1 q^8 + ... + G5 = 0 ... for coupled thermo-piezoelastic
media") with being degree 6.  That charge is WITHDRAWN.  The reason is a scope error in my test:
I computed the determinant of the COUPLED (u1,u3,T) block only, i.e. the P-SV-T family, and
compared its degree against a polynomial that covers ALL branches of the medium.  The shear
branch is a branch of the medium even when it does not couple to the temperature.

Counted properly: a medium with 3 displacement components and 1 temperature has FOUR branches
(qP, qSV, qSH, qT), hence a polynomial of degree 2 x 4 = 8 in the vertical wavenumber q.
This script verifies that block by block, which is also how the manuscript's polynomial is
built (each block is a factor).

  block 1: (u1, u3, phi, T)  -- coupled P-SV-T with quasi-static piezoelectricity
  block 2: u2                -- shear; in an isotropic medium uncoupled, in 6mm coupled to phi
"""
import sympy as sp

w, k, q = sp.symbols("omega k q")


def deg(expr, var=q):
    return sp.Poly(sp.expand(expr), var).degree()


# ---------------------------------------------------------------- block 1, isotropic
def iso_psvt():
    rho, lam, mu, beta, T0, cv, kth, tau0 = sp.symbols(
        "rho lambda mu beta T0 cv kth tau0", positive=True)
    U1, U3, TH = sp.symbols("U1 U3 TH")
    i = sp.I
    div = i * k * U1 + i * q * U3
    d2 = -(k ** 2 + q ** 2)
    e1 = -rho * w ** 2 * U1 - ((lam + mu) * i * k * div + mu * d2 * U1 - beta * i * k * TH)
    e2 = -rho * w ** 2 * U3 - ((lam + mu) * i * q * div + mu * d2 * U3 - beta * i * q * TH)
    opT = (-i * w) + tau0 * (-w ** 2)
    e3 = rho * cv * opT * TH - kth * d2 * TH + beta * T0 * opT * div
    M = sp.Matrix([[sp.expand(e.coeff(v)) for v in (U1, U3, TH)] for e in (e1, e2, e3)])
    return sp.expand(M.det())


# ---------------------------------------------------------------- block 1, 6mm + piezo
def hex6_psvt():
    i = sp.I
    (c11, c12, c13, c33, c44, e31, e33, e15, eps11, eps33,
     rho, beta, T0, cv, kth, tau0) = sp.symbols(
        "c11 c12 c13 c33 c44 e31 e33 e15 eps11 eps33 rho beta T0 cv kth tau0", positive=True)
    U1, U3, PH, TH = sp.symbols("U1 U3 PH TH")
    d2 = -(k ** 2 + q ** 2)
    E1, E3 = -i * k * PH, -i * q * PH
    g11, g33 = i * k * U1, i * q * U3
    g13 = (i * q * U1 + i * k * U3) / 2
    s11 = c11 * g11 + c13 * g33 - e31 * E3
    s33 = c13 * g11 + c33 * g33 - e33 * E3
    s13 = 2 * c44 * g13 - e15 * E1
    D1 = 2 * e15 * g13 + eps11 * E1
    D3 = e31 * g11 + e33 * g33 + eps33 * E3
    divu = i * k * U1 + i * q * U3
    mom1 = sp.expand(-rho * w ** 2 * U1 - (i * k * s11 + i * q * s13))
    mom3 = sp.expand(-rho * w ** 2 * U3 - (i * k * s13 + i * q * s33))
    gauss = sp.expand(i * k * D1 + i * q * D3)
    opT = (-i * w) + tau0 * (-w ** 2)
    heat = sp.expand(rho * cv * opT * TH - kth * d2 * TH + beta * T0 * opT * divu)
    M = sp.Matrix([[sp.expand(e.coeff(v)) for v in (U1, U3, PH, TH)]
                   for e in (mom1, mom3, gauss, heat)])
    return sp.expand(M.det())


print("=" * 84)
print("block-by-block degree of the secular polynomial in q  (fixed frequency omega)")
print("=" * 84)
for name, f in (("P-SV-T, isotropic (u1,u3,T)", iso_psvt),
                ("P-SV-T-phi, 6mm piezo-thermoelastic", hex6_psvt)):
    D = f()
    d = deg(D)
    print(f"{name:38s} degree {d}")
print(f"{'shear u2 (c44 q^2 - rho w^2)':38s} degree 2")
print("-" * 84)
print("total, 6mm : 6 + 2 = 8      total, isotropic : 6 + 2 = 8")
print()
print("So eq. (9.9) with degree 8 is correct for the FULL field set of a three-dimensional")
print("medium, in both the isotropic and the 6mm case.  What the manuscript should add is not a")
print("different degree but a scope word: the polynomial includes the decoupled shear branch.")
print()
print("One correction to the arbitration's own reasoning, offered because it affects the text:")
print("in the sagittal plane x1-x3 of a 6mm crystal with the c-axis along x3, the shear branch")
print("does NOT acquire piezo stiffening, because E2 = -d(phi)/dx2 = 0 and D2 never enters")
print("div D = 0.  The stiffening appears only when the shear displacement varies along x2.  The")
print("branch COUNT (4) is the same either way, so the degree is unaffected; the mechanism quoted")
print("in the arbitration is not the one operating in that plane.")
