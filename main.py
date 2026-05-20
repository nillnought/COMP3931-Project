# runs the whole application

from UI import UI
from audioFile import audioFile
from filter import highPass, lowPass, bandPass, echo, reverb

def main():
    app = UI()
    app.mainloop()

if __name__ == "__main__":
    main()
