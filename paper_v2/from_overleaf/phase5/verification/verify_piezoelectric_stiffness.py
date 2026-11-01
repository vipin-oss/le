#!/usr/bin/env python3
"""Verify the open-/short-circuit stiffness distinction for the displayed laws.

These are symbolic consequences of the displayed Section 5 linear dielectric
and piezoelectric constitutive equations under quasistatic electrical closure.
They do not establish source transcription, dynamic Maxwell effects, or a
universal piezoelectric energy/stiffness formula outside the stated conventions.
"""
from __future__ import annotations

import sympy as sp

# Vectorized strain/stress components; e maps strain to electric displacement.
C = sp.Matrix([[sp.Symbol("C00"), sp.Symbol("C01")],
               [sp.Symbol("C10"), sp.Symbol("C11")]])
e = sp.Matrix([[sp.Symbol("e00"), sp.Symbol("e01")],
               [sp.Symbol("e10"), sp.Symbol("e11")]])
K = sp.Matrix([[sp.Symbol("K00"), sp.Symbol("K01")],
               [sp.Symbol("K10"), sp.Symbol("K11")]])
eps = sp.Matrix([sp.Symbol("eps0"), sp.Symbol("eps1")])
E = sp.Matrix([sp.Symbol("E0"), sp.Symbol("E1")])

# Vector form of sigma = C eps - e^T E and D = e eps + K E.
sigma = C * eps - e.T * E
D = e * eps + K * E

# Under the uncoupled linear-dielectric closure D=K E, the electric-field
# contribution is 1/2 E.T D. In the coupled piezoelectric law, 1/2 E.T D
# also contains a strain-electric cross term and is not the total stored energy.
D_dielectric = K * E
W_electric = sp.Rational(1, 2) * (E.T * D_dielectric)[0]
assert sp.simplify(W_electric - sp.Rational(1, 2) * (E.T * K * E)[0]) == 0
W_from_coupled_D = sp.Rational(1, 2) * (E.T * D)[0]
assert sp.simplify(W_from_coupled_D - W_electric - sp.Rational(1, 2) * (E.T * e * eps)[0]) == 0
assert sp.simplify(W_from_coupled_D - W_electric) != 0

# Open circuit: D=0, with invertible permittivity K.
E_open = -K.inv() * e * eps
sigma_open = sp.simplify(sigma.subs(dict(zip(E, E_open)), simultaneous=True))
C_open = C + e.T * K.inv() * e
assert sp.simplify(sigma_open - C_open * eps) == sp.zeros(2, 1)

# Short circuit: E=0; no permittivity correction remains.
sigma_short = sp.simplify(sigma.subs({E[0]: 0, E[1]: 0}))
assert sp.simplify(sigma_short - C * eps) == sp.zeros(2, 1)

# Negative checks: the two boundary conditions are not interchangeable, and
# the opposite sign fails for generic nonzero coupling and invertible K.
wrong_sign = C - e.T * K.inv() * e
assert sp.simplify((C_open - wrong_sign) * eps) != sp.zeros(2, 1)
assert sp.simplify((C_open - C) * eps) != sp.zeros(2, 1)

print("PASS: for D=K E, the dielectric field-energy contribution equals E.T D / 2")
print("PASS: the coupled D law contributes a strain-electric cross term; Eq. 5.5 alone is not total stored energy")
print("PASS: D=0 gives C_open = C + e.T K^(-1) e; E=0 gives short-circuit C")
print("PASS: negative tests reject a minus correction and conflation of open/short circuit")
print("Scope: quasistatic linear constitutive equations only; no dynamic Maxwell or source-transcription claim")
