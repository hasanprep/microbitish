# scroll_text_microbit.py

'''
Description: Demonstrate scrolling text with no arguments.
'''

# Import modules
from microbit import *

# Run loop forever
while True:
    display.scroll('Python') # Scroll text
    sleep(1000)              # Wait 1 second
                   