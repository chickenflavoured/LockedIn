import tkinter as tk
from tkinter import ttk
import time
import sys
import threading

class Timer:
    """
    Docstring for Timer
    """
    def __init__(self, work_time, rest_time, longrest_time, sessions, running):
        self.work_time = work_time
        self.rest_time = rest_time
        self.longrest_time = longrest_time
        self.sessions = sessions
        self.running = running
        self.pause_event = threading.Event()
        # total time become work time make new var total time + shor tbreak +long break

    def pomodoro_countdown(self, window):
        """
        Simple countdown total_timer based on the user's input

        Args:
            
        """
        
        self.pause_event.set()
        timer_display = tk.Label(window)
        timer_display.grid(row = 4, column = 4)

        # Loop timer for every session
        for num in range(self.sessions):

            total_time = self.work_time + self.rest_time
            # Main timer countdown + rest loop
            while total_time >= 0:
                
                self.pause_event.wait() # Checks to see whether the event is set/cleared (running/paused)

                working = int(total_time - self.rest_time)

                # Work time
                if total_time >= self.rest_time:
                    timer_display.config(text = f"there's {(working//3600):02d}:{(working%3600//60):02d}:{(working%60):02d} left")
                # Rest time
                else:
                    timer_display.config(text = f"there's {(total_time//3600):02d}:{(total_time%3600//60):02d}:{(total_time%60):02d} left")

                total_time -= 1
                
                time.sleep(1)

                if not self.running:
                    self.sessions = 0
                    total_time = 0
                    timer_display.destroy()

            # Long break occurs every 3 working sessions
            if num % 3 == 0 and num != 0:
                
                resting = self.longrest_time

                while resting >= 0:

                    self.pause_event.wait() 

                    timer_display.config(text = f"there's {(resting//3600):02d}:{(resting%3600//60):02d}:{(resting%60):02d} left")
                    resting -= 1
                    time.sleep(1)



    def stopwatch(self, window):

        self.pause_event.set()
        timer_display = tk.Label(window)
        timer_display.grid(row = 4, column = 4)

        while self.running:

            self.pause_event.wait()

            timer_display.config(text = f"{(int(self.work_time)//3600):02d}:{(int(self.work_time)%3600//60):02d}:{(int(self.work_time)%60):02d}:{int(round(self.work_time % 1, 1)*10)}")

            self.work_time += 0.1

            time.sleep(0.1)

        timer_display.destroy() # remove display if the stopwatch is no longer running
