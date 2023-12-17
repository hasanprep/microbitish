# scroll_text_monospace_microbit.py

# Import modules
from microbit import *

# Run forever loop 
while True:
    display.scroll('Python', delay=500)                 # Scroll text with default font monospace=False
    sleep(1000)                                         # Wait 1 second
    display.scroll('Python', delay=500, monospace=True) # Scroll text with monospace=True
    sleep(1000)                                         # Wait 1 second