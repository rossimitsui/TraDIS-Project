#!/usr/bin/env python

import sys

data=open(sys.argv[1]).readlines()

for line in data:
  f=line.split('\t')
  print f[0]+'\t'+f[1]+'\t'+f[2]+'\t'+f[3]+'\t'+f[4]
