import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.graphics import Color, Rectangle
from kivy.clock import Clock

import re
import subprocess
import os
import threading

# Minimum Kivy version
kivy.require('2.0.0')

class SpotDownloaderApp(App):
    def build(self):
        Window.size = (400, 300)
        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        with self.layout.canvas.before:
            Color(0.2, 0.2, 0.2, 1)  # Dark background
            self.rect = Rectangle(size=Window.size, pos=(0, 0))
        Window.bind(on_resize=self.update_bg_rect)

        self.link_input = TextInput(hint_text='Enter Spotify Link', multiline=False)
        self.download_button = Button(text='Download Song', on_press=self.process_spotify_link)
        self.status_label = Label(text='', color=(1, 1, 1, 1))

        self.layout.add_widget(self.link_input)
        self.layout.add_widget(self.download_button)
        self.layout.add_widget(self.status_label)

        # Check for required dependencies at startup
        self.check_dependencies()

        return self.layout

    def update_bg_rect(self, *args):
        self.rect.size = Window.size

    def check_dependencies(self):
        """Check if yt-dlp and ffmpeg are available"""
        try:
            subprocess.run(['yt-dlp', '--version'], 
                         stdout=subprocess.PIPE, 
                         stderr=subprocess.PIPE,
                         check=True)
        except (subprocess.CalledProcessError, FileNotFoundError):
            self.status_label.text = 'Warning: yt-dlp not installed. Downloads will fail.'

    def process_spotify_link(self, instance):
        spotify_link = self.link_input.text.strip()
        if not spotify_link:
            self.status_label.text = 'Please enter a Spotify link'
            return

        self.status_label.text = 'Processing Spotify link...'
        self.download_button.disabled = True  # Disable button during download

        # Run the download in a separate thread to keep UI responsive
        threading.Thread(target=self._process_spotify_link_thread, args=(spotify_link,), daemon=True).start()

    def _process_spotify_link_thread(self, spotify_link):
        # 1. Parse Spotify Link to get Track ID
        track_id_match = re.search(r'track/([a-zA-Z0-9]+)', spotify_link)
        if not track_id_match:
            Clock.schedule_once(lambda dt: self._update_status('Invalid Spotify Link'))
            return

        track_id = track_id_match.group(1)
        Clock.schedule_once(lambda dt: self._update_status(f'Extracted Track ID: {track_id}, Searching YouTube...'))

        # 2. Construct YouTube search query
        # In a real app, you would use the Spotify API to get better metadata
        search_query = f"spotify track {track_id}"
        self.download_from_youtube(search_query)

    def download_from_youtube(self, query):
        # Try multiple possible download locations
        possible_download_folders = [
            os.path.join(os.path.expanduser("~"), "Downloads"),
            os.path.join(os.path.expanduser("~"), "downloads"),
            os.getcwd()  # Fallback to current directory
        ]

        downloads_folder = None
        for folder in possible_download_folders:
            if os.path.exists(folder) and os.access(folder, os.W_OK):
                downloads_folder = folder
                break

        if downloads_folder is None:
            Clock.schedule_once(lambda dt: self._update_status('Error: No writable download folder found'))
            return

        # Create the folder if it doesn't exist
        os.makedirs(downloads_folder, exist_ok=True)
        output_path = os.path.join(downloads_folder, '%(title)s.%(ext)s')

        try:
            command = [
                'yt-dlp',
                '-x',                     # Extract audio
                '--audio-format', 'mp3',   # Convert to MP3
                '--ffmpeg-location', 'ffmpeg',  # Explicit ffmpeg location
                '--no-playlist',           # Only download single video
                '--format', 'bestaudio',   # Best audio quality
                '--restrict-filenames',    # Avoid special characters in filename
                '-o', output_path,
                'ytsearch1:' + query       # Search YouTube for the top result
            ]

            Clock.schedule_once(lambda dt: self._update_status('Starting download...'))
            
            process = subprocess.Popen(command, 
                                     stdout=subprocess.PIPE, 
                                     stderr=subprocess.PIPE,
                                     universal_newlines=True)
            stdout, stderr = process.communicate()

            if process.returncode == 0:
                # Verify file was actually created
                downloaded_files = [f for f in os.listdir(downloads_folder) 
                                  if f.endswith('.mp3') and os.path.getsize(os.path.join(downloads_folder, f)) > 0]
                
                if downloaded_files:
                    latest_file = max(downloaded_files, key=lambda f: os.path.getctime(os.path.join(downloads_folder, f)))
                    Clock.schedule_once(lambda dt: self._update_status(f'Download Complete: {latest_file}'))
                else:
                    Clock.schedule_once(lambda dt: self._update_status('Download Failed: No file created'))
            else:
                error_message = stderr.strip()
                if "DRM" in error_message:
                    Clock.schedule_once(lambda dt: self._update_status('Download Failed: DRM protected'))
                elif "429" in error_message:
                    Clock.schedule_once(lambda dt: self._update_status('Download Failed: YouTube rate limit'))
                else:
                    Clock.schedule_once(lambda dt: self._update_status(f'Download Failed: {error_message[:200]}'))

        except FileNotFoundError:
            Clock.schedule_once(lambda dt: self._update_status('Error: yt-dlp or ffmpeg not installed. Please install both.'))
        except Exception as e:
            Clock.schedule_once(lambda dt: self._update_status(f'Error during download: {str(e)}'))
        finally:
            Clock.schedule_once(lambda dt: setattr(self.download_button, 'disabled', False))

    def _update_status(self, message):
        """Thread-safe way to update the status label"""
        self.status_label.text = message

if __name__ == '__main__':
    SpotDownloaderApp().run()