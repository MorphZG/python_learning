**day 23**
### Turtle Crossing
#### Capstone project

We all remember the games where we had a chicken or some other creature trying  
to cross the road with moving cars. Every decade had its own versions of such  
games. Player will control the turtle which can only go forward, trying to  
cross the road with many randomly generated cars. When you manage to cross the  
road, you will get the point, cars will speed up and you will respawn and try  
again.

This project will be my second capstone project (first was blackjack). Project  
will test my knowledge on many of OOP concepts i have learned so far.  

Instructor shared the 7 steps necessary to complete the project:  
1. Check out how the gameplay works
2. Break down the problem
3. Create the player behaviour
4. Create the car behaviour
5. Detect when the turtle collides with a car
6. Detect when the player has reached the other side
7. Add the scoreboard and game over sequence

There is also defined difficulty levels.  
- **Normal** difficulty: Use all video steps to complete the project
- **Hard** difficulty: Use only steps 1 and 2
- **Expert** difficulty: Only use step 1 to complete the project

As with any other project i will try to complete it with maximum effort and  
start with **expert** difficulty and see how it goes. I am confident that  
with enough time i can complete it. Instructor shared the starting project  
files with basic setup. Screen resolution of 600x600, tracer(0) and manual  
update() of screen every 0.1 seconds using time module in main.py. There is  
also player.py, scoreboard.py and car_manager.py. These files also have some  
basic constants defined. Car colors and moving distance for both player and  
cars.

#### Check out how the gameplay works
1. A turtle moves forwards when you press the "Up" key. It can only move  
   forwards, not back, left or right.
2. Cars are randomly generated along the y-axis and will move from the right  
   edge of the screen to the left edge.
3. When the turtle hits the top edge of the screen, it moves backt to the  
   original position and the player levels up. On the next level, the car speed  
   increases.
4. When the turtle collides with a car, it's game over and everything stops.  

#### Break down the problem
Instructor have provided her thought process on this one but since i am trying  
to complete this by myself with **expert** difficulty in mind i will not look  
at the rest of her seven steps. This is how i will continue forward.

- Create the turtle and make it move from starting position to finish line
- Detect when turtle reaches the finish line
- Create the cars at random vertical positions and make them move
- Increase the speed of moving cars on level up
- Detect when car hits the turtle and reset the game
- Make the scoreboard that will track the score

#### Create the turtle and make it move
In player.py i am defining the Player class that inherits from Turtle. Set the  
shape of turtle, heading toward North and starting position. Define move()  
method that will move the turtle up by adding move_distance to its current Y  
coordinate. In main.py start listening for events and call player.move() when  
"Up" key is pressed.

#### Detect when turtle hits the finish line
Screen is 600x600 pixels. So Y axis goes from -300 to +300. I have defined a  
starting position at -280 because turtle is 20x20 pixels so finish line should  
be between 280 and 300, will try to find the best value. All i have to do is  
define what happens when turtle crosses that line. At first just stop the game.  
Increasing the speed on level up and adding score will come later.

Few times i noticed the strange behaviour when turtle hits the Y of 290 but  
turtle displayed on screen seems far away from that coordinate. It is important  
to add screen.update() at the bottom of that code block so it will refresh with  
latest information. Keep in mind that **you need to manualy update the screen.**   
I should probably revisit two previous projects and check what i did there.  

#### Create the moving cars
After defining the basic class settings in car_manager.py i had strange problem  
with simple solution. Cars were created inside the main while loop and after  
each iteration previously generated car was deleted from the screen, was not  
sure why because everything is initialized properly, class settings were right.  
After few minutes of thinking i finally realized i need list of cars placed  
outside of main loop.  

To move the generated cars all i need is a method that will change the X   
coordinate by a fixed number and than loop through the list of generated cars  
and call the move_car() mehtod on every car. Since whole game is inside while  
loop it will continuously call the move_car() method with every iteration.

All i need to do now is reduce the number of generated cars to prevent them  
blocking the entire screen. Simplest soultion is to add some kind of counter  
that will spawn the car after it hits the certain number. Let the while loop  
do it's thing and when the count hits a number, spawn the car and reset the  
counter.


#tags: readme,
