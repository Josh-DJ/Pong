from turtle import Turtle


MOVE_DISTANCE = 20
class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("white")
        self.shapesize(stretch_wid= 3, stretch_len=.5)
        self.goto(position)

    def up(self):
        if self.ycor() < 260:
            self.setposition(self.xcor(),self.ycor() + MOVE_DISTANCE)

    def down(self):
        if self.ycor() > -260:
            self.setposition(self.xcor(), self.ycor() - MOVE_DISTANCE)

