import tkinter as tk
import yt_dlp
import os
from yt_dlp.postprocessor import FFmpegPostProcessor

import sdl2
import sdl2.sdlmixer as mixer

# https://pypi.org/project/PySDL2/
FFmpegPostProcessor._ffmpeg_location.set("./ffmpeg/bin/ffmpeg.exe")

# Think about tkSnack? https://www.speech.kth.se/snack/

mixer.Mix_OpenAudio(44100, sdl2.AUDIO_S16SYS, 2, 2048)

def play(event):
    if not mixer.Mix_Playing(-1):
        print(playlist.get(playlist.curselection()))
        file = mixer.Mix_LoadWAV(f"./tracks/{playlist.get(playlist.curselection())}".encode("utf-8"))
        mixer.Mix_PlayChannel(-1, file, 0)

    else:
        mixer.Mix_Resume(-1)


def pause():
    mixer.Mix_Pause(-1)


def stop():
    mixer.Mix_FadeOutChannel(-1, 1000)

# https://youtu.be/_RGp-Cynxkg
def download():

    url = link.get()

    ydl_options = {
        "outtmpl": f"tracks/{len(os.listdir('./tracks'))}",
        "format": "bestaudio/best",
        "ffmpeg-location": "./ffmpeg/bin/ffmpeg.exe",
        # "ffmpeg-location": "ffmpeg/bin/ffmpeg.exe",
        "postprocessors": [{
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": "44.1"
        }]
        }


    with yt_dlp.YoutubeDL(ydl_options) as ydl:
        ydl.download([url])

        info = ydl.extract_info(url, download=False)
        title = info.get("title", None)
        duration = info.get("duration", None)
        views = info.get("view_count", None)
    
    playlist.config(listvariable=tk.Variable(value=os.listdir("./tracks")), height=len(os.listdir("./tracks")))

root = tk.Tk()
root.title("Music Player")
root.geometry(f"480x360")

is_playing = False

link = tk.Entry(root)
link.grid(row=0, column=0)

play_button = tk.Button(root, text="Play", command=play)
play_button.grid(row=1, column=0, padx=10, pady=0)

pause_button = tk.Button(root, text="Pause", command=pause)
pause_button.grid(row=2, column=0, padx=10, pady=0)

stop_button = tk.Button(root, text="Stop", command=stop)
stop_button.grid(row=3, column=0, padx=10, pady=0)

dl_button = tk.Button(root, text="Download", command=download)
dl_button.grid(row=1, column=1, padx=10, pady=0)

playlist = tk.Listbox(root, listvariable=tk.Variable(value=os.listdir("./tracks")), selectmode="browse", height=len(os.listdir("./tracks")), exportselection=False)
playlist.bind("<<ListboxSelect>>", play)
playlist.grid(row=4, column=0, padx=40, pady=40)

root.mainloop()
