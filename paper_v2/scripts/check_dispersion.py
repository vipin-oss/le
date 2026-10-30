import sympy as sp
w,k,rho,cv,c1,T0,kc,ks,tq,tT,tv,beta=sp.symbols('w k rho cv c1 T0 kc ks tq tT tv beta')
U,Th,q=sp.symbols('U Theta q')
s=-sp.I*w; dx=sp.I*k; dt=s
mom=rho*dt**2*U-(rho*c1**2*dx**2*U-beta*dx*Th)
v=Th/dt
heat=q+tq*dt*q+kc*(dx*Th+tT*dt*dx*Th)+ks*(dx*v+tv*dt*dx*v)
qs=sp.solve(heat,q)[0]
en=rho*cv*dt*Th+beta*T0*dt*dx*U+dx*qs
M=sp.Matrix([[sp.diff(mom,U),sp.diff(mom,Th)],[sp.diff(en,U),sp.diff(en,Th)]])
G=(kc*(1+tT*s)+ks*(1+tv*s)/s)/(1+tq*s)
mine=(rho*c1**2*k**2-rho*w**2)*(s*rho*cv+G*k**2)+beta**2*T0*s*k**2
print('det - mine =',sp.simplify(M.det()-mine))
