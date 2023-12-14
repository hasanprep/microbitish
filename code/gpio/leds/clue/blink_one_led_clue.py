# blink_one_led_clue.py

'''
Description: Demonstrate blinking one led with CLUE.
'''

# Import modules
import board
import digitalio
from time import sleep

# Set led pin to pin 1 and set it to output
led_pin = digitalio.DigitalInOut(board.D1)

while True:
    led_pin.value = True  # Set led to high
    sleep(0.5)            # Wait 0.5 seconds
    led_pin.value = False # Set led to low
    sleep(0.5)            # Wait 0.5 seconds
    