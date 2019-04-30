#!/usr/bin/env python

import sys

data=open(sys.argv[1]).readlines() ##the split reads file

data2=open(sys.argv[2]).readlines() ##reads to essential genes file

split_dict={}

for line2 in data2:
  f=line2.split("\t")
  split_dict[f[8]]=line2
  
for line in data:
  g=line.split("\t")
  if g[0] in split_dict:
    print line,
  else:
    pass
