from turtle import Turtle

# constant variables
# if i want to change those parameters later i dont have to dig through the
# code to find them. They are visible on top. Read more on constants
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20


class Snake:
    """ creates a compact snake out of square turtles """

    def __init__(self):
        """ initialize the snake """

        self.snake_segments = []
        self.create_snake()

    def create_snake(self):
        """ creates the snake segment by segment, auto call on __init__"""

        for position in STARTING_POSITIONS:
            square = Turtle(shape='square')
            square.penup()  #               <! --- penup()
            square.color('white')
            square.goto(position)
            self.snake_segments.append(square)

    def move(self):
        """ moves the snake forward """
        for i in range(len(self.snake_segments)-1, 0, -1):  # loop from last to first index, reverse
            xpos = self.snake_segments[i - 1].xcor()  # position of middle square
            ypos = self.snake_segments[i - 1].ycor()  # position of middle square
            self.snake_segments[i].goto(xpos, ypos)  # move last square to middle square

        self.snake_segments[0].forward(MOVE_DISTANCE)



