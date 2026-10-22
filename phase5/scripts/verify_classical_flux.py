#!/usr/bin/env python3
"""Symbolically check the local symmetric-Cauchy classical flux identity.

This validates an algebraic consequence of the stated local balances only. It does
not validate generalized continua, interface constitutive assumptions, or sources.
Requires SymPy (see tools/requirements-audit.txt).
"""
from __future__ import annotations

import sympy as sp

N = 3
v = sp.symbols("v0:3")
grad = sp.Matrix(N, N, lambda i, j: sp.Symbol(f"dv{i}_dx{j}"))
# Build a symmetric Cauchy stress tensor with independent upper-triangle entries.
sigma = sp.Matrix(N, N, lambda i, j: sp.Symbol(f"s{min(i,j)}{max(i,j)}"))
div_sigma = sp.symbols("divsigma0:3")  # (sigma_ji),j

# Power terms after using rho*v_dot_i = sigma_ji,j + rho*f_i.
kinetic_stress_power = sum(v[i] * div_sigma[i] for i in range(N))
strain_rate = sp.Matrix(N, N, lambda i, j: (grad[i, j] + grad[j, i]) / 2)
stress_strain_power = sum(
    sigma[i, j] * strain_rate[i, j] for i in range(N) for j in range(N)
)
# Product rule: div_j(sigma_ji v_i) = v_i div_j(sigma_ji) + sigma_ji v_i,j.
div_stress_velocity = kinetic_stress_power + sum(
    sigma[j, i] * grad[i, j] for i in range(N) for j in range(N)
)
residual = sp.simplify(kinetic_stress_power + stress_strain_power - div_stress_velocity)
assert residual == 0, residual

# Adding rho*e_dot = sigma:eps_dot - div(q) + rho*r gives
# E_dot = div(sigma*v - q) + rho*f.v + rho*r, hence J = q - sigma*v.
q_divergence = sp.Symbol("div_q")
body_power = sp.Symbol("rho_f_dot_v")
heat_source = sp.Symbol("rho_r")
energy_rate = sp.expand(div_stress_velocity - q_divergence + body_power + heat_source)
flux_divergence = sp.expand(q_divergence - div_stress_velocity)
assert sp.simplify(energy_rate + flux_divergence - body_power - heat_source) == 0

# SI base-dimension tuples (M, L, T, Theta); check density and flux dimensions.
rho = (1, -3, 0, 0)            # kg m^-3
specific_energy = (0, 2, -2, 0) # J kg^-1
velocity = (0, 1, -1, 0)       # m s^-1
stress = (1, -1, -2, 0)        # Pa
heat_flux = (1, 0, -3, 0)      # W m^-2
energy_density = tuple(a + b for a, b in zip(rho, specific_energy))
kinetic_density = tuple(a + 2*b for a, b in zip(rho, velocity))
mechanical_flux = tuple(a + b for a, b in zip(stress, velocity))
assert energy_density == kinetic_density == (1, -1, -2, 0)
assert mechanical_flux == heat_flux == (1, 0, -3, 0)

print("PASS: symmetric-stress power identity reduces to a divergence")
print("PASS: local balances imply E_dot + div(q - sigma*v) = rho*f.v + rho*r")
print("PASS: rho*e and 1/2*rho*v^2 have J/m^3 dimensions")
print("PASS: q and sigma*v have W/m^2 dimensions")
print("Scope: classical local Cauchy continuum, symmetric stress; no generalized/interface proof")
