#!/usr/bin/env python3
"""Check the linearized classical thermoelastic heat equation.

The source-page anchor for the displayed equation is Biot (1956), printed
p. 242, Eqs. (3.3)--(3.4), recorded in OCL-513. This SymPy check is a separate
symbolic derivation from the manuscript's linear entropy relation and local
heat balance; it does not verify source transcription or nonlinear closure.
"""
from __future__ import annotations

from pathlib import Path
import sympy as sp

rho, cv, T0, beta, k = sp.symbols("rho cv T0 beta k", positive=True)
T, Tdot, epsdot, lap_T, r = sp.symbols("T Tdot epsdot lap_T r", real=True)

# Linear isotropic entropy relation from the displayed free energy:
# s = s0 + beta/rho * eps_kk + cv/T0 * T.
sdot = beta / rho * epsdot + cv / T0 * Tdot
# The local heat balance is rho*Theta*sdot + div(q) = rho*r.
# With Theta=T0+T and Fourier q=-k grad(T), div(q)=-k lap(T).
full_residual = sp.expand(rho * (T0 + T) * sdot - k * lap_T - rho * r)
linear_residual = beta * T0 * epsdot + rho * cv * Tdot - k * lap_T - rho * r
nonlinear_remainder = beta * T * epsdot + rho * cv * T * Tdot / T0
assert sp.simplify(full_residual - linear_residual - nonlinear_remainder) == 0

# Under first-order perturbation scaling, the remainder is second order.
eps = sp.symbols("epsilon", real=True)
T1, Tdot1, epsdot1 = sp.symbols("T1 Tdot1 epsdot1", real=True)
scaled_remainder = nonlinear_remainder.subs(
    {T: eps * T1, Tdot: eps * Tdot1, epsdot: eps * epsdot1}
)
assert sp.Poly(sp.expand(scaled_remainder), eps).degree() == 2
assert sp.expand(scaled_remainder).coeff(eps, 1) == 0

# Solving the source-free linear residual gives the displayed heat equation.
source_free = linear_residual.subs(r, 0)
expected = rho * cv * Tdot - (k * lap_T - beta * T0 * epsdot)
assert sp.simplify(source_free - expected) == 0
assert sp.simplify(source_free.subs(beta, 0) - (rho * cv * Tdot - k * lap_T)) == 0
assert sp.simplify(source_free.subs(k, 0) - (rho * cv * Tdot + beta * T0 * epsdot)) == 0

# STRUCTURAL ONLY: ensure the manuscript prints the formula represented above.
root = Path(__file__).resolve().parents[1]
section4 = (root / "master/sections/sec04_thermoelastic.tex").read_text(encoding="utf-8")
assert "zero body force and heat supply" in section4
assert "small perturbations about a uniform reference temperature" in section4
assert r"\rho c_v \dot{T} = k\nabla^2 T - \beta T_0 \dot{u}_{i,i}" in section4

print("PASS (SUBSTANTIVE): the entropy relation and local heat balance give the first-order thermoelastic heat equation")
print("PASS (ORDER CHECK): discarded terms are quadratic in temperature/strain perturbations")
print("PASS (NEGATIVE CONTROLS): beta=0 gives Fourier diffusion; k=0 retains thermoelastic strain-rate coupling")
print("PASS (STRUCTURAL ONLY): Section 4 prints the checked source-free equation")
print("Scope: linear isotropic thermoelasticity, constant coefficients, Fourier heat flux, first-order perturbations; no nonlinear or generalized-theory claim")
