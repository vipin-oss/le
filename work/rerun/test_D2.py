import sys, os, json, time
os.environ['OPENBLAS_NUM_THREADS']='1'
sys.path.insert(0,'/home/user/work/rerun'); 
exec(open('/home/user/work/rerun/test_D.py').read().split("cases = {")[0])   # reuse run_series / Dval
runs=[(10,5.0,[8,10,12,20,32]),(20,20.0,[8,12,32])]
t00=time.time(); out={}
for a_nm,tau,Ts in runs:
    for T in Ts:
        NT=int(round(16*T))   # keep dt = T/NT = 0.0625 t_th
        t,hf=run_series('FOURIER',0.0,a_nm,T_WIN=float(T),NT_T=NT)
        t,hc=run_series('CV',tau,a_nm,T_WIN=float(T),NT_T=NT)
        D=Dval(t,hc,hf); out[f'a{a_nm}_T{T}']=D
        print(f"[{time.time()-t00:4.0f}s] a={a_nm:2d} nm tau={tau:4.1f} ps  T_WIN={T:2d} t_th : D={D:.4e}   (quasi-static value 1.9975e-03)", flush=True)
json.dump(out,open('/home/user/work/rerun/D2_summary.json','w'),indent=1)
