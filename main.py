# runs the whole application

import tkinter as tk
from UI import UI

def main():
    root = tk.Tk()
    app = UI(root)
    root.mainloop()

if __name__ == "__main__":
    main()