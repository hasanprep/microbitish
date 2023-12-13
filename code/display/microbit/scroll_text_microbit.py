from microbit import *

while True:
    display.scroll('Python')             # Scroll text
    sleep(1000)
    display.scroll('Python', delay=100)  # Scroll text with 100ms delay``
    sleep(1000)
    display.scroll('Python', delay=50)   # Scroll text with 50ms delay
    sleep(1000)
    display.scroll('Python', delay=25)   # Scroll text with 25ms delay
    sleep(1000)
    display.scroll('Python', delay=10)   # Scroll text with 10ms delay
    sleep(1000)
    display.scroll('Python', delay=1)    # Scroll text with 1ms delayq
    sleep(1000)
    display.scroll('Python', delay=0)    # Scroll text with 0ms delay
    sleep(1000)
    display.scroll('Python', loop=True)  # Scroll text with loop
    sleep(1000)
    display.scroll('Python', loop=False) # Scroll text without loop
    sleep(1000)
    display.scroll('Python', wait=True)  # Scroll text with wait
    sleep(1000)
    display.scroll('Python', wait=False) # Scroll text without wait
                   