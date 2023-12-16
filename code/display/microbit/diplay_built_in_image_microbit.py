# ddiplay_built_in_image_microbit.py

'''
Description: Display built-in images on the micro:bit

Built-in images are as follows:
    - Image.ALL_ARROWS (Collection of all arrow images)
    - Image.ALL_CLOCKS (Collection of all clock images)
    - Image.ANGRY
    - Image.ARROW_E
    - Image.ARROW_N
    - Image.ARROW_NE
    - Image.ARROW_NW
    - Image.ARROW_S
    - Image.ARROW_SE
    - Image.ARROW_SW
    - Image.ARROW_W
    - Image.ASLEEP
    - Image.BUTTERFLY
    - Image.CHESSBOARD
    - Image.CLOCK1
    - Image.CLOCK2
    - Image.CLOCK3
    - Image.CLOCK4
    - Image.CLOCK5
    - Image.CLOCK6
    - Image.CLOCK7
    - Image.CLOCK8
    - Image.CLOCK9
    - Image.CLOCK10
    - Image.CONFUSED
    - Image.COW
    - Image.DIAMOND
    - Image.DIAMOND_SMALL
    - Image.DUCK
    - Image.FABULOUS
    - Image.GHOST
    - Image.GIRAFFE
    - Image.HAPPY   
    - Image.HEART
    - Image.HEART_SMALL
    - Image.HOUSE
    - Image.MEH
    - Image.MUSIC_CROTCHET
    - Image.MUSIC_QUAVER
    - Image.MUSIC_QUAVERS
    - Image.NO
    - Image.PACMAN
    - Image.PITCHFORK
    - Image.RABBIT
    - Image.ROLLERSKATE
    - Image.SAD
    - Image.SCISSORS
    - Image.SILLY
    - Image.SKULL
    - Image.SMILE
    - Image.SNAKE
    - Image.SQUARE
    - Image.SQUARE_SMALL
    - Image.STICKFIGURE
    - Image.SURPRISED
    - Image.SWORD
    - Image.TARGET
    - Image.TORTOISE
    - Image.TRIANGLE
    - Image.TRIANGLE_LEFT
    - Image.TSHIRT
    - Image.UMBRELLA
    - Image.XMAS
    - Image.YES
'''

# Import modules
from microbit import *

# Run forever
while True:
    display.show(Image.HEART)       # Display a heart
    sleep(500)                      # Wait 0.5 seconds
    display.show(Image.HEART_SMALL) # Display a small heart
    sleep(500)                      # Wait 0.5 seconds
