#!/usr/bin/env python3
# Insert a W3.3 worked-example paragraph after W1.1's Scope paragraph in sec12.
p = "/home/user/le/phase5/master/sections/sec12_comparative.tex"
s = open(p, encoding="utf-8").read()
anchor = (
    "\\paragraph{Scope.} These statements concern only the displayed equations. "
    "They are not convergence, stability, or source-transcription results.\n\n\n\n"
    "\\subsection{Verified equation register: assumptions and limits}"
)
insert = (
    "\\paragraph{Scope.} These statements concern only the displayed equations. "
    "They are not convergence, stability, or source-transcription results.\n\n"
    "\\paragraph{Worked example: Lord--Shulman reduction from the template.}"
    " Set $\\tau_T=\\tau_v=k^*=0$ and write $\\tau_q=\\tau_0$ in Eq.~\\eqref{eq:12.template}."
    " The lag terms $k\\tau_T\\dot T_{,i}$ and $k^*v_{,i}$ vanish and $\\tau_q\\dot q_i$"
    " becomes $\\tau_0\\dot q_i$, leaving $q_i+\\tau_0\\dot q_i+kT_{,i}=0$ (Eq.~\\eqref{eq:6.2}, Section~6)."
    " Setting further $\\tau_0=0$ gives $q_i+kT_{,i}=0$, Fourier's law."
    " The symbolic check applies this substitution and reports no residual;"
    " the residual against Fourier's law is $\\tau_0\\dot q_i$, present unless $\\tau_0\\to0$."
    " This is an exact substitution into the displayed template, not a convergence theorem.\n\n\n\n"
    "\\subsection{Verified equation register: assumptions and limits}"
)
assert anchor in s, "anchor not found"
s = s.replace(anchor, insert, 1)
open(p, "w", encoding="utf-8", newline="").write(s)
print("inserted W3.3 worked example")
