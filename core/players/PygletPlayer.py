import pyglet

import os

class PygletPlayer():

  CONF_NEED = {
    "Hide":bool
  }
  CONF_NAME = "Pyglet"

  def __init__(self,conf):
    self.conf = conf

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

  import pyglet
  from pyglet.gl import *
  from threading import *

  # REQUIRES: AVBin
  #pyglet.options['audio'] = ('alsa', 'openal', 'silent')
  key = pyglet.window.key

  class main(pyglet.window.Window):
      def __init__ (self):
          super(main, self).__init__(800, 800, fullscreen = False)
          self.x, self.y = 0, 0

          self.player = pyglet.media.Player()
          self.player.queue(pyglet.media.load("programs/emission1/test2.mp4"))
          self.sprites = {'video' : None}

          self.alive = 1

      def on_draw(self):
          self.render()

      def on_close(self):
          self.alive = 0

      def on_mouse_motion(self, x, y, dx, dy):
          pass

      def on_mouse_release(self, x, y, button, modifiers):
          pass

      def on_mouse_press(self, x, y, button, modifiers):
          pass

      def on_mouse_drag(self, x, y, dx, dy, button, modifiers):
          pass

      def on_key_release(self, symbol, modifiers):
          pass

      def on_key_press(self, symbol, modifiers):
          if symbol == 65307: # [ESC]
              self.alive = 0
          elif symbol == key.LCTRL:
              self.player.play()

      def render(self):
          self.clear()

          if self.player.playing:
              if self.sprites['video'] is None:
                  texture = self.player.get_texture()
                  if texture:
                      self.sprites['video'] = pyglet.sprite.Sprite(texture)
              else:
                  self.sprites['video'].draw()

          self.flip()

      def run(self):
          while self.alive == 1:
              self.render()

              # -----------> This is key <----------
              # This is what replaces pyglet.app.run()
              # but is required for the GUI to not freeze
              #
              event = self.dispatch_events()

  x = main()
  x.run()