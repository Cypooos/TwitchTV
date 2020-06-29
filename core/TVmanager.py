from core.programLoaders.ProgramLoader import ProgramLoader
from core.planning.GoogleCalendar import GoogleCalendarAgent
from core.players.VLCplayer import VLCplay
from core.players.CVplayer import CV2Player
from core.players.PygletPlayer import PygletPlayer

import core.com as com

from core.configParser import configParser

class TVmanager():

  PLANNINGS_SYSTEMS={
    "GoogleCalendar":GoogleCalendarAgent
    }
  DIRECTS_SYSTEM={}
  PROGRAMS_LOADERS={
    "classic":ProgramLoader,
    "default":ProgramLoader,
  }
  STREAMINGS_SERVICES={
    "VLC":VLCplay,
    "VLCPlayer":VLCplay,
    "Pyglet":PygletPlayer,
    "PygletPlayer":PygletPlayer,
    "CV2Player":CV2Player,
    "CV2":CV2Player,
    "VLC-server":VLCplay,
  }
  ACTIONS_LIST = [
    "playF",
    "playU",
    "pause",
    "setTime",
    "addText",
    "setVolume",
    "getTime",
    "getMax"
  ]

  def __init__(self,conf):
    self.allConf = conf
    self.conf = self.allConf["General"]
    self.reloadModules()

  def reloadModules(self):
    com.Out.info("Reloading internal modules")
    self.planningModule = self.PLANNINGS_SYSTEMS.get(self.conf.get(self.conf['PlanningSystem'],None),GoogleCalendarAgent)
    self.programsLoader = self.PROGRAMS_LOADERS.get(self.conf.get(self.conf['ProgramLoader'],None),ProgramLoader)
    self.streamingService = self.STREAMINGS_SERVICES.get(self.conf.get(self.conf['Player'],None),VLCplay)

    com.Out.debug("Instantiate classes")
    self.planningModule = self.planningModule(configParser(self.allConf[self.planningModule.CONF_NAME],self.planningModule))
    self.programsLoader = self.programsLoader(configParser(self.allConf[self.programsLoader.CONF_NAME],self.programsLoader))
    self.streamingService = self.streamingService(configParser(self.allConf[self.streamingService.CONF_NAME],self.streamingService))

  def start(self):
    # for test purpose
    self.planningModule.reloadEvents()
    self.programsLoader.start(self.toStreamingAction,self.planningModule.getNext)

  def toStreamingAction(self,action,*params):
    com.Out.debug("Taking command '"+action+"'"+" ".join(params))
    if not action in self.streamingService.ACTIONS:
      com.Out.warning("The ProgramLoader wanted to do '"+action+"' but the Streaming service didn't supported it.")
      return False
    elif not action in self.ACTIONS_LIST:
      com.Out.warning("The ProgramLoader wanted to do '"+action+"' this action does not exist.")
      return False
    elif action == "playF":
      return self.streamingService.playF(*params)
    elif action == "playU":
      return self.streamingService.playU(*params)
    elif action == "pause":
      return self.streamingService.pause(*params)
    elif action == "setTime":
      return self.streamingService.setTime(*params)
    elif action == "addText":
      return self.streamingService.addText(*params)
    elif action == "setVolume":
      return self.streamingService.setVolume(*params)
    elif action == "getTime": # float sec
      return self.streamingService.getTime(*params)
    elif action == "getMax": # float sec
      return self.streamingService.getMax(*params)
    else:
      com.Out.warning("Command not yet defined but existing '"+action+"'")
      return False
