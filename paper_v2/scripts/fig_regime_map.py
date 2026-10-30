import numpy as np, matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from models import model, coupled_k2
from fig_common import *
eps=0.02
def elastic_k(w,p):
    K=np.array(coupled_k2(w,p,beta2T0=eps)); k=np.sqrt(K.astype(complex)); k=np.where(k.imag<0,-k,k)
    return k[np.argmin(abs(k-w))]
ws=np.logspace(-2,1,60); taus=np.logspace(-3,1,60)
dQ=np.zeros((len(taus),len(ws))); dv=np.zeros_like(dQ)
for i,t in enumerate(taus):
    pls=model('LS',t); pc=model('Fourier')
    for j,w in enumerate(ws):
        kl=elastic_k(w,pls); kc=elastic_k(w,pc)
        dQ[i,j]=abs((kl.imag/kl.real)/(kc.imag/kc.real)-1); dv[i,j]=abs((w/kl.real)/(w/kc.real)-1)
fig,ax=plt.subplots(1,2,figsize=(7.2,3.0))
for a,Z,tit in [(ax[0],dQ,r'(a) relative change of $Q^{-1}$'),(ax[1],dv,r'(b) relative change of phase speed')]:
    cs=a.contourf(ws,taus,np.log10(np.maximum(Z,1e-6)),levels=np.arange(-5,1.01,1),cmap='viridis',extend='both')
    a.contour(ws,taus,Z,levels=[0.01,0.1],colors=['w','w'],linestyles=['--','-'],linewidths=0.9)
    a.set_xscale('log'); a.set_yscale('log'); a.set_xlabel(r'$\omega/\omega_*$'); a.set_title(tit,fontsize=9,loc='left')
ax[0].set_ylabel(r'lag time $\tau_0\omega_*$')
cb=fig.colorbar(cs,ax=ax,shrink=0.9,pad=0.02); cb.set_label(r'$\log_{10}$(relative difference, LS vs classical)')
# diagonal: omega*tau = 1
for a in ax: a.plot(ws,1/(ws*1.0)*1.0/ (1.0) ,color='r',lw=0.8,ls=':') 
for a in ax: a.set_ylim(taus[0],taus[-1])
fig.savefig('../figs/fig_regime_map.pdf',bbox_inches='tight'); fig.savefig('../figs/fig_regime_map.png',bbox_inches='tight',dpi=300)
# report where 10% difference first occurs on the omega*tau=1 line
for w in [0.1,1,10]:
    t=1.0/w
    pls=model('LS',t); pc=model('Fourier'); kl=elastic_k(w,pls); kc=elastic_k(w,pc)
    print('omega/omega*=',w,'omega*tau=1: dQ=',abs((kl.imag/kl.real)/(kc.imag/kc.real)-1),'dv=',abs(kl.real/kc.real-1)) 
