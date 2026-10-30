"""Sum rule  int Q^-1 dln(omega) = pi (v_0 - v_inf)/v_mean  for the classical coupled longitudinal wave (weak coupling)."""
import numpy as np
from models import *
p=model('Fourier')
for eps in [0.01,0.001]:
    w=np.logspace(-6,6,40001); Q=[]; V=[]; prev=None
    for x in w:
        K=coupled_k2(x,p,1,1,1,eps)
        ks=[np.sqrt(kk+0j) for kk in K]; ks=[k if k.imag>=0 else -k for k in ks]
        tgt=x/np.sqrt(1+eps) if prev is None else prev*(x/x_prev)
        k=min(ks,key=lambda z:abs(z-tgt)); prev=k; x_prev=x
        Q.append(2*k.imag/k.real); V.append(x/k.real)
    Q=np.array(Q); V=np.array(V)
    I=np.trapezoid(Q,np.log(w)); vm=0.5*(V[0]+V[-1]); R=np.pi*(V[0]-V[-1])/vm
    print(eps,'LHS %.6e RHS %.6e ratio %.5f'%(I,R,I/R))
