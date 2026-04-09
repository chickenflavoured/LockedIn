import tkinter as tk
import sounddevice as sd
import numpy as np
from scipy.io import wavfile

root = tk.Tk()
root.title("Oral Presentation")
root.geometry("600x720")

samplerate = 44100

recording = np.array()

def record():

    print("Recording")
    recording = sd.rec(4 * samplerate, samplerate=samplerate, channels=2)


def playback():

    print("Playing")
    sd.play(recording)


root.mainloop()


sd.wait()
print("Done")

