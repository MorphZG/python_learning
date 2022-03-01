from turtle import Turtle

# constant variables
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90  # heading toward North
DOWN = 270  # heading toward South
LEFT = 180  # heading toward West
RIGHT = 0  # heading toward East


class Snake:
    ''' creates a compact snake out of square turtles '''

    def __init__(self):
        ''' initialize the snake '''
        self.snake_segments = []
        self.create_snake()
        # in snake.move() every segment of snake goto() the part before it
        # snake_segment[0] is setting the position for the rest of body
        # will call it "head" to make it readable
        self.head = self.snake_segments[0]
        # to extend the snake, add to last snake_segment
        # will call it "tail" to make it readable
        self.tail = self.snake_segments[-1]

    def create_snake(self):
        '''
        add snake segment at each position in STARTING_POSITIONS
        auto call on __init__
        '''
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        ''' add a white square segment to snake '''
        square = Turtle(shape='square')
        square.color('white')
        square.penup()
        square.goto(position)
        self.snake_segments.append(square)

    def extend_snake(self):
        '''
        call add_segment(position) where position is
        position() of self.tail or last item in snake_segments
        '''
        self.add_segment(self.tail.position())

    def move(self):
        '''
        let the snake continously move forward
        body follows the head by taking position of segment in front
        '''
        for i in range(len(self.snake_segments)-1, 0, -1):  # loop from last to first index, reverse
            xpos = self.snake_segments[i - 1].xcor()  # position of middle square
            ypos = self.snake_segments[i - 1].ycor()  # position of middle square
            self.snake_segments[i].goto(xpos, ypos)  # move last square to middle square

        self.head.forward(MOVE_DISTANCE)


# define the movement methods
    def up(self):
        ''' set the snake heading North '''
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        ''' set the snake heading South '''
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        ''' set the snake heading West '''
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        ''' set the snake heading East '''
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

