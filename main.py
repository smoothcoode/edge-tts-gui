import edge_tts
import tkinter as tk
from tkinter import ttk  , messagebox  ,filedialog
import asyncio

async  def generate_audio(text,voice,rate,output_file):
    communicate= edge_tts.Communicate(text=text,voice=voice,rate=rate)
    await  communicate.save(output_file)
    messagebox.showinfo("Success", "File saved successfully"+output_file)

#asyncio.run(generate_audio("hello guys","en-US-AndrewNeural","+0%",output_file="hello.mp3"))

root = tk.Tk()
root.title("Text to Speech")
root.geometry("600x400")
# Selection Dropdown
VOICES=["en-US-AndrewNeural","en-US-AriaNeural","en-US-AshTurboMultilingualNeural","en-US-AshleyNeural"
       "en-US-AvaMultilingualNeural","en-US-AvaNeural" ]
ttk.Label(root,text="Select a Voice:").grid(column=0,row=0,padx=10,pady=10,sticky="w")
voice_var=tk.StringVar(value=VOICES[0])
voice_dropdown=ttk.Combobox(root,values=VOICES,textvariable=voice_var,state="readonly")
voice_dropdown.grid(row=0,column=1,padx=10,pady=10,sticky="ew")
root.columnconfigure(1,weight=3)
#Speed Selection Slider
ttk.Label(root,text="Select a speed Rate").grid(row=1,column=0,padx=10,pady=10,sticky="w")
speed_var=tk.IntVar(value=0)
speed_slider=ttk.Scale(root,from_=-50,to=50,orient="horizontal",variable=speed_var)
speed_slider.grid(row=1,column=1,padx=10,pady=10,sticky="ew")

#Text Input Box
ttk.Label(root,text="Enter a text").grid(row=2,column=0,padx=10,pady=10,sticky="w")
text_box=tk.Text(root,wrap="word")
text_box.grid(row=2,column=1,padx=10,pady=10,sticky="ew")
root.rowconfigure(2,weight=1)

#Upload button
def on_upload():
    file_path= filedialog.askopenfilename(filetypes=[("Text File","*.txt")])
    if file_path:
        with open(file_path,"r") as f:
            content= f.read()
            text_box.delete("1.0",tk.END)
            text_box.insert("1.0",content)

upload_button=ttk.Button(root,text="Upload a text",command=on_upload)
upload_button.grid(row=3,column=1,padx=10,pady=10,sticky="e")

#Generate audio button
def on_generate_audio():
    voice=voice_var.get()
    rate=speed_var.get()
    rate_str= f"+{rate}%" if rate>=0 else f"{rate}%"
    text=text_box.get("1.0",tk.END).strip()
    if text=="":
        messagebox.showwarning("Warning","No text Provided")
        return
    output_file=filedialog.asksaveasfilename(defaultextension=".mp3",filetypes=[("MP3","*.mp3")])
    if not output_file:
        return
    asyncio.run(generate_audio(text=text,voice=voice,rate=rate_str,output_file=output_file))

generate_button=ttk.Button(root,text="Generate Audio",command=on_generate_audio)
generate_button.grid(row=4,column=1,padx=10 , pady=10)

root.mainloop()