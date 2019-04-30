#!/usr/bin/env python
import sys
essendata=open(sys.argv[1]).readlines()[1:] ##csv of essential genes
readdata=open(sys.argv[2]).readlines() ##essential_reads.txt

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

for line in readdata:
  f=line.split('\t')
  ins_site=float(f[7])
  for line2 in essendata:
    g=line2.split(',')
    start=float(g[3])
    end=float(g[4])
    locus_tag=g[0]
    if ins_site>=start and ins_site<=end:
      gene_len=end-start
      dist_ins=ins_site-start
      perc_along=(dist_ins/gene_len)*100
      total+=1
      if perc_along>=0 and perc_along<10:
        zeroten+=1
      if perc_along>=10 and perc_along<20:
        tentwen+=1
      if perc_along>=20 and perc_along<30:
        twenthir+=1
      if perc_along>=30 and perc_along<40:
        thirfour+=1
      if perc_along>=40 and perc_along<50:
        fourfive+=1
      if perc_along>=50 and perc_along<60:
        fivesix+=1
      if perc_along>=60 and perc_along<70:
        sixsev+=1
      if perc_along>=70 and perc_along<80:
        seveight+=1
      if perc_along>=80 and perc_along<90:
        eightnine+=1
      if perc_along>=90 and perc_along<=100:
        ninecent+=1
print '0-10%:'+'\t'+'10-20%:'+'\t'+'20-30%:'+'\t'+'30-40%:'+'\t'+'40-50%:'+'\t'+'50-60%:'+'\t'+'60-70%:'+'\t'+'70-80%:'+'\t'+'80-90%:'+'\t'+'90+%:'+'\t'+'TOTAL:'
print str(zeroten)+'\t'+str(tentwen)+'\t'+str(twenthir)+'\t'+str(thirfour)+'\t'+str(fourfive)+'\t'+str(fivesix)+'\t'+str(sixsev)+'\t'+str(seveight)+'\t'+str(eightnine)+'\t'+str(ninecent)+'\t'+str(total)
