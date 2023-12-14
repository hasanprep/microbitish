# scroll_text_wait_true_microbit.py

'''
Description: Demonstrate scrolling text with wait.
'''

# Import modules
from microbit import *

# Run loop forever
while True:
    display.scroll('Python', wait=True) # Scroll text with wait
    sleep(1000)                         # Wait 1 second
