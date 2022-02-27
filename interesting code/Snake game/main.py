from turtle import Screen, Turtle
import time

from paddle import Paddle
from ball import Ball

LEFT_POSITION = (-370, 0)
RIGHT_POSITION = (370, 0)

screen = Screen()
screen.title('Pong Arcade')
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.tracer(0)  # improve the drawing of complex graphics, read documentation

# class instances
left_pad = Paddle(LEFT_POSITION)
right_pad = Paddle(RIGHT_POSITION)
ball = Ball()

# listen for screen events
screen.listen()
# up movement
screen.onkeypress(left_pad.move_up, 'w')
screen.onkeypress(right_pad.move_up, 'Up')
# down movement
screen.onkeypress(left_pad.move_down, 's')
screen.onkeypress(right_pad.move_down, 'Down')


game_on = True
while game_on:
    time.sleep(0.1)  # slow down the update of screen
    screen.update()  # if screen.tracer(0) manual screen update is necesary
    ball.move()

    # detect collision with top and bottom wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # detect collision with the paddle
    if (ball.distance(right_pad) < 50 and ball.xcor() > 350
            or ball.distance(left_pad) < 50 and ball.xcor() < -350):
        ball.bounce_x()

    # detect when paddle misses the ball       <! --- WORK IN PROGRESS!
    if ball.xcor() > 350 or ball.xcor() < -350:
        ball.goto(0, 0)
        game_on = False


screen.exitonclick()

#modules: turtle, time
#tags: pong game, coordinates, oop,
