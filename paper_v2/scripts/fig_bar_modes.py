import numpy as np, matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from fig_common import *
# Longitudinal modes of a bar (clamped u=0, insulated theta_x=0 at both ends): k_n=n pi/L real, s complex.
# nondim: rho=1,c1=1,c_v=1,k=1 (omega*=1), T0=1, beta^2=eps.  Polynomial in s for LS (tau) / classical (tau=0):
# (K + s^2)(s(1+tau s) + K) + eps s K (1+tau s)=0   [uses G=1/(1+tau s) form multiplied through]
eps=0.1
def modes(K,tau):
    # expand: (K+s^2)(s+tau s^2+K)+eps K s(1+tau s)
    # s^2 * (tau s^2 + s + K) = tau s^4 + s^3 + K s^2 ; K*(tau s^2+s+K)= K tau s^2 + K s + K^2 ; eps K (s + tau s^2)
    c=[tau,1,K+K*tau+eps*K*tau,K+eps*K,K*K]
    return np.roots(c)
def elastic_root(K,tau):
    r=modes(K,tau)
    target=-1j*np.sqrt(K*(1+eps))      # adiabatic elastic
    return min(r,key=lambda z:abs(z-target)) if True else None
ks=np.logspace(-3,2,400); K=ks**2
fig,ax=plt.subplots(1,2,figsize=(7.2,2.9))
for lab,tau,col,ls in [('classical',0.0,C['CD'],'-'),('LS, $\\tau\\omega_*=0.25$',0.25,C['LS'],'--'),('LS, $\\tau\\omega_*=1$',1.0,C['DPL'],'-.')]:
    Q=[];V=[]
    prev=None
    for k,KK in zip(ks,K):
        r=modes(KK,tau) if tau>0 else None
        if tau==0:
            c=[1,eps*0+1,KK+eps*KK,KK,0]  # classical: (K+s^2)(s+K)+eps K s -> s^3+K s^2 ... build below
            c=np.polymul([1,0,KK],[1,KK]); c=np.polyadd(c,[eps*KK,0]); r=np.roots(c)
        # follow branch by continuity (start adiabatic)
        tgt=-1j*k*np.sqrt(1+eps) if prev is None else prev*(k/ks[max(0,list(ks).index(k)-1)])
        z=min(r,key=lambda z:abs(z-tgt)); prev=z
        w=1j*z; Q.append(2*abs(w.imag)/abs(w.real)); V.append(abs(w.real)/k)
    ax[0].loglog(ks,Q,color=col,ls=ls,label=lab); ax[1].semilogx(ks,V,color=col,ls=ls,label=lab)
ax[0].set_xlabel(r'wavenumber $k\,c_1/\omega_*$'); ax[0].set_ylabel(r'$Q^{-1}$ of bar mode with $k=n\pi/L$'); ax[0].legend(frameon=False,fontsize=7); ax[0].set_title('(a) loss',fontsize=9,loc='left')
ax[1].set_xlabel(r'wavenumber $k\,c_1/\omega_*$'); ax[1].set_ylabel(r'$|\mathrm{Re}\,\omega|/(k c_1)$'); ax[1].set_title('(b) modal speed',fontsize=9,loc='left')
fig.tight_layout(); save(fig,'fig_bar_modes')
# printed checks
for tau in [0.0,0.25,1.0]:
    for k in [0.01,0.1,1.0,3.0,10.0,30.0]:
        KK=k*k
        r=np.roots(np.polyadd(np.polymul([1,0,KK],[1,KK]),[eps*KK,0])) if tau==0 else modes(KK,tau)
        # pick root with smallest |Re(s)... choose elastic-like: largest |Im| among those with |Im|>... use adiabatic target
        cands=[z for z in r if abs(z.imag)>1e-9]
        z=min(cands,key=lambda z:abs(abs(z.imag)-k*np.sqrt(1+eps))) if k<0.5 else max(cands,key=lambda z:abs(z.imag)) if tau>0 else min(cands,key=lambda z:abs(abs(z.imag)-k*(1+eps/2*(1/(1+(k)**2)))))
        w=1j*z; print('tau=%.2f k=%.2g  w=%.4g%+.4gi  Q^-1=%.4g  Debye eps*x/(1+x^2)=%.4g'%(tau,k,w.real,w.imag,2*abs(w.imag)/abs(w.real),eps*k/(1+k*k)))
