import tkinter as tk
from tkinter import ttk
import time
import sys
import threading

class Timer:
    """
    Docstring for Timer
    """
    def __init__(self, total_time:int):
        self.time = total_time
        self.pause_event = threading.Event()
        # total time become work time make new var total time + shor tbreak +long break

    def countdown(self, window):
        """
        Simple countdown total_timer based on the user's input

        Args:
            
        """
        
        self.pause_event.set()
        timer_display = tk.Label(window)
        timer_display.grid(row = 4, column = 4)

        # Main timer loop
        while self.total_time >= 0:

            self.pause_event.wait() # this checks to see whether the event is set/cleared (running/paused)
            
            hour = int(self.total_time // 3600)
            min = int((self.total_time % 3600) // 60)
            sec = int(self.total_time % 60)
            
            # Display amount of time left
            timer_display.config(text = f"There's {hour:02d}:{min:02d}:{sec:02d} left")

            # Let the second pass
            time.sleep(1)

            # Reduce timer
            self.total_time -= 1  
        
        print("timer over")
 

    def pomodoro(self):
        pass

    def stopwatch(self):
        pass


