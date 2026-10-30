import numpy as np, matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from fig_common import *
# uncoupled thermal branch, units: chi=k/c=1, tau=1.  GK: kw^2 = -s(1+tau s)/(chi + 3 l2 s)   (c_v absorbed)
w=np.logspace(-2,2.5,800); s=-1j*w
def kw(l2,tau=1.0):
    k2=-s*(1+tau*s)/(1+3*l2*s); k=np.sqrt(k2); return np.where(k.imag<0,-k,k)
fig,ax=plt.subplots(1,2,figsize=(7.2,2.9))
cases=[('Fourier ($\\tau=0,\\ell=0$)',dict(l2=0,tau=0),C['CD'],':'),('Cattaneo ($\\ell=0$)',dict(l2=0,tau=1),C['LS'],'-'),('GK, $\\ell^2=0.05$',dict(l2=0.05,tau=1),C['DPL'],'--'),('GK, $\\ell^2=0.3$',dict(l2=0.3,tau=1),C['GN'],'-.')]
for lab,p,col,ls in cases:
    k=kw(**p); ax[0].loglog(w,w/k.real,color=col,ls=ls,label=lab); ax[1].loglog(w,k.imag,color=col,ls=ls,label=lab)
ax[0].set_xlabel(r'$\omega\tau$'); ax[0].set_ylabel(r'$v_p/\sqrt{\chi/\tau}$'); ax[0].legend(frameon=False,fontsize=6.5); ax[0].set_title('(a) phase speed',fontsize=9,loc='left')
ax[1].set_xlabel(r'$\omega\tau$'); ax[1].set_ylabel(r'$\mathrm{Im}\,k\,\sqrt{\chi\tau}$'); ax[1].set_title('(b) attenuation',fontsize=9,loc='left')
fig.tight_layout(); save(fig,'fig_gk')
for lab,p,col,ls in cases:
    k=kw(**p); i=[np.argmin(abs(w-x)) for x in (0.1,1,10,100,300)]
    print(lab,' v_p:',np.round((w/k.real)[i],3),' Imk:',np.round(k.imag[i],3))
k=kw(0.3); print('GK 0.3 high-omega check v_p/sqrt(w): ',(w/k.real)[-1]/np.sqrt(w[-1]),' expect sqrt(2*3 l2/tau... )',np.sqrt(2*3*0.3))
