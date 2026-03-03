import tkinter as tk
import yt_dlp
import os
from yt_dlp.postprocessor import FFmpegPostProcessor

import sdl2
import sdl2.sdlmixer as mixer

# https://pypi.org/project/PySDL2/
#FFmpegPostProcessor._ffmpeg_location.set("./ffmpeg")

def play():
    pass

# https://www.youtube.com/watch?v=60ItHLz5WEA

def download():

    url = link.get()

    ydl_options = {
        "outtmpl":"music.mp3",
        "format": "bestaudio/best",
        "ffmpeg_location": "./ffmpeg",
        "postprocessors": [{
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": "192",
        }]
        }
    
    if os.path.isfile("music.mp3"):
        os.remove("music.mp3")


    with yt_dlp.YoutubeDL(ydl_options) as ydl:
        ydl.download([url])

        info = ydl.extract_info(url, download=False)
        title = info.get("title", None)
        duration = info.get("duration", None)
        views = info.get("view_count", None)

root = tk.Tk()
root.geometry(f"480x360")

link = tk.Entry(root)
link.grid(row=0, column=0)

button = tk.Button(root, text="Play", command=play)
button.grid(row=1, column=0, padx=10, pady=10)

button = tk.Button(root, text="Download", command=download)
button.grid(row=1, column=1, padx=10, pady=10)

root.mainloop()