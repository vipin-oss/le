import numpy as np
# high-frequency front speeds: LS: v^4 - v^2 (c1^2(1+eps)+cT^2) + c1^2 cT^2 = 0 ; GL: eps -> eps*tau1/tau0
eps=0.1; tau0=0.25; tau1=0.1; k=1.0
def roots_K(w,tau0,tauc,kind):
    s=-1j*w
    # (c1^2 K + s^2)(s(1+tau0 s)+kK)+ eps s K (1+tauc s)=0  (rho=c=c1=1)
    a=k; b=k*s**2+s*(1+tau0*s)+eps*s*(1+tauc*s); c=s**3*(1+tau0*s)
    d=np.sqrt(b*b-4*a*c); return [(-b+d)/(2*a),(-b-d)/(2*a)]
def speeds(w,tau0,tauc):
    K=roots_K(w,tau0,tauc,None); return sorted([w/np.sqrt(x).real if np.sqrt(x).real>0 else w/(-np.sqrt(x)).real for x in K])
cT2=k/tau0
for name,tauc in [('LS',tau0),('GL',tau1)]:
    e=eps*tauc/tau0
    pred=np.sqrt(np.roots([1,-((1+e)+cT2),cT2]).real)
    print(name,'numerical v at w=2e3:',np.round(speeds(2e3,tau0,tauc),4),' predicted fronts:',np.round(sorted(pred),4))
