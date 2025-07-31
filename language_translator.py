# Install required libraries:
# pip install googletrans==4.0.0-rc1
# pip install gTTS
# pip install playsound

import tkinter as tk
from tkinter import ttk, messagebox
from googletrans import Translator, LANGUAGES
from gtts import gTTS
import playsound
import os

# Function to translate
def translate_text():
    text = text_input.get("1.0", tk.END).strip()
    src_lang = source_lang.get()
    tgt_lang = target_lang.get()
    if text == "":
        messagebox.showwarning("Warning", "Please enter text to translate!")
        return
    translator = Translator()
    translated = translator.translate(text, src=src_lang, dest=tgt_lang)
    text_output.delete("1.0", tk.END)
    text_output.insert(tk.END, translated.text)

# Function to copy translated text
def copy_text():
    translated = text_output.get("1.0", tk.END).strip()
    root.clipboard_clear()
    root.clipboard_append(translated)
    messagebox.showinfo("Copied", "Translated text copied to clipboard!")

# Function to speak translated text
def speak_text():
    translated = text_output.get("1.0", tk.END).strip()
    if translated == "":
        messagebox.showwarning("Warning", "Nothing to speak!")
        return
    tts = gTTS(translated)
    tts.save("temp.mp3")
    playsound.playsound("temp.mp3")
    os.remove("temp.mp3")

# Setup window
root = tk.Tk()
root.title("Language Translator Tool")
root.geometry("600x500")
root.resizable(False, False)

# Source & Target language dropdowns
lang_list = list(LANGUAGES.keys())

ttk.Label(root, text="Source Language:").pack(pady=5)
source_lang = ttk.Combobox(root, values=lang_list)
source_lang.set("en")
source_lang.pack()

ttk.Label(root, text="Target Language:").pack(pady=5)
target_lang = ttk.Combobox(root, values=lang_list)
target_lang.set("fr")
target_lang.pack()

# Text input box
ttk.Label(root, text="Enter Text:").pack(pady=5)
text_input = tk.Text(root, height=7, width=70)
text_input.pack()

# Translate button
translate_button = ttk.Button(root, text="Translate", command=translate_text)
translate_button.pack(pady=10)

# Output text box
ttk.Label(root, text="Translated Text:").pack(pady=5)
text_output = tk.Text(root, height=7, width=70)
text_output.pack()

# Copy & Speak buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

copy_button = ttk.Button(button_frame, text="Copy", command=copy_text)
copy_button.pack(side=tk.LEFT, padx=10)

speak_button = ttk.Button(button_frame, text="Speak", command=speak_text)
speak_button.pack(side=tk.LEFT, padx=10)

root.mainloop()
