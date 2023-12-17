# blink_ramdom_pixel_microbit.py

'''
Description: Demonstrate blinking random pixel.
'''

# Import modules
from microbit import *
from random import randint 

# Run loop forever
while True:
    x = randint(0, 4)   # Generate random number between 0 and 4
    y = randint(0, 4)   # Generate random number between 0 and 4
    val = randint(1, 9) # Generate random number between 0 and 9

    display.set_pixel(x, y, val) # Set random pixel to high
    sleep(10)                    # Wait 0.5 seconds
    display.set_pixel(x, y, 0)   # Set random pixely to low
    sleep(10)                    # Wait 0.5 seconds