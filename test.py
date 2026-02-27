import tkinter as tk
from tkinter import ttk
from timers import Timer
import time

# window = tk.Tk()

# HEIGHT = 600
# WIDTH = 600
# # Window display size
# window.geometry(f"{WIDTH}x{HEIGHT}")

# def doSmt(timer):
#     timer.pomodoro(window)

# time_var1 = tk.IntVar() 
# time_entry1 = tk.Entry(window, textvariable = time_var1)

# timer = Timer()

# time_entry1.grid(row = 0, column = 1)

# time = time_var1.get()

# start_btn = tk.Button(window, text = "Begin Timer", command = lambda: doSmt(timer)) # Lambda allows command to pass arguments without immediately executing function

# start_btn.grid(row = 6, column = 0)

# window.mainloop()

time1 = 3
short_rest = 1
long_rest = 10
num_sessions = 2

total_session = (time1 + short_rest)*num_sessions + long_rest

while total_session >= 0:
    
    # hour = int(time1 // 3600))
    # min = int((time1 % 3600) // 60)
    # sec = int(time1 % 60)

    hour = int(total_session - short_rest)
    
    # Display amount of time left
    if total_session == 0:
        if num_sessions > 0:
            num_sessions -= 1
            total_session = time1 + short_rest
        elif num_sessions == 0:
            total_session = long_rest
    elif total_session == long_rest:
        print(f"\r(long break) there's {long_rest} left")
        long_rest -= 1
        total_session -= 1
        if total_session == 0 and long_rest == 0:
            total_session = -1
    elif total_session <= short_rest:
        print(f"\r(Break) There's {total_session} left", end = "")
        print(f"Num sessions left: {num_sessions}")
        total_session -= 1  
    else:
        print(f"\r There's {hour:02d} left", end = "")
        print(f"Num sessions left: {num_sessions}")
        total_session -= 1  

    time.sleep(1)


    # Reduce timer

while total_session >= 0:

    if total_session == 

print("timer over")