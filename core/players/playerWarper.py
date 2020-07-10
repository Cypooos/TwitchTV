import core.com as com

class Player():


  def __init__(self,class_):
    self.playerClass = class_
    self.conf = None
    self.player = None
    self.CONF_NAME = class_.CONF_NAME
    self.CONF_NEED = class_.CONF_NEED

  def instantiate(self,conf):
    self.conf = conf
    self.player = self.playerClass(self.conf)

  def __getattr__(self, method_name):
    com.Out.debug("Want to class: "+method_name)
    def warper(*args, **kwargs):
      ele = getattr(self.player, method_name,None)
      if ele == None: # Should not happen wtf 
        com.Out.error("The ProgramLoader wanted to do '"+action+"' on '"+str(self.playerClass.__name__)+"' this action does not exist.")
        return None
      return ele(*args, **kwargs)
    return warper

