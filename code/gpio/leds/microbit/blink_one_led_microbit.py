# blink_one_led_microbit.py

'''
Description: Demonstrate blinking one led.
'''

# Import modules
from microbit import *

# Set led pin to pin 1
led_pin = pin1

# Run loop forever
while True:
    led_pin.write_digital(1) # Set led to high
    sleep(500)               # Wait 0.5 seconds
    led_pin.write_digital(0) # Set led to low
    sleep(500)               # Wait 0.5 seconds