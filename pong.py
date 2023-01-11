import turtle
import random

game_view = turtle.Screen()
game_view.title("Pong")
game_view.setup(width=1000, height=600)
game_view.bgcolor("black")

# create left paddle
left_paddle = turtle.Turtle()
left_paddle.shape("square")
left_paddle.color("grey")
left_paddle.shapesize(stretch_wid=6, stretch_len=4)
left_paddle.penup()
left_paddle.goto(-400, 0)

# create the right paddle
right_paddle = turtle.Turtle()
right_paddle.shape("square")
right_paddle.color("red")
right_paddle.shapesize(stretch_wid=6, stretch_len=4)
right_paddle.penup()
right_paddle.goto(400, 0)

pong_ball = turtle.Turtle()
pong_ball.speed(40)
pong_ball.shape("circle")
pong_ball.color("white")
pong_ball.goto(0, 0)
pong_ball.penup()
pong_ball.dx = 5
pong_ball.dy = -5

# keep score
player_left = 0
player_right = 0


def leftpaddleUp():
    y = left_paddle.ycor()
    y += 20
    left_paddle.sety(y)


def leftpaddleDown():
    y = left_paddle.ycor()
    y -= 20
    left_paddle.sety(y)


def RightpaddleUp():
    y = right_paddle.ycor()
    y += 30
    right_paddle.sety(y)


def RightpaddleDown():
    y = right_paddle.ycor()
    y -= 30
    right_paddle.sety(y)


game_view.listen()
game_view.onkeypress(leftpaddleUp, "Up")
game_view.onkeypress(leftpaddleDown, "Down")

game_view.onkeypress(RightpaddleUp, "w")
game_view.onkeypress(RightpaddleDown, "s")


while True:
    game_view.update()
    pong_ball.setx(pong_ball.xcor() + pong_ball.dx)
    pong_ball.sety(pong_ball.ycor() + pong_ball.dy)

    # implement borders
    if pong_ball.ycor() > 280:
        pong_ball.sety(-280)
        pong_ball.dy *= -1
    if pong_ball.ycor() < -280:
        pong_ball.sety(-280)
        pong_ball.dy *= -1

    # statements for when the pall collides with the paddle
    if (pong_ball.xcor() > 340 and pong_ball.xcor() < 350) and (right_paddle.ycor() + 50 > pong_ball.ycor() - 50):
        pong_ball.setx(340)
        pong_ball.dx *= -1

    if (pong_ball.xcor() < -340 and pong_ball.xcor() > -350) and (left_paddle.ycor() + 50 > pong_ball.ycor() - 50):
        pong_ball.setx(-340)
        pong_ball.dx *= -1


turtle.done()
