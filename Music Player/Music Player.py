import os
import random

import kivy
from kivy.app import App
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.button import Button

from kivy.core.audio import SoundLoader
from kivy.core.window import Window
from kivy.graphics import Rectangle
from kivy.graphics import Color

Window.size = (400, 600)

class MusicPlayerApp(App):
    def build(self):
        layout = RelativeLayout()

        with layout.canvas.before:
            Color(0.2, 0.9, 0.6)
            self.rect = Rectangle(size = layout.size, pos = layout.pos)
            layout.bind(size = self._update_rect, pos = self._update_rect)

        return layout
    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size
    
if __name__ == "__main__":
    MusicPlayerApp().run()