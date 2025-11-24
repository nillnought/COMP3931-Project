from scipy import signal as sg
from scipy.fft import fft, ifft, fftfreq
import numpy as np


def reverb(audio, samp_freq, amp_reduction=0.5, delay_ms=50, repeats =8):
    #applies reverb
    delay_samps = int(samp_freq * delay_ms / 1000)
    impulse = np.zeros(delay_samps * repeats +1)
    for i in range(repeats):
        impulse[i * delay_samps] = amp_reduction ** i
    impulse[0] = 1.0

    if audio.ndim == 1:
        return sg.fftconvolve(audio, impulse, mode="full")
    else:
        filtered = sg.fftconvolve(audio, impulse[:, None], mode="full", axes=0)
        return filtered


def echo(audio, samp_freq, delay_ms=300, decay=0.3, repeats = 5):
    #applies echo
    delay_samps = int(samp_freq*delay_ms /1000)
    impulse = np.zeros(delay_samps*repeats + 1)
    for i in range(repeats):
        impulse[i * delay_samps] = decay ** i
    impulse[0] = 1.0
    if audio.ndim == 1:
        return(sg.fftconvolve(audio, impulse, mode="full"))
    else:
        filtered_data = sg.fftconvolve(audio, impulse[:, None], mode="full", axes=0)
        return filtered_data

#need to test
def lowPass(audio, samp_freq, cutoff=20):
    #cutoff high freqs
    N = audio.shape[0]
    freqs = fftfreq(N, 1/samp_freq)
    mask = np.abs(freqs) <= cutoff

    fft_data = fft(audio, axis=0)
    filtered_audio = ifft(fft_data * mask[:, None], axis=0)

    return np.real(filtered_audio)
    

def highPass(audio, samp_freq, cutoff=20):
    #cutoff low freqs
    N = audio.shape[0]
    freqs = fftfreq(N, 1/samp_freq)
    mask = np.abs(freqs) >= cutoff

    fft_data = fft(audio, axis=0)
    filtered_audio = ifft(fft_data * mask[:, None], axis=0)

    return np.real(filtered_audio)

def bandPass(audio, samp_freq, high=50, low=20):
    #keep freqs within certain range
    N = audio.shape[0]
    freqs = fftfreq(N, 1/samp_freq)
    mask = ((np.abs(freqs) >= low) & (np.abs(freqs) <= high))
    fft_data = fft(audio, axis=0)
    filtered_audio = ifft(fft_data * mask[:, None], axis=0)

    return np.real(filtered_audio)