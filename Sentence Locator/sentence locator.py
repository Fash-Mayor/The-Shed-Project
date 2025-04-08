import kivy

from kivymd.app import MDApp
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivymd.uix.button.button import MDButtonIcon
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.graphics import Rectangle
from kivy.graphics import Color

from tkinter.filedialog import askopenfile
from threading import Thread
from functools import partial

Window.size = (450, 600)

class SentenceLocatorApp(MDApp):
    #file selection dialogue box for choosing PDF files (only)
    def fileChooser(self, event):
        self.file = askopenfile(mode = "r", filetypes = [("pdf files", "*.pdf")])
        self.pdf_file = self.file.name

        self.locationtext.text = self.pdf_file
        self.locationtext.size_hint = (0.7, 0.11)
    

    def search(self, event):
        self.searchingLabel.text = "==Searching=="


    def build(self):
        layout = RelativeLayout()

        #changing backgroundcolor
        with layout.canvas.before:
            Color(0.8, 0.8, 0.8, 1)
            self.rect = Rectangle(pos = layout.pos, size = layout.size)

            layout.bind(pos = self._update_rect, size = self._update_rect)
        
        #widgets
        self.askopenfileButton = Button(text = "Choose File", size_hint = (None, None), height = 40,
                                        pos_hint = {"center_x": 0.14, "center_y": 0.9}, on_press = self.fileChooser)

        self.locationtext = TextInput(text ="", size_hint = (0.7, 0.07), pos_hint = {"center_x": 0.62, "center_y": 0.9},
                                      disabled = True)
        
        self.instructionLabel = Label(text = "Enter sentence or word to search for:", pos_hint = {"center_x": 0.4, "center_y": 0.8},
                                      font_name = "Tahoma", font_size = 20, bold = True, color = (0, 0, 0, 1))
        
        self.findmeTextbox = TextInput(size_hint = (0.9, 0.31), pos_hint = {"center_x": 0.48, "center_y": 0.6}, font_name = "Tahoma",
                                       font_size = 20)
        
        self.findmeButton = Button(text = "Search", size_hint = (None, None), height = 40, pos_hint = {"center_x": 0.14, "center_y": 0.39},
                                   on_press = self.search)
        
        self.searchingLabel = Label(text = "", size_hint = (1, 1), font_size = 24, font_name = "Tahoma", bold = True, color = (0, 0, 0, 1),
                                    pos_hint = {"center_x": 0.55, "center_y": 0.39})
        
        self.displayresult = TextInput(size_hint = (0.9, 0.31), pos_hint = {"center_x": 0.48, "center_y": 0.19}, font_name = "Tahoma",
                                       font_size = 20, disabled = True)
        

        
        #adding widgets to layout
        layout.add_widget(self.displayresult)
        layout.add_widget(self.searchingLabel)
        layout.add_widget(self.findmeButton)
        layout.add_widget(self.findmeTextbox)
        layout.add_widget(self.instructionLabel)
        layout.add_widget(self.locationtext)
        layout.add_widget(self.askopenfileButton)
        return layout
    
    #changing backgroundcolor according to the resizing of screen. Kinda like responsiveness but for backgroundcolor 
    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size

    
SentenceLocatorApp().run()