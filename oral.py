import tkinter as tk
import sounddevice as sd
import numpy as np
from scipy.io import wavfile
# Think abt using asyncio for recording in the background?

root = tk.Tk()
root.title("Oral Presentation")
root.geometry("600x720")

samplerate = 44100

recording = np.array([])

def record():

    print("Recording")
    recording = sd.rec(4 * samplerate, samplerate=samplerate, channels=2)

    sd.wait()
    print("Done")


def stop():

    recording = sd.stop()
    print("Done")


def playback():

    print("Playing")
    sd.play(recording)


start_button = tk.Button(root, text="Start recording", command=record)
start_button.grid(row=1, column=0, padx=10, pady=0)

end_button = tk.Button(root, text="Stop recording", command=stop)
end_button.grid(row=2, column=0, padx=10, pady=0)

play_button = tk.Button(root, text="Playback", command=playback)
play_button.grid(row=3, column=0, padx=10, pady=0)


root.mainloop()

