import numpy as np, mpmath as mp, matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy.integrate import quad
from fig_common import *
mp.mp.dps=20
# (a) fractional (Caputo) heat equation, prescribed boundary temperature: theta^ = (1/s) exp(-x s^{alpha/2})   (a=1)
def th(x,t,al):
    return float(mp.re(mp.invertlaplace(lambda s: mp.exp(-x*s**(mp.mpf(al)/2))/s,t,method='talbot')))
xs=np.linspace(0.0,3.5,70); t0=1.0
fig,ax=plt.subplots(1,3,figsize=(7.4,2.6))
for al,col,ls in [(0.5,'#D55E00','-'),(1.0,'#444444','-'),(1.5,'#0072B2','-'),(2.0,'#009E73','--')]:
    v=[th(x,t0,al) if (x>0 or al<2) else 1.0 for x in xs]
    if al==2.0: v=[1.0 if x<t0 else 0.0 for x in xs]
    ax[0].plot(xs,v,color=col,ls=ls,label=rf'$\alpha={al}$')
ax[0].set_xlabel(r'$x/\sqrt{a\,t_0^{\alpha}}$ ($t=t_0$)'); ax[0].set_ylabel(r'$\theta/\theta_0$'); ax[0].legend(frameon=False,fontsize=7); ax[0].set_title('(a) Caputo heat equation',fontsize=9,loc='left')
# (b) MDD kernels
u=np.linspace(0,1,200)
for (a_,b_),col,lab in [((1,1),'#0072B2',r'$a=b=1$:\ $(1-u/\tau)^2$'),((0,0.5),'#D55E00',r'$a=0,b=0.5$:\ $1-u/\tau$'),((0,0),'#444444',r'$a=b=0$:\ $1$')]:
    ax[1].plot(u,1-2*b_*u+a_*u**2,color=col,label=lab)
ax[1].set_xlabel(r'$u/\tau$'); ax[1].set_ylabel(r'$K(u)$'); ax[1].legend(frameon=False,fontsize=6); ax[1].set_title('(b) MDD kernels',fontsize=9,loc='left')
# (c) thermal-branch phase speed: Cattaneo (LS), fractional Cattaneo, MDD-Cattaneo; rho c=1,k=1,tau=1
w=np.logspace(-2,1.5,300)
def kappa(s,tau=1.0):
    f=lambda x,part: ((1-x/tau)**2*np.exp(-s*x)).real if part==0 else ((1-x/tau)**2*np.exp(-s*x)).imag
    return (quad(f,0,tau,args=(0,))[0]+1j*quad(f,0,tau,args=(1,))[0])/tau
def kth(G,s):
    k=np.sqrt(-s/G); return np.where(k.imag<0,-k,k)
def vp(Gfun):
    out=[]
    for x in w:
        s=-1j*x; k=complex(kth(Gfun(s),s)); out.append(x/k.real)
    return np.array(out)
ax[2].loglog(w,vp(lambda s:1.0),color='#444444',label='Fourier')
ax[2].loglog(w,vp(lambda s:1/(1+s)),color='#0072B2',label='Cattaneo')
ax[2].loglog(w,vp(lambda s:1/(1+s**0.8) if False else 1/(1+(s+0j)**0.8)),color='#D55E00',label=r'fractional, $\alpha=0.8$')
ax[2].loglog(w,vp(lambda s:1/(1+s*kappa(s))),color='#009E73',ls='--',label='MDD-Cattaneo')
ax[2].set_xlabel(r'$\omega\tau$'); ax[2].set_ylabel(r'$v_p/\sqrt{k/\rho c\tau}$'); ax[2].legend(frameon=False,fontsize=6); ax[2].set_title('(c) thermal-branch speed',fontsize=9,loc='left')
fig.tight_layout(); save(fig,'fig_fractional_mdd')
print('check alpha=1 vs erfc:', th(1.0,1.0,1.0), float(mp.erfc(0.5)))
print('kappa(0)=',kappa(0.0),'(= (1/tau) int (1-u)^2 du = 1/3)')
