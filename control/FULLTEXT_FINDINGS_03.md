# FULLTEXT FINDINGS 03 (supervisor): Guyer-Krumhansl 1966
Source: R. A. Guyer, J. A. Krumhansl, Phys. Rev. 148, 778 (1966), read from rendered pages 2 and 4 (supervisor). Paper is kinetic theory (phonon Boltzmann), NOT a continuum-thermoelasticity paper.
F10 What the paper prints:
- Eqs (1a)/(1b): macroscopic equations when R-processes (resistive) are fast relative to N-processes (normal): da0/dt + <0|c.grad|1> a1 = 0 and a1 - <1|R*^-1|1><1|c.grad|0> a0 = 0 (Fourier-type limit, valid for Omega*tau_R << 1).
- Eqs (2a)/(2b): when N-processes are fast (Omega*tau_N << 1): the energy equation plus a1 evolution with N* operator.
- Eq (4) (steady state, after specialising 2b): lap(a1z) + 2 grad(div a1z) - a1z/lambda^2 = 5<0|c.grad|1> a0/(tau_N c^2), with lambda^2 = c^2 tau_N tau_z / 5. So the GK spatial operator is lap + 2 grad div (non-local in the flux), and the length scale is lambda^2 = c^2 tau_N tau_R/5.
- Eq (6)/(8)/(10): steady-state Poiseuille result, effective conductivity kappa = kappa_z G(mu), G(mu)=1-2J1(iR/lambda)/((iR/lambda)J0(iR/lambda)), limit mu<<1 gives (5/4) C_v c^2 R^2/(c^2 tau_N)-type form (Sussmann-Thellung).
F11 What the paper does NOT print (so cannot be cited for it): the continuum "GK heat-flux law" tau_R dq/dt + q = -kappa grad T + ell^2 (lap q + 2 grad div q) as one displayed equation, nor a thermoelastic coupling. That time-dependent continuum form is a later reduction; any manuscript equation of that kind must cite a source that prints it, tagged SECONDARY-SOURCE, with lambda^2 = c^2 tau_N tau_R/5 (F10) as the checkable constant.
ORDERS
BRAVE: use F10/F11 to close the GK row in FULLTEXT_FACTS (PRIMARY-SOURCE-CHECKED for the Boltzmann-derived structure and lambda^2; UNVERIFIED for any specific continuum form). Check the manuscript's GK equation and tau_N/tau_R notation against F10.
ARENA: when writing the GK part, say "derived from phonon Boltzmann equation (Guyer-Krumhansl 1966)", quote lambda^2 = c^2 tau_N tau_R/5, and do not attribute a ready-made continuum flux law to the 1966 paper.

## F12 Clarification (supervisor, from page 4 of the paper, shown just above eq (4))
Page text: <1|R*|1> = -<0|tau_R(q)^-1|0> = -tau_z^-1, and "This average of the relaxation time rather than the relaxation time shall be referred to as the Ziman limit." So tau_z IS the Ziman-averaged resistive (R-process) relaxation time, i.e. the paper's tau_R averaged over the phonon distribution. F10 (tau_z, as printed) and F11 (tau_R, generic notation) are the same quantity: lambda^2 = c^2 tau_N tau_z / 5 with tau_z = Ziman-average of tau_R. Quote as printed (tau_z) and define it as the Ziman-averaged R-process time. No inconsistency.
