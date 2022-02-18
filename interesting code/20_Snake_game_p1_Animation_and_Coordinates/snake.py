from turtle import Turtle

# constant variables
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90  # heading toward North
DOWN = 270  # heading toward South
LEFT = 180  # heading toward West
RIGHT = 0  # heading toward East


class Snake:
    """ creates a compact snake out of square turtles """

    def __init__(self):
        """ initialize the snake """

        self.snake_segments = []
        self.create_snake()
        # in snake.move() every segment of snake goto() the part before it
        # snake_segment[0] is setting the position for the rest of body
        # will call it "head" to make it readable
        self.head = self.snake_segments[0]

    def create_snake(self):
        """ creates the snake segment by segment, auto call on __init__"""

        for position in STARTING_POSITIONS:
            square = Turtle(shape='square')
            square.penup()  #               <! --- penup()
            square.color('white')
            square.goto(position)
            self.snake_segments.append(square)

    def move(self):
        """
        let the snake continously move forward
        body follows the head by taking position of segment in front
        """
        for i in range(len(self.snake_segments)-1, 0, -1):  # loop from last to first index, reverse
            xpos = self.snake_segments[i - 1].xcor()  # position of middle square
            ypos = self.snake_segments[i - 1].ycor()  # position of middle square
            self.snake_segments[i].goto(xpos, ypos)  # move last square to middle square

        self.head.forward(MOVE_DISTANCE)

    def up(self):
        """ set the snake heading North """
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        """ set the snake heading South """
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        """ set the snake heading West """
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        """ set the snake heading East """
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

