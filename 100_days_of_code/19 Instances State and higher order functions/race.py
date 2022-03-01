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
    turtle_object = Turtle(shape='turtle')
    turtle_object.color(color)
    turtle_object.penup()
    turtle_object.goto(xpos, ypos)
    tlist.append(turtle_object)
    ypos += 50  # position turtles on starting line

race_on = False
if user_bet:  # if user_bet variable exist, user placed the bet
    race_on = True
# if user_bet exist than race_on is True and loop starts
while race_on:
    for turtle_object in tlist:
        turtle_object.forward(randint(1, 30))
        if turtle_object.xcor() > 220:  # finish line on x coordinate
            winner = turtle_object.pencolor()  # pencolor returns turtle color
            race_on = False
            if winner == user_bet:
                print(f'You won! {winner.title()} have won the race!')
            else:
                print(f'You lost! {winner.title()} have won the race!')


screen.exitonclick()

#modules: turtle
#tags: turtle race, coordinates,
