"""Pilot implementation of B01 source PDEs/Eq66, not a new tensor/model law.
Two independent numerical representations: transform modes and time-domain CV channels.
"""
import numpy as np
import mpmath as mp
from functools import lru_cache
from .common import INPUT
P=INPUT['material_parameters_SI'];TAU=float(INPUT['source_nondimensional_parameters']['tau']);TIME=float(INPUT['source_nondimensional_parameters']['time'])
FIELDS=('theta','sigma','u')
def derived_np(alpha=None):
 l=float(P['lambda_Pa']);mu=float(P['mu_Pa']);a=float(P['alpha_per_K']) if alpha is None else alpha
 gamma=(3*l+2*mu)*a;beta2=(l+2*mu)/mu;b=gamma*float(P['T0_K'])/mu;g=gamma/(float(P['rho_kg_m3'])*float(P['cE_J_kg_K']))
 return {'gamma':gamma,'beta2':beta2,'b':b,'g':g,'eps_coupling':b*g/beta2}
PARAMS=derived_np();SCALES={'theta':1.,'sigma':PARAMS['b'],'u':PARAMS['b']*TIME/PARAMS['beta2']}
def operator(model,s,tau=TAU):
 if model=='CV':return 1+tau*s,1+0*s
 if model=='MCV3':return 1+3*tau*s+tau*tau*s*s,1+tau*s
 raise ValueError('Model outside approved pilot')
def roots_np(model,s,params=PARAMS):
 M,N=operator(model,s);h=s*M/N;B=s*s+(1+params['eps_coupling'])*h;C=s*s*h
 disc=np.sqrt(B*B-4*C+0j);z1=(B+disc)/2;z2=(B-disc)/2
 # Avoid subtractive loss by recovering the smaller root from product.
 if abs(z1)>=abs(z2) and z1!=0:z2=C/z1
 elif z2!=0:z1=C/z2
 k1=np.sqrt(z1+0j);k2=np.sqrt(z2+0j)
 if k1.real<0:k1=-k1
 if k2.real<0:k2=-k2
 return z1,z2,k1,k2

def laplace_np(model,s,x,params=PARAMS,swap=False,derivatives=False):
 z1,z2,k1,k2=roots_np(model,s,params)
 if swap:z1,z2,k1,k2=z2,z1,k2,k1
 delta=z1-z2
 if abs(delta)<1e-14*max(abs(z1),abs(z2),1e-30):raise ArithmeticError('Degenerate roots require separate limit')
 e1=np.exp(-k1*x);e2=np.exp(-k2*x);b=params['b'];beta2=params['beta2']
 ct1=(z1-s*s)/(s*delta);ct2=-(z2-s*s)/(s*delta)
 cu1=-b*k1/(beta2*s*delta);cu2=b*k2/(beta2*s*delta)
 cs1=b*s/delta;cs2=-cs1
 out={'theta':ct1*e1+ct2*e2,'u':cu1*e1+cu2*e2,'sigma':cs1*e1+cs2*e2}
 if derivatives:
  for name,c1,c2 in [('theta',ct1,ct2),('u',cu1,cu2),('sigma',cs1,cs2)]:
   out[name+'_x']=-k1*c1*e1-k2*c2*e2;out[name+'_xx']=z1*c1*e1+z2*c2*e2
 return out

def laplace_matrix_np(model,s,x):
 # Independently coded first-order spatial system from coupled PDEs; does not use Eq66.
 a=PARAMS['b']/PARAMS['beta2'];M,N=operator(model,s);h=s*M/N
 A=np.array([[0,1,0,0],[s*s,0,0,a],[0,0,0,1],[0,PARAMS['g']*h,h,0]],dtype=complex)
 w,V=np.linalg.eig(A);ix=np.where(w.real<0)[0]
 if len(ix)!=2:raise ArithmeticError('Incorrect stable spatial mode count')
 w=w[ix];V=V[:,ix]
 BC=np.array([[0,0,1,0],[0,PARAMS['beta2'],-PARAMS['b'],0]],dtype=complex)
 amp=np.linalg.solve(BC@V,np.array([1/s,0],dtype=complex));y=V@(amp*np.exp(w*x))
 return {'u':y[0],'theta':y[2],'sigma':PARAMS['beta2']*y[1]-PARAMS['b']*y[2]}

@lru_cache(maxsize=5000)
def _mp_coeff(model,skey,dps):
 s=mp.mp.make_mpc(skey);tau=mp.mpf(str(TAU))
 l=mp.mpf(P['lambda_Pa']);mu=mp.mpf(P['mu_Pa']);alpha=mp.mpf(P['alpha_per_K']);rho=mp.mpf(P['rho_kg_m3']);ce=mp.mpf(P['cE_J_kg_K']);t0=mp.mpf(P['T0_K'])
 gamma=(3*l+2*mu)*alpha;beta2=(l+2*mu)/mu;b=gamma*t0/mu;g=gamma/(rho*ce);eps=b*g/beta2
 if model=='CV':M=1+tau*s;N=mp.mpf(1)
 elif model=='MCV3':M=1+3*tau*s+tau*tau*s*s;N=1+tau*s
 else:raise ValueError('outside approved pilot')
 h=s*M/N;B=s*s+(1+eps)*h;C=s*s*h;disc=mp.sqrt(B*B-4*C);z1=(B+disc)/2;z2=(B-disc)/2
 if abs(z1)>=abs(z2) and z1:z2=C/z1
 elif z2:z1=C/z2
 k1=mp.sqrt(z1);k2=mp.sqrt(z2)
 if mp.re(k1)<0:k1=-k1
 if mp.re(k2)<0:k2=-k2
 return s,z1,z2,k1,k2,b,beta2

def laplace_mp(model,s,x,field):
 # Cache includes the active mpmath precision: no low-precision values promoted as exact.
 key=(s._mpc_ if isinstance(s,mp.mpc) else mp.mpc(s)._mpc_)
 ss,z1,z2,k1,k2,b,beta2=_mp_coeff(model,key,mp.mp.dps)
 x=mp.mpf(str(x));e1=mp.exp(-k1*x);e2=mp.exp(-k2*x);delta=z1-z2
 if field=='theta':return ((z1-ss*ss)*e1-(z2-ss*ss)*e2)/(ss*delta)
 if field=='u':return b*(k2*e2-k1*e1)/(beta2*ss*delta)
 if field=='sigma':return b*ss*(e1-e2)/delta
 raise ValueError(field)

def inverse(model,x,field,degree=64,method='dehoog'):
 # Documented degenerate endpoint: Eq66 transform is identically zero here.
 # de Hoog Q-D cannot divide zero/zero. No interior/tail values are clipped.
 if field=='sigma' and float(x)==0.0:
  return 0.0
 mp.mp.dps=50
 val=mp.invertlaplace(lambda s:laplace_mp(model,s,x,field),mp.mpf(str(TIME)),method=method,degree=degree)
 return float(val)

def cv_channels(model):
 if model=='CV':return np.array([TAU]),np.array([1.])
 if model=='MCV3':
  slow=.5*(3+np.sqrt(5))*TAU;fast=.5*(3-np.sqrt(5))*TAU
  wf=(TAU-fast)/(slow-fast);return np.array([slow,fast]),np.array([1-wf,wf])
 raise ValueError(model)

def transport(model):
 taus,weights=cv_channels(model);n=3+len(taus);a=PARAMS['b']/PARAMS['beta2'];g=PARAMS['g'];A=np.zeros((n,n))
 A[0,1]=-1;A[1,0]=-1;A[1,2]=a;A[2,1]=g
 for j,(tau,w) in enumerate(zip(taus,weights)):A[2,3+j]=1;A[3+j,2]=w/tau
 ev,R=np.linalg.eig(A)
 if np.max(np.abs(ev.imag))>1e-10*max(np.max(np.abs(ev)),1):raise ArithmeticError('Nonreal transport speeds')
 ev=ev.real;R=R.real;order=np.argsort(ev);ev=ev[order];R=R[:,order];ev[np.abs(ev)<1e-10]=0
 invR=np.linalg.inv(R);return A,ev,R,invR,taus,weights

def front_positions():
 _,ev,*_=transport('CV');v=np.sort(ev[ev>0]);return {'slow':float(v[0]*TIME),'fast':float(v[-1]*TIME),'speeds':v.tolist()}

def off_front(x):
 x=np.asarray(x);p=front_positions();h=INPUT['numerics']['front_exclusion_halfwidth']
 return (np.abs(x-p['slow'])>h)&(np.abs(x-p['fast'])>h)
