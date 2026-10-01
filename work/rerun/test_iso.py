import sys, os, json, time
os.environ['OPENBLAS_NUM_THREADS']='1'
sys.path.insert(0,'/home/user/work/rerun/proj'); sys.path.insert(0,'/home/user/work/rerun/proj/src')
import numpy as np
import run_production as rp
from cg_grid import Grid
from cg_model import rho, cp_ESTIMATED, T0, derived, K_ac
from cg_solver import HarmonicSolver
from cg_transient import make_pulse, freq_grid, synthesize
DV=derived(); KISO,QISO,BISO=rp.KISO,rp.QISO,rp.BISO

def run_iso(a_nm=10, T_WIN=8.0, NT_T=128, W_CUT=12.0, eta_d=0.05, inertia=1.0, Rfac=80.0, NR=96, NTH=48, model='FOURIER'):
    a=a_nm*1e-9; t_th=a*a/DV['kappa']
    g=Grid(chi=1.0,a=a,R=Rfac*a,Nr=NR,Nt=NTH)
    s=HarmonicSolver(g,KISO,np.asarray(QISO,complex)*(1+1j*eta_d),BISO,rho,cp_ESTIMATED,T0,model=model,tau=0.0)
    if inertia!=1.0: s.Ain=s.Ain*inertia
    t,thp,TH=make_pulse(T_WIN*t_th,NT_T,2.5*t_th,1.2*t_th)
    wg=freq_grid(T_WIN*t_th,NT_T)
    nf=min(int(np.searchsorted(wg,W_CUT/t_th,side='right')),NT_T//2+1)
    H=np.zeros((nf,g.Nt),complex); HW=np.zeros((nf,g.Nt),complex)
    for ik in range(nf):
        U,_=s.solve(wg[ik]); H[ik]=s.stress_wall(U)[0]; HW[ik]=s.wall_theta(U)
    hoop=np.array([synthesize(H[:,j],TH,NT_T) for j in range(g.Nt)])
    wall=np.array([synthesize(HW[:,j],TH,NT_T) for j in range(g.Nt)])
    return t/t_th, hoop, wall, thp

lam,mu=QISO[0,1],QISO[2,2]; beta=BISO[0]
sig_an = 2*mu*beta/(lam+2*mu)
print(f"ANALYTIC quasi-static infinite-domain wall hoop per K: -(2*mu*beta/(lam+2mu)) = {sig_an:.1f} Pa/K  (beta={beta:.4e}, lam={lam:.3e}, mu={mu:.3e})", flush=True)
print("handoff stored D_iso_circle sig_max:", json.load(open('/home/user/work/rerun/proj/data/PROD/D_iso_circle.json'))['sig_max'], flush=True)
tests=[('dynamic, as handoff (96x48, T=8, eta=.05)',dict()),
       ('QUASI-STATIC 96x48',dict(inertia=1e-9)),
       ('QUASI-STATIC 192x96',dict(inertia=1e-9,NR=192,NTH=96)),
       ('dynamic, T=16 window',dict(T_WIN=16.0,NT_T=256)),
       ('dynamic, eta=0.2',dict(eta_d=0.2))]
for name,kw in tests:
    t0=time.time()
    t,h,w,thp=run_iso(**kw)
    pk=np.abs(h).max()
    # compare time-history against analytic quasi-static -sig_an*theta_w(t)
    hw=h[0]; ref=-sig_an*w[0].real
    n=int(np.searchsorted(t,6.0,side='right'))
    err=np.abs(hw[:n]-ref[:n]).max()/sig_an
    print(f"{name:45s} peak|hoop|={pk:12.1f} Pa/K  ratio to analytic={pk/sig_an:.4f}  max time-hist dev from analytic (t<=6)={err:.4f}  [{time.time()-t0:.0f}s]", flush=True)
