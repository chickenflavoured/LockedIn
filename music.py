import tkinter as tk
import yt_dlp
import os
from yt_dlp.postprocessor import FFmpegPostProcessor
import json

import sdl2
import sdl2.sdlmixer as mixer
from tkextrafont import Font

from ctypes import windll
#windll.shcore.SetProcessDpiAwareness(1)


# https://pypi.org/project/PySDL2/
#FFmpegPostProcessor._ffmpeg_location.set("./ffmpeg/bin/ffmpeg.exe")

# Think about tkSnack? https://www.speech.kth.se/snack/


class Player:

    def __init__(self, playlist: dict = {}):
        mixer.Mix_OpenAudio(44100, sdl2.AUDIO_S16SYS, 2, 2048)
        self.playlist = playlist
        self.counter = 0


    def play(self, event):
        if mixer.Mix_Playing(-1):
            mixer.Mix_HaltChannel(-1)
        
        selection = playlist_list.get(playlist_list.curselection())

        print(playlist_list.get(playlist_list.curselection()))
        file = mixer.Mix_LoadWAV(f"./tracks/{self.playlist[selection]}.mp3".encode("utf-8"))
        mixer.Mix_PlayChannel(-1, file, 0)
    

    def delete(self):
        selection = playlist_list.get(playlist_list.curselection())
        self.playlist.pop(selection)

        playlist_list.config(listvariable=tk.Variable(value=list(self.playlist.keys())), height=len(self.playlist))


    def toggle_pause(self, button):
        if mixer.Mix_Paused(-1):
            mixer.Mix_Resume(-1)
            button.config(text="Pause")
        else:
            mixer.Mix_Pause(-1)
            button.config(text="Resume")


    def stop(self, pause_button):
        pause_button.config(text="Pause")
        mixer.Mix_FadeOutChannel(-1, 500)

    # https://youtu.be/_RGp-Cynxkg
    def download(self):

        url = link.get()

        ydl_options = {
            "outtmpl": f"tracks/{self.counter}",
            "format": "bestaudio/best",
            # "ffmpeg-location": "./ffmpeg/bin/ffmpeg.exe",
            "ffmpeg-location": "ffmpeg/bin/ffmpeg.exe",
            "postprocessors": [{
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192"
            }]
            }


        with yt_dlp.YoutubeDL(ydl_options) as ydl:
            ydl.download([url])

            info = ydl.extract_info(url, download=False)
            title = info.get("title", None)
            duration = info.get("duration", None)
            views = info.get("view_count", None)
        self.playlist[title] = self.counter
        with open("playlistdata.json", "w") as f:
            json.dump(self.playlist, f)

        self.counter += 1

        playlist_list.config(listvariable=tk.Variable(value=list(self.playlist.keys())), height=len(self.playlist))


root = tk.Tk()
root.title("Music Player")
root.geometry("480x360")


root.title("Lockedin Music Player")
img = tk.PhotoImage(file='lockedin_mascot.png')
# The icon uses a .ico file so use iconphoto instead
root.iconphoto(False, img)

# Stops the user from entering full screen
root.resizable(False, False) 

# THIS SETS THE FONT
font = Font(file="sniglet.ttf", family="Sniglet")
root.option_add("*Font", "Sniglet 10")

bg = tk.PhotoImage(file = "music.png")
bg_label = tk.Label(root, image=bg)
bg_label.place(x = 0, y = 0)

link = tk.Entry(root)
link.grid(row=0, column=0)

with open("playlistdata.json") as f:
    player = Player(json.load(f))

play_button = tk.Button(root, text="Pause")
play_button.config(command=lambda: player.toggle_pause(play_button))
play_button.grid(row=1, column=0, padx=10, pady=0)

stop_button = tk.Button(root, text="Stop", command=lambda: player.stop(play_button))
stop_button.grid(row=3, column=0, padx=10, pady=0)

del_button = tk.Button(root, text="Delete", command=player.delete)
del_button.grid(row=4, column=0, padx=10, pady=0)

dl_button = tk.Button(root, text="Download", command=player.download)
dl_button.grid(row=1, column=1, padx=10, pady=0)


playlist_list = tk.Listbox(root, 
                           listvariable=tk.Variable(value=list(player.playlist.keys())), 
                           width=35,
                           height=len(player.playlist), 
                           exportselection=False)
playlist_list.bind("<<ListboxSelect>>", player.play)
playlist_list.grid(row=5, column=0, padx=40, pady=40)

root.mainloop()
