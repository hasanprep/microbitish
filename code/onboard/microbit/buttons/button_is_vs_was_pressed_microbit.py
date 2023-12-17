# button_is_vs_was_pressed.py

'''
TODO: Figure out what the difference is and how it can be demonstrated.
'''

# Import modules
from microbit import *

# Run loop forever
while True:
    if button_a.was_pressed(): 
        display.show('A')
    if button_b.is_pressed():
        display.show('B')
        sleep(1000)
    sleep(10000)