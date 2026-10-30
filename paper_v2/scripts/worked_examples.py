"""Worked numbers for the examples chapter (rounded handbook values, same as table_materials.py)."""
import numpy as np
T0=300.
M={'Aluminium':(2700,900,237,23e-6,70,0.33),'Copper':(8960,385,400,17e-6,120,0.34),'Silicon':(2330,700,150,2.6e-6,160,0.22),'Steel':(7850,490,50,12e-6,200,0.29)}
def props(n):
    rho,c,k,al,E,nu=M[n]; E*=1e9; lam=E*nu/((1+nu)*(1-2*nu)); mu=E/(2*(1+nu)); L=lam+2*mu
    c1=np.sqrt(L/rho); beta=(3*lam+2*mu)*al; eps=beta**2*T0/(rho**2*c*c1**2); ws=rho*c*c1**2/k
    return dict(rho=rho,c=c,k=k,al=al,E=E,nu=nu,c1=c1,beta=beta,eps=eps,ws=ws,chi=k/(rho*c),mu=mu,lam=lam)
print('--- Example 1: aluminium, longitudinal wave, tau_q = 1 ps')
p=props('Aluminium'); tau=1e-12
print('c1=%.0f m/s eps=%.4f omega*=%.3e rad/s f*=%.3e Hz'%(p['c1'],p['eps'],p['ws'],p['ws']/2/np.pi))
print('tau*omega*=%.3f ; c_T=sqrt(k/(rho c tau))=%.0f m/s ; c_T/c1=%.2f'%(tau*p['ws'],np.sqrt(p['chi']/tau),np.sqrt(p['chi']/tau)/p['c1']))
f=1e6; w=2*np.pi*f; x=w/p['ws']; print('at 1 MHz: x=w/w*=%.3e, Debye Q^-1=eps*x/(1+x^2)=%.3e'%(x,p['eps']*x/(1+x**2)))
f=1e9; w=2*np.pi*f; x=w/p['ws']; print('at 1 GHz: x=%.3e, Q^-1=%.3e ; omega*tau=%.3e'%(x,p['eps']*x/(1+x**2),w*tau))
print('thermal diffusion length at 1 GHz: sqrt(2chi/w)=%.2e m ; wavelength=%.2e m'%(np.sqrt(2*p['chi']/w),p['c1']/f))
print('--- Example 2: silicon beam, thickness 200 nm, flexure Zener peak')
p=props('Silicon'); h=200e-9; chi=p['chi']; fZ=np.pi**2*chi/h**2/2/np.pi
al=p['al']; cv=p['rho']*p['c']; Delta=p['E']*al**2*T0/cv
print('chi=%.2e m2/s fZ=%.3e Hz Delta=E al^2 T0/cv=%.3e peak Q^-1=Delta/2*0.988=%.3e'%(chi,fZ,Delta,Delta/2*0.988))
for h in [20e-9,100e-9,1e-6,10e-6]:
    print('  h=%.0e m  fZ=%.2e Hz'%(h,np.pi*chi/h**2/2))
print('--- Example 3: interface Al|Cu welded normal incidence (elastic)')
a=props('Aluminium'); b=props('Copper'); Z1=a['rho']*a['c1']; Z2=b['rho']*b['c1']
r=(Z1-Z2)/(Z1+Z2); t=2*Z1/(Z1+Z2); print('Z1=%.3e Z2=%.3e r=%.4f t=%.4f R=%.4f T=%.4f R+T=%.4f'%(Z1,Z2,r,t,r*r,Z2/Z1*t*t,r*r+Z2/Z1*t*t))
print('--- Example 4: thermal shock half-space steel, Fourier vs LS, front location after 1 ns? c_T for tau=1 ps')
s=props('Steel'); print('chi=%.2e ; diffusion length after 1 us: %.2e m; after 1 ns: %.2e m'%(s['chi'],np.sqrt(s['chi']*1e-6),np.sqrt(s['chi']*1e-9)))
print('LS front speed (tau=1ps) %.0f m/s -> travels in 1 ps: %.2e m'%(np.sqrt(s['chi']/1e-12),np.sqrt(s['chi']/1e-12)*1e-12))
