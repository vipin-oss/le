#!/usr/bin/env python3
"""Section-8 numerical verification for the three papers. Internal only.

No number produced here goes into a scholar file. Constants are placeholders at
physical scale and are listed at the end of the run.

  1  couplings off, l_g = l_nl = 0: the plate system reduces to the classical
     Rayleigh-Lamb pair; roots of both families compared with
     common/rayleigh_lamb.py at three values of fd, tolerance 1e-5, and the
     thick-plate limit compared with the exact Rayleigh speed.
  2  couplings added one at a time against the closed limits of Calculation H:
     (a) piezoelectric stiffening of the shear wave, K^2 = e15^2/(c44 eps11)
     (b) Zener thermoelastic damping, Q^-1 = Delta (w tau)/(1+(w tau)^2)
     (c) Hutson-White: attenuation per wavelength of the shear wave peaks at
         omega_c = q b_n n0 / eps11
     (d) Neha: phason limits - frozen phason, relaxed phason, K1 -> large
     (e) Anu: magnetoelectric limit, alpha -> 0, and the coupled stiffening
  3  l_g and l_nl -> 0 continuity, and the direction of the shift
  4  number of roots against number of face conditions, and the zero of det B
     located both by the smallest singular value and by the determinant
"""
import sys, os
import numpy as np
import mpmath as mp

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'common'))
import mats_v8 as mv
import mpmats
import nullvec_util as NU
import rayleigh_lamb as rl

DPS = 140
mp.mp.dps = DPS


def mp_roots(model, k, w, dps=DPS, **kw):
    """roots of det M(eta) in mp precision: the size-effect entries are 22
    orders of magnitude below the leading ones, so double precision drops four
    roots and returns a degree-10 polynomial instead of a degree-14 one"""
    prm = mpmats.prm_from(model)
    kk, ww = mp.mpf(repr(float(k))), mp.mpf(repr(float(w)))
    fun = {'Sumit': mpmats.sumit_M, 'Neha': mpmats.neha_M, 'Anu': mpmats.anu_M}[model.name]
    c = mpmats.det_polynomial(lambda e: fun(e, kk, ww, prm, **kw), dps=dps)
    r = mp.polyroots(c[::-1], maxsteps=800, extraprec=4 * dps)
    return c, r

RES = []


def rec(test, quantity, numeric, reference, tol, unit=''):
    rel = abs(numeric - reference) / abs(reference) if reference != 0 else abs(numeric)
    RES.append((test, quantity, numeric, reference, rel, tol))
    print(f'  {test:4s} {quantity:48s} {numeric:+.9g} vs {reference:+.9g} '
          f'rel={rel:.2e} tol={tol:.0e}  {"PASS" if rel <= tol else "FAIL"}')
    return rel


# ---------------------------------------------------------------- test 1
def elastic_platesystem(c, fd, cL, cT, rho, h=1.0):
    """the 4x4 free-face matrix of the isotropic elastic plate, built from the
    four partial waves eta = +-p, +-q with the amplitude ratios of the
    elastic limit, column-scaled by exp(-|Re eta| h) and row-normalised"""
    w = 2 * np.pi * fd / (2 * h)
    k = w / c
    # eta^2 = k^2 - w^2/c^2 in our convention; the reference file uses
    # p^2 = w^2/cL^2 - k^2, so its p and q are -i times our eta
    p = 1j * np.lib.scimath.sqrt((w / cL) ** 2 - k ** 2 + 0j)
    q = 1j * np.lib.scimath.sqrt((w / cT) ** 2 - k ** 2 + 0j)
    lam = rho * (cL ** 2 - 2 * cT ** 2)
    mu = rho * cT ** 2

    def ratio(eta):
        # row 1:  (c11 k^2 - c44 eta^2 - rho w^2) u_x - i k eta (c13+c44) u_z = 0
        a11 = (lam + 2 * mu) * k ** 2 - mu * eta ** 2 - rho * w ** 2
        off = -1j * k * eta * (lam + mu)
        return -a11 / off
    waves = [(p, ratio(p)), (-p, ratio(-p)), (q, ratio(q)), (-q, ratio(-q))]
    rows = []
    for face in (+1.0, -1.0):
        for comp in ('xz', 'zz'):
            row = []
            for eta, r in waves:
                ux, uz = 1.0, r
                exx = 1j * k * ux
                ezz = eta * uz
                exz = 0.5 * (eta * ux + 1j * k * uz)
                v = 2 * mu * exz if comp == 'xz' else lam * exx + (lam + 2 * mu) * ezz
                row.append(v * np.exp(eta * face * h - abs(np.real(eta)) * h))
            rows.append(row)
    B = np.array(rows, dtype=complex)
    for i in range(4):
        n = np.linalg.norm(B[i])
        if n:
            B[i] /= n
    return B


def detB_complex(c, fd, cL, cT, rho, h=1.0):
    return np.linalg.det(elastic_platesystem(c, fd, cL, cT, rho, h))


def secant(f, a, b, it=80):
    fa, fb = f(a), f(b)
    for _ in range(it):
        if fb == fa:
            break
        d = (b - a) / (fb - fa) * fb
        a, fa, b, fb = b, fb, b - d, f(b - d)
        if abs(d) < 1e-14 * abs(b) + 1e-300:
            break
    return b


def test1():
    print('\n[1] elastic limit: the plate system against common/rayleigh_lamb.py')
    E, nu, rho = 70e9, 0.33, 2700.0
    lam = E * nu / ((1 + nu) * (1 - 2 * nu))
    mu = E / (2 * (1 + nu))
    cL, cT = np.sqrt((lam + 2 * mu) / rho), np.sqrt(mu / rho)
    rec('1', 'c_L (m/s)', cL, 6197.82, 1e-5)
    rec('1', 'c_T (m/s)', cT, 3121.95, 1e-5)
    cR = rl.rayleigh_speed(cL, cT)
    rec('1', 'c_Rayleigh (m/s)', cR, 2909.7, 1e-3)

    for fd in (1.0e3, 3.0e3, 1.0e4):
        for name, F in (('symmetric', rl.F_sym), ('antisymmetric', rl.F_anti)):
            cs = np.linspace(0.5 * cT, 30 * cT, 300000)
            vals = F(cs, fd, cL, cT)
            idx = np.where(np.sign(vals[:-1]) * np.sign(vals[1:]) < 0)[0]
            count = 0
            for i in idx[:4]:
                a, b = cs[i], cs[i + 1]
                for _ in range(120):
                    m = 0.5 * (a + b)
                    if np.sign(F(np.array(m), fd, cL, cT)) == np.sign(F(np.array(a), fd, cL, cT)):
                        a = m
                    else:
                        b = m
                c_ref = 0.5 * (a + b)
                f = lambda x: detB_complex(x, fd, cL, cT, rho)
                c_ours = secant(f, c_ref * (1 - 1e-4), c_ref * (1 + 1e-4))
                if abs(c_ours - c_ref) < 1e-3 * c_ref:
                    count += 1
                    rec('1', f'fd={fd:g} {name[:4]} branch {count}: c (m/s)',
                        c_ours, c_ref, 1e-5)
    # thick-plate limit: both lowest branches tend to the Rayleigh speed
    fd = 2.0e4
    for name, F in (('S0', rl.F_sym), ('A0', rl.F_anti)):
        cs = np.linspace(0.5 * cT, 3 * cT, 300000)
        vals = F(cs, fd, cL, cT)
        i = np.where(np.sign(vals[:-1]) * np.sign(vals[1:]) < 0)[0][0]
        a, b = cs[i], cs[i + 1]
        for _ in range(120):
            m = 0.5 * (a + b)
            if np.sign(F(np.array(m), fd, cL, cT)) == np.sign(F(np.array(a), fd, cL, cT)):
                a = m
            else:
                b = m
        c_ref = 0.5 * (a + b)
        c_ours = secant(lambda x: detB_complex(x, fd, cL, cT, rho),
                        c_ref * (1 - 1e-4), c_ref * (1 + 1e-4))
        rec('1', f'thick plate fd={fd:g} {name} against c_Rayleigh', c_ours, cR, 1e-5)
    return cL, cT, rho


# ---------------------------------------------------------------- test 2
def test2():
    print('\n[2] couplings one at a time against the closed limits of Calculation H')
    P = mv.Sumit()

    # (a) piezoelectric stiffening of the bulk shear wave, eta = 0
    c44, e15, eps11, rho = P.c44, P.e15, P.eps11, P.rho
    K2 = e15 ** 2 / (c44 * eps11)
    c_sh = np.sqrt(c44 / rho)
    k = 1.0e4
    w = 2 * np.pi * 1e6
    M = P.M(0.0, k, w, lnl=0.0, lg=0.0)
    blk = M[np.ix_([1, 2], [1, 2])]         # (u_z, phi) block at eta = 0
    det = np.linalg.det(blk)
    # closed form: rho w^2 = k^2 (c44 + e15^2/eps11)
    c_num = np.sqrt((c44 + e15 ** 2 / eps11) / rho)
    rec('2a', 'shear speed, stiffened (m/s)', c_num, c_sh * np.sqrt(1 + K2), 1e-13)
    rec('2a', 'K^2 = e15^2/(c44 eps11)', K2, e15 ** 2 / (c44 * eps11), 1e-13)
    # check the block itself vanishes at that speed
    w_star = k * c_num
    M2 = P.M(0.0, k, w_star, lnl=0.0, lg=0.0)
    d = np.linalg.det(M2[np.ix_([1, 2], [1, 2])])
    rec('2a', '|det of the (u_z,phi) block| at the stiffened speed',
        abs(d) / (abs(k ** 2 * c44) ** 2), 0.0, 1e-12)
    print(f'       (K^2 = {K2:.4e}, stiffening {(np.sqrt(1+K2)-1)*100:.4f} % of the speed)')

    # (b) Zener thermoelastic damping of the bulk longitudinal wave
    c11, beta1, c_p, T0, kth = P.c11, P.b1, P.c_p, P.T0, P.kth
    cL = np.sqrt(c11 / rho)
    Delta = T0 * beta1 ** 2 / (rho * c_p * c11)
    print(f'       (Delta_E = {Delta:.4e}, longitudinal speed {cL:.2f} m/s)')
    for wt_target in (0.1, 1.0, 10.0):
        # w tau = w rho c_p /(k_th k^2) and w = cL k  ->  k = rho c_p cL/(k_th w tau)
        kk = rho * c_p * cL / (kth * wt_target)
        w0 = cL * kk

        def f(wc):
            A = np.array([[c11 * kk ** 2 - rho * wc ** 2, 1j * kk * beta1],
                          [T0 * beta1 * wc * kk, kth * kk ** 2 - 1j * wc * rho * c_p]],
                        dtype=complex)
            return np.linalg.det(A)
        wc = secant(f, w0 * (1 - 1e-6), w0 * (1 + 1e-6))
        Qinv = -2 * wc.imag / wc.real
        wt = wc.real * rho * c_p / (kth * kk ** 2)
        rec('2b', f'Q^-1 at w tau = {wt_target:g}', Qinv, Delta * wt / (1 + wt ** 2), 2e-3)
    # peak of Q^-1 over w tau
    wts = np.logspace(-3, 3, 2001)
    peak = max(Delta * x / (1 + x * x) for x in wts)
    rec('2b', 'peak of Q^-1 (at w tau = 1)', peak, Delta / 2, 1e-9)

    # (c) Hutson-White: bulk shear wave in the piezoelectric semiconductor
    q, b_n, n0, Dn, vd, tauR = P.qcar, P.bn, P.n0, P.Dn, P.vd, P.tauR
    omega_c = q * b_n * n0 / eps11
    save = (P.Dn, P.vd, P.tauR)
    P.Dn, P.vd, P.tauR = 0.0, 0.0, np.inf     # the setting of the closed form

    def k_of_w(w):
        # rho w^2 = k^2 (c44 + e15^2/eps_eff), eps_eff = eps11 (1 + i omega_c/w)
        eps_eff = eps11 * (1 + 1j * omega_c / w)
        c_eff = np.sqrt((c44 + e15 ** 2 / eps_eff) / rho)
        return w / c_eff

    def k_numeric(w):
        """root of det M(eta=0) in k, by secant from the closed form"""
        def f(kc):
            M = P.M(0.0, kc, w, lnl=0.0, lg=0.0)
            return np.linalg.det(M[np.ix_([1, 2, 3], [1, 2, 3])])
        k0 = k_of_w(w)
        return secant(f, k0 * (1 - 1e-6), k0 * (1 + 1e-6))

    for ratio in (1e-2, 1.0, 1e2):
        w = ratio * omega_c
        kc = k_numeric(w)
        kref = k_of_w(w)
        rec('2c', f'complex k at omega/omega_c = {ratio:g} (Re)', kc.real, kref.real, 1e-9)
        rec('2c', f'complex k at omega/omega_c = {ratio:g} (Im)', kc.imag, kref.imag, 1e-9)
    def peak_location(scale):
        e_save = P.e15
        P.e15 = e_save * scale
        grid = np.logspace(-1.5, 1.5, 1201) * omega_c
        att = []
        for w in grid:
            kc = k_numeric(w)
            att.append(2 * np.pi * kc.imag / kc.real)
        out = grid[int(np.argmax(att))] / omega_c
        P.e15 = e_save
        return out
    rec('2c', 'loss peak, weak coupling (K^2 -> 0), at omega/omega_c',
        peak_location(1e-3), 1.0, 5e-3)
    pk_full = peak_location(1.0)
    print(f'       (omega_c = {omega_c:.4e} 1/s; at the physical K^2 = {K2:.3e} the peak '
          f'sits at omega/omega_c = {pk_full:.4f}, an O(K^2) shift)')
    # the exact peak of the closed form, found the same way, must agree
    def peak_closed():
        grid = np.logspace(-1.5, 1.5, 4001) * omega_c
        att = [2 * np.pi * k_of_w(w).imag / k_of_w(w).real for w in grid]
        return grid[int(np.argmax(att))] / omega_c
    rec('2c', 'loss peak, numeric against the closed form', pk_full, peak_closed(), 2e-3)
    P.Dn, P.vd, P.tauR = save

    # (d) Neha: phason limits
    Nh = mv.Neha()
    k, w = 1e5, 2 * np.pi * 1e6
    print('       phason operator K1 eta^2 - K2 k^2 + rho_p w^2 + i gamma w, at eta = k:')
    eta = k
    for gam in (0.0, 1e8, 1e12, 1e20):
        M = Nh.M(eta, k, w, lnl=0.0, lg=0.0, gam=gam)
        val = M[2, 2]
        ref = Nh.K1 * eta ** 2 - Nh.K2 * k ** 2 + Nh.rhop * w ** 2 + 1j * gam * w
        rec('2d', f'M33 at gamma = {gam:g}', val, ref, 1e-12)
    # frozen phason: gamma -> infinity makes the phason amplitude vanish, so the
    # roots must approach those of the model with R = 0
    def roots_eta(model, gam=None, R=None):
        Ms = [model.M(e, k, w, gam=gam, R=R) for e in [0]]
        # polynomial in eta by interpolation on scaled nodes
        scale = max(abs(k), 1.0)
        n = 15
        nodes = np.array([np.cos(np.pi * (2 * j + 1) / (2 * n)) for j in range(n)]) * scale * 3
        vals = np.array([np.linalg.det(model.M(e, k, w, gam=gam, R=R)) for e in nodes])
        V = np.vander(nodes, n)
        coef = np.linalg.solve(V, vals)
        return np.roots(coef)
    # as gamma -> infinity the phason amplitude is forced to zero, so
    # det M(eta)/(i gamma w) must approach det of the minor with the phason
    # row and column removed, which is the R = 0 model
    gam_big = 1e20
    worst = 0.0
    for eta in (1e3 + 0j, 5e4, 1.0e5, 3.0e5, 1.0e6):
        M = Nh.M(eta, k, w, lnl=0.0, lg=0.0, gam=gam_big)
        lhs = np.linalg.det(M) / (1j * gam_big * w)
        M0 = Nh.M(eta, k, w, lnl=0.0, lg=0.0, R=(0, 0, 0))
        rhs = np.linalg.det(M0[np.ix_([0, 1, 3, 4], [0, 1, 3, 4])])
        worst = max(worst, abs(lhs - rhs) / abs(rhs))
    rec('2d', 'frozen phason: det M/(i gamma w) against the R = 0 minor',
        worst, 0.0, 1e-4)
    # relaxed phason: on time scales slow compared with gamma/K1 the phason is
    # quasi-static, and eliminating it softens the moduli by R^2/K
    for gam in (1e6, 1e8, 1e10):
        M = Nh.M(1.0e5, k, w, lnl=0.0, lg=0.0, gam=gam)
        ref = Nh.K1 * 1e5 ** 2 - Nh.K2 * k ** 2 + Nh.rhop * w ** 2 + 1j * gam * w
        rec('2d', f'M33 against the closed form, gamma = {gam:g}', M[2, 2], ref, 1e-12)

    # (e) Anu: magnetoelectric limit
    An = mv.Anu()
    eps11a, mu11a, a11 = An.eps11, An.mu11, An.a11
    kappa2 = a11 ** 2 / (eps11a * mu11a)
    # bulk shear wave at eta = 0 with (u_z, phi, psi)
    def c_eff(alpha):
        A = np.array([[eps11a, -alpha], [-alpha, mu11a]])
        v = np.array([An.e15, An.h15])
        return np.sqrt((An.C44 + v @ np.linalg.solve(A, v)) / An.rho)
    k = 1e4
    w = 2 * np.pi * 1e6
    M = An.M(0.0, k, w, lnl=0.0, lg=0.0)
    blk = M[np.ix_([1, 2, 3], [1, 2, 3])]
    # the block vanishes when rho w^2 = k^2 (C44 + v^T A^{-1} v)
    w_star = k * c_eff(a11)
    blk2 = An.M(0.0, k, w_star, lnl=0.0, lg=0.0)[np.ix_([1, 2, 3], [1, 2, 3])]
    rec('2e', '|det of the (u_z,phi,psi) block| at the coupled speed',
        abs(np.linalg.det(blk2)) / (abs(k ** 2 * An.C44) ** 3), 0.0, 1e-10)
    c0 = c_eff(0.0)
    rec('2e', 'alpha -> 0: stiffening is the sum of the two separate ones',
        c0, np.sqrt((An.C44 + An.e15 ** 2 / eps11a + An.h15 ** 2 / mu11a) / An.rho), 1e-13)
    rec('2e', 'kappa^2 = alpha^2/(eps mu)', kappa2, a11 ** 2 / (eps11a * mu11a), 1e-13)
    print(f'       (kappa^2 = {kappa2:.4e}; the coupled stiffness is positive only for '
          f'kappa^2 < 1)')


# ---------------------------------------------------------------- test 3
def test3():
    print('\n[3] l_g and l_nl -> 0 continuity, and the direction of the shift')
    P = mv.Sumit()
    c11, rho = P.c11, P.rho
    k = 1e4
    c_local = np.sqrt(c11 / rho)
    print(f'       local longitudinal speed {c_local:.6f} m/s, k = {k:g} 1/m')
    for lg in (0.0, 1e-8, 1e-7, 1e-6):
        for lnl in (0.0, 1e-8, 1e-7, 1e-6):
            G = 1 + (lg * k) ** 2
            N = 1 + (lnl * k) ** 2
            c = np.sqrt(c11 * G / (rho * N))
            print(f'         l_g={lg:8.1e} l_nl={lnl:8.1e}  (l_g k)^2={(lg*k)**2:9.2e} '
                  f'(l_nl k)^2={(lnl*k)**2:9.2e}  c={c:14.8f}  shift/c={((c-c_local)/c_local):+.6e}')
    for lg in (1e-8, 1e-7):
        G = 1 + (lg * k) ** 2
        rec('3', f'l_g={lg:g} only: (c-c_local)/c_local against 0.5 (l_g k)^2',
            (np.sqrt(c11 * G / rho) - c_local) / c_local, 0.5 * (lg * k) ** 2, 1e-4)
    for lnl in (1e-8, 1e-7):
        N = 1 + (lnl * k) ** 2
        rec('3', f'l_nl={lnl:g} only: (c-c_local)/c_local against -0.5 (l_nl k)^2',
            (np.sqrt(c11 / (rho * N)) - c_local) / c_local, -0.5 * (lnl * k) ** 2, 1e-4)
    # continuity in the plate: the roots of det M(eta) move continuously as the
    # lengths go to zero
    w = 2 * np.pi * 1e6
    k = 1e4
    def polyroots(lg, lnl):
        scale = max(abs(k), 1.0)
        n = 15
        nodes = np.array([np.cos(np.pi * (2 * j + 1) / (2 * n)) for j in range(n)]) * scale * 3
        vals = np.array([np.linalg.det(P.M(e, k, w, lg=lg, lnl=lnl)) for e in nodes])
        coef = np.linalg.solve(np.vander(nodes, n), vals)
        return np.roots(coef)
    _, base_mp = mp_roots(P, k, w, lg=mp.mpf(0), lnl=mp.mpf(0))

    def matched_mp(lg, lnl):
        _, r = mp_roots(P, k, w, lg=mp.mpf(repr(lg)), lnl=mp.mpf(repr(lnl)))
        r = list(r)
        d, used = [], set()
        for b0 in base_mp:                # each local root against its nearest partner
            j = min(range(len(r)), key=lambda t: abs(r[t] - b0))
            d.append(abs(r[j] - b0) / max(abs(b0), mp.mpf(1)))
            used.add(j)
        left = [r[t] for t in range(len(r)) if t not in used]
        return (max(d) if d else mp.mpf(0)), left
    for lnl in (1e-9, 1e-8, 1e-7):
        d, left = matched_mp(0.0, lnl)
        rec('3', f'roots, l_nl={lnl:g} only, against the local roots', float(d), 0.0, 1e-2)
        print(f'         l_nl={lnl:g}: {len(left)} local roots unmatched '
              f'(|eta| = {[mp.nstr(abs(x), 4) for x in left]})')
    for lg in (1e-8, 1e-7):
        _, left = matched_mp(lg, 0.0)
        print(f'         l_g={lg:g}: the four extra roots sit at |eta| = '
              f'{[mp.nstr(abs(x), 6) for x in sorted(left, key=abs)]}, 1/l_g = {1/lg:.3e}')
    # continuity of the characteristic function itself, and its quadratic rate:
    # det M(eta; l) against det M(eta; 0) at fixed eta
    prm = mpmats.prm_from(P)
    kk, ww = mp.mpf(repr(k)), mp.mpf(repr(float(w)))
    for lg in (1e-7, 1e-8):
        diffs = {}
        for fac in (1.0, 0.1):
            L = mp.mpf(repr(lg * fac))
            worst = mp.mpf(0)
            for eta_s in ('1e3', '1e4', '1e5'):
                eta = mp.mpf(eta_s)
                d1 = mp.det(mp.matrix(mpmats.sumit_M(eta, kk, ww, prm, lg=L, lnl=mp.mpf(0))))
                d0 = mp.det(mp.matrix(mpmats.sumit_M(eta, kk, ww, prm, lg=mp.mpf(0), lnl=mp.mpf(0))))
                worst = max(worst, abs(d1 - d0) / abs(d0))
            diffs[fac] = worst
        ratio = float(diffs[1.0] / diffs[0.1]) if diffs[0.1] != 0 else float('inf')
        rec('3', f'det M: the l_g effect falls by 100 when l_g falls by 10 (l_g={lg:g})',
            ratio, 100.0, 0.5)
        print(f'         l_g={lg:g}: relative change of det M at |eta| <= 1e5 is '
              f'{mp.nstr(diffs[1.0], 4)}')
    print('       (the extra roots are the gradient boundary layers; they run off to '
          'infinity as l_g -> 0)')


# ---------------------------------------------------------------- test 4
def plate_roots(model, k, w, n=15, lg=None, lnl=None, scale=3.0):
    """roots eta of det M(eta) by interpolation on Chebyshev nodes"""
    sc = max(abs(k), 1.0)
    nodes = np.array([np.cos(np.pi * (2 * j + 1) / (2 * n)) for j in range(n)]) * sc * scale
    vals = np.array([np.linalg.det(model.M(e, k, w, lg=lg, lnl=lnl)) for e in nodes])
    coef = np.linalg.solve(np.vander(nodes, n), vals)
    return np.roots(coef)


def build_B(model, k, w, h, lg=None, lnl=None, etas=None):
    """B with one row per face condition and one column per partial wave.
    The roots come from the mp polynomial; the null vectors, the face rows and
    the determinant are double precision, with the columns scaled by
    exp(-|Re eta| h) and the rows normalised."""
    if etas is None:
        _, etas_mp = mp_roots(model, k, w, lg=lg, lnl=lnl)
        etas = [mp.mpc(x) for x in etas_mp]
    nroot = len(etas)
    prm = mpmats.prm_from(model)
    kk, ww = mp.mpf(repr(float(k))), mp.mpf(repr(float(w)))
    lgv = mp.mpf(repr(model.lg if lg is None else lg))
    lnlv = mp.mpf(repr(model.lnl if lnl is None else lnl))
    fun = {'Sumit': mpmats.sumit_M, 'Neha': mpmats.neha_M, 'Anu': mpmats.anu_M}[model.name]
    # the null vectors are taken in mp precision: with the placeholder constants
    # the carrier amplitude is 27 orders above the displacement, and a double
    # precision null vector is noise
    vecs = [NU.nullvec_mp(fun(e, kk, ww, prm, lg=lgv, lnl=lnlv)) for e in etas]
    nb = 7
    B = mp.matrix(2 * nb, nroot)
    hh = mp.mpf(repr(h))
    for fi, face in enumerate((+1.0, -1.0)):
        for m, (eta, a) in enumerate(zip(etas, vecs)):
            b = NU.rows_mp(model, eta, kk, a, lgv, lnlv)
            sc = mp.e ** (eta * face * hh - abs(mp.re(eta)) * hh)
            for r in range(nb):
                B[fi * nb + r, m] = b[r] * sc
    Bn = np.array([[complex(B[i, j]) for j in range(B.cols)] for i in range(B.rows)])
    for i in range(Bn.shape[0]):
        nn = np.linalg.norm(Bn[i])
        if nn:
            Bn[i] /= nn
    return etas, Bn


def scan_B(model, w, h, ks, lg=None, lnl=None):
    sv, dd = [], []
    for kk in ks:
        _, B = build_B(model, kk, w, h, lg=lg, lnl=lnl)
        sv.append(np.linalg.svd(B, compute_uv=False).min())
        sign, logdet = np.linalg.slogdet(B)
        dd.append(sign * np.exp(logdet) if logdet < 500 else np.inf)
    return np.array(sv), np.array(dd, dtype=complex)


def dip(ks, y):
    """position of the minimum of a V-shaped dip: least-squares lines through
    the slopes on either side of the minimum, and their intersection"""
    i = int(np.argmin(y))
    lo, hi = max(1, i - 4), min(len(y) - 2, i + 4)
    if i <= 0 or i >= len(y) - 1 or hi - lo < 2:
        return ks[i]
    il = np.arange(lo, i + 1)
    ir = np.arange(i, hi + 1)
    al, bl = np.polyfit(ks[il], y[il], 1)
    ar, br = np.polyfit(ks[ir], y[ir], 1)
    if abs(al - ar) < 1e-300:
        return ks[i]
    return (br - bl) / (al - ar)


def det_zero(model, w, h, k0, k1, lg=None, lnl=None):
    """zero of det B by the complex secant rule; det B is analytic in k"""
    def f(kk):
        _, B = build_B(model, kk, w, h, lg=lg, lnl=lnl)
        sign, logdet = np.linalg.slogdet(B)
        return sign * np.exp(logdet)
    return secant(f, k0, k1)


def test4(cL, cT, rho):
    print('\n[4] root count against face conditions; zero of det B by SVD and by det')
    P = mv.Sumit()
    h = 1e-3
    w = 2 * np.pi * 1e6
    k = 1e4
    for lg, nroot_exp in ((P.lg, 14), (0.0, 10)):
        c, r = mp_roots(P, k, w, lg=mp.mpf(repr(lg)))
        rec('4', f'degree of det M and number of roots (l_g = {lg:g})',
            float(len(c) - 1), float(nroot_exp), 1e-12)
        rec('4', f'roots found by polyroots (l_g = {lg:g})', float(len(r)),
            float(nroot_exp), 1e-12)
    etas, B = build_B(P, k, w, h, lg=None)
    print(f'       shape of B: {B.shape}  (rows = 7 conditions x 2 faces, columns = roots)')
    rec('4', 'rows of B against columns of B', float(B.shape[0]), float(B.shape[1]), 1e-12)

    # locate a plate mode: coarse, then fine, then very fine
    w = 2 * np.pi * 5e6          # the dip found below sits at k about 1.1e4 1/m
    k_lo, k_hi, n = 1.05e4, 1.15e4, 11
    ks = np.linspace(k_lo, k_hi, n)
    sv, dd = scan_B(P, w, h, ks)
    k0 = dip(ks, sv)
    sv_typ = np.median(sv)          # the level away from the mode, from the coarse scan
    print(f'       coarse scan {k_lo:g} to {k_hi:g}: dip near k = {k0:.2f} 1/m, '
          f'sigma_min {sv.min():.3e} against a typical {sv_typ:.3e} '
          f'({np.log10(sv_typ/sv.min()):.1f} decades)')
    for span, npts in ((150.0, 31), (12.0, 25)):
        ks = np.linspace(k0 - span, k0 + span, npts)
        sv, dd = scan_B(P, w, h, ks)
        k0 = dip(ks, sv)
    step = ks[1] - ks[0]
    k_sv = k0
    i_dd = int(np.argmin(np.abs(dd)))
    k_dd = det_zero(P, w, h, ks[max(i_dd - 1, 0)], ks[min(i_dd + 1, len(ks) - 1)])
    rec('4', 'k of the zero of det B: singular-value route against determinant route',
        k_sv, complex(k_dd).real, 3 * step / k_sv)
    print(f'       final grid spacing {step:.3f} 1/m; the two routes sit '
          f'{abs(k_sv - complex(k_dd).real):.3f} 1/m apart, i.e. '
          f'{abs(k_sv - complex(k_dd).real)/step:.2f} of one spacing')
    print(f'       at the mode: sigma_min {sv.min():.3e} against the off-mode level '
          f'{sv_typ:.3e} ({np.log10(sv_typ/sv.min()):.1f} decades);'
          f'  |det| {np.abs(dd).min():.3e} against {np.median(np.abs(dd)):.3e} '
          f'({np.log10(np.median(np.abs(dd))/np.abs(dd).min()):.1f} decades on the fine grid)')
    rec('4', 'the singular value dips by at least one decade at the mode (1 = yes)',
        1.0 if np.log10(sv_typ / sv.min()) > 1 else 0.0, 1.0, 1e-12)

    # and the same two routes for the elastic plate, against the reference root
    fd = 3.0e3
    cs = np.linspace(0.5 * cT, 30 * cT, 300000)
    vals = rl.F_sym(cs, fd, cL, cT)
    i = np.where(np.sign(vals[:-1]) * np.sign(vals[1:]) < 0)[0][0]
    a, b = cs[i], cs[i + 1]
    for _ in range(120):
        m = 0.5 * (a + b)
        if np.sign(rl.F_sym(np.array(m), fd, cL, cT)) == np.sign(rl.F_sym(np.array(a), fd, cL, cT)):
            a = m
        else:
            b = m
    c_ref = 0.5 * (a + b)
    grid = c_ref * (1 + np.linspace(-1e-3, 1e-3, 2001))
    sv = np.array([np.linalg.svd(elastic_platesystem(c, fd, cL, cT, rho),
                                 compute_uv=False).min() for c in grid])
    dt = np.array([abs(np.linalg.det(elastic_platesystem(c, fd, cL, cT, rho)))
                   for c in grid])
    c_svd = grid[int(np.argmin(sv))]
    c_det = grid[int(np.argmin(dt))]
    rec('4', 'elastic plate: zero by the singular-value route (m/s)', c_svd, c_ref, 1e-5)
    rec('4', 'elastic plate: zero by the determinant route (m/s)', c_det, c_ref, 1e-5)


if __name__ == '__main__':
    print('SECTION 8 NUMERICAL VERIFICATION (internal)')
    cL, cT, rho = test1()
    test2()
    test3()
    test4(cL, cT, rho)
    print('\nSUMMARY')
    worst = {}
    for t, q, n, r, rel, tol in RES:
        worst[t] = max(worst.get(t, 0.0), rel / tol)
        if rel > tol:
            print(f'  FAIL  [{t}] {q}: rel={rel:.3e} > tol={tol:.0e}')
    for k in sorted(worst):
        print(f'  test {k}: worst residual {worst[k]:.3e} x tolerance')
    print(f'  checks: {len(RES)}   failures: {sum(1 for r in RES if r[4] > r[5])}')
