# scroll_text_delay_microbit.py

'''
Description: Demonstrate scroll text with various delays.
'''

# Import modules
from microbit import *

# Run loop forever
while True:
    display.scroll('Python', delay=100) # Scroll text with 100ms delay``
    sleep(1000)                         # Wait 1 second
    display.scroll('Python', delay=50)  # Scroll text with 50ms delay
    sleep(1000)                         # Wait 1 second
    display.scroll('Python', delay=25)  # Scroll text with 25ms delay
    sleep(1000)                         # Wait 1 second
    display.scroll('Python', delay=10)  # Scroll text with 10ms delay
    sleep(1000)                         # Wait 1 second
    display.scroll('Python', delay=1)   # Scroll text with 1ms delayq
    sleep(1000)                         # Wait 1 second 
    display.scroll('Python', delay=0)   # Scroll text with 0ms delay
    sleep(1000)                         # Wait 1 second
    