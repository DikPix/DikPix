# Built with python 3, dependencies installed with pip 
# library to generate images - Pillow 
# https://pillow.readthedocs.io/en/stable/installation.html
from PIL import Image

# library to work with arrays 
# https://numpy.org/
import numpy as np

# library to interact with the operating system
import os

# library to generate random integer values
from random import seed
from random import randint

# gets path to be used in image creation mechanism, using os
dirname = os.path.dirname(os.path.abspath(__file__))

# sets final image dimensions as 120x120 pixels
# the original 50x50 pixel image will be expanded to these dimensions
dimensions = 120, 120

# tells how many times to iterate through the following mechanism
# which equals the number of dicks
# e.g. 
# for x in range(0-200) 
# would generate 201 dicks numbered 0-200
for x in range(0, 100):

    # using ETH block number as starting random number seed
    a=11981207
    seed(x+a)

    #skin color - randomly generate each number in an RGB color
    b = randint(1,5)
    if b == 1:
        # if random number is 1 >> pale skin
        hd = (255, 219, 172)
    elif b == 2:
        # if random number is 2 >> light skin
        hd = (241, 194, 125)
    elif b == 3:
        # if random number is 3 >> tanned skin
        hd = (224, 172, 105)
    elif b == 4:
        # if random number is 4 >> brown skin
        hd = (198, 134, 66)
    else:
        # if random number is 5 >> dark skin
        hd = (141, 85, 36)

    c=randint(0,500)
    seed(c)

    #inner outline color
    th = (191, 120, 59) 
    d = randint(0,1000)
    seed(d)

    #eye "white" color
    # if random number between 1-1000 is 47 or less - Crazy Eyes!
    if d > 47:
        # normal eyes are always the same color
        ew = (240,248,255)
        ey = (0, 0, 0)
    else:
        # crazy eyes have the same (154, 0, 0) pupil and a random 'eye black' color
        ew = (240,248,255)
        ey = (randint(0, 256), randint(0, 256), randint(0, 256))
    e = randint(0,1000)
    seed(e)

    # lips color
    f = randint(0, 1000)
    if f > 500:
        # if random number is 501-1000 >> lightest shade pink lips
        bk = (219,172,152)
    elif 500 >= f > 47:
        # 48-500 >> light pink
        bk = (238,193,173)
    elif 47 >= f > 7:
        # 8 >> 47 >> darker pink lips
        bk = (210,153,133)
    else:
        # random number is 7 or less >> darkest pink lips
        bk = (227,93,106)

    # background color
    bg = (238, 238, 238)

    # outline color
    ol = (82, 42, 8)

    # first 17 rows are the head
    basic_head = [
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ol,bg,ol,ol,ew,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ol,ol,ol,th,hd,ol,ew,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ol,th,hd,ol,th,hd,th,ol,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ol,hd,hd,hd,hd,hd,hd,th,ol,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ol,hd,ew,hd,hd,hd,hd,ew,hd,th,ol,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ol,th,ew,ew,ew,hd,hd,hd,ew,ew,th,ol,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ol,hd,ew,ew,hd,hd,hd,hd,ew,ew,hd,th,ol,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ol,hd,ew,ew,hd,hd,hd,hd,hd,ew,ew,th,ol,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ol,th,hd,ew,ew,hd,hd,hd,hd,hd,hd,ew,th,ol,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ol,th,hd,ew,hd,th,th,hd,hd,hd,th,hd,hd,ol,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ol,th,hd,hd,th,ol,ol,th,hd,th,ol,ol,th,ol,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ol,th,hd,ol,ol,th,hd,hd,hd,hd,hd,ol,ol,ol,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ol,ol,ol,ol,th,hd,hd,hd,hd,hd,hd,th,ol,ol,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ol,ol,th,th,hd,hd,hd,hd,hd,hd,hd,ol,ol,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ol,th,hd,hd,th,ol,hd,hd,th,hd,th,ol,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
    ]

    # middle 10 rows are the shaft
    basic_shaft = [
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ol,th,hd,th,ol,th,hd,hd,ol,ol,th,ol,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ol,th,hd,hd,hd,hd,hd,hd,hd,hd,th,ol,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ol,th,hd,hd,th,th,hd,th,th,hd,th,ol,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ol,th,hd,th,ew,ew,th,ew,ew,ew,th,ol,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ol,th,hd,ew,ey,ew,th,ew,ey,ew,th,ol,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ol,th,hd,ew,ey,ey,hd,ew,ey,ey,th,ol,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ol,th,ew,ew,ew,ew,hd,ew,ew,ew,th,ol,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ol,th,ew,th,th,th,hd,th,th,th,th,ol,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ol,th,ew,ew,ew,hd,hd,hd,hd,hd,th,ol,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ol,th,ew,hd,bk,hd,hd,hd,bk,hd,th,ol,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
    ]

    # last 23 rows are the balls
    basic_balls = [
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ol,th,hd,hd,bk,hd,hd,hd,bk,hd,ol,ol,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ol,th,ew,hd,bk,bk,th,bk,bk,hd,th,ol,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ol,th,ew,hd,th,bk,bk,bk,th,hd,th,ol,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ol,th,hd,ew,ew,hd,th,bk,th,hd,hd,th,ol,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ol,hd,hd,ew,hd,hd,hd,hd,hd,hd,hd,th,ol,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ol,hd,hd,hd,hd,hd,hd,hd,hd,hd,hd,th,th,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ol,hd,hd,hd,hd,hd,hd,hd,hd,hd,hd,th,ol,ol,ol,ol,hd,ew,bg,bg,bg,bg,bg,ew,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ol,th,hd,hd,hd,hd,hd,hd,hd,hd,hd,hd,th,ol,hd,hd,th,ol,th,ew,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ol,hd,hd,hd,hd,hd,hd,hd,hd,hd,hd,hd,th,th,hd,hd,hd,hd,ol,th,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ol,th,hd,hd,hd,hd,hd,hd,hd,hd,hd,hd,hd,hd,hd,ew,ew,ew,ew,hd,ol,ew,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,th,ol,ol,ol,ol,ol,th,hd,hd,hd,hd,hd,hd,hd,hd,hd,hd,hd,ew,ew,ew,ew,hd,th,th,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ol,ol,th,hd,hd,hd,th,th,hd,hd,hd,hd,hd,hd,hd,hd,hd,hd,hd,ew,ew,ew,ew,hd,th,ol,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ol,th,hd,hd,hd,hd,hd,hd,hd,hd,hd,hd,hd,th,th,th,hd,hd,hd,hd,ew,ew,ew,ew,hd,th,ol,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,th,ol,hd,hd,ew,ew,ew,hd,hd,hd,hd,hd,hd,hd,th,ol,ol,th,hd,hd,hd,hd,ew,ew,hd,hd,ol,ol,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ol,th,hd,ew,ew,ew,ew,ew,hd,hd,hd,hd,hd,hd,hd,th,ol,th,hd,hd,hd,hd,hd,hd,hd,th,ol,th,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ol,th,hd,ew,ew,bg,ew,ew,hd,hd,hd,hd,hd,hd,hd,th,ol,th,hd,hd,hd,hd,hd,hd,th,ol,ol,ew,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ol,th,hd,ew,ew,ew,ew,hd,hd,hd,hd,hd,hd,hd,hd,ol,ol,th,th,th,hd,th,th,ol,ol,ol,ew,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ol,th,hd,hd,ew,ew,hd,hd,hd,hd,hd,hd,hd,hd,th,ol,ol,ol,ol,ol,ol,ol,ol,ol,th,ew,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ol,th,hd,hd,hd,hd,hd,hd,hd,hd,hd,hd,th,ol,ol,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ol,ol,th,hd,hd,hd,hd,hd,hd,hd,th,th,ol,ol,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ol,ol,ol,th,th,th,th,th,ol,ol,ol,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ol,ol,ol,ol,ol,ol,ol,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
    ]

    # first 17 rows are the head, this will add a beret as a hat
    cool_head = [
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ey,ey,ey,ey,ey,ey,ey,ey,ey,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ey,ey,ey,ey,ey,ey,ey,ey,ew,ey,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ey,ey,ey,ey,ey,ey,ey,ey,ew,ey,ey,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ew,ey,ey,ey,ey,ey,ey,ey,ew,ey,ew,ey,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ey,ey,ey,ey,ey,ey,ey,ey,ey,ey,ey,ey,ey,ey,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ey,ey,ey,ey,ey,ey,ey,ey,ey,ey,ey,hd,th,ol,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ey,ey,ol,th,ew,ew,ew,hd,hd,hd,ew,ew,th,ol,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ey,bg,ol,hd,ew,ew,hd,hd,hd,hd,ew,ew,hd,th,ol,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ol,hd,ew,ew,hd,hd,hd,hd,hd,ew,ew,th,ol,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ol,th,hd,ew,ew,hd,hd,hd,hd,hd,hd,ew,th,ol,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ol,th,hd,ew,hd,th,th,hd,hd,hd,th,hd,hd,ol,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ol,th,hd,hd,th,ol,ol,th,hd,th,ol,ol,th,ol,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ol,th,hd,ol,ol,th,hd,hd,hd,hd,hd,ol,ol,ol,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ol,ol,ol,ol,th,hd,hd,hd,hd,hd,hd,th,ol,ol,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ol,ol,th,th,hd,hd,hd,hd,hd,hd,hd,ol,ol,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ol,th,hd,hd,th,ol,hd,hd,th,hd,th,ol,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
    ]

    # middle 10 rows are the shaft, this will add shades as eyewear
    cool_shaft = [
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ol,th,hd,th,ol,th,hd,hd,ol,ol,th,ol,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ol,th,hd,hd,hd,hd,hd,hd,hd,hd,th,ol,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ol,th,hd,hd,th,th,hd,th,th,hd,th,ol,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ey,ey,ey,ey,ey,ey,ey,ey,ey,ey,ey,ey,ey,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ey,ol,ey,ey,ew,ey,ey,th,ey,ew,ey,ey,ol,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ol,th,ey,ey,ew,ey,hd,ey,ey,ew,ey,ol,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ol,th,ew,ey,ey,ey,hd,ey,ey,ey,th,ol,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ol,th,ew,th,th,th,hd,th,th,th,th,ol,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ol,th,ew,ew,ew,hd,hd,hd,hd,hd,th,ol,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ol,th,ew,hd,hd,hd,hd,hd,hd,hd,th,ol,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],

    ]

    # last 23 rows are the balls, this will add a joint to smoke
    cool_balls = [
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ol,th,hd,hd,bk,hd,hd,hd,ey,ey,ol,ol,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ol,th,ew,hd,bk,bk,th,bk,bk,ew,ey,ol,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ol,th,ew,hd,th,bk,bk,bk,hd,ey,ew,ey,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ol,th,hd,ew,ew,hd,th,bk,th,hd,ey,ew,ew,ey,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ol,hd,hd,ew,hd,hd,hd,hd,hd,hd,hd,ey,ew,ey,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ol,hd,hd,hd,hd,hd,hd,hd,hd,hd,hd,ey,ew,ey,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ol,hd,hd,hd,hd,hd,hd,hd,hd,hd,hd,ey,ew,ey,ol,ol,hd,ew,bg,bg,bg,bg,bg,ew,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ol,th,hd,hd,hd,hd,hd,hd,hd,hd,hd,hd,ey,ew,ew,ey,th,ol,th,ew,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ol,hd,hd,hd,hd,hd,hd,hd,hd,hd,hd,hd,ey,ew,ew,ew,ey,hd,ol,th,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ol,th,hd,hd,hd,hd,hd,hd,hd,hd,hd,hd,hd,hd,ey,ew,ew,ew,ey,hd,ol,ew,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,th,ol,ol,ol,ol,ol,th,hd,hd,hd,hd,hd,hd,hd,hd,hd,hd,hd,ey,ew,ew,ew,ey,th,th,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ol,ol,th,hd,hd,hd,th,th,hd,hd,hd,hd,hd,hd,hd,hd,hd,hd,hd,ew,ey,ew,ew,bk,ey,ol,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ol,th,hd,hd,hd,hd,hd,hd,hd,hd,hd,hd,hd,th,th,th,hd,hd,hd,hd,ew,ew,ey,bk,bk,ey,ol,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,th,ol,hd,hd,ew,ew,ew,hd,hd,hd,hd,hd,hd,hd,th,ol,ol,th,hd,hd,hd,hd,ew,ew,ey,ey,ol,ol,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ol,th,hd,ew,ew,ew,ew,ew,hd,hd,hd,hd,hd,hd,hd,th,ol,th,hd,hd,hd,hd,hd,hd,hd,th,ol,th,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ol,th,hd,ew,ew,bg,ew,ew,hd,hd,hd,hd,hd,hd,hd,th,ol,th,hd,hd,hd,hd,hd,hd,th,ol,ol,ew,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ol,th,hd,ew,ew,ew,ew,hd,hd,hd,hd,hd,hd,hd,hd,ol,ol,th,th,th,hd,th,th,ol,ol,ol,ew,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ol,th,hd,hd,ew,ew,hd,hd,hd,hd,hd,hd,hd,hd,th,ol,ol,ol,ol,ol,ol,ol,ol,ol,th,ew,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ol,th,hd,hd,hd,hd,hd,hd,hd,hd,hd,hd,th,ol,ol,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ol,ol,th,hd,hd,hd,hd,hd,hd,hd,th,th,ol,ol,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ol,ol,ol,th,th,th,th,th,ol,ol,ol,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ol,ol,ol,ol,ol,ol,ol,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
    ]

    # first 17 rows are the head, same as basic_head
    frankie_head = [
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ol,bg,ol,ol,ew,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ol,ol,ol,th,hd,ol,ew,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ol,th,hd,ol,th,hd,th,ol,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ol,hd,hd,hd,hd,hd,hd,th,ol,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ol,hd,ew,hd,hd,hd,hd,ew,hd,th,ol,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ol,th,ew,ew,ew,hd,hd,hd,ew,ew,th,ol,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ol,hd,ew,ew,hd,hd,hd,hd,ew,ew,hd,th,ol,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ol,hd,ew,ew,hd,hd,hd,hd,hd,ew,ew,th,ol,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ol,th,hd,ew,ew,hd,hd,hd,hd,hd,hd,ew,th,ol,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ol,th,hd,ew,hd,th,th,hd,hd,hd,th,hd,hd,ol,ew,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ol,th,hd,hd,th,ol,ol,th,hd,th,ol,ol,th,ol,ew,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ol,th,hd,ol,ol,th,hd,hd,hd,hd,hd,ol,ol,ol,hd,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ol,ol,ol,ol,th,hd,hd,hd,hd,hd,hd,th,ol,ol,hd,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ol,ol,th,th,hd,hd,hd,hd,hd,hd,hd,ol,ol,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ol,th,hd,hd,th,ol,hd,hd,th,hd,th,ol,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
    ]

    # middle 10 rows are the shaft, this will add the glasses as eyewear
    frankie_shaft = [
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ol,th,hd,th,ol,th,hd,hd,ol,ol,th,ol,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ol,th,hd,hd,hd,hd,hd,hd,hd,hd,th,ol,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ey,ey,ey,ey,ey,ey,ey,ey,ey,ey,ey,ey,ol,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ol,th,ey,ew,ew,ew,ey,ew,ew,ew,ey,ol,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ol,th,ey,ew,ey,ew,ey,ew,ey,ew,ey,ol,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ol,th,ey,ew,ey,ey,ey,ew,ey,ey,ey,ol,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ol,th,ey,ew,ew,ew,ey,ew,ew,ew,ey,ol,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ol,th,ey,ey,ey,ey,ey,ey,ey,ey,ey,ol,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ol,th,ew,ew,ew,hd,hd,hd,hd,hd,th,ol,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ol,th,ew,hd,hd,hd,hd,hd,hd,hd,th,ol,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
   ]

    # last 23 rows are the balls, this will add a beard as facial hair
    frankie_balls = [
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ol,th,th,th,th,th,th,th,th,th,th,ol,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ol,th,th,th,ew,ew,ew,ew,ew,th,th,ol,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ol,th,th,th,ew,ew,ew,ew,ew,th,th,ol,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ol,th,th,th,th,th,ew,ew,ew,th,th,th,ol,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ol,ol,th,th,th,th,th,th,th,th,th,th,ol,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ol,hd,ol,th,th,th,th,th,th,th,th,ol,ol,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ol,hd,hd,ol,th,th,th,th,th,th,ol,th,ol,ol,ol,ol,hd,ew,bg,bg,bg,bg,bg,ew,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ol,th,hd,hd,hd,ol,ol,ol,ol,ol,ol,hd,th,ol,hd,hd,th,ol,th,ew,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ol,hd,hd,hd,hd,hd,hd,hd,hd,hd,hd,hd,th,th,hd,hd,hd,hd,ol,th,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ol,th,hd,hd,hd,hd,hd,hd,hd,hd,hd,hd,hd,hd,hd,ew,ew,ew,ew,hd,ol,ew,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,th,ol,ol,ol,ol,ol,th,hd,hd,hd,hd,hd,hd,hd,hd,hd,hd,hd,ew,ew,ew,ew,hd,th,th,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ol,ol,th,hd,hd,hd,th,th,hd,hd,hd,hd,hd,hd,hd,hd,hd,hd,hd,ew,ew,ew,ew,hd,th,ol,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ol,th,hd,hd,hd,hd,hd,hd,hd,hd,hd,hd,hd,th,th,th,hd,hd,hd,hd,ew,ew,ew,ew,hd,th,ol,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,th,ol,hd,hd,ew,ew,ew,hd,hd,hd,hd,hd,hd,hd,th,ol,ol,th,hd,hd,hd,hd,ew,ew,hd,hd,ol,ol,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ol,th,hd,ew,ew,ew,ew,ew,hd,hd,hd,hd,hd,hd,hd,th,ol,th,hd,hd,hd,hd,hd,hd,hd,th,ol,th,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ol,th,hd,ew,ew,bg,ew,ew,hd,hd,hd,hd,hd,hd,hd,th,ol,th,hd,hd,hd,hd,hd,hd,th,ol,ol,ew,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ol,th,hd,ew,ew,ew,ew,hd,hd,hd,hd,hd,hd,hd,hd,ol,ol,th,th,th,hd,th,th,ol,ol,ol,ew,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ol,th,hd,hd,ew,ew,hd,hd,hd,hd,hd,hd,hd,hd,th,ol,ol,ol,ol,ol,ol,ol,ol,ol,th,ew,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ol,th,hd,hd,hd,hd,hd,hd,hd,hd,hd,hd,th,ol,ol,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ol,ol,th,hd,hd,hd,hd,hd,hd,hd,th,th,ol,ol,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ol,ol,ol,th,th,th,th,th,ol,ol,ol,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ol,ol,ol,ol,ol,ol,ol,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
    ]

    # first 17 rows are the head, this will add a cowboy hat as a hat
    cowboy_head = [
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ol,th,th,bg,bg,bg,bg,bg,th,th,ol,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ol,ol,ol,ol,th,th,th,th,th,ol,ol,ol,ol,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ol,ol,ol,ol,ol,ol,ol,ol,ol,ol,ol,ol,ol,ol,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ol,ol,ol,ol,ol,ol,ol,ol,ol,ol,ol,ol,ol,ol,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ol,ol,ol,ol,ol,ol,ol,ol,ol,ol,ol,ol,ol,ol,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ol,ol,ol,ol,ol,ol,ol,ol,ol,ol,ol,ol,ol,th,ol,ol,ol,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,th,th,th,bg,ol,ol,ol,ol,ol,ol,ol,ol,ol,ol,ol,ol,ol,th,ol,ol,ol,ol,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,th,ol,ol,ol,th,th,ol,ol,ol,ol,ol,ol,ol,ol,ol,ol,ol,ol,th,ol,ol,ol,ol,ol,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,th,ol,ol,ol,ol,ol,th,th,ey,ey,ey,ey,ey,ey,ey,ey,ey,ey,ey,ol,ol,ol,ol,ol,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,th,ol,ol,ol,ol,ol,ol,ol,th,th,ey,ey,ey,ey,ey,ey,ey,ey,ey,ol,ol,th,th,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ol,ol,ol,ol,ol,ol,ol,ol,ol,ol,th,th,th,ol,ol,ol,ol,ol,ol,th,th,th,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ol,ol,ol,ol,ol,ol,ol,ol,ol,th,ol,ol,th,th,th,th,th,th,ol,ew,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ol,ol,ol,ol,ol,ol,ol,ol,ol,th,hd,hd,hd,hd,hd,ol,ol,ol,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ol,ol,ol,ol,ol,ol,ol,th,hd,hd,hd,hd,hd,hd,th,ol,ol,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ol,ol,ol,ol,ol,th,th,hd,hd,hd,hd,hd,hd,hd,ol,ol,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ol,ol,th,hd,hd,th,ol,hd,hd,th,hd,th,ol,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
    ]

    # middle 10 rows are the shaft, same as basic_shaft
    cowboy_shaft = [
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ol,th,hd,th,ol,th,hd,hd,ol,ol,th,ol,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ol,th,hd,hd,hd,hd,hd,hd,hd,hd,th,ol,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ol,th,hd,hd,th,th,hd,th,th,hd,th,ol,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ol,th,hd,th,ew,ew,th,ew,ew,ew,th,ol,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ol,th,hd,ew,ey,ew,th,ew,ey,ew,th,ol,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ol,th,hd,ew,ey,ey,hd,ew,ey,ey,th,ol,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ol,th,ew,ew,ew,ew,hd,ew,ew,ew,th,ol,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ol,th,ew,th,th,th,hd,th,th,th,th,ol,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ol,th,ew,ew,ew,hd,hd,hd,hd,hd,th,ol,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ol,th,ew,hd,hd,hd,hd,hd,hd,hd,th,ol,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
    ]

    # last 23 rows are the balls, this will add a moustache as facial hair
    cowboy_balls = [
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ey,ey,ey,ey,hd,hd,hd,hd,hd,hd,hd,hd,ol,ol,ey,ey,ey,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ey,ey,bg,ol,ey,ew,hd,ey,ey,hd,ey,ey,hd,th,ol,ey,bg,ey,ey,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ey,ey,bg,ol,th,ew,ey,ey,ey,ey,ey,ey,ey,th,ol,bg,bg,ey,ey,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ey,ey,ol,th,hd,ey,ey,ey,ey,ey,ey,ey,ey,ey,ol,bg,bg,ey,ey,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ey,ey,ol,hd,ey,ey,ey,ey,ey,hd,ey,ey,ey,ey,ey,bg,bg,ey,ey,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ey,ey,ey,ey,ey,ey,ey,hd,hd,hd,ey,ey,ey,ey,ey,ey,ey,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ey,ey,hd,hd,hd,hd,hd,hd,hd,hd,hd,hd,th,ol,ey,ey,ol,hd,ew,bg,bg,bg,bg,bg,ew,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ol,th,hd,hd,hd,hd,hd,hd,hd,hd,hd,hd,th,ol,hd,hd,th,ol,th,ew,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ol,hd,hd,hd,hd,hd,hd,hd,hd,hd,hd,hd,th,th,hd,hd,hd,hd,ol,th,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ol,th,hd,hd,hd,hd,hd,hd,hd,hd,hd,hd,hd,hd,hd,ew,ew,ew,ew,hd,ol,ew,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,th,ol,ol,ol,ol,ol,th,hd,hd,hd,hd,hd,hd,hd,hd,hd,hd,hd,ew,ew,ew,ew,hd,th,th,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ol,ol,th,hd,hd,hd,th,th,hd,hd,hd,hd,hd,hd,hd,hd,hd,hd,hd,ew,ew,ew,ew,hd,th,ol,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ol,th,hd,hd,hd,hd,hd,hd,hd,hd,hd,hd,hd,th,th,th,hd,hd,hd,hd,ew,ew,ew,ew,hd,th,ol,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,th,ol,hd,hd,ew,ew,ew,hd,hd,hd,hd,hd,hd,hd,th,ol,ol,th,hd,hd,hd,hd,ew,ew,hd,hd,ol,ol,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ol,th,hd,ew,ew,ew,ew,ew,hd,hd,hd,hd,hd,hd,hd,th,ol,th,hd,hd,hd,hd,hd,hd,hd,th,ol,th,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ol,th,hd,ew,ew,bg,ew,ew,hd,hd,hd,hd,hd,hd,hd,th,ol,th,hd,hd,hd,hd,hd,hd,th,ol,ol,ew,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ol,th,hd,ew,ew,ew,ew,hd,hd,hd,hd,hd,hd,hd,hd,ol,ol,th,th,th,hd,th,th,ol,ol,ol,ew,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ol,th,hd,hd,ew,ew,hd,hd,hd,hd,hd,hd,hd,hd,th,ol,ol,ol,ol,ol,ol,ol,ol,ol,th,ew,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ol,th,hd,hd,hd,hd,hd,hd,hd,hd,hd,hd,th,ol,ol,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ol,ol,th,hd,hd,hd,hd,hd,hd,hd,th,th,ol,ol,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ol,ol,ol,th,th,th,th,th,ol,ol,ol,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ol,ol,ol,ol,ol,ol,ol,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
    ]

    # first 17 rows are the head, this will add a visor as a hat
    fly_head = [
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ol,bg,ol,ol,ew,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ol,ol,ol,th,hd,ol,ew,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ol,th,hd,ol,th,hd,th,ol,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ey,ey,ey,ey,hd,hd,hd,hd,hd,th,ol,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ey,bk,bk,bk,ey,ey,ey,ey,hd,hd,th,ol,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ey,bk,bk,bk,bk,bk,bk,bk,bk,ey,ew,th,ol,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ey,ey,ey,ey,ey,bk,bk,bk,bk,bk,ey,ey,ey,ey,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ey,ey,bk,bk,bk,bk,bk,ey,ey,ey,bk,bk,bk,bk,ey,ol,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ey,bk,bk,bk,bk,bk,bk,bk,bk,bk,bk,ey,ey,ey,ey,ey,ol,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ey,ey,ey,ey,ey,bk,bk,bk,bk,bk,bk,bk,bk,bk,ey,hd,hd,ol,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ey,bk,bk,ey,ol,ey,bk,bk,bk,bk,bk,bk,bk,ey,ol,ol,th,ol,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ey,ey,bg,ol,th,ey,bk,bk,bk,bk,bk,ey,hd,hd,ol,ol,ol,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ol,ol,ey,ey,ey,ey,ey,ol,hd,hd,th,ol,ol,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ol,ol,th,th,hd,hd,hd,hd,hd,hd,hd,ol,ol,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ol,th,hd,hd,th,ol,hd,hd,th,hd,th,ol,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
    ]

    # middle 10 rows are the shaft, same as basic_shaft
    fly_shaft = [
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ol,th,hd,th,ol,th,hd,hd,ol,ol,th,ol,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ol,th,hd,hd,hd,hd,hd,hd,hd,hd,th,ol,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ol,th,hd,hd,th,th,hd,th,th,hd,th,ol,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ol,th,hd,th,ew,ew,th,ew,ew,ew,th,ol,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ol,th,hd,ew,ey,ew,th,ew,ey,ew,th,ol,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ol,th,hd,ew,ey,ey,hd,ew,ey,ey,th,ol,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ol,th,ew,ew,ew,ew,hd,ew,ew,ew,th,ol,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ol,th,ew,th,th,th,hd,th,th,th,th,ol,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ol,th,ew,ew,ew,hd,hd,hd,hd,hd,th,ol,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ol,th,ew,hd,hd,hd,hd,hd,hd,hd,th,ol,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
   ]

    # last 23 rows are the balls, this will add a chain necklace
    fly_balls = [
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ol,th,hd,hd,bk,hd,hd,hd,bk,hd,ol,ol,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ol,th,ew,hd,bk,bk,th,bk,bk,hd,th,ol,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bk,bk,ew,hd,th,bk,bk,bk,th,hd,th,bk,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ol,bk,hd,ew,ew,hd,th,bk,th,hd,hd,th,bk,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ol,bk,bk,ew,hd,hd,hd,hd,hd,hd,bk,bk,bk,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ol,hd,bk,hd,hd,hd,hd,hd,hd,hd,bk,th,th,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ol,hd,bk,bk,hd,hd,hd,hd,hd,bk,bk,th,ol,ol,ol,ol,hd,ew,bg,bg,bg,bg,bg,ew,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ol,th,hd,hd,bk,hd,hd,hd,hd,hd,bk,hd,th,ol,hd,hd,th,ol,th,ew,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ol,hd,hd,hd,bk,bk,hd,bk,hd,bk,bk,hd,th,th,hd,hd,hd,hd,ol,th,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ol,th,hd,hd,hd,hd,bk,bk,bk,bk,bk,hd,hd,hd,hd,ew,ew,ew,ew,hd,ol,ew,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,th,ol,ol,ol,ol,ol,th,hd,hd,hd,hd,bk,hd,hd,hd,hd,hd,hd,ew,ew,ew,ew,hd,th,th,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ol,ol,th,hd,hd,hd,th,th,hd,hd,hd,hd,hd,hd,hd,hd,hd,hd,hd,ew,ew,ew,ew,hd,th,ol,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ol,th,hd,hd,hd,hd,hd,hd,hd,hd,hd,hd,hd,th,th,th,hd,hd,hd,hd,ew,ew,ew,ew,hd,th,ol,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,th,ol,hd,hd,ew,ew,ew,hd,hd,hd,hd,hd,hd,hd,th,ol,ol,th,hd,hd,hd,hd,ew,ew,hd,hd,ol,ol,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ol,th,hd,ew,ew,ew,ew,ew,hd,hd,hd,hd,hd,hd,hd,th,ol,th,hd,hd,hd,hd,hd,hd,hd,th,ol,th,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ol,th,hd,ew,ew,bg,ew,ew,hd,hd,hd,hd,hd,hd,hd,th,ol,th,hd,hd,hd,hd,hd,hd,th,ol,ol,ew,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ol,th,hd,ew,ew,ew,ew,hd,hd,hd,hd,hd,hd,hd,hd,ol,ol,th,th,th,hd,th,th,ol,ol,ol,ew,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ol,th,hd,hd,ew,ew,hd,hd,hd,hd,hd,hd,hd,hd,th,ol,ol,ol,ol,ol,ol,ol,ol,ol,th,ew,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ol,th,hd,hd,hd,hd,hd,hd,hd,hd,hd,hd,th,ol,ol,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ol,ol,th,hd,hd,hd,hd,hd,hd,hd,th,th,ol,ol,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ol,ol,ol,th,th,th,th,th,ol,ol,ol,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,ol,ol,ol,ol,ol,ol,ol,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
        [bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,bg,],
    ]

    # following 3 loops will choose 3 images: 1 head, 1 shaft and 1 balls
    # choose which head image to use
    seed(f)
    g = randint(0,1000)
    if g > 800:
        # if random number is 801 - 1000 >> basic head
        pixels_head = basic_head
        p = "basic head"
    elif 800 >= g > 600:
        # 601 - 800 >> cool head
        pixels_head = cool_head
        p = "cool head"
    elif 600 >= g > 400:
        # 401 - 600 >> cool head
        pixels_head = frankie_head
        p = "frankie head"
    elif 400 >= g > 200:
        # 201 - 400 >> cool head
        pixels_head = cowboy_head
        p = "cowboy head"
    else:
        # 1 - 200 >> frankie head
        pixels_head = fly_head
        p = "fly head"

    # choose which shaft image to use
    seed(g)
    h = randint(0,1000)
    if h > 800:
        # if random number is 801 - 1000 >> basic shaft
        pixels_shaft = basic_shaft
        p = "basic shaft"
    elif 800 >= h > 600:
        # 701 - 800 >> cool shaft
        pixels_shaft = cool_shaft
        p = "cool shaft"
    elif 600 >= h > 400:
        # 401 - 600 >> frankie shaft
        pixels_shaft = frankie_shaft
        p = "frankie shaft"
    elif 400 >= h > 200:
        # 201 - 400 >> cowboy shaft
        pixels_shaft = cowboy_shaft
        p = "cowboy shaft"
    else:
        # 1 - 200 >> fly shaft
        pixels_shaft = fly_shaft
        p = "fly shaft"

    # choose which balls image to use
    seed(h)
    i = randint(100,1000)
    if i > 800:
        # if random number is 801 - 1000 >> basic balls
        pixels_balls = basic_balls
        p = "basic balls"
    elif 800 >= i > 600:
        # 701 - 800  >> cool balls
        pixels_balls = cool_balls
        p = "cool balls"
    elif 600 >= i > 400:
        # 401 - 600 >> frankie balls
        pixels_balls = frankie_balls
        p = "frankie balls"
    elif 400 >= i > 200:
        # 201 - 400 >> cowboy balls
        pixels_balls = cowboy_balls
        p = "cowboy balls"
    else:
        # 1 - 200 >> fly balls
        pixels_balls = fly_balls
        p = "fly balls"

    # concatenates the 3 random sets of pixels
    pixels = np.concatenate((pixels_head, pixels_shaft, pixels_balls), axis=0)

    # convert the concatenated pixels into an array using numpy
    array = np.array(pixels, dtype=np.uint8)

    # use PIL to create an image from the new array of pixels
    new_image = Image.fromarray(array)
    new_image = new_image.resize(dimensions, resample=0)
    print(dirname + '/mickey_images/' + (str(x)) + '.png')
    imgname = dirname + '/mickey_images/' + (str(x)) + '.png'
    new_image.save(imgname)