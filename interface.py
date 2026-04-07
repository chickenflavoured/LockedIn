import tkinter as tk
import subprocess
"""
 NOTES

 my_button = tk.Button(
     window,
     text="Click Me",
     command=on_button_click,
     fg="white",           # Foreground (text) color
     bg="blue",            # Background color
     font=("Arial", 12),   # Font and size
     width=15,             # Width in characters
     height=2,             # Height in text lines
     bd=0,                 # No border
     relief=tk.FLAT        # Flat relief
 )
"""


# Initializes window display
window = tk.Tk()
# Constants
HEIGHT = 400
WIDTH = 400
# Window display size
window.geometry(f"{WIDTH}x{HEIGHT}")

# citation, oral helper, focus timer, td list
windows_on = [False, False, False, False]

def main_menu():
    # Create new window for the main menu

    start_btn.destroy()

    citation_btn = tk.Button(window, text = "Citation Machine", command = citation_machine)
    citation_btn.grid(row=0, column=0, padx=40, pady=40)
    
    presentation_btn = tk.Button(window, text = "Presentation Helper", command = oral_helper)
    presentation_btn.grid(row=1, column=0, padx=40, pady=40)

    timer_btn = tk.Button(window, text = "Study Timer", command = focus_timer)
    timer_btn.grid(row=0, column=1, padx=40, pady=40)

    td_btn = tk.Button(window, text = "To-Do List", command = td_list)
    td_btn.grid(row=1, column=1, padx=40, pady=40)

    td_btn = tk.Button(window, text = "Study Music", command = music)
    td_btn.grid(row=2, column=0, padx=40, pady=40)


def citation_machine():
    subprocess.Popen(["python", "citations.py"])

def oral_helper():
    subprocess.Popen(["python", "oral.py"])

def focus_timer():
    subprocess.Popen(["python", "study_timers.py"])

def td_list():
    subprocess.Popen(["python", "task_interface.py"])

def music():
    subprocess.Popen(["python", "music.py"])

# Function executes when button is pressed
start_btn = tk.Button(window, text = "Start", command = main_menu)
# Sets button on screen (place is the same as pack but it defines its location)
start_btn.place(x = WIDTH/2,
                  y = HEIGHT/2)

# Goes at the end of everything that should execute
window.mainloop()
