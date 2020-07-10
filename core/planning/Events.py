import datetime

class Event():

  STARTED = 0
  FINISH = 1
  FUTURE = 2

  def __init__(self,time,name,end):
    self.time = time
    self.name = name
    self.end = end
  
  def getstate(self):
    if datetime.now() > self.end:return self.FINISH
    if datetime.now() > self.start:return self.STARTED
    return self.FUTURE
  
  def getTime(self,type_=0):
    if type_==self.STARTED:return (datetime.now()-self.start).total_seconds()
    else:return (datetime.now()-self.start).total_seconds()