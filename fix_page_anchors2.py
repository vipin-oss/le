#!/usr/bin/env python3
# FIX-3 part 2: sec11 lines 51, 76, 103 (exact full-line replacement).
import io

def set_line(path, lineno, new_line):
    lines = io.open(path, encoding="utf-8").read().split("\n")
    idx = lineno - 1
    print(f"replacing {path}:{lineno}")
    print("  OLD:", lines[idx][:150])
    lines[idx] = new_line
    io.open(path, "w", encoding="utf-8", newline="").write("\n".join(lines))
    print("  NEW:", new_line[:150])

path = "phase5/master/sections/sec11_advanced.tex"

set_line(path, 51,
    "Povstenko’s Eq.~(29) gives the fractional Cattaneo-type flux law $q_i + \\zeta\\,{}^C D_t^\\alpha q_i = -k T_{,i}$ with source coefficient $\\zeta$, restricted to the order range $0<\\alpha\\leq1$. Appendix A identifies the derivative as Caputo, while the source omits the superscript $C$ used here for clarity. The source does not identify $\\zeta$ with $\\tau^\\alpha/\\Gamma(1+\\alpha)$ \\cite{Povstenko2011Cattaneo}. Printed pages not checked here:")

set_line(path, 76,
    "This is the strain-gradient law \\cite{Aifantis2003}; Aifantis treats the gradient coefficients as phenomenological rather than derived. Printed page not checked here.")

set_line(path, 103,
    "where $\\delta^2$ is the two-temperature parameter. Ezzat and El Karamany (2011) express the conductive-thermodynamic temperature difference using the Laplacian of temperature \\cite{Ezzat2011}; with $T$ conductive and $T^*$ thermodynamic, eq:11.7 is stated as the manuscript model definition. Sign and placement conventions must be stated explicitly; the two forms agree only to first order in the coefficient. Source page not checked here; class B. This model is distinct from the single-temperature, temperature-rate-dependent Green--Lindsay formulation.")
print("PART 2 APPLIED")
