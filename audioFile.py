import soundfile as sf
import numpy as np
import sounddevice as sd
import matplotlib as plt
from scipy.fft import fft, fftfreq
class audioFile:


# usage: audio = audioFile("filename.wav")
    def __init__(self, file_location):
        self.file_address = file_location
        self.audio_data, self.samp_freq = sf.read(file_location)
        self.playing = False
        audio_file = sf.SoundFile(file_location)
        self.duration = audio_file.frames / audio_file.samplerate

# usage: audio.saveFile("newName.wav") can look into appending a file format when user chooses to save
    def saveFile(self, new_file_name):
        sf.write(new_file_name, self.audio_data, self.samp_freq)

# usage: audio.playSound()
    def playSound(self):
        sd.play(self.audio_data, self.samp_freq)
        self.playing = True
        sd.wait()
        self.playing = False
    
    def pauseSound(self):
        if(self.playing):
            #pause logic
            print("pause")

#need to test
    def drawAmpDomain(self):
        plt.figure(figsize=(10, 5))
        plt.plot(self.duration, self.audio_data)
        plt.show()

#need to test
    def drawFreqDomain(self):
        N = len(self.audio_data)
        yf = fft(self.audio_data)
        xf = fftfreq(N, 1/self.samp_freq)[:N // 2]

        plt.figure(figsize=(10,5))
        plt.plot(xf, np.abs(yf[:N //2]))
        plt.show()