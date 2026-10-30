"""Thermoelastic Lamb (plate) problem, plane strain, plate -h<y<h, traction-free, insulated or isothermal faces.
Same nondimensionalisation as fig_rayleigh.py (rho=1, lambda+2mu=1, c_v=1, k_cond=1, T0=1, beta^2=eps).
Each of the three modes (two dilatational-thermal, one shear) contributes exp(+-m y); 6x6 determinant."""
import numpy as np, mpmath as mp
mp.mp.dps=30
nu=0.3; cs2=(1-2*nu)/(2-2*nu); mu=cs2; lam=1-2*mu
def modes(s,eps,G):
    a=G; b=-(G*s**2+s+eps*s); c=s**3
    d=mp.sqrt(b*b-4*a*c); return [(-b+d)/(2*a),(-b-d)/(2*a)]
def det6(s,k,h,eps,G=1,bc='ins'):
    beta=mp.sqrt(eps); I=mp.mpc(0,1)
    kap=modes(s,eps,G); th=[(kk-s**2)/beta for kk in kap]
    ms=[mp.sqrt(kk+k**2) for kk in kap]; msh=mp.sqrt(s**2/cs2+k**2)
    cols=[]
    for sgn in (+1,-1):                       # exp(-sgn*m*y): sgn=+1 decaying with y
        for j in range(2):
            m=sgn*ms[j]
            col=lambda y,m=m,j=j:[ (lam*kap[j]+2*mu*m**2-beta*th[j])*mp.e**(-m*y),
                                   (-2*mu*I*k*m)*mp.e**(-m*y),
                                   ((-m*th[j]) if bc=='ins' else th[j])*mp.e**(-m*y)]
            cols.append(col)
        m=sgn*msh
        cols.append(lambda y,m=m:[ (2*mu*I*k*m)*mp.e**(-m*y), (mu*(m**2+k**2))*mp.e**(-m*y), 0*y])
    M=mp.matrix(6,6)
    for c,col in enumerate(cols):
        top=col(h); bot=col(-h)
        for r in range(3): M[r,c]=top[r]; M[r+3,c]=bot[r]
    return mp.det(M)
def solve_s(k,h,eps,guess,G=1,bc='ins'):
    f=lambda s: det6(s,k,h,eps,G,bc)
    return mp.findroot(f,guess,solver='muller',tol=1e-20,maxsteps=100)
if __name__=='__main__':
    # sanity: nearly elastic (eps tiny) -> compare A0 with thin-plate and exact Rayleigh-Lamb at kh=0.3, h=1
    eps=1e-8; h=1.0; k=0.3
    # elastic plane-strain Lamb antisymmetric exact: use thin-plate guess
    Ep=(lam+2*mu)*(1-2*nu*nu/(1-nu)/1)  # placeholder
    E=mu*2*(1+nu); Ep=E/(1-nu**2); D=Ep*(2*h)**3/12; w=np.sqrt(D*k**4/(2*h))
    s=solve_s(k,h,eps,mp.mpc(0.0,-w),1,'ins'); print('thin-plate w',w,' root w=i s:',complex(1j*s))
