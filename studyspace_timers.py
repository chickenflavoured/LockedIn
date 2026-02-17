import tkinter as tk
from tkinter import ttk
import time
import sys
import threading

class Timer:
    """
    Docstring for Timer
    """
    def __init__(self, countdown_time:int):
        self.countdown_time = countdown_time
        self.pause_event = threading.Event()

    def countdown(self, window):
        
        self.pause_event.set()
        timer_display = tk.Label(window)
        timer_display.grid(row = 4, column = 4)
        # Main timer loop
        while self.countdown_time >= 0:

            self.pause_event.wait()
            
            hour = int(self.countdown_time // 3600)
            min = int((self.countdown_time % 3600) // 60)
            sec = int(self.countdown_time % 60)
            
            # Print amount of time left
            timer_display.config(text = f"There's {hour:02d}:{min:02d}:{sec:02d} left")

            # Let the second pass
            time.sleep(1)

            # Reduce timer
            self.countdown_time -= 1  
 

    def pomodoro(self):
        pass

    def stopwatch(self):
        pass


