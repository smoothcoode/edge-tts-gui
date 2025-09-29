import asyncio
import edge_tts
import tkinter as tk
from tkinter import ttk, messagebox, filedialog

# Define available voices
VOICES = [
    'en-US-AndrewNeural', 'es-US-AlonsoNeural', 'en-GB-RyanNeural',
    'en-AU-WilliamNeural', 'en-CA-ClaraNeural', 'en-CA-LiamNeural',] # get the full list with this command: python -m  edge_tts --list-voices

async def generate_audio(text, voice, rate, output_file):
    communicate = edge_tts.Communicate(text, voice, rate=rate)
    await communicate.save(output_file)
    messagebox.showinfo("Success", f"Audio saved to {output_file}")

def on_generate_audio():
    voice = voice_var.get()
    rate = speed_var.get()
    # Ensure rate is formatted correctly with a '+' or '-' prefix
    rate_str = f"+{rate}%" if rate >= 0 else f"{rate}%"
    text = text_box.get("1.0", tk.END).strip()
    
    if not text:
        messagebox.showwarning("Warning", "Please enter or upload text.")
        return

    # Prompt the user to choose the file name and location
    output_file = filedialog.asksaveasfilename(defaultextension=".mp3", filetypes=[("MP3 files", "*.mp3")])
    if not output_file:  # If the user cancels the dialog
        return
    
    # Run the TTS generation asynchronously
    loop = asyncio.get_event_loop()
    loop.run_until_complete(generate_audio(text, voice, rate_str, output_file))

def on_upload_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if file_path:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            text_box.delete("1.0", tk.END)
            text_box.insert(tk.END, content)

# Set up the tkinter GUI
root = tk.Tk()
root.title("Text-to-Speech Controller")

# Configure grid to expand widgets when resized
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=3)
root.rowconfigure(2, weight=1)

# Voice selection
ttk.Label(root, text="Select Voice:").grid(row=0, column=0, padx=10, pady=10, sticky="w")
voice_var = tk.StringVar(value=VOICES[0])
voice_dropdown = ttk.Combobox(root, textvariable=voice_var, values=VOICES, state="readonly")
voice_dropdown.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

# Speed selection (Rate slider)
ttk.Label(root, text="Select Speed (Rate):").grid(row=1, column=0, padx=10, pady=10, sticky="w")
speed_var = tk.IntVar(value=-1)  # Default rate of -1%
speed_slider = ttk.Scale(root, from_=-50, to=50, variable=speed_var, orient="horizontal")
speed_slider.grid(row=1, column=1, padx=10, pady=10, sticky="ew")

# Text input box
ttk.Label(root, text="Enter Text:").grid(row=2, column=0, padx=10, pady=10, sticky="nw")
text_box = tk.Text(root, wrap="word")
text_box.grid(row=2, column=1, padx=10, pady=10, sticky="nsew")

# File upload button
upload_button = ttk.Button(root, text="Upload Text File", command=on_upload_file)
upload_button.grid(row=3, column=1, pady=10, sticky="e")

# Generate audio button
generate_button = ttk.Button(root, text="Generate Audio", command=on_generate_audio)
generate_button.grid(row=4, column=0, columnspan=2, pady=20)

root.mainloop()