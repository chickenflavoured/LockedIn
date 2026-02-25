import tkinter as tk
from tkinter import ttk
from timers import Timer
import threading

window = tk.Tk()

HEIGHT = 600
WIDTH = 600
# Window display size
window.geometry(f"{WIDTH}x{HEIGHT}")

def start_timer_thread(timer, time1, time2, time3, time_begun, btn):
    """
    Starts running the countdown timer with a thread.

    Args:
        timer(Timer)
        time1(int)
        time2(int)
        time3(int)

    """

    timer.total_time = time1 + (time2*60) + (time3*3600)
    timer.running = time_begun[2]
    # Start running the thread with instance method
    separate = threading.Thread(target = timer.countdown, args = (window,), daemon = True) # Needs to be a comma at args = (window,)
    separate.start()

    if time_begun[1]:
        time_begun[1] = False
        btn.config(text = "Begin Timer")

    else:
        time_begun[1] = True
        time_begun[2] = False
        btn.config(text = "End Timer") 
    
def pause_timer_thread(timer, time_paused, btn):
    
    if not time_paused[0]:
        time_paused[0] = True
        btn.config(text = "Resume")
        timer.pause_event.clear() #.clear() pauses the thread attribute in timer
    else:
        time_paused[0] = False
        btn.config(text = "Pause")
        timer.pause_event.set() #.set() resumes the thread attribute in timer

# Create instance of Timer Class
time = 0
timer = Timer(time)

# Variable keeping track of the timer.
# [0] -> Whether the user is pausing or resuming the timer
# [1] -> Whether the user is beginning or ending the timer.
time_paused_and_started = [False, True, True]

# Variables
time_var1 = tk.IntVar(value = 0) 
time_var2 = tk.IntVar(value = 0) 
time_var3 = tk.IntVar(value = 0) 

# Time entries and labels initialization
time_label1 = tk.Label(window, text = "Seconds")
time_entry1 = tk.Entry(window, textvariable = time_var1)
time_label2 = tk.Label(window, text = "Minutes")
time_entry2 = tk.Entry(window, textvariable = time_var2)
time_label3 = tk.Label(window, text = "Hours")
time_entry3 = tk.Entry(window, textvariable = time_var3)

# Buttons initialization
start_btn = tk.Button(window, text = "Begin Timer", command = lambda: start_timer_thread(timer, time_var1.get(), time_var2.get(), time_var3.get(), time_paused_and_started, start_btn)) # Lambda allows command to pass arguments without immediately executing function
pause_btn = tk.Button(window, text = "Pause", command = lambda: pause_timer_thread(timer, time_paused_and_started, pause_btn))

# -- Grid Placements --

# Buttons
pause_btn.grid(row = 4, column = 0)
start_btn.grid(row = 6, column = 0)

# Labels
time_label1.grid(row = 0, column = 0)
time_label2.grid(row = 2, column = 0)
time_label3.grid(row = 3, column = 0)

# Entries
time_entry1.grid(row = 0, column = 1)
time_entry2.grid(row = 2, column = 1)
time_entry3.grid(row = 3, column = 1)

window.mainloop()