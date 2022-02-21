from turtle import Turtle
import random

class Food(Turtle):
    ''' turtle instance to represent the food '''

    def __init__(self):
        ''' initialise the food object '''
        # call the initializer of Turtle class
        # i can create subclass Food(Turtle) without super().__init__()
        # depends if i want __init__() of superclass or not
        # if sub class __init__() and super().__init__()
        # have same attributes they will be replaced
        super().__init__()
        # additional attributes of subclass
        self.penup()
        self.shape('circle')
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color('blue')
        self.speed('fastest')
        self.randomise_position()

    def randomise_position(self):
        ''' randomize position of food '''
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)






#tags: super(), __init__(), inheritance
