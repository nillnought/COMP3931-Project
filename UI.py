# all needed info on tkinter for GUI can be found here:
# https://www.geeksforgeeks.org/python/python-tkinter-tutorial/
#for custom tkinter: https://customtkinter.tomschimansky.com/

import tkinter as tk
from tkinter import messagebox
import customtkinter as ctk
from customtkinter import filedialog
from audioFile import audioFile
import filter


class UI(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.audio = None  # initializing
        self.filter = tk.StringVar(value="reverb")

        screen_width = 1200
        screen_height = 600

        toolbar_height = 150

        self.title("We Tried")
        self.geometry(str(screen_width) + "x" + str(screen_height))

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        self.toolbar_frame = ctk.CTkFrame(self, fg_color="darkblue")
        self.toolbar_frame.grid(row=0, column=0, sticky="nsew")
        self.toolbar_frame.grid_columnconfigure((0 ,1, 2), weight=1)


        self.files_frame = FilesFrame(self, toolbar_height)
        self.controls_frame = ControlsFrame(self, toolbar_height)
        self.filters_frame = FiltersFrame(self, toolbar_height)


        self.graph_frame = ctk.CTkFrame(self, fg_color="darkred")
        self.graph_frame.grid(row=1, column=0, sticky="nsew")
        self.graph_frame.grid_columnconfigure(0, weight=1)
        self.graph_frame.grid_rowconfigure((1, 3), weight=1)

        self.graph_label_freq = ctk.CTkLabel(self.graph_frame, fg_color="black", text="Frequency Domain", anchor="w", padx=10)
        self.graph_label_freq.grid(row=0, column=0, sticky="ew")
        self.freq_domain_graph = ctk.CTkCanvas(self.graph_frame)
        self.freq_domain_graph.grid(row=1, column=0, sticky="ew")
        self.graph_label_time = ctk.CTkLabel(self.graph_frame, fg_color="black", text="Time Domain", anchor="w", padx=10)
        self.graph_label_time.grid(row=2, column=0, sticky="ew")
        self.time_domain_graph = ctk.CTkCanvas(self.graph_frame)
        self.time_domain_graph.grid(row=3, column=0, sticky="ew")


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
                self.filters_frame.enable_filters()
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
                self.filters_frame.disable_filters()
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

    def pause_audio(self):
        if self.audio:
            try:
                self.audio.pauseSound()
            except Exception as e:
                messagebox.showerror("Error", f"Could not pause file:\n{e}")
        else:
            messagebox.showwarning("No file", "Please play a file first!")




class FilesFrame(ctk.CTkFrame):
    def __init__(self, master, height):
        super().__init__(master)

        self.files_frame = ctk.CTkFrame(master.toolbar_frame, height=height)
        self.files_frame.grid(row=0, column=0, sticky="nsew")
        self.files_frame.grid_columnconfigure(0, weight=1)
        self.files_frame.grid_rowconfigure((0, 1, 2, 3), weight=1)
        self.files_frame.grid_propagate(False)

        file_button_color = "grey"
        file_button_color_hover = "darkgreen"

        self.close_program_button = ctk.CTkButton(self.files_frame, text="Close Program", command=master.on_close,
                                           fg_color="darkred", hover_color="red")
        self.close_program_button.grid(row=0, column=0, sticky="nsew")
        self.import_button = ctk.CTkButton(self.files_frame, text="Import File", command=master.import_file,
                                           fg_color=file_button_color, hover_color=file_button_color_hover)
        self.import_button.grid(row=1, column=0, sticky="nsew")
        self.export_button = ctk.CTkButton(self.files_frame, text="Export File", command=master.export_file,
                                           fg_color=file_button_color, hover_color=file_button_color_hover)
        self.export_button.grid(row=2, column=0, sticky="nsew")
        self.close_button = ctk.CTkButton(self.files_frame, text="Close File", command=master.export_file,
                                           fg_color=file_button_color, hover_color=file_button_color_hover)
        self.close_button.grid(row=3, column=0, sticky="nsew")

class ControlsFrame(ctk.CTkFrame):
    def __init__(self, master, height):
        super().__init__(master)

        self.controls_frame = ctk.CTkFrame(master.toolbar_frame, height=height)
        self.controls_frame.grid(row=0, column=1, sticky="nsew")
        self.controls_frame.grid_columnconfigure((0, 1), weight=1)
        self.controls_frame.grid_rowconfigure(0, weight=1)
        self.controls_frame.grid_propagate(False)

        control_button_width = 10
        control_button_color = "grey"
        control_button_color_hover = "darkgreen"

        self.play_button = ctk.CTkButton(self.controls_frame, text="Play", command=master.play_audio,
                                         width=control_button_width,
                                         fg_color=control_button_color, hover_color=control_button_color_hover)
        self.play_button.grid(row=0, column=0, sticky="nsew")
        self.pause_button = ctk.CTkButton(self.controls_frame, text="Pause", command=master.pause_audio,
                                          width=control_button_width,
                                          fg_color=control_button_color, hover_color=control_button_color_hover)
        self.pause_button.grid(row=0, column=1, sticky="nsew")

class FiltersFrame(ctk.CTkFrame):
    def __init__(self, master, height):
        super().__init__(master)

        self.filters_frame = ctk.CTkFrame(master.toolbar_frame, fg_color="grey", height=height)
        self.filters_frame.grid(row=0, column=2, sticky="nsew")
        self.filters_frame.grid_columnconfigure(0, weight=1)
        self.filters_frame.grid_columnconfigure(1, weight=3)
        self.filters_frame.grid_rowconfigure(0, weight=1)
        self.filters_frame.grid_propagate(False)

        self.select_filter_frame = ctk.CTkFrame(self.filters_frame, fg_color="grey")
        self.select_filter_frame.grid(row=0, column=0, sticky="nsew", padx = 15, pady = 5)
        self.select_filter_frame.grid_columnconfigure(0, weight=1)
        self.select_filter_frame.grid_rowconfigure((0, 1, 2, 3, 4), weight=1)

        self.textbox_frame = ctk.CTkFrame(self.filters_frame, fg_color="grey")
        self.textbox_frame.grid(row=0, column=1, sticky="ew", padx = 15, pady = 5)

        def only_numbers(n):
            if n == "":
                return True
            try:
                float(n)
                return True
            except ValueError:
                return False

        validate_command = (self.register(only_numbers), "%P")

        self.textbox_label1 = ctk.CTkLabel(self.textbox_frame, text="Enter Cutoff Frequency (High):")
        self.textbox1 = ctk.CTkEntry(self.textbox_frame, placeholder_text="Frequency (Hz)",
            validate="key", validatecommand=validate_command)
        self.textbox_label2 = ctk.CTkLabel(self.textbox_frame, text="Enter Cutoff Frequency (Low):")
        self.textbox2 = ctk.CTkEntry(self.textbox_frame, placeholder_text="Frequency (Hz)",
            validate="key", validatecommand=validate_command)

        def apply_filter():
            match master.filter.get():
                case "reverb":
                    master.audio = filter.reverb(master.audio, master.audio.samp_freq)
                case "echo":
                    master.audio = filter.echo(master.audio, master.audio.samp_freq)
                case "lowpass":
                    master.audio = filter.lowPass(master.audio, master.audio.samp_freq, self.textbox1.get())
                case "highpass":
                    master.audio = filter.highPass(master.audio, master.audio.samp_freq, self.textbox2.get())
                case "bandpass":
                    master.audio = filter.bandPass(master.audio, master.audio.samp_freq, self.textbox1.get(), self.textbox2.get())


        self.apply_button = ctk.CTkButton(self.textbox_frame, text="Apply Filter", command=apply_filter)


        def radiobutton_event():
            print("Option toggled, current value:", master.filter.get())
            self.textbox1.delete(0, "end")
            self.textbox2.delete(0, "end")

            match master.filter.get():
                case "lowpass":
                    self.textbox_frame.grid_columnconfigure(0, weight=1)
                    self.textbox_frame.grid_rowconfigure(1, weight=1)
                    self.textbox_label2.grid_remove()
                    self.textbox2.grid_remove()
                    self.textbox_label1.grid(row=0, column=0, sticky="ew")
                    self.textbox1.grid(row=1, column=0, sticky="ew")
                    self.apply_button.grid(row=2, column=0, sticky="ew", pady=5)
                case "highpass":
                    self.textbox_frame.grid_columnconfigure(0, weight=1)
                    self.textbox_frame.grid_rowconfigure(1, weight=1)
                    self.textbox_label1.grid_remove()
                    self.textbox1.grid_remove()
                    self.textbox_label2.grid(row=0, column=0, sticky="ew")
                    self.textbox2.grid(row=1, column=0, sticky="ew")
                    self.apply_button.grid(row=2, column=0, sticky="ew", pady=5)
                case "bandpass":
                    self.textbox_frame.grid_columnconfigure(0, weight=1)
                    self.textbox_frame.grid_rowconfigure((1, 3), weight=1)
                    self.textbox_label1.grid(row=0, column=0, sticky="ew")
                    self.textbox1.grid(row=1, column=0, sticky="ew")
                    self.textbox_label2.grid(row=2, column=0, sticky="ew")
                    self.textbox2.grid(row=3, column=0, sticky="ew")
                    self.apply_button.grid(row=4, column=0, sticky="ew", pady=5)
                case _:
                    self.textbox_label1.grid_remove()
                    self.textbox1.grid_remove()
                    self.textbox_label2.grid_remove()
                    self.textbox2.grid_remove()
                    self.apply_button.grid_remove()
                    self.apply_button.grid(row=0, column=0, sticky="ew", pady=5)


        radiobutton_event()

        self.select_reverb = ctk.CTkRadioButton(self.select_filter_frame, text="Reverb",
                            command=radiobutton_event, variable=master.filter, value="reverb")
        self.select_reverb.grid(row=0, column=0, sticky="nsew")
        self.select_echo = ctk.CTkRadioButton(self.select_filter_frame, text="Echo",
                            command=radiobutton_event, variable=master.filter, value="echo")
        self.select_echo.grid(row=1, column=0, sticky="nsew")
        self.select_lowpass = ctk.CTkRadioButton(self.select_filter_frame, text="Low-Pass",
                            command=radiobutton_event, variable=master.filter, value="lowpass")
        self.select_lowpass.grid(row=2, column=0, sticky="nsew")
        self.select_highpass = ctk.CTkRadioButton(self.select_filter_frame, text="High-Pass",
                            command=radiobutton_event, variable=master.filter, value="highpass")
        self.select_highpass.grid(row=3, column=0, sticky="nsew")
        self.select_bandpass = ctk.CTkRadioButton(self.select_filter_frame, text="Band-Pass",
                            command=radiobutton_event, variable=master.filter, value="bandpass")
        self.select_bandpass.grid(row=4, column=0, sticky="nsew")

        self.disable_filters()

    def disable_filters(self):
        self.select_reverb.configure(state="disabled")
        self.select_echo.configure(state="disabled")
        self.select_lowpass.configure(state="disabled")
        self.select_highpass.configure(state="disabled")
        self.select_bandpass.configure(state="disabled")
        self.textbox1.configure(state="disabled")
        self.textbox2.configure(state="disabled")
        self.apply_button.configure(state="disabled")

    def enable_filters(self):
        self.select_reverb.configure(state="normal")
        self.select_echo.configure(state="normal")
        self.select_lowpass.configure(state="normal")
        self.select_highpass.configure(state="normal")
        self.select_bandpass.configure(state="normal")
        self.textbox1.configure(state="normal")
        self.textbox2.configure(state="normal")
        self.apply_button.configure(state="normal")



