#!/usr/bin/env python

import re
import sys 

data=open(sys.argv[1]).readlines()[1:] ##csv format file with all genes in annotation and essential calls (With Accession)
data2=open(sys.argv[2]).readlines() ##sam format file containing split reads that map to essential genes

print_dict={}
ess_dict={}

for line in data:
  f=line.split(',')
  start=int(f[4])
  end=int(f[5])
  for line2 in data2:
    g=line2.split('\t')
    FLAG=int(g[1])
    split=g[5].split()
    if FLAG&16: # Bitwise AND
      direction="-"
      ins_site=int(g[3])+len(g[9])
      if ins_site>=start and ins_site<=end:
        gene_len=float((int(f[5])+1)-int(f[4]))
        dist_ins=float(ins_site-int(f[4]))
        perc_along=(dist_ins/gene_len)*100
	if re.match("[0-9]{1,2}[M][0-9]{1,2}[SHD]$",g[5]):
	  part_of_read="end"
	elif re.match("[0-9]{1,2}[SHD][0-9]{1,2}[M]$",g[5]):
	  part_of_read="start"
	else:
	  part_of_read="middle"
	if f[-1]=="essential\n":
          print f[1]+'\t'+g[0]+'\t'+str(perc_along)+'\t'+direction+'\t'+part_of_read+'\t'+g[3]+'\t'+f[-1],
	  ess_dict[g[0]+g[3]]="essential"
	  print_dict[line2]=line
	else:
	  pass
    elif FLAG^16: # Bitwise XOR
      direction="+"
      if int(g[3])>=start and int(g[3])<=end:
        gene_len=float((int(f[5])+1)-int(f[4]))
        dist_ins=float(int(g[3])-int(f[4]))
        perc_along=(dist_ins/gene_len)*100
	if re.match("[0-9]{1,2}[M][0-9]{1,2}[SHD]$",g[5]):
	  part_of_read="start"
	elif re.match("[0-9]{1,2}[SHD][0-9]{1,2}[M]$",g[5]):
	  part_of_read="end"
	else:
	  part_of_read="middle"
	if f[-1]=="essential\n":
	  print f[1]+'\t'+g[0]+'\t'+str(perc_along)+'\t'+direction+'\t'+part_of_read+'\t'+g[3]+'\t'+f[-1],
	  ess_dict[g[0]+g[3]]="essential"
	  print_dict[line2]=line
	else:
	  pass
    else:
      print "error, can't determine direction"
      
read_dict={}

for line in data:
  f=line.split(',')
  start=int(f[4])
  end=int(f[5])
  for line2 in data2:
    g=line2.split('\t')
    FLAG=int(g[1])
    split=g[5].split()
    if FLAG&16: # Bitwise AND
      direction="-"
      ins_site=int(g[3])+len(g[9])
      if ins_site>=start and ins_site<=end:
        gene_len=float((int(f[5])+1)-int(f[4]))
        dist_ins=float(ins_site-int(f[4]))
        perc_along=(dist_ins/gene_len)*100
	if re.match("[0-9]{1,2}[M][0-9]{1,2}[SHD]$",g[5]):
	  part_of_read="end"
	elif re.match("[0-9]{1,2}[SHD][0-9]{1,2}[M]$",g[5]):
	  part_of_read="start"
	else:
	  part_of_read="middle"
	if f[-1]=="non-essential\n":
          print f[1]+'\t'+g[0]+'\t'+str(perc_along)+'\t'+direction+'\t'+part_of_read+'\t'+g[3]+'\t'+f[-1],
	  read_dict[g[0]]=f[1]
	  print_dict[line2]=line
	elif f[-1]=="ambiguous\n":
	  print f[1]+'\t'+g[0]+'\t'+str(perc_along)+'\t'+direction+'\t'+part_of_read+'\t'+g[3]+'\t'+f[-1],
	  read_dict[g[0]]=f[1]
	  print_dict[line2]=line
	else:
	  pass
    elif FLAG^16: # Bitwise XOR
      direction="+"
      if int(g[3])>=start and int(g[3])<=end:
        gene_len=float((int(f[5])+1)-int(f[4]))
        dist_ins=float(int(g[3])-int(f[4]))
        perc_along=(dist_ins/gene_len)*100
	if re.match("[0-9]{1,2}[M][0-9]{1,2}[SHD]$",g[5]):
	  part_of_read="start"
	elif re.match("[0-9]{1,2}[SHD][0-9]{1,2}[M]$",g[5]):
	  part_of_read="end"
	else:
	  part_of_read="middle"
	if f[-1]=="non-essential\n":
	  print f[1]+'\t'+g[0]+'\t'+str(perc_along)+'\t'+direction+'\t'+part_of_read+'\t'+g[3]+'\t'+f[-1],
	  read_dict[g[0]]=f[1]
	  print_dict[line2]=line
	elif f[-1]=="ambiguous\n":
	  print f[1]+'\t'+g[0]+'\t'+str(perc_along)+'\t'+direction+'\t'+part_of_read+'\t'+g[3]+'\t'+f[-1],
	  read_dict[g[0]]=f[1]
	  print_dict[line2]=line
	else:
	  pass
    else:
      print "error, can't determine direction"
      
otherdict={}

for line2 in data2:
  g=line2.split('\t')
  FLAG=int(g[1])
  if FLAG&16:
    direction="-"
    if re.match("[0-9]{1,2}[M][0-9]{1,2}[SHD]$",g[5]):
      part_of_read="end"
    elif re.match("[0-9]{1,2}[SHD][0-9]{1,2}[M]$",g[5]):
      part_of_read="start"
    else:
      part_of_read="middle"
  elif FLAG^16:
    direction="+"
    if re.match("[0-9]{1,2}[M][0-9]{1,2}[SHD]$",g[5]):
      part_of_read="start"
    elif re.match("[0-9]{1,2}[SHD][0-9]{1,2}[M]$",g[5]):
      part_of_read="end"
    else:
      part_of_read="middle"
  else:
    print "error, can't determine direction"
  if g[0]+g[3] in ess_dict:
    pass
  elif g[0] not in otherdict and g[0] not in read_dict:
    print "N/A"+'\t'+g[0]+'\t'+"N/A"+'\t'+direction+'\t'+part_of_read+'\t'+g[3]+'\t'+"intergenic"
    otherdict[g[0]]="intergenic"
    print_dict[line2]=line
  else:
    pass
    
for line2 in data2:
  g=line2.split('\t')
  FLAG=int(g[1])
  if line2 not in print_dict:
    if FLAG&16:
      direction="-"
      if re.match("[0-9]{1,2}[M][0-9]{1,2}[SHD]$",g[5]):
        part_of_read="end"
      elif re.match("[0-9]{1,2}[SHD][0-9]{1,2}[M]$",g[5]):
        part_of_read="start"
      else:
        part_of_read="middle"
      print "N/A"+'\t'+g[0]+'\t'+"N/A"+'\t'+direction+'\t'+part_of_read+'\t'+g[3]+'\t'+"intergenic"
      print_dict[line2]=line
    if FLAG^16:
      direction="+"
      if re.match("[0-9]{1,2}[M][0-9]{1,2}[SHD]$",g[5]):
        part_of_read="start"
      elif re.match("[0-9]{1,2}[SHD][0-9]{1,2}[M]$",g[5]):
        part_of_read="end"
      else:
        part_of_read="middle"
      print "N/A"+'\t'+g[0]+'\t'+"N/A"+'\t'+direction+'\t'+part_of_read+'\t'+g[3]+'\t'+"intergenic"
      print_dict[line2]=line
  else:
    pass
