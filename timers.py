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

    def pomodoro_countdown(self, window, timer_done):
        """
        Args:
            
        """
        
        self.pause_event.set()
        timer_display = tk.Label(window)
        timer_display.grid(row = 4, column = 4)

        # Loop timer for every session
        for num in range(self.sessions):

            # If the timer isn't running, end the loop
            if not self.running:
                break

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

                # Ends the loop, completing the thread
                if not self.running:
                    break

            # Long break occurs every 3 working sessions
            if num % 3 == 0 and num != 0:
                
                resting = self.longrest_time

                while resting >= 0:
                # Ends the loop, completing the thread
                    if not self.running:
                        break

                    self.pause_event.wait() 

                    timer_display.config(text = f"there's {(resting//3600):02d}:{(resting%3600//60):02d}:{(resting%60):02d} left")
                    resting -= 1
                    time.sleep(1)

        timer_display.grid_forget()
        # Whenever a loop has finished, call timer_done to complete it.
        window.after(0, timer_done)


    def stopwatch(self, window, timer_done):

        self.pause_event.set()
        timer_display = tk.Label(window)
        timer_display.grid(row = 4, column = 4)

        while self.running:

            self.pause_event.wait()

            timer_display.config(text = f"{(int(self.work_time)//3600):02d}:{(int(self.work_time)%3600//60):02d}:{(int(self.work_time)%60):02d}:{int(round(self.work_time % 1, 1)*10)}")

            self.work_time += 0.1

            time.sleep(0.1)

        timer_display.grid_forget() # remove display if the stopwatch is no longer running]
        window.after(0, timer_done)
