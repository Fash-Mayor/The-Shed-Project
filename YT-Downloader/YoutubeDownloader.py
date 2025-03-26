from functools import partial
from pytube import YouTube
from pytube.exceptions import RegexMatchError

from kivy.uix.relativelayout import RelativeLayout
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.graphics import Color
from kivy.graphics import Rectangle

Window.size = (500, 600)

class MyApp(App):
    
    def getLinkInfo(self, event): #event, window
        self.link = self.linkinput.text
        try:
            self.yt = YouTube(self.link)

            self.title = str(self.yt.title)
            self.views = str(self.yt.views)
            self.length = str(self.yt.length)

            self.titleLabel.text = self.title
            self.titleLabel.pos_hint = {"center_x" : 0.5, "center_y" : 0.4}

            self.viewsLabel.text = f"Views: {self.views}"
            self.viewsLabel.pos_hint = {"center_x" : 0.5, "center_y" : 0.35}

            self.lengthLabel.text = f"Length: {self.length}"
            self.lengthLabel.pos_hint = {"center_x" : 0.5, "center_y" : 0.3}

            print(f"Title: {self.title}")
            print(f"Views: {self.views}")
            print(f"length: {self.length}")

            self.downloadButton.text = "Download"
            self.downloadButton.pos_hint = {"center_x" : 0.5, "center_y" : 0.2}
            self.downloadButton.size_hint = (0.3, 0.1)

        except RegexMatchError:
            print("Invalid Youtube Link")
        except Exception as e:
            print(f"An error occurred: {e}")


    def download(self, event, layout):
        try:
            self.ys= self.yt.streams.get_highest_resolution()

            print("Downloading...")

            self.ys.download()

            print("Download Complete!")

        except Exception as e:
            print(f"Download error: {e}")

    def build(self):
        layout = RelativeLayout()

        with layout.canvas.before:
            Color(0.8, 0.8, 0.8)
            self.rect = Rectangle(size = layout.size, pos = layout.pos)

        layout.bind(size=self._update_rect, pos=self._update_rect)

        self.img = Image(source = "yt-text-logo.png", size_hint = (.5, .5),
                         pos_hint = {"center_x": 0.5, "center_y": 0.86})
        
        self.youtubelink = Label(text = "Paste Youtube Link:",
                                 pos_hint = {"center_x": 0.5, "center_y": 0.7},
                                 size_hint = (2, 2), font_size = 20, color = (1, 5, 2))
        
        self.linkinput = TextInput(text = "",
                                   pos_hint = {"center_x": 0.5, "center_y": 0.64},
                                   size_hint = (0.85, 0.06), height = 36, font_size = 16, foreground_color = (0, 0, 5),
                                   font_name = "Verdana")
        
        self.linkbutton = Button(text = "Get Link", pos_hint = {"center_x" : 0.5, "center_y": 0.55},
                                 size_hint = (0.2, 0.09), font_name = "Tahoma", font_size = 17,
                                 background_color = [0, 1, 0])
        
        self.linkbutton.bind(on_press = partial(self.getLinkInfo)) #.getLinkInfo, layout

        self.titleLabel = Label(text = "", pos_hint = {"center_x" : 0.5, "center_y" : 20},
                                size_hint = (1, 1), font_size = 20)
        
        self.viewsLabel = Label(text = "", pos_hint = {"center_x" : 0.5, "center_y" : 20},
                                size_hint = (1, 1), font_size = 20)
        
        self.lengthLabel = Label(text = "", pos_hint = {"center_x" : 0.5, "center_y" : 30},
                                 size_hint = (1, 1), font_size = 20)
        
        self.downloadButton = Button(pos_hint = {"center_x" : 0.5, "center_y" : 20},
                                     size_hint = (0.2, 0.1), size = (75, 75), font_name = "Verdana",
                                     bold = True, font_size = 24, background_color =  (1, 1, 0))

        self.downloadButton.bind(on_press = partial(self.download, layout))

        layout.add_widget(self.img)
        layout.add_widget(self.youtubelink)
        layout.add_widget(self.linkinput)
        layout.add_widget(self.linkbutton)
        layout.add_widget(self.titleLabel)
        layout.add_widget(self.viewsLabel)
        layout.add_widget(self.lengthLabel)
        layout.add_widget(self.downloadButton)
        return layout
    
    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size

    
if __name__ == "__main__":
    MyApp().run()

