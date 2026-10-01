import sys, os, time
os.environ['OPENBLAS_NUM_THREADS']='1'
sys.path.insert(0,'/home/user/work/rerun/proj'); sys.path.insert(0,'/home/user/work/rerun/proj/src')
import numpy as np
from scipy.integrate import quad
import run_production as rp
from cg_grid import Grid
from cg_model import rho, cp_ESTIMATED, T0
from cg_solver import HarmonicSolver
KISO,QISO,BISO=rp.KISO,rp.QISO,rp.BISO
lam,mu,beta=QISO[0,1],QISO[2,2],BISO[0]
a=1e-8; R=80*a
# exact steady (omega=0) solution: theta = ln(R/r)/ln(R/a), clamped outer (u=0), traction-free wall
th=lambda r: np.log(R/r)/np.log(R/a)
I=lambda r: quad(lambda s: th(s)*s, a, r, epsabs=0, epsrel=1e-13)[0]
IR=I(R)
C1=-(beta/(lam+2*mu))*IR/R/(R/2+(lam+mu)*a*a/(2*mu*R))
sig_exact = -(2*mu/(lam+2*mu))*beta + 2*(lam+mu)*C1
print(f"exact steady wall hoop (thermal-gradient load, clamped R=80a): {sig_exact:.2f} Pa/K ; infinite-domain local term alone: {-(2*mu/(lam+2*mu))*beta:.2f}")
for (Nr,Nt) in ((48,24),(96,48),(192,96),(384,96)):
    t0=time.time()
    g=Grid(chi=1.0,a=a,R=R,Nr=Nr,Nt=Nt)
    s=HarmonicSolver(g,KISO,np.asarray(QISO,complex),BISO,rho,cp_ESTIMATED,T0,model='FOURIER',tau=0.0)
    U,back=s.solve(0.0)
    hoop,t1,t2=s.stress_wall(U)
    th_num=s.fields(U)[0]
    # also check theta accuracy at a few radii
    r=g.r[:,None]*np.ones((1,Nt)); err_th=np.abs(th_num.real-th(r)).max()
    h=hoop.real.mean()
    print(f"{Nr:3d}x{Nt:3d}: wall hoop = {h:.1f} Pa/K  rel.err vs exact = {(h-sig_exact)/abs(sig_exact):+.4f}   (max theta err {err_th:.1e}, back {back:.1e}, {time.time()-t0:.0f}s)", flush=True)
