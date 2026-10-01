from pathlib import Path
import json,hashlib,platform,time,resource,os
from importlib.metadata import version
ROOT=Path(__file__).resolve().parents[1]
INPUT=json.loads((ROOT/'case_input.json').read_text())
def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def cpu_self():
 r=resource.getrusage(resource.RUSAGE_SELF);return r.ru_utime+r.ru_stime
class Stage:
 def __init__(self,name):self.name=name;self.wall0=time.perf_counter();self.cpu0=0.;self.done=False
 def check(self):
  ledger=json.loads((ROOT/'logs/CPU_LEDGER.json').read_text());total=ledger['setup_reserve_seconds']+ledger['measured_CPU_total']+cpu_self()
  if total>INPUT['budget']['max_aggregate_CPU_seconds']:raise RuntimeError('STOP: approved aggregate CPU cap exceeded')
  size=sum(p.stat().st_size for p in ROOT.rglob('*') if p.is_file())
  if size>INPUT['budget']['max_generated_bytes']:raise RuntimeError('STOP: approved generated-data cap exceeded')
 def finish(self,status='RUN_SUCCESS',extra=None):
  if self.done:return
  if status == 'RUN_SUCCESS': self.check()
  ledger=json.loads((ROOT/'logs/CPU_LEDGER.json').read_text())
  record={'stage':self.name,'status':status,'CPU_seconds':cpu_self(),'wall_seconds':time.perf_counter()-self.wall0,'max_RSS_kB':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,'code_version':{str(p.relative_to(ROOT)):sha(p) for p in list((ROOT/'src').glob('*.py'))+list(ROOT.glob('run_*.py'))},'input_sha256':sha(ROOT/'case_input.json'),'plan_sha256':sha(ROOT/'PILOT_PLAN_FROZEN.md'),'source_pdf_sha256':sha(INPUT['source_pdf']),'python':platform.python_version(),'environment':{p:version(p) for p in ['numpy','scipy','mpmath','matplotlib','PyMuPDF']},'threads':{'OPENBLAS_NUM_THREADS':os.environ.get('OPENBLAS_NUM_THREADS'),'OMP_NUM_THREADS':os.environ.get('OMP_NUM_THREADS')},'label':'PILOT — NOT FINAL VALIDATION'}
  if extra:record.update(extra)
  (ROOT/'logs'/f'{self.name}.json').write_text(json.dumps(record,indent=2))
  ledger['stages'].append(record);ledger['measured_CPU_total']+=record['CPU_seconds'];(ROOT/'logs/CPU_LEDGER.json').write_text(json.dumps(ledger,indent=2));self.done=True
  print('STAGE',self.name,status,'CPU_s',record['CPU_seconds'],'wall_s',record['wall_seconds'],flush=True)
