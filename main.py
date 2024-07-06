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

height = screen.window_height()/2
width = screen.window_width()/2
print(height)

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    #Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    if ball.xcor() > 325 or ball.xcor() < -325 and( ball.distance(r_paddle) < 15 or ball.distance(l_paddle) < 15):
        ball.bounce_x()













screen.exitonclick()

