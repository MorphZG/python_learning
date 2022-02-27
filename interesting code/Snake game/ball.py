from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        """ initialize the moving ball at center of screen """
        super().__init__()
        self.penup()
        self.shape('circle')
        self.color('white')
        self.goto(0, 0)
        self.x_distance = 5
        self.y_distance = 5

    def move(self):
        """ make the ball alive and make it roll """
        xpos = self.xcor() + self.x_distance
        ypos = self.ycor() + self.y_distance
        self.goto(xpos, ypos)

    def bounce_y(self):
        """ ball moves in opposite Y direction """
        self.y_distance *= -1

    def bounce_x(self):
        """ ball moves in opposiste X direction """
        self.x_distance *= -1



