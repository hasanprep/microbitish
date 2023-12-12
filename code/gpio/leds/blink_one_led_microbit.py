from microbit import *

# Set led pin to pin 1
led = pin1

while True:
    led.write_digital(1) # Set led to high
    sleep(500)           # Wait 0.5 seconds
    led.write_digital(0) # Set led to low
    sleep(500)           # Wait 0.5 seconds