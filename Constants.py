import random
from enum import Enum

PX_SIZE = 15
ROWS = 40
COLUMNS = 50

SNAKE_SIZE = PX_SIZE
FRUIT_SIZE = PX_SIZE+2
REFRESH_RATE = 1000 // 200      #time at which the freames update
SNAKE_SPEED = 1     # initial speed
SPEED_fACTOR = 10   #Increase speed after given number of fruits are eaten


class Moves(Enum):
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3
    NONE = -1


def changeColor(pos):
    # de = ("%02x" % random.randint(0, 255))
    # re = ("%02x" % random.randint(0, 255))
    # we = ("%02x" % random.randint(0, 255))
    # ge = "#"
    # color = ge + de + re + we
    colors = ["white", "purple", "orange", "yellow", "green", "blue", "indigo", "violet"]
    return colors[pos % 8]
