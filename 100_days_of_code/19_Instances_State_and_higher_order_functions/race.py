from turtle import Turtle, Screen
from random import randint, choice

# define screen
screen = Screen()
screen.setup(width=500, height=400)  # (x-250 to x250), (y-200 to y200)

# let the user bet on winning turtle
user_bet = screen.textinput(
            title='Make your bet',
            prompt='Which turtle will win the race? Enter a color: ')

# define 6 different turtles and position them one above the other
colors = ['red', 'orange', 'yellow', 'green', 'purple', 'blue']
tlist = []  # append turtle objects to tlist
xpos = -230  # starting coordinates
ypos = -130

for color in colors:
    turtle = Turtle(shape='turtle')
    turtle.color(color)
    turtle.penup()
    turtle.goto(xpos, ypos)
    tlist.append(turtle)
    ypos += 50

race_on = False
if user_bet:  # if user_bet variable exist, user placed the bet
    race_on = True
# if user_bet exist than race_on is True and loop starts
while race_on:
    for turtle in tlist:
        turtle.forward(randint(1, 30))
        if turtle.xcor() > 220:
            winner = turtle
            race_on = False



screen.exitonclick()

#modules: turtle
#tags: turtle race, coordinates,
