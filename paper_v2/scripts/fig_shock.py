"""Thermal shock of a thermoelastic half-space (1D, coupled), Laplace domain + Talbot inversion.
Nondimensional: rho=c=c1=1 (i.e. lengths in c1/omega*, times in 1/omega*, k_cond=1), beta^2 T0 = eps.
BC at x=0: theta = theta0 H(t) (theta0 = 1), traction-free sigma=0.  x>0 half-space.
Fields ~ exp(-m x):  K=-m^2 roots of  (K + s^2)(s + G K) + eps s K = 0   (rho=c=c1=1)
   U = beta m Theta /(s^2 - m^2),  sigma = -m U - beta Theta  (units rho c1^2 = 1).
"""
import numpy as np, mpmath as mp, matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from fig_common import *
mp.mp.dps=25
eps=0.1; beta=mp.sqrt(eps)   # beta^2 T0 = eps with T0 absorbed: use beta=sqrt(eps), T0=1
def G_of(s,model,tq,tT):
    if model=='CD': return mp.mpf(1)
    if model=='LS': return 1/(1+tq*s)
    if model=='DPL': return (1+tT*s)/(1+tq*s)
def fields(s,x,model,tq,tT):
    G=G_of(s,model,tq,tT)
    # (K+s^2)(s+G K)+eps s K=0 -> G K^2 + (s + G s^2 + eps s) K + s^3 = 0
    a=G; b=s+G*s**2+eps*s; c=s**3
    d=mp.sqrt(b*b-4*a*c); K1=(-b+d)/(2*a); K2=(-b-d)/(2*a)
    ms=[]
    for K in (K1,K2):
        m=mp.sqrt(-K)
        if mp.re(m)<0: m=-m
        ms.append(m)
    m1,m2=ms
    # Theta_j amplitudes A1,A2: sum A=1/s ; sum A*s^2/(s^2-m^2)=0
    w1=s**2/(s**2-m1**2); w2=s**2/(s**2-m2**2)
    A1=(1/s)*(-w2)/(w1-w2); A2=(1/s)-A1
    Th=A1*mp.exp(-m1*x)+A2*mp.exp(-m2*x)
    U=sum(beta*m*A*mp.exp(-m*x)/(s**2-m**2) for m,A in ((m1,A1),(m2,A2)))
    sig=sum((-m*beta*m/(s**2-m**2)-beta)*A*mp.exp(-m*x) for m,A in ((m1,A1),(m2,A2)))
    return Th,sig
def invert(fun,t):
    return float(mp.re(mp.invertlaplace(fun,t,method='talbot')))
def history(model,tq,tT,x,ts):
    Th=[];Sg=[]
    for t in ts:
        Th.append(invert(lambda s: fields(s,x,model,tq,tT)[0],t))
        Sg.append(invert(lambda s: fields(s,x,model,tq,tT)[1],t))
    return np.array(Th),np.array(Sg)
if __name__=='__main__':
    # sanity: surface temperature step and traction free: sigma(0,s)=0 by construction. Check theta(0,t)=1.
    s=mp.mpc(2,1); Th0,sg0=fields(s,0,'LS',0.25,0)
    print('BC check theta(0,s)*s =',complex(Th0*s),' sigma(0,s)=',complex(sg0))
    x=2.0; ts=np.linspace(0.04,12,260)
    fig,ax=plt.subplots(1,2,figsize=(7.2,2.9))
    for model,col,ls,lab,tq,tT in [('CD','CD','-','classical',0,0),('LS','LS','-','Lord–Shulman',0.25,0),('DPL','DPL','--','DPL',0.25,0.125)]:
        Th,Sg=history(model,tq,tT,x,ts)
        ax[0].plot(ts,Th,color=C[col],ls=ls,label=lab); ax[1].plot(ts,Sg,color=C[col],ls=ls,label=lab)
        print(model,'theta max',Th.max(),'sigma min',Sg.min())
    ax[0].axvline(x/1.0,color='k',ls=':',lw=0.7); ax[1].axvline(x/1.0,color='k',ls=':',lw=0.7)
    ax[0].set_xlabel(r'$\omega_* t$'); ax[0].set_ylabel(r'$\theta/\theta_0$'); ax[0].set_title(r'(a) temperature at $x=2c_1/\omega_*$',fontsize=9,loc='left'); ax[0].legend(frameon=False,fontsize=7)
    ax[1].set_xlabel(r'$\omega_* t$'); ax[1].set_ylabel(r'$\sigma/(\rho c_1^2)$'); ax[1].set_title('(b) stress at the same point',fontsize=9,loc='left')
    fig.tight_layout(); save(fig,'fig_shock')
