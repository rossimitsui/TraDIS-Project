#!/usr/bin/env python
import sys
data=open(sys.argv[1]).readlines() ##paper
data2=open(sys.argv[2]).readlines() ##bwa
gene_dict={}
for line in data:
  f=line.split(',')
  gene_dict[f[1]]=line
for line2 in data2:
  g=line2.split(',')
  if g[1] in gene_dict:
    print line2,
