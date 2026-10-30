"""Normal-incidence interface between two thermoelastic half-spaces (1D, template heat law).
Left medium x<0 (index 1), right medium x>0 (index 2). Incident: elastic-type wave from the left.
Continuity at x=0: u, sigma, theta, q (perfect mechanical and thermal contact).
Energy flux (positive-definite quadratic energy):  P = < -sigma*udot + theta*q/T0 >,  time average = 1/2 Re[...*]"""
import numpy as np
T0=1.0
class Med:
    def __init__(s,rho,c1,cv,kc,beta,tq=0.0,tT=0.0,ks=0.0,tv=0.0):
        s.rho,s.c1,s.cv,s.kc,s.beta,s.tq,s.tT,s.ks,s.tv=rho,c1,cv,kc,beta,tq,tT,ks,tv
    def G(s,sv): return (s.kc*(1+s.tT*sv)+s.ks*(1+s.tv*sv)/sv)/(1+s.tq*sv)
    def roots(m,w):
        sv=-1j*w; g=m.G(sv)
        a=m.rho*m.c1**2*g; b=m.rho*m.c1**2*sv*m.rho*m.cv-m.rho*w**2*g+m.beta**2*T0*sv; c=-m.rho*w**2*sv*m.rho*m.cv
        d=np.sqrt(b*b-4*a*c); K=[(-b+d)/(2*a),(-b-d)/(2*a)]
        ks=[]
        for Kj in K:
            k=np.sqrt(Kj+0j); 
            if k.imag<0 or (abs(k.imag)<1e-14 and k.real<0): k=-k
            ks.append(k)
        # order: elastic-type first (closest to w/c1)
        ks.sort(key=lambda k: abs(k-w/m.c1)); return ks
    def mode(m,w,k):
        """fields per unit displacement amplitude for wave exp(i(kx-wt)) (k may be negative: left-going)"""
        sv=-1j*w
        th=-1j*(m.rho*w**2-m.rho*m.c1**2*k**2)/(m.beta*k)
        sig=m.rho*m.c1**2*1j*k-m.beta*th
        q=-m.G(sv)*1j*k*th
        return dict(u=1.0,sig=sig,th=th,q=q,ud=-1j*w)
def flux(f):
    return 0.5*np.real(-f['sig']*np.conj(f['ud'])+f['th']*np.conj(f['q'])/T0)
def combine(parts):
    return {k:sum(p[k] for p in parts) for k in parts[0]}
def solve(m1,m2,w):
    k1=m1.roots(w); k2=m2.roots(w)
    inc=m1.mode(w,k1[0])
    r_e=m1.mode(w,-k1[0]); r_t=m1.mode(w,-k1[1])
    t_e=m2.mode(w,k2[0]); t_t=m2.mode(w,k2[1])
    keys=['u','sig','th','q']
    A=np.array([[r_e[k],r_t[k],-t_e[k],-t_t[k]] for k in keys],dtype=complex)
    b=-np.array([inc[k] for k in keys],dtype=complex)
    x=np.linalg.solve(A,b)
    def sc(f,a): return {k:f[k]*a for k in f}
    R_e,R_t,T_e,T_t=sc(r_e,x[0]),sc(r_t,x[1]),sc(t_e,x[2]),sc(t_t,x[3])
    Pinc=flux(inc)
    res=dict(Pinc=Pinc,Re=-flux(R_e)/Pinc,Rt=-flux(R_t)/Pinc,Te=flux(T_e)/Pinc,Tt=flux(T_t)/Pinc)
    res['naive_sum']=res['Re']+res['Rt']+res['Te']+res['Tt']
    Lt=combine([inc,R_e,R_t]); Rt_=combine([T_e,T_t])
    res['total_left']=flux(Lt)/Pinc; res['total_right']=flux(Rt_)/Pinc
    res['cross']=1-res['naive_sum']
    res['amp']=x
    return res
if __name__=='__main__':
    m1=Med(1.0,1.0,1.0,1.0,np.sqrt(0.1),tq=0.25)
    m2=Med(2.0,1.2,0.8,0.6,np.sqrt(0.3),tq=0.15)
    for w in [0.1,0.5,1.0,2.0,5.0]:
        r=solve(m1,m2,w); print(w,{k:(round(float(v),5) if k!='amp' else '') for k,v in r.items() if k!='amp'})
