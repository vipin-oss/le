import numpy as np, matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt, mpmath as mp
from fig_common import *
# semi-infinite rod, flux q0 H(t) at x=0, alpha=1, tau relaxation. Uncoupled, Laplace domain:
# Fourier: T^=q0/(k) * exp(-x sqrt(s/alpha))/(s sqrt(s/alpha))
# Cattaneo (prescribed flux q(0,t)=q0 H(t), q^=-k/(1+tau s) T^_x): T^=q0 (1+tau s)/(k s) * exp(-x sqrt(s(1+tau s)/alpha))/sqrt(s(1+tau s)/alpha)
al=1.0; tau=1.0; k=1.0; q0=1.0
def Tf(x,t): return (q0/k)*(2*mp.sqrt(al*t/mp.pi)*mp.exp(-x*x/(4*al*t))-x*mp.erfc(x/(2*mp.sqrt(al*t))))
def Tc(x,t):
    F=lambda s: (q0/k)*(1+tau*s)/s*mp.exp(-x*mp.sqrt(s*(1+tau*s)/al))/mp.sqrt(s*(1+tau*s)/al)
    if t<=x/mp.sqrt(al/tau): return mp.mpf(0)   # exact: no signal ahead of the front
    return mp.invertlaplace(F,t,method='talbot')
mp.mp.dps=20
xs=1.5; ts=np.linspace(0.02,6,160)
Tfv=[float(Tf(xs,t)) for t in ts]; Tcv=[float(Tc(xs,t)) for t in ts]
# front: x = c t, c=sqrt(al/tau)
fig,ax=plt.subplots(1,2,figsize=(7.2,2.8))
ax[0].plot(ts,Tfv,color=C['CD'],label='Fourier'); ax[0].plot(ts,Tcv,color=C['LS'],label='Cattaneo / LS')
ax[0].axvline(xs/np.sqrt(al/tau),color='k',ls=':',lw=0.8); ax[0].text(0.08,1.05,'wave front\n$t=x/c_T$',fontsize=7)
ax[0].set_xlabel(r'time $t/\tau$'); ax[0].set_ylabel(r'temperature $T k/(q_0 \ell)$'); ax[0].set_title(r'(a) history at $x=1.5\,\ell$',fontsize=9,loc='left'); ax[0].legend(frameon=False)
xx=np.linspace(0.02,5,140); tt=2.0
ax[1].plot(xx,[float(Tf(x,tt)) for x in xx],color=C['CD'],label='Fourier')
ax[1].plot(xx,[float(Tc(x,tt)) for x in xx],color=C['LS'],label='Cattaneo / LS')
ax[1].axvline(np.sqrt(al/tau)*tt,color='k',ls=':',lw=0.8)
ax[1].set_xlabel(r'position $x/\ell$,  $\ell=\sqrt{\alpha\tau}$'); ax[1].set_title(r'(b) profile at $t=2\tau$',fontsize=9,loc='left')
fig.tight_layout(); save(fig,'fig_heatpulse')
# checks
print('Cattaneo at x=1.5,t=0.9 (before front 1.5):',float(Tc(1.5,0.9)),' Fourier:',float(Tf(1.5,0.9)))
print('late time ratio t=40:',float(Tc(1.5,40)/Tf(1.5,40)))
