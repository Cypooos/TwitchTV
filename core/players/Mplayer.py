import time 
from subprocess import Popen, PIPE 


#import core.com as com

import os

class Mplayer():

  CONF_NEED = {
    "Path":str
  }
  CONF_NAME = "Mplayer"

  ACTIONS = [
    "playF",
    "playU",
    "setTime",
    "getTime",
    "getMax",
    "stop",
    "volume"
  ]

  def __init__(self,conf):
    self.conf = conf
    command = [self.conf["Path"]]
    command.extend([
      "-idle", "-fixed-vo", "-slave", "quiet"
    ])

    LINE_BUFFERED = 1 
    filename = r"programs/emission1/test2.mp4"
    #filename = r"https://storage.googleapis.com/disruptplus_archives/Nature/Nature_Desert.mp4"
    self.process = Popen(command + [filename], stdin=PIPE, universal_newlines=True, bufsize=LINE_BUFFERED) 
    while True:
      self.__processCommand(input("=> "))
    time.sleep(8)
    self.__processCommand("loadfile 'programs/emission1/test.mp4' append")
    time.sleep(8)
    self.__processCommand("pausing_keep_force pt_step 1")
    self.__processCommand("get_property pause")
    time.sleep(8)
    self.__processCommand('quit') 

  def __processCommand(self,command):
    print(command, flush=True, file=self.process.stdin)


if __name__ == "__main__":
  s = Mplayer({"Path":"extern/mplayer/mplayer.exe"})
  time.sleep(4)









"""

import time 
from subprocess import Popen, PIPE 

LINE_BUFFERED = 1 
filename = r"https://storage.googleapis.com/disruptplus_archives/Nature/Nature_Desert.mp4"
with Popen('mplayer -slave -quiet'.split() + [filename], 
      stdin=PIPE, universal_newlines=True, bufsize=LINE_BUFFERED) as process: 
    send_command = lambda command: print(command, flush=True, file=process.stdin) 
    time.sleep(1) 
    for _ in range(2): 
     send_command('pause') 
     time.sleep(1) 
    send_command('quit') 
"""