import tkinter as tk
from tkinter import ttk
from studyspace_timers import Timer
import threading

window = tk.Tk()

HEIGHT = 600
WIDTH = 600
# Window display size
window.geometry(f"{WIDTH}x{HEIGHT}")

def start_timer(countdown_time, running):


    print(countdown_time, running)
    timer = Timer(countdown_time, running)
    timer.countdown(window)



# Thread that executes start_timer separately so that main can also continue to execute
def start_timer_thread(time_arg, run_arg, pause):

    # Somethign with this pause thread stuff doesn't work
    pause_thread = threading.Event
    pause_thread.set

    separate = threading.Thread(target = start_timer, args = (time_arg, run_arg))
    separate.start()

    while not pause:
        pause_thread.wait()

time_var = tk.IntVar()

time_label = tk.Label(window, text = "Time")
time_entry = tk.Entry(window, textvariable = time_var)

start_btn = tk.Button(window, text = "Begin Timer", command = lambda: start_timer_thread(time_var.get(), True)) # Lambda allows command to pass arguments without immediately executing function
pause_btn = tk.Button(window, text = "Pause", command = lambda: start_timer_thread(time_var.get(), True, False))

pause_btn.grid(row = 2, column = 0)
time_label.grid(row = 0, column = 0)
time_entry.grid(row = 0, column = 1)
start_btn.grid(row = 1, column = 0)


window.mainloop()