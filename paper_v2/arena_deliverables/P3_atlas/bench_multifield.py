#!/usr/bin/env python3
"""BK-15: the multifield (magneto-electro-elastic) invariant.

The six multifield atlas cases - AT-04, AT-05, AT-06, AT-09, AT-13, AT-40 - carried
`coverage = no` for one stated reason: "no coupled-field invariant exists: piezo/magneto
branch speeds need the coupled constitutive matrix". Inventing a coupled material would have
meant publishing numbers about a body nobody uses, so the case waited. Eringen and Maugin,
*Electrodynamics of Continua I* (1990), **§5.11, printed pp. 165-166, eqs. (5.11.4)-(5.11.6)**,
print the matrix:

    ^E T_KL = A_KL - B_KL T + C_KLMN E_MN - e_MKL E_M - q_MKL B_M      (5.11.4)
    P_K     = P0_K + w_K T + chi^E_KL E_L + e_KLM E_LM + A_KL B_L       (5.11.5)
    M_K     = M0_K + G_K T + chi^B_KL B_L + q_KLM E_LM + A_LK E_L       (5.11.6)

and (5.11.1) prints the single quadratic free energy that all of these moduli come from.  That
is what makes a *coupled-field invariant* possible, and this file tests six consequences of it,
none of which needs a fitted material:

    I1  the 12x12 Hessian of the free energy is symmetric - it is one quadratic form;
    I2  it is positive definite - a stable material;
    I3  the open-circuit (D = 0, B = 0) elastic tensor is stiffened: C* - C is PSD;
    I4  every acoustic branch is real, and the coupled speeds are never below the bare ones,
        over 48 directions;
    I5  the 6mm piezoelectric limit reproduces v^2 = (C44 + e15^2/chi11)/rho exactly;
    I6  switching the coupling off returns C exactly, and a huge dielectric constant
        (short circuit) makes the piezoelectric stiffening vanish.

Output: bench_multifield_results.csv.  check_multifield.py recomputes all six.
"""
import csv
import os
import random

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "bench_multifield_results.csv")
RHO = 7500.0
VOIGT = [(0, 0), (1, 1), (2, 2), (1, 2), (0, 2), (0, 1)]


def hex_elastic(C11=2.71e11, C12=0.91e11, C13=0.83e11, C33=2.12e11, C44=0.55e11):
    C66 = 0.5*(C11 - C12)
    return np.array([[C11, C12, C13, 0, 0, 0],
                     [C12, C11, C13, 0, 0, 0],
                     [C13, C13, C33, 0, 0, 0],
                     [0, 0, 0, C44, 0, 0],
                     [0, 0, 0, 0, C44, 0],
                     [0, 0, 0, 0, 0, C66]], dtype=float)


def voigt_to_tensor(C6):
    """6x6 Voigt stiffness -> 3x3x3x3, with the engineering-shear convention."""
    T = np.zeros((3, 3, 3, 3))
    for a, (i, j) in enumerate(VOIGT):
        for b, (k, l) in enumerate(VOIGT):
            for ii, jj in {(i, j), (j, i)}:
                for kk, ll in {(k, l), (l, k)}:
                    T[ii, jj, kk, ll] = C6[a, b]
    return T


def hessian(C6, e36, q36, chi, mu, lam):
    """Hessian of (5.11.1) in the conjugate pairs (E, T), (E_k, -P_k), (B_k, -M_k) - the
    arrangement in which (5.11.4)-(5.11.6) is manifestly the gradient of one potential."""
    W = np.zeros((12, 12))
    W[:6, :6] = C6
    W[:6, 6:9] = -e36.T
    W[6:9, :6] = -e36
    W[:6, 9:12] = -q36.T
    W[9:12, :6] = -q36
    W[6:9, 6:9] = chi
    W[9:12, 9:12] = mu
    W[6:9, 9:12] = lam
    W[9:12, 6:9] = lam.T
    return W


def open_circuit(C6, e36, q36, chi, mu, lam):
    """D = 0, B = 0: the textbook elimination, C* = C + K D^-1 K^T with K = [e^T, q^T] and
    D the (3+3)-block of chi^E, chi^B and Lambda. Positive-definite D makes C* - C PSD."""
    K = np.hstack([e36.T, q36.T])
    D = np.block([[chi, lam], [lam.T, mu]])
    return C6 + K @ np.linalg.solve(D, K.T)


def christoffel(Ct, n):
    G = np.einsum("ijkl,j,l->ik", Ct, n, n)
    return 0.5*(G + G.T)


def lambdas(Ct, n):
    return np.linalg.eigvalsh(christoffel(Ct, n))


def main():
    rows = []
    rng = random.Random(15)
    dirs = []
    for _ in range(48):
        v = np.array([rng.gauss(0, 1) for _ in range(3)])
        dirs.append(v/np.linalg.norm(v))

    C = hex_elastic()
    e36 = np.zeros((3, 6)); e36[0, 4] = 0.05; e36[1, 3] = 0.05
    q36 = np.zeros((3, 6)); q36[0, 4] = 0.30; q36[1, 3] = 0.30
    chi = np.diag([1.2e-8, 1.2e-8, 1.4e-8])
    mu = np.diag([3.0e-4, 3.0e-4, 3.6e-4])
    lam = np.array([[0.0, 0.0, 1.0e-6], [0.0, 0.0, 0.0], [1.0e-6, 0.0, 0.0]])
    lam = 0.5*(lam + lam.T)

    W = hessian(C, e36, q36, chi, mu, lam)
    asym = float(np.max(np.abs(W - W.T)))
    rows.append(("I1", "the 12x12 Hessian of (5.11.1) is symmetric",
                 "max |W - W^T|", "%.3e" % asym, "0", asym < 1e-3,
                 "PASS" if asym < 1e-3 else "FAIL"))

    # W mixes 1e11 elastic moduli with 1e-8 dielectric ones, so its raw spectrum is useless in
    # double precision; PD is a congruence-invariant property, so scale to unit diagonal first.
    dscale = np.sqrt(np.diag(W))
    Wn = 0.5*((W/dscale[:, None])/dscale[None, :] + ((W/dscale[:, None])/dscale[None, :]).T)
    evW = np.linalg.eigvalsh(Wn)
    rows.append(("I2", "the Hessian is positive definite (stable material; min eigenvalue after "
                 "diagonal scaling)", "min eigenvalue of D^-1/2 W D^-1/2", "%.6e" % evW.min(),
                 "> 0", evW.min() > 0, "PASS" if evW.min() > 0 else "FAIL"))

    Cstar = open_circuit(C, e36, q36, chi, mu, lam)
    dC = Cstar - C
    evd = np.linalg.eigvalsh(0.5*(dC + dC.T))
    rel_stiff = float(np.max(np.diag(dC))/np.max(np.diag(C)))
    rows.append(("I3", "open circuit stiffens: C* - C is positive semi-definite and non-trivial",
                 "min, max eigenvalue of C* - C; relative stiffening",
                 "%.3e, %.6e; %.2e" % (evd.min(), evd.max(), rel_stiff), ">= 0; > 1e4; > 1e-6",
                 evd.min() > -1e-3 and evd.max() > 1e4 and rel_stiff > 1e-6,
                 "PASS" if (evd.min() > -1e-3 and evd.max() > 1e4 and rel_stiff > 1e-6) else "FAIL"))

    Cbare = voigt_to_tensor(C)
    Cst = voigt_to_tensor(Cstar)
    worst = 1e9
    allreal = True
    for n in dirs:
        lb = lambdas(Cbare, n)
        lc = lambdas(Cst, n)
        worst = min(worst, float(np.min(lc - lb)))
        allreal = allreal and bool(np.all(lc > 0))
    rows.append(("I4", "all branches real; coupled speeds never below the bare ones (48 directions)",
                 "min of (lambda_coupled - lambda_bare)", "%.6e" % worst, ">= 0",
                 worst > -1e-3 and allreal, "PASS" if (worst > -1e-3 and allreal) else "FAIL"))

    e15 = np.zeros((3, 6)); e15[0, 4] = 0.05
    q0 = np.zeros((3, 6))
    C5 = open_circuit(C, e15, q0, chi, mu, np.zeros((3, 3)))
    closed = C[4, 4] + 0.05**2/1.2e-8
    rel = abs(C5[4, 4] - closed)/abs(closed)
    rows.append(("I5", "6mm piezo limit reproduces C44* = C44 + e15^2/chi11 exactly",
                 "relative error on C44*", "%.3e" % rel, "0", rel < 1e-12,
                 "PASS" if rel < 1e-12 else "FAIL"))

    Cz = open_circuit(C, np.zeros((3, 6)), np.zeros((3, 6)), chi, mu, lam)
    dec = float(np.max(np.abs(Cz - C)))
    big = np.diag([1.2e-8*1e12, 1.2e-8*1e12, 1.4e-8*1e12])
    Csc = open_circuit(C, e36, np.zeros((3, 6)), big, mu, lam)
    ratio = float(np.max(np.diag(Csc - C))/np.max(np.diag(dC)))
    rows.append(("I6", "no coupling returns C exactly; short circuit kills the piezo stiffening",
                 "max |C(e=q=0) - C|; stiffening ratio chi*1e12 vs chi",
                 "%.3e; %.3e" % (dec, ratio), "0; < 1e-9",
                 dec < 1e-3 and ratio < 1e-9, "PASS" if (dec < 1e-3 and ratio < 1e-9) else "FAIL"))

    with open(OUT, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["invariant", "what_it_tests", "measured_quantity", "measured", "required",
                    "ok", "verdict"])
        for r in rows:
            w.writerow([r[0], r[1], r[2], r[3], r[4], r[5], r[6]])
    for r in rows:
        print("%-3s %-5s %-62s %s" % (r[0], r[6], r[1][:62], r[3]))
    print("wrote", OUT)


if __name__ == "__main__":
    main()
