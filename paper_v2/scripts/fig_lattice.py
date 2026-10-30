import numpy as np, matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from fig_common import *
a=1.0; k=np.linspace(0,np.pi/a,300)
chain=np.abs(np.sin(k*a/2))*2/a          # omega/c0, c0^2=K a^2/m
x2=0.25-1/np.pi**2                        # (xi/a)^2 matching omega at zone boundary
xi=np.sqrt(x2)
er_zb=k/np.sqrt(1+x2*(k*a)**2)
x2b=1/12.                                  # matching k^2 coefficient
er_sm=k/np.sqrt(1+x2b*(k*a)**2)
gr_neg=k*np.sqrt(np.clip(1-(k*a)**2/12,0,None))   # negative gradient coefficient
gr_pos=k*np.sqrt(1+(k*a)**2/12)
fig,ax=plt.subplots(1,2,figsize=(7.2,2.9))
ax[0].plot(k*a/np.pi,chain,color='k',label='monatomic chain (exact)')
ax[0].plot(k*a/np.pi,er_zb,color=C['LS'],label=rf'Eringen, $\xi={xi:.3f}a$ (zone-boundary fit)')
ax[0].plot(k*a/np.pi,er_sm,color=C['LS'],ls='--',label=r'Eringen, $\xi^2=a^2/12$ (long-wave fit)')
ax[0].plot(k*a/np.pi,gr_neg,color=C['DPL'],ls='-.',label=r'gradient, $\ell^2=-a^2/12$')
ax[0].plot(k*a/np.pi,gr_pos,color=C['DPL'],ls=':',label=r'gradient, $\ell^2=+a^2/12$')
ax[0].plot(k*a/np.pi,k,color=C['CD'],lw=0.8,ls=':',label='local')
ax[0].set_xlabel(r'$ka/\pi$'); ax[0].set_ylabel(r'$\omega a/c_0$'); ax[0].legend(frameon=False,fontsize=6,loc='upper left'); ax[0].set_ylim(0,3.4); ax[0].set_title('(a) dispersion',fontsize=9,loc='left')
vg_chain=np.cos(k*a/2)
vg_er=1/(1+x2*(k*a)**2)**1.5
ax[1].plot(k*a/np.pi,vg_chain,color='k',label='chain'); ax[1].plot(k*a/np.pi,vg_er,color=C['LS'],label='Eringen (zone-boundary fit)')
ax[1].set_xlabel(r'$ka/\pi$'); ax[1].set_ylabel(r'$v_g/c_0$'); ax[1].legend(frameon=False,fontsize=7); ax[1].set_title('(b) group velocity',fontsize=9,loc='left')
fig.tight_layout(); save(fig,'fig_lattice')
print('xi/a=',xi,' (Eringen quotes e0 a ~0.39 a)')
