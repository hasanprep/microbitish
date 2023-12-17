# temperature_simple_microbit.py

'''
Description: Demonstrate displaying temperature with onboard sensor.
Note: The temperature sensor is not very accurate.
'''

# Import modules
from microbit import *

# Run loop forever
while True:
    display.scroll(temperature()) # Display temperature in degrees Celsius
    sleep(1000)                   # Wait 1 second