import sys, os
os.environ['OPENBLAS_NUM_THREADS']='1'
sys.path.insert(0,'/home/user/work/rerun/proj'); sys.path.insert(0,'/home/user/work/rerun/proj/src')
import numpy as np
import run_production as rp
from cg_grid import Grid
from cg_model import plane_strain_block, K_ac, rho, cp_ESTIMATED, T0, derived, rotate_Q_beta, Cij_GPa, GPa, alpha_crys
from cg_solver import HarmonicSolver
DV=derived(); Q0,b0=plane_strain_block()
def fixed(Q,beta,phi):
    Qr,br=rotate_Q_beta(Q,beta,phi); c,s=np.cos(phi),np.sin(phi); br=br.copy(); br[1]+=4*s*c*Cij_GPa['C25']*GPa*alpha_crys[1]; return Qr,br
dQ=lambda Q: np.asarray(Q,complex)*(1+0.05j)     # same damping as VERIFY (assumed eta=0.05)
g=Grid(chi=1.0,a=1e-8,R=80.0*1e-8,Nr=96,Nt=48); t_th=g.a**2/DV['kappa']
w_test=[2*np.pi/(3*t_th),2*np.pi/(0.8*t_th)]
sA=HarmonicSolver(g,K_ac,dQ(Q0),b0,rho,cp_ESTIMATED,T0,model='CV',tau=0.3*t_th)
def rot_case(phi_deg,fn):
    phi=np.radians(phi_deg); Q,b=fn(Q0,b0,phi); K=rp.rotate2(K_ac,phi)
    sC=HarmonicSolver(g,K,dQ(Q),b,rho,cp_ESTIMATED,T0,model='CV',tau=0.3*t_th)
    errs=[]
    for w in w_test:
        UA,_=sA.solve(w); UC,_=sC.solve(w)
        hA=sA.stress_wall(UA)[0]; hC=sC.stress_wall(UC)[0]
        sh=phi_deg/360.0*g.Nt; j0=int(np.floor(sh)); fr=sh-j0
        hA_s=(1-fr)*np.roll(hA,j0)+fr*np.roll(hA,j0+1)
        errs.append(float(np.abs(hC-hA_s).max()/np.abs(hA).max()))
    return max(errs)
for phi in (37.0,45.0,15.0,135.0):
    print(f"phi={phi:5.1f} deg  wall-hoop covariance error: ORIGINAL rotate_Q_beta = {rot_case(phi,rotate_Q_beta):.3e}   |  FIXED = {rot_case(phi,fixed):.3e}   {'(exact lattice rotation, no interpolation)' if (phi*48/360)%1==0 else '(needs interpolation)'}")
