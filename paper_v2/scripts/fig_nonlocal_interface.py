import numpy as np, matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from fig_common import *
k=np.linspace(0,4,400)
# nonlocal (Eringen): w^2=c^2 k^2/(1+xi^2 k^2); gradient (Aifantis-type): w^2=c^2 k^2 (1+l^2 k^2); xi,l = 0.5 ell
xi=0.5
wn=k/np.sqrt(1+(xi*k)**2); wg=k*np.sqrt(1+(xi*k)**2)
fig,ax=plt.subplots(1,3,figsize=(7.4,2.6))
ax[0].plot(k,k,color=C['CD'],ls=':',label='classical'); ax[0].plot(k,wn,color=C['LS'],label='Eringen nonlocal'); ax[0].plot(k,wg,color=C['DPL'],label='strain gradient')
ax[0].axhline(1/xi,color=C['LS'],lw=0.6,ls='--'); ax[0].text(0.1,1/xi+0.08,r'cut-off $c/\xi$',fontsize=7,color=C['LS'])
ax[0].set_xlabel(r'wavenumber $k\ell$'); ax[0].set_ylabel(r'$\omega\ell/c$'); ax[0].set_title('(a) dispersion',fontsize=9,loc='left'); ax[0].legend(frameon=False,loc='upper left',fontsize=7); ax[0].set_ylim(0,6)
vp_n=1/np.sqrt(1+(xi*k)**2); vg_n=1/(1+(xi*k)**2)**1.5
vp_g=np.sqrt(1+(xi*k)**2); vg_g=(1+2*(xi*k)**2)/np.sqrt(1+(xi*k)**2)
ax[1].plot(k,vp_n,color=C['LS'],label=r'$v_p$'); ax[1].plot(k,vg_n,color=C['LS'],ls='--',label=r'$v_g$')
ax[1].set_xlabel(r'$k\ell$'); ax[1].set_ylabel(r'speed$/c$'); ax[1].set_title('(b) nonlocal: speeds',fontsize=9,loc='left'); ax[1].legend(frameon=False)
ax[2].plot(k,vp_g,color=C['DPL'],label=r'$v_p$'); ax[2].plot(k,vg_g,color=C['DPL'],ls='--',label=r'$v_g$')
ax[2].set_xlabel(r'$k\ell$'); ax[2].set_title('(c) gradient: speeds',fontsize=9,loc='left'); ax[2].legend(frameon=False)
fig.tight_layout(); save(fig,'fig_nonlocal')
# interface
Z=np.logspace(-1.5,1.5,400)  # Z2/Z1
r=(1-Z)/(1+Z); t=2/(1+Z); RE=r**2; TE=4*Z/(1+Z)**2
assert np.allclose(RE+TE,1)
fig,ax=plt.subplots(1,2,figsize=(7.2,2.7))
ax[0].semilogx(Z,r,color=C['LS'],label=r'$r=(Z_1-Z_2)/(Z_1+Z_2)$'); ax[0].semilogx(Z,t,color=C['DPL'],label=r'$t=2Z_1/(Z_1+Z_2)$')
ax[0].axhline(0,color='k',lw=0.5); ax[0].axvline(1,color='k',lw=0.5,ls=':')
ax[0].set_xlabel(r'impedance ratio $Z_2/Z_1$'); ax[0].set_ylabel('amplitude coefficient'); ax[0].set_title('(a) amplitudes (displacement)',fontsize=9,loc='left'); ax[0].legend(frameon=False,fontsize=7,loc='upper right')
ax[1].semilogx(Z,RE,color=C['LS'],label=r'$\mathcal{R}=r^2$'); ax[1].semilogx(Z,TE,color=C['DPL'],label=r'$\mathcal{T}=4Z_1Z_2/(Z_1+Z_2)^2$'); ax[1].semilogx(Z,RE+TE,color='k',ls=':',lw=1,label=r'$\mathcal{R}+\mathcal{T}=1$')
ax[1].axvline(1,color='k',lw=0.5,ls=':'); ax[1].set_ylim(-0.02,1.15); ax[1].set_xlabel(r'impedance ratio $Z_2/Z_1$'); ax[1].set_ylabel('energy fraction'); ax[1].set_title('(b) energy partition',fontsize=9,loc='left'); ax[1].legend(frameon=False,fontsize=7,loc='upper center',ncol=1)
fig.tight_layout(); save(fig,'fig_interface')
# piezo stiffening
K2=np.linspace(0,0.6,100)
fig,ax=plt.subplots(figsize=(3.4,2.5))
ax.plot(K2,np.sqrt(1+K2),color=C['GN'],label=r'$v/v_0=\sqrt{1+K^2}$'); ax.plot(K2,1+0*K2,color=C['CD'],ls=':',label='no piezoelectric coupling')
ax.set_xlabel(r'coupling $K^2=e^2/(\varepsilon c^E)$'); ax.set_ylabel(r'$v/v_0$'); ax.legend(frameon=False,fontsize=7); fig.tight_layout(); save(fig,'fig_piezo')
print('ok')
