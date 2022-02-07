from turtle import Turtle, Screen
from random import randint, choice

# read official documentation for turtle module
# create the drawing turtle called tim
tim = Turtle()
# set the shape
tim.shape('arrow')
# set the color
tim.color('black')

# create screen
screen = Screen()
screen.colormode(255)


# <! ---  exercise 1
# how to draw sqaure 100 x 100
def square(size):
    ''' draw the square on screen, :param1: int '''
    for _ in range(4):
        tim.forward(size)
        tim.right(90)


# <! --- exercise 2
# draw a dashed line
def dash_line(repetitions):
    ''' draw dashed line forward, :param1: int '''
    for _ in range(repetitions):
        tim.pendown()
        tim.forward(10)
        tim.penup()
        tim.forward(5)


# <! --- exercise 3
# draw a triangle, square, pentagon, hexagon, heptagon, octagon, nonagon and
# decagon. So start with 3 sided shape and end with 10 sided shape.
# Each of those shapes mus be drawn with random color. Each side must be
# 100 lenght long. All shapes overlayed on each other.
# Tip: Divide 360 with number of sides to get the angle degree.

def draw_shape(sides):
    ''' draw a shape with number of sides of same lenght, :param1: int '''
    angle = 360 / sides
    for _ in range(sides):
        tim.forward(100)
        tim.right(angle)

# loop from number 3 to number 10
# every iteration will randomize colors and call draw_shape()
for i in range(3, 11): # start with 3 sided shape to 10 sided shape
    # randomize the rgb value for pencolor()
    r, g, b = randint(1, 255),randint(1, 255),randint(1, 255)
    tim.pencolor(r, g, b)
    draw_shape(i)

tim.reset()


# <! --- exercise 4
# draw a random walk. use random colors, change thickens of pen,
# try to speed up the turtle.
# turtle should make random movements and progress the same distance each time
# en.wikipedia.org/wiki/Random_walk


# list of functions, possible turns. random.choice() will select one
direction = [tim.left, tim.right]
# list of functions must be without arguments
# function name stores the reference to the function while
# parenthesis with arguments make the function call
# argument will be added later: random.choice(direction)(90)

# increase the thicknes of pen (default is 1) and speed (default is 3)
tim.pensize(5)
tim.speed(6)
# loop and randomize color and movement of the turtle
for _ in range(100):
    r, g, b = randint(1, 255),randint(1, 255),randint(1, 255)
    tim.pencolor(r, g, b)
    tim.forward(50)
    choice(direction)(90)

tim.reset()


# <! --- exercise 5
# make a spirograph
# how to draw a circle? set radius? how to repeat it? change tilt?
# how to draw just enough circles to complete the picture and not draw
# over previous circles?
tim.pensize(1)
tim.speed(11)
# full circle is 360 degrees, if tim.left(10) i will create 10 size gap
# between circles. to draw just enough circles without overlaping i must
# divide 360 by 10 an that is 36 circles.
for _ in range(36):
    r, g, b = randint(1, 255), randint(1, 255), randint(1, 255)
    tim.pencolor(r, g, b)
    tim.circle(100)
    tim.left(10)

tim.reset()


"""
# <! --- AUTHOR'S Solution
# exercise 4
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
# east, north, west, south
directions = [0, 90, 180, 270]
tim.pensize(15)
tim.speed("fastest")
for _ in range(100):
    tim.color(choice(colours))
    tim.forward(30)
    tim.setheading(choice(directions))

# exercise 5
def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    color = (r, g, b)
    return color

def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)

draw_spirograph(5)
# <! --- end
tim.reset()
"""


# screen object will loop so it doesnt close until mouse click
screen.exitonclick()


#modules: turtle
#tags: turtle drawing,
