from turtle import Turtle
UP= 90
DOWN = 270

class Paddle(Turtle):
    def __init__(self,x,y):
        super().__init__()
        self.goto(x,y)
        self.speed("fastest")
        self.setheading(270)
        self.shape("square")
        self.shapesize(1,5,1)
        self.color("white")

    def up(self):
        self.penup()
        self.speed("fastest")
        new_y = self.ycor() + 20
        self.goto(self.xcor(),new_y)


    def down(self):
        self.penup()
        self.speed("fastest")
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)


    def nahoru(self):
        self.penup()
        self.speed("fastest")
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)


    def dolu(self):
        self.penup()
        self.speed("fastest")
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)



