from kivy.app import App
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.button import Button
from kivy.clock import Clock

from kivy.graphics import Rectangle, Color
from kivy.core.window import Window

from PIL import Image
import cv2
import numpy as np
import pyautogui
#pip install opencv-python, numpy, puautogui

Window.size = (450, 150)

class screenRecorderApp(App):
    def __init__(self):
        super().__init__()
        self.recording_counter = 1 #increamenting the name of recording to prevent overriding

    def recordScreen(self, event):
        img = pyautogui.screenshot()
        frame = np.array(img)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        self.out.write(frame)
        pass

    def toggle_recording(self, event):
        if not self.recording:
            self.out = cv2.VideoWriter(self.output_file, self.fps, self.out, self.recording, self.screen_size)
            self.recording = True

            self.recordButton.text = "Stop Recording"
            Window.minimize()

            Clock.schedule_interval(self.recordScreen, 1/30)

        else:
            self.recording = False
            self.recordButton.text = "Record"
            Clock.unschedule(self.recordScreen)
            self.out.release()
    
        self.recording_counter += 1 #might have to move

    def build(self):
        layout = RelativeLayout()

        self.fourcc = cv2.VideoWriter_fourcc(*"mp4v")
        self.output_file = f"Recording{self.recording_counter}.mp4"
        self.fps = 30
        self.out = None
        self.recording = False
        self.screen_size = (1920, 1080)

        with layout.canvas.before:
            Color(0.8, 0.8, 0.8, 1)
            self.rect = Rectangle(size = layout.size, pos = layout.pos)
            layout.bind(size = self._update_rect, pos = self._update_rect)

        #widget
        self.recordButton = Button(text = "Record", pos_hint = {"center_x": 0.5, "center_y": 0.55}, height = 100,
                                   size_hint = (0.8, None), font_name = "Tahoma", font_size = 45, bold = True,
                                   background_color = (1, 1, 0, 1), on_press = self.toggle_recording)

        #adding widget to layout
        layout.add_widget(self.recordButton)
        return layout
    
    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size
    
if __name__ == "__main__":
    screenRecorderApp().run()
