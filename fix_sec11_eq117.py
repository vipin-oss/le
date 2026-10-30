#!/usr/bin/env python3
# Rewrite sec11_advanced.tex line 103 as correct LaTeX: single backslashes,
# and the two-temperature equation wrapped in $...$ math mode.
p = "/home/user/le/phase5/master/sections/sec11_advanced.tex"
lines = open(p, encoding="utf-8").read().split("\n")
lines[102] = (
    "where $\\delta^2$ is the two-temperature parameter. "
    "Ezzat and El Karamany (2011) p.~940 Eq.~(15) give "
    "$T^* = T - \\delta^2 \\nabla^2 T$ with $T$ the conductive "
    "temperature and $T^*$ the thermodynamic temperature, "
    "matching the manuscript definitions exactly \\cite{Ezzat2011}; "
    "class A anchor to ZAMP p.~940 Eq.~(15). This model is distinct "
    "from the single-temperature, temperature-rate-dependent "
    "Green--Lindsay formulation."
)
open(p, "w", encoding="utf-8", newline="").write("\n".join(lines))
print("line 103 rewritten")
print(lines[102][:150])
