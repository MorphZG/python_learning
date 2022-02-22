from turtle import Screen, Turtle
import time

from snake import Snake
from food import Food
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('My Snake Game')
screen.tracer(0)  # improve the animation, look at doc. for more info

snake = Snake()  # initialize the snake and keep it moving
food = Food()  # initialize the food and display it on screen
scoreboard = Scoreboard()  # initialize the scoreboard and display it on screen

# start listening for keystrokes
# define movement methods in snake class
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_on = True
while game_on:
    screen.update()  # update screen after all segments complete the movement
    time.sleep(0.1)  # 0.1 second pause/delay to make movements smooth.
    snake.move()  # continuously move the snake forward

    # detect collision with food
    if snake.head.distance(food) < 15:
        scoreboard.update_score()
        food.randomise_position()
        snake.extend_snake()

    # detect collision with walls
    if (snake.head.xcor() > 295 or snake.head.xcor() < -295
            or snake.head.ycor() > 295 or snake.head.ycor() < -295):
        game_on = False
        scoreboard.game_over()

    # detect collision with body/tail
    for segment in snake.snake_segments[1:]:
        # slice[1:] will ignore distance between head and it self
        # will prevent game_over() on game start
        if snake.head.distance(segment) < 10:
            game_on = False
            scoreboard.game_over()


screen.exitonclick()


#modules: turtle, time, random
#tags: snake game, coordinates, reverse loop, class inhertance, super()__init__()
