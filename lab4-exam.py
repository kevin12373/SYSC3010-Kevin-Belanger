from sense_hat import SenseHat
import time 
s = SenseHat()
s.low_light = True

s.show_letter("K")

count = 0

while True:
    events = s.stick.get_events()
    for event in events:
        if event.action == "pressed":
          if event.direction == "left":
                s.show_letter("K")
                time.sleep(5)
                s.clear()
                
    for event in events:
          if event.direction == "right":
                s.show_letter("D")
                time.sleep(5)
                s.clear()