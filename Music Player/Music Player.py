import os
import random

import kivy
import kivymd
from kivymd.app import MDApp
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.button import Button
from kivymd.uix.button import MDIconButton

from kivy.core.audio import SoundLoader
from kivy.core.window import Window
from kivy.graphics import Rectangle
from kivy.graphics import Color

Window.size = (400, 600)

class MusicPlayerApp(MDApp):
    def build(self):
        layout = RelativeLayout()

        with layout.canvas.before:
            Color(0.2, 0.9, 0.6)
            self.rect = Rectangle(size = layout.size, pos = layout.pos)
            layout.bind(size = self._update_rect, pos = self._update_rect)

        self.playButton = MDIconButton(pos_hint = {"center_x": 0.4, "center_y": 0.05}, 
                                     icon = "play-circle-regular-24.png")
        self.pauseButton = MDIconButton(pos_hint = {"center_x": 0.55, "center_y": 0.05}, 
                                     icon = "pause-circle-regular-24.png")


        layout.add_widget(self.playButton)
        layout.add_widget(self.pauseButton)
        return layout

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size
    
if __name__ == "__main__":
    MusicPlayerApp().run()