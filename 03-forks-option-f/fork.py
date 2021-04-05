#!/usr/bin/python3.8

import os

def child():
   print('\n{} : Hello Xavki !!'.format(os.getpid()))
   os._exit(0)

def parent():
   while True:
      newpid = os.fork()
      if newpid == 0:
         child()
      else:
         pids = (os.getpid(), newpid)
         print("parent: %d, child: %d\n" % pids)
      reply = input("q : quit / c : create a new fork")
      if reply == 'c': 
          continue
      else:
          break

parent()
