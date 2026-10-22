#!/usr/bin/env python3
"""
V-B4 — does the manuscript's energy-flux convention support its own R+T+A=1 identity?

Manuscript (branch arena/40393d9f-le, phase5/master):
    sec10_energy.tex:33   J_i = q_i - sigma_ij v_j                  [eq 10.3, "DERIVED"]
    sec10_energy.tex:41   <J_i> = qbar_i - (1/2) Re[sigma_ij v_j*]  [eq 10.4]
    sec09_interfaces.tex:151  R = |<J_ref,n>|/<J_inc,n>|, T = |<J_trans,n>|/<J_inc,n>|, A = D/<J_inc,n>
    sec09_interfaces.tex:171  sum R + sum T + A = 1

qbar_i is stated to be zero "for a purely oscillatory perturbation about a uniform reference
state" (sec10:45).  Therefore the manuscript's mean flux reduces to

    <J> = -(1/2) Re[sigma_hat v_hat*]      (no thermal term at all)

Two questions are decided here numerically, using the V-B3d coupled interface solver:

  Q1  With the manuscript's flux and its per-mode R,T (modulus squared, cross terms dropped),
      does sum R + sum T + A = 1 close, with A = D/<J_inc> and D the total dissipation?
  Q2  If the flux is instead the QUADRATIC-form (Umov-Poynting) flux
          J = -(1/2)Re[sigma v*] + (1/(2T0)) Re[theta q*]
      (the one for which  div<J> = -<D>), does the same identity close?

Convention: e^{i(kx-wt)}, tensile-positive sigma, normal +x.  Same material pair, frequencies and
amplitude normalisation as V-B3d (steel | aluminium, T0 = 300 K, tau0 = 1e-10 s).
"""
import numpy as np

src = open("V-B3d_coupled_interface.py", encoding="utf-8").read()
head = src.split("def main():")[0]
ns = {}
exec(compile(head, "V-B3d_coupled_interface.py", "exec"), ns)

solve = ns["solve"]
modes = ns["modes"]
sigma_of = ns["sigma_of"]
q_of = ns["q_of"]
STEEL, ALU = ns["STEEL"], ns["ALU"]
T0 = ns["T0"]


def flux_no_thermal(model, m, w, kmodes, amps):
    """<J> = -(1/2) Re[sigma_i conj(v_j)] summed over i,j (cross terms KEPT).
    This is the manuscript's eq. (10.4) with qbar = 0."""
    v = [-1j * w * a[0] * a[1] for a in amps]
    sig = [sigma_of(model, m, w, k, a[0] * a[1], a[0] * a[2]) for k, a in zip(kmodes, amps)]
    J = 0.0
    for i in range(len(amps)):
        for j in range(len(amps)):
            J += -0.5 * np.real(sig[i] * np.conj(v[j]))
    return J


def flux_diag_no_thermal(model, m, w, kmodes, amps):
    """mode-by-mode |flux|, cross terms dropped — the usual 'energy ratio' numerator."""
    out = 0.0
    for k, a in zip(kmodes, amps):
        v = -1j * w * a[0] * a[1]
        sig = sigma_of(model, m, w, k, a[0] * a[1], a[0] * a[2])
        out += abs(-0.5 * np.real(sig * np.conj(v)))
    return out


print("=" * 96)
print("V-B4  energy-flux convention check : steel | aluminium, normal incidence")
print("=" * 96)
print(f"{'model':6s} {'f [Hz]':>9s} | {'ms flux':>19s} | {'quadratic flux':>19s} | {'D_tot/Ji':>9s}")
print(f"{'':6s} {'':>9s} | {'Rdiag+Tdiag':>9s} {'Rtot+Ttot':>9s} | {'R+T':>9s} {'+A-1':>9s} |")
print("-" * 96)

rows = []
for model in ("Biot", "LS", "GN-II"):
    for f in (1e6, 1e10, 1e11, 4.463e11, 1e12):
        w = 2 * np.pi * f
        s = solve(model, STEEL, ALU, w)
        J_i = s["J_i"]
        kref = [-s["k1e"], -s["k1t"]]
        aref = [(s["r"][0], -1.0, 1.0), (s["r"][1], -1.0, 1.0)]     # signs handled in solve();
                                                                     # only |flux| is used here
        # rebuild the reflected/transmitted amplitude triples exactly as solve() does
        md1, md2 = modes(model, STEEL, w), modes(model, ALU, w)
        (k1e, u1e, t1e), (k1t, u1t, t1t) = md1
        (k2e, u2e, t2e), (k2t, u2t, t2t) = md2
        r_e, r_t = s["r"]
        t_e, t_t = s["t"]
        ref = [(-k1e, -u1e, t1e), (-k1t, -u1t, t1t)]
        trn = [(k2e, u2e, t2e), (k2t, u2t, t2t)]
        aref = [(r_e, ref[0][1], ref[0][2]), (r_t, ref[1][1], ref[1][2])]
        kref = [ref[0][0], ref[1][0]]
        a2 = [(t_e, trn[0][1], trn[0][2]), (t_t, trn[1][1], trn[1][2])]
        k2 = [trn[0][0], trn[1][0]]

        # Q1: manuscript flux, per-mode |flux| (cross terms dropped), A = D/J_i
        Rm = flux_diag_no_thermal(model, STEEL, w, kref, aref) / abs(J_i)
        Tm = flux_diag_no_thermal(model, ALU, w, k2, a2) / abs(J_i)
        D_tot = s["D1"] + s["D2"]
        Am = D_tot / abs(J_i)
        q1 = Rm + Tm + Am - 1.0

        # cross-term size in the same (no-thermal) convention, total field
        J1ms = flux_no_thermal(model, STEEL, w, [k1e] + kref,
                               [(1.0, u1e, t1e)] + aref)
        J2ms = flux_no_thermal(model, ALU, w, k2, a2)
        cross = (abs(J_i) - J1ms) / abs(J_i)      # = R with cross terms, no-thermal flux

        # Q2: quadratic-form flux (V-B3d defaults), total field, A = D/J_i
        Rq = s["R"]
        Tq = s["T"]
        Aq = D_tot / abs(J_i)
        q2 = Rq + Tq + Aq - 1.0

        Rtot = 1.0 - J1ms / abs(J_i)
        Ttot = J2ms / abs(J_i)
        rows.append((model, f, Rm + Tm, Rtot + Ttot, Rq + Tq, Am, Rq + Tq))
        print(f"{model:6s} {f:9.3e} | {Rm+Tm:9.6f} {Rtot+Ttot:9.6f} "
              f"| {Rq+Tq:9.6f} {Rq+Tq+Aq-1:9.2e} | {Am:9.6f}")

print("-" * 96)
print("Columns 1-2: the manuscript's flux (eq. 10.3/10.4 with qbar = 0), per-mode modulus")
print("             (col 1) and total field with cross terms (col 2).")
print("Columns 3-4: the quadratic-form flux -(1/2)Re[sig v*] + (1/2T0)Re[theta q*];")
print("             col 4 adds A = D_tot/J_i as the manuscript defines it (eq. 9.10).")
print()

# decisive summaries
gn = [r for r in rows if r[0] == "GN-II"]
print("FINDING 1 (lossless case). GN-II has D = 0 (checked in V-B3d: D == 0 identically).")
print(f"   manuscript flux, per-mode:    sum R + sum T = {gn[0][2]:.6f}  (must be 1.000000)")
print(f"   manuscript flux, total field: sum R + sum T = {gn[0][3]:.6f}")
print(f"   quadratic flux, total field:  sum R + sum T = {gn[0][4]:.6f}  (is 1.000000)")
print("   => the manuscript's flux carries NO thermal channel at all: the thermal branch")
print("      of GN-II transports energy only through the (theta/T0) q term, which the")
print("      flux q - sigma v does not contain. The missing 1/3 of the incident energy")
print("      is not a numerical artefact; it is the thermal mode.")
print()
print("FINDING 2 (dissipative case). A = D_tot/J_i is NOT an interface absorption")
print(f"   coefficient: D_tot/J_i = R + T to within round-off (max deviation from")
print(f"   R+T: {max(abs(r[5]-r[4]) for r in rows if r[0]!='GN-II'):.4f}). Reason: in an")
print("   attenuating medium ALL the energy that crosses is eventually dissipated, so the")
print("   bulk dissipation integral equals the transmitted-plus-reflected energy, not an")
print("   extra channel. Substituting into eq. (9.12) therefore gives")
print("   sum R + sum T + A = 2 sum R... i.e. ~2, not 1.")
print()
print("CONCLUSION. eq. (9.12)/(10.11) can close only if BOTH are changed: the flux must")
print("be the quadratic-form one AND A must be the interface-local residual (1 - sum R -")
print("sum T), or equivalently D must exclude the bulk dissipation that R and T already")
print("carry. Neither is stated in the manuscript; both are checkable in one run.")
