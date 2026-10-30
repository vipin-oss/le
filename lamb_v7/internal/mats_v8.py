#!/usr/bin/env python3
"""Numeric 5x5 matrices and face-row functions for the three papers.

Internal only. Written from the entries as they stand in the masters, with
placeholder constants at physical scale. Nothing here reaches a scholar file.
"""
import numpy as np


# ------------------------------------------------------------------ Paper A
class Sumit:
    name = 'Sumit'
    labels = ['u_x', 'u_z', 'phi', 'n', 'theta']

    def __init__(self):
        p = self
        # ZnO-scale placeholders (Set L of the internal notes)
        p.c11, p.c13, p.c33, p.c44 = 209.7e9, 105.4e9, 211.2e9, 42.4e9
        p.e31, p.e33, p.e15 = -0.57, 1.32, -0.48
        p.eps11 = 8.854e-12 * 8.54
        p.eps33 = 8.854e-12 * 10.2
        p.b1, p.b3 = 1.7e6, 1.5e6
        p.beta_th, p.Pi_th, p.Eg = 2.5e5, 0.05, 1.2e-19
        p.p3, p.qcar = 0.5, 1.602e-19
        p.rho, p.c_p, p.kth, p.T0 = 5680.0, 3.4e6, 60.0, 300.0
        p.Dn, p.bn, p.n0, p.vd, p.tauR = 1e-3, 0.02, 1e21, 1e3, 1e-9
        p.lnl, p.lg = 2e-7, 3e-7
        p.tau_q = 1e-11

    def M(self, eta, k, w, lnl=None, lg=None):
        p = self
        lnl = p.lnl if lnl is None else lnl
        lg = p.lg if lg is None else lg
        L = eta ** 2 - k ** 2
        N = 1 + lnl ** 2 * (k ** 2 - eta ** 2)
        G = 1 + lg ** 2 * (k ** 2 - eta ** 2)
        f = 1 - 1j * w * p.tau_q
        M = np.zeros((5, 5), dtype=complex)
        M[0, 0] = -N * p.rho * w ** 2 + G * (p.c11 * k ** 2 - p.c44 * eta ** 2)
        M[0, 1] = -1j * k * eta * G * (p.c13 + p.c44)
        M[0, 2] = -1j * k * eta * (p.e31 + p.e15)
        M[0, 4] = 1j * k * p.b1
        M[1, 0] = M[0, 1]
        M[1, 1] = -N * p.rho * w ** 2 + G * (p.c44 * k ** 2 - p.c33 * eta ** 2)
        M[1, 2] = p.e15 * k ** 2 - p.e33 * eta ** 2
        M[1, 4] = eta * p.b3
        M[2, 0] = 1j * k * eta * (p.e15 + p.e31)
        M[2, 1] = p.e33 * eta ** 2 - p.e15 * k ** 2
        M[2, 2] = p.eps11 * k ** 2 - p.eps33 * eta ** 2
        M[2, 3] = p.qcar
        M[2, 4] = eta * p.p3
        M[3, 2] = p.bn * p.n0 * L
        M[3, 3] = -1j * w - p.Dn * L - 1j * k * p.vd + 1.0 / p.tauR
        M[3, 4] = -p.beta_th * L
        M[4, 0] = f * p.T0 * w * k * p.b1
        M[4, 1] = -1j * w * f * p.T0 * p.b3 * eta
        M[4, 2] = 1j * w * f * p.T0 * p.p3 * eta
        M[4, 3] = f * (-1j * w * p.qcar * p.Pi_th + p.Eg / p.tauR)
        M[4, 4] = -1j * w * f * p.rho * p.c_p - p.kth * L
        return M

    def sigmas(self, eta, k, w, a, lg=None):
        """(sigma_zz, sigma_xz) amplitudes for the amplitudes a"""
        p = self
        lg = p.lg if lg is None else lg
        G = 1 + lg ** 2 * (k ** 2 - eta ** 2)
        X, Z, Ph, Nu, Th = a
        szz = G * (1j * k * p.c13 * X + eta * p.c33 * Z) + eta * p.e33 * Ph - p.b3 * Th
        sxz = G * p.c44 * (eta * X + 1j * k * Z) + 1j * k * p.e15 * Ph
        return szz, sxz

    def rows(self, eta, k, w, a, lg=None, lnl=None):
        """the seven face-row functions b_1..b_7 of Calculation F"""
        p = self
        lg = p.lg if lg is None else lg
        lnl = p.lnl if lnl is None else lnl
        N = 1 + lnl ** 2 * (k ** 2 - eta ** 2)
        X, Z, Ph, Nu, Th = a
        szz, sxz = self.sigmas(eta, k, w, a, lg)
        b = np.zeros(7, dtype=complex)
        b[0] = (szz - lg ** 2 * 1j * k * eta * p.c44 * (eta * X + 1j * k * Z)) / N
        b[1] = (sxz - lg ** 2 * 1j * k * eta * (1j * k * p.c11 * X + eta * p.c13 * Z)) / N
        b[2] = lg ** 2 * eta * p.c44 * (eta * X + 1j * k * Z) / N
        b[3] = lg ** 2 * eta * (1j * k * p.c13 * X + eta * p.c33 * Z) / N
        b[4] = 1j * k * p.e31 * X + eta * p.e33 * Z - eta * p.eps33 * Ph + p.p3 * Th
        b[5] = -p.Dn * eta * Nu + p.bn * p.n0 * eta * Ph - p.beta_th * eta * Th
        b[6] = eta * Th
        return b


# ------------------------------------------------------------------ Paper B
class Neha:
    name = 'Neha'
    labels = ['u_x', 'u_z', 'w', 'phi', 'theta']

    def __init__(self):
        p = self
        p.C11, p.C13, p.C33, p.C44 = 150e9, 60e9, 130e9, 40e9
        p.K1, p.K2 = 30e9, 20e9
        p.R1, p.R2, p.R3 = 2e9, 3e9, 1.5e9
        p.e31, p.e33, p.e15 = 0.4, 1.1, 0.3
        p.eps11 = 8.854e-12 * 8.54
        p.eps33 = 8.854e-12 * 10.2
        p.b1, p.b3, p.bw = 1.7e6, 1.5e6, 1.0e6
        p.p3 = 0.5
        p.rho, p.rhop, p.gam = 4200.0, 12.0, 1e8
        p.c_p, p.kth, p.T0 = 2.9e6, 4.0, 300.0
        p.lnl, p.lg = 2e-7, 3e-7
        p.tau_q = 1e-11

    def M(self, eta, k, w, lnl=None, lg=None, gam=None, R=None):
        p = self
        lnl = p.lnl if lnl is None else lnl
        lg = p.lg if lg is None else lg
        gam = p.gam if gam is None else gam
        R1, R2, R3 = (p.R1, p.R2, p.R3) if R is None else tuple(R)
        L = eta ** 2 - k ** 2
        N = 1 + lnl ** 2 * (k ** 2 - eta ** 2)
        G = 1 + lg ** 2 * (k ** 2 - eta ** 2)
        f = 1 - 1j * w * p.tau_q
        M = np.zeros((5, 5), dtype=complex)
        M[0, 0] = -N * p.rho * w ** 2 + G * (p.C11 * k ** 2 - p.C44 * eta ** 2)
        M[0, 1] = -1j * k * eta * G * (p.C13 + p.C44)
        M[0, 2] = -1j * k * eta * (R1 + R3)
        M[0, 3] = -1j * k * eta * (p.e31 + p.e15)
        M[0, 4] = 1j * k * p.b1
        M[1, 0] = M[0, 1]
        M[1, 1] = -N * p.rho * w ** 2 + G * (p.C44 * k ** 2 - p.C33 * eta ** 2)
        M[1, 2] = R3 * k ** 2 - R2 * eta ** 2
        M[1, 3] = p.e15 * k ** 2 - p.e33 * eta ** 2
        M[1, 4] = eta * p.b3
        M[2, 0] = 1j * k * eta * (R1 + R3)
        M[2, 1] = R2 * eta ** 2 - R3 * k ** 2
        M[2, 2] = p.K1 * eta ** 2 - p.K2 * k ** 2 + p.rhop * w ** 2 + 1j * gam * w
        M[2, 4] = eta * p.bw
        M[3, 0] = 1j * k * eta * (p.e15 + p.e31)
        M[3, 1] = p.e33 * eta ** 2 - p.e15 * k ** 2
        M[3, 3] = p.eps11 * k ** 2 - p.eps33 * eta ** 2
        M[3, 4] = eta * p.p3
        M[4, 0] = f * p.T0 * w * k * p.b1
        M[4, 1] = -1j * w * f * p.T0 * p.b3 * eta
        M[4, 2] = -1j * w * f * p.T0 * p.bw * eta
        M[4, 3] = 1j * w * f * p.T0 * p.p3 * eta
        M[4, 4] = -1j * w * f * p.rho * p.c_p - p.kth * L
        return M


# ------------------------------------------------------------------ Paper C
class Anu:
    name = 'Anu'
    labels = ['u_x', 'u_z', 'phi', 'psi', 'theta']

    def __init__(self):
        p = self
        p.C11, p.C13, p.C33, p.C44 = 220e9, 110e9, 215e9, 45e9
        p.e31, p.e33, p.e15 = 12.0, 15.0, -4.5
        p.h31, p.h33, p.h15 = 200.0, 250.0, 100.0
        p.a11, p.a33 = 1.2e-9, 3.4e-9
        p.eps11 = 8.854e-12 * 8.0
        p.eps33 = 8.854e-12 * 9.0
        p.mu11 = 1.2566e-6 * 2.0
        p.mu33 = 1.2566e-6 * 1.5
        p.b1, p.b3 = 1.7e6, 1.5e6
        p.p3, p.m3 = 0.5, 0.05
        p.rho, p.c_p, p.kth, p.T0 = 5500.0, 3.2e6, 6.0, 300.0
        p.lnl, p.lg = 2e-7, 3e-7
        p.tau_q = 1e-11

    def M(self, eta, k, w, lnl=None, lg=None, al=None):
        p = self
        lnl = p.lnl if lnl is None else lnl
        lg = p.lg if lg is None else lg
        a11, a33 = (p.a11, p.a33) if al is None else al
        L = eta ** 2 - k ** 2
        N = 1 + lnl ** 2 * (k ** 2 - eta ** 2)
        G = 1 + lg ** 2 * (k ** 2 - eta ** 2)
        f = 1 - 1j * w * p.tau_q
        M = np.zeros((5, 5), dtype=complex)
        M[0, 0] = -N * p.rho * w ** 2 + G * (p.C11 * k ** 2 - p.C44 * eta ** 2)
        M[0, 1] = -1j * k * eta * G * (p.C13 + p.C44)
        M[0, 2] = -1j * k * eta * (p.e31 + p.e15)
        M[0, 3] = -1j * k * eta * (p.h31 + p.h15)
        M[0, 4] = 1j * k * p.b1
        M[1, 0] = M[0, 1]
        M[1, 1] = -N * p.rho * w ** 2 + G * (p.C44 * k ** 2 - p.C33 * eta ** 2)
        M[1, 2] = p.e15 * k ** 2 - p.e33 * eta ** 2
        M[1, 3] = p.h15 * k ** 2 - p.h33 * eta ** 2
        M[1, 4] = eta * p.b3
        M[2, 0] = 1j * k * eta * (p.e15 + p.e31)
        M[2, 1] = p.e33 * eta ** 2 - p.e15 * k ** 2
        M[2, 2] = p.eps11 * k ** 2 - p.eps33 * eta ** 2
        M[2, 3] = a33 * eta ** 2 - a11 * k ** 2
        M[2, 4] = eta * p.p3
        M[3, 0] = 1j * k * eta * (p.h15 + p.h31)
        M[3, 1] = p.h33 * eta ** 2 - p.h15 * k ** 2
        M[3, 2] = a33 * eta ** 2 - a11 * k ** 2
        M[3, 3] = p.mu11 * k ** 2 - p.mu33 * eta ** 2
        M[3, 4] = eta * p.m3
        M[4, 0] = f * p.T0 * w * k * p.b1
        M[4, 1] = -1j * w * f * p.T0 * p.b3 * eta
        M[4, 2] = 1j * w * f * p.T0 * p.p3 * eta
        M[4, 3] = 1j * w * f * p.T0 * p.m3 * eta
        M[4, 4] = -1j * w * f * p.rho * p.c_p - p.kth * L
        return M
