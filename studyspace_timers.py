import tkinter as tk
from tkinter import ttk
import time
import sys
import threading

class Timer:
    def __init__(self, countdown_time:int, timer_running:bool):
        self.countdown_time = countdown_time * 60
        self.timer_running = timer_running
        self.pause_event = threading.Event
        self.pause_event.set()

    def countdown(self, window):
        
        timer_display = tk.Label(window)
        timer_display.grid(row = 4, column = 4)
        # Main timer loop
        while self.countdown_time >= 0:

            self.pause_event.wait()
            
            hour = int(self.countdown_time // 3600)
            min = int(self.countdown_time // 60)
            sec = int(self.countdown_time % 60)
            
            # Print amount of time left
            timer_display.config(text = f"There's {hour}:{min}:{sec} left")

            # Let the second pass
            time.sleep(1)

            # Reduce timer
            self.countdown_time -= 1  
 

    def pomodoro(self):
        pass

    def stopwatch(self):
        pass


