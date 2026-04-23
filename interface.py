import tkinter as tk
import subprocess

# Initializes window display
window = tk.Tk()

# Constants
HEIGHT = 400
WIDTH = 400

# Window display size
window.geometry(f"{WIDTH}x{HEIGHT}")

# Track processes
td_process = None

# citation, oral helper, focus timer, td list
windows_on = [False, False, False, False]

bg = tk.PhotoImage(file = "main_interface.png")
bg_label = tk.Label(window, image = bg)
bg_label.place(x = 0, y = 0)


def main_menu():
    start_btn.destroy()

    citation_btn = tk.Button(window, text="Citation Machine", command=citation_machine)
    citation_btn.grid(row=0, column=0, padx=40, pady=40)

    presentation_btn = tk.Button(window, text="Presentation Helper", command=oral_helper)
    presentation_btn.grid(row=1, column=0, padx=40, pady=40)

    timer_btn = tk.Button(window, text="Study Timer", command=focus_timer)
    timer_btn.grid(row=0, column=1, padx=40, pady=40)

    td_btn = tk.Button(window, text="To-Do List", command=handle_td)
    td_btn.grid(row=1, column=1, padx=40, pady=40)

    music_btn = tk.Button(window, text="Study Music", command=music)
    music_btn.grid(row=2, column=0, padx=40, pady=40)


def citation_machine():
    subprocess.Popen(["python", "citations.py"])


def oral_helper():
    subprocess.Popen(["python", "oral.py"])


def focus_timer():
    subprocess.Popen(["python", "study_timers.py"])


def td_list(td_process):
    if td_process is None or td_process.poll() is not None:
        td_process = subprocess.Popen(["python", "task_interface.py"])
        windows_on[3] = True
    return td_process


def handle_td():
    global td_process
    td_process = td_list(td_process)


def music():
    subprocess.Popen(["python", "music.py"])


# Start button
start_btn = tk.Button(window, text="Start", command=main_menu)
start_btn.place(x=WIDTH/2, y=HEIGHT/2)

# Run app
window.mainloop()
