# The Shed Project

![TheShedProject.png](The_Shed_Project.png)

![Github last commit](https://img.shields.io/github/last-commit/Fash-Mayor/The-Shed-Project)\
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://GitHub.com/Fash-Mayor/The-Shed-Project/graphs/commit-activity)

## Overview

Hi, welcome to The Shed Project! This repository contains various tools and applications built using the Kivy framework. As a learning project, it serves as a digital workshop where different utilities are built to explore and master Kivy's capabilities. Each tool aims to solve a task.

## Table of Content

- [Overview](#overview)
- [Tools/Apps](#toolsapps)
     - [Project 1 - Audio Recorder](https://github.com/Fash-Mayor/The-Shed-Project?tab=readme-ov-file#audio-recorder)
     - [Project 2 - Mp4 to Mp3 (Audio Extractor)](https://github.com/Fash-Mayor/The-Shed-Project?tab=readme-ov-file#mp4-to-mp3-audio-extractor)
     - [Project 3 - Music Player](https://github.com/Fash-Mayor/The-Shed-Project?tab=readme-ov-file#music-player)
     - [Project 4 - PDF to Audio](https://github.com/Fash-Mayor/The-Shed-Project?tab=readme-ov-file#pdf-to-audio)
     - [Project 5 - Password Generator](https://github.com/Fash-Mayor/The-Shed-Project?tab=readme-ov-file#password-generator)
     - [Project 6 - Sentence Locator](https://github.com/Fash-Mayor/The-Shed-Project?tab=readme-ov-file#sentence-locator)
     - [Project 7](https://github.com/Fash-Mayor/The-Shed-Project?tab=readme-ov-file#project-7)
     - [Project 8](https://github.com/Fash-Mayor/The-Shed-Project?tab=readme-ov-file#project-8)
    - [Project 9](https://github.com/Fash-Mayor/The-Shed-Project?tab=readme-ov-file#project-9)
    - [Project 10](https://github.com/Fash-Mayor/The-Shed-Project?tab=readme-ov-file#project-10)
- [Usage](#usage)
- [Contributing](#contributing)

## Tools/Apps

## Audio Recorder 

**Description:**\
A simple application to record audio using the device's microphone and save it to a file. Using ```pyaudio``` and ```wave``` modules to record the audio and save it to a file in the WAV format.

**Code:**
```python
def record_audio(self):
    #set recording parameters
    audio = pyaudio.PyAudio()

    FORMAT = pyaudio.paInt16 #-32768 to +32767

    CHANNELS = 1

    RATE = 44100

        CHUNK = 1024

    #open stream for recording
    stream = audio.open(format = FORMAT, channels = CHANNELS, rate = RATE,frames_per_buffer = CHUNK, input = True)

    #directory to save recorded audio
    directory = self.get_downloads_path()
    file_name = f"recording{self.recording_counter}.wave"

    #create wave file for saving recording
    wf = wave.open(os.path.join(directory, file_name), "wb")
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(audio.get_sample_size(FORMAT))
    wf.setframerate(RATE)

    #start recording
    self.messageLabel.text = f"Recording..."
    #self.record_button.text = "Recording..."
    self.recording_active = True

    while self.recording_active:
        data = stream.read(CHUNK)
        wf.writeframes(data)

    #stop recording
    self.recordButton.text = "Record"
    stream.stop_stream()
    stream.close()
    audio.terminate()
    wf.close()

    self.messageLabel.text = f"Recording {self.recording_counter} Saved"
    print("Recording Ended...")

    self.recording_counter += 1
```

**Output:**

![app view](./md%20imgs/audioRecorder.png)



## Mp4 to Mp3 (Audio Extractor)

**Description**\
An application that extracts the audio from any selected video in ``.mp4`` or ``.mkv`` format using the ``moviepy`` module and saves it in a ``.mp3`` format in the same directory as the selected video.

**Code**
```python
#extracting audio from video
self.video = VideoFileClip(self.mp4_file)
self.audio = self.video.audio
#basic error handling
try:
    self.audio.write_audiofile(self.mp3_file) #saves audio file to the same directory as the video

    print("Completed Sucessfully")

    self.successLabel.text = "Successfully Extracted"

    self.audio.close()
    self.video.close()
except:
    print("Error Writing Audio. Please Try Again")

    self.errLabel.text = "An Error Occured While Extracting. Please Try Again."
```

**Output**

![app view](./md%20imgs/mp4_mp3.png)



## Music Player

**Description**\
A music player app put together using various kivy modules including ``soundloader``, ``progressbar``, ``slider`` and other python modules like the ``os``, ``time``, and ``random``.

**Code**
```python
self.playButton.disabled = True
    self.stopButton.disabled = False
    self.song_title = self.song_list[random.randrange(0, self.song_count)]
    print(self.song_title)
    self.sound = SoundLoader.load("{}/{}".format(self.music_dir, selfsong_title))
    self.songLabel.text = self.song_title[0:-4]

    jpg_path = os.path.join(self.music_dir, self.songLabel.text + ".jpg")
    png_path = os.path.join(self.music_dir, self.songLabel.text + ".png")
    if os.path.exists(jpg_path):
        self.albumImage.source = jpg_path
    elif os.path.exists(png_path):
        self.albumImage.source = png_path
    else:
        self.albumImage.source = "music_dir/default_album.png"

    self.progressbarEvent = Clock.schedule_interval(self.updateprogressbar, self.sound.length / 60)
    self.timeEvent = Clock.schedule_interval(self.settime, 1)

    self.sound.play()
    self.playingLabel.text = " === Playing === "
    self.stopButton.disabled = False
```

**Output**

![app view](./md%20imgs/musicplayer.png)



## PDF to Audio

**Description**\
This tool converts PDF's into ``.mp3`` audio files with the use of ``PyPDF3``, ``pyttsx3``, and ``pdfplumber`` modules.

**Code**
```python
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
                    engine.save_to_file(finalText, "audiobook.mp3") #saves to the directory where the code is run#how to save to downloads folder??
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
```

**Output**

![app view](./md%20imgs/mp4_mp3.png)



## Password Generator

**Description**\
This app generates a random password of any length between 7 and 95. It uses the ``string`` and ``random`` modules to merge and shuffle ``ascii`` characters then generates a sample of any length inputed by the user.

**Code**
```python
def generatePassword(self, length):
    #code block to generate the password
    upper = string.ascii_uppercase
    lower = string.ascii_lowercase
    symbols = string.punctuation
    numbers = string.digits

    merge = upper + lower + symbols + numbers
    shuffle = random.sample(merge, length)#Cannot generate more than 94 length of password
    password = "".join(shuffle)
    print(f"Password is: {password}")
    self.GeneratingLabel.text = "Generated"
    self.GeneratedPasswordDisplay.text = password
```

**Output**

![app view](./md%20imgs/mp4_mp3.png)



## Sentence Locator

**Description**\
This app helps to locate words or sentences in any uploaded file of ``.docx`` and ``.pdf`` format. Using the ``PyPDF2`` module for extracting texts from ``.pdf`` files and the ``docx`` module for extracting texts from ``.docx`` files. The app will display the number of times the word or sentence appears and what line(s) they can be found.

**Code**
```python
lines = self.text.lower().splitlines()
occurences = 0
found_lines = []
line_number = 1

for line in lines:
    if search_text in line:
        occurences += line.count(search_text)
        found_lines.append(str(line_number))
        self.searchingLabel.text = "==Found=="
    line_number += 1 

self.displayResultCount.text = f"Occurences: {occurences}"
if found_lines:
    self.displayResultLocation.pos_hint = {"center_x": 0.31}
    self.displayResultLocation.text = f"Found on lines: {', '.join(found_lines)}"
else:
    self.displayResultLocation.text = "Found on lines: No lines contain the search term."
```

**Output**

![app view](./md%20imgs/sentenceLocator.png)



## Project 7

**Description**\
This project is about creating a tool for devices. The tool will be used to perform a specific task

**Code**
python

**Output**

![alt text](Project_2.png)



## Project 8

**Description**\
This project is about creating a tool for devices. The tool will be used to perform a specific task

**Code**
python

**Output**

![alt text](Project_2.png)



## Project 9

**Description**\
This project is about creating a tool for devices. The tool will be used to perform a specific task

**Code**
python

**Output**

![alt text](Project_2.png)



## Project 10

**Description**\
This project is about creating a tool for devices. The tool will be used to perform a specific task

**Code**
python

**Output**

![alt text](Project_2.png)

