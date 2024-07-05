import time
import turtle
from turtle import Screen,Turtle

from ball import Ball
from paddle import Paddle

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


game_is_on = True
while game_is_on:
    screen.update()
    ball.move()
    time.sleep(0.1)












screen.exitonclick()

