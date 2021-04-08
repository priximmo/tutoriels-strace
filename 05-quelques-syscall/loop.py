#!/usr/bin/python3

import time
import os

pid = os.getpid()
for i in range(1,1000000000):
  time.sleep(2)
  time.sleep(1)
  print("{} : Hello xavki {}".format(pid,i))
