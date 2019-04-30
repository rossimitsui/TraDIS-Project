#!/usr/bin/env python

import sys
import re

data=open(sys.argv[1]).readlines() ##sam of ALL splits (incl. masks)

zeroten=0
tentwen=0
twenthir=0
thirfour=0
fourfive=0
fivesix=0
sixsev=0
seveight=0
eightnine=0
ninecent=0
total=0

for line in data:
  f=line.split('\t')
  g=list(f[5])
  FLAG=int(f[1])
  match=re.search("([0-9]{1,2})([H])",f[5])
  if FLAG&16: ## reverse complement of read
    if re.match('[0-9]', g[-2]) and re.match('[0-9]', g[-3]) and re.match('[0-9]', g[-4]):
      breakpoint=float(g[-4]+g[-3]+g[-2])
    elif re.match('[0-9]', g[-2]) and re.match('[0-9]', g[-3]):
      breakpoint=float(g[-3]+g[-2])
    elif re.match('[0-9]', g[-2]):
      breakpoint=float(g[-2])
  elif FLAG^16:
    if re.match('[0-9]', g[0]) and re.match('[0-9]', g[1]) and re.match('[0-9]', g[2]):
      breakpoint=float(g[0]+g[1]+g[2])
    elif re.match('[0-9]', g[0]) and re.match('[0-9]', g[1]):
      breakpoint=float(g[0]+g[1])
    elif re.match('[0-9]', g[0]):
      breakpoint=float(g[0])
  if match:
    item=match.groups()
    break_rat=((float(breakpoint))/((float(len(f[9])))+(float(item[0]))))
    break_perc=break_rat*100
  else:
    break_rat=((float(breakpoint))/(float(len(f[9]))))
    break_perc=break_rat*100
  total+=1
  if break_perc>=0 and break_perc<=10:
    zeroten+=1
  if break_perc>10 and break_perc<=20:
    tentwen+=1
  if break_perc>20 and break_perc<=30:
    twenthir+=1
  if break_perc>30 and break_perc<=40:
    thirfour+=1
  if break_perc>40 and break_perc<=50:
    fourfive+=1
  if break_perc>50 and break_perc<=60:
    fivesix+=1
  if break_perc>60 and break_perc<=70:
    sixsev+=1
  if break_perc>70 and break_perc<=80:
    seveight+=1
  if break_perc>80 and break_perc<=90:
    eightnine+=1
  if break_perc>90 and break_perc<=100:
    ninecent+=1
print '0-10%:'+'\t'+'10-20%:'+'\t'+'20-30%:'+'\t'+'30-40%:'+'\t'+'40-50%:'+'\t'+'50-60%:'+'\t'+'60-70%:'+'\t'+'70-80%:'+'\t'+'80-90%:'+'\t'+'90+%:'+'\t'+'TOTAL:'
print str(zeroten)+'\t'+str(tentwen)+'\t'+str(twenthir)+'\t'+str(thirfour)+'\t'+str(fourfive)+'\t'+str(fivesix)+'\t'+str(sixsev)+'\t'+str(seveight)+'\t'+str(eightnine)+'\t'+str(ninecent)+'\t'+str(total)
