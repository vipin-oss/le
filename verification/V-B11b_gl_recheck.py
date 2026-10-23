#!/usr/bin/env python3
"""
V-B11b — Green–Lindsay recomputed from the PRIMARY system (BRAVE_B11 condition 2).

Primary text (relayed by the supervisor from J. Elasticity 2:1-7, sec. 4):
    sigma_ij = 2 mu e_ij + [lambda e_kk - beta (T + tau1 T_dot)] delta_ij     (4.11)/(4.13)
    q_i = -k theta_,i                                    (FOURIER, no flux relaxation)
    k lap T = rho c_E (T_dot + tau0 T_ddot) + beta T0 e_dot_kk        (4.13)
      -- the STRAIN-RATE COUPLING CARRIES NO tau0
    tau1 >= tau0 > 0                                      (4.14)/(4.16)

The manuscript's eq (4.9) is the same energy equation WITH tau0 also on the coupling term
(beta T0 (u_dot_ii + tau0 u_ddot_ii)); the supervisor's finding F1 is that this is a variant,
not Green-Lindsay 1972. Both are run here so the size of the difference is measured.

Harness: same 1-D normal-incidence coupled interface as V-B3d (steel | aluminium, perfect
contact). The Biot branch must reproduce V-B3d's frozen numbers, which validates the harness.

Convention: e^{i(kx - w t)}, tensile-positive sigma, J = -<sigma v> + <theta q>/T0.
"""
import numpy as np

T0 = 300.0


def material(name, rho, cL, cv, kth, K, alpha_lin, tau0, tau1):
    M = rho * cL ** 2
    beta = 3.0 * K * alpha_lin
    return dict(name=name, rho=rho, M=M, cv=cv, kth=kth, beta=beta,
                tau0=tau0, tau1=tau1, kappa=kth / (rho * cv))


STEEL = material("steel", 7800.0, 5900.0, 460.0, 45.0, 160e9, 12e-6, 1e-10, 5e-10)
ALU = material("alu", 2700.0, 6300.0, 900.0, 205.0, 76e9, 23e-6, 1e-10, 5e-10)
# tau1 = 5e-10 > tau0 = 1e-10: GL's own ordering (4.14)/(4.16).


def k2_roots(model, m, w):
    """Quadratic in x = k^2 of the coupled determinant (same bookkeeping as V-B3d)."""
    A2, A0 = m["M"], -m["rho"] * w ** 2
    f0 = 1.0 - 1j * w * m["tau0"]                    # energy operator (T + tau0 T_dot)
    d2, d0 = m["kth"], -1j * w * m["rho"] * m["cv"] * f0
    if model == "GL":                                # primary: no tau on the coupling
        fc = 1.0
    elif model == "GL_ms":                           # manuscript (4.9): tau0 on coupling
        fc = f0
    elif model == "Biot":
        d0 = -1j * w * m["rho"] * m["cv"]
        fc = 1.0
    else:
        raise ValueError(model)
    b2 = 1j * m["beta"] ** 2 * T0 * w * fc
    return np.roots([A2 * d2, A2 * d0 + A0 * d2 - b2, A0 * d0])


def modes(model, m, w):
    out = []
    for x in k2_roots(model, m, w):
        k = np.sqrt(complex(x))
        if k.imag < 0:
            k = -k
        A = m["M"] * k ** 2 - m["rho"] * w ** 2
        th = A / (1.0 - 1j * w * m["tau1"])           # GL stress time; =A for Biot
        v = np.array([-1j * k * m["beta"], th])
        v = v / np.linalg.norm(v)
        out.append((k, v[0], v[1]))
    out.sort(key=lambda t: -abs(t[1]))
    return out


def sigma_of(model, m, w, k, u, th):
    f1 = 1.0 if model == "Biot" else (1.0 - 1j * w * m["tau1"])
    return m["M"] * (1j * k) * u - m["beta"] * f1 * th


def q_of(model, m, w, k, th):
    return -1j * k * m["kth"] * th                    # GL and Biot: Fourier


def flux_of_one(model, m, w, k, u, th):
    v = -1j * w * u
    return (-0.5 * np.real(sigma_of(model, m, w, k, u, th) * np.conj(v))
            + 0.5 * np.real(th * np.conj(q_of(model, m, w, k, th))) / T0)


def flux_total(model, m, w, kmodes, amps):
    v = [-1j * w * a[0] * a[1] for a in amps]
    sig = [sigma_of(model, m, w, k, a[0] * a[1], a[0] * a[2]) for k, a in zip(kmodes, amps)]
    th = [a[0] * a[2] for a in amps]
    q = [q_of(model, m, w, k, a[0] * a[2]) for k, a in zip(kmodes, amps)]
    J = 0.0
    for i in range(len(amps)):
        for j in range(len(amps)):
            J += -0.5 * np.real(sig[i] * np.conj(v[j])) + 0.5 * np.real(th[i] * np.conj(q[j])) / T0
    return J


def flux_diag(model, m, w, kmodes, amps):
    return sum(flux_of_one(model, m, w, k, a[0] * a[1], a[0] * a[2])
               for k, a in zip(kmodes, amps))


def solve(model, m1, m2, w):
    md1, md2 = modes(model, m1, w), modes(model, m2, w)
    (k1e, u1e, t1e), (k1t, u1t, t1t) = md1
    (k2e, u2e, t2e), (k2t, u2t, t2t) = md2
    J_i = flux_of_one(model, m1, w, k1e, u1e, t1e)     # > 0 towards +x
    ref = [(-k1e, -u1e, t1e), (-k1t, -u1t, t1t)]
    trn = [(k2e, u2e, t2e), (k2t, u2t, t2t)]

    rows, rhs = [], []
    for kind in ("u", "s", "t", "q"):
        r = []
        for (k, u, th), m in zip(ref, (m1, m1)):
            if kind == "u":
                r.append(u)
            elif kind == "s":
                r.append(sigma_of(model, m, w, k, u, th))
            elif kind == "t":
                r.append(th)
            else:
                r.append(q_of(model, m, w, k, th))
        for (k, u, th), m in zip(trn, (m2, m2)):
            if kind == "u":
                r.append(-u)
            elif kind == "s":
                r.append(-sigma_of(model, m, w, k, u, th))
            elif kind == "t":
                r.append(-th)
            else:
                r.append(-q_of(model, m, w, k, th))
        val = {"u": u1e, "s": sigma_of(model, m1, w, k1e, u1e, t1e),
               "t": t1e, "q": q_of(model, m1, w, k1e, t1e)}[kind]
        rows.append(r)
        rhs.append(-val)                                # incident moved to the RHS
    amps = np.linalg.solve(np.array(rows, dtype=complex), np.array(rhs, dtype=complex))

    refA = [(ref[0][0], amps[0] * ref[0][1], amps[0] * ref[0][2]),
            (ref[1][0], amps[1] * ref[1][1], amps[1] * ref[1][2])]
    trnA = [(refA and trn[0][0], amps[2] * trn[0][1], amps[2] * trn[0][2]),
            (trn[1][0], amps[3] * trn[1][1], amps[3] * trn[1][2])]
    J1 = flux_total(model, m1, w, [ref[0][0], ref[1][0]], refA)   # reflected sum, incident excluded
    J2 = flux_total(model, m2, w, [trn[0][0], trn[1][0]], trnA)
    R = -J1 / J_i
    Tr = J2 / J_i
    Rmode = -flux_diag(model, m1, w, [ref[0][0], ref[1][0]], refA) / J_i
    return dict(R=R, T=Tr, A=1 - R - Tr, Rmode=Rmode, Ji=J_i,
                kratio=abs(trn[1][0]) / abs(trn[0][0]),
                k1e=k1e, k1t=k1t, k2e=trn[0][0], k2t=trn[1][0], amps=amps)


def main():
    print("=" * 72)
    print("HARNESS VALIDATION: Biot must reproduce V-B3d's frozen row")
    print("  V-B3d @ 4.46e11 Hz : R_flux 0.212026  R_mode 0.211592  T 0.787974")
    d = solve("Biot", STEEL, ALU, 2 * np.pi * 4.46e11)
    print("  this script        : R_flux %.6f  R_mode %.6f  T %.6f  (A = %.2e)"
          % (d["R"], d["Rmode"], d["T"], d["A"]))
    print("=" * 72)

    print("\nGL: dispersion comparison (steel, |k| and branch content)")
    for w_hz in (1e6, 1e8, 1e10, 1e11, 4.46e11, 1e12):
        w = 2 * np.pi * w_hz
        o, ms = modes("GL", STEEL, w), modes("GL_ms", STEEL, w)
        print("  f=%.2e Hz  k_e: GL %.6e%+.6ej | ms %.6e%+.6ej   k_t: GL %.6e%+.6ej | ms %.6e%+.6ej"
              % (w_hz, o[0][0].real, o[0][0].imag, ms[0][0].real, ms[0][0].imag,
                 o[1][0].real, o[1][0].imag, ms[1][0].real, ms[1][0].imag))

    print("\nGL interface: steel | aluminium, perfect contact, normal incidence")
    print("  %-10s %-9s %-9s %-9s %-11s %-9s" %
          ("f [Hz]", "R_GL", "R_ms(4.9)", "dR", "T_GL", "T_ms"))
    for w_hz in (1e6, 1e8, 1e10, 1e11, 4.46e11, 1e12):
        w = 2 * np.pi * w_hz
        a = solve("GL", STEEL, ALU, w)
        b = solve("GL_ms", STEEL, ALU, w)
        print("  %-10.2e %-9.6f %-9.6f %+.2e %-11.6f %-9.6f"
              % (w_hz, a["R"], b["R"], a["R"] - b["R"], a["T"], b["T"]))
        print("             A = %.2e (GL)  %.2e (ms)   R_mode %.6f / %.6f   |k_t|/|k_e| %.4f / %.4f"
              % (a["A"], b["A"], a["Rmode"], b["Rmode"], a["kratio"], b["kratio"]))

    print("\nLIMIT CHECKS")
    w = 2 * np.pi * 1e11
    gl = solve("GL", STEEL, ALU, w)
    bi = solve("Biot", STEEL, ALU, w)
    print("  GL with tau0=tau1=0 must equal Biot:")
    m0 = dict(STEEL); m0["tau0"] = 0.0; m0["tau1"] = 0.0
    m0b = dict(ALU); m0b["tau0"] = 0.0; m0b["tau1"] = 0.0
    z = solve("GL", m0, m0b, w)
    print("    GL(0,0) R = %.9f  T = %.9f | Biot R = %.9f  T = %.9f"
          % (z["R"], z["T"], bi["R"], bi["T"]))

    print("\n  GL at tau1 = tau0 is NOT Lord-Shulman (different energy coupling). Check:")
    meq = dict(STEEL); meq["tau1"] = meq["tau0"]
    meqb = dict(ALU); meqb["tau1"] = meqb["tau0"]
    g = solve("GL", meq, meqb, w)
    ls = solve("GL_ms", meq, meqb, w)
    print("    GL(tau1=tau0) R = %.6f T = %.6f | manuscript-variant R = %.6f T = %.6f"
          % (g["R"], g["T"], ls["R"], ls["T"]))
    print("    (they coincide only because the ms variant with tau1=tau0 differs from GL only")
    print("     in the coupling operator; see the dispersion table for the actual split)")

    print("\n  rigid GL thermal speed: c_h = sqrt(kappa/tau0) = %.4f m/s (unchanged by the coupling)"
          % np.sqrt(STEEL["kappa"] / STEEL["tau0"]))


if __name__ == "__main__":
    main()
