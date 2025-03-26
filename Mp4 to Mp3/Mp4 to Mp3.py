from threading import Thread
from moviepy import *
from tkinter.filedialog import askopenfile

from kivy.uix.relativelayout import RelativeLayout
from kivy.app import App

from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.graphics import Rectangle
from kivy.graphics import Color

from kivy.core.window import Window

Window.size = (500, 600)

class Mp4ToMp3App(App):
    def fileChooser(self, event):
        self.file = askopenfile(mode = "r", filetypes = [("mp4 file", "*.mp4")])
        self.mp4_file = self.file.name
        self.mp3_file = self.mp4_file.replace("mp4", "mp3")

        self.locationLabel.text = self.mp4_file
        self.locationLabel.pos_hint = {"center_x": 0.5, "center_y": 0.5}

        self.convertButton.pos_hint = {"center_x": 0.5, "center_y": 0.35}

    def writeAudio(self):
        self.video = VideoFileClip(self.mp4_file)
        self.audio = self.video.audio
        try:
            self.audio.write_audiofile(self.mp3_file)

            print("Completed Sucessfully")

            self.successLabel.text = "Successfully Converted"
            self.successLabel.pos_hint = {"center_x": 0.5, "center_y": 0.2}

            self.audio.close()
            self.video.close()
        except:
            print("Error Writing Audio. Please Try Again")

            self.errLabel.text = "An Error Occured While Converting. Please Try Again."
            self.errLabel.pos_hint = {"center_x": 0.5, "center_y": 0.2}

    def writeAudioThread(self, event):
        thread1 = Thread(target = self.writeAudio)
        thread1.start()

    def build(self):
        layout = RelativeLayout()

        with layout.canvas.before:
            Color(0.8, 0.8, 0.8)
            self.rect = Rectangle(size = layout.size, pos = layout.pos)
            layout.bind(size = self._update_rect, pos = self._update_rect)

        self.img = Image(source = "Creative & Graphics (108).jpg", size_hint = (0.5, 0.5),
                        pos_hint = {"center_x": 0.5, "center_y": 0.85})

        self.fileChooserLabel = Label(text = "Select the video to convert",
                                      pos_hint = {"center_x": 0.4, "center_y": 0.6},
                                      size_hint = (1, 1), font_size = 20, color = (1, 0, 0))

        self.select_button = Button(text = "Select", size_hint = (None, None), pos = (375, 340),
                                    height = 40, on_press = self.fileChooser)
        
        self.locationLabel = Label(text = "", pos_hint = {"center_x": 0.5, "center_y": 20},
                                   size_hint = (1, 1), font_size = 20, color = (1, 0, 0))

        self.convertButton = Button(text = "Convert", pos_hint = {"center_x": 0.5, "center_y": 20},
                                    size_hint = (0.2, 0.1), size = (75, 75), font_name = "Tahoma",
                                    bold = True, font_size = 24, background_color = (0, 1, 0), on_press = self.writeAudioThread)

        self.successLabel = Label(text = "", pos_hint = {"center_x": 0.5, "center_y": 20},
                                   size_hint = (1, 1), font_size = 20, color = (1, 0, 0))

        self.errLabel = Label(text = "", pos_hint = {"center_x": 0.5, "center_y": 20},
                                   size_hint = (1, 1), font_size = 20, color = (1, 0, 0))

        layout.add_widget(self.errLabel)
        layout.add_widget(self.successLabel)
        layout.add_widget(self.convertButton)
        layout.add_widget(self.locationLabel)
        layout.add_widget(self.select_button)
        layout.add_widget(self.fileChooserLabel)
        layout.add_widget(self.img)
        return layout
    
    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size

if __name__ == "__main__":
    Mp4ToMp3App().run()