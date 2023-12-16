# scroll_text_wait_true_microbit.py

'''
Description: Demonstrate scrolling text with wait parameter.
Note: The default wait parameter is True.
'''

# Import modules
from microbit import *

# Run loop forever
while True:
    display.scroll('Python')             # Scroll text with default wait=True
    sleep(1000)                          # Wait 1 second
    display.scroll('Python', wait=False) # Scroll text with wait=False
    sleep(1000)                          # Wait 1 second
