from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score1 = 0
        self.score2 = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0,240)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f'{self.score1} : {self.score2}', align="center", font= ("Arial", 50, "normal"))

    def increase_score1(self):
        self.score1 += 1
        self.update_score()

    def increase_score2(self):
        self.score2 += 1
        self.update_score()






