"""Symbolic check: 1D thermopiezoelectric field equations (quasi-electrostatic, no free charge)
reduce to the thermoelastic dispersion polynomial with renormalised constants
   c~ = c + e^2/eps_e,  beta~ = beta - e p/eps_e,  rho c~_v = rho c_E - T0 p^2/eps_e."""
import sympy as sp
w,k,rho,cE,c,e,eps_e,p,beta,T0,kc=sp.symbols('w k rho cE c e epsE p beta T0 kc')
s=-sp.I*w; dx=sp.I*k
U,Th,Phi=sp.symbols('U Theta Phi')
E=-dx*Phi
sigma=c*dx*U-e*E-beta*Th
D=e*dx*U+eps_e*E+p*Th
eta_rho=beta*dx*U+p*E+rho*cE*Th/T0          # rho*eta
mom=rho*s**2*U-dx*sigma
gauss=dx*D
energy=T0*s*eta_rho+kc*dx*dx*Th*(-1)*(-1)*(-1)   # rho T0 eta_dot = -q_x = k theta_xx -> T0 s eta - k (ik)^2 Th ... see below
energy=T0*s*eta_rho-kc*dx**2*Th
M=sp.Matrix([[sp.diff(mom,U),sp.diff(mom,Th),sp.diff(mom,Phi)],
             [sp.diff(gauss,U),sp.diff(gauss,Th),sp.diff(gauss,Phi)],
             [sp.diff(energy,U),sp.diff(energy,Th),sp.diff(energy,Phi)]])
det=sp.simplify(M.det())
# renormalised thermoelastic polynomial  (rho c1~^2 K + rho s^2)(s rho c~ + kc K) + beta~^2 T0 s K   (times T0 factor from energy scaling)
ct=c+e**2/eps_e; bt=beta-e*p/eps_e; rct=rho*cE-T0*p**2/eps_e
K=k**2
ren=(ct*K+rho*s**2)*(s*rct+kc*K)*T0+bt**2*T0*s*K*T0   # energy eq scaled by T0
ratio=sp.simplify(det/ren)
print('det/renormalised polynomial =',ratio)
