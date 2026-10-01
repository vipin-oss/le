"""cg_ops.py — CONSERVATIVE narrow-stencil operators on the TFI mapped grid.
Fixes the parity null-mode of composed first-derivative stencils (D@D gives j±2 wide
stencils with odd-even decoupling). Contravariant flux form (verified identities):

  J div(K grad th) = d_xi(A th_xi + B th_eta) + d_eta(B th_xi + D th_eta)
  A = (K11 y_eta^2 - 2 K13 x_eta y_eta + K33 x_eta^2)/J
  D = (K11 y_xi^2 - 2 K13 x_xi y_xi + K33 x_xi^2)/J
  B = (K13(x_xi y_eta + x_eta y_xi) - K11 y_xi y_eta - K33 x_xi x_eta)/J

  J div(v) = d_xi(vx y_eta - vy x_eta) + d_eta(-vx y_xi + vy x_xi)   [Thompson identity]

Half-point coefficients: arithmetic averages of node values. Stencils use only i±1, j±1.
Thermal-stress load is NOT put in the flux (handled exactly as beta·grad th by first
derivatives, so uniform-theta gives exactly zero body force).
"""
import numpy as np
from scipy import sparse

class MappedOps:
    def __init__(self, grid):
        self.g = grid
        self.Nr, self.Nt = grid.Nr, grid.Nt
        self.n = grid.Nr * grid.Nt
        self.hxi, self.heta = grid.dxi, grid.deta
        # FD metrics: mixed partials commute exactly -> discrete identity
        # cxi(y_eta) == ceta(y_xi) holds at interior nodes => uniform-stress
        # fields have EXACTLY zero discrete divergence (patch test passes).
        def _cxi(arr):
            out = np.zeros_like(arr)
            out[1:-1] = (arr[2:] - arr[:-2]) / (2 * self.hxi)
            out[0] = (-3 * arr[0] + 4 * arr[1] - arr[2]) / (2 * self.hxi)
            out[-1] = (3 * arr[-1] - 4 * arr[-2] + arr[-3]) / (2 * self.hxi)
            return out

        def _ceta(arr):
            return (np.roll(arr, -1, axis=1) - np.roll(arr, 1, axis=1)) / (2 * self.heta)

        self.x_xi, self.x_eta = _cxi(grid.X), _ceta(grid.X)
        self.y_xi, self.y_eta = _cxi(grid.Y), _ceta(grid.Y)
        self.J = self.x_xi * self.y_eta - self.x_eta * self.y_xi

    def nid(self, i, j):
        return i * self.Nt + (j % self.Nt)

    # ---------- half-point metric averages ----------
    def _half_i(self, arr):
        return 0.5 * (arr[:-1, :] + arr[1:, :])

    def _half_j(self, arr):
        hh = 0.5 * (arr[:, :-1] + arr[:, 1:])
        return np.concatenate([hh, 0.5 * (arr[:, -1:] + arr[:, :1])], axis=1)

    # ---------- strain/gradient coefficient builders ----------
    def _grad_coeff(self, ye, yx, xe, xx, Javg):
        """coefficients of u_x,u_y at a half point given averaged metrics there.
        returns two dicts {(di,dj):coef} for u_x and u_y (offsets relative to the
        two bracketing nodes of the normal direction chosen by caller)."""
        raise NotImplementedError

    # ---------- thermal ----------
    def thermal(self, K2):
        g, Nr, Nt, n = self.g, self.Nr, self.Nt, self.n
        hxi, heta, Jn = self.hxi, self.heta, self.J
        K2 = np.asarray(K2, float)
        K11, K13, K33 = K2[0, 0], K2[0, 1], K2[1, 1]
        A = (K11 * self.y_eta**2 - 2 * K13 * self.x_eta * self.y_eta + K33 * self.x_eta**2) / self.J
        D = (K11 * self.y_xi**2 - 2 * K13 * self.x_xi * self.y_xi + K33 * self.x_xi**2) / self.J
        B = (K13 * (self.x_xi * self.y_eta + self.x_eta * self.y_xi)
             - K11 * self.y_xi * self.y_eta - K33 * self.x_xi * self.x_eta) / self.J
        A_i = self._half_i(A); B_i = self._half_i(B); D_i = self._half_i(D)
        A_j = self._half_j(A); B_j = self._half_j(B); D_j = self._half_j(D)
        rows, cols, vals = [], [], []
        def add(r, c, v):
            if v != 0.0:
                rows.append(r); cols.append(c); vals.append(v)
        for i in range(1, Nr - 1):
            for j in range(Nt):
                r = self.nid(i, j)
                Jv = Jn[i, j]
                # xi-fluxes at ip+1/2, ip=i and i-1
                for sgn, ip in ((+1, i), (-1, i - 1)):
                    c0 = sgn / (hxi * Jv)
                    a = A_i[ip, j]; b = B_i[ip, j]
                    # P = a*(th_{ip+1}-th_ip)/hxi + b*(Deta th at ip and ip+1)/2
                    add(r, self.nid(ip + 1, j), c0 * a / hxi)
                    add(r, self.nid(ip, j), -c0 * a / hxi)
                    w = c0 * b / (4.0 * heta)
                    add(r, self.nid(ip + 1, j + 1), w); add(r, self.nid(ip + 1, j - 1), -w)
                    add(r, self.nid(ip, j + 1), w); add(r, self.nid(ip, j - 1), -w)
                # eta-fluxes at jp+1/2, jp=j and j-1
                for sgn, jp in ((+1, j), (-1, j - 1)):
                    c0 = sgn / (heta * Jv)
                    b = B_j[i, jp % Nt]; d = D_j[i, jp % Nt]
                    # R = b*(Dxi th at jp and jp+1)/2 + d*(th_{jp+1}-th_{jp})/heta
                    add(r, self.nid(i, jp + 1), c0 * d / heta)
                    add(r, self.nid(i, jp), -c0 * d / heta)
                    w = c0 * b / (4.0 * hxi)
                    add(r, self.nid(i + 1, jp + 1), w); add(r, self.nid(i - 1, jp + 1), -w)
                    add(r, self.nid(i + 1, jp), w); add(r, self.nid(i - 1, jp), -w)
        return sparse.csr_matrix((vals, (rows, cols)), shape=(n, n))

    # ---------- momentum ----------
    def momentum(self, Q):
        """Conservative rows (div sigma_mech)_1 and (div sigma_mech)_2 for sigma=Q:eps(u).
        Returns M1, M2 (n x 3n) acting on U=[th|u1|u3] (theta columns are zero here)."""
        g, Nr, Nt, n = self.g, self.Nr, self.Nt, self.n
        hxi, heta, Jn = self.hxi, self.heta, self.J
        Q = np.asarray(Q, complex)
        yeta_i, xeta_i = self._half_i(self.y_eta), self._half_i(self.x_eta)
        yxi_i, xxi_i = self._half_i(self.y_xi), self._half_i(self.x_xi)
        yeta_j, xeta_j = self._half_j(self.y_eta), self._half_j(self.x_eta)
        yxi_j, xxi_j = self._half_j(self.y_xi), self._half_j(self.x_xi)
        Ji = self._half_i(self.J); Jj = self._half_j(self.J)
        rows1, cols1, vals1 = [], [], []
        rows2, cols2, vals2 = [], [], []

        def build(which, ye, xe, yx, xx, Javg, mode):
            """flux coefficients dict {(comp,di,dj):coef} for P1/P2 (mode='i') or R1/R2 (mode='j').
            mode 'i': normal dir is xi, nodes at (ip..ip+1, j..j±1); offsets di∈{0,1}, dj∈{-1,0,1}
            mode 'j': normal dir is eta, nodes at (i..i±1, jp..jp+1); offsets di∈{-1,0,1}, dj∈{-1,0}"""
            co = {}
            def add(comp, di, dj, val):
                if val != 0.0:
                    key = (comp, di, dj)
                    co[key] = co.get(key, 0.0) + val
            invJ = 1.0 / Javg
            if mode == 'i':
                # dxi u = (u[ip+1]-u[ip])/hxi ; deta u = (Deta|ip + Deta|ip+1)/2, Deta|k=(u[k,j+1]-u[k,j-1])/(2heta)
                def ux(comp, s):
                    add(comp, 1, 0, s * ye * invJ / hxi); add(comp, 0, 0, -s * ye * invJ / hxi)
                    w = -s * yx * invJ / (4 * heta)
                    add(comp, 1, 1, w); add(comp, 1, -1, -w); add(comp, 0, 1, w); add(comp, 0, -1, -w)
                def uy(comp, s):
                    add(comp, 1, 0, -s * xe * invJ / hxi); add(comp, 0, 0, s * xe * invJ / hxi)
                    w = s * xx * invJ / (4 * heta)
                    add(comp, 1, 1, w); add(comp, 1, -1, -w); add(comp, 0, 1, w); add(comp, 0, -1, -w)
            else:
                # deta u = (u[jp+1]-u[jp])/heta ; dxi u = (Dxi|jp + Dxi|jp+1)/2, Dxi|k=(u[i+1,k]-u[i-1,k])/(2hxi)
                # offsets: dj=0 -> jp+1 ; dj=-1 -> jp
                def ux(comp, s):
                    add(comp, 0, 0, -s * yx * invJ / heta); add(comp, 0, -1, s * yx * invJ / heta)
                    w = s * ye * invJ / (4 * hxi)
                    add(comp, 1, 0, w); add(comp, -1, 0, -w); add(comp, 1, -1, w); add(comp, -1, -1, -w)
                def uy(comp, s):
                    add(comp, 0, 0, s * xx * invJ / heta); add(comp, 0, -1, -s * xx * invJ / heta)
                    w = -s * xe * invJ / (4 * hxi)
                    add(comp, 1, 0, w); add(comp, -1, 0, -w); add(comp, 1, -1, w); add(comp, -1, -1, -w)
            # sigma11 = Q00 e11 + Q01 e33 + Q02 g13 ; sigma13 = Q20.. ; sigma33 = Q10? (row1 of Q is e11 row)
            if which == 1:
                if mode == 'i':   # P1 = ye s11 - xe s13
                    a1 = ye * Q[0, 0] - xe * Q[2, 0]; a3 = ye * Q[0, 1] - xe * Q[2, 1]; ag = ye * Q[0, 2] - xe * Q[2, 2]
                else:             # R1 = -yx s11 + xx s13
                    a1 = -yx * Q[0, 0] + xx * Q[2, 0]; a3 = -yx * Q[0, 1] + xx * Q[2, 1]; ag = -yx * Q[0, 2] + xx * Q[2, 2]
            else:
                if mode == 'i':   # P2 = ye s13 - xe s33
                    a1 = ye * Q[2, 0] - xe * Q[1, 0]; a3 = ye * Q[2, 1] - xe * Q[1, 1]; ag = ye * Q[2, 2] - xe * Q[1, 2]
                else:             # R2 = -yx s13 + xx s33
                    a1 = -yx * Q[2, 0] + xx * Q[1, 0]; a3 = -yx * Q[2, 1] + xx * Q[1, 1]; ag = -yx * Q[2, 2] + xx * Q[1, 2]
            ux(1, a1)      # e11 = u1,x
            uy(2, a3)      # e33 = u3,y
            ux(2, ag)      # g13 includes u3,x
            uy(1, ag)      # g13 includes u1,y
            return co

        for i in range(1, Nr - 1):
            for j in range(Nt):
                r = self.nid(i, j)
                # xi-fluxes
                for sgn, ip in ((+1, i), (-1, i - 1)):
                    c0 = sgn / (hxi * Jn[i, j])
                    ye, xe = yeta_i[ip, j], xeta_i[ip, j]
                    yx, xx = yxi_i[ip, j], xxi_i[ip, j]
                    for which, rows, cols, vals in ((1, rows1, cols1, vals1), (2, rows2, cols2, vals2)):
                        co = build(which, ye, xe, yx, xx, Ji[ip, j], 'i')
                        for (comp, di, dj), val in co.items():
                            node = self.nid(ip + di, j + dj)
                            rows.append(r); cols.append(comp * n + node); vals.append(c0 * val)
                # eta-fluxes
                for sgn, jp in ((+1, j), (-1, j - 1)):
                    c0 = sgn / (heta * Jn[i, j])
                    ye, xe = yeta_j[i, jp % Nt], xeta_j[i, jp % Nt]
                    yx, xx = yxi_j[i, jp % Nt], xxi_j[i, jp % Nt]
                    for which, rows, cols, vals in ((1, rows1, cols1, vals1), (2, rows2, cols2, vals2)):
                        co = build(which, ye, xe, yx, xx, Jj[i, jp % Nt], 'j')
                        for (comp, di, dj), val in co.items():
                            node = self.nid(i + di, jp + 1 + dj)
                            rows.append(r); cols.append(comp * n + node); vals.append(c0 * val)
        M1 = sparse.csr_matrix((vals1, (rows1, cols1)), shape=(n, 3 * n))
        M2 = sparse.csr_matrix((vals2, (rows2, cols2)), shape=(n, 3 * n))
        return M1, M2

    def beta_grad_rows(self, beta):
        """G1 = beta0 th_x + beta2 th_y ; G2 = beta2 th_x + beta1 th_y  (n x n each).
        Momentum rows: M u - G th + rho w^2 u = 0  (equals div(Q:eps u - beta th) + ...)."""
        g, n = self.g, self.n
        Dx, Dy = g.Dx, g.Dy
        G1 = (beta[0] * Dx + beta[2] * Dy).tocsr()
        G2 = (beta[2] * Dx + beta[1] * Dy).tocsr()
        return G1, G2

    def stress_first(self, Q, beta=None):
        """First-derivative stress operators (for BC traction rows and postprocessing):
        S11,S13,S33 (n x 3n) with sigma = Q:eps(u) [- beta theta if beta given]."""
        g, n = self.g, self.n
        Dx, Dy = g.Dx, g.Dy
        I = sparse.identity(n, format='csr', dtype=complex)
        Z = sparse.csr_matrix((n, n), dtype=complex)
        Q = np.asarray(Q, complex)
        b = np.zeros(3) if beta is None else np.asarray(beta, float)
        S11 = sparse.hstack([-b[0] * I, Q[0, 0] * Dx + Q[0, 2] * Dy, Q[0, 1] * Dy + Q[0, 2] * Dx]).tocsr()
        S13 = sparse.hstack([-b[2] * I, Q[2, 0] * Dx + Q[2, 2] * Dy, Q[2, 1] * Dy + Q[2, 2] * Dx]).tocsr()
        S33 = sparse.hstack([-b[1] * I, Q[1, 0] * Dx + Q[1, 2] * Dy, Q[1, 1] * Dy + Q[1, 2] * Dx]).tocsr()
        return S11, S13, S33
