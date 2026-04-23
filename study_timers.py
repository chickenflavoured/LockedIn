import tkinter as tk
from tkinter import ttk
from timers import Timer
import threading

window = tk.Tk()

HEIGHT = 200
WIDTH = 400
# Window display size
window.geometry(f"{WIDTH}x{HEIGHT}")

bg = tk.PhotoImage(file = "study_timers.png")
bg_label = tk.Label(window, image = bg)
bg_label.place(x = 0, y = 0)

def validation(P):

    if P == 0 or P.isdigit():
        valid = True
    else:
        valid = False

    return valid

def timer_finished(btn, p_btn, time_begun):

    time_begun[1] = True
    btn.config(text = "Begin Timer")
    p_btn.grid_remove()

def start_timer_thread(timer, work_var, rest_var, longrest_var, session_var, time_begun, btn, p_btn):
    """
    Starts running the countdown timer with a thread.

    Args:
        timer(Timer)
        time1(int)
        time2(int)
        time3(int)

    """

    # - the _var variables are the ones that have the active variable (eg - stringvar) whereas just the name is the its .get() version

    work = work_var.get()
    rest = rest_var.get()
    longrest = longrest_var.get()
    session = session_var.get()

    # Another set of validation to ensure that a blankspace won't cause an error
    if work == "":
        work = "0"
    if rest == "":
        rest = "0"
    if longrest == "":
        longrest = "0"
    if session in ("", "0"):
        session = "1" # Session must be 1 for the timer to progress

    timer.work_time = int(work)*60
    timer.rest_time = int(rest) * 60 # Add an extra second towards rest_time because the pomodoro jumps over one second on the rest in display
    timer.longrest_time = int(longrest) * 60
    timer.sessions = int(session)

    # Reset the input boxes
    work_var.set("")
    rest_var.set("")
    longrest_var.set("")
    session_var.set("")
    
    timer_done = lambda: timer_finished(btn, p_btn, time_begun)

    if time_begun[1]:
        time_begun[1] = False
        btn.config(text = "End Timer")
        p_btn.grid() # Pause button only shows up once the start button has been pressed
        timer.running = True

        if not time_begun[2]:
            # Start running the thread with instance method
            separate = threading.Thread(target = timer.pomodoro_countdown, args = (window, timer_done,), daemon = True) # Needs to be a comma at args = (window,)
        else:
            separate = threading.Thread(target = timer.stopwatch, args = (window, timer_done,), daemon = True)
        
        separate.start()

    else:
        timer.running = False
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
    time_var = tk.StringVar() 
    rest_var = tk.StringVar() 
    longrest_var = tk.StringVar()
    session_var = tk.StringVar()

    # Input Validation
    check_valid = (window.register(validation), "%P")

    if choice == "pomodoro":

        # Time entries and labels initialization
        rest_label = tk.Label(window, text = "Short rest (Minutes)")
        longrest_label = tk.Label(window, text = "Long rest (Minutes)")
        session_label = tk.Label(window, text = "Sessions")
        # validatecommand links to the function that validates all of the entries
        rest_entry = tk.Entry(window, textvariable = rest_var, validate = "key", validatecommand = check_valid)
        longrest_entry = tk.Entry(window, textvariable = longrest_var, validate = "key", validatecommand = check_valid)
        session_entry = tk.Entry(window, textvariable = session_var, validate = "key", validatecommand = check_valid)

        # Labels
        rest_label.grid(row = 2, column = 0)
        longrest_label.grid(row = 3, column = 0)
        session_label.grid(row = 4, column = 0)

        # Entries
        rest_entry.grid(row = 2, column = 1)
        longrest_entry.grid(row = 3, column = 1)
        session_entry.grid(row = 4, column = 1)

        # Input Validation


    if choice == "pomodoro" or choice == "countdown":

        # Time entries and labels initialization
        time_label = tk.Label(window, text = "Minutes")
        time_entry = tk.Entry(window, textvariable = time_var, validate = "key", validatecommand = check_valid)
        
        # Labels
        time_label.grid(row = 0, column = 0)

        # Entries
        time_entry.grid(row = 0, column = 1)


    # Buttons initialization
    start_btn = tk.Button(window, text = "Begin Timer", command = lambda: start_timer_thread(timer, time_var, rest_var, longrest_var, session_var, time_paused_and_started, start_btn, pause_btn)) # Lambda allows command to pass arguments without immediately executing function
    pause_btn = tk.Button(window, text = "Pause", command = lambda: pause_timer_thread(timer, time_paused_and_started, pause_btn))

    # -- Grid Placements --

    # Buttons
    start_btn.grid(row = 5, column = 0)
    pause_btn.grid(row = 6, column = 0)
    pause_btn.grid_remove()

pomodoro_btn = tk.Button(window, text = "Pomodoro", command = lambda: main("pomodoro", False))
countdown_btn = tk.Button(window, text = "Countdown", command = lambda: main("countdown", False))
stopwatch_btn = tk.Button(window, text = "Stopwatch", command = lambda: main("stopwatch", True))

pomodoro_btn.grid(row = 2, column = 1)
countdown_btn.grid(row = 2, column = 3)
stopwatch_btn.grid(row = 2, column = 5)

window.mainloop()
