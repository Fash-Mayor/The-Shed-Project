from kivy.app import App
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.dropdown import DropDown
from kivy.graphics import Rectangle, Color

from kivy.core.window import Window

Window.size = (400, 600)

class UnitConvertorApp(App):

    def build(self):
        layout = RelativeLayout()

        with layout.canvas.before:
            Color(0.6, 0.6, 0.6, 1)
            self.rect = Rectangle(size = layout.size, pos = layout.pos)
            layout.bind(size = self._update_rect, pos = self._update_rect)

        return layout
    
if __name__ == "__main__":
    UnitConvertorApp().run()