import tkinter as tk
from tkinter import ttk
from timers import Timer
import threading
from tkextrafont import Font


window = tk.Tk()

HEIGHT = 200
WIDTH = 400

# Window display size
window.geometry(f"{WIDTH}x{HEIGHT}")

# Background
bg = tk.PhotoImage(file = "g_study_timers.png")
bg_label = tk.Label(window, image = bg)
bg_label.place(x = 0, y = 0)

# Font
font = Font(file="sniglet.ttf", family="Sniglet")
window.option_add("*Font", "Sniglet 10")

# Changing colours of entries, labels, and buttons
window.option_add('*Button.Background', "#d06caa")
window.option_add('*Button.Foreground', 'white')
window.option_add('*Entry.background', '#d06caa')
window.option_add('*Entry.foreground', 'white')
window.option_add('*Label.background', '#d06caa')
window.option_add('*Label.foreground', 'white')

# Stops the user from entering full screen
window.resizable(False, False) 


def validation(P):
    """
    Validates so that the user can only enter numbers.

    Args:
        P(int)

    Returns:
        valid(Bool)

    """

    if P == 0 or P.isdigit():
        valid = True
    else:
        valid = False

    return valid

def timer_finished(btn, p_btn, b_btn, time_begun):
    """
    Resets UI once the timer has naturally ended (ended without the user manually ending it with a button).

    Args:
        btn(tk.Button): "Begin Timer"
        p_btn(tk.Button): "Pause/Resume"
        b_btn(tk.Button): "Back"
        time_begun(list[Bool])
    """

    time_begun[1] = True # Ensures that the "Begin Timer" button will reappear since the timer has ended.
    btn.config(text = "Begin Timer")
    p_btn.grid_remove()
    b_btn.grid()

def start_timer_thread(timer, work_var, rest_var, longrest_var, session_var, time_begun, btn, p_btn, b_btn):
    """
    Starts running the countdown timer with a thread.

    Args:
        work_var(tk.stringVar)
        rest_var(tk.stringVar)
        longrest_var(tk.stringVar)
        session_var(tk.stringVar)

        time_begun(list[Bool])

        btn(tk.Button): "Begin Timer"
        p_btn(tk.Button): "Pause/Resume"
        b_btn(tk.Button): "Back"

    """
    
    # Obtain the str from the tk.stringVar
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
        session = "1" # Session must be 1 for the timer to progress (Pomodoro or Countdown)

    timer.work_time = int(work)*60
    timer.rest_time = int(rest) * 60 
    timer.longrest_time = int(longrest) * 60
    timer.sessions = int(session)

    # Reset the input boxes after timer has started
    work_var.set("")
    rest_var.set("")
    longrest_var.set("")
    session_var.set("")
    
    # Unsure of how this works
    timer_done = lambda: timer_finished(btn, p_btn, b_btn, time_begun)

    # Timer has begun
    if time_begun[1]:
        time_begun[1] = False
        btn.config(text = "End Timer")
        p_btn.grid() # Pause button only shows up once the start button has been pressed
        b_btn.grid_remove() # The user cannot go back unless the timer is over
        timer.running = True

        if not time_begun[2]: # If the timer is not a stopwatch
            # Start running the thread with instance method
            separate = threading.Thread(target = timer.pomodoro_countdown, args = (window, timer_done,), daemon = True) # begins a thread with a timer (Thread allows code to run in parallel, so users can interact with the interface at the same time the timer is running.)
        else: # timer is a stopwatch
            separate = threading.Thread(target = timer.stopwatch, args = (window, timer_done,), daemon = True)
        
        # Start the threads
        separate.start()

    # Timer has not begun
    else:
        timer.running = False
        time_begun[1] = True
        btn.config(text = "Begin Timer")
        b_btn.grid()

def pause_timer_thread(timer, time_paused, btn):
    """
    Pauses and resumes the running timer and updates UI.

    Args:
        timer(Timer)
        time_paused(list[bool])
        btn(tk.Button): "Pause/Resume"

    """
    
    # Timer is paused
    if not time_paused[0]:
        time_paused[0] = True
        btn.config(text = "Resume")
        timer.pause_event.clear() #.clear() pauses the thread attribute in timer
    # Timer is not paused
    else:
        time_paused[0] = False
        btn.config(text = "Pause")
        timer.pause_event.set() #.set() resumes the thread attribute in timer


def main(choice, is_stopwatch):
    """
    Initializes variables for timers and displays correct UI based on the selected timer.

    Args:
        choice(str): Variable in charge of keeping track of what timer the user has selected
        is_stopwatch(Bool)

    """

    # Remove the buttons
    for item in window.winfo_children():
        if item != bg_label:
            item.destroy() # The buttons are destroyed so that they do not take too much memory space

    # Create instance of Timer Class
    timer = Timer(0, 0, 0, 0, True)

    # Variable keeping track of the timer.
    # [0] -> Whether the user is pausing or resuming the timer (False -> Pause button has not appeared)
    # [1] -> Whether the user is beginning or ending the timer. (False -> Start Timer button has not appeared)
    # [2] -> Whether it is a stopwatch (False -> is not a stopwatch)
    time_paused_and_started = [False, True, is_stopwatch]

    # Variables (Pomodoro and Countdown)
    time_var = tk.StringVar() 
    rest_var = tk.StringVar() 
    longrest_var = tk.StringVar()
    session_var = tk.StringVar()

    # Input Validation, If function, validation, returns False, nothing will appear in entry
    check_valid = (window.register(validation), "%P")

    # Entry and label displays based on whether the timer is Pomodoro or Countdown
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
        rest_label.grid(row = 2, column = 0, padx = 10, pady = 2)
        longrest_label.grid(row = 3, column = 0, padx = 10, pady = 2)
        session_label.grid(row = 4, column = 0, padx = 10, pady = 2)

        # Entries
        rest_entry.grid(row = 2, column = 1, padx = 10, pady = 2)
        longrest_entry.grid(row = 3, column = 1, padx = 10, pady = 2)
        session_entry.grid(row = 4, column = 1, padx = 10, pady = 2)


    if choice == "pomodoro" or choice == "countdown":

        # Time entries and labels initialization
        time_label = tk.Label(window, text = "Minutes")
        time_entry = tk.Entry(window, textvariable = time_var, validate = "key", validatecommand = check_valid)
        
        # Labels grid
        time_label.grid(row = 0, column = 0, padx = 10, pady = 5)

        # Entries grid
        time_entry.grid(row = 0, column = 1, padx = 10, pady = 5)


    # Buttons initialization
    # In charge of beginning and ending the timer -> function: start_timer_thread
    start_btn = tk.Button(window, text = "Begin Timer", command = lambda: start_timer_thread(timer, time_var, rest_var, longrest_var, session_var, time_paused_and_started, start_btn, pause_btn, back_btn)) # Lambda allows command to pass arguments without immediately executing function
    # In charge of pausing and resuming the timer -> function: timer_paused_and_started
    pause_btn = tk.Button(window, text = "Pause", command = lambda: pause_timer_thread(timer, time_paused_and_started, pause_btn))
    # Allows user to return to starting screen -> function: start
    back_btn = tk.Button(window, text = "Back", command = start)

    # -- Grid Placements --

    # Buttons
    start_btn.grid(row = 5, column = 0, padx = 10, pady = 2)
    pause_btn.grid(row = 6, column = 0, padx = 10, pady = 2)
    back_btn.grid(row = 6, column = 0, padx = 10, pady = 2)
    pause_btn.grid_remove()

def start():
    """
    Starting screen of the program, allows user to select between 3 timers (pomodoro, countdown, stopwatch).

    """

    # Clear all the buttons on screen
    for item in window.winfo_children():
        if item != bg_label:
            item.destroy()

    # Timer buttons
    pomodoro_btn = tk.Button(window, text = "Pomodoro", command = lambda: main("pomodoro", False))
    countdown_btn = tk.Button(window, text = "Countdown", command = lambda: main("countdown", False))
    stopwatch_btn = tk.Button(window, text = "Stopwatch", command = lambda: main("stopwatch", True))

    # Timer buttons grid
    pomodoro_btn.grid(row = 2, column = 1, padx = 5, pady = 10)
    countdown_btn.grid(row = 2, column = 3, padx = 5, pady = 10)
    stopwatch_btn.grid(row = 2, column = 5, padx = 5, pady = 10)

# launches the starting screen
start()

window.mainloop()
