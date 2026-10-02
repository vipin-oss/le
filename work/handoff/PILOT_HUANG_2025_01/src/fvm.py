"""Independent time-domain first-order source PDE implementation.
Does not use the published Laplace response or its root amplitudes.
"""
import numpy as np,time
from .physics import PARAMS,TIME,transport
from .common import INPUT

def minmod3(a,b,c):
 same=(np.sign(a)==np.sign(b))&(np.sign(b)==np.sign(c))
 return np.where(same,np.sign(a)*np.minimum(np.minimum(np.abs(a),np.abs(b)),np.abs(c)),0.)

def solve(model,nx,stage=None):
 L=float(INPUT['numerics']['domain_length_FVM']);dx=L/nx;x=(np.arange(nx)+.5)*dx
 A,speeds,R,invR,taus,weights=transport(model);n=len(speeds)
 pos=speeds>1e-10;neg=speeds<-1e-10;stay=~pos
 if np.count_nonzero(pos)!=2 or np.count_nonzero(neg)!=2:raise RuntimeError('Expected two incoming characteristics per physical boundary')
 B=np.zeros((2,n));B[0,2]=1;B[1,0]=PARAMS['beta2'];B[1,2]=-PARAMS['b'];BR=B@R
 BCinv=np.linalg.inv(BR[:,pos]);target=np.array([1.,0.])
 U=np.zeros((n,nx));dt0=float(INPUT['numerics']['FVM_CFL'])*dx/np.max(np.abs(speeds));steps=int(np.ceil(TIME/dt0));dt=TIME/steps
 relax=np.exp(-.5*dt/taus);lam=speeds[:,None]

 def rhs(Z):
  # Monotonized-central limiter in characteristics, not temperature clipping.
  slope=np.zeros_like(Z)
  dl=Z[:,1:-1]-Z[:,:-2];dr=Z[:,2:]-Z[:,1:-1]
  slope[:,1:-1]=minmod3(2*dl,.5*(dl+dr),2*dr)
  # Outgoing trace extrapolated from interior; solve only incoming boundary modes.
  zl=Z[:,0]-.5*slope[:,0];zin=BCinv@(target-BR[:,stay]@zl[stay]);zl=zl.copy();zl[pos]=zin
  zr=Z[:,-1]+.5*slope[:,-1];zr=zr.copy();zr[neg]=0.
  left=Z[:,:-1]+.5*slope[:,:-1];right=Z[:,1:]-.5*slope[:,1:]
  mid=np.where(lam>=0,left,right)
  flux=np.empty((n,nx+1));flux[:,1:-1]=lam*mid;flux[:,0]=speeds*zl;flux[:,-1]=speeds*zr
  return -(flux[:,1:]-flux[:,:-1])/dx

 start=time.perf_counter()
 for k in range(steps):
  U[3:]*=relax[:,None]
  Z=invR@U;Z1=Z+dt*rhs(Z);Z2=.5*Z+.5*(Z1+dt*rhs(Z1));U=R@Z2
  U[3:]*=relax[:,None]
  if stage and k%100==0:stage.check()
 e=U[0];v=U[1];theta=U[2];sigma=PARAMS['beta2']*e-PARAMS['b']*theta
 # Cell-centred strain integral from the untouched right side; u(L,t)=0 by causal truncation.
 u=-dx*(np.cumsum(e[::-1])[::-1]-.5*e)
 # Explicit boundary traces for verification (do not confuse cell centre with x=0).
 Z=invR@U;zl=Z[:,0].copy();zl[pos]=BCinv@(target-BR[:,stay]@zl[stay]);ub=R@zl
 bc={'theta_left':float(ub[2]),'sigma_left':float(PARAMS['beta2']*ub[0]-PARAMS['b']*ub[2])}
 return {'x':x,'theta':theta,'sigma':sigma,'u':u,'strain':e,'velocity':v,'q_total':U[3:].sum(axis=0),'dx':dx,'dt':dt,'steps':steps,'speeds':speeds,'tau_channels':taus,'weights':weights,'boundary':bc,'wall_seconds':time.perf_counter()-start}
