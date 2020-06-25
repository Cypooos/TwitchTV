from __future__ import print_function
import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

import output.log

class GoogleCalendarAgent():

  SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']

  def __init__(self,secret_file,pickle_file):
    creds = None
    if os.path.exists(pickle_file):
      with open(pickle_file, 'rb') as token:
        creds = pickle.load(token)
    if not creds or not creds.valid:
      if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
      else:
        self.flow = InstalledAppFlow.from_client_secrets_file(secret_file, self.SCOPES)
        creds = self.flow.run_local_server(port=0)
      # save flow obj
      with open(pickle_file, 'wb') as token:
        pickle.dump(creds, token)
    # start the service
    self.service = build('calendar', 'v3', credentials=creds)

  def getEvents(self):
    
    now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
    print('Getting the upcoming 10 events')
    events_result = self.service.events().list(calendarId='primary', timeMin=now,maxResults=10, singleEvents=True,orderBy='startTime').execute()
    events = events_result.get('items', [])

    if not events:
      print('No upcoming events found.')
    for event in events:
      start = event['start'].get('dateTime', event['start'].get('date'))
      print(start, event['summary'])



