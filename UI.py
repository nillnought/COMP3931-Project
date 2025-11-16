#all needed info on tkinter for GUI can be found here:
# https://www.geeksforgeeks.org/python/python-tkinter-tutorial/

import tkinter as tk


class UI:
    def __init__(self, root):
        self.root = root
        self.root.title("AppName")
        self.root.geometry("500x500")

        self.label = tk.Label(root, text="Simple Window", font=("Arial Bold", 20))
        self.label.pack(expand=True)
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)

    def on_close(self):
        self.root.destroy()

