from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('turtle')
        self.setheading(90)
        self.goto(STARTING_POSITION)

    def move(self):
        """ add MOVE_DISTANCE to current y coordinate """
        ycor = self.ycor() + MOVE_DISTANCE
        self.sety(ycor)

    def completed_level(self):
        """ return True if player reach the finish line """
        return self.ycor() >= FINISH_LINE_Y

    def goto_start(self):
        self.goto(STARTING_POSITION)
