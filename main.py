from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = Screen()
screen.bgcolor("black")
screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
screen.title("Pong")
screen.tracer(0)


l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))
ball = Ball()

screen.listen()
screen.onkeypress(key="Up", fun=l_paddle.up)
screen.onkeypress(key="Down", fun=l_paddle.down)
screen.onkeypress(key="w", fun=r_paddle.up)
screen.onkeypress(key="s", fun=r_paddle.down)

game_on = True
while game_on:
    time.sleep(0.1)
    screen.update()
    ball.move()
    # Collision with top/bottom wall
    if ball.ycor() > 290 or ball.ycor() < -290:
        #Bounce ball
        ball.bounce()

    # Collision with paddle. Checks distance away from paddle and also x coord of ball from paddle.
    if (ball.distance(l_paddle) < 30 and ball.xcor() < -330) or (ball.distance(r_paddle) < 30 and ball.xcor() > 330):
        #Paddle hit
        ball.hit()

    # Collision with left/right walls
    if ball.xcor() > 390:
        # Left paddle gets a point
        l_paddle.score += 1
        ball.reset_position()

    elif ball.xcor() < -390:
        # Right paddle gets a point
        r_paddle.score += 1
        ball.reset_position()

screen.exitonclick()
