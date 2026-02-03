import tkinter as tk
from tkinter import ttk
from lockedin_timers import Timer

window = tk.Tk()

HEIGHT = 600
WIDTH = 600
# Window display size
window.geometry(f"{WIDTH}x{HEIGHT}")

def start_timer(countdown_time, running):

    timer = Timer(countdown_time, running)
    timer.countdown()


time_var = tk.IntVar()

time_label = tk.Label(window, text = "Time")
time_entry = tk.Entry(window, textvariable = time_var)

start_btn = tk.Button(window, text = "Begin Timer", command = start_timer(time_var.get(), True))

time_label.grid(row = 0, column = 0)
time_entry.grid(row = 0, column = 1)
start_btn.grid(row = 1, column = 0)

window.mainloop()