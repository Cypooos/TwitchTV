
import core.com as com
com.Out.debug("Logger imported")

import configparser

CONF = configparser.ConfigParser()
CONF.read("config.conf")
com.Out.debug("Configuration Setup")

from core.TVmanager import TVmanager

manager = TVmanager(CONF)
com.Out.debug("Manager Setup")


if __name__ == "__main__":
  com.Out.debug("Starting manager")
  manager.start()
  com.Out.warning("Manager stoped ? Or did program close ?")