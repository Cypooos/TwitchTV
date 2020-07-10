import traceback, sys
import core.com as com
com.Out.info("Logger imported :D")
import sys, traceback

try:
  import configparser

  CONF = configparser.ConfigParser()
  CONF.read("config.conf")
  com.Out.setLogMode(CONF["General"].get("LogLevel","INFO,ERROR,WARNING").split(","))
  
  com.Out.debug("Configuration Loaded & LogLevel Setup")

  from core.TVmanager import TVmanager

  manager = TVmanager(CONF)
  com.Out.debug("Manager Setup")


  if __name__ == "__main__":
    try:
      com.Out.debug("Starting manager")
      manager.start()
      com.Out.warning("Manager stoped ? Or did program close ?")
    except Exception as e:
      com.Out.error("Crash in code : "+str(e))
      com.Out.betterCrash(e)
      raise e
      exit()
except SystemExit as e:
  com.Out.info("System exit with code : "+str(e))
except Exception as e:
  com.Out.error("Crash in importing : "+str(e))
  com.Out.betterCrash(e)
  raise e
