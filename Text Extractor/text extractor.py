from kivy.app import App
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput


from kivy.graphics import Rectangle, Color
from kivy.core.window import Window

from tkinter.filedialog import askopenfile
from PIL import Image
import pytesseract #https://github.com/UB-Mannheim/tesseract/wiki for tesseract exe


Window.size = (500, 500)

class ExttractingTextApp(App):
    def extract_Text(self, event):
        self.path_to_tesseract = r"Tesseract/tesseract.exe"
        path_to_image = self.image_file

        #Point Tesseract_cmd to tesseract.exe
        pytesseract.tesseract_cmd = self.path_to_tesseract

        img = Image.open(path_to_image)

        #Extract tezt from image
        text = pytesseract.image_to_string(img)

        print(text)
        self.imageText.text = text

    def fileChooser(self, event):
        self.file = askopenfile(mode = "r", filetypes = [("images", "*.png *.jpg"), ("png", "*.png"), ("jpg", "*.jpg")])
        self.image_file = self.file.name

        self.locationLabel.text = self.image_file #displaying just the name of file (without the directory)
        self.locationLabel.pos_hint = {"canter_x": 0.5, "center_y": 0.2}

        self.extract_text_button.disabled = False
        self.choose_button.disabled = True

    def build(self):
        layout = RelativeLayout()

        with layout.canvas.before:
            Color(0.8, 0.8, 0.8, 1)
            self.rect = Rectangle(size = layout.size, pos= layout.pos)
            layout.bind(size = self._update_rect, pos = self._update_rect)

        #widgets
        self.imageText = TextInput(text = "", pos_hint ={"center_x": 0.5, "center_y": 0.62},
                                   size_hint = (None, None), height = 340, width = 480,
                                   font_size = 25, foreground_color = (0, 0.5, 0),
                                   font_name = "Tahoma")
        
        self.choose_button = Button(text = "Select File", pos_hint = {"center_x": 0.35, "center_y": 0.07},
                                    size_hint = (0.28, 0.1), font_name = "Verdana", font_size = 24,
                                    background_color = (0, 1, 0), disabled = False,
                                    on_press = self.fileChooser)
        
        self.extract_text_button = Button(text = "Extract", pos_hint = {"center_x": 0.65, "center_y": 0.07},
                                    size_hint = (0.2, 0.1), font_name = "Verdana", font_size = 24,
                                    background_color = (0, 1, 0), disabled = True,
                                    on_press = self.extract_Text)
        
        self.locationLabel = Label(text = "", pos_hint = {"center_x": 0.5, "center_y": 20},
                                   size_hint = (1, 1), font_size = 20, color = (0, 0, 1))
        
        #add widgets to layout
        layout.add_widget(self.imageText)
        layout.add_widget(self.choose_button)
        layout.add_widget(self.extract_text_button)
        layout.add_widget(self.locationLabel)
        return layout
    
    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size
    
if __name__ == "__main__":
    ExttractingTextApp().run()
