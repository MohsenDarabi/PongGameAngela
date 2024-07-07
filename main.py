import time
import turtle
from turtle import Screen,Turtle

from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard
scoreboard = Scoreboard()

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350,0)
ball = Ball()

screen.listen()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")
screen.onkey(l_paddle.go_up,"q")
screen.onkey(l_paddle.go_down,"a")


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    if (ball.xcor() > 300 and ball.distance(r_paddle) <30) or ball.xcor() < -300 and ball.distance(l_paddle) <20:
        ball.bounce_x()

    # Detect R paddle miss
    if ball.xcor() > 380 and ball.distance(r_paddle) > 15:
        scoreboard.l_point()
        ball.reset_position()

    # Detect L Paddle miss
    if ball.xcor() < -380 and ball.distance(l_paddle) > 15:
        scoreboard.r_point()
        ball.reset_position()
















screen.exitonclick()

