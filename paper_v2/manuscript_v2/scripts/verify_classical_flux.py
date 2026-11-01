#!/usr/bin/env python3
"""Derive the classical energy balance from material balances symbolically.

The field identities below are independent symbolic checks: mass, material
momentum, and internal-energy residuals are constructed from the underlying
fields, then compared with the Eulerian total-energy residual. This is not a
verification of generalized continua or interface constitutive assumptions.
Requires SymPy (see tools/requirements-audit.txt).
"""
from __future__ import annotations

import sympy as sp

N = 3
x = sp.symbols("x0:3", real=True)
t = sp.symbols("t", real=True)
coords = tuple(x) + (t,)


def field(name: str):
    return sp.Function(name)(*coords)


def vec(name: str):
    return [field(f"{name}{i}") for i in range(N)]


def mat(name: str):
    return sp.Matrix(N, N, lambda i, j: field(f"{name}{i}{j}"))


def divergence(vector):
    return sum(sp.diff(vector[j], x[j]) for j in range(N))


def gradient_dot(vector, scalar):
    return sum(vector[j] * sp.diff(scalar, x[j]) for j in range(N))

rho, e, r = field("rho"), field("e"), field("r")
v, q, f = vec("v"), vec("q"), vec("f")
sigma = mat("sigma")
sigma = sigma.subs({sigma[j, i]: sigma[i, j] for i in range(N) for j in range(i)})

# Independent local field residuals for the continuum balances.
# Mass conservation: D rho / Dt + rho div(v) = 0, equivalently the Eulerian form.
continuity_residual = sp.diff(rho, t) + divergence([rho * v[j] for j in range(N)])

# Material momentum balance: rho Dv_i/Dt = sigma_ij,j + rho f_i.
div_sigma = [sum(sp.diff(sigma[i, j], x[j]) for j in range(N)) for i in range(N)]
momentum_residual = [
    rho * (sp.diff(v[i], t) + gradient_dot(v, v[i])) - div_sigma[i] - rho * f[i]
    for i in range(N)
]

# Internal-energy balance: rho De/Dt = sigma:eps_dot - div(q) + rho r.
eps_dot = sp.Matrix(
    N, N, lambda i, j: sp.Rational(1, 2) * (sp.diff(v[i], x[j]) + sp.diff(v[j], x[i]))
)
stress_strain_power = sum(sigma[i, j] * eps_dot[i, j] for i in range(N) for j in range(N))
internal_residual = (
    rho * (sp.diff(e, t) + gradient_dot(v, e))
    - stress_strain_power
    + divergence(q)
    - rho * r
)

# Combining v_i times the momentum residual with the internal-energy residual
# gives the material total-energy balance by the product rule and symmetry of sigma.
kinetic_specific = sp.Rational(1, 2) * sum(v[i] ** 2 for i in range(N))
h = kinetic_specific + e
stress_power_flux = [sum(sigma[j, i] * v[i] for i in range(N)) for j in range(N)]
material_total_residual = (
    rho * (sp.diff(h, t) + gradient_dot(v, h))
    + divergence([q[j] - stress_power_flux[j] for j in range(N)])
    - sum(rho * f[i] * v[i] for i in range(N))
    - rho * r
)
combined_material_residual = sum(v[i] * momentum_residual[i] for i in range(N)) + internal_residual
assert sp.simplify(combined_material_residual - material_total_residual) == 0

# Eulerian conversion: rho Dh/Dt = d_t(rho h) + div(rho h v) - h*mass_residual.
energy_density = rho * h
advective_flux = [energy_density * v[j] for j in range(N)]
eulerian_flux = [q[j] - stress_power_flux[j] + advective_flux[j] for j in range(N)]
source_power = sum(rho * f[i] * v[i] for i in range(N)) + rho * r
eulerian_total_residual = sp.diff(energy_density, t) + divergence(eulerian_flux) - source_power
assert sp.simplify(
    eulerian_total_residual - material_total_residual - h * continuity_residual
) == 0
assert sp.simplify(
    eulerian_total_residual - combined_material_residual - h * continuity_residual
) == 0

# Negative control: dropping advection from the exact Eulerian flux leaves
# precisely minus its divergence after the material balances and continuity hold.
short_flux = [q[j] - stress_power_flux[j] for j in range(N)]
short_eulerian_residual = sp.diff(energy_density, t) + divergence(short_flux) - source_power
assert sp.simplify(
    short_eulerian_residual - combined_material_residual - h * continuity_residual
    + divergence(advective_flux)
) == 0

# Explicit nonzero example: rho=1, e=0, v=(x0,0,0) gives div(rho*h*v)=3*x0^2/2.
x0 = sp.symbols("x0", real=True)
example_advective_divergence = sp.diff(sp.Rational(1, 2) * x0**3, x0)
assert sp.simplify(example_advective_divergence - sp.Rational(3, 2) * x0**2) == 0
assert example_advective_divergence != 0

# SI base-dimension tuples (M, L, T, Theta); check density and exact flux terms.
rho_dim = (1, -3, 0, 0)             # kg m^-3
specific_energy_dim = (0, 2, -2, 0)  # J kg^-1
velocity_dim = (0, 1, -1, 0)         # m s^-1
stress_dim = (1, -1, -2, 0)          # Pa
heat_flux_dim = (1, 0, -3, 0)        # W m^-2
energy_density_dim = tuple(a + b for a, b in zip(rho_dim, specific_energy_dim))
kinetic_density_dim = tuple(a + 2 * b for a, b in zip(rho_dim, velocity_dim))
mechanical_flux_dim = tuple(a + b for a, b in zip(stress_dim, velocity_dim))
advective_flux_dim = tuple(a + b + c for a, b, c in zip(rho_dim, specific_energy_dim, velocity_dim))
assert energy_density_dim == kinetic_density_dim == (1, -1, -2, 0)
assert mechanical_flux_dim == heat_flux_dim == advective_flux_dim == (1, 0, -3, 0)

# Under Fourier closure the thermal contribution to Clausius--Duhem is
# non-negative for positive conductivity and absolute temperature.
absolute_temperature = sp.symbols("absolute_temperature", positive=True)
conductivity = sp.symbols("conductivity", positive=True)
grad_theta = sp.symbols("grad_theta0:3", real=True)
q_fourier = [-conductivity * component for component in grad_theta]
thermal_dissipation = sp.simplify(
    -sum(qi * gi for qi, gi in zip(q_fourier, grad_theta)) / absolute_temperature**2
)
expected_dissipation = conductivity * sum(component**2 for component in grad_theta) / absolute_temperature**2
assert sp.simplify(thermal_dissipation - expected_dissipation) == 0

print("PASS (SUBSTANTIVE): material momentum and internal-energy residuals combine to the material total-energy balance")
print("PASS (SUBSTANTIVE): mass conservation converts that balance to the Eulerian flux q - sigma.v + rho*(|v|^2/2 + e)*v")
print("PASS (NEGATIVE CONTROL): dropping the advective flux leaves exactly -div[rho*(|v|^2/2 + e)*v]")
print("PASS (NEGATIVE CONTROL): the omitted divergence is nonzero for rho=1, e=0, v=(x,0,0)")
print("PASS (DIMENSIONAL CHECK): total energy density and all three energy-flux contributions have consistent SI dimensions")
print("PASS (SUBSTANTIVE): Fourier thermal entropy production is k|grad(Theta)|^2/Theta^2 >= 0 for k, Theta > 0")
print("Scope: classical local Cauchy continuum, symmetric stress, continuity, and material momentum/internal-energy balances; no generalized/interface proof")
