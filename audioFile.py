import soundfile as sf
import numpy as np
class audioFile:


# usage: audio = audioFile("filename.wav")
    def __init__(self, file_location):
        self.file_address = file_location
        self.audio_data, self.samp_freq = sf.read(file_address)

# usage: audio.saveFile("newName.wav") can look into appending a file format when user chooses to save
    def saveFile(self, new_file_name):
        sf.write(new_file_name, self.audio_data, self.samp_freq)