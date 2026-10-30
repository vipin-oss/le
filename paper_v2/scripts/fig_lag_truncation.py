import numpy as np, matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from fig_common import *
# Uncoupled thermal branch for q(t+tau) = -k theta_x(t)  (DPL with tau_T = 0): G(s)=k e^{-tau s}
# truncations: first order 1/(1+tau s); second order 1/(1+tau s+tau^2 s^2/2); exact delay e^{-tau s}
w=np.logspace(-2,1.2,600); tau=1.0
fam=[('exact delay $e^{-\\tau s}$',lambda s:np.exp(-s*tau),'k','-'),
     ('1st order (Cattaneo)',lambda s:1/(1+tau*s),C['LS'],'--'),
     ('2nd order',lambda s:1/(1+tau*s+(tau*s)**2/2),C['DPL'],'-.')]
fig,ax=plt.subplots(1,2,figsize=(7.2,2.9))
for name,Gf,col,ls in fam:
    s=-1j*w; k2=-s/Gf(s); k=np.sqrt(k2)
    # choose root with Im k >=0
    kk=np.where(k.imag<0,-k,k)
    ax[0].loglog(w,np.abs(w/kk.real),color=col,ls=ls,label=name); ax[1].semilogx(w,kk.imag,color=col,ls=ls,label=name)
    if name.startswith('exact'): 
        kexact=k; 
ax[0].set_xlabel(r'$\omega\tau$'); ax[0].set_ylabel(r'$|v_p|/(\alpha/\tau)^{1/2}$'); ax[0].legend(frameon=False,fontsize=7); ax[0].set_title('(a) thermal-branch speed',fontsize=9,loc='left')
ax[1].set_xlabel(r'$\omega\tau$'); ax[1].set_ylabel(r'$\mathrm{Im}\,k\,(\alpha\tau)^{1/2}$'); ax[1].set_title('(b) attenuation',fontsize=9,loc='left'); ax[1].axvline(np.pi/2,color='k',ls=':',lw=0.7)
ax[1].set_ylim(-0.2,3.5)
fig.tight_layout(); save(fig,'fig_lag_truncation')
# exact-delay model: principal-branch k = sqrt(omega/alpha) exp(i(pi/4 - omega tau/2)); Im k changes sign at omega tau = pi/2
s=-1j*np.array([1.0,np.pi/2,2.0]); k=np.sqrt(-s/np.exp(-s*tau)); print('exact delay k (principal):',k, ' Im sign at 1, pi/2, 2:',np.sign(k.imag).tolist())
# quantify validity of truncations: relative error of k(1st order) vs exact at small omega tau
for wt in [0.05,0.1,0.3,1.0]:
    s=-1j*wt; ke=np.sqrt(-s/np.exp(-s)); k1=np.sqrt(-s*(1+s)); k2=np.sqrt(-s*(1+s+s*s/2))
    print(wt,'rel err 1st:',abs(k1-ke)/abs(ke),' 2nd:',abs(k2-ke)/abs(ke))
