import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10  # increase move distance after each level


class CarManager:

    generated_cars = []

    def __init__(self):
        self.move_distance = STARTING_MOVE_DISTANCE

    def spawn_car(self):
        """ spawn the car on random Y position """
        car = Turtle()
        car.penup()
        car.shape('square')
        car.shapesize(stretch_len=2)
        car.color(random.choice(COLORS))

        ypos = random.randint(-250, 250)
        car.goto(300, ypos)

        CarManager.generated_cars.append(car)  # what if list is to large?

    def move_cars(self):
        """
        moves the car from right to left screen corner
        size of the move depends on self.move_distance
        """
        for car in CarManager.generated_cars:  # what if list is to large?
            ypos = car.ycor()
            xpos = car.xcor() - self.move_distance
            car.goto(xpos, ypos)

    def increase_speed(self):
        """ increase the movement speed """
        self.move_distance += MOVE_INCREMENT
