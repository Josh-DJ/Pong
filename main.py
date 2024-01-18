from turtle import Screen
from paddle import Paddle
from ball import Ball

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = Screen()
screen.bgcolor("black")
screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
screen.title("Pong")
screen.tracer(0)


l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))

screen.listen()
screen.onkeypress(key="Up", fun=l_paddle.up)
screen.onkeypress(key="Down", fun=l_paddle.down)
screen.onkeypress(key="w", fun=r_paddle.up)
screen.onkeypress(key="s", fun=r_paddle.down)

game_on = True
while game_on:
    screen.update()

screen.exitonclick()
