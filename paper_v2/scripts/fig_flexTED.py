import numpy as np, matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from fig_common import *
# Zener vs Lifshitz-Roukes (exact, Fourier heat, 1D thermal profile across thickness h)
x=np.logspace(-2,2,600)  # x = omega/omega_Z, omega_Z = pi^2 chi/h^2
xi=lambda w: np.sqrt(w*pi2)  # placeholder
pi2=np.pi**2
# define xi = h sqrt(omega/(2 chi)); omega/omega_Z = omega h^2/(pi^2 chi)  => xi^2 = pi^2 x/2
xi=np.sqrt(np.pi**2*x/2)
LR=6/xi**2-6/xi**3*(np.sinh(xi)+np.sin(xi))/(np.cosh(xi)+np.cos(xi))
Z=x/(1+x**2)
fig,ax=plt.subplots(1,2,figsize=(7.2,2.9))
ax[0].loglog(x,LR,color=C['LS'],label='Lifshitz--Roukes'); ax[0].loglog(x,Z,color=C['DPL'],ls='--',label='Zener (single relaxation)')
ax[0].set_xlabel(r'$\omega/\omega_Z$'); ax[0].set_ylabel(r'$Q^{-1}/\Delta$'); ax[0].set_ylim(1e-3,1); ax[0].legend(frameon=False,fontsize=7); ax[0].set_title('(a) normalised loss',fontsize=9,loc='left')
ax[1].semilogx(x,(Z-LR)/LR,color=C['GN']); ax[1].axhline(0,color='k',lw=0.5); ax[1].set_xlabel(r'$\omega/\omega_Z$'); ax[1].set_ylabel('relative error of Zener'); ax[1].set_title('(b) Zener error',fontsize=9,loc='left'); ax[1].set_ylim(-0.6,0.6)
fig.tight_layout(); save(fig,'fig_flexTED')
i=np.argmax(LR); print('LR peak %.4f at x=%.3f ; Zener peak 0.5 at 1'%(LR[i],x[i]))
for xv in [0.01,0.1,1,10,100]:
    j=np.argmin(abs(x-xv)); print(xv,'LR %.4g Z %.4g rel %.3f'%(LR[j],Z[j],(Z[j]-LR[j])/LR[j]))
