import cv2
import numpy as np
from ffpyplayer.player import MediaPlayer
import os
import time

class CV2Player():

  CONF_NEED = {
    "Hide":bool
  }
  CONF_NAME = "CV2"

  def __init__(self,conf):
    self.conf = conf
    self.player = None
    self.cap = None
    self.fps = 30
  
  def setTime(self,time):
    """
    time_length = 60*60.0
    frame_seq = 749
    frame_no = (frame_seq /(time_length*self.fps))
    self.cap.set(cv2.CAP_PROP_POS_FRAMES,frame_no);"""
    self.cap.set(cv2.CAP_PROP_POS_MSEC,time*1000)

  def playF(self,path):
    self.getVideoSource(path,720, 480)
    self.player = MediaPlayer(path)
    prev = time.time()
    start = time.time()
    frame_rate = 30
    while True:
      time_elapsed = time.time() - prev
      if time_elapsed > 1./frame_rate:
        prev = time.time()
        ret, frame = self.cap.read()
        audio_frame, val = self.player.get_frame()

        if val != 'eof' and audio_frame is not None:
          frame, t = audio_frame
        print(frame)
        

        if (ret == 0):
          print("End of video")
          break

        frame = cv2.resize(frame, (720, 480))
        cv2.imshow('Hellow', frame)

        if cv2.waitKey(1) == ord("a"):
          self.setTime(1000)
        elif cv2.waitKey(1) == 27:
          break



    self.cap.release()
    cv2.destroyAllWindows()

  def getVideoSource(self,source, width, height):
    self.cap = cv2.VideoCapture(source)
    self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
    self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
    self.cap.set(cv2.CAP_PROP_FPS, 30)


if __name__ == "__main__":
  t = CV2Player({"Hide":False})
  t.playF("https://storage.googleapis.com/disruptplus_archives/Nature/Nature_Desert.mp4")

