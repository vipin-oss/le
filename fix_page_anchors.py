#!/usr/bin/env python3
# FIX-3: Withdraw all unverifiable page/equation anchors (no source PDFs in repo,
# so no held-copy page can be opened). Replace with class B "not checked here".
# Touches sec07 (eq:7.1 Eringen p430; eq:7.2 Aifantis p263) and sec11
# (eq:11.2/11.4 Povstenko p112/p101; eq:11.5 Aifantis p263; eq:11.7 Ezzat p940).
import io

def replace_line(path, lineno, old_sub, new_sub):
    lines = io.open(path, encoding="utf-8").read().split("\n")
    idx = lineno - 1
    assert old_sub in lines[idx], f"{path}:{lineno}: substring not found:\n{lines[idx]}"
    lines[idx] = lines[idx].replace(old_sub, new_sub, 1)
    io.open(path, "w", encoding="utf-8", newline="").write("\n".join(lines))
    print(f"patched {path}:{lineno}")

# --- sec07 ---
replace_line(
    "phase5/master/sections/sec07_nonlocal.tex", 22,
    "Eringen (1999) prints this integral nonlocal law as Eq.~(4.2) on p.~430 \\cite{Eringen1999}; the manuscript form matches up to symbol names.",
    "Eringen (1999) states this integral nonlocal law \\cite{Eringen1999}; the manuscript form matches up to symbol names. The printed page and equation were not checked here.",
)
replace_line(
    "phase5/master/sections/sec07_nonlocal.tex", 34,
    "This differential (Helmholtz) form is printed in Aifantis (2003) as Eq.~(2.1) with the Helmholtz pair (2.2) on p.~263 \\cite{Aifantis2003}; Eringen (1983) developed the differential form of nonlocal elasticity \\cite{Eringen1983} but does not print this specific Helmholtz pair. With $c_1=0$ and $c_2=\\ell^2$ it reduces to the strain-gradient law of Section~\\ref{sec:7.2}; Aifantis (1992) p.~1282 notes that stress-gradient terms were then unexplored.",
    "This differential (Helmholtz) form is associated with Aifantis (2003) \\cite{Aifantis2003}; Eringen (1983) developed the differential form of nonlocal elasticity \\cite{Eringen1983}. The printed page and equation were not checked here. With $c_1=0$ and $c_2=\\ell^2$ it reduces to the strain-gradient law of Section~\\ref{sec:7.2}.",
)

# --- sec11 ---
replace_line(
    "phase5/master/sections/sec11_advanced.tex", 30,
    "printed as Povstenko (A.5), p.~112;",
    "printed as Povstenko (A.5) (printed page not checked here);",
)
replace_line(
    "phase5/master/sections/sec11_advanced.tex", 43,
    "the Caputo definition (A.5), p.~112 \\cite{Povstenko2011};",
    "the Caputo definition (A.5) \\cite{Povstenko2011} (printed page not checked here);",
)
replace_line(
    "phase5/master/sections/sec11_advanced.tex", 51,
    "Povstenko's Eq.~(29), on printed p.~101, gives the fractional Cattaneo-type flux law",
    "Povstenko's Eq.~(29) gives the fractional Cattaneo-type flux law",
)
replace_line(
    "phase5/master/sections/sec11_advanced.tex", 51,
    "Appendix A identifies the derivative as Caputo (printed p.~112), while the source omits",
    "Appendix A identifies the derivative as Caputo, while the source omits",
)
# Add "printed pages not checked here" sentence after the Caputo sentence on L51
replace_line(
    "phase5/master/sections/sec11_advanced.tex", 51,
    "The source does not identify $\\zeta$ with $\\tau^\\alpha/\\Gamma(1+\\alpha)$ \\cite{Povstenko2011Cattaneo}:",
    "The source does not identify $\\zeta$ with $\\tau^\\alpha/\\Gamma(1+\\alpha)$ \\cite{Povstenko2011Cattaneo}. Printed pages not checked here:",
)
replace_line(
    "phase5/master/sections/sec11_advanced.tex", 76,
    "This is the strain-gradient law printed in Aifantis (2003) Eq.~(2.1) on p.~263 \\cite{Aifantis2003}; Aifantis treats the gradient coefficients as phenomenological rather than derived.",
    "This is the strain-gradient law \\cite{Aifantis2003}; Aifantis treats the gradient coefficients as phenomenological rather than derived. Printed page not checked here.",
)
replace_line(
    "phase5/master/sections/sec11_advanced.tex", 103,
    "Ezzat and El Karamany (2011) p.~940 Eq.~(15) give $T^* = T - \\delta^2 \\nabla^2 T$ with $T$ the conductive temperature and $T^*$ the thermodynamic temperature, matching the manuscript definitions exactly \\cite{Ezzat2011}; class A anchor to ZAMP p.~940 Eq.(15).",
    "Ezzat and El Karamany (2011) express the conductive-thermodynamic temperature difference using the Laplacian of temperature \\cite{Ezzat2011}; with $T$ conductive and $T^*$ thermodynamic, eq:11.7 is stated as the manuscript model definition. Sign and placement conventions must be stated explicitly; the two forms agree only to first order in the coefficient. Source page not checked here; class B.",
)
print("ALL PROSE PATCHES APPLIED")
