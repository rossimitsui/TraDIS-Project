#!/usr/bin/env python
import sys
data=open(sys.argv[1]).readlines()[1:]

for line in data:
  f=line.split(",")
  print f[0]
