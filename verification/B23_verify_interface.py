#!/usr/bin/env python3
"""B23 independent check of the 1D welded-interface energy partition.

Derived from the printed Section 10 text only (commit 4caa9a8). The point is to
test the two things the manuscript asks a reader to trust:
  (i) the stress/velocity flux really gives R + T = 1 for a welded lossless joint,
  (ii) the incident-reflected cross term is nonzero before time averaging and
      zero after it (the B22 finding that was repaired).
No source script is imported.
"""
from __future__ import annotations

import sympy as sp

x, t, om = sp.symbols("x t omega", real=True, positive=True)
Z1, Z2, k1, k2, Ai, Ar, At = sp.symbols("Z1 Z2 k1 k2 A_i A_r A_t", real=True)
Z1p, Z2p = sp.symbols("Z1 Z2", positive=True)
rho1, rho2, c1, c2 = sp.symbols("rho1 rho2 c1 c2", positive=True)

# Conventions of the manuscript: e^{-i omega t}, v = du/dt, sigma = -i omega Z u
v_i = -sp.I * om * Ai * sp.exp(sp.I * k1 * x)
v_r = -sp.I * om * Ar * sp.exp(-sp.I * k1 * x)
s_i = sp.I * k1 * rho1 * c1**2 * Ai * sp.exp(sp.I * k1 * x)
s_r = -sp.I * k1 * rho1 * c1**2 * Ar * sp.exp(-sp.I * k1 * x)
J = lambda s, v: -sp.Rational(1, 2) * sp.re(s * sp.conjugate(v))

# modal fluxes
Ji = sp.simplify(J(s_i, v_i))
Jr = sp.simplify(J(s_r, v_r))
print("incident flux  <J_i> =", Ji)
print("reflected flux <J_r> =", Jr)
# Sign convention: with sigma = -i omega Z u the backward wave carries a negative
# <J>; the manuscript's ratios use the magnitudes, so compare absolute values.
assert sp.simplify((Ji - Z1 * om**2 * Ai**2 / 2).subs({Z1: rho1 * c1, k1: om / c1})) == 0
assert sp.simplify((-Jr - Z1 * om**2 * Ar**2 / 2).subs({Z1: rho1 * c1, k1: om / c1})) == 0
print("(reflected modal flux is negative under this convention; ratios use magnitudes)")

# cross term before and after averaging
cross_pre = sp.simplify(s_i * sp.conjugate(v_r) + s_r * sp.conjugate(v_i))
cross_post = sp.simplify(J(s_i + s_r, v_i + v_r) - Ji - Jr)
print("cross term (before averaging) =", cross_pre)
print("cross term (time-averaged)    =", cross_post)
assert cross_pre != 0
assert sp.simplify(cross_post) == 0

# continuity of displacement and traction at x = 0
Z = lambda m: rho1 * c1 if m == 1 else rho2 * c2
eq1 = sp.Eq(Ai + Ar, At)
eq2 = sp.Eq(sp.I * k1 * rho1 * c1**2 * (Ai - Ar), sp.I * k2 * rho2 * c2**2 * At)
sol = sp.solve([eq1, eq2], [Ar, At], dict=True)[0]
r = sp.simplify(sol[Ar] / Ai)
tt = sp.simplify(sol[At] / Ai)
print("r =", r)
print("t =", tt)
# with k = omega/c and Z = rho c
r_z = sp.simplify(r.subs({k1: om / c1, k2: om / c2, rho1 * c1: Z1, rho2 * c2: Z2}))
t_z = sp.simplify(tt.subs({k1: om / c1, k2: om / c2, rho1 * c1: Z1, rho2 * c2: Z2}))
print("r(Z) =", r_z, "  t(Z) =", t_z)
assert sp.simplify(r_z - (Z1 - Z2) / (Z1 + Z2)) == 0
assert sp.simplify(t_z - 2 * Z1 / (Z1 + Z2)) == 0

r_pos = r_z.subs({Z1: Z1p, Z2: Z2p})
t_pos = t_z.subs({Z1: Z1p, Z2: Z2p})
R = sp.simplify(r_pos**2)
T = sp.simplify((Z2p / Z1p) * t_pos**2)
print("R =", sp.factor(R), "  T =", sp.factor(T))
assert sp.simplify(sp.together(R + T - 1)) == 0

# wrong weighting is caught
bad = sp.simplify(r_pos**2 + t_pos**2)
print("|r|^2+|t|^2-1 =", sp.simplify(bad - 1), "(nonzero: the Z2/Z1 weight matters)")

# note on the manuscript's own wording: J_inc,n is defined as net incident power
print("interface-plane residual for the welded lossless joint:", sp.simplify(1 - R - T))
print("PASS: 1D welded lossless partition, cross-term behaviour, and weighting all reproduced")
