from random import randint
from Constants import *


class Fruit:

    def isValidCoordinate(self, coordinate, coordinates: []):
        for i in coordinates:
            if coordinate == i:
                return False
        if coordinate == self.position:
            return False
        return True

    def getRandom(self, coordinates: []):
        xc = randint(0, COLUMNS-1) * PX_SIZE
        yc = randint(0, ROWS-1) * PX_SIZE
        while not self.isValidCoordinate((xc, yc), coordinates):
            xc = randint(0, COLUMNS) * PX_SIZE
            yc = randint(0, ROWS) * PX_SIZE
        return xc, yc

    def generateFruit(self, coordinates: []):
        item = self.getRandom(coordinates)
        self.position = item

    def __init__(self):
        self.position = (10 * PX_SIZE, 10 * PX_SIZE)
