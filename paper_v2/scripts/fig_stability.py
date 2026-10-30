import numpy as np, matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from numpy.polynomial import polynomial as P
from fig_common import *
# Coupled 1D DPL, real wavenumber k, temporal roots s (rho=c=c1=k_cond=1, tau_q=1):
#   (K+s^2)(s L(s)+(1+tT s)K) + eps s K L(s) = 0,
#   L = 1+tq s  (first-order in tau_q)  or  1+tq s+tq^2 s^2/2  (second-order)
eps=0.1; tq=1.0
def smax(tT,K,order):
    L=np.array([1.0,tq]) if order==1 else np.array([1.0,tq,tq**2/2])
    A=np.array([K,0,1.0]); sL=np.concatenate([[0],L])
    B=P.polyadd(sL,K*np.array([1.0,tT])); Cc=eps*K*P.polymul([0,1.0],L)
    return np.roots(P.polyadd(P.polymul(A,B),Cc)[::-1]).real.max()
Ks=np.logspace(-2,6,1200)
fig,ax=plt.subplots(1,2,figsize=(7.2,2.9))
for r,col in [(0.3,'#D55E00'),(0.45,'#E69F00'),(0.5,'#009E73'),(0.7,'#0072B2')]:
    m=[smax(r*tq,K,2) for K in Ks]
    ax[0].semilogx(np.sqrt(Ks),m,color=col,label=rf'$\tau_T/\tau_q={r}$')
ax[0].axhline(0,color='k',lw=0.6); ax[0].set_xlabel(r'wavenumber $k\,c_1\tau_q$'); ax[0].set_ylabel(r'$\max\,\mathrm{Re}\,s\;\tau_q$')
ax[0].legend(frameon=False,fontsize=7); ax[0].set_title(r'(a) growth rate, 2nd-order in $\tau_q$',fontsize=9,loc='left'); ax[0].set_ylim(-0.2,1.6)
rr=np.linspace(0.05,1.2,70)
w2=[max(smax(r*tq,K,2) for K in Ks) for r in rr]; w1=[max(smax(r*tq,K,1) for K in Ks) for r in rr]
ax[1].plot(rr,w2,color=C['DPL'],label=r'second order in $\tau_q$'); ax[1].plot(rr,w1,color=C['LS'],label=r'first order in $\tau_q$')
ax[1].axhline(0,color='k',lw=0.6); ax[1].axvline(0.5,color='k',ls=':',lw=0.8)
ax[1].set_xlabel(r'$\tau_T/\tau_q$'); ax[1].set_ylabel(r'$\sup_k\,\mathrm{Re}\,s\;\tau_q$'); ax[1].set_ylim(-0.1,1.6)
ax[1].set_title('(b) stability boundary',fontsize=9,loc='left'); ax[1].legend(frameon=False,fontsize=7)
fig.tight_layout(); save(fig,'fig_stability')
print('max growth 2nd order at r=0.3:',max(smax(0.3,K,2) for K in Ks),' first order r=0.3:',max(smax(0.3,K,1) for K in Ks))
