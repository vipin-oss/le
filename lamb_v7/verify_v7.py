#!/usr/bin/env python3
"""v7 internal check: degree in eta and the eta-parity of det M(eta), three papers.

The matrices are the ones written out in the three masters, with placeholder
constants (internal only). det M is sampled on a circle in eta at 60 digits,
Fourier-fitted to a polynomial, and the coefficients are inspected: the highest
non-zero power gives the degree, and the odd coefficients decide the parity.
Nothing on this page goes into a scholar file.
"""
import mpmath as mp

mp.mp.dps = 90
I = mp.mpc(0, 1)
K = mp.mpf('1234.5')
W = mp.mpf('6.283185307179586') * mp.mpf('1e6')


def ops(eta, lg, lnl):
    L = eta**2 - K**2
    return L, 1 + lnl**2 * (K**2 - eta**2), 1 + lg**2 * (K**2 - eta**2)


def sumit(eta, lg=0.3, lnl=0.2, bth=1.7, pith=2.3, e=(1.1, 2.2, 3.3), p3=0.9):
    L, N, G = ops(eta, lg, lnl)
    c11, c13, c33, c44 = 209.7, 121.1, 211.2, 42.4
    e31, e33, e15 = e
    b1, b3 = mp.mpf('1.7e6'), mp.mpf('1.5e6')
    rho, Dn, bn, n0, vd, tauR = 5680., mp.mpf('1e-6'), 0.02, mp.mpf('1e21'), 12.0, mp.mpf('1e-9')
    c_p, kth, T0, q = mp.mpf('3.4e6'), 60., 300., mp.mpf('1.6e-19')
    f = 1 - I * W * mp.mpf('1e-11')
    M = mp.zeros(5, 5)
    M[0, 0] = -N * rho * W**2 + G * (c11 * K**2 - c44 * eta**2)
    M[0, 1] = -I * K * eta * G * (c13 + c44)
    M[0, 2] = -I * K * eta * (e31 + e15)
    M[0, 4] = I * K * b1
    M[1, 0] = M[0, 1]
    M[1, 1] = -N * rho * W**2 + G * (c44 * K**2 - c33 * eta**2)
    M[1, 2] = e15 * K**2 - e33 * eta**2
    M[1, 4] = eta * b3
    M[2, 0] = I * K * eta * (e15 + e31)
    M[2, 1] = e33 * eta**2 - e15 * K**2
    M[2, 2] = mp.mpf('8.854e-12') * 8.54 * K**2 - mp.mpf('8.854e-12') * 10.2 * eta**2
    M[2, 3] = q
    M[2, 4] = eta * p3
    M[3, 2] = bn * n0 * L
    M[3, 3] = -I * W - Dn * L - I * K * vd + 1 / tauR
    M[3, 4] = -bth * L
    M[4, 0] = f * T0 * W * K * b1
    M[4, 1] = -I * W * f * T0 * b3 * eta
    M[4, 2] = I * W * f * T0 * p3 * eta
    M[4, 3] = f * (-I * W * q * pith + mp.mpf('1.2e-19') / tauR)
    M[4, 4] = -I * W * f * c_p - kth * L
    return M


def neha(eta, lg=0.3, lnl=0.2, R=(1.1, 2.2, 3.3), bth=mp.mpf('1e6'), bw=mp.mpf('8e5')):
    L, N, G = ops(eta, lg, lnl)
    C11, C13, C33, C44 = 150., 60., 130., 40.
    K1, K2 = 30., 20.
    R1, R2, R3 = R
    e31, e33, e15, p3 = 0.4, 1.1, 0.3, 0.7
    rho, rhop, gam = 4200., 12.0, mp.mpf('1e8')
    c_p, kth, T0 = mp.mpf('2.9e6'), 4.0, 300.
    f = 1 - I * W * mp.mpf('1e-11')
    M = mp.zeros(5, 5)
    M[0, 0] = -N * rho * W**2 + G * (C11 * K**2 - C44 * eta**2)
    M[0, 1] = -I * K * eta * G * (C13 + C44)
    M[0, 2] = -I * K * eta * (R1 + R3)
    M[0, 3] = -I * K * eta * (e31 + e15)
    M[0, 4] = I * K * bth
    M[1, 0] = M[0, 1]
    M[1, 1] = -N * rho * W**2 + G * (C44 * K**2 - C33 * eta**2)
    M[1, 2] = R3 * K**2 - R2 * eta**2
    M[1, 3] = e15 * K**2 - e33 * eta**2
    M[1, 4] = eta * bth
    M[2, 0] = I * K * eta * (R1 + R3)
    M[2, 1] = R2 * eta**2 - R3 * K**2
    M[2, 2] = K1 * eta**2 - K2 * K**2 + rhop * W**2 + I * gam * W
    M[2, 4] = eta * bw
    M[3, 0] = I * K * eta * (e15 + e31)
    M[3, 1] = e33 * eta**2 - e15 * K**2
    M[3, 3] = mp.mpf('8.854e-12') * 10.2 * eta**2 - mp.mpf('8.854e-12') * 8.54 * K**2
    M[3, 4] = eta * p3
    M[4, 0] = f * T0 * W * K * bth
    M[4, 1] = -I * W * f * T0 * bth * eta
    M[4, 2] = -I * W * f * T0 * bw * eta
    M[4, 3] = I * W * f * T0 * p3 * eta
    M[4, 4] = -I * W * f * c_p - kth * L
    return M


def anu(eta, lg=0.3, lnl=0.2, al=(mp.mpf('1.2e-9'), mp.mpf('3.4e-9'))):
    L, N, G = ops(eta, lg, lnl)
    C11, C13, C33, C44 = 220., 110., 215., 45.
    e31, e33, e15 = 0.4, 1.1, 0.3
    h31, h33, h15 = 0.2, 0.6, 0.15
    a11, a33 = al
    eps11, eps33 = mp.mpf('8.854e-12') * 8.0, mp.mpf('8.854e-12') * 9.0
    mu11, mu33 = mp.mpf('1.26e-6') * 2.0, mp.mpf('1.26e-6') * 1.5
    p3, m3 = 0.7, 0.5
    b1, b3 = mp.mpf('1.7e6'), mp.mpf('1.5e6')
    rho, c_p, kth, T0 = 5500., mp.mpf('3.2e6'), 6.0, 300.
    f = 1 - I * W * mp.mpf('1e-11')
    M = mp.zeros(5, 5)
    M[0, 0] = -N * rho * W**2 + G * (C11 * K**2 - C44 * eta**2)
    M[0, 1] = -I * K * eta * G * (C13 + C44)
    M[0, 2] = -I * K * eta * (e31 + e15)
    M[0, 3] = -I * K * eta * (h31 + h15)
    M[0, 4] = I * K * b1
    M[1, 0] = M[0, 1]
    M[1, 1] = -N * rho * W**2 + G * (C44 * K**2 - C33 * eta**2)
    M[1, 2] = e15 * K**2 - e33 * eta**2
    M[1, 3] = h15 * K**2 - h33 * eta**2
    M[1, 4] = eta * b3
    M[2, 0] = I * K * eta * (e15 + e31)
    M[2, 1] = e33 * eta**2 - e15 * K**2
    M[2, 2] = eps33 * eta**2 - eps11 * K**2
    M[2, 3] = a33 * eta**2 - a11 * K**2
    M[2, 4] = eta * p3
    M[3, 0] = I * K * eta * (h15 + h31)
    M[3, 1] = h33 * eta**2 - h15 * K**2
    M[3, 2] = M[2, 3]
    M[3, 3] = mu33 * eta**2 - mu11 * K**2
    M[3, 4] = eta * m3
    M[4, 0] = f * T0 * W * K * b1
    M[4, 1] = -I * W * f * T0 * b3 * eta
    M[4, 2] = I * W * f * T0 * p3 * eta
    M[4, 3] = I * W * f * T0 * m3 * eta
    M[4, 4] = -I * W * f * c_p - kth * L
    return M


def report(name, build):
    """Parity by direct comparison of det(eta) and det(-eta); degree by scaling."""
    worst = mp.mpf(0)
    scale = mp.mpf(0)
    for e in ['0.7', '3.3', '17.9', '91.7']:
        eta = mp.mpf(e)
        a, b = mp.det(build(eta)), mp.det(build(-eta))
        worst = max(worst, abs(a - b) / max(abs(a), abs(b)))
    # degree: ratio det(L eta)/det(eta) -> L^deg for large eta
    L = mp.mpf(4)
    r = abs(mp.det(build(100 * L)) / mp.det(build(100)))
    deg = mp.log(r) / mp.log(L)
    verdict = 'EVEN (split exists)' if worst < mp.mpf('1e-25') else 'NOT even (no split)'
    print(f'{name:34s} deg~{float(deg):5.1f}  max|d(eta)-d(-eta)|/|d|={float(worst):.1e}   {verdict}')
    return deg, worst


if __name__ == '__main__':
    print('det M: parity by comparing d(eta) with d(-eta); degree from d(4 eta)/d(eta). dps 90\n')
    print('--- Sumit ---')
    report('full: beta_th, Pi_th on', sumit)
    report('Pi_th = 0, beta_th on', lambda e: sumit(e, pith=0))
    report('beta_th = 0, Pi_th on', lambda e: sumit(e, bth=0))
    report('both off', lambda e: sumit(e, bth=0, pith=0))
    report('both off, no piezo/pyro', lambda e: sumit(e, bth=0, pith=0, e=(0, 0, 0), p3=0))
    report('l_g = 0 (full)', lambda e: sumit(e, lg=0.0))
    report('l_g = 0, both off', lambda e: sumit(e, lg=0.0, bth=0, pith=0))
    report('l_g = 0, l_nl = 0, both off', lambda e: sumit(e, lg=0.0, lnl=0.0, bth=0, pith=0))
    print('\n--- Neha ---')
    report('full', neha)
    report('l_g = 0', lambda e: neha(e, lg=0.0))
    print('\n--- Anu ---')
    report('full', anu)
    report('l_g = 0', lambda e: anu(e, lg=0.0))
    report('alpha = 0', lambda e: anu(e, al=(mp.mpf(0), mp.mpf(0))))
