#!/usr/bin/env python3
"""B22 -- independent re-derivation of the Section 10 (v1.1) 1D welded interface.

Written from the physics, before/independently of reading
phase5/verification/verify_interface_energy.py. Two purposes:

 1. reproduce the amplitudes, flux-weighted power ratios, and the lossless
    closure R + T = 1;
 2. show exactly which part of the printed claim is mathematics and which part
    is bookkeeping-by-definition.

Conventions: e^{-i w t}, displacement u, stress sigma = rho c^2 du/dx,
time-averaged mechanical flux <J> = -1/2 Re[sigma * conj(v)].
Run: python3 B22_derivation.py
"""
import sympy as sp

x, t, w = sp.symbols('x t omega', real=True, positive=True)
Z1, Z2, k1, k2 = sp.symbols('Z1 Z2 k1 k2', positive=True, real=True)
Ai, Ar, At = sp.symbols('A_i A_r A_t', real=True)

# ---------- 1. fields and the two matching conditions --------------------
u1 = Ai * sp.exp(sp.I*(k1*x - w*t)) + Ar * sp.exp(sp.I*(-k1*x - w*t))
u2 = At * sp.exp(sp.I*(k2*x - w*t))
s1 = (Z1*w*sp.I*Ai*sp.exp(sp.I*(k1*x - w*t))          # forward:  sigma = +i w Z u
      - Z1*w*sp.I*Ar*sp.exp(sp.I*(-k1*x - w*t)))      # backward: sigma = -i w Z u
s2 = Z2*w*sp.I*At*sp.exp(sp.I*(k2*x - w*t))
# continuity at x = 0: u1 = u2 and sigma1 = sigma2
eq_disp = sp.Eq(u1.subs(x, 0), u2.subs(x, 0))
eq_trac = sp.Eq(s1.subs(x, 0), s2.subs(x, 0))
sol = sp.solve([sp.expand(eq_disp), sp.expand(eq_trac)], [Ar, At], simplify=True)
r = sp.simplify(sol[Ar]/Ai)
tt = sp.simplify(sol[At]/Ai)
assert sp.simplify(r - (Z1 - Z2)/(Z1 + Z2)) == 0
assert sp.simplify(tt - 2*Z1/(Z1 + Z2)) == 0
print("amplitudes: r =", r, "  t =", tt)

# ---------- 2. fluxes derived, not postulated -----------------------------
def mean_flux(u_field, Z, sgn=+1):
    v = sp.diff(u_field, t)
    sig = sgn*Z*w*sp.I*u_field
    return sp.simplify(-sp.Rational(1, 2)*sp.re(sp.simplify(sig*sp.conjugate(v))))

J_inc = mean_flux(Ai*sp.exp(sp.I*(k1*x - w*t)), Z1)
J_ref = mean_flux(Ar*sp.exp(sp.I*(-k1*x - w*t)), Z1, sgn=-1)   # -x direction
J_tr = mean_flux(At*sp.exp(sp.I*(k2*x - w*t)), Z2)
print("fluxes:  J_inc =", J_inc, " J_ref =", J_ref, " J_tr =", J_tr)
assert sp.simplify(J_inc - Z1*w**2*Ai**2/2) == 0
assert sp.simplify(J_ref + Z1*w**2*Ar**2/2) == 0   # -x travelling wave: negative x-flux
assert sp.simplify(J_tr - Z2*w**2*At**2/2) == 0

R = sp.simplify((-J_ref/J_inc).subs(Ar, r*Ai))    # reflected power ratio
T = sp.simplify((J_tr/J_inc).subs(At, tt*Ai))
assert sp.simplify(R + T - 1) == 0
print("power ratios: R =", sp.simplify(R), " T =", sp.simplify(T), " R+T-1 = 0  [PASS]")

# ---------- 3. the cross term, stated honestly ----------------------------
# total field on side 1: instantaneous flux is NOT the sum of the modal ones.
u_tot = Ai*sp.exp(sp.I*(k1*x - w*t)) + Ar*sp.exp(sp.I*(-k1*x - w*t))
sig_tot = (Z1*w*sp.I*Ai*sp.exp(sp.I*(k1*x - w*t)) - Z1*w*sp.I*Ar*sp.exp(sp.I*(-k1*x - w*t)))
J_inst_tot = -sp.Rational(1, 2)*sp.re(sp.simplify(sig_tot*sp.conjugate(sp.diff(u_tot, t))))
J_modes = (J_inc - Z1*w**2*Ar**2/2)
cross = sp.simplify(J_inst_tot - J_modes)
print("cross term (time-averaged total flux minus modal sum):", cross)
assert sp.simplify(cross) == 0, "time-averaged cross term must vanish"
# ... but the cross term is NOT identically zero before time averaging:
cross_inst = sp.simplify(sig_tot*sp.conjugate(sp.diff(u_tot, t))
                         - (Z1*w*sp.I*Ai*sp.exp(sp.I*(k1*x - w*t)))*sp.conjugate(
                             sp.diff(Ai*sp.exp(sp.I*(k1*x - w*t)), t))
                         - (Z1*w*sp.I*Ar*sp.exp(sp.I*(-k1*x - w*t)))*sp.conjugate(
                             sp.diff(Ar*sp.exp(sp.I*(-k1*x - w*t)), t)))
print("cross term before Re[-]/2 and time averaging:", sp.simplify(cross_inst))
assert sp.simplify(cross_inst) != 0
print("NOTE: cancellation is a property of the TIME-AVERAGED flux for real Z and")
print("      co-linear (same-medium) k. It is not an instantaneous identity.")

# why the naive 'check' Re(z - conj(z)) == 0 proves nothing:
z = sp.symbols('z', complex=True)
print("Re(z-conj(z)) =", sp.simplify(sp.re(z - sp.conjugate(z))),
      "-> identically zero for ANY complex z: a vacuous test of the cross term.")

# ---------- 4. control-volume split (bookkeeping vs physics) --------------
I, Rf, Tf, JL, JR = sp.symbols('P_i P_r P_t J_L J_R', real=True)
D_L = I - Rf - JL
D_S = JL - JR
D_R = JR - Tf
print("\ncontrol volume: P_i = P_r + P_t + D_L + D_S + D_R :",
      sp.simplify((Rf + Tf + D_L + D_S + D_R) - I) == 0,
      "<- true BY DEFINITION of D_L, D_S, D_R (no physics assumed)")
A_remote = sp.simplify(I - Rf - Tf)
print("1 - R - T = D_L + D_S + D_R :", sp.simplify(A_remote - (D_L + D_S + D_R)) == 0)
print("A_int = D_S/P_i requires reading J_inc as the NET incident flux P_i:")
print("  (J1_tot - J2_tot)/J_inc = (J_L - J_R)/P_i only when J_inc == P_i.")

# ---------- 5. remote-plane loss for a lossy left half-space -------------
al, L = sp.symbols('alpha_att L', positive=True)
rz = sp.symbols('r_z', positive=True)
remote_loss = sp.simplify(4*rz*(sp.exp(2*al*L) - 1)*sp.exp(-2*al*L)/(rz + 1)**2)
print("\nremote-plane absorption for attenuation alpha over length L:", remote_loss)
print("\nSUMMARY: 1D lossless welded interface reproduced; closure is algebraic;")
print("cross-term cancellation is time-averaged-only; control-volume split is definitional.")
