# Voice Control Assistant

A desktop voice assistant built using Python.

## Features

- Voice input
- Text-to-speech responses
- Open Google and YouTube
- Google search by voice
- Tell the current time and date
- Open Notepad, Calculator and Paint
- Take screenshots
- Create a folder
- Open the project folder
- Exit using voice

## Technologies

- Python
- SpeechRecognition
- pyttsx3
- PyAudio
- PyAutoGUI
- Python standard library

## Installation

Open PowerShell in this folder and run:

```bash
pip install -r requirements.txt
```

If PyAudio installation fails on Windows, tell me your Python version and I can give you the exact fix.

## Run

```bash
python assistant.py
```

## Example commands

- "Hello"
- "What is the time?"
- "What is the date?"
- "Open YouTube"
- "Open Google"
- "Search for Python tutorials"
- "Open Notepad"
- "Open Calculator"
- "Open Paint"
- "Take a screenshot"
- "Create folder"
- "Open project folder"
- "Exit"

Note: speech recognition through `recognize_google()` requires an internet connection. Text-to-speech with pyttsx3 works offline.
