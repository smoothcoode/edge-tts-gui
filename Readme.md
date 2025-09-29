Text-to-Speech Application
A Python-based Text-to-Speech (TTS) application that combines the power of Microsoft Edge's neural voices with an intuitive graphical user interface. This tool allows you to convert text into natural-sounding speech and save it as MP3 audio files.

Requirements
Python 3.7+
Required packages:
edge-tts
tkinter (usually included with Python)


Features
Multiple Voice Options: Choose from various neural voices including US English, British English, Australian English, Canadian English, and US Spanish

Customizable Speech Rate: Adjust speaking speed from -50% (slower) to +50% (faster) using an intuitive slider

Text Input Flexibility:

Direct text input via text box

Upload text files (.txt) for longer content

File Export: Save generated audio as MP3 files to your preferred location

User-Friendly Interface: Clean and intuitive GUI built with tkinter



Installation
Install the required package:

bash
pip install edge-tts
Download the Python script and run it:

bash
python main.py
Usage
Select Voice: Choose from the available neural voices in the dropdown menu

Adjust Speed: Use the slider to set the speaking rate (-50% to +50%)

Input Text:

Type directly into the text box, OR

Click "Upload Text File" to load text from a .txt file

Generate Audio: Click "Generate Audio" and choose where to save your MP3 file

Enjoy: Your text-to-speech audio will be saved as an MP3 file

Available Voices
The application includes several high-quality neural voices:



Technical Details
Backend: Uses edge-tts library, which leverages Microsoft Edge's TTS service

GUI: Built with Python's built-in tkinter library

Audio Format: Outputs high-quality MP3 files

Async Operations: Uses asyncio for efficient TTS generation
