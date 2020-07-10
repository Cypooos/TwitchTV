
import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

import core.com as com

from core.planning.Events import Event

from datetime import datetime

JESUS = datetime(2012, 1, 1)

class GoogleCalendarAgent():

  SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']
  CONF_NEED = {
    "ReloadAccount":bool,
    "BufferSize":int,
    "ShowOnEmpty":str,
    "CalendarName":str,
    "Client_secret_file":str,
    "Client_flow_pickle_file":str,
  }
  CONF_NAME = "GoogleCalendar"

  def __init__(self,CalendarConf):
    
    self.service = None
    self.calendarID = None
    self.conf = None
    self.events = []

    creds = None
    self.conf = CalendarConf
    if os.path.exists(self.conf["Client_flow_pickle_file"]):
      com.Out.debug("Loading credential")
      with open(self.conf["Client_flow_pickle_file"], 'rb') as token:
        creds = pickle.load(token)
    if not creds or not creds.valid:
      if creds and creds.expired and creds.refresh_token:
        com.Out.warning("Creditial have expired, refreshing.")
        creds.refresh(Request())
      else:
        com.Out.warning("Making new Flow (connexion)")
        self.flow = InstalledAppFlow.from_client_secrets_file(self.conf["Client_secret_file"], self.SCOPES)
        creds = self.flow.run_local_server(port=0)
      # save flow obj
      com.Out.debug("Saving credential")
      with open(self.conf["Client_flow_pickle_file"], 'wb') as token:
        pickle.dump(creds, token)
    # start the service
    com.Out.debug("Starting service")
    self.service = build('calendar', 'v3', credentials=creds)
    self.reload()


  
  def reload(self):
    com.Out.info("Reloading calendar...")
    calendars_list = self.service.calendarList().list().execute()['items']
    calendar = next((x for x in calendars_list if x['summary'] == self.conf["CalendarName"]), None)
    if calendar == None:
      com.Out.error("No calenders find as '"+str(self.conf["CalendarName"])+"'")
      com.Out.debug("confName = "+str(self.conf["CalendarName"])+", Calendar_list = "+str(calendars_list))
      exit()
    self.calendarID = calendar["id"]
    com.Out.debug("Set calendar as '"+str(self.calendarID)+"'")

  def reloadEvents(self):
    if self.service == None: com.Out.error("getEvent called but service not startup !");exit()
    if self.calendarID == None: com.Out.error("getEvent called but calendarID not setup !");exit()
    now = datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
    com.Out.info('Getting the upcoming '+str(self.conf["BufferSize"])+' events')
    events_result = self.service.events().list(calendarId=self.calendarID, timeMin=now,maxResults=self.conf["BufferSize"], singleEvents=True,orderBy='startTime').execute()
    events = events_result.get('items', [])
    self.events = []

    if not events or events == []:
      com.Out.error("No events find in Google Calendar !")
      com.Out.debug("bufferSize = "+str(self.conf["BufferSize"])+", CalendarID = "+str(self.calendarID))
      #exit()
    for event in events:
      start = event['start'].get('dateTime', None)
      end = event['end'].get('dateTime', None)
      name = event.get('summary',"")
      com.Out.debug("event at "+str(start)+" finish at "+str(end)+" called "+str(name))
      start = datetime.fromisoformat(start)
      end = datetime.fromisoformat(end)
      if name == "": com.Out.error("Event with no title program for time: "+str(start))
      else:
        self.events.append(Event(start,name,end))
        com.Out.debug("Conversion done: "+str(start)+" finish at "+str(end)+" called "+str(name))
    return self.events