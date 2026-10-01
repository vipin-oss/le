"""cg_solver.py — frequency-domain coupled anisotropic generalized thermoelasticity
on the body-fitted grid (PROJECT_CRYSTAL_GEOMETRY_01).
Harmonic convention: fields ~ exp(+i w t).  Equations (MATHEMATICAL_FORMULATION.md):
  (C:eps(u) - beta theta)_,j + rho w^2 u_i = 0
  div(K g(w) grad theta) = i w (rho cp theta + T0 beta:eps(u))
  g(w) = 1 (Fourier) | 1/(1+i w tau) (CV) | 0.5/(1+i w ta)+0.5/(1+i w tb) (MCV3-type)
BCs: cavity wall: theta = 1 (unit transfer) [or outer_theta_value at outer], traction free;
outer: theta = outer_theta_value, u = 0.
Caching: A(w) = Abase + w^2 Ain + i w Ad + g(w) Alap.
Rows of A: [mom1 | mom2 | energy]; boundary rows live in Abase only.
"""
import numpy as np
from scipy import sparse
from scipy.sparse.linalg import splu

class HarmonicSolver:
    def __init__(self, grid, K2, Q, beta, rho, cp, T0, model='CV', tau=0.0, outer_theta_value=0.0, energy_coupling=True):
        from cg_ops import MappedOps
        self.g = grid
        self.K2 = np.asarray(K2, float); self.Q = np.asarray(Q, complex)
        self.beta = np.asarray(beta, float)
        self.rho, self.cp, self.T0 = rho, cp, T0
        self.model, self.tau = model, tau
        self.energy_coupling = energy_coupling
        self.outer_theta_value = outer_theta_value
        self.n = grid.Nr * grid.Nt
        self.Dx, self.Dy = grid.Dx, grid.Dy
        n = self.n
        I = sparse.identity(n, format='csr', dtype=complex)
        self.I = I
        self.i_cav = np.arange(grid.Nt)
        self.i_out = (grid.Nr - 1) * grid.Nt + np.arange(grid.Nt)
        ops = MappedOps(grid)
        self.ops = ops
        # stress operators (first-derivative; for traction BCs and postprocessing)
        self._S11, self._S13, self._S33 = ops.stress_first(Q, self.beta)
        # conservative thermal + momentum operators
        Lap = ops.thermal(self.K2)                       # div(K grad)
        M1c, M2c = ops.momentum(Q)                       # div(Q:eps u)
        G1, G2 = ops.beta_grad_rows(self.beta)           # beta·grad theta rows
        Z = sparse.csr_matrix((n, n), dtype=complex)
        Z3 = sparse.csr_matrix((n, 3 * n), dtype=complex)
        # Abase: momentum rows = [ -G | M1c_u ] (theta cols from -G), energy base 0
        Mom1 = sparse.hstack([-G1.astype(complex), M1c[:, n:2 * n], M1c[:, 2 * n:3 * n]]).tocsr()
        Mom2 = sparse.hstack([-G2.astype(complex), M2c[:, n:2 * n], M2c[:, 2 * n:3 * n]]).tocsr()
        coup1 = (T0 * (self.beta[0] * self.Dx + self.beta[2] * self.Dy)).tocsr()
        coup2 = (T0 * (self.beta[2] * self.Dx + self.beta[1] * self.Dy)).tocsr()
        Ain = sparse.vstack([
            sparse.hstack([Z, self.rho * I, Z]),
            sparse.hstack([Z, Z, self.rho * I]),
            Z3]).tocsr()
        ec1, ec2 = (coup1, coup2) if energy_coupling else (None, None)
        Zn = sparse.csr_matrix((n, n), dtype=complex)
        Ad = sparse.vstack([
            Z3, Z3,
            sparse.hstack([-self.rho * self.cp * I, -coup1 if energy_coupling else Zn, -coup2 if energy_coupling else Zn])]).tocsr()
        Alap = sparse.vstack([Z3, Z3, sparse.hstack([Lap.astype(complex), Z, Z])]).tocsr()
        Abase = sparse.vstack([Mom1, Mom2, Z3]).tocsr()
        # ---- boundary row replacement ----
        nxf, nyf = np.zeros(n), np.zeros(n)
        nx, ny = self.g.normals_cavity()
        nxf[self.i_cav] = nx; nyf[self.i_cav] = ny
        T1 = (sparse.diags(nxf) @ self._S11 + sparse.diags(nyf) @ self._S13).tolil()
        T2 = (sparse.diags(nxf) @ self._S13 + sparse.diags(nyf) @ self._S33).tolil()
        Ab = Abase.tolil(); Ai = Ain.tolil(); Adl = Ad.tolil(); Al = Alap.tolil()
        def srow(dst, r, cols, vals):
            dst.rows[r] = list(cols); dst.data[r] = list(vals)
        for node in self.i_cav:
            srow(Ab, node, [node], [1.0 + 0j])
            srow(Ab, n + node, T1.rows[node], T1.data[node])
            srow(Ab, 2 * n + node, T2.rows[node], T2.data[node])
            for P in (Ai, Adl, Al):
                srow(P, node, [], []); srow(P, n + node, [], []); srow(P, 2 * n + node, [], [])
        for node in self.i_out:
            srow(Ab, node, [node], [1.0 + 0j])
            srow(Ab, n + node, [n + node], [1.0 + 0j])
            srow(Ab, 2 * n + node, [2 * n + node], [1.0 + 0j])
            for P in (Ai, Adl, Al):
                srow(P, node, [], []); srow(P, n + node, [], []); srow(P, 2 * n + node, [], [])
        self.Abase = Ab.tocsr(); self.Ain = Ai.tocsr(); self.Ad = Adl.tocsr(); self.Alap = Al.tocsr()
        # row scaling: multiply interior rows by J_node so that with SI scales
        # (J~1e-16) the PDE rows stay O(1e5) instead of O(1e20) (round-off fix);
        # boundary rows keep scale 1 (they are unit/traction rows).
        Dj = np.ones(3 * n)
        for i in range(1, grid.Nr - 1):
            for j in range(grid.Nt):
                node = self.nid(i, j) if hasattr(self, 'nid') else i * grid.Nt + j
                Dj[node] = self.ops.J[i, j]; Dj[n + node] = self.ops.J[i, j]; Dj[2 * n + node] = self.ops.J[i, j]
        self.Dj = Dj
        self.rhs = np.zeros(3 * n, dtype=complex)
        self.rhs[self.i_cav] = 1.0
        self.rhs[self.i_out] = self.outer_theta_value

    def gfac(self, w):
        if self.model == 'FOURIER':
            return 1.0 + 0j
        if self.model == 'CV':
            return 1.0 / (1.0 + 1j * w * self.tau)
        if self.model == 'MCV3':
            ta, tb = 0.5 * self.tau, 2.0 * self.tau
            return 0.5 / (1.0 + 1j * w * ta) + 0.5 / (1.0 + 1j * w * tb)
        raise ValueError(self.model)

    def stress_wall(self, U, w=None):
        S11, S13, S33 = self._S11, self._S13, self._S33
        s11 = (S11 @ U)[self.i_cav]; s13 = (S13 @ U)[self.i_cav]; s33 = (S33 @ U)[self.i_cav]
        tx, ty = self.g.hoop_dir(); nx, ny = self.g.normals_cavity()
        hoop = tx * tx * s11 + 2 * tx * ty * s13 + ty * ty * s33
        t1 = nx * s11 + ny * s13; t2 = nx * s13 + ny * s33
        return hoop, t1, t2

    def solve(self, w):
        A = (sparse.diags(self.Dj) @ (self.Abase + (w**2) * self.Ain + (1j * w) * self.Ad + self.gfac(w) * self.Alap)).tocsr()
        # row equilibration: scale each row to unit max |entry| (round-off control;
        # rhs is nonzero only on boundary rows whose scale is already 1).
        rm = np.asarray(abs(A).max(axis=1).todense()).ravel()
        rm[rm == 0.0] = 1.0
        A = (sparse.diags(1.0 / rm) @ A).tocsc()
        lu = splu(A)
        U = lu.solve(self.rhs)
        r = A @ U - self.rhs
        absA = abs(A)
        rowsum = np.asarray(absA.sum(axis=1)).ravel()
        back = np.abs(r).max() / max((rowsum * np.abs(U).max()).max(), 1e-300)
        return U, float(back)

    def wall_theta(self, U):
        return U[self.i_cav]

    def fields(self, U):
        n = self.n
        return U[:n].reshape(self.g.X.shape), U[n:2*n].reshape(self.g.X.shape), U[2*n:].reshape(self.g.X.shape)

if __name__ == '__main__':
    from cg_grid import Grid
    from cg_model import plane_strain_block, K_ac, rho, cp_ESTIMATED, T0
    import time
    Q, beta = plane_strain_block()
    for Nr2, Nt2 in ((48, 24), (96, 48), (192, 96)):
        grid2 = Grid(chi=1.0, Nr=Nr2, Nt=Nt2)
        s2 = HarmonicSolver(grid2, K_ac, Q, beta, rho, cp_ESTIMATED, T0, model='CV', tau=1e-11)
        t0 = time.time(); U, back = s2.solve(2 * np.pi / 0.6e-9); dt = time.time() - t0
        hoop, t1, t2 = s2.stress_wall(U)
        print(f'{Nr2}x{Nt2}: {dt:.2f}s backward_err {back:.2e} traction {np.abs(t1).max():.1e},{np.abs(t2).max():.1e} hoop0 {hoop[0].real:.4e}')
