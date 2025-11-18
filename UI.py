# all needed info on tkinter for GUI can be found here:
# https://www.geeksforgeeks.org/python/python-tkinter-tutorial/

import tkinter as tk
from tkinter import filedialog, messagebox
from audioFile import audioFile


class UI:
    def __init__(self, root):
        SCREEN_WIDTH = 1200
        SCREEN_HEIGHT = 600


        self.root = root
        self.root.title("AppName")
        self.root.geometry(str(SCREEN_WIDTH) + "x" + str(SCREEN_HEIGHT))
        self.audio = None #initializing

        # self.label = tk.Label(root, text="Simple Window", font=("Arial Bold", 20))
        # self.label.pack(expand=True)
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)


        self.file_frame = tk.Frame(root)
        self.file_frame.pack(fill="x", expand=True)

        self.import_button = tk.Button(self.file_frame, text="Import Audio File", command=self.load_file)
        self.import_button.pack(side = "left", expand = True, fill = "x")
        self.export_button = tk.Button(self.file_frame, text="Export Audio File", command=self.load_file)
        self.export_button.pack(side = "left", expand = True, fill = "x")
        self.close_button = tk.Button(self.file_frame, text="Close File", command=self.on_close)
        self.close_button.pack(side = "left", expand = True, fill = "x")

        self.wave_graph = tk.Canvas(background="grey", width=SCREEN_WIDTH)
        self.wave_graph.pack(fill="both", expand=True)


        self.control_frame = tk.Frame(root)
        self.control_frame.pack(fill="x", expand=True)

        self.play_button = tk.Button(self.control_frame, text="Play", command=self.load_file)
        self.play_button.pack(side = "left", expand = True, fill = "x")
        self.pause_button = tk.Button(self.control_frame, text="Pause", command=self.load_file)
        self.pause_button.pack(side = "left", expand = True, fill = "x")
        self.replay_button = tk.Button(self.control_frame, text="Replay", command=self.load_file)
        self.replay_button.pack(side = "left", expand = True, fill = "x")

# #some example buttons
#         self.import_label = tk.Label(root, text="Test Input")
#         self.import_label.pack(side="left")
#         self.import_entry = tk.Entry(root,)
#         self.import_entry.pack(side="left")
#
#
#         self.import_button = tk.Button(root, text="Import Audio File", command=self.load_file)
#         self.import_button.pack(pady=10)
#
#         self.import_button = tk.Button(root, text="Export Audio File", command=self.export_file)
#         self.import_button.pack(pady=10)
#
#         self.import_button = tk.Button(root, text="Play", command=self.play_audio)
#         self.import_button.pack(pady=10)

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

