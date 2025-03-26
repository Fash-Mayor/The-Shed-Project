from threading import Thread
import pyaudio
import wave

from kivy.uix.relativelayout import RelativeLayout
from kivy.app import App

from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.graphics import Rectangle
from kivy.graphics import Color

Window.size = (350, 300)

class AudioRecorderApp(App):
    def record_audio(self):
        #set recording parameters
        audio = pyaudio.PyAudio()

        FORMAT = pyaudio.paInt16 #-32768 - +32767

        CHANNELS = 1

        RATE = 44100

        CHUNK = 1024

        #open stream for recording
        stream = audio.open(format = FORMAT, channels = CHANNELS, rate = RATE, frames_per_buffer = CHUNK, input = True)

        #create wave file for saving recording
        wf = wave.open("recording.wave", "wb")
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(audio.get_sample_size(FORMAT))
        wf.setframerate(RATE)

        #start recording
        self.message_label.text = "Recording..."
        #self.record_button.text = "Recording..."
        self.recording_active = True

        while self.recording_active:
            data = stream.read(CHUNK)
            wf.writeframes(data)

        #stop recording
        self.record_button.text = "Record"
        stream.stop_stream()
        stream.close()
        audio.terminate()
        wf.close()

        self.message_label.text = "Recording Saved"
        print("Recording Ended...")

    def start_recording(self, event):
        #thread for recording audio
        self.recording_thread = Thread(target = self.record_audio)
        self.recording_thread.start()

        #enable stop button
        self.stop_buton.disabled = False
        self.record_button.disabled = True

    def stop_recording(self, event):
        self.recording_active = False

        #stop recording thread
        self.recording_thread.join()
        self.recording_thread = None

        #disable the stop button
        self.record_button.disabled = False
        self.stop_buton.disabled = True 

    def build(self):
        layout = RelativeLayout()

        with layout.canvas.before:
            Color(1.8, 0.8, 1.8)
            self.rect = Rectangle(size = layout.size, pos = layout.pos)

            layout.bind(size = self._update_rect, pos = self._update_rect)
 
        self.record_button = Button(text = "Record", pos_hint = {"center_x": 0.5, "center_y": 0.8},
                                    size_hint = (0.4, 0.23), font_name = "verdana", bold = True,
                                    font_size = 30, background_color = (1, 0, 0), on_press = self.start_recording)

        self.stop_buton = Button(text = "Stop Recording", pos_hint = {"center_x": 0.5, "center_y": 0.25},
                                size_hint = (0.7, 0.23), font_name = "Verdana", bold = True, font_size = 24,
                                background_color = (0, 1, 0), disabled = True, on_press = self.stop_recording)
        
        self.message_label = Label(text = "", pos_hint = {"center_x": 0.5, "center_y": 0.5},
                                   font_size = 24, font_name = "Tahoma", bold = True,
                                   color = (1, 0.1, 0.4))

        layout.add_widget(self.message_label)
        layout.add_widget(self.record_button)
        layout.add_widget(self.stop_buton)
        return layout
    
    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size


if __name__ == "__main__":
    AudioRecorderApp().run()