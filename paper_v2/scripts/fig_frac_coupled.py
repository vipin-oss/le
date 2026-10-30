import numpy as np, matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from fig_common import *
eps=0.1; tau=0.25
def Gfun(s,alpha):  # Caputo-type fractional Cattaneo: q + tau^a D^a q = -k grad T
    return 1/(1+(tau**alpha)*(s**alpha)) if alpha>0 else 1.0
def roots(w,alpha):
    s=-1j*w; sa=(w**alpha)*np.exp(-1j*np.pi*alpha/2)
    g=1/(1+tau**alpha*sa) if alpha>0 else 1.0
    a=g; b=s-w**2*g+eps*s; c=-w**2*s
    d=np.sqrt(b*b-4*a*c); return (-b+d)/(2*a),(-b-d)/(2*a)
def track(alpha,w):
    out=[]; prev=None
    for x in w:
        ks=[np.sqrt(K) for K in roots(x,alpha)]; ks=[k if k.imag>=0 else -k for k in ks]
        if prev is None: k=min(ks,key=lambda z:abs(z.real-x/np.sqrt(1+eps)))
        else: k=min(ks,key=lambda z:abs(z-prev))
        out.append(k); prev=k
    return np.array(out)
w=np.logspace(-3,2,1500)
fig,ax=plt.subplots(1,2,figsize=(7.2,2.9))
sty={1.0:('LS ($\\alpha=1$)',C['LS'],'-'),0.8:('$\\alpha=0.8$',C['DPL'],'--'),0.6:('$\\alpha=0.6$',C['GN'],'-.'),0.0:('classical',C['CD'],':')}
res={}
for al,(lab,col,ls) in sty.items():
    k=track(al,w); res[al]=k
    ax[0].semilogx(w,w/k.real,color=col,ls=ls,label=lab)
    ax[1].loglog(w,2*k.imag/k.real,color=col,ls=ls,label=lab)
ax[0].set_xlabel(r'$\omega/\omega^*$'); ax[0].set_ylabel(r'$v_p/c_1$'); ax[0].legend(frameon=False,fontsize=7); ax[0].set_title('(a) phase speed',fontsize=9,loc='left')
ax[1].set_xlabel(r'$\omega/\omega^*$'); ax[1].set_ylabel(r'$Q^{-1}=2\,\mathrm{Im}k/\mathrm{Re}k$'); ax[1].set_ylim(1e-6,1); ax[1].set_title('(b) loss',fontsize=9,loc='left')
fig.tight_layout(); save(fig,'fig_frac_coupled')
for al in res:
    k=res[al]; i=np.argmax(2*k.imag/k.real); 
    print(al,'peak Q^-1=%.4f at w=%.3f'%((2*k.imag/k.real)[i],w[i]),' v(w=100)=%.3f'%(w[-1]/k[-1].real),' v(1e-3)=%.4f'%(w[0]/k[0].real))
print('Debye peak eps/2=',eps/2,' adiabatic speed',np.sqrt(1+eps))
