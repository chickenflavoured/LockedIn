import tkinter as tk
import sounddevice as sd
import numpy as np
from scipy.io import wavfile

root = tk.Tk()
root.title("Oral Presentation")
root.geometry("600x720")

samplerate = 44100

recording = sd.rec(6 * samplerate, samplerate=samplerate, channels=2)


root.mainloop()
