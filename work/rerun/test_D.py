import sys, os, json, time
os.environ['OPENBLAS_NUM_THREADS']='1'
sys.path.insert(0,'/home/user/work/rerun/proj'); sys.path.insert(0,'/home/user/work/rerun/proj/src')
import numpy as np
from cg_grid import Grid
from cg_model import plane_strain_block, K_ac, rho, cp_ESTIMATED, T0, derived
from cg_solver import HarmonicSolver
from cg_transient import make_pulse, freq_grid, synthesize
DV=derived(); Q0,BETA0=plane_strain_block()

def run_series(model, tau_ps, a_nm, T_WIN=8.0, NT_T=128, W_CUT=12.0, eta_d=0.05, inertia=1.0, Rfac=80.0, NR=96, NTH=48):
    a=a_nm*1e-9; t_th=a*a/DV['kappa']; tau=tau_ps*1e-12
    g=Grid(chi=1.0,a=a,R=Rfac*a,Nr=NR,Nt=NTH)
    s=HarmonicSolver(g,K_ac,np.asarray(Q0,complex)*(1+1j*eta_d),BETA0,rho,cp_ESTIMATED,T0,model=model,tau=tau)
    if inertia!=1.0: s.Ain=s.Ain*inertia
    t,thp,TH=make_pulse(T_WIN*t_th,NT_T,2.5*t_th,1.2*t_th)
    wg=freq_grid(T_WIN*t_th,NT_T)
    nf=min(int(np.searchsorted(wg,W_CUT/t_th,side='right')),NT_T//2+1)
    H=np.zeros((nf,g.Nt),complex)
    for ik in range(nf):
        U,_=s.solve(wg[ik]); H[ik]=s.stress_wall(U)[0]
    hoop=np.array([synthesize(H[:,j],TH,NT_T) for j in range(g.Nt)])
    return t/t_th, hoop

def Dval(tc,hc,hf,tmax=None):
    if tmax is not None:
        n=int(np.searchsorted(tc,tmax,side='right')); hc=hc[:,:n]; hf=hf[:,:n]
    return float(np.abs(hc-hf).max()/np.abs(hf).max())

cases = {
 'baseline (as handoff: T=8, eta=0.05, inertia on)': dict(),
 'QUASI-STATIC (inertia switched off)':               dict(inertia=1e-9),
 'longer DFT window T=16':                            dict(T_WIN=16.0, NT_T=256),
 'more damping eta_d=0.20':                           dict(eta_d=0.20),
 'less damping eta_d=0.02':                           dict(eta_d=0.02),
}
pairs = {'a=10nm tau=5ps  (Lam=0.198)':(10,5.0), 'a=20nm tau=20ps (Lam=0.198)':(20,20.0)}
res={}
t00=time.time()
for cname,kw in cases.items():
    for pname,(a_nm,tau) in pairs.items():
        t,hf=run_series('FOURIER',0.0,a_nm,**kw)
        t,hc=run_series('CV',tau,a_nm,**kw)
        res[(cname,pname)]=(Dval(t,hc,hf),Dval(t,hc,hf,6.0), float(np.abs(hf).max()))
        print(f"[{time.time()-t00:5.0f}s] {cname:52s} | {pname} | D_full={res[(cname,pname)][0]:.4e}  D(t<=6)={res[(cname,pname)][1]:.4e}  max|sig_F|={res[(cname,pname)][2]:.5e}", flush=True)
print("\n==== SUMMARY: D at equal Lambda=0.198 ====")
print("stored handoff values: a=10/tau=5 -> 7.358e-3 ; a=20/tau=20 -> 2.102e-3  (ratio 3.50)")
for cname in cases:
    d10=res[(cname,'a=10nm tau=5ps  (Lam=0.198)')][0]; d20=res[(cname,'a=20nm tau=20ps (Lam=0.198)')][0]
    print(f"{cname:52s}: D10={d10:.3e}  D20={d20:.3e}  ratio D10/D20={d10/d20:.2f}")
json.dump({f'{k[0]}|{k[1]}':v for k,v in res.items()}, open('/home/user/work/rerun/D_tests_summary.json','w'), indent=1)
