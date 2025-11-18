# all needed info on tkinter for GUI can be found here:
# https://www.geeksforgeeks.org/python/python-tkinter-tutorial/
#for custom tkinter: https://customtkinter.tomschimansky.com/

# import tkinter as tk
import customtkinter as ctk
from customtkinter import filedialog
from audioFile import audioFile
from tkinter import messagebox


class UI(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.audio = None  # initializing

        screen_width = 1200
        screen_height = 600

        self.title("We Tried")
        self.geometry(str(screen_width) + "x" + str(screen_height))

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        self.toolbar_frame = ctk.CTkFrame(self, fg_color="darkblue")
        self.toolbar_frame.grid(row=0, column=0, sticky="nsew")
        self.toolbar_frame.grid_columnconfigure((0 ,1, 2), weight=1)

        toolbar_height = 150

        self.files_frame = ctk.CTkFrame(self.toolbar_frame, height=toolbar_height)
        self.files_frame.grid(row=0, column=0, sticky="nsew")
        self.files_frame.grid_columnconfigure(0, weight=1)
        self.files_frame.grid_rowconfigure((0, 1, 2, 3), weight=1)

        file_button_color = "grey"
        file_button_color_hover = "darkgreen"

        self.close_program_button = ctk.CTkButton(self.files_frame, text="Close Program", command=self.on_close,
                                           fg_color="darkred", hover_color="red")
        self.close_program_button.grid(row=0, column=0, sticky="nsew")
        self.import_button = ctk.CTkButton(self.files_frame, text="Import File", command=self.import_file,
                                           fg_color=file_button_color, hover_color=file_button_color_hover)
        self.import_button.grid(row=1, column=0, sticky="nsew")
        self.export_button = ctk.CTkButton(self.files_frame, text="Export File", command=self.export_file,
                                           fg_color=file_button_color, hover_color=file_button_color_hover)
        self.export_button.grid(row=2, column=0, sticky="nsew")
        self.close_button = ctk.CTkButton(self.files_frame, text="Close File", command=self.export_file,
                                           fg_color=file_button_color, hover_color=file_button_color_hover)
        self.close_button.grid(row=3, column=0, sticky="nsew")



        self.filters_frame = ctk.CTkFrame(self.toolbar_frame, fg_color="grey", height=toolbar_height)
        self.filters_frame.grid(row=0, column=1, sticky="ew")
        self.filters_frame.grid_columnconfigure((0, 1, 2), weight=1)
        self.filters_frame.grid_rowconfigure(0, weight=1)

        control_button_width = 10
        control_button_color = "grey"
        control_button_color_hover = "darkgreen"

        self.close_program_button = ctk.CTkButton(self.files_frame, text="Close Program", command=self.on_close,
                                           fg_color="darkred", hover_color="red")



        self.controls_frame = ctk.CTkFrame(self.toolbar_frame, height=toolbar_height)
        self.controls_frame.grid(row=0, column=2, sticky="ew")

        #         self.play_button = tk.Button(self.control_frame, text="Play", command=self.load_file)
        #         self.play_button.pack(side = "left", expand = True, fill = "x")
        #         self.pause_button = tk.Button(self.control_frame, text="Pause", command=self.load_file)
        #         self.pause_button.pack(side = "left", expand = True, fill = "x")
        #         self.replay_button = tk.Button(self.control_frame, text="Replay", command=self.load_file)
        #         self.replay_button.pack(side = "left", expand = True, fill = "x")


        self.graph_frame = ctk.CTkFrame(self, fg_color="darkred")
        self.graph_frame.grid(row=1, column=0, sticky="nsew")

        self.graph_frame.grid_columnconfigure(0, weight=1)
        self.graph_frame.grid_rowconfigure(0, weight=1)

        self.wave_graph = ctk.CTkCanvas(self.graph_frame)
        self.wave_graph.grid(row=0, column=0, sticky="nsew")


# # #some example buttons
# #         self.import_label = tk.Label(root, text="Test Input")
# #         self.import_label.pack(side="left")
# #         self.import_entry = tk.Entry(root,)
# #         self.import_entry.pack(side="left")
# #
# #
# #         self.import_button = tk.Button(root, text="Import Audio File", command=self.load_file)
# #         self.import_button.pack(pady=10)
# #
# #         self.import_button = tk.Button(root, text="Export Audio File", command=self.export_file)
# #         self.import_button.pack(pady=10)
# #
# #         self.import_button = tk.Button(root, text="Play", command=self.play_audio)
# #         self.import_button.pack(pady=10)

    def on_close(self):
        self.destroy()

    def import_file(self):
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

    def export_file(self):
        file_path = None
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

    def close_file(self):
        if self.audio:
            try:
                self.audio = None
            except Exception as e:
                messagebox.showerror("Error", f"Could not close file:\n{e}")
        else:
            messagebox.showwarning("No file", "No file is open!")

    def play_audio(self):
        if self.audio:
            try:
                self.audio.playSound()
            except Exception as e:
                messagebox.showerror("Error", f"Could not play file:\n{e}")
        else:
            messagebox.showwarning("No file", "Please load a file first!")