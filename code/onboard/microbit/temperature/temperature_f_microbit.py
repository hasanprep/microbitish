# temperation_f_microbit.py

'''
Description: Demonstrate displaying temperature in Fahrenheit.
Note: The temperature sensor is not very accurate.
'''

# Import modules
from microbit import *

# Run loop forever
while True:
    temp_f = round(temperature() * 9 / 5 + 32) # Convert temperature to Fahrenheit
    display.scroll(temp_f)                     # Display temperature in degrees Fahrenheit
    sleep(1000)                                # Wait 1 second