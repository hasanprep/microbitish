# display_custom_image_microbit.py

'''
Description: Demonstrate displaying custom image.
'''

# Import modules
from microbit import *

# Create custom image
curl = Image('99887:'
             '00007:'
             '22106:'
             '30006:'
             '34455:')

display.show(curl) # Display custom image