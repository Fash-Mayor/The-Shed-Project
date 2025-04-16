from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.filechooser import FileChooserIconView
from kivy.uix.popup import Popup
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window

from PyPDF2 import PdfReader
import os

class PDFSearchApp(App):
    def build(self):
        self.extracted_text = ""
        self.selected_pdf_path = ""

        layout = BoxLayout(orientation='vertical', padding=10)

        self.file_label = Label(text="No PDF selected")
        file_chooser_button = Button(text="Select PDF", on_press=self.show_file_chooser)

        self.search_input = TextInput(hint_text="Enter word or sentence to search")
        search_button = Button(text="Search", on_press=self.perform_search)

        self.result_count_label = Label(text="Occurrences: 0")
        self.result_location_label = Label(text="Found on lines:")
        self.result_lines_layout = GridLayout(cols=1, size_hint_y=None)
        self.result_lines_layout.bind(minimum_height=self.result_lines_layout.setter('height'))
        self.scroll_view = ScrollView(size_hint_y=0.5)
        self.scroll_view.add_widget(self.result_lines_layout)

        layout.add_widget(self.file_label)
        layout.add_widget(file_chooser_button)
        layout.add_widget(self.search_input)
        layout.add_widget(search_button)
        layout.add_widget(self.result_count_label)
        layout.add_widget(self.result_location_label)
        layout.add_widget(self.scroll_view)

        return layout

    def show_file_chooser(self, btn):
        content = FileChooserIconView(on_submit=self.load_pdf, on_cancel=self.dismiss_popup)
        self.popup = Popup(title="Select PDF File", content=content,
                            size_hint=(0.9, 0.9))
        self.popup.open()

    def dismiss_popup(self, instance):
        if self.popup:
            self.popup.dismiss()

    def load_pdf(self, chooser, selection, touch):
        if selection:
            self.selected_pdf_path = selection[0]
            self.file_label.text = f"Selected PDF: {os.path.basename(self.selected_pdf_path)}"
            self.extracted_text = self.extract_text_from_pdf(self.selected_pdf_path)
        self.dismiss_popup(None)

    def extract_text_from_pdf(self, pdf_path):
        text = ""
        try:
            with open(pdf_path, 'rb') as file:
                reader = PdfReader(file)
                for page_num in range(len(reader.pages)):
                    page = reader.pages[page_num]
                    text += page.extract_text() + "\n"
        except FileNotFoundError:
            return "Error: PDF file not found."
        except Exception as e:
            return f"Error reading PDF: {e}"
        return text

    def perform_search(self, btn):
        search_term = self.search_input.text.lower()
        if not self.extracted_text:
            self.result_count_label.text = "Occurrences: 0"
            self.result_location_label.text = "Found on lines: No PDF loaded."
            self.result_lines_layout.clear_widgets()
            return

        lines = self.extracted_text.lower().splitlines()
        occurrences = 0
        found_lines = []
        line_number = 1

        self.result_lines_layout.clear_widgets() # Clear previous results

        for line in lines:
            if search_term in line:
                occurrences += line.count(search_term)
                found_lines.append(str(line_number))
                line_label = Label(text=f"Line {line_number}: {line[:80]}...") # Show a snippet of the line
                self.result_lines_layout.add_widget(line_label)
            line_number += 1

        self.result_count_label.text = f"Occurrences: {occurrences}"
        if found_lines:
            self.result_location_label.text = "Found on lines:"
            self.scroll_view.scroll_y = 1 # Scroll to the top of the results
        else:
            self.result_location_label.text = "Found on lines: Not found."

        # Adjust scroll view size if needed
        self.result_lines_layout.height = max(self.scroll_view.height, self.result_lines_layout.minimum_height)

if __name__ == '__main__':
    PDFSearchApp().run()