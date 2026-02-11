import tkinter as tk
from tkinter import ttk
from studyspace_timers import Timer
import threading

window = tk.Tk()

HEIGHT = 600
WIDTH = 600
# Window display size
window.geometry(f"{WIDTH}x{HEIGHT}")

def start_timer_thread(timer, time, run):
    
    timer.countdown_time = time
    timer.running = run
    separate = threading.Thread(target = timer.countdown, args = (window,))
    separate.start()
    

def pause_timer_thread(timer):
    
    print("paused")
    timer.pause_event.clear()

def resume_timer_thread(timer):

    timer.pause_event.set()

time = 0
run = False

timer = Timer(time, run)

time_var = tk.IntVar()

time_label = tk.Label(window, text = "Time")
time_entry = tk.Entry(window, textvariable = time_var)

crt_time_lst = [time_var.get()]

start_btn = tk.Button(window, text = "Begin Timer", command = lambda: start_timer_thread(timer, time_var.get(), True)) # Lambda allows command to pass arguments without immediately executing function
pause_btn = tk.Button(window, text = "Pause", command = lambda: pause_timer_thread(timer))
resume_btn = tk.Button(window, text = "Resume", command = lambda: resume_timer_thread(timer))

pause_btn.grid(row = 2, column = 0)
resume_btn.grid(row = 3, column = 0)
time_label.grid(row = 0, column = 0)
time_entry.grid(row = 0, column = 1)
start_btn.grid(row = 1, column = 0)


window.mainloop()