#!/usr/bin/env python3
"""B23b — independent re-derivation of the Eulerian total-energy flux.

Checks the repaired Section 3/10 statements at head d9bf722 without importing
phase5/scripts/verify_classical_flux.py.

 (A) Derive the fixed-volume (Eulerian) balance from the *material* balances by an
     explicit Reynolds-transport argument, keeping every term.
 (B) Exhibit a genuine steady solution of the three balances and show numerically
     that the reduced flux q - sigma.v alone leaves a nonzero residual equal to
     -div(E v): the advective term is not optional.
 (C) Check the two claims Section 10 now makes about the reduced flux:
       - a lossless adiabatic (isentropic) wave has zero mean advective flux, so the
         welded-interface example is internally consistent;
       - a non-adiabatic / thermodynamically general harmonic field has a nonzero
         mean advective flux, so the caveat "evaluate it or justify it" is needed
         and is not decorative.
"""
from __future__ import annotations

import sympy as sp

# ---------------------------------------------------------------- (A) identity
x, y, z, t = sp.symbols("x y z t", real=True)
X = (x, y, z)


def F(name):
    return sp.Function(name)(x, y, z, t)


def V(name):
    return [sp.Function(f"{name}{i}")(x, y, z, t) for i in (1, 2, 3)]


def M(name):
    return sp.Matrix(3, 3, lambda i, j: sp.Function(f"{name}{i+1}{j+1}")(x, y, z, t))


rho, e, r, h = F("rho"), F("e"), F("r"), F("h")
v, q, f = V("v"), V("q"), V("f")
sig = M("s")
sig = sig.subs({sig[j, i]: sig[i, j] for i in range(3) for j in range(i)})
D = lambda g, k: sp.diff(g, X[k])
div = lambda w: sum(D(w[k], k) for k in range(3))
grad_dot = lambda w, s: sum(w[k] * D(s, k) for k in range(3))
eps_dot = sp.Matrix(3, 3, lambda i, j: sp.Rational(1, 2) * (D(v[i], j) + D(v[j], i)))

mass = sp.diff(rho, t) + div([rho * v[k] for k in range(3)])
mom = [rho * (sp.diff(v[i], t) + grad_dot(v, v[i])) - sum(D(sig[i, j], j) for j in range(3)) - rho * f[i]
       for i in range(3)]
ener = rho * (sp.diff(e, t) + grad_dot(v, e)) - sum(sig[i, j] * eps_dot[i, j] for i in range(3) for j in range(3)) \
    + div(q) - rho * r

kin_spec = sp.Rational(1, 2) * sum(v[i] ** 2 for i in range(3))
spec_total = kin_spec + e
E = rho * spec_total
mech_flux = [sum(sig[j, i] * v[i] for i in range(3)) for j in range(3)]
src = sum(rho * f[i] * v[i] for i in range(3)) + rho * r

material = rho * (sp.diff(spec_total, t) + grad_dot(v, spec_total)) + div([q[j] - mech_flux[j] for j in range(3)]) - src
combined = sum(v[i] * mom[i] for i in range(3)) + ener
print("(A1) material total-energy residual - [v.(momentum) + internal energy] =",
      sp.simplify(material - combined))
assert sp.simplify(material - combined) == 0

exact_flux = [q[j] - mech_flux[j] + E * v[j] for j in range(3)]
euler = sp.diff(E, t) + div(exact_flux) - src
print("(A2) Eulerian(F_i = q_i - s_ij v_j + E v_i) - material - h*mass =",
      sp.simplify(euler - material - spec_total * mass))
assert sp.simplify(euler - material - spec_total * mass) == 0
reduced = sp.diff(E, t) + div([q[j] - mech_flux[j] for j in range(3)]) - src
r_red = sp.simplify(reduced - euler)
print("(A3) reduced(q - s.v only) - exact =", sp.simplify(r_red + div([E * v[j] for j in range(3)])) , " (= -div(E v))")
assert sp.simplify(r_red + div([E * v[j] for j in range(3)])) == 0

# ------------------------------------------------- (B) concrete steady solution
# Uniform steady flow in 1-D: rho = 1, v = const keeps continuity exact; a constant
# stress keeps momentum exact; e = x^2 is carried by the flow, with q = 0 and the
# heat supply chosen so that the internal-energy balance holds identically.
x1 = sp.symbols("x1", positive=True)
rho_c, v0 = sp.Integer(1), sp.Integer(1)
sig_c = sp.Integer(2)
e_c = x1**2
r_c = sp.simplify(v0 * sp.diff(e_c, x1) - sig_c * sp.diff(v0, x1))   # rho v e' = sigma v' - q' + rho r
E_c = rho_c * (sp.Rational(1, 2) * v0**2 + e_c)
flux_exact = -sig_c * v0 + E_c * v0                                  # q = 0
res_exact = sp.simplify(sp.diff(flux_exact, x1) - rho_c * r_c)
res_reduced = sp.simplify(sp.diff(-sig_c * v0, x1) - rho_c * r_c)
val = 2
print("\n(B) steady solution rho=1, v=1, sigma=2, e=x^2, q=0, r = v e':")
print("    exact   Eulerian residual at x=2 :", res_exact.subs(x1, val))
print("    reduced residual (no advection)   :", res_reduced.subs(x1, val))
print("    predicted -div(E v)              :", sp.simplify(-sp.diff(E_c * v0, x1).subs(x1, val)))
assert res_exact == 0
assert sp.simplify(res_reduced) != 0
assert sp.simplify(res_reduced.subs(x1, val)) == sp.simplify(-sp.diff(E_c * v0, x1).subs(x1, val))

# ------------------------------------- (C) mean advective flux for harmonic waves
om, kk = sp.symbols("omega k", positive=True)
tt = sp.symbols("t", real=True)
A, phi = sp.symbols("A varphi", real=True)
u = A * sp.cos(kk * x1 - om * tt)                       # displacement
v = sp.diff(u, tt)
eps = sp.diff(u, x1)
print("\n(C) harmonic wave: u = A cos(k x - w t); time mean of <rho (e-e0) v>")
# lossless elastic case: e - e0 = 1/2 sigma*eps / rho  (quadratic)  -> cubic in A
e_el = sp.Rational(1, 2) * sig_c * eps / rho_c          # placeholder replaced below
E_elas = sp.symbols("E_mod", positive=True)
e_el = sp.Rational(1, 2) * E_elas * eps**2 / rho_c
adv_el = sp.simplify(sp.integrate((rho_c * e_el) * v, (tt, 0, 2 * sp.pi / om)) * om / (2 * sp.pi))
print("    purely elastic (e quadratic): mean =", sp.simplify(adv_el))
assert sp.simplify(adv_el) == 0

# thermoelastic adiabatic wave: s = const => e - e0 = (beta T0/rho) eps + c_v T with
# T = -(beta T0/(rho c_v)) eps, so the linear part of e cancels exactly.
beta_t, T0_t, cv_t = sp.symbols("beta_T T0_t c_v_t", positive=True)
T_ad = -beta_t * T0_t / (rho_c * cv_t) * eps
e_lin_ad = beta_t * T0_t / rho_c * eps + cv_t * T_ad
print("    adiabatic (isentropic) linear part of e-e0 :", sp.simplify(e_lin_ad))
assert sp.simplify(e_lin_ad) == 0
adv_ad = sp.simplify(sp.integrate((rho_c * e_lin_ad) * v, (tt, 0, 2 * sp.pi / om)) * om / (2 * sp.pi))
print("    adiabatic mean advective flux =", adv_ad)

# non-adiabatic: allow a phase lag between temperature and strain
T_gen = beta_t * T0_t / rho_c * sp.symbols("B", real=True) * A * sp.cos(kk * x1 - om * tt + phi)
e_lin_gen = beta_t * T0_t / rho_c * eps + cv_t * T_gen
adv_gen = sp.simplify(sp.integrate((rho_c * e_lin_gen) * v, (tt, 0, 2 * sp.pi / om)) * om / (2 * sp.pi))
adv_gen = sp.simplify(adv_gen)
print("    general (phase-lagged) mean advective flux =", adv_gen)
assert sp.simplify(adv_gen.subs(phi, 0)) != 0

print("\nRESULT: the exact fixed-volume flux is q - sigma.v + E v (A), the reduced flux")
print("        fails by exactly -div(E v) on a genuine steady solution (B), and Section")
print("        10's caveat is correct: the mean advective flux vanishes for the lossless")
print("        adiabatic/elastic examples but not for a general thermoelastic field (C).")
