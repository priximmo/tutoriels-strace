#!/usr/bin/python3.8

import os
import time
import signal



def receiveSignal(signalNumber, frame):
    print('Received:', signalNumber)
    return

def readConfiguration(signalNumber, frame):
    print ('(SIGHUP) reading configuration')
    return

def terminateProcess(signalNumber, frame):
    print('Waiting for terminating the process...')
    time.sleep(2)
    print ('(SIGTERM) terminating the process')
    sys.exit()


def child():
   time.sleep(2)
   print('\n{} : Hello Xavki !!'.format(os.getpid()))
   signal.signal(signal.SIGTERM, terminateProcess)
   os._exit(1)

def parent():
   while True:
      time.sleep(5)
      newpid = os.fork()
      if newpid == 0:
         child()
      else:
         pid, status = os.wait()
         pids = (os.getpid(), newpid)
         print("parent: %d, child: %d\n" % pids)
         print("Pid {} : status {}".format(pid,status))
         time.sleep(3)
  

if __name__ == '__main__':
    # register the signals to be caught
    signal.signal(signal.SIGHUP, readConfiguration)
    signal.signal(signal.SIGINT, receiveSignal)
    signal.signal(signal.SIGQUIT, receiveSignal)
    signal.signal(signal.SIGILL, receiveSignal)
    signal.signal(signal.SIGTRAP, receiveSignal)
    signal.signal(signal.SIGABRT, receiveSignal)
    signal.signal(signal.SIGBUS, receiveSignal)
    signal.signal(signal.SIGFPE, receiveSignal)
    #signal.signal(signal.SIGKILL, receiveSignal)
    signal.signal(signal.SIGUSR1, receiveSignal)
    signal.signal(signal.SIGSEGV, receiveSignal)
    signal.signal(signal.SIGUSR2, receiveSignal)
    signal.signal(signal.SIGPIPE, receiveSignal)
    signal.signal(signal.SIGALRM, receiveSignal)
    
    parent()
