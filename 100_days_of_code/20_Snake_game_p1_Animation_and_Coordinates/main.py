from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('My Snake Game')

# turtle list
tlist = []

xpos = 0
ypos = 0
for t in range(3):
    t = Turtle(shape='square')
    t.color('white')
    t.goto(xpos, ypos)
    xpos -= 20






screen.exitonclick()

#modules: turtle
#tags: snake game, coordinates,
