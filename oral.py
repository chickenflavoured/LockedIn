import tkinter as tk
import sounddevice as sd
import numpy as np
import threading
from scipy.io import wavfile

root = tk.Tk()
root.title("Oral Presentation")
root.geometry("600x720")

# https://python-sounddevice.readthedocs.io/en/latest/examples.html#recording-with-arbitrary-duration

samplerate = 44100

recording = np.array([])
is_active = [False]

def record():
    is_active[0] = True

    print("Recording")
    print(is_active)
    while is_active[0]:
        data = sd.rec(samplerate, samplerate=samplerate, channels=2)
        np.append(recording, data)
    print("Done")


def start_recording():
    t = threading.Thread(target=record)
    t.start()

def end_recording():
    is_active[0] = False


def playback():

    print("Playing")
    print(recording)
    sd.play(recording)


rec_button = tk.Button(root, text="Record", command=record)
rec_button.grid(row=1, column=0, padx=10, pady=0)

rec_button = tk.Button(root, text="End", command=end_recording)
rec_button.grid(row=1, column=1, padx=10, pady=0)

play_button = tk.Button(root, text="Play", command=playback)
play_button.grid(row=2, column=0, padx=10, pady=0)


root.mainloop()
