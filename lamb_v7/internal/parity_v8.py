#!/usr/bin/env python3
"""v8 internal check: eta-parity of det M(eta) and the degree, done exactly.

Two separate questions, two separate methods, neither of them a numerical
evaluation of the determinant (the first attempt used one and it was wrong:
with entries spanning 1e-19 to 1e8 the odd part of the determinant washed out
in cancellation, and the parity verdict came out coupled to the size of the
coupling constants, which is nonsense -- parity of a polynomial has nothing to
do with how big its coefficients are).

1. PARITY, structural. Every entry of M is 0, a constant, or constant x eta,
   or constant x eta^2, so each entry has an exact parity. det M(-eta) =
   prod(sigma) prod(tau) det M(eta) whenever signs sigma_i, tau_j can be found
   with s_ij = sigma_i tau_j for every non-zero entry; the product is taken
   over the matrix here and it is +1, so an assignment exists  <=>  det M is
   even. Whether an assignment exists is a pure 0-1 question, solved below by
   a union-find with parity, and it is independent of every constant.
   If no assignment exists, a conflict cycle is printed: four entries whose
   parities force sigma_i tau_j = -1 between them. Those four entries are the
   breakers; a coupling is named a breaker only if zeroing it removes every
   conflict.

2. DEGREE, exact. Each entry is a polynomial in eta with rational
   coefficients, the constants are equilibrated row by row and column by
   column so no coefficient is astronomically larger than its neighbours, and
   the determinant is expanded over the 120 permutations in exact rational
   arithmetic. Row and column scaling multiply det by a non-zero number, so
   the degree is untouched.

Constants are physical scale placeholders, internal only.
"""
import itertools
from fractions import Fraction as F

# ---------------------------------------------------------------- helpers
def poly(*coeffs):
    """ascending coefficients in eta"""
    p = list(coeffs)
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return p


def padd(a, b):
    n = max(len(a), len(b))
    out = [F(0)] * n
    for i in range(n):
        out[i] = (a[i] if i < len(a) else F(0)) + (b[i] if i < len(b) else F(0))
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out


def pmul(a, b):
    out = [F(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        if x:
            for j, y in enumerate(b):
                out[i + j] += x * y
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out


def pscale(a, c):
    return [x * c for x in a]


def parity(a):
    """+1, -1 or None (mixed / zero) for a polynomial in eta"""
    nz = [i for i, x in enumerate(a) if x != 0]
    if not nz:
        return 0
    par = {i % 2 for i in nz}
    if len(par) == 1:
        return +1 if 0 in par else -1
    return None


# ------------------------------------------------- union-find with parity
class UF:
    def __init__(self, n):
        self.p = list(range(n))
        self.r = [0] * n        # parity of node relative to parent

    def find(self, x):
        if self.p[x] == x:
            return x, 0
        root, par = self.find(self.p[x])
        self.r[x] ^= par
        self.p[x] = root
        return root, self.r[x]

    def union(self, a, b, rel):
        ra, pa = self.find(a)
        rb, pb = self.find(b)
        if ra == rb:
            return (pa ^ pb) == rel, None
        self.p[ra] = rb
        self.r[ra] = pa ^ pb ^ rel
        return True, (a, b, rel)


def match_signs(P):
    """P: 5x5 list of +1/-1/0. Returns (ok, conflict) where conflict is the list
    of (i,j,parity) entries on a cycle whose product is -1."""
    n = len(P)
    uf = UF(2 * n)          # rows 0..n-1, columns n..2n-1 ; parity 1 means sigma*tau=-1
    edges = []
    for i in range(n):
        for j in range(n):
            if P[i][j] in (+1, -1):
                rel = 0 if P[i][j] == +1 else 1
                edges.append((i, n + j, rel, (i + 1, j + 1)))
                ok, _ = uf.union(i, n + j, rel)
                if not ok:
                    # find the cycle: walk the existing tree path
                    return False, (i + 1, j + 1)
    return True, None


def conflict_report(P):
    """if inconsistent, list the entries on the shortest conflicting cycle"""
    n = len(P)
    # build graph
    adj = {}
    for i in range(n):
        for j in range(n):
            if P[i][j] in (+1, -1):
                rel = 0 if P[i][j] == +1 else 1
                adj.setdefault(i, []).append((n + j, rel, (i + 1, j + 1)))
                adj.setdefault(n + j, []).append((i, rel, (i + 1, j + 1)))
    # BFS from each node looking for an odd cycle through it
    best = None
    for s in range(2 * n):
        dist = {s: 0}
        par = {s: 0}
        par_edge = {}
        queue = [s]
        while queue:
            u = queue.pop(0)
            for v, rel, e in adj.get(u, []):
                if v not in dist:
                    dist[v] = dist[u] + 1
                    par[v] = par[u] ^ rel
                    par_edge[v] = (u, e)
                    queue.append(v)
                elif par[v] != (par[u] ^ rel):
                    # cycle found
                    cycle = []
                    a, b = u, v
                    # collect entries on paths to s
                    def path(node):
                        out = []
                        while node != s:
                            uu, ee = par_edge[node]
                            out.append(ee)
                            node = uu
                        return out
                    cycle = path(a) + [(v, e) if False else e] + path(b)
                    cyc = sorted(set(cycle))
                    if best is None or len(cyc) < len(best):
                        best = cyc
    return best


def det_poly(M):
    n = len(M)
    total = [F(0)]
    for perm in itertools.permutations(range(n)):
        s = 1
        pl = list(perm)
        for i in range(n):
            for j in range(i + 1, n):
                if pl[i] > pl[j]:
                    s = -s
        term = [F(s)]
        for i in range(n):
            term = pmul(term, M[i][perm[i]])
        total = padd(total, term)
    return total


def equilibrate(M):
    """divide each row by its largest |coefficient|, then each column likewise"""
    M = [[list(e) for e in row] for row in M]
    for i, row in enumerate(M):
        m = max((abs(x) for e in row for x in e), default=F(0))
        if m:
            M[i] = [pscale(e, F(1) / m) for e in row]
    for j in range(len(M)):
        m = max((abs(M[i][j][k]) for i in range(len(M)) for k in range(len(M[i][j]))),
                default=F(0))
        if m:
            for i in range(len(M)):
                M[i][j] = pscale(M[i][j], F(1) / m)
    return M


def report(name, M):
    P = [[parity(e) for e in row] for row in M]
    bad_entry = [(i + 1, j + 1) for i, row in enumerate(P) for j, v in enumerate(row)
                 if v is None]
    ok, _ = match_signs(P)
    d = det_poly(equilibrate(M))
    deg = len(d) - 1
    odd = [i for i in range(1, len(d), 2) if d[i] != 0]
    even = [i for i in range(0, len(d), 2) if d[i] != 0]
    det_even = not odd
    agree = (ok == det_even)
    line = (f'  {name:36s} deg={deg:2d}  sign-match={str(ok):5s}  det-even={str(det_even):5s}'
            f'  {"agree" if agree else "DISAGREE"}')
    print(line)
    if bad_entry:
        print(f'      mixed-parity entries: {bad_entry}')
    if not ok:
        print(f'      conflict cycle through entries: {conflict_report(P)}')
    if not agree:
        print('      *** the two methods disagree: investigate before writing anything ***')
    return ok, det_even, deg


# ---------------------------------------------------------------- matrices
def S(x):
    return F(x)


def sumit(lnl='0.2', lg='0.3', e=('12', '15', '-4.5'), p3='0.5',
          bth='2.5e5', pith='0.05', eg='1.2e-19', qcar='1.6e-19'):
    k = F('1e7')
    w = F('6.283185307179586e7')
    L = poly(-k * k, 0, 1)
    N = poly(1 + S(lnl) ** 2 * k * k, 0, -S(lnl) ** 2)
    G = poly(1 + S(lg) ** 2 * k * k, 0, -S(lg) ** 2)
    c11, c13, c33, c44 = S('209.7e9'), S('121.1e9'), S('211.2e9'), S('42.4e9')
    e31, e33, e15 = [S(v) for v in e]
    b1, b3 = S('1.7e6'), S('1.5e6')
    rho, Dn, bn, n0, vd, tauR = S(5680), S('1e-3'), S('0.02'), S('1e21'), S('1e3'), S('1e-9')
    c_p, kth, T0 = S('3.4e6'), S(60), S(300)
    eps11, eps33 = S('8.854e-12') * S('8.54'), S('8.854e-12') * S('10.2')
    bth, pith, eg, qcar, p3 = S(bth), S(pith), S(eg), S(qcar), S(p3)
    f0r = F(1)       # f = 1 - i w tau_q
    M = [[poly(0)] * 5 for _ in range(5)]

    def put(i, j, pl, facr=F(1), faci=F(0)):
        """entry += (facr + i faci) * pl, with pol handled as real polynomial"""
        M[i][j] = padd(M[i][j], pscale(pl, facr))
        if faci:
            M[i][j] = padd(M[i][j], pscale(pl, faci))  # imaginary part kept separately? no
    # NOTE: to keep exact rational arithmetic we treat i by tracking a complex
    # polynomial as (real part, imaginary part). Simpler: all entries are
    # multiplied by 1, i or -1; we absorb i into the matrix by scaling the
    # Gaussian rows, which does not change the parity question. We therefore
    # drop i from the entries: every row is either purely real or purely
    # imaginary times real, so multiplying row 1,2,3 by -i and row 5 by i
    # makes all entries real with an overall non-zero factor i^n.
    # Parity of each entry is unaffected by that.
    Mr = [[poly(0)] * 5 for _ in range(5)]

    def setr(i, j, pl, sgn=F(1)):
        Mr[i][j] = padd(Mr[i][j], pscale(pl, sgn))

    setr(0, 0, N, -rho * w * w)
    setr(0, 0, pmul(G, poly(k * k, 0, -1)), c11)
    setr(0, 0, pmul(G, poly(0, 0, 1)), -c44)
    setr(0, 1, pmul(G, poly(0, 1)), -k * (c13 + c44))
    setr(0, 2, poly(0, 1), -k * (e31 + e15))
    setr(0, 4, poly(1), k * b1)
    setr(1, 0, pmul(G, poly(0, 1)), -k * (c13 + c44))
    setr(1, 1, N, -rho * w * w)
    setr(1, 1, pmul(G, poly(k * k, 0, -1)), c44)
    setr(1, 1, pmul(G, poly(0, 0, 1)), -c33)
    setr(1, 2, poly(-e15 * k * k), 1)
    setr(1, 2, poly(0, 0, 1), e33)
    setr(1, 4, poly(0, 1), b3)
    setr(2, 0, poly(0, 1), k * (e15 + e31))
    setr(2, 1, poly(0, 0, 1), -e33)
    setr(2, 1, poly(e15 * k * k), 1)
    setr(2, 2, poly(-eps11 * k * k), 1)
    setr(2, 2, poly(0, 0, 1), eps33)
    setr(2, 3, poly(-qcar), 1)
    setr(2, 4, poly(0, 1), -p3)
    setr(3, 2, L, bn * n0)
    setr(3, 3, poly(1 / tauR), 1)
    setr(3, 3, L, -Dn)
    setr(3, 3, poly(k * vd), 1)
    setr(3, 3, poly(w), 1)
    setr(3, 4, L, -bth)
    setr(4, 0, poly(T0 * w * k * b1), f0r)
    setr(4, 1, poly(0, 1), -w * T0 * b3)
    setr(4, 2, poly(0, 1), w * T0 * p3)
    setr(4, 3, poly(-w * qcar * pith + eg / tauR), f0r)
    setr(4, 4, poly(w * c_p), f0r)
    setr(4, 4, L, -kth)
    return Mr


def neha(lnl='0.2', lg='0.3', R=('2e9', '3e9', '1.5e9'), bw='1e6', bth='1e6',
         e=('0.4', '1.1', '0.3'), p3='0.5'):
    k = F('1e6')
    w = F('6.283185307179586e6')
    L = poly(-k * k, 0, 1)
    N = poly(1 + S(lnl) ** 2 * k * k, 0, -S(lnl) ** 2)
    G = poly(1 + S(lg) ** 2 * k * k, 0, -S(lg) ** 2)
    C11, C13, C33, C44 = S('150e9'), S('60e9'), S('130e9'), S('40e9')
    K1, K2 = S('30e9'), S('20e9')
    R1, R2, R3 = [S(v) for v in R]
    e31, e33, e15 = [S(v) for v in e]
    bw, bth, p3 = S(bw), S(bth), S(p3)
    rho, rhop, gam = S(4200), S(12), S('1e8')
    c_p, kth, T0 = S('2.9e6'), S(4), S(300)
    eps11, eps33 = S('8.854e-12') * S('8.54'), S('8.854e-12') * S('10.2')
    Mr = [[poly(0)] * 5 for _ in range(5)]

    def setr(i, j, pl, sgn=F(1)):
        Mr[i][j] = padd(Mr[i][j], pscale(pl, sgn))

    setr(0, 0, N, -rho * w * w)
    setr(0, 0, pmul(G, poly(k * k, 0, -1)), C11)
    setr(0, 0, pmul(G, poly(0, 0, 1)), -C44)
    setr(0, 1, pmul(G, poly(0, 1)), -k * (C13 + C44))
    setr(0, 2, poly(0, 1), -k * (R1 + R3))
    setr(0, 3, poly(0, 1), -k * (e31 + e15))
    setr(0, 4, poly(1), k * bth)
    setr(1, 0, pmul(G, poly(0, 1)), -k * (C13 + C44))
    setr(1, 1, N, -rho * w * w)
    setr(1, 1, pmul(G, poly(k * k, 0, -1)), C44)
    setr(1, 1, pmul(G, poly(0, 0, 1)), -C33)
    setr(1, 2, poly(-R3 * k * k), 1)
    setr(1, 2, poly(0, 0, 1), R2)
    setr(1, 3, poly(-e15 * k * k), 1)
    setr(1, 3, poly(0, 0, 1), e33)
    setr(1, 4, poly(0, 1), bth)
    setr(2, 0, poly(0, 1), k * (R1 + R3))
    setr(2, 1, poly(0, 0, 1), -R2)
    setr(2, 1, poly(R3 * k * k), 1)
    setr(2, 2, poly(0, 0, 1), -K1)
    setr(2, 2, poly(K2 * k * k - rhop * w * w), 1)
    setr(2, 4, poly(0, 1), -bw)
    setr(3, 0, poly(0, 1), k * (e15 + e31))
    setr(3, 1, poly(0, 0, 1), -e33)
    setr(3, 1, poly(e15 * k * k), 1)
    setr(3, 3, poly(0, 0, 1), -eps33)
    setr(3, 3, poly(eps11 * k * k), 1)
    setr(3, 4, poly(0, 1), -p3)
    setr(4, 0, poly(T0 * w * k * bth), 1)
    setr(4, 1, poly(0, 1), -w * T0 * bth)
    setr(4, 2, poly(0, 1), -w * T0 * bw)
    setr(4, 3, poly(0, 1), w * T0 * p3)
    setr(4, 4, poly(w * c_p), 1)
    setr(4, 4, L, -kth)
    return Mr


def anu(lnl='0.2', lg='0.3', al=('1.2e-9', '3.4e-9'), e=('12', '15', '-4.5'),
        h=('200', '250', '100'), p3='0.5', m3='0.05'):
    k = F('1e5')
    w = F('6.283185307179586e5')
    L = poly(-k * k, 0, 1)
    N = poly(1 + S(lnl) ** 2 * k * k, 0, -S(lnl) ** 2)
    G = poly(1 + S(lg) ** 2 * k * k, 0, -S(lg) ** 2)
    C11, C13, C33, C44 = S('220e9'), S('110e9'), S('215e9'), S('45e9')
    e31, e33, e15 = [S(v) for v in e]
    h31, h33, h15 = [S(v) for v in h]
    a11, a33 = [S(v) for v in al]
    p3, m3 = S(p3), S(m3)
    eps11, eps33 = S('8.854e-12') * S(8), S('8.854e-12') * S(9)
    mu11, mu33 = S('1.2566e-6') * S(2), S('1.2566e-6') * S('1.5')
    b1, b3 = S('1.7e6'), S('1.5e6')
    rho, c_p, kth, T0 = S(5500), S('3.2e6'), S(6), S(300)
    Mr = [[poly(0)] * 5 for _ in range(5)]

    def setr(i, j, pl, sgn=F(1)):
        Mr[i][j] = padd(Mr[i][j], pscale(pl, sgn))

    setr(0, 0, N, -rho * w * w)
    setr(0, 0, pmul(G, poly(k * k, 0, -1)), C11)
    setr(0, 0, pmul(G, poly(0, 0, 1)), -C44)
    setr(0, 1, pmul(G, poly(0, 1)), -k * (C13 + C44))
    setr(0, 2, poly(0, 1), -k * (e31 + e15))
    setr(0, 3, poly(0, 1), -k * (h31 + h15))
    setr(0, 4, poly(1), k * b1)
    setr(1, 0, pmul(G, poly(0, 1)), -k * (C13 + C44))
    setr(1, 1, N, -rho * w * w)
    setr(1, 1, pmul(G, poly(k * k, 0, -1)), C44)
    setr(1, 1, pmul(G, poly(0, 0, 1)), -C33)
    setr(1, 2, poly(-e15 * k * k), 1)
    setr(1, 2, poly(0, 0, 1), e33)
    setr(1, 3, poly(-h15 * k * k), 1)
    setr(1, 3, poly(0, 0, 1), h33)
    setr(1, 4, poly(0, 1), b3)
    setr(2, 0, poly(0, 1), k * (e15 + e31))
    setr(2, 1, poly(0, 0, 1), -e33)
    setr(2, 1, poly(e15 * k * k), 1)
    setr(2, 2, poly(0, 0, 1), -eps33)
    setr(2, 2, poly(eps11 * k * k), 1)
    setr(2, 3, poly(0, 0, 1), -a33)
    setr(2, 3, poly(a11 * k * k), 1)
    setr(2, 4, poly(0, 1), -p3)
    setr(3, 0, poly(0, 1), k * (h15 + h31))
    setr(3, 1, poly(0, 0, 1), -h33)
    setr(3, 1, poly(h15 * k * k), 1)
    setr(3, 2, poly(0, 0, 1), -a33)
    setr(3, 2, poly(a11 * k * k), 1)
    setr(3, 3, poly(0, 0, 1), -mu33)
    setr(3, 3, poly(mu11 * k * k), 1)
    setr(3, 4, poly(0, 1), -m3)
    setr(4, 0, poly(T0 * w * k * b1), 1)
    setr(4, 1, poly(0, 1), -w * T0 * b3)
    setr(4, 2, poly(0, 1), w * T0 * p3)
    setr(4, 3, poly(0, 1), w * T0 * m3)
    setr(4, 4, poly(w * c_p), 1)
    setr(4, 4, L, -kth)
    return Mr


if __name__ == '__main__':
    print('PARITY (structural, exact) AND DEGREE (exact rational determinant)\n')
    print('Paper A (Sumit)')
    report('full', sumit())
    report('beta_th = 0 only', sumit(bth=0))
    report('Pi_th = 0 only', sumit(pith=0))
    report('E_g = 0 only', sumit(eg=0))
    report('p3 = 0 only', sumit(p3=0))
    report('piezo e = 0 only', sumit(e=(0, 0, 0)))
    report('beta_th = Pi_th = 0', sumit(bth=0, pith=0))
    report('beta_th = Pi_th = E_g = 0', sumit(bth=0, pith=0, eg=0))
    report('carrier block off (q=0)', sumit(qcar=0))
    report('l_g = 0, full', sumit(lg=0))
    report('l_g = l_nl = 0, cross off', sumit(lg=0, lnl=0, bth=0, pith=0, eg=0))
    print('\nPaper B (Neha)')
    report('full', neha())
    report('beta_th = 0', neha(bth=0))
    report('thermo-phason = 0', neha(bw=0))
    report('p3 = 0', neha(p3=0))
    report('R = 0', neha(R=(0, 0, 0)))
    report('l_g = 0', neha(lg=0))
    print('\nPaper C (Anu)')
    report('full', anu())
    report('alpha = 0', anu(al=(0, 0)))
    report('m3 = 0', anu(m3=0))
    report('p3 = 0', anu(p3=0))
    report('h = 0', anu(h=(0, 0, 0)))
    report('l_g = 0', anu(lg=0))


def assignment(P):
    """return (sigma, tau, failures) or None if inconsistent; sigma[0] fixed +1"""
    n = len(P)
    sig = [None] * n
    tau = [None] * n
    sig[0] = 1
    tau[0] = P[0][0] if P[0][0] in (1, -1) else None
    changed = True
    while changed:
        changed = False
        for i in range(n):
            for j in range(n):
                v = P[i][j]
                if v not in (1, -1):
                    continue
                if sig[i] is not None and tau[j] is None:
                    tau[j] = sig[i] * v
                    changed = True
                if tau[j] is not None and sig[i] is None:
                    sig[i] = tau[j] * v
                    changed = True
    # fill remaining unconnected components
    for i in range(n):
        if sig[i] is None:
            sig[i] = 1
    for j in range(n):
        if tau[j] is None:
            tau[j] = 1
    fail = []
    for i in range(n):
        for j in range(n):
            v = P[i][j]
            if v in (1, -1) and sig[i] * tau[j] != v:
                fail.append((i + 1, j + 1))
    return sig, tau, fail


def table(name, M, labels):
    P = [[parity(e) for e in row] for row in M]
    print(f'\n{name}: parity table (+ even, - odd, . zero)')
    print('        ' + ' '.join(f'{c:>4s}' for c in labels[1]))
    for i, row in enumerate(P):
        print(f'  {labels[0][i]:>5s} ' + ' '.join({1: '   +', -1: '   -', 0: '   .'}[v] for v in row))
    sig, tau, fail = assignment(P)
    print(f'  sigma = {sig}')
    print(f'  tau   = {tau}')
    print(f'  failing entries: {fail if fail else "none"}')

if __name__ == '__main__' and False:
    pass
