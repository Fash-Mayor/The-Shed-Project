import os
import random

import kivy
from kivymd.app import MDApp
from kivy.uix.relativelayout import RelativeLayout
from kivymd.uix.button.button import MDIconButton
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.progressbar import ProgressBar

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

        self.music_dir = "/Users/Fash Mayor/OneDrive/Documents/Getting Started/Lnt/Py/Python Project Apps/The-Shed-Project/Music Player/music_dir/"
        self.music_files = os.listdir(self.music_dir)
        #print(self.music_files)

        self.song_list = [x for x in self.music_files if x.endswith(".mp3")]
        print(self.song_list)

        self.song_count = len(self.song_list)
        print(self.song_count)

        self.songLabel = Label(pos_hint = {"center_x": 0.5, "center_y": 0.26},
                               size_hint = (1, 1), font_size = 20, color = (0, 0, 0, 1))
        
        self.albumImage = Image(pos_hint = {"center_x": 0.5, "center_y": 0.65},
                                size_hint = (0.7, 0.55))
        
        self.playingLabel = Label(pos_hint = {"center_x": 0.5, "center_y": 0.33},
                                  size_hint = (1, 1), font_size = 21, color = (0, 0, 0, 1))

        self.progressbar = ProgressBar(max = 100, value = 0, size_hint = (0.8, 0.75),
                                       pos_hint = {"center_x": 0.5, "center_y": 0.19},)

        self.playButton = MDIconButton(pos_hint = {"center_x": 0.42, "center_y": 0.12}, 
                                     icon = "play", on_press = self.playAudio)
        
        self.stopButton = MDIconButton(pos_hint = {"center_x": 0.58, "center_y": 0.12}, 
                                     icon = "pause", on_press = self.stopAudio, disabled = True)

        layout.add_widget(self.playingLabel)
        layout.add_widget(self.songLabel)
        layout.add_widget(self.albumImage)
        layout.add_widget(self.playButton)
        layout.add_widget(self.stopButton)
        layout.add_widget(self.progressbar)

        Clock.schedule_once(self.playAudio)
        self.playingLabel.text = " === Playing === "

        return layout
    
    def playAudio(self, obj):
        self.playButton.disabled = True
        self.stopButton.disabled = False
        self.song_title = self.song_list[random.randrange(0, self.song_count)]
        print(self.song_title)
        self.sound = SoundLoader.load("{}/{}".format(self.music_dir, self.song_title))
        self.songLabel.text = self.song_title[0:-4]

        jpg_path = os.path.join(self.music_dir, self.songLabel.text + ".jpg")
        png_path = os.path.join(self.music_dir, self.songLabel.text + ".png")
        if os.path.exists(jpg_path):
            self.albumImage.source = jpg_path
        elif os.path.exists(png_path):
            self.albumImage.source = png_path
        else:
            self.albumImage.source = "music_dir/default_album.png"

        self.progressbarEvent = Clock.schedule_interval(self.updateprogressbar, self.sound.length / 60)

        self.sound.play()
        self.playingLabel.text = " === Playing === "
        self.stopButton.disabled = False

    def stopAudio(self, obj):
        self.sound.stop()
        self.playButton.disabled = False
        self.stopButton.disabled = True
        self.playingLabel.text = " === Stopped === "

    def updateprogressbar(self, value):
        if self.progressbar.value < 100:
            self.progressbar.value += 1


    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size
    

MusicPlayerApp().run()