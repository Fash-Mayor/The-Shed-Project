from kivy.app import App
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.graphics import Rectangle
from kivy.graphics import Color
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
import os

from tkinter import Tk
from tkinter.filedialog import askopenfile
from PyPDF2 import PdfReader

Window.size = (450, 600)

class SentenceLocatorApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.extracted_text = ""
        self.selected_pdf_path = ""

    def fileChooser(self, event):
        # Initialize Tkinter
        root = Tk()
        root.withdraw()  # Hide the main Tkinter window

        # Select the PDF file
        self.file = askopenfile(mode="r", filetypes=[("PDF files", "*.pdf")])

        # Destroy the Tkinter root after use
        root.destroy()

        if self.file:
            self.selected_pdf_path = self.file.name
            self.locationtext.text = os.path.basename(self.selected_pdf_path)
            self.extracted_text = self.extract_text_from_pdf(self.selected_pdf_path)

    def extract_text_from_pdf(self, pdf_path):
        text = ""
        try:
            with open(pdf_path, 'rb') as file:
                reader = PdfReader(file)
                for page_num in range(len(reader.pages)):
                    page = reader.pages[page_num]
                    text += page.extract_text() + "\n"
        except FileNotFoundError:
            self.update_search_results("Error: PDF file not found.")
            return ""
        except Exception as e:
            self.update_search_results(f"Error reading PDF: {e}")
            return ""
        return text

    def perform_search(self, btn):
        search_term = self.findmeTextbox.text.lower()
        self.update_searching_label("==Searching==")
        self.update_search_results(search_term = search_term)

    def update_searching_label(self, text):
        self.searchingLabel.text = text

    def update_search_results(self, error_message=None, search_term=""):
        self.displayResultCount.text = "Occurrences: 0"
        self.displayResultLocation.text = "Found on lines:"
        self.result_lines_layout.clear_widgets()

        if error_message:
            error_label = Label(text=error_message)
            self.result_lines_layout.add_widget(error_label)
            self.scroll_view.scroll_y = 1
            return

        if not self.extracted_text:
            no_file_label = Label(text="No PDF loaded.")
            self.result_lines_layout.add_widget(no_file_label)
            self.scroll_view.scroll_y = 1
            return

        lines = self.extracted_text.lower().splitlines()
        occurrences = 0
        found_lines = []
        line_number = 1

        for line in lines:
            if search_term in line:
                occurrences += line.count(search_term)
                found_lines.append(str(line_number))
                line_label = Label(text=f"Line {line_number}: {line[:80]}...")
                self.result_lines_layout.add_widget(line_label)
            line_number += 1

        self.displayResultCount.text = f"Occurrences: {occurrences}"
        if found_lines:
            self.displayResultLocation.text = "Found on lines:"
            self.scroll_view.scroll_y = 1
        else:
            no_match_label = Label(text="No lines contain the search term.")
            self.result_lines_layout.add_widget(no_match_label)
            self.scroll_view.scroll_y = 1

        self.update_searching_label("==Found==" if occurrences > 0 else "")
        self.result_lines_layout.height = max(self.scroll_view.height, self.result_lines_layout.minimum_height)


    def build(self):
        layout = RelativeLayout()

        # changing background color
        with layout.canvas.before:
            Color(0.8, 0.8, 0.8, 1)
            self.rect = Rectangle(pos=layout.pos, size=layout.size)
            layout.bind(pos=self._update_rect, size=self._update_rect)

        # widgets
        self.askopenfileButton = Button(text="Choose File", size_hint=(None, None), height=40,
                                         pos_hint={"center_x": 0.14, "center_y": 0.9}, on_press=self.fileChooser) # Changed back to fileChooser

        self.locationtext = TextInput(text="", size_hint=(0.7, 0.07), pos_hint={"center_x": 0.62, "center_y": 0.9},
                                      disabled=True)

        self.instructionLabel = Label(text="Enter sentence or word to search for:", pos_hint={"center_x": 0.4, "center_y": 0.8},
                                      font_name="Tahoma", font_size=20, bold=True, color=(0, 0, 0, 1))

        self.findmeTextbox = TextInput(size_hint=(0.9, 0.31), pos_hint={"center_x": 0.48, "center_y": 0.6}, font_name="Tahoma",
                                        font_size=20)

        self.findmeButton = Button(text="Search", size_hint=(None, None), height=40, pos_hint={"center_x": 0.14, "center_y": 0.39},
                                   on_press=self.perform_search)

        self.searchingLabel = Label(text="", size_hint=(1, 1), font_size=24, font_name="Tahoma", bold=True, color=(0, 0, 0, 1),
                                     pos_hint={"center_x": 0.55, "center_y": 0.39})

        self.displayResultCount = Label(text="Occurrences: 0", size_hint=(None, None), height=40, bold=True, color=(0, 0, 0, 1),
                                          pos_hint={"center_x": 0.2, "center_y": 0.26}, font_size=25, font_name="Tahoma")

        self.displayResultLocation = Label(text="Found on lines:", size_hint=(None, None), height=40, bold=True, color=(0, 0, 0, 1),
                                             pos_hint={"center_x": 0.217, "center_y": 0.15}, font_size=25, font_name="Tahoma")

        self.result_lines_layout = GridLayout(cols=1, size_hint_y=None)
        self.result_lines_layout.bind(minimum_height=self.result_lines_layout.setter('height'))
        self.scroll_view = ScrollView(size_hint_y=0.5)
        self.scroll_view.add_widget(self.result_lines_layout)

        # adding widgets to layout
        layout.add_widget(self.displayResultLocation)
        layout.add_widget(self.displayResultCount)
        layout.add_widget(self.searchingLabel)
        layout.add_widget(self.findmeButton)
        layout.add_widget(self.findmeTextbox)
        layout.add_widget(self.instructionLabel)
        layout.add_widget(self.locationtext)
        layout.add_widget(self.askopenfileButton)
        layout.add_widget(self.scroll_view) # Add the scroll view

        return layout

    # changing background color according to the resizing of screen. Kinda like responsiveness but for background color
    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size

if __name__ == "__main__":
    SentenceLocatorApp().run()