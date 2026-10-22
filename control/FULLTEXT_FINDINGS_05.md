# FULLTEXT FINDINGS 05 (supervisor): equations transcribed from rendered pages
Read by supervisor from handler's Downloads (page renders, not text layer). Facts only. Tag: PRIMARY-SOURCE-CHECKED for the printed equations below (transcription by supervisor from the image; density factor in GN 1993 (3.16) printed as "c theta-ddot", read from render).

## F16 GN type III - GN 1992, J. Thermal Stresses 15:253-264, eqs (3.19),(3.20),(4.1),(4.2) (p.261)
(3.19) (lambda+mu) grad div u + mu lap u - [E beta*/(3(1-2nu))] grad theta + rho0 b = rho0 u-ddot
(3.20) rho0 c theta-ddot + [E beta* theta0/(3(1-2nu))] div u-ddot = rho0 r-dot + kappa lap theta-dot + kappa* lap theta
Restrictions (3.18): kappa** = 0, kappa >= 0, c >= 0. 1-D forms (4.1),(4.2) carry theta_xt-type and third-order u_xtt terms: rho0 c theta_tt + (1/3)((1+nu)/(1-nu))(lambda+2mu) beta* theta0 u_xtt = rho0 r_t + kappa theta_xxt + kappa* theta_xx.
Here theta = temperature variation; coupling is div u-ddot paired with theta-ddot (two derivatives each).

## F17 GN type II - GN 1993, J. Elasticity 31:189-208, eqs (3.15)-(3.17) (p.202)
(3.15) same momentum equation as (3.19) above.
(3.16) c theta-ddot + [E beta* theta0/(3(1-2nu))] div u-ddot = rho0 r + kappa* lap theta   (density factor as printed; theta = temperature)
(3.17) restrictions c > 0, kappa* >= 0, lambda + 2 mu >= 0; "the system permits propagation of harmonic waves without damping".
Type II = type III with kappa = 0. No dissipation.
CONSEQUENCE for manuscript EQ-016: in the TEMPERATURE variable the coupling is div u-ddot with theta-ddot (as printed). In the THERMAL-DISPLACEMENT variable alpha (alpha-dot = theta) integrate once in time: c alpha-ddot + [..] theta0 div u-dot = kappa* lap alpha. So manuscript EQ-016 "k lap alpha = rho c alpha-ddot + beta T0 u-ddot" (alpha with u-ddot) mixes the two forms: one time derivative too many on the coupling. Brave B9 verdict CONFIRMED by two routes (derivation + primary source).

## F18 Continuum GK law as printed in Tzou 1995 (J. Heat Transfer 117, p.10, eqs (15)-(17))
(15) dq/dt + (c^2 C_p/3) grad T + (1/tau_R) q = (tau_N c^2/5)[ lap q + 2 grad(div q) ]   [Tzou quotes GK 1966; tau_R = umklapp (momentum-nonconserving), tau_N = normal]
(16) lap T + (9 tau_N/5) d/dt(lap T) = (3/(tau_R c^2)) dT/dt + (3/c^2) d2T/dt2   [Tzou notes Joseph-Preziosi 1989 derived it earlier; two typos in JP's Cp placement]
(17) mapping to DPL: alpha = tau_R c^2/3, tau_T = 9 tau_N/5, tau_q = tau_R.
Consistency with F10: tau_R-form of (15) times tau_R gives tau_R dq/dt + q = ... + ell^2(lap q + 2 grad div q) with ell^2 = c^2 tau_N tau_R/5 = GK lambda^2 (tau_z Ziman average). So F11's "later continuum reduction" is now sourced: Tzou 1995 (15) = SECONDARY printed continuum GK law; GK 1966 = primary for the Boltzmann-derived structure. Tzou's (17) shows DPL (tau_T = 9 tau_N/5) is a stretched-time image of GK, not an independent postulate in the phonon case.

## ORDERS
BRAVE: add F16-F18 to FULLTEXT_FACTS (GN1992 (3.19-3.20), GN1993 (3.15-3.17), Tzou1995 (15)-(17)) as PRIMARY-SOURCE-CHECKED (supervisor-transcribed); close the "untranscribed" items of B14 #9 for GN 1992 (3.19)-(3.20), GN 1993 (3.15)-(3.17), Tzou 1995 (15)-(17); sections 4.5/4.6/4.7 can now be signed off on these equations (not on the GN 1993 identity (4.15), still untranscribed). Re-check EQ-044/045/098/120 and EQ-047/099 against the printed forms, list any whose verdict changes.
ARENA (after CI work): write GN-II/III and GK sections from F16-F18; GK law quoted as Tzou (15) with source tag SECONDARY; GK 1966 for structure and lambda^2.
