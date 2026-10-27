#!/usr/bin/env python3
"""Audit selected Q1 notation harmonization and algebra for displayed dispersion laws.

This checks the symbols as written in the manuscript; it does not verify source
transcription, material-model applicability, convergence, or stability.
"""
from __future__ import annotations

from pathlib import Path
import re

import sympy as sp

ROOT = Path(__file__).resolve().parents[2]
SEC6 = (ROOT / "phase5/master/sections/sec06_transport.tex").read_text(encoding="utf-8")
SEC7 = (ROOT / "phase5/master/sections/sec07_nonlocal.tex").read_text(encoding="utf-8")
SEC17 = (ROOT / "phase5/master/sections/sec17_conclusions.tex").read_text(encoding="utf-8")
NOTATION = (ROOT / "phase5/master/frontmatter/notation.tex").read_text(encoding="utf-8")
APPENDIX = (ROOT / "phase5/master/appendices/energy_flux_derivations.tex").read_text(encoding="utf-8")
EQ_REGISTER = (ROOT / "phase5/master/appendices/appA_equation_register.tex").read_text(encoding="utf-8")
SVG = (ROOT / "phase5/figures/source/fig11-nonlocality.svg").read_text(encoding="utf-8")

# The MDD finite-history window and its kernel use distinct labels from angular
# frequency and from GN-III/dielectric kappa symbols.
assert r"D_{\omega_M} f(t)" in SEC6
assert r"K_{\mathrm{MDD}}(t-\theta)" in SEC6
assert r"D_\omega f(t)" not in SEC6
assert r"\xi" not in SEC6  # reserve xi for the spatial nonlocal length
assert r"\omega_M" in NOTATION and "Angular frequency" in NOTATION
assert r"$K_{\mathrm{MDD}}$" in NOTATION
assert r"\kappa, \kappa^*" in NOTATION and r"\kappa_{ij}" in NOTATION
assert r"D_{\omega_M}" in APPENDIX and r"K_{\mathrm{MDD}}(t-\theta)" in APPENDIX
assert r"K_{\mathrm{MDD}}(s)" in APPENDIX
assert "equation-level source check pending" in APPENDIX
assert r"s=t-\theta" in APPENDIX

# Separate the Section 7 one-dimensional dispersion wave number from the
# thermal-conductivity coefficient k used in the local heat-flux laws.
assert r"c(k_{\mathrm w})" in SEC7
assert r"k_{\mathrm w}" in NOTATION
assert "distinct from the thermal conductivity" in SEC7
assert r"c(k_{\mathrm w})" in EQ_REGISTER
assert "k_w" in SVG and "c₀k_w" in SVG and "ℓ²k_w²" in SVG
assert not re.search(r"(?<![A-Za-z_])c\(k\)", SEC7)

# Verify algebraic consequences only for the displayed one-dimensional laws.
k_w, xi, c0, ell = sp.symbols("k_w xi c0 ell", positive=True)
phase_speed = c0 / sp.sqrt(1 + xi**2 * k_w**2)
angular_frequency = k_w * phase_speed
group_velocity = sp.diff(angular_frequency, k_w)
assert sp.simplify(
    group_velocity - c0 / (1 + xi**2 * k_w**2) ** sp.Rational(3, 2)
) == 0
assert sp.limit(phase_speed, k_w, 0) == c0
assert sp.limit(phase_speed, k_w, sp.oo) == 0
assert sp.limit(angular_frequency, k_w, sp.oo) == c0 / xi
assert sp.limit(group_velocity, k_w, sp.oo) == 0

gradient_speed_squared = c0**2 * (1 + ell**2 * k_w**2)
assert sp.diff(gradient_speed_squared, k_w) == 2 * c0**2 * ell**2 * k_w

# The Section 17 table's two labels must match the equation/notation entries.
assert "$\\tau_0$ & LS heat-flux relaxation time" in SEC17
assert "$c_T$ & LS thermal characteristic speed" in SEC17

print("PASS: MDD window/kernel labels, distinct conductivity/wavenumber notation, and Section 17 labels are consistent.")
print("PASS: derivatives and limits follow algebraically from the displayed 1D nonlocal and positive-gradient laws.")
print("Scope: no source-transcription, family-wide equivalence, convergence, stability, or admissibility claim.")
