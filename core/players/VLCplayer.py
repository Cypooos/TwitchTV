import core.players.vlc as vlc
#import vlc as vlc
import time
#
# instressting for RTMP support : Instance.vlm_add_broadcast()
#

# Instance.vlm_play_media
# Instance.vlm_change_media
# Instance.vlm_pause_media
# Instance.media_new_location
# Instance.playlist_play (not quite usefull ??)

# HCeck doc : https://www.olivieraubert.net/vlc/python-ctypes/doc/vlc.MediaPlayer-class.html

#     player = vlc.MediaPlayer(song) # song = string to file .
#   	player.play()
#
""" BASIC VIDEO PLAY
import vlc
import time
url = "file:///home/rolf/GWPE.mp4" # taking link really this easy ? Nice ^w^

playing = set([1,2,3,4])
instance=vlc.Instance()
player=instance.media_player_new()
media = instance.media_new(url)
media.add_option('start-time=600.00') # 600 seconds (10 minutes)
player.set_media(media)
player.play()
time.sleep(0.1) # wait briefly for it to start
while True:
    state = player.get_state()
    if state not in playing:
        break
"""
#import core.com as com

import os

class VLCplay():

  CONF_NEED = {
    "Hide":bool
  }
  CONF_NAME = "VLC"

  ACTIONS = [
    "playF",
    "playU",
    "setTime",
    "getTime",
    "getMax"
  ]

  def __init__(self,conf):
    self.conf = conf
    self.instance = vlc.Instance()
    self.player=self.instance.media_player_new()


  def playU(self,url,s_time=0.0):
    self.play(url,s_time)
  def playF(self,file,s_time=0.0):
    self.play(file,s_time)

  def play(self,file_url,s_time=0.0):
    self.media = file_url
    media = self.instance.media_new(file_url)
    media.add_option('start-time='+str(s_time))
    self.player.set_media(media)
    self.player.play()
    time.sleep(0.1) # wait briefly for it to start
    while True:
      state = self.player.get_state()
      if state in set([1,2,3,4]):
        break

  def getTime(self):
    return self.player.get_time()

  def getMaxTime(self):
    return self.player.get_length()

  def setTime(self,i_time):
    #self.play(self.media,i_time)
    # for some reason player.set_time have a lot of errors
    self.player.set_position(i_time/self.player.get_length())


if __name__ == "__main__":
  t = VLCplay({"HideVLC":False})
  t.play("https://storage.googleapis.com/disruptplus_archives/Nature/Nature_Desert.mp4",300)
  time.sleep(20)
  t.play("https://storage.googleapis.com/disruptplus_archives/Nature/Nature_waves.mp4",300)
  while True:
    pass