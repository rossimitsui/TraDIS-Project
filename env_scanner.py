#!/usr/bin/env python
import sys
data=open(sys.argv[1]).readlines()

essplusend=0
neplusend=0
ambplusend=0
intplusend=0

essplusstart=0
neplusstart=0
ambplusstart=0
intplusstart=0

essplusmid=0
neplusmid=0
ambplusmid=0
intplusmid=0

essminusend=0
neminusend=0
ambminusend=0
intminusend=0

essminusstart=0
neminusstart=0
ambminusstart=0
intminusstart=0

essminusmid=0
neminusmid=0
ambminusmid=0
intminusmid=0

esscount=0
necount=0
ambcount=0
intcount=0
totalcount=0

for line in data:
  f=line.split('\t')
  if f[3]=='+' and f[4]=='end':
    if f[6]=="essential\n":
      essplusend+=1
      esscount+=1
    if f[6]=="non-essential\n":
      neplusend+=1
      necount+=1
    if f[6]=="ambiguous\n":
      ambplusend+=1
      ambcount+=1
    if f[6]=="intergenic\n":
      intplusend+=1
      intcount+=1
  if f[3]=='+' and f[4]=='start':
    if f[6]=="essential\n":
      essplusstart+=1
      esscount+=1
    if f[6]=="non-essential\n":
      neplusstart+=1
      necount+=1
    if f[6]=="ambiguous\n":
      ambplusstart+=1
      ambcount+=1
    if f[6]=="intergenic\n":
      intplusstart+=1
      intcount+=1
  if f[3]=='+' and f[4]=='middle':
    if f[6]=="essential\n":
      essplusmid+=1
      esscount+=1
    if f[6]=="non-essential\n":
      neplusmid+=1
      necount+=1
    if f[6]=="ambiguous\n":
      ambplusmid+=1
      ambcount+=1
    if f[6]=="intergenic\n":
      intplusmid+=1
      intcount+=1
  if f[3]=='-' and f[4]=='end':
    if f[6]=="essential\n":
      essminusend+=1
      esscount+=1
    if f[6]=="non-essential\n":
      neminusend+=1
      necount+=1
    if f[6]=="ambiguous\n":
      ambminusend+=1
      ambcount+=1
    if f[6]=="intergenic\n":
      intminusend+=1
      intcount+=1
  if f[3]=='-' and f[4]=='start':
    if f[6]=="essential\n":
      essminusstart+=1
      esscount+=1
    if f[6]=="non-essential\n":
      neminusstart+=1
      necount+=1
    if f[6]=="ambiguous\n":
      ambminusstart+=1
      ambcount+=1
    if f[6]=="intergenic\n":
      intminusstart+=1
      intcount+=1
  if f[3]=='-' and f[4]=='middle':
    if f[6]=="essential\n":
      essminusmid+=1
      esscount+=1
    if f[6]=="non-essential\n":
      neminusmid+=1
      necount+=1
    if f[6]=="ambiguous\n":
      ambminusmid+=1
      ambcount+=1
    if f[6]=="intergenic\n":
      intminusmid+=1
      intcount+=1
  totalcount+=1
print "ESSENTIAL:\t"+str(esscount)
print "ess plus end:\t"+str(essplusend)
print "ess plus start:\t"+str(essplusstart)
print "ess plus mid:\t"+str(essplusmid)
print "ess min end:\t"+str(essminusend)
print "ess min start:\t"+str(essminusstart)
print "ess min mid:\t"+str(essminusmid)
print "NON-ESSENTIAL:\t"+str(necount)
print "ne plus end:\t"+str(neplusend)
print "ne plus start:\t"+str(neplusstart)
print "ne plus mid:\t"+str(neplusmid)
print "ne min end:\t"+str(neminusend)
print "ne min start:\t"+str(neminusstart)
print "ne min mid:\t"+str(neminusmid)
print "AMBIGUOUS:\t"+str(ambcount)
print "amb plus end:\t"+str(ambplusend)
print "amb plus start:\t"+str(ambplusstart)
print "amb plus mid:\t"+str(ambplusmid)
print "amb min end:\t"+str(ambminusend)
print "amb min start:\t"+str(ambminusstart)
print "amb min mid:\t"+str(ambminusmid)
print "INTERGENIC:\t"+str(intcount)
print "int plus end:\t"+str(intplusend)
print "int plus start:\t"+str(intplusstart)
print "int plus mid:\t"+str(intplusmid)
print "int min end:\t"+str(intminusend)
print "int min start:\t"+str(intminusstart)
print "int min mid:\t"+str(intminusmid)
print "TOTAL:\t"+str(totalcount)
