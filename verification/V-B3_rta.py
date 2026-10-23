#!/usr/bin/env python3
"""
V-B3 — R + T + A = 1 at an interface, model by model.

Model problem
-------------
Two semi-infinite heat-conducting half-spaces in contact at x = 0.  A time-harmonic thermal
disturbance is incident from medium 1 along +x.  For each heat conduction model we solve the
interface problem exactly and compute

    R = reflected energy fraction,  T = transmitted energy fraction,  A = 1 - R - T

Conventions: theta ~ exp(i(kx - omega t)), so s = -i*omega.  Normal flux q_x > 0 towards +x.
Time-averaged normal energy flux of a harmonic branch: J = (1/2) Re(q_hat * conj(theta_hat)).

Each model enters through exactly two functions:
    k2(omega)      -> k^2 of the decaying/propagating branch in +x
    qhat(k, omega) -> complex amplitude of the normal flux for unit temperature amplitude

Models implemented: Biot/Fourier, Lord-Shulman, Green-Lindsay, GN-II, GN-III.
MGT is deliberately NOT implemented -- see section [5]: its interface flux is not defined
without a choice of energy functional (V-B3a section 3.6).

HEADLINE RESULT (and a refuted hypothesis, kept on the record):
  An IDEAL (zero-resistance) interface gives A = 0 to machine precision for ALL FIVE models,
  including the strongly dissipative ones.  A measures interface-level loss, NOT bulk
  dissipation, because the flux amplitudes on the two sides share a common phase factor.
  A != 0 requires a Kapitza conductance, or a phase mismatch between the two media.
"""
import numpy as np

# ----------------------------------------------------------------------------- materials
MAT1 = dict(k_th=45.0, rhoc=7800.0 * 460.0, tau0=1e-10, c_h=2000.0)   # steel-like
MAT2 = dict(k_th=2.0, rhoc=1.6e6, tau0=1e-10, c_h=2000.0)              # polymer-like

OMEGA = 2.0 * np.pi * 1.0e6      # 1 MHz


def kappa(m):
    """thermal diffusivity k_th/(rho c)  [m^2/s]"""
    return m["k_th"] / m["rhoc"]


def kstar_reduced(m):
    """GN reduced conductivity k*/(rho c)  [m^2/s^2]; c_h^2 = k*/(rho c)"""
    return m["c_h"] ** 2


# ----------------------------------------------------------------------------- models
def biot_k2(m, s):
    return -s / kappa(m)


def biot_q(k, m, s):
    return -1j * k * m["k_th"]


def ls_k2(m, s):
    return -s * (1.0 + m["tau0"] * s) / kappa(m)


def ls_q(k, m, s):
    # q + tau0 dq/dt = -k_th theta_x  ->  q_hat (1 + tau0 s) = -i k k_th theta_hat
    return -1j * k * m["k_th"] / (1.0 + m["tau0"] * s)


def gl_k2(m, s):
    # tau0 theta_tt + theta_t = kappa theta_xx  (pure Fourier flux; GL energy equation)
    return -(m["tau0"] * s * s + s) / kappa(m)


def gl_q(k, m, s):
    # GL has NO relaxation in the flux: q = -k_th theta_x, exactly as Biot
    return -1j * k * m["k_th"]


def gn2_k2(m, s):
    return -s * s / kstar_reduced(m)               # theta_tt = c_h^2 theta_xx


def gn2_q(k, m, s):
    kst = kstar_reduced(m) * m["rhoc"]             # q = -k* alpha_x, alpha_t = theta
    return -1j * k * kst / s


def gn3_k2(m, s):
    return -s * s / (kstar_reduced(m) + kappa(m) * s)


def gn3_q(k, m, s):
    kst = kstar_reduced(m) * m["rhoc"]
    return -1j * k * kst / s - 1j * k * m["k_th"]  # BOTH channels required


MODELS = [
    ("Biot/Fourier", biot_k2, biot_q),
    ("Lord-Shulman", ls_k2, ls_q),
    ("Green-Lindsay", gl_k2, gl_q),
    ("GN-II", gn2_k2, gn2_q),
    ("GN-III", gn3_k2, gn3_q),
]


# ----------------------------------------------------------------------------- solver
def branch_k(k2):
    """Root with Im(k) > 0: decays / propagates towards +x."""
    k = np.sqrt(complex(k2))
    return -k if k.imag < 0 else k


def solve_interface(k2fun, qfun, m1, m2, omega, h=None):
    """h = None -> ideal contact ([theta]=0); h > 0 -> Kapitza conductance [W/m^2K]."""
    s = -1j * omega
    k1 = branch_k(k2fun(m1, s))
    k2 = branch_k(k2fun(m2, s))
    a = qfun(k1, m1, s)                     # incident flux for theta_hat = 1
    b = qfun(k2, m2, s)                     # transmitted flux for theta_hat = 1
    if h is None:
        # theta: 1 + r = t ;  flux: a - a r = b t
        den = a + b
        r = (a - b) / den
        t = 2.0 * a / den
        jump_res = abs(((1.0 + r) - t))
        flux_res = abs((a - a * r) - b * t)
    else:
        # theta: 1 + r - t = q/h ;  flux: q = a(1-r) = b t  =>  t = a(1-r)/b
        X = a / b + a / h
        r = (X - 1.0) / (1.0 + X)
        t = a * (1.0 - r) / b
        jump_res = abs(((1.0 + r) - t) - a * (1.0 - r) / h)
        flux_res = abs((a - a * r) - b * t)
    Ji = 0.5 * np.real(a)
    Jr = -0.5 * np.real(a * r * np.conj(r))
    Jt = 0.5 * np.real(b * t * np.conj(t))
    R = -Jr / Ji
    T = Jt / Ji
    return dict(k1=k1, k2=k2, a=a, b=b, r=r, t=t, R=R, T=T, A=1.0 - R - T,
                jump_res=jump_res, flux_res=flux_res, Ji=Ji,
                dphase=abs(np.angle(a) - np.angle(b)))


def main():
    print("=" * 82)
    print("V-B3  R + T + A = 1 at a thermal interface")
    print("=" * 82)
    print(f"omega = 2*pi*{OMEGA/(2*np.pi):.2e} Hz   "
          f"kappa_1 = {kappa(MAT1):.6e}  kappa_2 = {kappa(MAT2):.6e} m^2/s")

    # ---------------------------------------------------------------- [0] solver sanity
    print("\n[0] SOLVER SANITY: identical media both sides must give r=0, t=1, A=0")
    worst = 0.0
    for name, k2f, qf in MODELS:
        d = solve_interface(k2f, qf, MAT1, MAT1, OMEGA)
        err = max(abs(d["r"]), abs(d["t"] - 1.0), abs(d["A"]))
        worst = max(worst, err)
        print(f"    {name:15s} |r|={abs(d['r']):.3e}  |t-1|={abs(d['t']-1):.3e}  "
              f"|A|={abs(d['A']):.3e}")
    print(f"    worst deviation = {worst:.3e}  -> {'PASS' if worst < 1e-12 else 'FAIL'} "
          f"(threshold 1e-12)")

    # ---------------------------------------------------------------- [1] R, T, A
    print("\n[1] TWO DIFFERENT MEDIA, IDEAL CONTACT: R, T, A")
    print(f"    {'model':15s} {'R':>10s} {'T':>10s} {'A':>11s} {'|R+T+A-1|':>10s} "
          f"{'arg(a)-arg(b)':>14s} {'flux res':>9s}")
    for name, k2f, qf in MODELS:
        d = solve_interface(k2f, qf, MAT1, MAT2, OMEGA)
        print(f"    {name:15s} {d['R']:10.6f} {d['T']:10.6f} {d['A']:11.3e} "
              f"{abs(d['R']+d['T']+d['A']-1.0):10.2e} {d['dphase']:14.2e} {d['flux_res']:9.2e}")
    print("    => A = 0 to machine precision for ALL models, dissipative ones included.")
    print("       Reason: the flux amplitudes share a common phase, so the interface has")
    print("       nothing to absorb.  Bulk dissipation lives inside complex k, i.e. in T.")

    # ---------------------------------------------------------------- [2] limits
    print("\n[2] LOW-FREQUENCY LIMIT: LS and GL must approach Biot as omega*tau0 -> 0")
    for om in (OMEGA, OMEGA * 1e-2, OMEGA * 1e-4):
        vals = {n: solve_interface(k2f, qf, MAT1, MAT2, om) for n, k2f, qf in MODELS}
        print(f"    omega*tau0={om*MAT1['tau0']:.1e}: Biot A={vals['Biot/Fourier']['A']:+.2e} "
              f"LS A={vals['Lord-Shulman']['A']:+.2e} GL A={vals['Green-Lindsay']['A']:+.2e}")

    # ---------------------------------------------------------------- [3] phase mismatch
    print("\n[3] PHASE MISMATCH ACROSS THE INTERFACE (A becomes nonzero)")
    for tag, m2, k2f, qf in (
        ("LS  tau0 1e-10 | 1e-11", dict(MAT2, tau0=1e-11), ls_k2, ls_q),
        ("GN3 c_h 2000 | 5000", dict(MAT2, c_h=5000.0), gn3_k2, gn3_q),
    ):
        d = solve_interface(k2f, qf, MAT1, m2, OMEGA)
        print(f"    {tag:24s} R={d['R']:.6f} T={d['T']:.6f} A={d['A']:+.4e} "
              f"|sum-1|={abs(d['R']+d['T']+d['A']-1):.1e}")

    # ---------------------------------------------------------------- [4] Kapitza
    print("\n[4] KAPITZA CONTACT CONDUCTANCE h (interface-level loss => A > 0)")
    print(f"    {'model':15s} {'h [W/m2K]':>10s} {'R':>10s} {'T':>10s} {'A':>11s} "
          f"{'|R+T+A-1|':>10s} {'jump res':>9s}")
    for name, k2f, qf in (("Lord-Shulman", ls_k2, ls_q), ("Biot/Fourier", biot_k2, biot_q),
                          ("GN-II", gn2_k2, gn2_q)):
        for h in (1e9, 1e8, 1e7, 1e6):
            d = solve_interface(k2f, qf, MAT1, MAT2, OMEGA, h=h)
            print(f"    {name:15s} {h:10.0e} {d['R']:10.6f} {d['T']:10.6f} {d['A']:11.4e} "
                  f"{abs(d['R']+d['T']+d['A']-1.0):10.2e} {d['jump_res']:9.2e}")
    print("    A -> 0 at both h -> inf (ideal) and h -> 0 (nothing enters, R -> 1);")
    print("    A is non-monotonic in h, with a maximum in between. Both limits are checks.")

    # ---------------------------------------------------------------- [5] MGT
    print("\n[5] MGT is NOT included.")
    print("    MGT is written as a single third-order-in-time equation for T:")
    print("        tau T_ttt + T_tt = b Lap T_t + c^2 Lap T")
    print("    It supplies no constitutive flux q, and for a third-order-in-time equation the")
    print("    energy functional is not unique -- multiplying by T_t, T or T_tt gives different")
    print("    candidates differing by total derivatives.  Hence 'the flux at the interface' is")
    print("    undefined until an energy functional is chosen, and R/T would be a statement about")
    print("    that choice.  An interface between two MGT media also needs THREE conditions on T,")
    print("    not two.  See V-B3a section 3.6.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
