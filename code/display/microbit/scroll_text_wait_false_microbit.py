# scroll_text_wait_false_microbit.py

'''
Description: Demonstrate scrolling text without wait.
'''

# Import modules
from microbit import *

# Run loop forever
while True:
    display.scroll('Python', wait=False) # Scroll text without wait
    sleep(1000)                          # Wait 1 second
