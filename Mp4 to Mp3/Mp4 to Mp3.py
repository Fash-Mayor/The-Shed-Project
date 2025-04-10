from kivy.app import App
from kivy.uix.relativelayout import RelativeLayout

from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.graphics import Rectangle, Color
from kivy.core.window import Window

from threading import Thread
from moviepy import *
from tkinter.filedialog import askopenfile

Window.size = (450, 350)

class Mp4ToMp3App(App):
    def fileChooser(self, event):
    #select the video file to convert
        self.file = askopenfile(mode = "r", filetypes = [("mp4 file", "*.mp4")])
        self.mp4_file = self.file.name
        self.locationtext.text = self.mp4_file
        self.locationtext.size_hint = (0.7, 0.19)
        self.mp3_file = self.mp4_file.replace("mp4", "mp3")

        self.convertButton.disabled = False

    def writeAudio(self):
        #converting the video to audio
        self.video = VideoFileClip(self.mp4_file)
        self.audio = self.video.audio
        #basic error handling
        try:
            self.audio.write_audiofile(self.mp3_file) #saves audio file to the same directory as the video

            print("Completed Sucessfully")

            self.successLabel.text = "Successfully Converted"

            self.audio.close()
            self.video.close()
        except:
            print("Error Writing Audio. Please Try Again")

            self.errLabel.text = "An Error Occured While Converting. Please Try Again."

    def writeAudioThread(self, event):
        #start writeaudiothread
        thread1 = Thread(target = self.writeAudio)
        thread1.start()
        self.successLabel.text = "Converting..."

    def build(self):
        layout = RelativeLayout()

        with layout.canvas.before:
            Color(0.8, 0.8, 0.8, 1)
            self.rect = Rectangle(size = layout.size, pos = layout.pos)
            layout.bind(size = self._update_rect, pos = self._update_rect)

        #widgets
        self.selectfileButton = Button(text = "Choose File", pos_hint = {"center_x": 0.14, "center_y": 0.87},
                                    size_hint = (None, None), height = 40, on_press = self.fileChooser)
        
        self.locationtext = TextInput(text ="", size_hint = (0.7, 0.11), pos_hint = {"center_x": 0.62, "center_y": 0.87},
                                      disabled = True, font_name = "Tahoma")

        self.convertButton = Button(text = "Convert", pos_hint = {"center_x": 0.5, "center_y": 0.66}, size_hint = (None, None),
                                    height = 50, bold = True, font_size = 24, on_press = self.writeAudioThread, disabled = True)

        self.successLabel = Label(text = "", pos_hint = {"center_x": 0.5, "center_y": 0.5}, size_hint = (1, 1),
                                  font_size = 24, color = (0, 0, 0, 1))

        self.errLabel = Label(text = "", pos_hint = {"center_x": 0.5, "center_y": 66}, size_hint = (1, 1),
                              font_size = 24, color = (0, 0, 0, 1))

        #add widgets to layout
        layout.add_widget(self.errLabel)
        layout.add_widget(self.successLabel)
        layout.add_widget(self.convertButton)
        layout.add_widget(self.selectfileButton)
        layout.add_widget(self.locationtext)
        return layout
    
    #changing backgroundcolor according to the resizing of screen. Kinda like responsiveness but for backgroundcolor 
    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size

Mp4ToMp3App().run()