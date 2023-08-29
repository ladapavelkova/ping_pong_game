from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.goto(0,0)
        self.shape("circle")
        self.color("white")
        self.penup()
        self.xmove = 10
        self.ymove = 10


    def move(self):
        x = self.xcor() + self.xmove
        y = self.ycor() + self.ymove
        self.goto(x, y)

    def bounce(self):
        self.ymove *= -1

    def bounce1(self):
        self.xmove *= -1

    def reset_position(self):
        self.goto(0,0)
        self.bounce1()