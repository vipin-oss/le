import numpy as np, matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from models import model, coupled_k2
from fig_common import *
def elastic_k(w,p,eps):
    K=np.array(coupled_k2(w,p,beta2T0=eps)); k=np.sqrt(K.astype(complex)); k=np.where(k.imag<0,-k,k)
    return k[np.argmin(abs(k-w))]   # branch closest to w/c1
w=np.logspace(-2,2,400)
fig,ax=plt.subplots(1,2,figsize=(7.2,2.8))
for eps,ls in [(0.02,'-'),(0.1,'--')]:
    k=np.array([elastic_k(x,model('Fourier'),eps) for x in w])
    Q=2*k.imag/k.real
    ax[0].semilogx(w,Q/eps,ls=ls,color=C['CD'],label=rf'$\varepsilon={eps}$')
ax[0].semilogx(w,w/(1+w**2),color=C['accent'],ls=':',label=r'$\omega/\omega_*\,/\,(1+\omega^2/\omega_*^2)$ (Debye)')
ax[0].set_xlabel(r'$\omega/\omega_*$'); ax[0].set_ylabel(r'$Q^{-1}/\varepsilon$'); ax[0].legend(frameon=False,fontsize=7); ax[0].set_title('(a) classical thermoelastic damping',fontsize=9,loc='left')
eps=0.1; tau=0.25
for name,col,ls,lab in [('Fourier','CD','-','classical'),('LS','LS','-','Lord–Shulman'),('DPL','DPL','--','DPL')]:
    k=np.array([elastic_k(x,model(name,tau),eps) for x in w]); Q=2*k.imag/k.real
    ax[1].loglog(w,Q,color=C[col],ls=ls,label=lab)
ax[1].set_xlabel(r'$\omega/\omega_*$'); ax[1].set_ylabel(r'$Q^{-1}$'); ax[1].legend(frameon=False,fontsize=7); ax[1].set_title(r'(b) effect of the heat law, $\varepsilon=0.1$',fontsize=9,loc='left')
fig.tight_layout(); save(fig,'fig_zener')
# check: weak-coupling Debye prediction Q^-1 = eps x/(1+x^2)
k=elastic_k(1.0,model('Fourier'),0.001); print('Q^-1/eps at omega*:',2*k.imag/k.real/0.001,'(Debye 0.5)')
