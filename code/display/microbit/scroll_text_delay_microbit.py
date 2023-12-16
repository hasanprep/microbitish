# scroll_text_delay_microbit.py

'''
Description: Demonstrate scroll text with various delays.
Note: The defsult delay parameter is 150ms.
'''

# Import modules
from microbit import *

# Run loop forever
while True:
    display.scroll('150ms:')            # Display the delay time
    display.scroll('Python')            # Scroll text with default delay of 150ms
    sleep(1000)                         # Wait 1 second
    display.scroll('100ms:')            # Display the delay time
    display.scroll('Python', delay=100) # Scroll text with 100ms delay``
    sleep(1000)                         # Wait 1 second
    display.scroll('50ms:')             # Scroll text with default delay of 150ms Display the delay time
    display.scroll('Python', delay=50)  # Scroll text with 50ms delay
    sleep(1000)                         # Wait 1 second
    display.scroll('25ms:')             # Display the delay time
    display.scroll('Python', delay=25)  # Scroll text with 25ms delay
    sleep(1000)                         # Wait 1 second
    display.scroll('10ms:')             # Display the delay time
    display.scroll('Python', delay=10)  # Scroll text with 10ms delay
    sleep(1000)                         # Wait 1 second
    display.scroll('5ms:')              # Display the delay time
    display.scroll('Python', delay=1)   # Scroll text with 1ms delayq
    sleep(1000)                         # Wait 1 second 
    display.scroll('0ms:')              # Display the delay time
    display.scroll('Python', delay=0)   # Scroll text with 0ms delay
    sleep(1000)                         # Wait 1 second
    