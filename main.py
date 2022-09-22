
import Constants
import FruitClass
from CanvasClass import CanvasClass
from Constants import *
from SnakeClass import Snake
from tkinter import *
import keyboard

master = Tk()
fruit = FruitClass.Fruit()
snake = Snake()
canvas = CanvasClass(master)
movesList = []
SNAKE_COLOR = "white"


def detectKey():
    if keyboard.is_pressed('w'):
        onKeyPressed(Moves.UP)
    elif keyboard.is_pressed('s'):
        onKeyPressed(Moves.DOWN)
    elif keyboard.is_pressed('a'):
        onKeyPressed(Moves.LEFT)
    elif keyboard.is_pressed('d'):
        onKeyPressed(Moves.RIGHT)


def fruitEaten():
    snake.grow()
    fruit.generateFruit(snake.getCoordinates())


def moveSnake():
    if movesList:
        snake.onMove(movesList[-1])
        movesList.pop()
    else:
        snake.onMove(Moves.NONE)
    if snake.getHead() == fruit.position:
        fruitEaten()


def onKeyPressed(move: Moves):
    if move != Moves.NONE:
        if movesList:
            if movesList[0] != move:
                movesList.insert(0, move)
        else:
            movesList.insert(0, move)


def onRun(snakeColor:str):
    detectKey()
    canMoveSnake = snake.getUpdateFlag()
    if canMoveSnake:
        moveSnake()
        if changeColor(snake.getLength() // SPEED_fACTOR) != snakeColor:
            snakeColor = changeColor((snake.getLength() // SPEED_fACTOR))
            canvas.updateColor(snakeColor)

    canvas.draw(snake.getCoordinates(), canMoveSnake, fruit.position)


canvas.run(onRun)
mainloop()
