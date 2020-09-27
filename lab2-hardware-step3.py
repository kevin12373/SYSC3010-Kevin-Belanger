#temperature sensor using the sense hat

import random
from sense_emu import SenseHat

s = SenseHat()

print('Temperature is shown when up is pressed')

def temperature(event):
    if event.action == 'pressed':
        print ('The current temperature is now:', random.randint(-30, 40))
    
s.stick.direction_up = temperature

    