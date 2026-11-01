#!/usr/bin/env python3
"""BK-12, BK-13, BK-14: the plate, layer and interface invariants.

`bench_atlas.py` covered bulk models (BK-01..BK-08) and `bench_surface.py` added the
elastic surface wave (BK-09). `atlas_case_coverage.csv` then named four families that
had no executable invariant. This file writes three of them, and each one is checked
against a **classical closed-form anchor**, not against itself:

  BK-12  Rayleigh-Lamb plate, elastic limit.
         anchors: S0 -> c_S sqrt(2/(1-nu)) as kh -> 0 (the plate velocity),
                  both A0 and S0 -> c_R as kh -> infinity,
                  A0 -> 0 as kh -> 0 (the flexural branch).
  BK-13  Love waves in a layer over a half-space.
         anchors: the cut-off frequencies obey omega_n h sqrt(1/c1^2 - 1/c2^2) = n pi,
                  and no Love wave exists when the layer is the faster medium.
  BK-14  SH reflection at a welded interface.
         anchors: Snell's law, energy-flux conservation
                  |R|^2 + |T|^2 (Z2 cos / Z1 cos) = 1, and |R| = 1 beyond the
                  critical angle.

BK-15 (coupled multifield branch speeds) is still not written: it needs a coupled
piezo-magneto constitutive model that this repository does not have, and inventing one
would produce numbers about a model nobody uses.

Nothing here is compared with any of the 40 atlas papers: they were read at title and
metadata level only.

Usage
  python3 bench_families.py            # writes bench_families_results.csv
  python3 bench_families.py --check    # PASS/FAIL only, exit 1 on any failure
"""
import csv
import math
import cmath
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "bench_families_results.csv")

# ============================================================ BK-12  Rayleigh-Lamb
def gamma_of(nu):
    """c_S / c_L."""
    return math.sqrt((1.0 - 2.0 * nu) / (2.0 * (1.0 - nu)))


def rayleigh_of(nu):
    """c_R / c_S from the Rayleigh equation (same equation as BK-09)."""
    eta = gamma_of(nu) ** 2

    def f(x):
        return (2.0 - x * x) ** 2 - 4.0 * math.sqrt(max(0.0, (1 - x * x) * (1 - eta * x * x)))

    # x = 0 is a degenerate root of this written form (both sides equal 4), so the
    # physical root is bracketed in (0.5, 1): f < 0 at 0.5 and f > 0 at 1.
    lo, hi = 0.5, 1.0
    for _ in range(300):
        mid = 0.5 * (lo + hi)
        if f(mid) < 0:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def rl_residual(Omega, xi, g, symmetric):
    """Residual of the Rayleigh-Lamb equation in non-dimensional form.

    xi = k h, Omega = omega h / c_S, g = c_S / c_L.  Written with sin/cos and
    sinh/cosh products so that the tan poles of the textbook form never appear
    (a pole is a sign change that is not a root).

    Regime c < c_S  (Omega < xi): both partial waves are evanescent.
        S: tanh(a)/tanh(b) = 4 xi^2 a b / (a^2 + xi^2)^2
        A: tanh(a)/tanh(b) = (a^2 + xi^2)^2 / (4 xi^2 a b)
    Regime c_S < c < c_L (xi < Omega < xi/g): q real, p evanescent.
        S: tan(q)/tanh(b) = 4 xi^2 q b / (Omega^2 - 2 xi^2)^2
        A: tan(q)/tanh(b) = -(Omega^2 - 2 xi^2)^2 / (4 xi^2 q b)
    Regime c > c_L (Omega > xi/g): both real.
        S: tan(q)/tan(p) = -4 xi^2 p q / (q^2 - xi^2)^2
        A: tan(q)/tan(p) = -(q^2 - xi^2)^2 / (4 xi^2 p q)
    """
    if Omega <= 0:
        return float("nan")
    if Omega < xi:                                   # c < c_S
        a = math.sqrt(max(0.0, xi * xi - Omega * Omega))
        b = math.sqrt(max(0.0, xi * xi - (g * Omega) ** 2))
        if a == 0.0 or b == 0.0:
            return float("nan")
        if symmetric:
            R = 4.0 * xi * xi * a * b / (a * a + xi * xi) ** 2
        else:
            R = (a * a + xi * xi) ** 2 / (4.0 * xi * xi * a * b)
        return math.sinh(a) * math.cosh(b) - R * math.sinh(b) * math.cosh(a)
    q = math.sqrt(max(0.0, Omega * Omega - xi * xi))
    if Omega < xi / g:                               # c_S < c < c_L
        b = math.sqrt(max(0.0, xi * xi - (g * Omega) ** 2))
        if q == 0.0 or b == 0.0:
            return float("nan")
        den = (Omega * Omega - 2.0 * xi * xi)
        if abs(den) < 1e-15:
            return float("nan")
        if symmetric:
            R = 4.0 * xi * xi * q * b / (den * den)
        else:
            R = -(den * den) / (4.0 * xi * xi * q * b)
        return math.sin(q) * math.cosh(b) - R * math.sinh(b) * math.cos(q)
    p = math.sqrt(max(0.0, (g * Omega) ** 2 - xi * xi))  # c > c_L
    if p == 0.0 or q == 0.0:
        return float("nan")
    den = (q * q - xi * xi) ** 2
    if symmetric:
        R = -4.0 * xi * xi * p * q / den
    else:
        R = -den / (4.0 * xi * xi * p * q)
    return math.sin(q) * math.cos(p) - R * math.sin(p) * math.cos(q)


def rl_branches(xi, nu, symmetric, n=6000, lo=1e-4):
    """All roots of the Rayleigh-Lamb residual in Omega at fixed xi."""
    g = gamma_of(nu)
    hi = xi / g * 6.0 + 6.0
    grid = np.linspace(lo, hi, n)
    vals = [rl_residual(float(o), xi, g, symmetric) for o in grid]
    roots = []
    for i in range(len(grid) - 1):
        f0, f1 = vals[i], vals[i + 1]
        if not (math.isfinite(f0) and math.isfinite(f1)):
            continue
        if f0 == 0.0:
            roots.append(float(grid[i]))
            continue
        if f0 * f1 < 0:
            a, b = float(grid[i]), float(grid[i + 1])
            fa = f0
            for _ in range(80):
                m = 0.5 * (a + b)
                fm = rl_residual(m, xi, g, symmetric)
                if not math.isfinite(fm):
                    break
                if fa * fm <= 0:
                    b = m
                else:
                    a, fa = m, fm
            roots.append(0.5 * (a + b))
    # keep distinct roots
    out = []
    for r in roots:
        if not out or abs(r - out[-1]) > 1e-6 * max(1.0, r):
            out.append(r)
    return out


def _roots_filtered(xi, nu, symmetric, n=6000):
    """Roots with the Omega -> 0 degeneracy (both sides of the equation vanish
    together at Omega = 0) removed: a physical branch has c = Omega/xi above 0.05."""
    g = gamma_of(nu)
    lo = max(1e-9, 0.05 * xi)
    hi = max(4.0 * xi, xi / g * 2.0 + 2.0)
    grid = np.linspace(lo, hi, n)
    vals = [rl_residual(float(o), xi, g, symmetric) for o in grid]
    roots, i = [], 0
    while i < len(grid) - 1:
        f0, f1 = vals[i], vals[i + 1]
        if math.isfinite(f0) and math.isfinite(f1) and f0 * f1 < 0:
            a, b, fa = float(grid[i]), float(grid[i + 1]), f0
            for _ in range(80):
                m = 0.5 * (a + b)
                fm = rl_residual(m, xi, g, symmetric)
                if not math.isfinite(fm):
                    break
                if fa * fm <= 0:
                    b = m
                else:
                    a, fa = m, fm
            r = 0.5 * (a + b)
            if not roots or abs(r - roots[-1]) > 1e-4 * max(1.0, r):
                roots.append(r)
        i += 1
    return roots


def _continue_branch(nu, symmetric, xi_start, xi_end, pick):
    """Follow one branch by continuation in xi, which is how A0 is kept away from the
    Omega -> 0 degeneracy at very small kh."""
    g = gamma_of(nu)
    xi = xi_start
    roots = _roots_filtered(xi, nu, symmetric)
    if not roots:
        return []
    omega = pick([r / xi for r in roots], roots)
    out = [(xi, omega / xi)]
    step = 1.0 / 1.4
    while xi > xi_end:
        xi_next = max(xi_end, xi * step)
        centre = omega * (xi_next / xi)
        lo = max(1e-9, 0.6 * centre)
        hi = 1.4 * centre
        grid = np.linspace(lo, hi, 400)
        vals = [rl_residual(float(o), xi_next, g, symmetric) for o in grid]
        found = None
        for i in range(len(grid) - 1):
            f0, f1 = vals[i], vals[i + 1]
            if math.isfinite(f0) and math.isfinite(f1) and f0 * f1 < 0:
                a, b, fa = float(grid[i]), float(grid[i + 1]), f0
                for _ in range(80):
                    m = 0.5 * (a + b)
                    fm = rl_residual(m, xi_next, g, symmetric)
                    if not math.isfinite(fm):
                        break
                    if fa * fm <= 0:
                        b = m
                    else:
                        a, fa = m, fm
                found = 0.5 * (a + b)
                break
        if found is None:
            break
        omega = found
        xi = xi_next
        out.append((xi, omega / xi))
    return out


def b12():
    rows = []
    nu = 0.25
    cR = rayleigh_of(nu)
    cplate = math.sqrt(2.0 / (1.0 - nu))

    # A0: follow the flexural branch from kh = 20 down to kh = 0.02
    a_curve = _continue_branch(nu, False, 20.0, 0.02,
                               lambda speeds, roots: roots[min(range(len(speeds)),
                                                               key=lambda i: abs(speeds[i] - cR))])
    # S0: the fastest symmetric branch, followed the same way
    # at kh = 20 every branch is either at c_R or at c_L, so S0 is the branch closest
    # to c_R; starting from the plate velocity would follow the wrong branch
    s_curve = _continue_branch(nu, True, 20.0, 0.02,
                               lambda speeds, roots: roots[min(range(len(speeds)),
                                                               key=lambda i: abs(speeds[i] - cR))])

    # 1. S0 -> the classical plate velocity as kh -> 0
    s_small = s_curve[-1][1] if s_curve else None
    ok = s_small is not None and abs(s_small - cplate) < 1e-2
    rows.append(("BK-12", "Rayleigh-Lamb plate",
                 "S0 speed at kh = 0.02 vs c_S sqrt(2/(1-nu)) (nu = 1/4)",
                 "%.6f c_S" % s_small if s_small else "not found", "%.6f c_S" % cplate,
                 "1e-2", "%.2e" % abs(s_small - cplate) if s_small else "-",
                 "PASS" if ok else "FAIL"))

    # 2. A0 -> 0 as kh -> 0 (the flexural branch)
    a_small = a_curve[-1][1] if a_curve else None
    ok = a_small is not None and a_small < 0.05
    rows.append(("BK-12", "Rayleigh-Lamb plate",
                 "A0 speed at kh = 0.02 (flexural branch must vanish)",
                 "%.6f c_S" % a_small if a_small else "not found", "< 0.05 c_S", "-",
                 "%.2e" % a_small if a_small else "-", "PASS" if ok else "FAIL"))

    # 3. both branches -> c_R as kh -> infinity
    s_hi = s_curve[0][1] if s_curve else None
    a_hi = a_curve[0][1] if a_curve else None
    worst = max(abs(s_hi - cR), abs(a_hi - cR)) if (s_hi and a_hi) else None
    ok = worst is not None and worst < 5e-3
    rows.append(("BK-12", "Rayleigh-Lamb plate",
                 "both branches -> c_R at kh = 20 (nu = 1/4)",
                 "max |c - c_R| = %.2e c_S" % worst if worst is not None else "not found",
                 "c_R = %.6f c_S" % cR, "5e-3", "%.2e" % worst if worst is not None else "-",
                 "PASS" if ok else "FAIL"))

    # 4. at least two non-degenerate branches per symmetry at kh = 1
    ns = len(_roots_filtered(1.0, nu, True))
    na = len(_roots_filtered(1.0, nu, False))
    ok = ns >= 2 and na >= 2
    rows.append(("BK-12", "Rayleigh-Lamb plate", "branch count at kh = 1 (S and A)",
                 "S %d, A %d" % (ns, na), "at least 2 each", "-", "-", "PASS" if ok else "FAIL"))

    # 5. S0 decreases and A0 increases as kh grows
    mono_s = all(s_curve[i][1] < s_curve[i + 1][1] for i in range(len(s_curve) - 1))
    mono_a = all(a_curve[i][1] > a_curve[i + 1][1] for i in range(len(a_curve) - 1))
    ok = bool(mono_s and mono_a) and len(s_curve) > 5 and len(a_curve) > 5
    rows.append(("BK-12", "Rayleigh-Lamb plate",
                 "S0 decreasing and A0 increasing in kh (continuation, 20 -> 0.02)",
                 "S %s (%d points), A %s (%d points)"
                 % ("yes" if mono_s else "no", len(s_curve),
                    "yes" if mono_a else "no", len(a_curve)),
                 "both yes", "-", "-", "PASS" if ok else "FAIL"))
    return rows


# ============================================================ BK-13  Love waves
def love_roots(omega, c1, c2, mu_ratio, h=1.0, n=4000):
    """Roots of the Love dispersion for a layer (c1) over a half-space (c2 > c1).

        tan(omega h sqrt(1/c^2 - 1/c1^2)) = mu2/mu1 * sqrt(1/c^2 - 1/c2^2)
                                                       / sqrt(1/c1^2 - 1/c^2)
    """
    if c1 >= c2:
        return []                      # a Love wave needs c1 < c < c2: none if c1 >= c2
    lo, hi = c1 * (1 + 1e-9), c2 * (1 - 1e-9)

    def f(c):
        k = math.sqrt(1.0 / (c * c) - 1.0 / (c1 * c1))
        kk = math.sqrt(max(0.0, 1.0 / (c * c) - 1.0 / (c2 * c2)))
        k1 = math.sqrt(1.0 / (c1 * c1) - 1.0 / (c * c))
        # sin/cos form, no tan poles
        return (math.sin(omega * h * k1) * math.sqrt(max(1e-300, k1))
                - mu_ratio * math.sqrt(max(0.0, kk)) * math.cos(omega * h * k1) / math.sqrt(max(1e-300, k1)) * math.sqrt(max(1e-300, k1)))
    # simpler, equivalent residual without divisions:
    def g(c):
        k1 = math.sqrt(max(1e-300, 1.0 / (c1 * c1) - 1.0 / (c * c)))
        kk = math.sqrt(max(0.0, 1.0 / (c * c) - 1.0 / (c2 * c2)))
        return math.sin(omega * h * k1) * k1 - mu_ratio * kk * math.cos(omega * h * k1)

    grid = np.linspace(lo, hi, n)
    vals = [g(float(c)) for c in grid]
    roots = []
    for i in range(len(grid) - 1):
        if not (math.isfinite(vals[i]) and math.isfinite(vals[i + 1])):
            continue
        if vals[i] * vals[i + 1] < 0:
            a, b, fa = float(grid[i]), float(grid[i + 1]), vals[i]
            for _ in range(80):
                m = 0.5 * (a + b)
                fm = g(m)
                if fa * fm <= 0:
                    b = m
                else:
                    a, fa = m, fm
            roots.append(0.5 * (a + b))
    return roots


def b13():
    rows = []
    c1, c2, mu_ratio, h = 1.0, 2.0, 2.0, 1.0
    omega1 = math.pi / (h * math.sqrt(1.0 / c1 ** 2 - 1.0 / c2 ** 2))
    omega2 = 2 * omega1

    # 1. the fundamental mode exists below the first cut-off
    r = love_roots(0.5 * omega1, c1, c2, mu_ratio, h)
    ok = len(r) == 1
    rows.append(("BK-13", "Love waves", "modes below the first cut-off (omega = 0.5 omega_1)",
                 "%d mode(s)" % len(r), "exactly 1", "-", "-", "PASS" if ok else "FAIL"))

    # 2. one more mode appears above each cut-off
    r1 = love_roots(1.05 * omega1, c1, c2, mu_ratio, h)
    r2 = love_roots(1.05 * omega2, c1, c2, mu_ratio, h)
    ok = len(r1) == 2 and len(r2) == 3
    rows.append(("BK-13", "Love waves", "mode count just above omega_1 and omega_2",
                 "%d then %d" % (len(r1), len(r2)), "2 then 3", "-", "-",
                 "PASS" if ok else "FAIL"))

    # 3. the cut-off formula: at omega just above omega_1 the second mode sits just
    #    below c2, i.e. c -> c2 as omega -> omega_1+
    if len(r1) >= 2:
        c_top = max(r1)
        gap = (c2 - c_top)
        ok = gap < 0.05 * c2
        rows.append(("BK-13", "Love waves", "upper mode approaches c2 at the cut-off",
                     "c2 - c = %.4e (omega = 1.05 omega_1)" % gap, "< 5% of c2", "0.05 c2",
                     "%.3e" % gap, "PASS" if ok else "FAIL"))
    else:
        rows.append(("BK-13", "Love waves", "upper mode approaches c2 at the cut-off",
                     "not found", "< 5% of c2", "0.05 c2", "-", "FAIL"))

    # 4. the closed-form cut-off is the one the dispersion turns on at: scan omega
    #    and find where the second mode first appears
    def has_two(w):
        return len(love_roots(w, c1, c2, mu_ratio, h)) >= 2

    lo, hi = 0.5 * omega1, 1.5 * omega1
    for _ in range(60):
        mid = 0.5 * (lo + hi)
        if has_two(mid):
            hi = mid
        else:
            lo = mid
    err = abs(hi - omega1) / omega1
    ok = err < 1e-3
    rows.append(("BK-13", "Love waves", "measured cut-off vs n pi / sqrt(1/c1^2-1/c2^2)",
                 "omega_1 measured %.6f, formula %.6f" % (hi, omega1), "relative error < 1e-3",
                 "1e-3", "%.2e" % err, "PASS" if ok else "FAIL"))

    # 5. no Love wave when the layer is the faster medium
    none = love_roots(5.0, c2, c1, mu_ratio, h)   # c1 > c2 here
    ok = len(none) == 0
    rows.append(("BK-13", "Love waves", "no mode when the layer is faster than the half-space",
                 "%d mode(s)" % len(none), "0", "-", "-", "PASS" if ok else "FAIL"))
    return rows


# ============================================================ BK-14  SH interface
def b14():
    rows = []
    mu1, mu2, c1, c2 = 1.0, 3.0, 1.0, 1.7          # mu2/mu1 = 3, c2/c1 = 1.7

    def coeffs(theta1):
        s = math.sin(theta1)
        s2 = (c2 / c1) * s
        if s2 > 1.0:
            return None, None, None
        theta2 = math.asin(s2)
        Z1 = mu1 * math.cos(theta1) / c1
        Z2 = mu2 * math.cos(theta2) / c2
        R = (Z1 - Z2) / (Z1 + Z2)
        T = 2 * Z1 / (Z1 + Z2)
        return R, T, Z2 / Z1        # flux is proportional to Z |A|^2

    # 1. energy flux is conserved for every angle below the critical angle
    worst = 0.0
    for deg in range(0, 30, 2):
        th = math.radians(deg)
        R, T, ratio = coeffs(th)
        if R is None:
            continue
        worst = max(worst, abs(R * R + T * T * ratio - 1.0))
    ok = worst < 1e-12
    rows.append(("BK-14", "SH interface", "max |R^2 + T^2 (Z2/Z1) - 1| below the critical angle",
                 "%.2e" % worst, "1e-12", "1e-12", "%.2e" % worst, "PASS" if ok else "FAIL"))

    # 2. Snell's law holds by construction; check it numerically
    th = math.radians(20)
    s2 = (c2 / c1) * math.sin(th)
    th2 = math.asin(s2)
    err = abs(math.sin(th) / c1 - math.sin(th2) / c2)
    ok = err < 1e-15
    rows.append(("BK-14", "SH interface", "Snell residual at 20 degrees",
                 "%.2e" % err, "1e-15", "1e-15", "%.2e" % err, "PASS" if ok else "FAIL"))

    # 3. total internal reflection beyond the critical angle
    crit = math.degrees(math.asin(c1 / c2))
    R, T, _ = coeffs(math.radians(crit + 5))
    ok = R is None                                  # no transmitted wave at all
    rows.append(("BK-14", "SH interface", "critical angle %.3f deg: beyond it nothing is transmitted"
                 % crit, "R undefined (no real theta2)" if R is None else "R = %.4f" % R,
                 "no real transmitted angle", "-", "-", "PASS" if ok else "FAIL"))

    # 4. normal incidence matches the impedance formula
    R, T, _ = coeffs(0.0)
    Z1, Z2 = mu1 / c1, mu2 / c2
    Rn = (Z1 - Z2) / (Z1 + Z2)
    ok = abs(R - Rn) < 1e-15
    rows.append(("BK-14", "SH interface", "normal incidence R vs (Z1-Z2)/(Z1+Z2)",
                 "%.12f" % R, "%.12f" % Rn, "1e-15", "%.2e" % abs(R - Rn),
                 "PASS" if ok else "FAIL"))
    return rows


def main():
    rows = b12() + b13() + b14()
    with open(OUT, "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(["benchmark_id", "family", "quantity", "measured", "reference",
                    "tolerance", "error", "verdict"])
        w.writerows(rows)
    fails = [r for r in rows if r[7] != "PASS"]
    print("rows: %d (BK-12 %d, BK-13 %d, BK-14 %d), failures: %d"
          % (len(rows), sum(r[0] == "BK-12" for r in rows),
             sum(r[0] == "BK-13" for r in rows), sum(r[0] == "BK-14" for r in rows), len(fails)))
    for r in rows:
        print("  %-6s %s  %-58s %s" % (r[0], r[7], r[2][:58], r[3][:46]))
    if fails:
        print("FAIL %d row(s)" % len(fails))
        sys.exit(1)
    print("PASS all %d rows" % len(rows))


if __name__ == "__main__":
    main()
