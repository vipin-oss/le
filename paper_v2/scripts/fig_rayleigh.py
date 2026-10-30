"""Thermoelastic Rayleigh waves on a half-space y>0, plane strain, propagation along x (wavenumber k real).
Nondim: rho=1, lambda+2mu=1 (c1=1), c=1, k_cond=1 (omega_*=1), T0=1, beta=sqrt(eps).
Temporal roots s=-i w of the 3x3 boundary determinant (traction-free; insulated or isothermal)."""
import numpy as np, mpmath as mp, matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy.optimize import brentq
from fig_common import *
nu=0.3; cs2=(1-2*nu)/(2-2*nu); mu=cs2; lam=1-2*mu
def Gof(s,model,tq,tT):
    return {'CD':1,'LS':1/(1+tq*s),'DPL':(1+tT*s)/(1+tq*s)}[model] if model!='CD' else 1
def det(s,k,eps,model,tq,tT,bc):
    G=Gof(s,model,tq,tT); beta=mp.sqrt(eps)
    a=G; b=-(G*s**2+s+eps*s); c=s**3
    d=mp.sqrt(b*b-4*a*c); kap=[(-b+d)/(2*a),(-b-d)/(2*a)]
    ms=[]; 
    for kk in kap:
        m=mp.sqrt(kk+k**2); m= m if mp.re(m)>0 else -m; ms.append(m)
    kaps=s**2/cs2; msh=mp.sqrt(kaps+k**2); msh= msh if mp.re(msh)>0 else -msh
    th=[(kk-s**2)/beta for kk in kap]       # theta_j per unit phi_j
    I=mp.mpc(0,1)
    row_sig=[lam*kap[j]+2*mu*ms[j]**2-beta*th[j] for j in range(2)]+[2*mu*I*k*msh]
    row_tau=[-2*mu*I*k*ms[j] for j in range(2)]+[mu*(msh**2+k**2)]
    row_th=[(-ms[j]*th[j] if bc=='ins' else th[j]) for j in range(2)]+[0]
    return mp.matrix([row_sig,row_tau,row_th])
def D(s,*a): return mp.det(det(s,*a))
def rayleigh_classical():
    f=lambda c: (2-c**2/cs2)**2-4*np.sqrt(1-c**2)*np.sqrt(1-c**2/cs2)
    return brentq(f,0.5*np.sqrt(cs2),np.sqrt(cs2)*0.999)
def root(k,eps,model,tq,tT,bc,guess):
    f=lambda s: D(s,k,eps,model,tq,tT,bc)
    return mp.findroot(f,guess,solver='muller',tol=1e-18,maxsteps=80)

def track(eps,model,tq,tT,bc,ks):
    out=[]; g=mp.mpc(0,-cR_ * ks[0])
    for i,k in enumerate(ks):
        g0=g if i==0 else mp.mpc(0,-1)*w_prev
        f=lambda s: D(s,k,eps,model,tq,tT,bc)
        s=mp.findroot(f,(g0*1.001,g0*0.999),solver='secant',tol=1e-16,maxsteps=100)
        w_prev=1j*s*(k_next:=1.0) if False else 1j*s
        out.append(complex(1j*s)/k)    # complex w/k
        w_prev=1j*s*((ks[min(i+1,len(ks)-1)])/k)
    return np.array(out)
cR_=rayleigh_classical()

def make_figure():
    ks=np.logspace(-2,2,50); eps=0.05
    cases=[('CD','CD',0,0,'ins','classical, insulated','-','CD'),('CD','CD',0,0,'iso','classical, isothermal','--','accent'),
           ('LS','LS',0.25,0,'ins','Lord–Shulman, insulated','-','LS')]
    fig,ax=plt.subplots(1,2,figsize=(7.2,2.9)); cR=rayleigh_classical()
    for m,_,tq,tT,bc,lab,ls,col in cases:
        r=track(eps,m,tq,tT,bc,ks)
        ax[0].semilogx(ks,(r.real/cR-1)*1e3,color=C[col],ls=ls,label=lab)
        ax[1].loglog(ks,2*np.abs(r.imag)/r.real,color=C[col],ls=ls,label=lab)
    ax[0].set_xlabel(r'wavenumber $k c_1/\omega_*$'); ax[0].set_ylabel(r'$(c_R/c_R^{\rm iso}-1)\times10^{3}$'); ax[0].legend(frameon=False,fontsize=6.5); ax[0].set_title('(a) Rayleigh speed',fontsize=9,loc='left')
    ax[1].set_xlabel(r'wavenumber $k c_1/\omega_*$'); ax[1].set_ylabel(r'$Q^{-1}=2|\mathrm{Im}\,\omega|/\mathrm{Re}\,\omega$'); ax[1].set_title('(b) temporal damping',fontsize=9,loc='left')
    fig.tight_layout(); save(fig,'fig_rayleigh')
if __name__=='__main__': make_figure()
