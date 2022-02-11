from turtle import Turtle, Screen


# define screen
screen = Screen()
screen.setup(width=500, height=400)
# let the user bet on winning turtle
user_bet = screen.textinput(
    title='Make your bet',
    prompt='Which turtle will win the race? Enter a color: ')

# define 6 different turtles and position them one above the other
colors = ['red', 'orange', 'yellow', 'green', 'purple', 'blue']

xpos = -230
ypos = -130
for turtle_index in colors:
    turtle_name = 't' + turtle_index[:2]  # expected names: tre,tor,tye,tgr,tpu
    turtle_name = Turtle(shape='turtle')
    turtle_name.color(turtle_index)
    turtle_name.penup()
    turtle_name.goto(xpos, ypos)
    ypos += 50


screen.exitonclick()

#modules: turtle
#tags: turtle race, coordinates,
