import PyPDF3
import pyttsx3
import pdfplumber

from kivy.uix.relativelayout import RelativeLayout
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.graphics import Rectangle
from kivy.graphics import Color

from threading import Thread
from tkinter.filedialog import askopenfile

#size of the app window
Window.size = (500, 600)

#main class
class PDF2AudioApp(App):
    #function that does the conversion
    def convertToAudio(self):
        self.successErrlabel.text = ""
        #error handling while converting
        try:
            book = open(self.pdf_file, "rb")
            pdfReader = PyPDF3.PdfFileReader(book)

            pages = pdfReader.numPages

            finalText = ""

            try:        
                self.successErrlabel.text = "Extracting text..."
                self.successErrlabel.pos_hint = {"center_x": 0.5, "center_y": 0.23}
                with pdfplumber.open(self.pdf_file) as pdf:
                    for i in range(0, pages):
                        page = pdf.pages[i]
                        text = page.extract_text()
                        finalText += text

                self.successErrlabel.text = ""
                self.successErrlabel.text = "Successfully Extracted the Text"
                self.successErrlabel.pos_hint = {"center_x": 0.5, "center_y": 0.23}

                try:
                    self.successErrlabel.text = ""
                    self.successErrlabel.text = "Converting...please wait"
                    self.successErrlabel.pos_hint = {"center_x": 0.5, "center_y": 0.23}                    
                    
                    engine = pyttsx3.init()
                    engine.save_to_file(finalText, "") #how to save to downloads folder??
                    engine.runAndWait()

                    self.successErrlabel.text = ""
                    self.successErrlabel.text = "Successfully Converted"
                    self.successErrlabel.pos_hint = {"center_x": 0.5, "center_y": 0.23}
                    
                except:
                    self.successErrlabel.text = "Problem converting...Please try again"
                    self.successErrlabel.pos_hint = {"center_x": 0.5, "center_y": 0.23}
            except:
                self.successErrlabel.text = "Problem extracting the text"
                self.successErrlabel.pos_hint = {"center_x": 0.5, "center_y": 0.23}

        except:
            self.successErrlabel.text = "Problem opening the pdf file"
            self.successErrlabel.pos_hint = {"center_x": 0.5, "center_y": 0.23}

    #Starting a Thread for the conversion process
    def convertToAudioThread(self, event):
        thread1 = Thread(target = self.convertToAudio)
        thread1.start() #starts the thread

    #file selection dialogue box for choosing PDF files (only)
    def fileChooser(self, event):
        self.file = askopenfile(mode = "r", filetypes = [("pdf files", "*.pdf")])
        self.pdf_file = self.file.name

        self.locationLabel.text = self.pdf_file
        self.locationLabel.pos_hint = {"center_x": 0.25, "center_y": 0.43}
        
        self.convertButton.pos_hint = {"center_x": 0.5, "center_y": 0.35}

    #main build function
    def build(self):
        layout = RelativeLayout()

        #changing the background color
        with layout.canvas.before:
            Color(0.5, 0.1, 0.4)
            self.rect = Rectangle(size = layout.size, pos = layout.pos)
            layout.bind(size = self._update_rect, pos = self._update_rect)

        #Creating the widgets(image, file chooser, select button, location label, convert button, success & error label)
        self.img = Image(source = "The-Juicebox.jpg", size_hint = (0.5, 0.7),
                         pos_hint = {"center_x": 0.5, "center_y": 0.75})

        self.fileChooserLabel = Label(text = "Select PDF to Convert",
                                      pos_hint = {"center_x": 0.3, "center_y": 0.5},
                                      size_hint = (1, 1), font_size = 20)
        
        self.select_button = Button(text = "Select", size_hint = (None, None), pos_hint = {"center_x": 0.63, "center_y": 0.5},
                                    height = 40, on_press = self.fileChooser)

        self.locationLabel = Label(text = "", pos_hint = {"center_x": 0.25, "cenyer_y": 20},
                                   size_hint = (1, 1), font_size = 20, color = (0, 0, 1))

        self.convertButton = Button(text = "Convert", pos_hint = {"center_x": 0.2, "center_y": 20},
                                    size_hint = (0.2, 0.1), size = (75, 75), font_name = "Verdana",
                                    bold = True, font_size = 24, background_color = (0, 1, 0.5),
                                    on_press = self.convertToAudioThread)
        
        self.successErrlabel = Label(text = "", pos_hint = {"center_x":0.15, 'center_y': 20},
                                     size_hint = (1, 1), font_size = 20, color = (1, 0, 0))
        
        #Adding the widgets to the layout
        layout.add_widget(self.successErrlabel)
        layout.add_widget(self.convertButton)
        layout.add_widget(self.locationLabel)
        layout.add_widget(self.select_button)
        layout.add_widget(self.fileChooserLabel)
        layout.add_widget(self.img)
        return layout
    
    #Enabling consistent color on the background even when resizing the app
    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size

if __name__ == "__main__":
    PDF2AudioApp().run()