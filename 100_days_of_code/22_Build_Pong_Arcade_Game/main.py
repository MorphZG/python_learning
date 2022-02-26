from turtle import Screen, Turtle

from paddle import Paddle

LEFT_POSITION = (-350, 0)
RIGHT_POSITION = (350, 0)

screen = Screen()
screen.title('Pong Arcade')
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.tracer(0)  # improve the drawing of complex graphics, read documentation

# create the paddles
left_pad = Paddle(LEFT_POSITION)
right_pad = Paddle(RIGHT_POSITION)
screen.update()  # if screen.tracer(0) manual screen update is necesary

# listen for screen events
screen.listen()
# up movement
screen.onkeypress(left_pad.move_up, 'Up')
screen.onkeypress(right_pad.move_up, 'w')
# down movement
screen.onkeypress(left_pad.move_down, 'Down')
screen.onkeypress(right_pad.move_down, 's')

game_on = True
while game_on:
    screen.update()  # if screen.tracer(0) manual screen update is necesary


screen.exitonclick()
#modules: turtle,
#tags: pong game,
