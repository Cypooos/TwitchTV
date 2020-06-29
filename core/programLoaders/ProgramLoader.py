import core.com as com
from core.configParser import configParser

import configparser
import os


class Program():

  SUPPORTED_FILES = [
    "mp4"
  ]
  SUPPORTED_LINKS = [
    "link","txt"
  ]
  CONF_NEED = {
    "PlayingOrder":("Random","RandomMixed","Order"),
    "OnFileEnd":str,
    "OnPlanEnd":("Continue", "Save"),
    "FileStart":int,
    "ProgramName":str
  }
  CONF_NAME = "Program"

  def __init__(self,path):
    self.path = path
    self.name = "Yet Undefined"
    self.confF = None
    self.vids = None
    self.links = None
    self.conf = None
    self.refreshConf()
    self.name = self.conf["ProgramName"]
    self.refreshPath()
    com.Out.debug("File list:"+",".join(self.vids))
    com.Out.debug("Links list:"+",".join(self.links))
    
  
  def getFiles(self,formats):
    returning = []
    for r, _, f in os.walk(self.path):
      for fileF in f:
        if fileF.split(".")[-1] in formats:
          returning.append(os.path.join(r, fileF))
          com.Out.debug("Adding file file="+str(fileF)+", format="+"-".join(formats))
    com.Out.debug("For Path ="+str(self.path)+", format="+"-".join(formats)+", result is '"+str(", ".join(returning))+"'")
    return returning

  def refreshConf(self):
    com.Out.debug("Loading conf at "+self.path)
    CONF = configparser.ConfigParser()
    CONF.read(self.getFiles(["conf"])[0])
    print(self.getFiles(["conf"])[0])
    self.conf = configParser(CONF["Program"],self.__class__)
  
  def refreshPath(self):
    com.Out.debug("Refreshing files")
    self.vids = self.getFiles(self.SUPPORTED_FILES)
    self.links = self.getFiles(self.SUPPORTED_LINKS)



class ProgramLoader():

  CONF_NEED = {
    "ProgramsFolder":str
  }
  CONF_NAME = "ProgramLoader"

  def __init__(self,ProgramLoaderConf):
    self.conf = ProgramLoaderConf
    self.programs = [Program(os.path.join(self.conf["ProgramsFolder"], o)) for o in os.listdir(self.conf["ProgramsFolder"]) if os.path.isdir(os.path.join(self.conf["ProgramsFolder"],o))]
    com.Out.debug("programs: "+", ".join([x.path for x in self.programs]))


  def reload(self):
    pass