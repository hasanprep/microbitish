# scroll_text_monospace_microbit.py

# Import modules
from microbit import *

# Run forever loop 
while True:
    display.scroll('Python', monospace=True) # Scroll text in monospace font
    sleep(1000)                              # Wait 1 second
    display.scroll('Python')                 # Scroll text in default font monospace=False
    sleep(1000)                              # Wait 1 second