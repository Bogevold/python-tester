#!/bin/env python
import os,time,shutil
from os import walk

def crePath(sti):
  if not os.path.exists(sti):
    print "Lag: %s" % (sti)
    os.makedirs(sti)
  else:
    print "%s finnes" % (sti)

sti=os.getcwd()
f = []
for (dirpath, dirnames, filenames) in walk(sti):
  f.extend(filenames)
  break

for (fil) in f:
  tid=os.path.getmtime(sti+"/"+fil)
  strTid=time.strftime("%Y%m%d",time.localtime(tid))
  print "%s ble opprettet %s" % (fil, strTid)
  crePath(sti+"/"+strTid)
  shutil.move(sti+"/"+fil, sti+"/"+strTid+"/"+fil)
