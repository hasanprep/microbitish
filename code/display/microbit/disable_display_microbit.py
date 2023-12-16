# disable_display_microbit.py

'''
Description: This program disables the display on the micro:bit to access
the pins theat are used by the display (pins 3, 4, 6, 7, and 10).
'''

# Import modules
from microbit import *

# Disable display
display.disable() # This enables pins 3, 4, 6, 7, and 10 without the display 

# Set led_pin to pin3
led_pin = pin3 

# Run loop forever
while True:
    led_pin.write_digital(1) # Turn LED on
    sleep(1000)              # Wait 1 second
    led_pin.write_digital(0) # Turn LED off
    sleep(1000)              # Wait 1 second
