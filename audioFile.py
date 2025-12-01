import soundfile as sf
import numpy as np
import sounddevice as sd
from matplotlib.figure import Figure
from scipy.fft import fft, fftfreq
class audioFile:


# usage: audio = audioFile("filename.wav")
    def __init__(self, file_location):
        self.file_address = file_location
        self.audio_data, self.samp_freq = sf.read(file_location)
        self.playing = False
        self.undo_stack = []
        self.redo_stack = []

        audio_file = sf.SoundFile(file_location)
        total_duration = audio_file.frames / audio_file.samplerate
        self.duration = np.linspace(
            0, total_duration, len(self.audio_data)
        )

# usage: audio.saveFile("newName.wav") can look into appending a file format when user chooses to save
    def saveFile(self, new_file_name):
        sf.write(new_file_name, self.audio_data, self.samp_freq)

# usage: audio.playSound()
    def playSound(self):
        sd.play(self.audio_data, self.samp_freq)
        self.playing = True
        sd.wait()
        self.playing = False
    

#Call this before applying a filter
    def saveState(self):
        self.undo_stack.append(self.audio_data.copy())
        self.redo_stack.clear()

    def drawAmpDomain(self):
        fig = Figure(figsize=(10, 5))
        ax = fig.add_subplot(111)
        audio_file = sf.SoundFile(self.file_address)
        total_duration = audio_file.frames / audio_file.samplerate
        self.duration = np.linspace(
            0, total_duration, len(self.audio_data)
        )
        ax.plot(self.duration, self.audio_data)
        ax.axis("off")
        fig.patch.set_facecolor("none")
        ax.set_facecolor("none")

        return fig


    def undo(self):
        if not self.undo_stack:
            return
        self.redo_stack.append(self.audio_data.copy())
        self.audio_data = self.undo_stack.pop()
        
    def redo(self):
        if not self.redo_stack:
            return
        self.undo_stack.append(self.audio_data.copy)
        self.audio_data = self.redo_stack.pop()

    def drawFreqDomain(self):
        N = len(self.audio_data)
        yf = fft(self.audio_data)
        xf = fftfreq(N, 1/self.samp_freq)[:N // 2]

        fig = Figure(figsize=(10,5))
        ax = fig.add_subplot(111)
        
        ax.plot(xf, np.abs(yf[:N //2]))

        # ax.axis("off")
        fig.patch.set_facecolor("none")
        ax.set_facecolor("none")
        ax.tick_params(axis='x', colors='white')  # X-axis numbers
        ax.tick_params(axis='y', colors='white')
        return fig
        