from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        """ initialize the moving ball at center of screen """
        super().__init__()
        self.penup()
        self.shape('circle')
        self.color('white')
        self.goto(0, 0)
        self.x_distance = 10
        self.y_distance = 10
        self.speed_factor = 0.1  # will pass over to time.sleep(speed_factor)

    def move(self):
        """
        move the ball XY ammount of pixels
        call in loop to make continuous movement
        """
        xpos = self.xcor() + self.x_distance
        ypos = self.ycor() + self.y_distance
        self.goto(xpos, ypos)

    def bounce_y(self):
        """ ball moves in opposite Y direction """
        self.y_distance *= -1

    def bounce_x(self):
        """ ball moves in opposiste X direction """
        self.x_distance *= -1

    def reset_game(self):
        """ reset after paddle miss the ball """
        self.speed_factor = 0.1
        self.goto(0, 0)
        self.bounce_x()

    def increase_speed_factor(self):
        """ increase ball movement speed by 10% """
        self.speed_factor *= 0.9


