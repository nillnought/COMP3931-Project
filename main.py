# runs the whole application

from UI import UI
from audioFile import audioFile

def main():
    app = UI()
    app.mainloop()
    # audio = audioFile("test.wav")
    # audio.drawAmpDomain()
    # audio.drawFreqDomain()

if __name__ == "__main__":
    main()