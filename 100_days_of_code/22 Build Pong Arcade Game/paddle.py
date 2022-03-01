from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, coordinates):
        """
        :param1: tuple(x, y) coordinates
        """
        super().__init__()
        self.shape('square')
        self.shapesize(stretch_wid=5, stretch_len=1)  # width = default * 5
        self.penup()
        self.color('white')
        self.goto(coordinates)

    def move_up(self):
        """ move the paddle 20px up """
        ycor = self.ycor() + 20
        self.sety(ycor)

    def move_down(self):
        """ move the paddle 20px down """
        ycor = self.ycor() - 20
        self.sety(ycor)
