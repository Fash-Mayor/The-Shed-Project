import os
import random

import kivy
import kivymd
from kivymd.app import MDApp
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.button import Button
from kivymd.uix.button import MDIconButton
from kivy.uix.label import Label
from kivy.uix.image import Image

from kivy.clock import Clock
from kivy.core.audio import SoundLoader
from kivy.core.window import Window
from kivy.graphics import Rectangle
from kivy.graphics import Color

Window.size = (400, 600)

class MusicPlayerApp(MDApp):
    def build(self):
        layout = RelativeLayout()

        with layout.canvas.before:
            Color(1.2, 1.9, 0.7, 1)
            self.rect = Rectangle(size = layout.size, pos = layout.pos)
            layout.bind(size = self._update_rect, pos = self._update_rect)

        self.music_dir = "/Users/Fash Mayor/OneDrive/Documents/Getting Started/Lnt/Py/Python Project Apps/The-Shed-Project/Music Player/music_dir"
        self.music_files = os.listdir(self.music_dir)
        #print(self.music_files)

        self.song_list = [x for x in self.music_files if x.endswith(".mp3")]
        print(self.song_list)

        self.song_count = len(self.song_list)
        print(self.song_count)

        self.songLabel = Label(pos_hint = {"center_x": 0.5, "center_y": 0.96},
                               size_hint = (1, 1), font_size = 20, color = (0, 0, 0, 1))
        
        self.albumImage = Image(pos_hint = {"center_x": 0.5, "center_y": 0.55},
                                size_hint = (0.8, 0.75))

        self.playButton = MDIconButton(pos_hint = {"center_x": 0.4, "center_y": 0.05}, 
                                     icon = "play-circle-regular-24.png", on_press = self.playAudio)
        
        self.stopButton = MDIconButton(pos_hint = {"center_x": 0.55, "center_y": 0.05}, 
                                     icon = "pause-circle-regular-24.png", on_press = self.stopAudio, disabled = True)

        layout.add_widget(self.songLabel)
        layout.add_widget(self.albumImage)
        layout.add_widget(self.playButton)
        layout.add_widget(self.stopButton)
        Clock.schedule_once(self.playAudio)
        return layout
    
    def playAudio(self, obj):
        self.song_title = self.song_list[random.randrange(0, self.song_count)]
        print(self.song_title)
        self.sound = SoundLoader.load("{}/{}".format(self.music_dir, self.song_title))
        self.songLabel.text = self.song_title[0:-4]
        self.albumImage.source = "C:/Users/Fash Mayor/OneDrive/Documents/Getting Started/Lnt/Py/Python Project Apps/The-Shed-Project/Music Player/music_dir/gsp Cover.png"
        self.sound.play()
        self.stopButton.disabled = False

    def stopAudio(self, obj):
        self.sound.stop()

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size
    
if __name__ == "__main__":
    MusicPlayerApp().run()