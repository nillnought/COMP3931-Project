# runs the whole application

from UI import UI
from audioFile import audioFile
from filter import highPass, lowPass, bandPass, echo, reverb

def main():
    app = UI()
    app.mainloop()
    # audio = audioFile("test.wav")
    # audio.playSound()
    # YAY LOW PASS WORKS!!!
    # audio.audio_data = lowPass(audio.audio_data, audio.samp_freq, 600)
    # audio.playSound()
    # YAY HIGH PASS WORKS!!!
    # audio.audio_data = highPass(audio.audio_data, audio.samp_freq, 300)
    # audio.playSound()
    # YAY BANDPASS WORKS!!!
    # audio.audio_data = bandPass(audio.audio_data, audio.samp_freq, 600, 300)
    # audio.playSound()
    # YAY ECHO WORKS!!
    # audio.audio_data = echo(audio.audio_data, audio.samp_freq)
    # audio.playSound()
    # YAY REVERB WORKS!!
    # audio.audio_data = reverb(audio.audio_data, audio.samp_freq)
    # audio.playSound()

if __name__ == "__main__":
    main()