from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from score import Score
import time



timmy = Turtle()
screen = Screen()
screen.tracer(0)
player1 = Paddle(350,0)
player2 = Paddle(-350,0)
ball = Ball()
score = Score()

screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PING-PONG")


timmy.speed("fastest")
timmy.goto(0, 300)
timmy.color("white")
timmy.setheading(270)
timmy.pensize(15)
for _ in range(8):
    timmy.forward(40)
    timmy.penup()
    timmy.forward(40)
    timmy.pendown()


screen.listen()
screen.onkey(player1.up,"Up")
screen.onkey(player1.down,"Down")
screen.onkey(player2.nahoru,"s")
screen.onkey(player2.dolu,"y")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    if ball.ycor() == 280 or ball.ycor() == -280:
        ball.bounce()

    if ball.distance(player1) <50 and ball.xcor() > 320 or ball.distance(player2) < 50 and ball.xcor() < -320:
        ball.bounce1()

    if ball.xcor() > 380:
        ball.reset_position()
        score.increase_score1()

    if ball.xcor() < -380:
        ball.reset_position()
        score.increase_score2()


screen.exitonclick()
