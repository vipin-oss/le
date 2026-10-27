#!/usr/bin/env python3
"""B23 independent check of the classical power/energy identity, in 3-D.

What is tested (from the printed Section 3/8 balances, no import from
phase5/scripts/verify_classical_flux.py):

 (i)   symmetric Cauchy stress  =>  sigma_ij v_i,j = sigma_ij eps_dot_ij.
 (ii)  with mass, momentum (material form) and internal-energy balances imposed,
       the conserved form is
           d/dt[rho(1/2|v|^2+e)] + div(q - sigma.v + rho(1/2|v|^2+e)v)
               = rho f.v + rho r .
 (iii) the shorter statement "E_dot + div(q - sigma v) = rho f.v + rho r"
       (the wording asserted by the Arena script) is only valid for a material
       volume / moving control volume: a fixed control volume needs the
       advective flux div[rho(1/2|v|^2+e)v], which the script never forms.
"""
from __future__ import annotations

import sympy as sp

c = sp.symbols("x y z", real=True)
t = sp.symbols("t", real=True)


def s(name):
    return sp.Function(name)(*c, t)


def vec(name):
    return [sp.Function(f"{name}{i}")(*c, t) for i in (1, 2, 3)]


def mat(name):
    return sp.Matrix(3, 3, lambda i, j: sp.Function(f"{name}{i+1}{j+1}")(*c, t))


v, q, f = vec("v"), vec("q"), vec("f")
sig = mat("s")
rho, e, r = s("rho"), s("e"), s("r")
D = lambda g, k: sp.diff(g, c[k])
divw = lambda w: sum(D(w[k], k) for k in range(3))

sym = {sig[i, j]: sig[j, i] for i in range(3) for j in range(3) if j < i}
sig = sig.subs(sym)
eps_dot = sp.Matrix(3, 3, lambda i, j: sp.Rational(1, 2) * (D(v[i], j) + D(v[j], i)))
divsig = [sum(D(sig[i, j], j) for j in range(3)) for i in range(3)]

lhs = sum(sig[i, j] * D(v[i], j) for i in range(3) for j in range(3))
rhs = sum(sig[i, j] * eps_dot[i, j] for i in range(3) for j in range(3))
print("(i)  sigma:grad v - sigma:eps_dot (symmetric sigma) =", sp.simplify(lhs - rhs))
assert sp.simplify(lhs - rhs) == 0

mass = sp.diff(rho, t) + divw([rho * v[k] for k in range(3)])
mom = [rho * (sp.diff(v[i], t) + sum(v[k] * D(v[i], k) for k in range(3))) - divsig[i] - rho * f[i]
       for i in range(3)]
en = rho * (sp.diff(e, t) + sum(v[k] * D(e, k) for k in range(3))) - lhs + divw(q) - rho * r

dens = rho * (sp.Rational(1, 2) * sum(v[i] ** 2 for i in range(3)) + e)
flux = [q[k] - sum(sig[k, j] * v[j] for j in range(3)) + dens * v[k] for k in range(3)]
total = sp.diff(dens, t) + divw(flux) - sum(rho * f[i] * v[i] for i in range(3)) - rho * r
combined = sum(v[i] * mom[i] for i in range(3)) + en + (dens / rho) * mass
r2 = sp.expand(total - combined)
print("(ii) conserved-form residual =", r2)
assert r2 == 0

# (iii) drop the advective flux: what remains is exactly its divergence
short = total - divw([dens * v[k] for k in range(3)])
r3 = sp.expand(short - combined)
print("(iii) (short-form residual) + div[rho(1/2|v|^2+e)v] =",
      sp.simplify(r3 + divw([dens * v[k] for k in range(3)])))
print("      hence short-form residual = -div[rho(1/2|v|^2+e)v], nonzero in a deforming medium")
assert sp.simplify(r3 + divw([dens * v[k] for k in range(3)])) == 0

print()
print("RESULT: (i) and (ii) reproduce. (iii) shows the Arena script's printed wording")
print("        'E_dot + div(q - sigma*v) = rho*f.v + rho*r' is a material-volume statement;")
print("        for a fixed control volume the advective energy flux must be carried.")
print("PASS: symmetric-stress power identity and the conserved energy identity reproduced")
