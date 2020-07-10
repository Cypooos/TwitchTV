from core.programLoaders.ProgramLoader import ProgramLoader
from core.planning.GoogleCalendar import GoogleCalendarAgent
from core.players.VLCplayer import VLCplayer
from core.players.VLCserver import VLCserverPlayer
from core.players.CVplayer import CV2Player
from core.players.PygletPlayer import PygletPlayer
from core.players.playerWarper import Player

import core.com as com

from core.configParser import configParser

import asyncio

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
    "VLC":VLCserverPlayer,
    "VLCPlayer":VLCplayer,
    "VLCserver":VLCserverPlayer,
    "VLCserverPlayer":VLCserverPlayer,
    "VLC-server":VLCserverPlayer,
    "VLC-serverPlayer":VLCserverPlayer,
    "Pyglet":PygletPlayer,
    "PygletPlayer":PygletPlayer,
    "CV2Player":CV2Player,
    "CV2":CV2Player,
  }

  def __init__(self,conf):
    self.allConf = conf
    self.conf = self.allConf["General"]
    self.reloadModules()
    self.loop = None

  def reloadModules(self):
    com.Out.info("Reloading internal modules")
    self.planningModule = self.PLANNINGS_SYSTEMS.get(self.conf.get('PlanningSystem',None),GoogleCalendarAgent)
    self.programsLoader = self.PROGRAMS_LOADERS.get(self.conf.get('ProgramLoader',None),ProgramLoader)
    self.player = Player(self.STREAMINGS_SERVICES.get(self.conf.get('Player',None),VLCserverPlayer))

    com.Out.debug("Instantiate classes")
    self.planningModule = self.planningModule(configParser(self.allConf[self.planningModule.CONF_NAME],self.planningModule))
    self.programsLoader = self.programsLoader(configParser(self.allConf[self.programsLoader.CONF_NAME],self.programsLoader))
    self.player.instantiate(configParser(self.allConf[self.player.CONF_NAME],self.player.playerClass))

  def start(self):
    # for test purpose
    self.planningModule.reloadEvents()
    self.programsLoader.start(self.player,self.planningModule)
    return
    

