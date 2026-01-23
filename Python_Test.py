import tkinter as tk
from tkinter import ttk
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
HEIGHT = 900
WIDTH = 1800
# Window display size
window.geometry(f"{WIDTH}x{HEIGHT}")

# citation, oral helper, focus timer, td list
windows_on = [False, False, False, False]

def main_menu():
    # Create new window for the main menu

    start_btn.destroy()

    citation_btn = tk.Button(window, 
                             text = "Citation Machine", 
                             command = citation_machine,
                             fg = "white",
                             bg = "blue",
                             font = ("Cabin", 12),
                             width = 15,
                             height = 2)
    citation_btn.place(x = WIDTH/3, y = HEIGHT/2)
    
    presentation_btn = tk.Button(window, text = "Presentation Helper", command = oral_helper)
    presentation_btn.place(x = WIDTH/5, y = HEIGHT/2)

    timer_btn = tk.Button(window, text = "Focus Timer", command = focus_timer)
    timer_btn.place(x = WIDTH/2, y = HEIGHT/2)

    td_btn = tk.Button(window, text = "To-Do List", command = td_list)
    td_btn.place(x = WIDTH-WIDTH/8, y = HEIGHT/2)

def citation_machine():
    if windows_on[0] == False:
        citation_window = tk.Toplevel(window) # Toplevel is used as inheritence so that when window closes it also closes
        windows_on[0] = True

def oral_helper():
    if windows_on[1] == False:
        oral_helper_window = tk.Toplevel(window)
        windows_on[1] = True

def focus_timer():
    if windows_on[2] == False:
        focus_time_window = tk.Toplevel(window)
        windows_on[2] = True

def td_list():
    if windows_on[3] == False:
        td_list_window = tk.Toplevel(window)
        windows_on[3] = True

# Function executes when button is pressed
start_btn = tk.Button(window, text = "Start", command = main_menu)
# Sets button on screen (place is the same as pack but it defines its location)
start_btn.place(x = WIDTH/2,
                  y = HEIGHT/2)

# Goes at the end of everything that should execute
window.mainloop()