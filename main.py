import turtle
from turtle import Screen,Turtle

from paddle import Paddle

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

paddle_1 = Paddle(350,0)
paddle_2 = Paddle(-350,0)
def go_up():
    paddle_1.goto(paddle_1.xcor(), paddle_1.ycor()+20)

def go_down():
    paddle_1.goto(paddle_1.xcor(), paddle_1.ycor()-20)
screen.listen()
screen.onkey(go_up,"Up")
screen.onkey(go_down,"Down")

game_is_on = True
while game_is_on:
    screen.update()












screen.exitonclick()

