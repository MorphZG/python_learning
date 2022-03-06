import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10  # increase move distance after each level


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.spawn_car()
        self.move_distance = STARTING_MOVE_DISTANCE

    def spawn_car(self):
        """ spawn the car on random Y position """
        self.penup()
        self.shape('square')
        self.shapesize(stretch_len=2)
        self.color(random.choice(COLORS))
        ypos = random.randint(-250, 250)
        self.goto(300, ypos)

    def move_cars(self):
        """ moves the car from right to left screen corner """
        ypos = self.ycor()
        xpos = self.xcor() - self.move_distance
        self.goto(xpos, ypos)

