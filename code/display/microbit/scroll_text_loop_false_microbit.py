# scroll_text_loop_false_microbit.py

'''
Description: Demonstrate scrolling text without loop.
'''

# Import modules
from microbit import *

# Run loop forever
while True:
    display.scroll('Python', loop=False) # Scroll text without loop
    sleep(1000)                          # Wait 1 second
