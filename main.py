from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard
from boarder import Boarder


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

l_paddle = Paddle(-350, 0)
r_paddle = Paddle(+350, 0)
scoreboard = Scoreboard()
boarder = Boarder()
ball = Ball()


screen.listen()
screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, "Down")
screen.onkey(l_paddle.move_up, "w")
screen.onkey(l_paddle.move_down, "s")


is_game_on = True
while is_game_on:
    time.sleep(ball.move_speed)
    ball.move()
    screen.update()
    # detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    # detect collision with r_paddle
    if ball.distance(r_paddle) < 45 and ball.xcor() > 330:
        ball.bounce_x()

    # detect collision with l_paddle
    if ball.distance(l_paddle) < 45 and ball.xcor() < -330:
        ball.bounce_x()

    # Detect r_paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # Detect l_paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()
screen.exitonclick()
