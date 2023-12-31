# blink_one_led_unihiker.py

'''
Description: Demonstrate blinking one led with UNIHIKER.
'''

# Import modules
from pingpong.board import Board, Pin
from time import sleep

# Initialize the board
Board().begin()

# Set led pin to pin 1 and set it to output
led_pin = Pin(Pin.P1, Pin.OUT)

while True:
    led_pin.write_digital(1) # Set led to high
    sleep(0.5)               # Wait 0.5 seconds
    led_pin.write_digital(0) # Set led to low
    sleep(0.5)               # Wait 0.5 seconds
    