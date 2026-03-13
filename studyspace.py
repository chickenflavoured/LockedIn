import tkinter as tk
from tkinter import ttk
from timers import Timer
import threading

window = tk.Tk()

HEIGHT = 600
WIDTH = 600
# Window display size
window.geometry(f"{WIDTH}x{HEIGHT}")

def placeholder():
    print("This is a placeholder")

def start_timer_thread(timer, work, rest, longrest, session, time_begun, btn):
    """
    Starts running the countdown timer with a thread.

    Args:
        timer(Timer)
        time1(int)
        time2(int)
        time3(int)

    """

    timer.work_time = work * 60
    timer.rest_time = rest * 60 # Add an extra second towards rest_time because the pomodoro jumps over one second on the rest in display
    timer.longrest_time = longrest * 60
    timer.sessions = session
    timer.running = time_begun[1]

    if not time_begun[2]:
        # Start running the thread with instance method
        separate = threading.Thread(target = timer.pomodoro_countdown, args = (window,), daemon = True) # Needs to be a comma at args = (window,)
    else:
        separate = threading.Thread(target = timer.stopwatch, args = (window,), daemon = True)

    separate.start()

    if time_begun[1]:
        time_begun[1] = False
        btn.config(text = "End Timer")

    else:
        time_begun[1] = True
        btn.config(text = "Begin Timer") 
    
def pause_timer_thread(timer, time_paused, btn):
    
    if not time_paused[0]:
        time_paused[0] = True
        btn.config(text = "Resume")
        timer.pause_event.clear() #.clear() pauses the thread attribute in timer
    else:
        time_paused[0] = False
        btn.config(text = "Pause")
        timer.pause_event.set() #.set() resumes the thread attribute in timer

def main(choice, is_stopwatch):

    # Remove the buttons
    pomodoro_btn.destroy()
    countdown_btn.destroy()
    stopwatch_btn.destroy()

    # Create instance of Timer Class
    timer = Timer(0, 0, 0, 0, True)

    # Variable keeping track of the timer.
    # [0] -> Whether the user is pausing or resuming the timer
    # [1] -> Whether the user is beginning or ending the timer.
    # [2] -> Whether it is a stopwatch
    time_paused_and_started = [False, True, is_stopwatch]

    # Variables
    time_var = tk.IntVar(value = 0) 
    rest_var = tk.IntVar(value = 0) 
    longrest_var = tk.IntVar(value = 0)
    session_var = tk.IntVar(value = 1)

    if choice == "pomodoro":

        # Time entries and labels initialization
        rest_label = tk.Label(window, text = "Short rest (Minutes)")
        longrest_label = tk.Label(window, text = "Long rest (Minutes)")
        rest_entry = tk.Entry(window, textvariable = rest_var)
        longrest_entry = tk.Entry(window, textvariable = longrest_var)
        session_label = tk.Label(window, text = "Sessions")
        session_entry = tk.Entry(window, textvariable = session_var)

        # Labels
        rest_label.grid(row = 0, column = 2)
        longrest_label.grid(row = 0, column = 4)
        session_label.grid(row = 0, column = 6)

        # Entries
        rest_entry.grid(row = 0, column = 3)
        longrest_entry.grid(row = 0, column = 5)
        session_entry.grid(row = 0, column = 7)

    if choice == "pomodoro" or choice == "countdown":
        # Time entries and labels initialization
        time_label = tk.Label(window, text = "Minutes")
        time_entry = tk.Entry(window, textvariable = time_var)
        
        # Labels
        time_label.grid(row = 0, column = 0)

        # Entries
        time_entry.grid(row = 0, column = 1)

    else:
        print(choice)


    # Buttons initialization
    start_btn = tk.Button(window, text = "Begin Timer", command = lambda: start_timer_thread(timer, time_var.get(), rest_var.get(), longrest_var.get(), session_var.get(), time_paused_and_started, start_btn)) # Lambda allows command to pass arguments without immediately executing function
    pause_btn = tk.Button(window, text = "Pause", command = lambda: pause_timer_thread(timer, time_paused_and_started, pause_btn))

    # -- Grid Placements --

    # Buttons
    pause_btn.grid(row = 4, column = 0)
    start_btn.grid(row = 6, column = 0)


pomodoro_btn = tk.Button(window, text = "Pomodoro", command = lambda: main("pomodoro", False))
countdown_btn = tk.Button(window, text = "Countdown", command = lambda: main("countdown", False))
stopwatch_btn = tk.Button(window, text = "Stopwatch", command = lambda: main("stopwatch", True))

pomodoro_btn.grid(row = 2, column = 1)
countdown_btn.grid(row = 2, column = 3)
stopwatch_btn.grid(row = 2, column = 5)

window.mainloop()