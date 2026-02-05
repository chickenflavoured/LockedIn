import time
import sys

class Timer:
    def __init__(self, countdown_time:int, timer_running:bool):
        self.countdown_time = countdown_time * 60
        self.timer_running = timer_running

    def countdown(self):
    
        # Main timer loop
        while self.countdown_time >= 0 and self.timer_running == True:
            
            hour = int(self.countdown_time // 3600)
            min = int(self.countdown_time // 60)
            sec = int(self.countdown_time % 60)
            
            # Print amount of time left
            print(f"\rThere's {hour}:{min}:{sec} left", end ="", flush = True )

            # Let the second pass
            time.sleep(1)

            # Reduce timer
            self.countdown_time -= 1    

        print("Time's up")


    def pomodoro(self):
        pass

    def stopwatch(self):
        pass



