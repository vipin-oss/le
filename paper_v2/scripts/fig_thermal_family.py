import numpy as np, matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from models import G
from fig_common import *
w=np.logspace(-2.5,2,500)
fam=[('Fourier',dict(k=1,ks=0,tq=0,tT=0,tv=0),'#444444','-'),
     ('Lord–Shulman',dict(k=1,ks=0,tq=1,tT=0,tv=0),'#0072B2','-'),
     ('DPL ($\\tau_T=0.5\\tau_q$)',dict(k=1,ks=0,tq=1,tT=0.5,tv=0),'#D55E00','--'),
     ('GN-II',dict(k=0,ks=0.25,tq=0,tT=0,tv=0),'#009E73','-'),
     ('GN-III',dict(k=1,ks=0.25,tq=0,tT=0,tv=0),'#CC79A7','-'),
     ('MGT',dict(k=1,ks=0.25,tq=1,tT=0,tv=0),'#E69F00','--')]
fig,ax=plt.subplots(1,2,figsize=(7.2,2.9))
for name,p,col,ls in fam:
    s=-1j*w; k2=-s/G(s,p); k=np.sqrt(k2); k=np.where(k.imag<0,-k,k)
    ax[0].loglog(w,w/k.real,color=col,ls=ls,label=name)
    ax[1].loglog(w,k.imag,color=col,ls=ls,label=name)
ax[0].set_xlabel(r'$\omega\tau$'); ax[0].set_ylabel(r'phase speed $v_p/(\alpha/\tau)^{1/2}$'); ax[0].legend(frameon=False,fontsize=6.5,loc='upper left'); ax[0].set_title('(a) uncoupled thermal branch',fontsize=9,loc='left')
ax[1].set_xlabel(r'$\omega\tau$'); ax[1].set_ylabel(r'attenuation $\mathrm{Im}\,k\,(\alpha\tau)^{1/2}$'); ax[1].set_title('(b)',fontsize=9,loc='left')
for a in ax: a.set_ylim(None,None)
ax[0].set_ylim(0.05,30)
fig.tight_layout(); save(fig,'fig_thermal_family')
# checks of limiting speeds
for name,p,_,_ in fam:
    for ww in (1e-3,1e2):
        s=-1j*ww; k=np.sqrt(-s/G(s,p)); k=k if k.imag>=0 else -k; print(name,ww,'v_p=',round(ww/k.real,4))
