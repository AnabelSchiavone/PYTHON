seconds = 0
minutes = 0
hours = 0

import time
import turtle

t1 = turtle.Turtle()
while True:
    t1.clear()
    t1.write(str(hours).zfill(2) + ":" + str (minutes).zfill(2) + ":"+ str (seconds).zfill(2), font = ("arial", 25, "normal"))
    seconds = seconds + 1
    time.sleep(1)
    if seconds == 60:
        seconds = 0
        minutes = minutes + 1
        
