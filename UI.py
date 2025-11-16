#all needed info on tkinter for GUI can be found here:
# https://www.geeksforgeeks.org/python/python-tkinter-tutorial/

import tkinter as tk

root = tk.Tk()
root.title("AppName")
root.geometry("500x500")

label = tk.Label(root, text="Simple Window", font=("Arial Bold", 20))
label.pack(expand=True)

def on_close():
    root.destroy()

root.protocol("WM_DELETE_WINDOW", on_close)
root.mainloop()
