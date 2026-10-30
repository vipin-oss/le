import numpy as np
from models import model, coupled_k2
# GN-II: speeds from  v^4 - v^2 (c1^2(1+eps)+cT^2) + c1^2 cT^2 = 0 ; compare with dispersion polynomial roots at some omega
eps=0.1; cT2=1/1.0   # k*=1 -> cT^2=k*/(rho c)=1
p=model('GN-II')
for w in [0.5,2.0,10.0]:
    K=np.array(coupled_k2(w,p,beta2T0=eps)); v=w/np.sqrt(K.astype(complex)).real
    print(w,sorted(np.round(v,6)))
a=1; b=-(1*(1+eps)+cT2); c=1*cT2
print('formula',sorted(np.sqrt(np.roots([a,b,c]))))
