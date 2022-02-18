from turtle import Screen, Turtle
import time

from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('My Snake Game')
screen.tracer(0)  # improve the animation, look at doc. for more info

snake = Snake()

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
    snake.move()  # continuously move the snake forward.

screen.exitonclick()


#modules: turtle, time
#tags: snake game, coordinates, reverse loop,
