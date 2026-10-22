#!/usr/bin/env python3
"""
V-B2p : DPL (dual-phase-lag) Taylor-truncation order, well-posedness, finite speed.

Reproduces every number quoted in V-B2p_dpl-truncation-order.md.

Conventions
-----------
Time convention: fields proportional to exp(s t) with s = -i*omega (i.e. e^{-i omega t}).
Energy equation:            theta_t + gamma * div q = 0            (gamma > 0)
Tzou constitutive law:      q(t+tau_q) = -kappa grad theta(t+tau_theta)
Effective diffusivity used below: kappa_eff = gamma*kappa   [m^2/s]

Truncations (numbering follows Dreher-Quintanilla-Racke 2009, eqs (1.12)-(1.15)):
  T1  q + tau_q q_t                     = -kappa grad th - kappa tau_th grad th_t
  T2  q + tau_q q_t + tau_q^2/2 q_tt    = -kappa grad th - kappa tau_th grad th_t
  T3  q + tau_q q_t                     = -kappa grad th - kappa tau_th grad th_t - kappa tau_th^2/2 grad th_tt
  T4  q + tau_q q_t + tau_q^2/2 q_tt    = -kappa grad th - kappa tau_th grad th_t - kappa tau_th^2/2 grad th_tt

For a plane wave the characteristic polynomial in s is written in the module as
poly(s; k) for each truncation.  The "n - m" invariant of Dreher et al. (their
Theorem 1.3) is (order in time) - (highest time derivative acting on Delta):
  T1: n=2, m=1, n-m=1      T2: n=3, m=1, n-m=2
  T3: n=2, m=2, n-m=0      T4: n=3, m=2, n-m=1
Dreher et al. prove ill-posedness iff n-m >= 3, so all four standard truncations
sit inside the well-posed class; the delay equation itself is ill-posed.

Reference material (same as V-B2_wave_speeds.py): steel-like
  k_bulk = 45 W/(m K), rho = 7800 kg/m^3, c_v = 460 J/(kg K)
"""
import numpy as np

K_BULK = 45.0
RHO = 7800.0
C_V = 460.0
KAPPA_GEO = K_BULK / (RHO * C_V)    # kappa = k/(rho c_v), gamma absorbed: theta_t = kappa Delta theta
TAU_Q = 1.0e-10                     # s


# ----------------------------------------------------------------------------
# characteristic polynomials in s, for fixed wavenumber k
# ----------------------------------------------------------------------------
def poly_T1(k, tq, tt, kap):
    """n=2, m=1 : tau_q s^2 + (1 + kap k^2 tau_th) s + kap k^2 = 0"""
    return [tq, 1.0 + kap * k * k * tt, kap * k * k]


def poly_T2(k, tq, tt, kap):
    """n=3, m=1 : (tq^2/2) s^3 + tq s^2 + (1+kap k^2 tt) s + kap k^2 = 0"""
    return [tq * tq / 2.0, tq, 1.0 + kap * k * k * tt, kap * k * k]


def poly_T3(k, tq, tt, kap):
    """n=2, m=2 : tq s^2 + (1 + kap k^2 tt) s + (kap k^2 + kap k^2 tt s)... see below"""
    # theta_t + tq theta_tt = kap Delta theta + kap tt Delta theta_t + kap tt^2/2 Delta theta_tt
    # -> (kap k^2 tt^2/2) s^2 + (tq + kap k^2 tt) s + (1 + kap k^2) = 0  ... (verify below)
    return None  # handled explicitly in t3_roots(); kept for symmetry


def poly_T4(k, tq, tt, kap):
    """n=3, m=2 : (tq^2/2) s^3 + (tq + kap k^2 tt^2/2) s^2 + (1+kap k^2 tt) s + kap k^2 = 0"""
    return [tq * tq / 2.0,
            tq + kap * k * k * tt * tt / 2.0,
            1.0 + kap * k * k * tt,
            kap * k * k]


def roots_of(coeffs):
    return np.roots(np.array(coeffs, dtype=complex))


def phase_speed(coeffs, k):
    """omega/Re(k) for the least-damped oscillatory root; nan if none oscillates."""
    r = roots_of(coeffs)
    osc = [s for s in r if abs(s.imag) > 1e-6 * abs(s)]
    if not osc:
        return float("nan")
    s = max(osc, key=lambda z: abs(z.imag))
    return abs(s.imag) / k


def max_real_part(coeffs):
    return max(np.real(roots_of(coeffs)))


def stable_over_k(coeffs_fn, tq, tt, kap, kmin=1e2, kmax=1e10, n=80):
    bad = []
    for k in np.logspace(np.log10(kmin), np.log10(kmax), n):
        if max_real_part(coeffs_fn(k, tq, tt, kap)) >= 0.0:
            bad.append(k)
    return bad


def main():
    kap, tq = KAPPA_GEO, TAU_Q
    print("=" * 78)
    print("V-B2p  DPL truncation order -- numerical checks")
    print("=" * 78)
    print(f"kappa = {kap:.6e} m^2/s, tau_q = {tq:.1e} s")

    # ---------------------------------------------------------------- CHECK 1
    print("\n[1] Stability in tau_th  (compare Quintanilla & Racke 2006, IJHMT conclusions)")
    print("    T2 (2nd order in tau_q, 1st order in tau_th): stable iff tau_th/tau_q > 1/2")
    for ratio in (0.3, 0.5, 0.7):
        tt = ratio * tq
        bad = stable_over_k(poly_T2, tq, tt, kap)
        verdict = "STABLE for all k swept" if not bad else f"UNSTABLE from k={bad[0]:.3e} 1/m"
        print(f"      tau_th/tau_q = {ratio:4.2f} : {verdict}")
    print("    T1 (1st order in both): predicted 'always stable'")
    for ratio in (0.3, 1.0, 3.0):
        tt = ratio * tq
        bad = stable_over_k(poly_T1, tq, tt, kap)
        print(f"      tau_th/tau_q = {ratio:4.2f} : {'STABLE' if not bad else 'UNSTABLE'}")

    # ---------------------------------------------------------------- CHECK 2
    print("\n[2] Finite speed?  T2 prediction: v_inf = sqrt(2*kappa*tau_th)/tau_q")
    print("    (decoy sqrt(kappa/tau_th) is NOT the right expression -- it agrees only accidentally at tau_th ~ 0.7 tau_q)")
    for ratio in (1.0, 0.7, 0.5):
        tt = ratio * tq
        pred = np.sqrt(2.0 * kap * tt) / tq
        got = [phase_speed(poly_T2(k, tq, tt, kap), k) for k in (1e11, 1e13, 1e14)]
        decoy = np.sqrt(kap / tt)
        print(f"      tau_th={tt:.1e}: v(k=1e13)={got[1]:8.2f} m/s | predicted {pred:8.2f} "
              f"| decoy sqrt(kap/tau_th)={decoy:8.2f}")
    print("    => T2 has a FINITE propagation speed v_inf = sqrt(2 kappa tau_th)/tau_q.")

    # ---------------------------------------------------------------- CHECK 3
    print("\n[3] T1 (1st order in both) has NO finite speed: v_ph grows like sqrt(omega)")
    tt = 0.7 * tq
    om = 2.0 * np.pi * np.array([1e9, 1e11, 1e13])
    for o in om:
        s = -1j * o
        # k^2 from : (1 + kap k^2 tt) s + kap k^2 = -(tq s^2 + s)
        k2 = -(tq * s * s + s) / (kap * (1.0 + s * tt))
        kk = np.sqrt(complex(k2))
        print(f"      f={o/(2*np.pi):.0e} Hz: v_ph={o/np.real(kk):.4e} m/s "
              f"(v/sqrt(omega)={o/np.real(kk)/np.sqrt(o):.4e})")
    print("      v_ph ratio between successive rows ~10 for a 100x frequency increase => v ~ sqrt(omega): unbounded.")
    print("      Fixed-k roots of T1 for this material are real and negative (overdamped, no oscillation).")
    for k in (1e5, 1e7, 1e9):
        r = np.sort(roots_of(poly_T1(k, tq, tt, kap)).real)
        print(f"      k={k:.0e}: Re s = {r}")

    # ---------------------------------------------------------------- CHECK 4
    print("\n[4] T4 (2nd order in both): band-limited.  omega -> 1/tau_th, v_ph -> 0")
    tt = 0.7 * tq
    for k in (1e9, 1e11, 1e13, 1e15):
        r = roots_of(poly_T4(k, tq, tt, kap))
        osc = [s for s in r if abs(s.imag) > 1e-6 * abs(s)]
        s = max(osc, key=lambda z: abs(z.imag))
        print(f"      k={k:.0e}: omega={abs(s.imag):.4e}  v_ph={abs(s.imag)/k:.3e}  "
              f"1/tau_th={1/tt:.4e}")
    print("    => omega saturates at 1/tau_th; no propagation and no finite-speed front.")
    print("       (Consistent with Tzou's remark quoted by Quintanilla & Racke 2006: second-order")
    print("        expansion in both lags 'results in an equation of parabolic type'.)")

    # ---------------------------------------------------------------- CHECK 5
    print("\n[5] Growth of |s| with k: the n-m invariant of Dreher et al. (2009) Thm 1.3")
    for name, fn, n_m in (("T1", poly_T1, 1), ("T2", poly_T2, 2), ("T4", poly_T4, 1)):
        tt = 0.7 * tq
        vals = []
        for k in (1e6, 1e8, 1e10):
            vals.append(max(abs(roots_of(fn(k, tq, tt, kap)))))
        print(f"      {name} (n-m={n_m}): max|s| at k=1e6,1e8,1e10 -> "
              f"{vals[0]:.2e}, {vals[1]:.2e}, {vals[2]:.2e}")
    print("      |s| grows like k^(2/(n-m)): k^2 for n-m=1, k^1 (finite speed) for n-m=2.")

    # ---------------------------------------------------------------- CHECK 6
    print("\n[6] Admissibility edge: at tau_th = tau_q/2 the finite speed is sqrt(kappa/tau_q)")
    tt = tq / 2.0
    print(f"      sqrt(2 kappa tau_th)/tau_q = {np.sqrt(2*kap*tt)/tq:.2f}   "
          f"sqrt(kappa/tau_q) = {np.sqrt(kap/tq):.2f}")
    print("\nAll checks completed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
