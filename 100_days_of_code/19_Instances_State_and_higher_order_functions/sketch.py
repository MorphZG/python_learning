from turtle import Turtle, Screen


# create Turtle()
tim = Turtle()
# create Screen()
screen = Screen()

# assignment
# build Etch a Sketch kids game
# turtle should make a simple drawings on keypress

# turtle already have functions to move in these directions but i want it
# to happen on key press by calling turtle.onkey(function, key)
# it accepts functions with no arguments so i must create higher order
# function with no arguments to call another function with defined parameters

def forward():
    ''' move forward 50 steps '''
    tim.forward(5)

def backward():
    ''' move backward 50 steps '''
    tim.back(5)

def left():
    ''' turn counter-clockwise '''
    tim.left(5)

def right():
    ''' turn clockwise '''
    tim.right(5)

# start listening the key presses
screen.listen()
# define the events, call functions on key press.
screen.onkey(fun=forward, key='w')
screen.onkey(fun=backward, key='s')
screen.onkey(fun=left, key='a')
screen.onkey(fun=right, key='d')
screen.onkey(fun=tim.reset, key='c')  # clear and reset the screen

screen.exitonclick()

#modules: turtle
#tags:event listener, higher order function,
