import tkinter as tk
from tkinter import ttk,messagebox,filedialog
import asyncio
import edge_tts

# Defining Voices
VOICES=["en-US-AndrewNeural","en-GB-Andy","en-US-Andy","en-GB-Andy","en-US-AvaMultilingualNeural","en-US-AvaNeural"]
async def generate_audio(text,voice,rate,output_file):
    communicate=edge_tts.Communicate(text=text,voice=voice,rate=rate)
    await communicate.save(output_file)
    messagebox.showinfo("Success", "File saved successfully to "+output_file)
#asyncio.run(generate_audio("helo guys",VOICES[0],"+0%","output.mp3"))
root = tk.Tk()
root.title("TTS")
root.geometry("600x400")
#Voice Selection
ttk.Label(root,text="Select Voice:").grid(column=0,row=0,padx=10,pady=10, sticky="w")
voice_var= tk.StringVar(value=VOICES[0])
voice_dropdown = ttk.Combobox(root,textvariable=voice_var,values=VOICES,state="readonly")
voice_dropdown.grid(column=1,row=0,padx=10,pady=10,sticky="ew")

#root.columnconfigure(0,weight=1)
root.columnconfigure(1,weight=3)

#Speed Selection
ttk.Label(root,text="Select Speed Rate:").grid(column=0,row=1,padx=10,pady=10, sticky="w")
speed_var =tk.IntVar(value=0)
speed_slider=ttk.Scale(root,from_=-50,to=50,orient="horizontal",variable=speed_var)
speed_slider.grid(column=1,row=1,padx=10,pady=10,sticky="ew")
# Text Input Box
ttk.Label(root,text="Enter a Text:").grid(column=0,row=2,padx=10,pady=10,sticky="w")
text_box=tk.Text(root,wrap="word")
text_box.grid(column=1,row=2,padx=10,pady=10,sticky="nsew")
root.rowconfigure(2,weight=1)
# file upload button
def on_upload():
    file_path = filedialog.askopenfilename( filetypes=[("Text File","*.txt")])
    if file_path:
        with open(file_path,"r") as f:
            content= f.read()
            text_box.delete("1.0",tk.END)
            text_box.insert("1.0",content)

upload_button=ttk.Button(root,text="Upload Text",command=on_upload)
upload_button.grid(column=1,row=3,padx=10,pady=10,sticky="e")

# Generate audio button
def on_generate_audio():
    voice = voice_var.get()
    rate = speed_var.get()
    text = text_box.get("1.0",tk.END).strip()
    rate_str= f"+{rate}%" if rate>=0 else f"{rate}%"
    if not text:
        messagebox.showwarning("Warning","No Text Provided")
        return
    output_file= filedialog.asksaveasfilename(defaultextension=".mp3",filetypes=[("MP3","*.mp3")])
    if not output_file:
        return
    asyncio.run(generate_audio(text,voice,rate_str,output_file))


generate_button=ttk.Button(root,text="Generate audio ",command=on_generate_audio)
generate_button.grid(column=1,row=4,padx=10,pady=10)
root.mainloop()
