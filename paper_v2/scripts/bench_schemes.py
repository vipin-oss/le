"""Finite-difference benchmark for the Cattaneo (telegraph) heat pulse, uncoupled. Units: rho c=1, k=1, tau=1 -> c_T=1, ell=c_T tau=1.
System: th_t + q_x = 0 ; q_t + th_x/tau = -q/tau ; boundary q(0,t)=1 (step), initial zero.
Exact: Laplace th^ = (1+tau s)/(s m) exp(-x m), m=sqrt(s(1+tau s)); zero ahead of x=t."""
import numpy as np, mpmath as mp
mp.mp.dps=20
tau=1.0
def exact(x,t):
    if x>=t: return 0.0
    f=lambda s:(1+tau*s)/(s*mp.sqrt(s*(1+tau*s)))*mp.e**(-x*mp.sqrt(s*(1+tau*s)))
    return float(mp.invertlaplace(f,t,method='dehoog'))
def run(N,scheme,T=5.0,L=10.0,cfl=0.9):
    dx=L/N; x=(np.arange(N)+0.5)*dx; c=1/np.sqrt(tau); dt=cfl*dx/c; n=int(round(T/dt)); dt=T/n
    th=np.zeros(N); q=np.zeros(N)
    A=np.array([[0,1],[1/tau,0]])   # u=(th,q): u_t + A u_x = S
    lam,V=np.linalg.eig(A); Vi=np.linalg.inv(V)
    for _ in range(n):
        # source half step (exact: q decays)
        q*=np.exp(-0.5*dt/tau)
        u=np.vstack([th,q]); 
        # ghost cells: left q=1 (th zero-gradient), right zero-gradient
        ug=np.hstack([np.array([[th[0]],[2*1.0-q[0]]]),u,u[:,-1:]])
        if scheme=='upwind':
            w=Vi@ug; wn=w.copy()
            for p in range(2):
                if lam[p]>0: wn[p,1:-1]=w[p,1:-1]-lam[p]*dt/dx*(w[p,1:-1]-w[p,:-2])
                else:        wn[p,1:-1]=w[p,1:-1]-lam[p]*dt/dx*(w[p,2:]-w[p,1:-1])
            un=V@wn[:,1:-1]
        elif scheme=='LW':
            a=dt/dx; Ai=A
            f=Ai@ug
            un=ug[:,1:-1]-0.5*a*(f[:,2:]-f[:,:-2])+0.5*a*a*(Ai@(Ai@(ug[:,2:]-2*ug[:,1:-1]+ug[:,:-2])))
        elif scheme=='LF':
            a=dt/dx; f=A@ug
            un=0.5*(ug[:,2:]+ug[:,:-2])-0.5*a*(f[:,2:]-f[:,:-2])
        th,q=un[0],un[1]
        q*=np.exp(-0.5*dt/tau)
    return x,th
if __name__=='__main__':
    xs=np.linspace(0.05,4.95,200); ex=np.array([exact(xx,5.0) for xx in xs])
    print('exact theta at x=1,3,4.9:',ex[[19,59,97]],' front jump (1/cT... ) exp(-x/2l)*1:',np.exp(-4.9/2))
    for sch in ['LF','upwind','LW']:
        errs=[];Ns=[100,200,400,800,1600]
        for N in Ns:
            x,th=run(N,sch); thi=np.interp(xs,x,th); errs.append(np.mean(abs(thi-ex))*(xs[-1]-xs[0]))
        order=[np.log2(errs[i]/errs[i+1]) for i in range(len(errs)-1)]
        print(sch,'L1 errors:',['%.2e'%e for e in errs],' observed orders:',['%.2f'%o for o in order])
