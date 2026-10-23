#!/usr/bin/env python3
"""
V-B3d — COUPLED thermoelastic interface at normal incidence, 1-D.

Problem
-------
Two thermoelastic half-spaces in perfect contact at x = 0:
    continuity of displacement u, traction sigma, temperature theta, normal heat flux q.
A longitudinal wave (the quasi-elastic branch of the coupled system) is incident from medium 1.
Each side carries TWO modes (quasi-elastic + quasi-thermal) with COMPLEX wavenumbers.

Unknowns: r_e, r_t (reflected elastic, thermal), t_e, t_t (transmitted elastic, thermal) -> 4.
Conditions: [u]=0, [sigma]=0, [theta]=0, [q]=0 -> 4.  Determined.

Energy flux (time-averaged), stated convention
---------------------------------------------
Stress is TENSILE-positive and the surface normal is +x, so the power per unit area is sigma*v and
    J = (1/2) Re[ sigma_hat * conj(v_hat) ] + (1/(2 T0)) Re[ theta_hat * conj(q_hat) ]
The second term is (theta/T0)*q, NOT q: the time average of a single harmonic q is zero, and the
transported thermal energy is the QUADRATIC product.  With compressive-positive stress
sigma_c = -sigma this reads J = -sigma_c*v + q/T0, i.e. the "q - sigma*v" form quoted in the order,
up to the T0 normalisation.  Both forms are the same quantity; the convention is stated once here.

R and T are computed from the TOTAL flux on each side (cross terms included), not mode by mode:
    R = (J_i - J_side1_total)/J_i ,  T = J_side2_total/J_i ,  A = 1 - R - T
J_side1_total includes the incident/reflected cross terms; J_side2_total includes the
elastic/thermal cross terms.  With attenuated waves the flux of a sum is NOT the sum of fluxes,
which is exactly why this must be done with total fields.

Independent check (the real one; A = 1-R-T alone is an identity)
---------------------------------------------------------------
The transmitted energy must all be dissipated in medium 2, and the reflected energy in medium 1:
    int_0^inf <D> dx  ==  T * J_i          (medium 2)
    int_-inf^0 <D> dx ==  R * J_i          (medium 1, reflected modes only)
with <D> = (k_th/(2 T0^2)) |d theta_hat/dx|^2   for Biot and LS, and <D> = 0 for GN-II.
These integrals are computed analytically from the mode expansion (cross terms included).

Models: Biot, Lord-Shulman, GN-II.  GN-III and MGT are not implemented (see report).
"""
import numpy as np

T0 = 300.0


def material(name, rho, cL, cv, kth, K, alpha_lin, tau0=1e-10, ch=None):
    M = rho * cL ** 2
    beta = 3.0 * K * alpha_lin            # beta = 3 K alpha_linear
    m = dict(name=name, rho=rho, M=M, cv=cv, kth=kth, beta=beta, tau0=tau0, ch=ch)
    m["delta"] = T0 * beta ** 2 / (rho * cv * M)   # thermoelastic coupling parameter
    m["kappa"] = kth / (rho * cv)
    return m


# "steel-like" and "aluminium-like": typical textbook values, used for arithmetic only.
STEEL = material("steel", rho=7800.0, cL=5900.0, cv=460.0, kth=45.0,
                 K=160e9, alpha_lin=12e-6, tau0=1e-10, ch=3000.0)
ALU = material("alu", rho=2700.0, cL=6300.0, cv=900.0, kth=205.0,
               K=76e9, alpha_lin=23e-6, tau0=1e-10, ch=6000.0)


# ------------------------------------------------------------------ dispersion
def k2_roots(model, m, w):
    """Return the two k^2 roots of the coupled determinant (quadratic in x = k^2)."""
    s = -1j * w
    a2, a0 = m["M"], -m["rho"] * w ** 2                       # A(k^2) = M k^2 - rho w^2
    if model == "Biot":
        d2, d0 = m["kth"], -1j * w * m["rho"] * m["cv"]
        b2 = 1j * m["beta"] ** 2 * T0 * w
    elif model == "LS":
        f = 1.0 - 1j * w * m["tau0"]
        d2, d0 = m["kth"], f * (-1j * w * m["rho"] * m["cv"])
        b2 = 1j * m["beta"] ** 2 * T0 * w * f
    elif model == "GN-II":
        kst = m["rho"] * m["cv"] * m["ch"] ** 2
        d2, d0 = kst, -m["rho"] * m["cv"] * w ** 2
        b2 = m["beta"] ** 2 * T0 * w ** 2
    else:
        raise ValueError(model)
    # (a2 x + a0)(d2 x + d0) - b2 x = 0
    c2 = a2 * d2
    c1 = a2 * d0 + a0 * d2 - b2
    c0 = a0 * d0
    return np.roots([c2, c1, c0])


def modes(model, m, w):
    """Two +x-propagating modes: (k, u_hat, theta_hat), each normalised to unit 2-norm."""
    s = -1j * w
    out = []
    for x in k2_roots(model, m, w):
        k = np.sqrt(complex(x))
        if k.imag < 0:
            k = -k
        A = m["M"] * k ** 2 - m["rho"] * w ** 2
        v = np.array([-1j * k * m["beta"], A])     # (u, theta) up to scale; B = +i k beta
        v = v / np.linalg.norm(v)
        out.append((k, v[0], v[1]))
    # order: elastic-like first (larger |u|), thermal-like second
    out.sort(key=lambda t: -abs(t[1]))
    return out


# ------------------------------------------------------------------ field quantities
def sigma_of(model, m, w, k, u, th):
    return m["M"] * (1j * k) * u - m["beta"] * th


def q_of(model, m, w, k, th):
    s = -1j * w
    if model in ("Biot", "LS"):
        return -1j * k * m["kth"] * th
    kst = m["rho"] * m["cv"] * m["ch"] ** 2
    return -1j * k * kst * (th / s)          # q = -k* d(alpha)/dx , alpha_hat = theta_hat/s


def flux(model, m, w, k, u, th):
    """Time-averaged normal energy flux of one mode (J > 0 towards +x)."""
    v = -1j * w * u
    sig = sigma_of(model, m, w, k, u, th)
    J = -0.5 * np.real(sig * np.conj(v))          # flux = -sigma*u_t  (tensile-positive sigma)
    if model in ("Biot", "LS"):
        q = q_of(model, m, w, k, th)
        J += 0.5 * np.real(th * np.conj(q)) / T0
    else:
        kst = m["rho"] * m["cv"] * m["ch"] ** 2
        s = -1j * w
        dalpha = 1j * k * (th / s)
        J += -0.5 * kst * np.real(th * np.conj(dalpha)) / T0      # S_th = -(k*/T0) theta grad(alpha)
    return J


def flux_total(model, m, w, kmodes, amps):
    """Flux of a SUM of modes on the same side (cross terms included)."""
    # amplitudes MUST be applied here, otherwise the cross terms are unweighted
    v = [-1j * w * a[0] * a[1] for a in amps]
    sig = [sigma_of(model, m, w, k, a[0] * a[1], a[0] * a[2]) for k, a in zip(kmodes, amps)]
    th = [a[0] * a[2] for a in amps]
    if model in ("Biot", "LS"):
        q = [q_of(model, m, w, k, a[0] * a[2]) for k, a in zip(kmodes, amps)]
    J = 0.0
    for i in range(len(amps)):
        for j in range(len(amps)):
            J += -0.5 * np.real(sig[i] * np.conj(v[j]))
            if model in ("Biot", "LS"):
                J += 0.5 * np.real(th[i] * np.conj(q[j])) / T0
            else:
                kst = m["rho"] * m["cv"] * m["ch"] ** 2
                s = -1j * w
                dalpha = 1j * kmodes[j] * (th[j] / s)
                J += -0.5 * kst * np.real(th[i] * np.conj(dalpha)) / T0
    return J


def flux_diag(model, m, w, kmodes, amps):
    """Sum of the individual mode fluxes, cross terms DROPPED (the usual literature definition)."""
    return sum(flux(model, m, w, k, a[0] * a[1], a[0] * a[2]) for k, a in zip(kmodes, amps))


def dissipation_integral(model, m, w, kmodes, amps, sign_side):
    """int <D> dx over the side, <D> = (k_th/(2T0^2))|dtheta/dx|^2 (0 for GN-II)."""
    if model == "GN-II":
        return 0.0
    coef = m["kth"] / (2.0 * T0)
    if model == "LS":
        # LS flux is q_hat = -k grad(theta)/(1 - i w tau0), so the time-averaged dissipation
        # carries Re[1/(1 - i w tau0)] = 1/(1 + w^2 tau0^2).  Using the Fourier normalisation
        # here instead over-predicts D by exactly that factor -- which is what the first run showed.
        coef = coef / (1.0 + (w * m["tau0"]) ** 2)
    a = [1j * k * t[0] * t[2] for k, t in zip(kmodes, amps)]     # dtheta/dx amplitudes (weighted)
    tot = 0.0 + 0.0j
    for i in range(len(a)):
        for j in range(len(a)):
            d = kmodes[i] - np.conj(kmodes[j])
            if abs(d) < 1e-300:
                continue
            integ = (-1.0 / (1j * d)) if sign_side > 0 else (1.0 / (1j * d))
            tot += a[i] * np.conj(a[j]) * integ
    return coef * tot.real


# ------------------------------------------------------------------ interface solve
def solve(model, m1, m2, w):
    md1, md2 = modes(model, m1, w), modes(model, m2, w)
    (k1e, u1e, t1e), (k1t, u1t, t1t) = md1
    (k2e, u2e, t2e), (k2t, u2t, t2t) = md2
    # incident: elastic-like mode of medium 1 travelling +x, unit amplitude
    J_i = flux(model, m1, w, k1e, u1e, t1e)

    # reflected branches: wavenumber -k AND the matching eigenvector, which has u -> -u
    # (A = M k^2 - rho w^2 is even in k, while B = -i k beta is odd, so u = -B theta / A flips)
    ref = [(-k1e, -u1e, t1e), (-k1t, -u1t, t1t)]
    trn = [(k2e, u2e, t2e), (k2t, u2t, t2t)]

    def row(kind, k, u, th, m):
        if kind == "u":
            return u
        if kind == "s":
            return sigma_of(model, m, w, k, u, th)
        if kind == "t":
            return th
        return q_of(model, m, w, k, th)

    A = np.zeros((4, 4), dtype=complex)
    rhs = np.zeros(4, dtype=complex)
    for r, kind in enumerate(("u", "s", "t", "q")):
        for c in range(2):
            A[r, c] = row(kind, ref[c][0], ref[c][1], ref[c][2], m1)
            A[r, 2 + c] = -row(kind, trn[c][0], trn[c][1], trn[c][2], m2)
        rhs[r] = -row(kind, k1e, u1e, t1e, m1)
    scale = np.abs(A).max(axis=1)
    A = A / scale[:, None]
    rhs = rhs / scale
    sol = np.linalg.solve(A, rhs)
    res = np.abs(A @ sol - rhs).max()

    r_e, r_t, t_e, t_t = sol
    # total field side 1 = incident + reflected
    k1 = [k1e, ref[0][0], ref[1][0]]
    a1 = [(1.0, u1e, t1e), (r_e, ref[0][1], ref[0][2]), (r_t, ref[1][1], ref[1][2])]
    J1 = flux_total(model, m1, w, k1, a1)
    k2 = [trn[0][0], trn[1][0]]
    a2 = [(t_e, trn[0][1], trn[0][2]), (t_t, trn[1][1], trn[1][2])]
    J2 = flux_total(model, m2, w, k2, a2)

    R = (J_i - J1) / J_i
    T = J2 / J_i
    A_ = 1.0 - R - T

    # mode-projected coefficients (no cross terms): what the reflected/transmitted modes
    # actually carry away, as opposed to the total-field flux
    aref = [(r_e, ref[0][1], ref[0][2]), (r_t, ref[1][1], ref[1][2])]
    kref = [ref[0][0], ref[1][0]]
    R_mode = -flux_diag(model, m1, w, kref, aref) / J_i      # diagonal only
    R_ref = -flux_total(model, m1, w, kref, aref) / J_i      # reflected SUM, cross terms kept
    T_diag = flux_diag(model, m2, w, k2, a2) / J_i

    # independent dissipation checks (reflected modes only on side 1)
    D2 = dissipation_integral(model, m2, w, k2, a2, +1)
    D1 = dissipation_integral(model, m1, w, kref, aref, -1)

    # ratio of thermal to elastic wavenumber magnitude, for the "coupling" column
    ratio = abs(k1t) / abs(k1e)
    return dict(R=R, T=T, A=A_, R_mode=R_mode, R_ref=R_ref, T_diag=T_diag, J_i=J_i, J1=J1, J2=J2,
                res=res, D1=D1, D2=D2,
                chk2=D2 / (T * J_i) if T != 0 else np.nan,
                chk1=D1 / (R_ref * J_i) if R_ref != 0 else np.nan,
                ratio=ratio, r=(r_e, r_t), t=(t_e, t_t), k1e=k1e, k1t=k1t)


def main():
    print("=" * 96)
    print("V-B3d  COUPLED thermoelastic interface, normal incidence (steel | aluminium)")
    print("=" * 96)
    print(f"T0={T0} K")
    for m in (STEEL, ALU):
        print(f"  {m['name']:9s} rho={m['rho']:.0f} cL={np.sqrt(m['M']/m['rho']):.0f} m/s "
              f"beta={m['beta']:.3e} Pa/K delta={m['delta']:.4f} kappa={m['kappa']:.3e} m^2/s")

    print("\n[1] COUPLED INTERFACE, steel | aluminium -- THREE distinct reflection coefficients")
    print("    R_flux : from the TOTAL field on side 1 (incident+reflected, all cross terms)")
    print("    R_ref  : reflected modes as a SUM (intra-side cross terms kept, incident removed)")
    print("    R_mode : sum of individual reflected mode fluxes (diagonal only = what papers square)")
    print("    With complex k NONE of these sums to 1 exactly: R+T-1 is the interference term,")
    print("    which vanishes identically only in the lossless case (see GN-II row).")
    hdr = (f"    {'model':6s} {'f[Hz]':>8s} {'R_flux':>9s} {'R_ref':>9s} {'R_mode':>9s} "
           f"{'T':>9s} {'A_flux':>9s} {'Rref+T-1':>9s} {'Rmode+T-1':>10s} {'|kt|/|ke|':>9s} "
           f"{'D2chk':>8s} {'D1chk':>8s}")
    print(hdr)
    for model in ("Biot", "LS", "GN-II"):
        for f in (1e6, 1e8, 1e10, 1e11, 4.46e11, 1e12):
            d = solve(model, STEEL, ALU, 2 * np.pi * f)
            c2 = np.nan if model == "GN-II" else d["chk2"]
            c1 = np.nan if model == "GN-II" else d["chk1"]
            print(f"    {model:6s} {f:8.2e} {d['R']:9.6f} {d['R_ref']:9.6f} {d['R_mode']:9.6f} "
                  f"{d['T']:9.6f} {d['A']:9.2e} {d['R_ref']+d['T']-1:9.1e} "
                  f"{d['R_mode']+d['T']-1:10.2e} {d['ratio']:9.3e} {c2:8.5f} {c1:8.5f}")
        print()

    print("[2] WHERE ARE THE MODES STRONGLY COUPLED?  (ratio |k_thermal|/|k_elastic| = 1)")
    for model in ("Biot", "LS"):
        f_lo, f_hi = 1e6, 1e15
        r_lo = solve(model, STEEL, ALU, 2 * np.pi * f_lo)["ratio"]
        r_hi = solve(model, STEEL, ALU, 2 * np.pi * f_hi)["ratio"]
        if (r_lo - 1) * (r_hi - 1) > 0:
            print(f"      {model}: no crossing in [1e6, 1e15] Hz "
                  f"(ratio {r_lo:.3e} -> {r_hi:.3e}); modes never have equal wavelength")
        else:
            for _ in range(200):
                mid = np.sqrt(f_lo * f_hi)
                if solve(model, STEEL, ALU, 2 * np.pi * mid)["ratio"] > 1:
                    f_lo = mid
                else:
                    f_hi = mid
            print(f"      {model}: f ~ {f_lo:.3e} Hz  (thermal wavelength == elastic wavelength)")

    print("\n[3] SAME MEDIUM ON BOTH SIDES (must give R=0, T=1, A=0)")
    for model in ("Biot", "LS", "GN-II"):
        d = solve(model, STEEL, STEEL, 2 * np.pi * 1e8)
        print(f"    {model:6s} R={d['R']:+.3e} T={d['T']:.9f} A={d['A']:+.3e} "
              f"res={d['res']:.1e}")

    print("\n[4] GN-II IS LOSSLESS: dissipation integrals must vanish and A must be 0")
    d = solve("GN-II", STEEL, ALU, 2 * np.pi * 1e10)
    print(f"    D2={d['D2']:+.3e}  D1={d['D1']:+.3e}  J1={d['J1']:.6e}  J2={d['J2']:.6e}  "
          f"J1-J2={d['J1']-d['J2']:+.3e}  (lossless: flux conserved, nothing dissipated)")

    print("\n[5] LS DISCRIMINATION: the Fourier-normalised dissipation check FAILS by 1/(1+w^2 tau0^2)")
    d = solve("LS", STEEL, ALU, 2 * np.pi * 1e10)
    fac = 1.0 / (1.0 + (2 * np.pi * 1e10 * STEEL["tau0"]) ** 2)
    print(f"    at 1e10 Hz: 1/(1+w^2 tau0^2) = {fac:.6f}")
    print(f"    D2 with LS factor / (T Ji) = {d['chk2']:.8f}   (must be 1)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
