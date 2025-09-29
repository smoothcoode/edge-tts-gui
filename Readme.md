# 🎙️ Text-to-Speech Application

A **Python-based Text-to-Speech (TTS)** application that combines the power of Microsoft Edge's **neural voices** with an intuitive **graphical user interface (GUI)**.  
This tool allows you to **convert text into natural-sounding speech** and save it as **MP3 audio files**.

![ python tts](https://github.com/smoothcoode/Image/blob/main/tts.png?raw=true)


---

## ✨ Features

- 🎤 **Multiple Voice Options**  
  Choose from various neural voices (US English, British English, Australian English, Canadian English, US Spanish, and more).

- ⚡ **Customizable Speech Rate**  
  Adjust speaking speed from **-50% (slower)** to **+50% (faster)** using a slider.

- 📝 **Flexible Text Input**  
  - Direct text input via the built-in text box  
  - Upload `.txt` files for longer content  

- 💾 **File Export**  
  Save generated speech as **MP3 files** to your preferred location.

- 🖥️ **User-Friendly Interface**  
  Clean and intuitive GUI built with **tkinter**.

![ python tts](https://github.com/smoothcoode/Image/blob/main/ttsgui.png?raw=true)


---

## 🛠️ Requirements

- **Python 3.7+**

### Required Packages:
- [`edge-tts`](https://pypi.org/project/edge-tts/)  
- `tkinter` (usually included with Python installations)

---

## 📦 Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/smoothcoode/edge-tts-gui
   cd edge-tts-gui
2. Install dependencies:

    ```bash
    pip install edge-tts


3. Run the application:

    ```bash
    python main.py


## 🗣️ Available Voices
To list all available voices, run:

    python -m  edge_tts --list-voices
