import asyncio
import requests
from urllib.parse import urljoin
import os
from time import sleep
import core.com as com
"""
CODE PARTIALLY TAKEN FROM https://github.com/EugeneDae/VLC-Scheduler
"""

class VLCError(Exception):
    pass

class VLCConnectionError(VLCError):
  pass

class VLCExitError(VLCError):
  pass

class VLCserverPlayer():

  CONF_NEED = { 
    "Hide":bool,
    "Port":int,
    "Host":str,
    "Pass":str,
    "User":str,
    "Path":str,
    "CmdOptions":list,
  }
  CONF_NAME = "VLCserver"

  def __init__(self,conf):
    self.conf = conf
    self.port = conf["Port"]
    self.serverUrl = 'http://' + self.conf['Host'] + ':' + str(self.conf['Port'])
    self.process = None
    self.session = requests.session()

  def check_connection(self, retries=0):
    for i in range(retries, -1, -1):
      try:
        resp = requests.get(self.serverUrl, timeout=5)
      except requests.exceptions.RequestException as e:
        com.Out.debug('Error='+str(e))
        if i > 0:
          com.Out.warning('Connection fail: '+str(i)+'/'+str(retries+1))
          time.sleep(3)
          continue
      else:
        if 'VideoLAN' in resp.text:
          return True

    raise VLCConnectionError('Failed to connect to the VLC web server.')

  async def start(self):
    try:
      self.check_connection()
    except VLCConnectionError:
      pass
    else:
      com.Out.warning('Found existing VLC instance.')
      return
    
        
    command = [
      self.conf['Path'],
      '--extraintf', 'http',
      '--http-host', self.conf['Host'],
      '--http-port', str(self.conf['Port']),
      '--http-password', self.conf['Pass'],
      '--repeat', '--image-duration', '-1'
    ] + self.conf['CmdOptions']
    com.Out.debug('VLCserver command:'+str(" ".join(command)))
    kwargs = {}
    
    if not "DEBUG" in com.Out.log_levels or not "ALL" in com.Out.log_levels:
      kwargs['stderr'] = asyncio.subprocess.DEVNULL
      kwargs['stdout'] = asyncio.subprocess.DEVNULL
        
    self.process = await asyncio.create_subprocess_exec(*command, **kwargs)
    sleep(1)
    self.check_connection(3)
    return self.process


  def _request(self, path, **kwargs):
    resp = self.session.get(urljoin(self.serverUrl, path), **kwargs)

    if resp.status_code != requests.codes.ok:
      resp.raise_for_status()

    self.session.close()

    return resp
    
  def _command(self, command, params={}):
    params = ('command='+command+'&'+'&'.join('%s=%s' % (k, v) for k, v in params.items()))
      
    return self._request('requests/status.xml', params=params)
    
  def _format_uri(self, uri):
    return uri.replace('=', '%3D')
  
  def status(self):
    return self._request('requests/status.json').json()
    
  def add(self, uri):
    return self._command('in_play', {'input': self._format_uri(uri)})
    
  def enqueue(self, uri):
    return self._command('in_enqueue', {'input': self._format_uri(uri)})
    
  def play(self, uid=None):
    if uid:
      return self._command('pl_play', {'id': self._format_uri(uid)})
    else:
      return self._command('pl_play')
    
  def pause(self):
    return self._command('pl_pause')
    
  def stop(self):
    return self._command('pl_stop')
    
  def next(self):
    return self._command('pl_next')
    
  def previous(self):
    return self._command('pl_previous')
    
  def empty(self):
    return self._command('pl_empty')
    
  def toggle_repeat(self):
    return self._command('pl_repeat')

  def seek(self,time):
    return self._command('seek', {"val":time})
    
  def repeat(self, value=None):
    if value is None:
      return self._command('pl_repeat')
        
    if self.status()['repeat'] != value:
      return self._command('pl_repeat')
