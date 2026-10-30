import numpy as np, matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from models import model, coupled_k2
from fig_common import *
eps=0.1; tau=0.25   # thermal wave speed sqrt(kc/(rcv tau)) = 2 c1
w=np.logspace(-2,1.6,1500)
def track(p):
    kel=[];kth=[];prev=None
    for wi in w:
        K=np.array(coupled_k2(wi,p,beta2T0=eps))
        ks=np.sqrt(K.astype(complex)); ks=np.where(ks.imag<0,-ks,ks)
        if prev is None:
            ie=np.argmin(abs(ks)); order=[ks[ie],ks[1-ie]]
        else:
            d=abs(ks[0]-prev[0])+abs(ks[1]-prev[1]); d2=abs(ks[1]-prev[0])+abs(ks[0]-prev[1])
            order=[ks[0],ks[1]] if d<=d2 else [ks[1],ks[0]]
        prev=order; kel.append(order[0]); kth.append(order[1])
    return np.array(kel),np.array(kth)
fig,ax=plt.subplots(2,2,figsize=(7.2,5.2),sharex=True)
for name,col,ls in [('Fourier','CD','-'),('LS','LS','-'),('DPL','DPL','--')]:
    p=model(name,tau); kel,kth=track(p)
    lab={'Fourier':'classical (Biot)','LS':'Lord–Shulman','DPL':r'DPL ($\tau_T=\tau_q/2$)'}[name]
    ax[0,0].semilogx(w,w/kel.real,color=C[col],ls=ls,label=lab)
    ax[0,1].loglog(w,kel.imag,color=C[col],ls=ls,label=lab)
    ax[1,0].semilogx(w,w/kth.real,color=C[col],ls=ls,label=lab)
    ax[1,1].loglog(w,kth.imag,color=C[col],ls=ls,label=lab)
ax[0,0].set_ylabel(r'phase speed $v_p/c_1$'); ax[0,0].set_title('elastic-type branch',fontsize=9)
ax[0,1].set_ylabel(r'attenuation $\mathrm{Im}\,k\;c_1/\omega_*$'); ax[0,1].set_title('elastic-type branch',fontsize=9)
ax[1,0].set_ylabel(r'phase speed $v_p/c_1$'); ax[1,0].set_title('thermal-type branch',fontsize=9); ax[1,0].set_yscale('log')
ax[1,1].set_ylabel(r'attenuation $\mathrm{Im}\,k\;c_1/\omega_*$'); ax[1,1].set_title('thermal-type branch',fontsize=9)
for a in ax[1]: a.set_xlabel(r'frequency $\omega/\omega_*$,  $\omega_*=\rho c_v c_1^2/k$')
ax[0,0].axhline(1,color='k',lw=0.5,ls=':'); ax[1,0].axhline(2,color='k',lw=0.5,ls=':')
ax[1,0].legend(loc='upper left',frameon=False)
ax[0,0].axhline(np.sqrt(1+eps),color='k',lw=0.5,ls=':'); ax[0,0].text(0.012,np.sqrt(1+eps)+0.001,r'adiabatic $\sqrt{1+\varepsilon}$',fontsize=7); ax[0,0].text(0.012,1.001,'isothermal',fontsize=7)
for a,l in zip(ax.flat,'abcd'): a.text(-0.02,1.12,f'({l})',transform=a.transAxes,fontweight='bold')
fig.tight_layout(); save(fig,'fig_dispersion')
# print checks
p=model('LS',tau); kel,kth=track(p)
print('LS thermal speed at high w:', (w/kth.real)[-1], 'expected', np.sqrt(1/tau))
print('LS elastic speed high w:', (w/kel.real)[-1])
pc=model('Fourier',tau); kel,kth=track(pc); print('CD elastic speed low w',(w/kel.real)[0],'high',(w/kel.real)[-1], 'expected high c1*sqrt(1+eps)=',np.sqrt(1+eps))
