from turtle import Turtle

POSITIONS = [(-350, 0)]
MOVE_DISTANCE = 20
class Paddle:

    def __init__(self):
        self.seg = Turtle(shape="square")
        self.seg.penup()
        self.seg.color("white")
        self.seg.shapesize(stretch_wid= 3, stretch_len=.5)
        print(self.seg.turtlesize())
        self.seg.goto(POSITIONS[0])

    def up(self):
        if self.seg.ycor() < 260:
            self.seg.setposition(self.seg.xcor(),self.seg.ycor() + MOVE_DISTANCE)

    def down(self):
        if self.seg.ycor() > -260:
            self.seg.setposition(self.seg.xcor(), self.seg.ycor() - MOVE_DISTANCE)