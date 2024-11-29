from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()

screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Ping_Pong_game")
screen.tracer(0)


l_paddle = Paddle((-385, 0))
r_paddle = Paddle((375, 0))
ball = Ball()
score = Scoreboard()


screen.listen()

screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")
screen.onkeyrelease(l_paddle.go_up, "w")
screen.onkeyrelease(l_paddle.go_down, "s")
screen.onkeypress(r_paddle.go_up, "o")
screen.onkeypress(r_paddle.go_down, "l")
screen.onkeyrelease(r_paddle.go_up, "o")
screen.onkeyrelease(r_paddle.go_down, "l")


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move_right()

    # Detect collision with the wall
    if ball.ycor() > 280.0 or ball.ycor() < -280.0:
        ball.bounce_y()

    # Detect collision with paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 360 or ball.distance(l_paddle) < 50 and ball.xcor() < -370:
        ball.bounce_x()

    # Detect when right paddle misses
    if ball.xcor() > 400 or ball.ycor() > 300:
        ball.reset_position()
        score.l_point()

    # Detect when left paddle misses
    if ball.xcor() < -400 or ball.ycor() < -300:
        ball.reset_position()
        score.r_point()


screen.exitonclick()
