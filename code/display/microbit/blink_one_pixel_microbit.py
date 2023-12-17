# blink_one_pixel_microbit.py

'''
Description: Demonstrate blinking one pixel.
'''

# Import modules
from microbit import *

# Run loop forever
while True:
    display.set_pixel(2, 2, 9) # Set pixel to high
    sleep(500)                 # Wait 0.5 seconds
    display.set_pixel(2, 2, 0) # Set pixel to low
    sleep(500)                 # Wait 0.5 seconds