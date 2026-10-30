import re, os
files=[
 'phase5/master/sections/sec03_foundations.tex',
 'phase5/master/sections/sec05_multiphysics.tex',
 'phase5/master/sections/sec06_transport.tex',
 'phase5/master/sections/sec07_nonlocal.tex',
 'phase5/master/sections/sec09_interfaces.tex',
 'phase5/master/sections/sec11_advanced.tex',
 'phase5/master/sections/sec12_comparative.tex',
 'phase5/master/sections/sec14_taxonomy.tex',
]
env_start=re.compile(r'\\begin\{(equation|displaymath|eqnarray|align|align\*|math)\}')
env_end=re.compile(r'\\end\{(equation|displaymath|eqnarray|align|align\*|math)\}')
for f in files:
    s=open(f,encoding='utf-8').read()
    lines=s.split('\n')
    in_disp=False
    issues=[]
    for i,line in enumerate(lines,1):
        if env_start.search(line): in_disp=True
        if env_end.search(line): in_disp=False
        if in_disp: continue
        # strip inline math $...$ and \(...\)
        tmp=re.sub(r'\$[^$]*\$',' ',line)
        tmp=re.sub(r'\\\([^\)]*\\\)',' ',tmp)
        # find _ or ^ not preceded by backslash
        for m in re.finditer(r'(?<!\\)[_^]', tmp):
            issues.append((i,m.group(0),line.rstrip()[:80]))
    if issues:
        print('=== %s: %d GENUINE text-mode _/^ ==='%(f,len(issues)))
        seen=set()
        for it in issues:
            k=(it[0],it[2])
            if k not in seen:
                seen.add(k)
                print('  line %d %s | %s'%it)
    else:
        print('%s: clean'%f)
