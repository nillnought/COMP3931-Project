#all needed info on tkinter for GUI can be found here:
# https://www.geeksforgeeks.org/python/python-tkinter-tutorial/

import tkinter as tk
from tkinter import filedialog, messagebox
from audioFile import audioFile


class UI:
    def __init__(self, root):
        self.root = root
        self.root.title("AppName")
        self.root.geometry("500x500")
        self.audio = None #initializing

        self.label = tk.Label(root, text="Simple Window", font=("Arial Bold", 20))
        self.label.pack(expand=True)
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)

#some example buttons
        self.import_button = tk.Button(root, text="Import Audio File", command=self.load_file)
        self.import_button.pack(pady=10)

        self.import_button = tk.Button(root, text="Export Audio File", command=self.export_file)
        self.import_button.pack(pady=10)

        self.import_button = tk.Button(root, text="Play", command=self.play_audio)
        self.import_button.pack(pady=10)

    def on_close(self):
        self.root.destroy()

    def load_file(self):
        file_path = filedialog.askopenfilename(
            title="Select a file to open",
            filetypes =[("Audio files", "*.wav *.flac *.ogg *.aiff *.aif")]
        )
        if file_path:
            try:
                self.audio = audioFile(file_path)
                messagebox.showinfo("Loaded", f"Loaded file:\n{file_path}")
            except Exception as e:
                messagebox.showerror("Error", f"Could not load file:\n{e}")

    def play_audio(self):
        if self.audio:
            try:
                self.audio.playSound()
            except Exception as e:
                messagebox.showerror("Error", f"Could not play file:\n{e}")
        else:
            messagebox.showwarning("No file", "Please load a file first!")

    def export_file(self):
        if self.audio:
           file_path = filedialog.asksaveasfilename(
                defaultextension=".wav",
                filetypes=[("WAV files", "*.wav"), ("All files", "*.*")]
            )
        if file_path:
            try:
                self.audio.saveFile(file_path)
                messagebox.showinfo("Saved", f"Saved file as:\n{file_path}")
            except Exception as e:
                messagebox.showerror("Error", f"Could not save file:\n{e}")
        else:
            messagebox.showwarning("No file", "Please load a file first!") 
    
