from Constants import *


class Snake:
    __snakeCoordinate = []
    __currentMove = Moves.RIGHT
    __snakeSpeed = 0
    __counter = 0

    def __init__(self):
        pair = ((COLUMNS * PX_SIZE) / 2, (ROWS * PX_SIZE) / 2)
        self.__snakeCoordinate.append(pair)

    def updatePosition(self, x: float, y: float):
        x = x % (COLUMNS * PX_SIZE)
        y = y % (ROWS * PX_SIZE)
        val = (x, y)
        for index, p in enumerate(self.__snakeCoordinate):
            temp = p
            self.__snakeCoordinate[index] = val
            val = temp

    def onMove(self, move: Moves):

        if move == Moves.NONE:
            move = self.__currentMove
        elif move != self.__currentMove:
            self.__currentMove = move
        pos = self.__snakeCoordinate[0]
        if move == Moves.RIGHT:
            self.updatePosition(pos[0] + PX_SIZE, pos[1])
        elif move == Moves.LEFT:
            self.updatePosition(pos[0] - PX_SIZE, pos[1])
        elif move == Moves.UP:
            self.updatePosition(pos[0], pos[1] - PX_SIZE)
        elif move == Moves.DOWN:
            self.updatePosition(pos[0], pos[1] + PX_SIZE)

    def getUpdateFlag(self):
        self.__counter = self.__counter + 1
        self.__snakeSpeed = len(self.__snakeCoordinate) // SPEED_fACTOR + SNAKE_SPEED
        if self.__counter + self.__snakeSpeed >= (REFRESH_RATE * 2):
            self.__counter = 0
            return True
        else:
            return False

    def getLength(self):
        return len(self.__snakeCoordinate)

    def getCoordinates(self):
        return self.__snakeCoordinate
    def getLength(self):
        return len(self.__snakeCoordinate)

    def getHead(self):
        return self.__snakeCoordinate[0]

    def grow(self):
        self.__snakeCoordinate.append(self.__snakeCoordinate[-1])
