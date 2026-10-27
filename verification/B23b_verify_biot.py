#!/usr/bin/env python3
"""B23b — independent check of manuscript Eq. (4.2) against Biot (1956) pp. 241–242.

Nothing from phase5/verification/verify_classical_thermoelastic.py is imported.

Printed source facts (Biot, J. Appl. Phys. 27:240, PDF pp. 3–4 = printed 241–242):
  (2.2)  sigma_xx = 2 mu e_xx + lambda e - beta theta   (and the y,z,xy components)
  (2.14) s = (c/T) theta + beta e
  (2.15) h = c theta + T beta e           [heat absorbed per unit volume]
  (3.3)  dh/dt = k div grad theta = k lap(theta)
  (3.4)  k lap(theta) = c dtheta/dt + T beta de/dt
"""
from __future__ import annotations

import sympy as sp

rho, cv, T0, beta, k, c_vol = sp.symbols("rho c_v T0 beta k c", positive=True)
theta, thdot, edot, lap, r, T_abs, sdot, h, hdot = sp.symbols(
    "theta theta_dot e_dot lap r Theta s_dot h h_dot", real=True
)

print("1. Biot (3.4) -> manuscript Eq. (4.2)")
biot34 = sp.Eq(c_vol * thdot + T_abs * beta * edot, k * lap)
# maps used by the manuscript: c  = rho*c_v (heat capacity per unit volume),
# T_abs = T0, e = u_{i,i}
ms = sp.Eq(rho * cv * thdot, k * lap - beta * T0 * edot)
subs = {c_vol: rho * cv, T_abs: T0}
resid = sp.simplify((biot34.lhs - biot34.rhs).subs(subs) - (ms.lhs - ms.rhs))
print("   residual after the map c=rho c_v, T_abs=T0, e=u_i,i :", resid)
assert resid == 0
print("   => Eq. (4.2) is exactly Biot (3.4) with r=0.           CONFIRMED")

print("\n2. Biot (2.2) stress sign")
lam, mu, exx, e, th = sp.symbols("lambda mu e_xx e theta")
sigma_biot = 2 * mu * exx + lam * e - beta * th
sigma_ms = lam * e + 2 * mu * exx - beta * th
print("   sigma_biot - sigma_ms =", sp.simplify(sigma_biot - sigma_ms))
assert sp.simplify(sigma_biot - sigma_ms) == 0
print("   => the negative temperature-increment term is the printed one.  CONFIRMED")

print("\n3. Biot heat form h = c*theta + T*beta*e  (2.15) equals T*s to first order")
h_biot = c_vol * th + T_abs * beta * e
# rho*s = c*theta/T_abs + beta*e  =>  T_abs*rho*s = c*theta + T_abs*beta*e
rho_s = c_vol * th / T_abs + beta * e
print("   T_abs*rho*s - h =", sp.simplify(T_abs * rho_s - h_biot))
assert sp.simplify(T_abs * rho_s - h_biot) == 0
print("   => the entropy route used by the checklist script and Biot's heat route agree. OK")

print("\n4. The script's route: rho*Theta*s_dot = k*lap + rho*r with s from Eq. (3.22)")
beta_s, rho_sym = sp.symbols("beta_s rho_sym", positive=True)
s_dot = beta_s / rho_sym * edot + cv / T0 * thdot
full = sp.expand(rho_sym * (T0 + theta) * s_dot - k * lap - rho_sym * r)
linear = beta_s * T0 * edot + rho_sym * cv * thdot - k * lap - rho_sym * r
remainder = beta_s * theta * edot + rho_sym * cv * theta * thdot / T0
print("   full - linear - remainder =", sp.simplify(full - linear - remainder))
assert sp.simplify(full - linear - remainder) == 0
eps = sp.symbols("eps", positive=True)
T1, Td1, Ed1 = sp.symbols("T1 Tdot1 epsdot1", real=True)
scaled = remainder.subs({theta: eps * T1, thdot: eps * Td1, edot: eps * Ed1})
print("   degree in eps of the remainder:", sp.Poly(sp.expand(scaled), eps).degree())
assert sp.Poly(sp.expand(scaled), eps).degree() == 2
assert sp.expand(scaled).coeff(eps, 1) == 0
print("   => the discarded terms are quadratic.                       OK")

print("\n5. Negative controls")
src_free = (linear - rho_sym * r).subs(r, 0)
print("   beta=0 :", sp.simplify(src_free.subs(beta_s, 0) - (rho_sym * cv * thdot - k * lap)))
print("   k=0    :", sp.simplify(src_free.subs(k, 0) - (rho_sym * cv * thdot + beta_s * T0 * edot)))
assert sp.simplify(src_free.subs(beta_s, 0) - (rho_sym * cv * thdot - k * lap)) == 0
assert sp.simplify(src_free.subs(k, 0) - (rho_sym * cv * thdot + beta_s * T0 * edot)) == 0

print("\n6. Dimensional consistency of beta*T0*epsdot against rho*c_v*Tdot")
M, L, T, K = sp.symbols("M L T K", positive=True)
dim = {
    "rho": M * L**-3, "cv": L**2 * T**-2 * K**-1, "T0": K,
    "beta": M * L**-1 * T**-2 * K**-1, "epsdot": T**-1, "k": M * L * T**-3 * K**-1,
}
lhs = dim["rho"] * dim["cv"] * dim["T0"] / T
rhs1 = dim["beta"] * dim["T0"] * dim["epsdot"]
rhs2 = dim["k"] * dim["T0"] / L**2
print("   rho*cv*Tdot :", sp.simplify(lhs))
print("   beta*T0*epsdot :", sp.simplify(rhs1))
print("   k*lap(T) :", sp.simplify(rhs2))
assert sp.simplify(lhs - rhs1) == 0 and sp.simplify(lhs - rhs2) == 0

print("\nRESULT: OCL-513's anchor (Biot p. 242 Eqs. (3.3)-(3.4)) supports Eq. (4.2);")
print("        the linearization/order claim in the checklist script is reproduced")
print("        independently, and the negative controls behave as stated.")
