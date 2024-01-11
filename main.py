from turtle import Screen
from paddle import Paddle

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = Screen()
screen.bgcolor("black")
screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
screen.title("Pong")
screen.tracer(0)


paddle = Paddle()

screen.listen()
screen.onkeypress(key="Up", fun=paddle.up)
screen.onkeypress(key="Down", fun=paddle.down)

game_on = True
while game_on:
    screen.update()

screen.exitonclick()
