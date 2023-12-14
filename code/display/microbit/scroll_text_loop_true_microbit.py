# scroll_text_loop_true_microbit.py

'''
Description: Demonstrate scrolling text with loop.
'''

from microbit import *

while True:
    display.scroll('Python', loop=True) # Scroll text with loop
    sleep(1000)                         # Wait 1 second
