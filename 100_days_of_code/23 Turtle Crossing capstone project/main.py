import time
from turtle import Screen

from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)  # require manual screen.update(), read documentation
player = Player()
carmanager = CarManager()
scoreboard = Scoreboard()

# listen for screen events
screen.listen()
# call player.move() on key press
screen.onkeypress(player.move, 'Up')

game_on = True
counter = 0
while game_on:
    counter += 1
    time.sleep(0.1)
    screen.update()

    # move generated cars
    carmanager.move_cars()
    # generate the car when count equals 6
    if counter == 6:
        carmanager.spawn_car()
        # reset the counter
        counter = 0

    # game over if car hits the player
# <! --- is this looping through huge list efficient?
    for car in carmanager.generated_cars:
        if player.distance(car) < 25:
            scoreboard.gameover()
            screen.update()
            game_on = False

    # turtle reach the finish line
    # level up
    if player.completed_level():
        carmanager.increase_speed()
        scoreboard.increase_score()
        player.goto_start()
        screen.update()


screen.exitonclick()

#modules: turtle, time, random
#tags: turtle crossing game, oop
