**day 20 and 21**

## Building a Snake game!  
This one makes me happy. Brings back the memories on my firs Nokia 3310.
Snake project will be split in 2 parts and across 2 "days", or should i better
say 2 folders.

### first part  
In first part instructor presents the project and breakdown the goals on smaller
parts.
```
- create snake body
- move and control the snake.
```
What surprised me is the use of turtle library. I will build the snake by
creating the square turtles. Starting snake will be made out of 3 square
turtles. That is my first challange, simple. Think about how to line them up
one behind the other in the center of the screen. Each turtle should be a white
square with default size of 20x20.

Huge knowledge bomb on how different pieces are shown on the screen. If i try
to move each snake segment as i normaly would, i get strange animation where
each segment moves with a delay or head spins in circle while body continue
forward. I had to rethink on how to move different parts on the screen since
they are not linked together. Thanks to instructor i was able to solve the
problem. Instead of moving the first segment than the second segment and so on,
solution is to move them in opposite sequence. Last segment moves first and
fills the position of previous segment. That way there is no delays and snake
looks like a single item.

After defining the basic setup and movement of first 3 snake pieces i am
creating a Snake() class to make the code simpler and modable. At the end, i
will have 3 separate classes. Snake(), Food() and Scoreboard() with every
class in its own separate file.

### second part  
```
- detect collison with food
- create a scoreboard,
- detect collision with walls
- detect collision with tail
```
Defining the Food class that will first inherit from the Turtle class, then
add additional attributes like color, size and random coordinates. We need
Turtle as parent (super) class because of its methods listed in official
documentation. Adding small scoreboard at the top. Surprise! Surprise!
Scoreboard will also be another turtle. Defined in scoreboard.py i will use
turtle.write() method to paste the text object screen.

**note**   
Its interesting how snake.py module is designed. Movement of snake. Snake is
built out of separate turtle segments and they all move together as a one
compact object following the snakes head. Snake have 3 parts, loop goes from
last to first, takes the current position of middle part and than tells the 
last part to goto that position. While game_on, for loop moves snake_segments
with goto(xpos, ypos)



#tags: readme
