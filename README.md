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
     - [Project 2 - Mp4 to Mp3](https://github.com/Fash-Mayor/The-Shed-Project?tab=readme-ov-file#mp4-to-mp3-audio-extractor)
     - [Project 3 - Music Player](https://github.com/Fash-Mayor/The-Shed-Project?tab=readme-ov-file#music-player)
     - [Project 4 - PDF to Audio](https://github.com/Fash-Mayor/The-Shed-Project?tab=readme-ov-file#pdf-to-audio)
     - [Project 5 - Spotify Downloader](https://github.com/Fash-Mayor/The-Shed-Project?tab=readme-ov-file#spotify-downloader)
     - [Project 6 - Password Generator](https://github.com/Fash-Mayor/The-Shed-Project?tab=readme-ov-file#password-generator)
     - [Project 7 - Sentence Locator](https://github.com/Fash-Mayor/The-Shed-Project?tab=readme-ov-file#sentence-locator)
     - [Project 8 - Youtube Downloader](https://github.com/Fash-Mayor/The-Shed-Project?tab=readme-ov-file#youtube-downloader)
     - [Project 9](https://github.com/Fash-Mayor/The-Shed-Project?tab=readme-ov-file#project-9)
     - [Project 10](https://github.com/Fash-Mayor/The-Shed-Project?tab=readme-ov-file#project-10)

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
        stream = audio.open(format = FORMAT, channels = CHANNELS, rate = RATE, frames_per_buffer = CHUNK, input = True)

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

**Project 1 Output:**

![app view](./md%20imgs/audioRecorder.png)

**Project 1 Lesson:**\
This project is about creating a tool for devices. The tool will be used to perform a specific task

**Project 1 Code Issues Faced:**\
This project is about creating a tool for devices. The tool will be used to perform a specific task


## Mp4 to Mp3 (Audio Extractor)
### Project 2 Description
This project is about creating a tool for devices. The tool will be used to perform a specific task
### Project 2 Code
python
python
python
### Project 2 Output
![alt text](Project_2.png)
### Project 2 Explanation
This project is about creating a tool for devices. The tool will be used to perform a specific task
### Project 2 Conclusion
This project is about creating a tool for devices. The tool will be used to perform a specific task
### Project 2 Code Explanation
This project is about creating a tool for devices. The tool will be used to perform a specific task


## Music Player
### Project 3 Description
This project is about creating a tool for devices. The tool will be used to perform a specific task
### Project 3 Code
python
python
python
### Project 3 Output
![alt text](Project_2.png)
### Project 3 Explanation
This project is about creating a tool for devices. The tool will be used to perform a specific task
### Project 3 Conclusion
This project is about creating a tool for devices. The tool will be used to perform a specific task
### Project 3 Code Explanation
This project is about creating a tool for devices. The tool will be used to perform a specific task


## PDF to Audio
### Project 4 Description
This project is about creating a tool for devices. The tool will be used to perform a specific task
### Project 4 Code
python
python
python
### Project 4 Output
![alt text](Project_2.png)
### Project 4 Explanation
This project is about creating a tool for devices. The tool will be used to perform a specific task
### Project 4 Conclusion
This project is about creating a tool for devices. The tool will be used to perform a specific task
### Project 4 Code Explanation
This project is about creating a tool for devices. The tool will be used to perform a specific task


## Spotify Downloader
### Project 5 Description
This project is about creating a tool for devices. The tool will be used to perform a specific task
### Project 5 Code
python
python
python
### Project 5 Output
![alt text](Project_2.png)
### Project 5 Explanation
This project is about creating a tool for devices. The tool will be used to perform a specific task
### Project 5 Conclusion
This project is about creating a tool for devices. The tool will be used to perform a specific task
### Project 5 Code Explanation
This project is about creating a tool for devices. The tool will be used to perform a specific task


## Password Generator
### Project 6 Description
This project is about creating a tool for devices. The tool will be used to perform a specific task
### Project 6 Code
python
python
python
### Project 6 Output
![alt text](Project_2.png)
### Project 6 Explanation
This project is about creating a tool for devices. The tool will be used to perform a specific task
### Project 6 Conclusion
This project is about creating a tool for devices. The tool will be used to perform a specific task
### Project 6 Code Explanation
This project is about creating a tool for devices. The tool will be used to perform a specific task


## Sentence Locator
### Project 7 Description
This project is about creating a tool for devices. The tool will be used to perform a specific task
### Project 7 Code
python
python
python
### Project 7 Output
![alt text](Project_2.png)
### Project 7 Explanation
This project is about creating a tool for devices. The tool will be used to perform a specific task
### Project 7 Conclusion
This project is about creating a tool for devices. The tool will be used to perform a specific task
### Project 7 Code Explanation
This project is about creating a tool for devices. The tool will be used to perform a specific task


## Youtube Downloader
### Project 8 Description
This project is about creating a tool for devices. The tool will be used to perform a specific task
### Project 8 Code
python
python
python
### Project 8 Output
![alt text](Project_2.png)
### Project 8 Explanation
This project is about creating a tool for devices. The tool will be used to perform a specific task
### Project 8 Conclusion
This project is about creating a tool for devices. The tool will be used to perform a specific task
### Project 8 Code Explanation
This project is about creating a tool for devices. The tool will be used to perform a specific task


## Project 9
### Project 9 Description
This project is about creating a tool for devices. The tool will be used to perform a specific task
### Project 9 Code
python
python
python
### Project 9 Output
![alt text](Project_2.png)
### Project 9 Explanation
This project is about creating a tool for devices. The tool will be used to perform a specific task
### Project 9 Conclusion
This project is about creating a tool for devices. The tool will be used to perform a specific task
### Project 9 Code Explanation
This project is about creating a tool for devices. The tool will be used to perform a specific task


## Project 10
### Project 10 Description
This project is about creating a tool for devices. The tool will be used to perform a specific task
### Project 10 Code
python
python
python
### Project 10 Output
![alt text](Project_2.png)
### Project 10 Explanation
This project is about creating a tool for devices. The tool will be used to perform a specific task
### Project 10 Conclusion
This project is about creating a tool for devices. The tool will be used to perform a specific task
### Project 10 Code Explanation
This project is about creating a tool for devices. The tool will be used to perform a specific task
