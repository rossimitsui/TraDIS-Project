#!/usr/bin/env python

import sys

data=open(sys.argv[1]).readlines()

for line in data:
  f=line.split('\t')
  if f[5]=='-\n':
    print f[0]+'\t'+str(int(f[2])-1)+'\t'+f[2]+'\t'+f[3]+'\t'+f[4]+'\t'+f[5],
  elif f[5]=='+\n':
    print f[0]+'\t'+f[1]+'\t'+str(int(f[1])+1)+'\t'+f[3]+'\t'+f[4]+'\t'+f[5],
  else:
    print "ERROR: unable to determine direction of read"
