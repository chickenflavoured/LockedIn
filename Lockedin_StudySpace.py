# import tkinter as tk
# from tkinter import ttk

import time
import sys

# class Timer:
#     def __init__(self,)

def countdown_timer(countdown_time:int):

    # Turn minutes into seconds
    countdown_time *= 60
    running = True
    
    # Main timer loop
    while countdown_time >= 0 and running == True:
        
        hour = int(countdown_time // 3600)
        min = int(countdown_time // 60)
        sec = int(countdown_time % 60)
        
        # Print amount of time left
        print(f"\rThere's {hour}:{min}:{sec} left", end ="", flush = True )

        # Let the second pass
        time.sleep(1)

        # Reduce timer
        countdown_time -= 1    

    print("Time's up")

countdown_timer(2.5)


class Timer:
    def __init__(self, countdown_time:int, timer_running:bool):
        self.countdown_time = countdown_time
        self.timer_running = timer_running

    def pause_time(self):
        pass
    
    def stop_time(self):
        pass

    def reset_time(self):
        pass

    def start_time(self):
        pass
