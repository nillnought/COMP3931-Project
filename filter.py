from scipy import signal as sg
import numpy as np


def reverb(audio, samp_freq, amp_reduction=0.5, delay_ms=50):
    #applies reverb
    delay_samps = int(samp_freq * delay_ms / 1000)
    impulse = np.zeros(delay_samps * 8)
    for i in range(8):
        impulse[i * delay_samps] = amp_reduction ** i

    return(sg.fftconvolve(audio, impulse, mode="same"))

def echo(audio, samp_freq, delay_ms=300, decay=0.6):
    #applies echo
    delay_samps = int(samp_freq*delay_ms /1000)
    impulse = np.zeros(delay_samps + 1)
    impulse[0] = 1.0
    impulse[-1] = decay
    return(sg.fftconvolve(audio, impulse, mode="same"))

def lowPass(audio, samp_freq, cutoff=20):
    #cutoff high freqs
    print("placeholder")

def highPass(audio, samp_freq, cutoff=20):
    #cutoff low freqs
    print("placeholder")

def bandPass(audio, samp_freq, high=50, low=20):
    #keep freqs within certain range
    print("placeholder")