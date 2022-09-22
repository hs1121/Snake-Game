from tkinter import *

import Constants
from Constants import *

canvas_height = ROWS * PX_SIZE
canvas_width = COLUMNS * PX_SIZE


class CanvasClass:
    __snakeBody = []
    __fruitBody = None
    __snakeColor = changeColor(0)

    def __init__(self, root):
        self.window = Canvas(root, width=canvas_width, height=canvas_height)
        self.window.configure(background='black')
        self.window.pack()

    def updateColor(self, color):
        self.__snakeColor = color
        for viewId in self.__snakeBody:
            self.window.itemconfigure(viewId, fill=color)

    def draw(self, snakeCoordinates: [], updateSnake: bool, fruitCoordinate):
        fruitId = self.window.create_oval(fruitCoordinate[0], fruitCoordinate[1], fruitCoordinate[0] + FRUIT_SIZE,
                                          fruitCoordinate[1] + FRUIT_SIZE, fill="red", width=2)
        if self.__fruitBody is not None:
            self.window.delete(self.__fruitBody)
        self.__fruitBody = fruitId

        if updateSnake:
            if self.__snakeBody and len(snakeCoordinates) == len(self.__snakeBody):
                self.window.delete(self.__snakeBody.pop())
            x = snakeCoordinates[0][0]
            y = snakeCoordinates[0][1]
            rec = self.window.create_rectangle(x, y, x + SNAKE_SIZE, y + SNAKE_SIZE,
                                               fill=self.__snakeColor)
            self.__snakeBody.insert(0, rec)

    def run(self, callback):
        callback(self.__snakeColor)
        self.window.after(REFRESH_RATE, self.run, callback)
