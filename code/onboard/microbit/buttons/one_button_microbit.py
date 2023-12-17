# one_button_microbit.py

'''
Description: Demonstrate one button.
'''

# Import modules
from microbit import *

# Run loop forever
while True:
    if button_a.is_pressed(): # If button a is pressed
        display.show('A')     # Show happy face
    else: # Otherwise
        display.clear()       # Clear display
    sleep(100)                # Wait 0.1 seconds