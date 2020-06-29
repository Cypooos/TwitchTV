import cv2

import os

class CV2Player():

  CONF_NEED = {
    "Hide":bool
  }
  CONF_NAME = "VLC"

  def __init__(self,conf,eventManager):
    self.conf = conf
    self.eventManager = eventManager

  def launch(self):
    self.window= pyglet.window.Window()
    self.player = pyglet.media.Player()
    self.source = pyglet.media.StreamingSource()
    pyglet.app.run()


  def play(self,file,i_time=0.0):
    cap = cv2.VideoCapture('tree.mp4') 

  def setTime(self,i_time):
    pass

if __name__ == "__main__":
  while True:
    pass

