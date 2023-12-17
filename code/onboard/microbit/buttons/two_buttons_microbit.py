# two_buttons_microbit.py

'''
Description: Demonstrate using two buttons.
'''

# Import modules
from microbit import *

# Run loop forever
while True:
    if button_a.is_pressed() and button_b.is_pressed():   # If button A and B are pressed
        display.show('AB')                                # Show 'AB'
    elif button_a.is_pressed():                           # If button A is pressed
        display.show('A')                                 # Show 'A'
    elif button_b.is_pressed():                           # If button B is pressed
        display.show('B')                                 # Show 'B'
    else:                                                 # Otherwise  
        display.clear()                                   # Clear display
    sleep(100)                                            # Wait 0.1 seconds