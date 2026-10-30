#!/usr/bin/env python3
"""Verify Eq. 4.5 by eliminating div(q) from the stated Cattaneo law.

This is an algebraic derivation from the displayed source-free local balance
and flux law; it does not independently verify either source transcription.
"""
import sympy as sp

rho, cv, tau, k, beta, T0 = sp.symbols("rho cv tau k beta T0", positive=True)
Tdot, Tddot, lapT = sp.symbols("Tdot Tddot lapT")
divq, divqdot = sp.symbols("divq divqdot")
divudot, divuddot = sp.symbols("divudot divuddot")

# Classical source-free local balance and its tau-weighted time derivative.
energy = rho * cv * Tdot + divq + beta * T0 * divudot
energy_dot = rho * cv * Tddot + divqdot + beta * T0 * divuddot
weighted_energy = rho * cv * (Tdot + tau * Tddot) + divq + tau * divqdot + beta * T0 * (divudot + tau * divuddot)
assert sp.simplify(weighted_energy - (energy + tau * energy_dot)) == 0
# Divergence of q + tau qdot = -k grad(T).
cattaneo_divergence = divq + tau * divqdot + k * lapT
reduced = sp.simplify(weighted_energy.subs(divq + tau * divqdot, -k * lapT))
assert sp.simplify(cattaneo_divergence.subs(divq + tau * divqdot, -k * lapT)) == 0
expected = rho * cv * (Tdot + tau * Tddot) - k * lapT + beta * T0 * (divudot + tau * divuddot)
assert sp.simplify(reduced - expected) == 0

# Negative control: omitting the tau-weighted mechanical coupling leaves a term.
omitted_coupling = rho * cv * (Tdot + tau * Tddot) - k * lapT + beta * T0 * divudot
assert sp.simplify(expected - omitted_coupling - beta * T0 * tau * divuddot) == 0
assert sp.simplify(expected - omitted_coupling) != 0

# In the uncoupled scalar thermal branch beta=0, the principal part gives c^2=k/(rho cv tau).
omega, wave_number = sp.symbols("omega wave_number", positive=True)
principal = rho * cv * tau * omega**2 - k * wave_number**2
c_squared = sp.solve(principal, omega**2)[0] / wave_number**2
assert sp.simplify(c_squared - k / (rho * cv * tau)) == 0
assert sp.limit(c_squared, tau, 0, dir="+") == sp.oo

print("PASS: applying (1+tau*d/dt) to the balance and using Cattaneo divergence gives Eq. 4.5")
print("PASS: negative control detects omitted tau-weighted strain-rate coupling")
print("PASS: uncoupled principal thermal branch has c_T^2=k/(rho cv tau)")
print("Scope: constant isotropic coefficients, source-free local balance; the coupled modes require the full system")
