import numpy as np, mpmath as mp, matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from fig_common import *
from lamb_te import *
eps=0.05; h=20.0; H=2*h; chi=1.0
E=mu*2*(1+nu); Ep=E/(1-nu**2)
K=lam+2*mu/3; alpha=np.sqrt(eps)/(3*K)           # beta=(3 lam+2 mu) alpha = 3K alpha ; beta^2=eps (T0=1,c_v=1)
Delta_beam=E*alpha**2/1.0
Delta_plate=Delta_beam*(1+nu)/(1-nu)
print('Delta beam %.5f, plate-strain %.5f, eps*? %.5f'%(Delta_beam,Delta_plate,eps))
ks=np.logspace(-4.3,-0.8,46)
def trackA0(G,bc='ins'):
    out=[]; wprev=None
    for i,k in enumerate(ks):
        D=Ep*H**3/12; w0=np.sqrt(D*k**4/H) if wprev is None else wprev*(k/ks[i-1])**1.5
        g=mp.mpc(0,-w0)
        try:
            s=mp.findroot(lambda s: det6(s,k,h,eps,G,bc),(g*1.001,g*0.999),solver='secant',tol=1e-20,maxsteps=120)
        except Exception as e:
            out.append(np.nan); continue
        w=complex(1j*s); out.append(w); wprev=abs(w.real)
    return np.array(out)
w=trackA0(1)
Q=2*np.abs(w.imag)/w.real
x=w.real/(np.pi**2*chi/H**2)
xi=np.sqrt(np.pi**2*x/2)
LR=Delta_plate*(6/xi**2-6/xi**3*(np.sinh(xi)+np.sin(xi))/(np.cosh(xi)+np.cos(xi)))
np.save('lamb_te_out.npy',np.array([ks,w.real,w.imag,Q,x,LR]))
for i in range(0,len(ks),5): print('kh=%.3g x=%.3g Q=%.4g LR(plate)=%.4g ratio=%.3f'%(ks[i]*h,x[i],Q[i],LR[i],Q[i]/LR[i]))
i=np.nanargmax(Q); print('peak Q=%.4g at x=%.3g kh=%.3g ; LR peak %.4g'%(Q[i],x[i],ks[i]*h,np.nanmax(LR)))
fig,ax=plt.subplots(1,2,figsize=(7.2,2.9))
ax[0].loglog(x,Q,color=C['LS'],label='plane-strain plate (6x6 determinant)'); ax[0].loglog(x,LR,color=C['DPL'],ls='--',label='Lifshitz--Roukes, plate $\\Delta$')
ax[0].set_xlabel(r'$\omega/\omega_Z$'); ax[0].set_ylabel(r'$Q^{-1}$'); ax[0].legend(frameon=False,fontsize=6.5); ax[0].set_title('(a) A0 mode loss',fontsize=9,loc='left')
ax[1].semilogx(ks*h,Q/LR,color=C['GN']); ax[1].axhline(1,color='k',lw=0.5); ax[1].set_xlabel(r'$k h$ (half thickness)'); ax[1].set_ylabel(r'$Q^{-1}_{\rm exact}/Q^{-1}_{\rm LR}$'); ax[1].set_title('(b) ratio',fontsize=9,loc='left')
fig.tight_layout(); save(fig,'fig_lamb_te')
