import json,traceback,numpy as np
from src.common import ROOT,Stage,INPUT
from src.physics import FIELDS,SCALES,inverse,off_front
stage=Stage('P03B_INVERSION_PROBES_ENDPOINT_CORRECTED')
try:
 x=np.asarray(INPUT['numerics']['probes']);rows=[];vals={};degrees=INPUT['numerics']['Laplace_probe_degrees']
 for model in INPUT['models']:
  vals[model]={}
  for f in FIELDS:
   vals[model][f]={}
   for deg in degrees:
    out=[]
    for xx in x:
     stage.check();out.append(inverse(model,float(xx),f,degree=deg,method='dehoog'))
    vals[model][f][f'dehoog_{deg}']=out
    (ROOT/'data/INVERSION_PROBES_PARTIAL_CHECKPOINT.json').write_text(json.dumps({'x':x.tolist(),'values':vals,'status':'PARTIALLY_RUN'},indent=2))
    print('PROBES',model,f,'dehoog',deg,flush=True)
   out=[]
   for xx in x:
    stage.check();out.append(inverse(model,float(xx),f,degree=80,method='cohen'))
   vals[model][f]['cohen_80']=out
   arr=np.asarray(vals[model][f]['dehoog_64']);a48=np.asarray(vals[model][f]['dehoog_48']);ac=np.asarray(out);mask=off_front(x)
   change=float(np.max(np.abs(arr[mask]-a48[mask]))/SCALES[f]);alg=float(np.max(np.abs(arr[mask]-ac[mask]))/SCALES[f])
   rows.append({'model':model,'field':f,'dehoog_48_64_scaled_max':change,'cohen80_dehoog64_scaled_max':alg,'dehoog_refinement_pass':change<=2e-5,'algorithm_crosscheck_pass':alg<=5e-5,'finite':bool(np.all(np.isfinite(arr)))})
 result={'label':'PILOT — NOT FINAL VALIDATION','x':x.tolist(),'values':vals,'metrics':rows,'all_diagnostics_pass':all(r['dehoog_refinement_pass'] and r['algorithm_crosscheck_pass'] and r['finite'] for r in rows)}
 (ROOT/'data/INVERSION_PROBES.json').write_text(json.dumps(result,indent=2))
 print(json.dumps({'metrics':rows,'all_diagnostics_pass':result['all_diagnostics_pass']},indent=2));stage.finish('RUN_SUCCESS',{'scientific_check_status':'PASS' if result['all_diagnostics_pass'] else 'PARTIAL'})
except Exception as e:
 (ROOT/'logs/P03B_ERROR.txt').write_text(traceback.format_exc());stage.finish('RUN_FAILED',{'error':str(e)});raise
