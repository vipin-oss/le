import sys, os, json, time
os.environ['OPENBLAS_NUM_THREADS']='1'
sys.path.insert(0,'/home/user/work/rerun/proj'); sys.path.insert(0,'/home/user/work/rerun/proj/src')
import numpy as np
import run_production as rp
from cg_grid import Grid
from cg_model import rho, cp_ESTIMATED, T0, derived, K_ac, Cij_GPa, GPa, alpha_crys
from cg_solver import HarmonicSolver
from cg_transient import make_pulse, freq_grid, synthesize
DV=derived(); Q0,B0=rp.Q0,rp.BETA0; KISO,QISO,BISO=rp.KISO,rp.QISO,rp.BISO
orig=rp.rotate_Q_beta
def fixed(Q,beta,phi):
    Qr,br=orig(Q,beta,phi); c,s=np.cos(phi),np.sin(phi); br=br.copy(); br[1]+=4*s*c*Cij_GPa['C25']*GPa*alpha_crys[1]; return Qr,br
def series(chi=1.0,phi_deg=0,iso=False,T_WIN=8.0,inertia=1.0,eta_d=0.05,W_CUT=10.0,NR=96,NTH=48,a_nm=10):
    a=a_nm*1e-9; t_th=a*a/DV['kappa']; phi=np.radians(phi_deg)
    if iso: K2,Q,b=KISO,QISO,BISO
    else:
        K2=rp.rotate2(K_ac,phi) if phi_deg else K_ac
        Q,b=fixed(Q0,B0,phi) if phi_deg else (Q0,B0)
    g=Grid(chi=chi,a=a,R=80.0*a,Nr=NR,Nt=NTH)
    s=HarmonicSolver(g,K2,np.asarray(Q,complex)*(1+1j*eta_d),b,rho,cp_ESTIMATED,T0,model='FOURIER',tau=0.0)
    if inertia!=1.0: s.Ain=s.Ain*inertia
    NT_T=int(round(16*T_WIN))
    t,thp,TH=make_pulse(T_WIN*t_th,NT_T,2.5*t_th,1.2*t_th)
    wg=freq_grid(T_WIN*t_th,NT_T); nf=min(int(np.searchsorted(wg,W_CUT/t_th,side='right')),NT_T//2+1)
    H=np.zeros((nf,g.Nt),complex)
    for ik in range(nf):
        U,_=s.solve(wg[ik]); H[ik]=s.stress_wall(U)[0]
    hoop=np.array([synthesize(H[:,j],TH,NT_T) for j in range(g.Nt)])
    tn=t/t_th; n=int(np.searchsorted(tn,6.0,side='right'))
    return float(np.abs(hoop[:,:n]).max()), tn, hoop
which=sys.argv[1]
t00=time.time()
if which=='A':
    jobs=[('iso circle',dict(iso=True)),('aniso circle phi=0',dict())]
else:
    jobs=[('ellipse phi=90',dict(chi=2.0,phi_deg=90)),('ellipse phi=150',dict(chi=2.0,phi_deg=150))]
for name,kw in jobs:
    for T in (8.0,64.0):
        pk,tn,h=series(T_WIN=T,inertia=1e-9,**kw)
        print(f"[{time.time()-t00:4.0f}s] {name:20s} QUASI-STATIC elasticity, DFT window T={T:4.0f} t_th (pulse-train mean={1.7725*1.2/T:.3f}):  peak|hoop| = {pk:.1f} Pa/K", flush=True)
