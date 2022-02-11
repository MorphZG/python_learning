from turtle import Turtle, Screen
from random import choice
import colorgram


# <! --- begin color extraction here, delete when done
"""
# extract colors from the image
# we need list of tuples representing RGB colors (turtle works with tuples)
rgb_tuples = []
colors = colorgram.extract('image.jpg', 10)

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    color_tuple = (r, g, b)
    rgb_tuples.append(color_tuple)

print(rgb_tuples)
"""
# <! --- end!

# clean up the values and remove background colors
# remove values close to white (255, 255, 255)
rgb_tuples = [(50, 157, 240), (141, 87, 66), (51, 98, 127),
              (230, 150, 97), (136, 173, 155), (63, 109, 85),
              (125, 162, 188), (160, 82, 45), (255, 69, 0)]


# create a painting with 10 x 10 rows of spots (100 spots total)
# every dot must be size 20
# spacing between is 50

def draw_line(number):
    ''' draw number of dots in a single line '''
    tim.penup()
    for _ in range(number):
        tim.dot(20, (choice(rgb_tuples)))  # tim.dot(size, (rgb tuple))
        tim.forward(50)  # spacing between every dot is 50


tim = Turtle()
screen = Screen()
screen.colormode(255)

screen_width = screen.window_width()
screen_height = screen.window_height()

# go to starting X, Y position. include the dot spacing of 50
# (screen_width / 2) because default position is in the middle of screen
tim.penup()
tim.goto(50 - screen_width/2, 50 - screen_height/2)  # goto(X_width, Y_height)

# starting x position -590
# starting y position -490
xpos = -590
ypos = -490

for _ in range(10):
    draw_line(10)
    ypos += 50
    tim.goto(xpos, ypos)




screen.exitonclick()

#modules: turtle, colorgram
#tags: turtle drawing, tuple, coordinate
