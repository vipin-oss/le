"""mp-precision versions of the three 5x5 matrices, for polynomial work.

Internal only. The formulas are those written in the masters; the arithmetic
is done in mp precision because the size-effect terms are 30 orders of
magnitude below the leading entries and are lost in double precision.
"""
import mpmath as mp


def sumit_M(eta, k, w, prm, lg=None, lnl=None):
    p = prm
    lg = p['lg'] if lg is None else lg
    lnl = p['lnl'] if lnl is None else lnl
    L = eta ** 2 - k ** 2
    N = 1 + lnl ** 2 * (k ** 2 - eta ** 2)
    G = 1 + lg ** 2 * (k ** 2 - eta ** 2)
    f = 1 - mp.mpc(0, 1) * w * p['tau_q']
    M = [[mp.mpc(0)] * 5 for _ in range(5)]
    M[0][0] = -N * p['rho'] * w ** 2 + G * (p['c11'] * k ** 2 - p['c44'] * eta ** 2)
    M[0][1] = -mp.mpc(0, 1) * k * eta * G * (p['c13'] + p['c44'])
    M[0][2] = -mp.mpc(0, 1) * k * eta * (p['e31'] + p['e15'])
    M[0][4] = mp.mpc(0, 1) * k * p['b1']
    M[1][0] = M[0][1]
    M[1][1] = -N * p['rho'] * w ** 2 + G * (p['c44'] * k ** 2 - p['c33'] * eta ** 2)
    M[1][2] = p['e15'] * k ** 2 - p['e33'] * eta ** 2
    M[1][4] = eta * p['b3']
    M[2][0] = mp.mpc(0, 1) * k * eta * (p['e15'] + p['e31'])
    M[2][1] = p['e33'] * eta ** 2 - p['e15'] * k ** 2
    M[2][2] = p['eps11'] * k ** 2 - p['eps33'] * eta ** 2
    M[2][3] = p['qcar']
    M[2][4] = eta * p['p3']
    M[3][2] = p['bn'] * p['n0'] * L
    M[3][3] = -mp.mpc(0, 1) * w - p['Dn'] * L - mp.mpc(0, 1) * k * p['vd'] + 1 / p['tauR']
    M[3][4] = -p['beta_th'] * L
    M[4][0] = f * p['T0'] * w * k * p['b1']
    M[4][1] = -mp.mpc(0, 1) * w * f * p['T0'] * p['b3'] * eta
    M[4][2] = mp.mpc(0, 1) * w * f * p['T0'] * p['p3'] * eta
    M[4][3] = f * (-mp.mpc(0, 1) * w * p['qcar'] * p['Pi_th'] + p['Eg'] / p['tauR'])
    M[4][4] = -mp.mpc(0, 1) * w * f * p['rho'] * p['c_p'] - p['kth'] * L
    return M


def neha_M(eta, k, w, prm, lg=None, lnl=None, gam=None, R=None):
    p = prm
    lg = p['lg'] if lg is None else lg
    lnl = p['lnl'] if lnl is None else lnl
    gam = p['gam'] if gam is None else gam
    R1, R2, R3 = (p['R1'], p['R2'], p['R3']) if R is None else tuple(R)
    L = eta ** 2 - k ** 2
    N = 1 + lnl ** 2 * (k ** 2 - eta ** 2)
    G = 1 + lg ** 2 * (k ** 2 - eta ** 2)
    f = 1 - mp.mpc(0, 1) * w * p['tau_q']
    M = [[mp.mpc(0)] * 5 for _ in range(5)]
    M[0][0] = -N * p['rho'] * w ** 2 + G * (p['C11'] * k ** 2 - p['C44'] * eta ** 2)
    M[0][1] = -mp.mpc(0, 1) * k * eta * G * (p['C13'] + p['C44'])
    M[0][2] = -mp.mpc(0, 1) * k * eta * (R1 + R3)
    M[0][3] = -mp.mpc(0, 1) * k * eta * (p['e31'] + p['e15'])
    M[0][4] = mp.mpc(0, 1) * k * p['b1']
    M[1][0] = M[0][1]
    M[1][1] = -N * p['rho'] * w ** 2 + G * (p['C44'] * k ** 2 - p['C33'] * eta ** 2)
    M[1][2] = R3 * k ** 2 - R2 * eta ** 2
    M[1][3] = p['e15'] * k ** 2 - p['e33'] * eta ** 2
    M[1][4] = eta * p['b3']
    M[2][0] = mp.mpc(0, 1) * k * eta * (R1 + R3)
    M[2][1] = R2 * eta ** 2 - R3 * k ** 2
    M[2][2] = p['K1'] * eta ** 2 - p['K2'] * k ** 2 + p['rhop'] * w ** 2 + mp.mpc(0, 1) * gam * w
    M[2][4] = eta * p['bw']
    M[3][0] = mp.mpc(0, 1) * k * eta * (p['e15'] + p['e31'])
    M[3][1] = p['e33'] * eta ** 2 - p['e15'] * k ** 2
    M[3][3] = p['eps11'] * k ** 2 - p['eps33'] * eta ** 2
    M[3][4] = eta * p['p3']
    M[4][0] = f * p['T0'] * w * k * p['b1']
    M[4][1] = -mp.mpc(0, 1) * w * f * p['T0'] * p['b3'] * eta
    M[4][2] = -mp.mpc(0, 1) * w * f * p['T0'] * p['bw'] * eta
    M[4][3] = mp.mpc(0, 1) * w * f * p['T0'] * p['p3'] * eta
    M[4][4] = -mp.mpc(0, 1) * w * f * p['rho'] * p['c_p'] - p['kth'] * L
    return M


def anu_M(eta, k, w, prm, lg=None, lnl=None, al=None):
    p = prm
    lg = p['lg'] if lg is None else lg
    lnl = p['lnl'] if lnl is None else lnl
    a11, a33 = (p['a11'], p['a33']) if al is None else tuple(al)
    L = eta ** 2 - k ** 2
    N = 1 + lnl ** 2 * (k ** 2 - eta ** 2)
    G = 1 + lg ** 2 * (k ** 2 - eta ** 2)
    f = 1 - mp.mpc(0, 1) * w * p['tau_q']
    M = [[mp.mpc(0)] * 5 for _ in range(5)]
    M[0][0] = -N * p['rho'] * w ** 2 + G * (p['C11'] * k ** 2 - p['C44'] * eta ** 2)
    M[0][1] = -mp.mpc(0, 1) * k * eta * G * (p['C13'] + p['C44'])
    M[0][2] = -mp.mpc(0, 1) * k * eta * (p['e31'] + p['e15'])
    M[0][3] = -mp.mpc(0, 1) * k * eta * (p['h31'] + p['h15'])
    M[0][4] = mp.mpc(0, 1) * k * p['b1']
    M[1][0] = M[0][1]
    M[1][1] = -N * p['rho'] * w ** 2 + G * (p['C44'] * k ** 2 - p['C33'] * eta ** 2)
    M[1][2] = p['e15'] * k ** 2 - p['e33'] * eta ** 2
    M[1][3] = p['h15'] * k ** 2 - p['h33'] * eta ** 2
    M[1][4] = eta * p['b3']
    M[2][0] = mp.mpc(0, 1) * k * eta * (p['e15'] + p['e31'])
    M[2][1] = p['e33'] * eta ** 2 - p['e15'] * k ** 2
    M[2][2] = p['eps11'] * k ** 2 - p['eps33'] * eta ** 2
    M[2][3] = a33 * eta ** 2 - a11 * k ** 2
    M[2][4] = eta * p['p3']
    M[3][0] = mp.mpc(0, 1) * k * eta * (p['h15'] + p['h31'])
    M[3][1] = p['h33'] * eta ** 2 - p['h15'] * k ** 2
    M[3][2] = a33 * eta ** 2 - a11 * k ** 2
    M[3][3] = p['mu11'] * k ** 2 - p['mu33'] * eta ** 2
    M[3][4] = eta * p['m3']
    M[4][0] = f * p['T0'] * w * k * p['b1']
    M[4][1] = -mp.mpc(0, 1) * w * f * p['T0'] * p['b3'] * eta
    M[4][2] = mp.mpc(0, 1) * w * f * p['T0'] * p['p3'] * eta
    M[4][3] = mp.mpc(0, 1) * w * f * p['T0'] * p['m3'] * eta
    M[4][4] = -mp.mpc(0, 1) * w * f * p['rho'] * p['c_p'] - p['kth'] * L
    return M


def prm_from(model):
    return {k: mp.mpf(repr(v)) if not isinstance(v, str) else v
            for k, v in model.__dict__.items()}


def det_polynomial(Mfun, dps=120):
    """coefficients of det M(eta), ascending, by exact polynomial arithmetic
    in mp precision. Entries are at most quadratic in eta."""
    old = mp.mp.dps
    mp.mp.dps = dps
    try:
            # entries are at most quartic in eta (the gradient factor G multiplies
        # a quadratic), so sample at five nodes and solve the 5x5 Vandermonde
        nodes = [mp.mpf(v) for v in (-2, -1, 0, 1, 2)]
        Ms = {n: Mfun(n) for n in nodes}
        E = [[None] * 5 for _ in range(5)]
        V = mp.matrix(5, 5)
        for a in range(5):
            for b in range(5):
                V[a, b] = nodes[a] ** b
        Vinv = mp.inverse(V)
        for i in range(5):
            for j in range(5):
                rhs = mp.matrix([Ms[n][i][j] for n in nodes])
                E[i][j] = list(Vinv * rhs)
        total = [mp.mpc(0)]
        import itertools
        for perm in itertools.permutations(range(5)):
            s = 1
            pl = list(perm)
            for i in range(5):
                for j in range(i + 1, 5):
                    if pl[i] > pl[j]:
                        s = -s
            term = [mp.mpc(s)]
            for i in range(5):
                a, b = term, E[i][perm[i]]
                new = [mp.mpc(0)] * (len(a) + len(b) - 1)
                for p_, x in enumerate(a):
                    if x:
                        for q_, y in enumerate(b):
                            new[p_ + q_] += x * y
                term = new
            n = max(len(total), len(term))
            total = [(total[t] if t < len(total) else mp.mpc(0)) +
                     (term[t] if t < len(term) else mp.mpc(0)) for t in range(n)]
        while len(total) > 1 and abs(total[-1]) < abs(total[0]) * mp.mpf(10) ** (-dps + 20):
            total.pop()
        return total
    finally:
        mp.mp.dps = old
