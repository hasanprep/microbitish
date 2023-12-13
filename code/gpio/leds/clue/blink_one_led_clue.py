import board
import digitalio
from time import sleep

# Set led pin to pin 1 and set it to output
led = digitalio.DigitalInOut(board.D1)

while True:
    led.value = True  # Set led to high
    sleep(0.5)        # Wait 0.5 seconds
    led.value = False # Set led to low
    sleep(0.5)        # Wait 0.5 seconds