import core.com as com
com.Out.debug("Config Parser Imported")

def configParser(configDict,classObj):
  new = {}
  com.Out.debug("Encoding config for class :'"+classObj.__name__+"'")
  for name,typein in classObj.CONF_NEED.items():
    if not name in configDict:com.Out.warning("Config file not have the needed config for '"+classObj.__name__+"' at '"+name+"'")
    else:
      try:
        com.Out.debug("Converting '"+configDict[name]+"' to '"+typein.__name__+"' for param '"+name+"'")
      except:
        com.Out.debug("Converting '"+configDict[name]+"' to '"+typein.__class__.__name__+"' for param '"+name+"'")
      try:
        if isinstance(typein,tuple):
          new[name] = None
          for x in typein:
            if configDict[name] == x:
              new[name] = configDict[name];break
          if new[name] == None:
            new[name] = typein[0]
            com.Out.error("the value :"+name+":"+configDict[name]+" in section ["+classObj.CONF_NAME+"] is not a option. Chossing '"+str(typein[0])+"'")
        elif typein == int: new[name] = int(configDict[name])
        elif typein == str: new[name] = configDict[name]
        elif typein == bool:
          new[name] = configDict.getboolean(name,None)
        elif typein == list: new[name] = configDict[name].split(",")
        else:
          com.Out.debug("Didn't find for '"+name+":"+configDict[name]+"' basic class entry '"+typein.__name__+"'")
          new[name] = typein(configDict[name])
      except ValueError:
        com.Out.error("Convertion impossible for config file: "+name+":"+configDict[name]+" in section ["+classObj.CONF_NAME+"] can't become a "+typein.__name__)
        new[name] = configDict[name]
        exit()
  return new