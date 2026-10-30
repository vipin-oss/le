import numpy as np, matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from models import model, G
from fig_common import *
def roots(w,p,eps,xi,form):
    s=-1j*w; g=G(s,p); a1=1+xi**2*s**2; a0=s**2; h=s; b=eps*s
    A=a1*g; B=a1*h+a0*g+b; Cc=a0*h
    if form=='B': A=A+b*xi**2
    d=np.sqrt(B*B-4*A*Cc+0j); return [(-B+d)/(2*A),(-B-d)/(2*A)]
def kroots(w,p,eps,xi,form):
    K=roots(w,p,eps,xi,form); k=[np.sqrt(x+0j) for x in K]; return [x if x.imag>=0 else -x for x in k]
def elastic(w,p,eps,xi,form,prev=None):
    k=kroots(w,p,eps,xi,form)
    if prev is None: return min(k,key=lambda x:abs(x))
    return min(k,key=lambda x:abs(x-prev))
def track(ws,p,eps,xi,form):
    out=[]; prev=None
    for x in ws:
        prev=elastic(x,p,eps,xi,form,prev); out.append(prev)
    return np.array(out)
eps=0.1; xi=0.3; wc=1/xi
w=np.linspace(0.02,0.95*wc,500)
fig,ax=plt.subplots(1,2,figsize=(7.2,2.8))
for lab,xi_,form,col,ls in [('local',0.0,'A','#444444','-'),('nonlocal, form A',xi,'A','#0072B2','-'),('nonlocal, form B',xi,'B','#D55E00','--')]:
    k=track(w,model('Fourier'),eps,xi_,form)
    ax[0].plot(w,w/k.real,color=col,ls=ls,label=lab)
    ax[1].semilogy(w,2*k.imag/k.real,color=col,ls=ls,label=lab)
ax[0].set_xlabel(r'$\omega/\omega_*$'); ax[0].set_ylabel(r'$v_p/c_1$'); ax[0].legend(frameon=False,fontsize=7); ax[0].set_title('(a) elastic-type branch',fontsize=9,loc='left')
ax[1].set_xlabel(r'$\omega/\omega_*$'); ax[1].set_ylabel(r'$Q^{-1}$'); ax[1].set_title(r'(b) damping, $\xi=0.3c_1/\omega_*$',fontsize=9,loc='left')
fig.tight_layout(); save(fig,'fig_nonlocal_te')
# checks: xi->0 recovers local; eps->0 recovers nonlocal elastic
k0=elastic(1.0,model('Fourier'),eps,0.0,'A'); k1=elastic(1.0,model('Fourier'),eps,1e-9,'B'); print('xi->0:',k0,k1)
ke=track(np.linspace(0.02,1.5,300),model('Fourier'),1e-9,xi,'A')[-1]; print('eps->0 k=',ke,' nonlocal elastic k=',1.5/np.sqrt(1-(xi*1.5)**2)) 
