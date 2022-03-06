import time
from turtle import Screen

from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)  # require manual screen.update(), read documentation
player = Player()

# listen for screen events
screen.listen()
# call player.move() on key press
screen.onkeypress(player.move, 'Up')

game_on = True
generated_cars = []
counter = 0
while game_on:
    counter += 1
    time.sleep(0.1)
    screen.update()

    # generate the car when count == 6
    if counter == 6:
        car_object = CarManager()
        generated_cars.append(car_object)
        print(len(generated_cars))
        counter = 0

    # move generated cars
    for car in generated_cars:
        car.move_cars()

    # turtle reach the finish line
    if player.ycor() >= 280:
        print("Game over!")
        print(f'current position is {player.position()}')
        game_on = False
        screen.update()

screen.exitonclick()

#modules: turtle, time, random
#tags: turtle crossing game, oop
