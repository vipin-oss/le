"""diag_covariance_floor.py — is the ~1e-8 field-covariance floor (V3, run 2) a round-off/conditioning effect?
Compares the stock solve with (i) one step of iterative refinement and (ii) column-equilibrated solve (unknowns rescaled).
Mathematically identical solutions; differences show the forward-error floor of the stock solve."""
import sys, os, time
sys.dont_write_bytecode = True
os.environ.setdefault('OPENBLAS_NUM_THREADS', '1')
def _pp_root(_start):
    """walk up from _start to the PAPER_PROJECT directory (path-independent replacement
    for the hard-coded '/home/user/PAPER_PROJECT' that used to be here)."""
    _p = os.path.abspath(_start)
    while True:
        if os.path.basename(_p) == 'PAPER_PROJECT':
            return _p
        _q = os.path.dirname(_p)
        if _q == _p:
            break
        _p = _q
    return os.environ.get('PAPER_PROJECT_ROOT', '/home/user/PAPER_PROJECT')
SRC = os.path.join(_pp_root(os.path.dirname(os.path.abspath(__file__))), '06_Source_Code', 'src'); sys.path.insert(0, SRC)
import numpy as np
from scipy import sparse
from scipy.sparse.linalg import splu
import cg_model as M, cg_pipeline as cp
from cg_grid import Grid
from cg_solver import HarmonicSolver
from cg_model import rho, cp_ESTIMATED, T0, K_ac
a = cp.A0; R = 80 * a; t_th = a * a / cp.KAPPA
Q0, B0 = M.plane_strain_block()
g = Grid(chi=1.0, a=a, R=R, Nr=96, Nt=48)
def mk(phi):
    K2 = M.rotate2(K_ac, np.radians(phi)) if phi else K_ac
    Q, b = M.rotate_Q_beta(Q0, B0, np.radians(phi)) if phi else (Q0, B0)
    return HarmonicSolver(g, K2, np.asarray(Q, complex), b, rho, cp_ESTIMATED, T0, model='CV', tau=0.3 * t_th)
def assemble(s, w):
    A = (sparse.diags(s.Dj) @ (s.Abase + (w ** 2) * s.Ain + (1j * w) * s.Ad + s.gfac(w) * s.Alap)).tocsr()
    rm = np.asarray(abs(A).max(axis=1).todense()).ravel(); rm[rm == 0] = 1.0
    return (sparse.diags(1.0 / rm) @ A).tocsc()
def solve_variants(s, w):
    A = assemble(s, w)
    lu = splu(A); U0 = lu.solve(s.rhs)
    r = s.rhs - A @ U0; U1 = U0 + lu.solve(r)                                   # iterative refinement x1
    cm = np.asarray(abs(A).max(axis=0).todense()).ravel(); cm[cm == 0] = 1.0   # column equilibration
    As = (A @ sparse.diags(1.0 / cm)).tocsc(); lus = splu(As); U2 = lus.solve(s.rhs) / cm
    return U0, U1, U2
def cov_err(sA, sB, w, shift, c, s_, variant):
    UA = solve_variants(sA, w)[variant]; UB = solve_variants(sB, w)[variant]
    thA, u1A, u3A = sA.fields(UA); thB, u1B, u3B = sB.fields(UB)
    r = lambda x: np.roll(x, shift, axis=1)
    eu = max(np.abs(u1B - (c * r(u1A) - s_ * r(u3A))).max(), np.abs(u3B - (s_ * r(u1A) + c * r(u3A))).max()) / max(np.abs(u1A).max(), np.abs(u3A).max())
    hA = sA.stress_wall(UA)[0]; hB = sB.stress_wall(UB)[0]
    eh = np.abs(hB - np.roll(hA, shift)).max() / np.abs(hA).max()
    return float(eu), float(eh)
sA = mk(0)
for phi in (90, 45):
    sB = mk(phi); shift = phi // 15 * 2; c, s_ = np.cos(np.radians(phi)), np.sin(np.radians(phi))
    for sv in (0.9 + 0j, 0.9 + 2.5j, 0.9 + 6j):
        w = -1j * sv / t_th
        out = [cov_err(sA, sB, w, shift, c, s_, v) for v in (0, 1, 2)]
        print(f"phi={phi} s={sv}: (u,hoop) stock={out[0][0]:.1e},{out[0][1]:.1e}  refined={out[1][0]:.1e},{out[1][1]:.1e}  colscaled={out[2][0]:.1e},{out[2][1]:.1e}", flush=True)
