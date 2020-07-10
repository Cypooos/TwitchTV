import inspect, sys, traceback
from time import gmtime, strftime
import colorama
colorama.init()

class bcolors:
    
    colors = {
    "Default"      : "\033[39m",
    "Black"        : "\033[30m",
    "Red"          : "\033[31m",
    "Green"        : "\033[32m",
    "Yellow"       : "\033[33m",
    "Blue"         : "\033[34m",
    "Magenta"      : "\033[35m",
    "Cyan"         : "\033[36m",
    "LightGray"    : "\033[37m",
    "DarkGray"     : "\033[90m",
    "LightRed"     : "\033[91m",
    "LightGreen"   : "\033[92m",
    "LightYellow"  : "\033[93m",
    "LightBlue"    : "\033[94m",
    "LightMagenta" : "\033[95m",
    "LightCyan"    : "\033[96m",
    "White"        : "\033[97m"
    }

    @staticmethod
    def colored(string,color):
        if not color in bcolors.colors.keys(): return string
        else:return bcolors.colors[color]+str(string)+'\033[0m'


class Log():

    COLORS = {
        "WARNING":'Yellow',
        "ERROR":'Red',
        "INFO":'Green',
        "TEST":'Blue',
        "DEBUG":"Magenta"
    }

    def __init__(self,**kwargs):
        self.__log_file = kwargs.get("log_file","core/com/log.txt")
        self.log_levels = kwargs.get("log_level",[])
        with open(self.__log_file,"a") as f:
            f.write("\n["+strftime("%Y-%m-%d %H:%M:%S", gmtime())+"]"+" Start\n")
        
    def setLogMode(self,mode):
        if mode.__class__ == list:self.log_levels = mode
    
    def __out(self,message,log_type):
        stack = inspect.stack()
        modCaller = inspect.getmodule(stack[2][0])
        try:
            classCaller = str(stack[2][0].f_locals["self"].__class__)
        except KeyError:
            classCaller = ""
        if classCaller != "": classCaller +=" "
        methodCaller = stack[2][0].f_code.co_name
        log = log_type+" - ["+strftime("%Y-%m-%d %H:%M:%S", gmtime())+"] {"+str(modCaller.__name__)+"} "+str(classCaller)+str(methodCaller)+": "+str(message)
        if log_type in self.log_levels or "ALL" in self.log_levels:
            if log_type in self.COLORS.keys():
                print("["+bcolors.colored(log_type, self.COLORS[log_type])+"] "+str(message).replace("\n","\\n"))
            else:
                print(("["+str(log_type)+"] "+str(message)).replace("\n","\\n"))
        with open(self.__log_file,"a") as f:
            f.write(log+"\n")

    def read(self,nbLines):
        f = open(self.__log_file,"r")
        ret = f.readlines()
        f.close()
        return ret[-nbLines:-1]
        

    def debug(self,message):self.__out(message,"DEBUG")
    def info(self,message):self.__out(message,"INFO")
    def test(self,message):self.__out(message,"TEST")
    def warning(self,message):self.__out(message,"WARNING")
    def error(self,message):self.__out(message,"ERROR")
    def custom(self,message,logName):self.__out(message,logName)

    def betterCrash(self,exception="none"):
        exc_type, exc_value, exc_traceback = sys.exc_info()
        self.debug("--- Traceback at log ---")
        for a,b,c,d in traceback.extract_tb(exc_traceback):
            self.debug("in method "+str(c)+" line "+str(b)+" of'"+str(a)+"': "+str(d))
        self.debug("Message: \""+str(exception)+"\" in method "+str(traceback.extract_tb(exc_traceback)[-1][2]))


