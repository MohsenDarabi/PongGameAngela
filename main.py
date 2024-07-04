import turtle
from turtle import Screen,Turtle
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")

paddle = Turtle()
paddle.shape("square")
paddle.shapesize(stretch_wid=5, stretch_len=1)
paddle.color("white")
paddle.penup()
paddle.goto(350, 0)

def go_up():
    paddle.goto(paddle.xcor(), paddle.ycor()+20)

def go_down():
    paddle.goto(paddle.xcor(), paddle.ycor()-20)
screen.listen()
screen.onkey(go_up,"Up")
screen.onkey(go_down,"Down")














screen.exitonclick()

