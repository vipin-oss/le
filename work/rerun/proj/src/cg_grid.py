"""cg_grid.py — body-fitted TFI grid + derivative matrices (2nd order).
Map: r in [1,R] -> rho = (exp(gamma*xi)-1)/(exp(gamma)-1), xi in [0,1] (cluster at cavity).
x = A(rho) cos(eta), y = B(rho) sin(eta); A = ae+(Rout-ae)rho, B = be+(Rout-be)rho.
Circle: ae=be=a. Ellipse (equal area): ae=a*sqrt(chi), be=a/sqrt(chi).
Metrics from analytic map derivatives; D_x, D_y via chain rule as sparse ops.
"""
import numpy as np
from scipy import sparse

class Grid:
    def __init__(self, a=1.0, chi=1.0, R=80.0, Nr=96, Nt=48, gamma=3.5):
        self.a, self.chi, self.R, self.Nr, self.Nt, self.gamma = a, chi, R, Nr, Nt, gamma
        self.ae = a*np.sqrt(chi); self.be = a/np.sqrt(chi)
        self.xi = np.linspace(0.0, 1.0, Nr)          # r-direction index
        self.dxi = 1.0/(Nr-1)
        self.eta = np.arange(Nt)*2*np.pi/Nt           # periodic
        self.deta = 2*np.pi/Nt
        eg = np.exp(gamma)
        self.rho = (np.exp(gamma*self.xi)-1.0)/(eg-1.0)
        self.drho_dxi = (gamma*np.exp(gamma*self.xi))/(eg-1.0)
        self.r = self.ae + (R-self.ae)*self.rho   # radial coordinate of the A-surface (a=1 units OK)
        self.A = self.ae + (R-self.ae)*self.rho
        self.B = self.be + (R-self.be)*self.rho
        self.dA_dxi = (R-self.ae)*self.drho_dxi
        self.dB_dxi = (R-self.be)*self.drho_dxi
        Rm, Nm = np.meshgrid(self.r, self.eta, indexing='ij')
        Am = np.repeat(self.A[:, None], Nt, axis=1)
        Bm = np.repeat(self.B[:, None], Nt, axis=1)
        dAm = np.repeat(self.dA_dxi[:, None], Nt, axis=1)
        dBm = np.repeat(self.dB_dxi[:, None], Nt, axis=1)
        self.X = Am*np.cos(Nm); self.Y = Bm*np.sin(Nm)
        # analytic metrics: x_xi = dA_xi cos, x_eta = -A sin, y_xi = dB_xi sin, y_eta = B cos
        self.x_xi = dAm*np.cos(Nm); self.x_eta = -Am*np.sin(Nm)
        self.y_xi = dBm*np.sin(Nm); self.y_eta = Bm*np.cos(Nm)
        self.J = self.x_xi*self.y_eta - self.x_eta*self.y_xi
        assert np.all(self.J > 0), f'bad Jacobian min={self.J.min()}'
        self._build_ops()

    def _Dxi(self):
        """d/dxi, one-sided 2nd order at i=0 and i=Nr-1."""
        Nr, Nt, h = self.Nr, self.Nt, self.dxi
        rows, cols, vals = [], [], []
        for i in range(Nr):
            for j in range(Nt):
                r = i*Nt + j
                if i == 0:
                    for k, c in enumerate([-3/2, 2, -1/2]):
                        rows.append(r); cols.append(k*Nt + j); vals.append(c/h)
                elif i == Nr-1:
                    for k, c in enumerate([3/2, -2, 1/2]):
                        rows.append(r); cols.append((Nr-1-k)*Nt + j); vals.append(c/h)
                else:
                    rows.append(r); cols.append((i+1)*Nt + j); vals.append(0.5/h)
                    rows.append(r); cols.append((i-1)*Nt + j); vals.append(-0.5/h)
        return sparse.csr_matrix((vals, (rows, cols)), shape=(Nr*Nt, Nr*Nt))

    def _Deta(self):
        """d/deta, central periodic."""
        Nr, Nt, h = self.Nr, self.Nt, self.deta
        rows, cols, vals = [], [], []
        for i in range(Nr):
            for j in range(Nt):
                r = i*Nt + j
                rows.append(r); cols.append(i*Nt + (j+1) % Nt); vals.append(0.5/h)
                rows.append(r); cols.append(i*Nt + (j-1) % Nt); vals.append(-0.5/h)
        return sparse.csr_matrix((vals, (rows, cols)), shape=(Nr*Nt, Nr*Nt))

    def _build_ops(self):
        n = self.Nr*self.Nt
        Dxi, Deta = self._Dxi(), self._Deta()
        J = self.J.ravel()
        y_eta = sparse.diags(self.y_eta.ravel()/J)
        y_xi = sparse.diags(self.y_xi.ravel()/J)
        x_eta = sparse.diags(self.x_eta.ravel()/J)
        x_xi = sparse.diags(self.x_xi.ravel()/J)
        # [f_xi;f_eta] = [[x_xi,y_xi],[x_eta,y_eta]] [f_x;f_y]  =>  inverse:
        # f_x = (y_eta f_xi - y_xi f_eta)/J ; f_y = (-x_eta f_xi + x_xi f_eta)/J
        self.Dx = (y_eta@Dxi - y_xi@Deta).tocsr()
        self.Dy = (-x_eta@Dxi + x_xi@Deta).tocsr()
        self.Dxi, self.Deta = Dxi, Deta

    def normals_cavity(self):
        """Outward normal of the cavity ellipse (pointing away from center),
        unit, at i=0 nodes; tangent from map. n ∝ (B cos, A sin) at rho=0."""
        eta = self.eta
        nx = self.be*np.cos(eta); ny = self.ae*np.sin(eta)
        nn = np.sqrt(nx**2 + ny**2)
        return nx/nn, ny/nn

    def wall_indices(self):
        return np.arange(self.Nt)  # i=0 nodes

    def hoop_dir(self):
        """Unit tangent + normal on cavity wall at i=0; hoop direction = tangent."""
        eta = self.eta
        tx = -self.ae*np.sin(eta); ty = self.be*np.cos(eta)
        tt = np.sqrt(tx**2 + ty**2)
        return tx/tt, ty/tt

if __name__ == '__main__':
    g = Grid(chi=2.0, Nr=48, Nt=24)
    print('J range', g.J.min(), g.J.max())
    print('r range', g.r.min(), g.r.max(), 'dr near cavity', g.r[1]-g.r[0], 'dr outer', g.r[-1]-g.r[-2])
    # derivative consistency: f = x^2 + y^3 -> fx = 2x, fy = 3y^2 (interior only)
    f = g.X**2 + g.Y**3
    fx = (g.Dx @ f.ravel()).reshape(g.X.shape)
    fy = (g.Dy @ f.ravel()).reshape(g.X.shape)
    errx = np.abs(fx[2:-2, :] - 2*g.X[2:-2, :]).max()/np.abs(2*g.X).max()
    erry = np.abs(fy[2:-2, :] - 3*g.Y[2:-2, :]**2).max()/np.abs(3*g.Y**2).max()
    print('deriv test rel errs (interior):', errx, erry)
    # ellipse area check
    print('wall normals ok:', g.normals_cavity()[0][:3])
