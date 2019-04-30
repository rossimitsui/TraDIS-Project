#!/usr/bin/env python
import sys
import re

data=open(sys.argv[1]).readlines()

for line in data:
  f= line.split('\t')
  if re.search('SA:Z:',line):
    print line,
  elif re.search('[SH]',f[5]):
    print line,
  else:
    pass
