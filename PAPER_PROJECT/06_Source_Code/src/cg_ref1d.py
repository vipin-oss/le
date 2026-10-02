"""cg_ref1d.py — INDEPENDENT 1-D axisymmetric references for the isotropic plane-strain annulus
a <= r <= R  (theta(a)=1, sigma_rr(a)=0 ; theta(R)=0, u(R)=0).               [added 2026-10-01, Phase 7/8]

These share NO code path with the 2-D mapped finite-difference solver (different formulation, different
discretisation): a log-radial Chebyshev spectral collocation in the Laplace domain (dynamic, coupled), and a
log-radial Crank-Nicolson time-domain heat solver + closed-form quasi-static (Lame) stress.  They are VERIFICATION
references (same mathematical model), not physical validation.

Model (per unit wall temperature amplitude, Laplace variable s):
  lam,mu : Lame constants;  m = lam + 2 mu;  gT = (3 lam + 2 mu) alpha   (plane strain, eps_zz = 0)
  sigma_rr = m u' + lam u/r - gT theta ;  sigma_tt = lam u' + m u/r - gT theta
  momentum : m (u'' + u'/r - u/r^2) - gT theta' = rho s^2 u
  energy   : (1/r) (r k g(s) theta')' = s ( rho cp theta + T0 gT (u' + u/r) )
  g(s) = 1 (Fourier) | 1/(1+s tau) (CV) | 0.5/(1+0.5 s tau) + 0.5/(1+2 s tau) (MCV3-type)
With x = ln(r/a), uh = u/a:
  m (uh_xx - uh) - gT r_h theta_x - rho s^2 a^2 r_h^2 uh = 0
  k g theta_xx - s rho cp a^2 r_h^2 theta - s T0 gT a^2 r_h (uh_x + uh) = 0           (r_h = e^x)
"""
import numpy as np
from scipy import sparse
from scipy.sparse.linalg import splu


def cheb(N):
    """Chebyshev differentiation matrix and nodes (Trefethen)."""
    x = np.cos(np.pi * np.arange(N + 1) / N)
    c = np.hstack([2.0, np.ones(N - 1), 2.0]) * (-1.0) ** np.arange(N + 1)
    X = np.tile(x, (N + 1, 1)).T
    dX = X - X.T
    D = np.outer(c, 1.0 / c) / (dX + np.eye(N + 1))
    D = D - np.diag(D.sum(axis=1))
    return D, x


def gfac(s, model, tau):
    if model == 'FOURIER':
        return 1.0
    if model == 'CV':
        return 1.0 / (1.0 + s * tau)
    if model == 'MCV3':
        return 0.5 / (1.0 + s * 0.5 * tau) + 0.5 / (1.0 + s * 2.0 * tau)
    raise ValueError(model)


def transfer_1d(s, a, R, k, rho, cp, T0, lam, mu, alpha, model='FOURIER', tau=0.0, N=120,
                coupling=True, inertia=True):
    """Wall hoop-stress transfer function (per unit wall temperature) at complex s [1/s]."""
    m = lam + 2.0 * mu
    gT = (3.0 * lam + 2.0 * mu) * alpha
    X = np.log(R / a)
    D, xi = cheb(N)
    x = X * (1.0 + xi) / 2.0                      # j=0 -> outer (x=X), j=N -> wall (x=0)
    Dx = (2.0 / X) * D
    Dxx = Dx @ Dx
    rh = np.exp(x)
    n = N + 1
    I = np.eye(n)
    g = gfac(s, model, tau)
    Rh = np.diag(rh)
    Rh2 = np.diag(rh ** 2)
    A = np.zeros((2 * n, 2 * n), complex)
    b = np.zeros(2 * n, complex)
    cpl = T0 * gT * (1.0 if coupling else 0.0)
    A[:n, :n] = k * g * Dxx - s * rho * cp * a * a * Rh2
    A[:n, n:] = -s * cpl * a * a * (Rh @ (Dx + I))
    A[n:, n:] = m * (Dxx - I) - ((rho * s * s * a * a) * Rh2 if inertia else 0.0)
    A[n:, :n] = -gT * (Rh @ Dx)
    jo, jw = 0, N
    # theta BCs
    A[jo, :] = 0.0; A[jo, jo] = 1.0; b[jo] = 0.0
    A[jw, :] = 0.0; A[jw, jw] = 1.0; b[jw] = 1.0
    # u BCs: outer clamped; wall traction-free  m uh_x + lam uh - gT theta = 0
    A[n + jo, :] = 0.0; A[n + jo, n + jo] = 1.0; b[n + jo] = 0.0
    A[n + jw, :] = 0.0
    A[n + jw, n:] = m * Dx[jw, :]
    A[n + jw, n + jw] += lam
    A[n + jw, jw] = -gT
    sol = np.linalg.solve(A, b)
    th, uh = sol[:n], sol[n:]
    uhx = Dx @ uh
    hoop = lam * uhx[jw] + m * uh[jw] - gT * th[jw]
    thx = Dx @ th
    q_wall = -k * g * thx[jw] / a                 # heat flux (outward normal = +r), per unit wall temp
    return dict(hoop=hoop, q_wall=q_wall, theta=th, uh=uh, x=x, residual=float(np.linalg.norm(A @ sol - b)))


def qs_single_pulse_reference(a, R, lam, mu, alpha, t0=2.5, tw=1.2, tstart=-7.0, tmax=9.0,
                              dt=0.002, N=1600):
    """Time-domain reference, Fourier conduction, quasi-static uncoupled isotropic plane strain.
    Heat equation  u_tau = exp(-2x) u_xx  (tau = t kappa/a^2, x = ln(r/a)), Crank-Nicolson, u(0)=p(tau), u(X)=0,
    zero initial state at tau=tstart.  Stress: closed-form Lame solution
        sigma_tt(a,t) = -2 mu g p(t) - 2 (lam+m) g F(t) / (R^2 + (lam+m) a^2/(2 mu)),
        g = gT/m,  F = int_a^R r theta dr   (free wall, clamped outer boundary).
    Returns tau, sigma_tt(a,tau) [Pa/K], p(tau)."""
    m = lam + 2.0 * mu
    gT = (3.0 * lam + 2.0 * mu) * alpha
    g = gT / m
    X = np.log(R / a)
    dx = X / N
    x = np.linspace(0.0, X, N + 1)
    w = np.exp(-2.0 * x[1:-1])                                   # coefficient at interior nodes
    nint = N - 1
    main = -2.0 * w / dx ** 2
    # row i (node x_{i+1}) uses w_i for both neighbours: sub-diagonal entry (i+1,i) = w_{i+1}/dx^2, super-diagonal (i,i+1) = w_i/dx^2
    L = sparse.diags([w[1:] / dx ** 2, main, w[:-1] / dx ** 2], [-1, 0, 1], shape=(nint, nint), format='csc')
    Id = sparse.identity(nint, format='csc')
    Aimp = (Id - 0.5 * dt * L).tocsc()
    Aexp = (Id + 0.5 * dt * L).tocsc()
    lu = splu(Aimp)
    nsteps = int(round((tmax - tstart) / dt))
    tau = tstart + dt * np.arange(nsteps + 1)
    p = np.exp(-((tau - t0) / tw) ** 2)
    u = np.zeros(nint)
    out = np.zeros(nsteps + 1)
    e2x = np.exp(2.0 * x)
    wts = np.full(N + 1, dx); wts[0] = wts[-1] = dx / 2.0        # trapezoid weights in x
    def stress(u_int, pw):
        full = np.concatenate(([pw], u_int, [0.0]))
        F = a * a * np.sum(wts * e2x * full)
        return -2.0 * mu * g * pw - 2.0 * (lam + m) * g * F / (R ** 2 + (lam + m) * a * a / (2.0 * mu))
    out[0] = stress(u, p[0])
    bc = np.zeros(nint)
    for n in range(nsteps):
        bc[0] = 0.5 * dt * w[0] / dx ** 2 * (p[n] + p[n + 1])
        u = lu.solve(Aexp @ u + bc)
        out[n + 1] = stress(u, p[n + 1])
    return tau, out, p
