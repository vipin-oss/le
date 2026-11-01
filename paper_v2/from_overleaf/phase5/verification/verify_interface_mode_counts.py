#!/usr/bin/env python3
"""Verify selected interface mode counts and boundary-system dimensions.

The checks are restricted to the displayed isotropic local equations and the
listed interface conditions. A square matrix size is a count, not a proof of
rank, uniqueness, radiation admissibility, or well-posedness.
"""
from __future__ import annotations

from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]

# Plane-strain classical coupled thermoelasticity, using Eqs. (4.1)--(4.2)
# with Fourier flux. Set s=k^2+q^2 and L=lambda+mu. The sagittal symbol has
# mechanical block a I + L v v^T, thermal block d, and cross-couplings along v.
q, k = sp.symbols("q k", real=True)
rho, omega, lam, mu = sp.symbols("rho omega lambda mu", positive=True)
beta, T0, cv, conductivity = sp.symbols(
    "beta T0 c_v conductivity", positive=True
)
I = sp.I
s = sp.symbols("s", real=True)
s_q = k**2 + q**2
a = mu * s - rho * omega**2
L = lam + mu
d = conductivity * s - I * omega * rho * cv
a_q = mu * s_q - rho * omega**2
d_q = conductivity * s_q - I * omega * rho * cv

m11 = a_q + L * k**2
m22 = a_q + L * q**2
m12 = L * k * q
m13 = I * beta * k
m23 = I * beta * q
gamma_k = beta * T0 * omega * k
gamma_q = beta * T0 * omega * q

# Explicit 3x3 determinant expansion, avoiding costly generic determinant
# factorization. The second expression follows from resolving longitudinal and
# transverse directions of the isotropic mechanical block.
det_expanded = (
    m11 * m22 * d_q
    + m12 * m23 * gamma_k
    + m13 * m12 * gamma_q
    - m13 * m22 * gamma_k
    - m12 * m12 * d_q
    - m11 * m23 * gamma_q
)
coupled_factor = (a + L * s) * d - I * beta**2 * T0 * omega * s
det_factored = a * coupled_factor
coupled_factor_q = (a_q + L * s_q) * d_q - I * beta**2 * T0 * omega * s_q
det_factored_q = a_q * coupled_factor_q
assert sp.expand(det_expanded - det_factored_q) == 0
assert sp.Poly(det_factored_q, q).degree() == 6
assert sp.expand(det_factored_q.subs(q, -q) - det_factored_q) == 0
assert sp.Poly(a, s).degree() == 1
assert sp.Poly(coupled_factor, s).degree() == 2
print("PASS: displayed plane-strain thermoelastic characteristic determinant is even and degree six in q")
print("PASS: generic distinct roots give one shear pair and two coupled thermo-compressional pairs")

# In the uncoupled isotropic elastic sagittal system, the determinant separates
# into shear and P factors and is degree four/even in q: two modes per direction.
elastic_det = a_q * (a_q + L * s_q)
assert sp.Poly(elastic_det, q).degree() == 4
assert sp.expand(elastic_det.subs(q, -q) - elastic_det) == 0
assert sp.Poly(a + L * s, s).degree() == 1
print("PASS: isotropic plane-strain elasticity has one shear pair and one P pair")


def matching_matrix_size(n_modes_per_side: int, fields: tuple[str, ...], label: str) -> tuple[int, int]:
    """Build generic continuity equations and return their coefficient shape."""
    reflected = sp.symbols(f"{label}_r0:{n_modes_per_side}")
    transmitted = sp.symbols(f"{label}_t0:{n_modes_per_side}")
    unknowns = (*reflected, *transmitted)
    equations = []
    for field_index, field in enumerate(fields):
        left = sum(
            sp.Symbol(f"{label}_{field}_r{j}") * reflected[j]
            for j in range(n_modes_per_side)
        )
        right = sum(
            sp.Symbol(f"{label}_{field}_t{j}") * transmitted[j]
            for j in range(n_modes_per_side)
        )
        incident = sp.Symbol(f"{label}_{field}_inc{field_index}")
        equations.append(left - right + incident)
    matrix, _ = sp.linear_eq_to_matrix(equations, unknowns)
    return matrix.shape


# One-dimensional welded longitudinal example: u and sigma continuity.
assert matching_matrix_size(1, ("u3", "sigma33"), "oned") == (2, 2)
# Oblique plane-strain elastic P-SV scattering: two outgoing modes on each side;
# two displacement and two traction components are matched.
assert matching_matrix_size(
    2, ("u1", "u3", "sigma13", "sigma33"), "elastic"
) == (4, 4)
# Classical coupled plane-strain thermoelasticity: three outgoing modes on each
# side; two displacements, two tractions, temperature, and normal heat flux match.
assert matching_matrix_size(
    3,
    ("u1", "u3", "sigma13", "sigma33", "T", "q3"),
    "thermoelastic",
) == (6, 6)
print("PASS: selected matching conditions produce 2x2, 4x4, and 6x6 scattering systems")

mode_table = (ROOT / "master/tables/source/T6_mode_counts.tex").read_text(encoding="utf-8").lower()
for expected in (
    "1d longitudinal welded", "plane-strain isotropic elastic",
    "classical fourier thermoelastic", r"$2\times2$", r"$4\times4$", r"$6\times6$",
):
    assert expected in mode_table, f"mode-count table missing {expected}"
section9 = (ROOT / "master/sections/sec09_interfaces.tex").read_text(encoding="utf-8")
assert r"\input{tables/source/T6_mode_counts}" in section9
assert "does not by itself prove rank" in section9
print("PASS: rendered-scope table records the checked examples and leaves rank/model-wide counts open")
print("Scope: no universal count for GL, LS, phase-lag, GN, piezoelectric, nonlocal, or memory-dependent interfaces")
