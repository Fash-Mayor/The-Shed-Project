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

        self.music_dir = "/Users/Fash Mayor/OneDrive/Documents/Getting Started/Lnt/Py/Python Project Apps/The-Shed-Project/Music Player/music_dir"
        self.music_files = os.listdir(self.music_dir)
        #print(self.music_files)

        self.song_list = [x for x in self.music_files if x.endswith(".mp3")]
        # print(self.song_list)

        self.song_count = len(self.song_list)
        print(self.song_count)

        self.playButton = MDIconButton(pos_hint = {"center_x": 0.4, "center_y": 0.05}, 
                                     icon = "play-circle-regular-24.png", on_press = self.playAudio)
        
        self.pauseButton = MDIconButton(pos_hint = {"center_x": 0.55, "center_y": 0.05}, 
                                     icon = "pause-circle-regular-24.png", on_press = self.stopAudio)


        layout.add_widget(self.playButton)
        layout.add_widget(self.pauseButton)
        return layout
    
    def playAudio(self, obj):
        self.song_title = self.song_list[random.randrange(0, self.song_count)]
        print(self.song_title)
        self.sound = SoundLoader.load("{}/{}".format(self.music_dir, self.song_title))
        self.sound.play()

    def stopAudio(self, obj):
        self.sound.stop()

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size
    
if __name__ == "__main__":
    MusicPlayerApp().run()