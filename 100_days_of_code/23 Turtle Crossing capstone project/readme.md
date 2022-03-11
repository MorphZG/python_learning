**day 23**
### Turtle Crossing
#### Capstone project

We all remember the games where we had a chicken or some other creature trying  
to cross the road with moving cars. Every decade had its own version of such  
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
-  A turtle moves forwards when you press the "Up" key. It can only move  
   forwards, not back, left or right.
-  Cars are randomly generated along the y-axis and will move from the right  
   edge of the screen to the left edge.
-  When the turtle hits the top edge of the screen, it moves backt to the  
   original position and the player levels up. On the next level, the car speed  
   increases.
-  When the turtle collides with a car, it's game over and everything stops.  
 

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
Screen is 600x600 pixels. So Y axis goes from -300 to +300. Defined starting  
position is at -280 because turtle is 20x20 pixels so finish line should  
be at 280. Currently all want to do now is define what happens when turtle  
touch that line. For now just stop the game. Increasing the speed on level  
up and adding score will come later.

Few times i noticed the strange behaviour when turtle hits the Y of 290 but  
turtle displayed on screen seems far away from that coordinate. It is important  
to add screen.update() at the bottom of that code block so it will refresh with  
latest information. Keep in mind that **you need to manualy update the screen.**   

To keep the code clean i moved the main logic away from main.py and defined  
a simple method player.completed_level() that will return True if y coordinate  
is equal to 280. And also a player.goto_start() that will bring the player  
back to starting position.


#### Create the moving cars
After defining the basic class settings in car_manager.py i had strange problem  
with simple solution. Cars were created inside the main while loop and after  
each iteration previously generated car was deleted from the screen, was not  
sure why because everything is initialized properly, class settings were right.  
After few minutes of thinking i finally realized i need list of cars placed  
outside of main loop or even better, inside the class as a class viariable.  

To move the generated cars all i need is a method that will change the x   
coordinate by a fixed number and than loop through the list of generated cars.  
**What happens if the list becomes to large? Maybe add some kind of cleaner?**  
**If lenght of list is more than x, remove the item at first index position?**  

All i need to do now is reduce the number of generated cars to prevent them  
blocking the entire screen. Simple soultion is to add some kind of counter  
that will spawn the car after it hits the certain number. Let the while loop  
do it's thing and when the count hits a number, spawn the car and reset the  
counter.


#### Level up and game over
After every sucessful cross cars will speed up and increase the difficulty.
Instructor already defined variables for starting move distance and also move  
increment of 10. I will define simple method that adds move increment to move  
distance attribute and call it increase_speed().

If car hits the turtle it is game over. I am not sure is this the best solution.  
I will loop through the list of all generated cars and check if the distance  
between current car and player is less than 25. Will i notice the distance if  
player is hit by a car checked moment before?  

Don't forget to include screen.update().


#### Build the scoarboard
This will be a simple class that inherits from Turtle. Need to find a good  
position in  the upper left corner. Initialize the basics like hideturtle()  
penup() and goto(). When defining increase_score() method, dont forget to  
clear() previous score from the screen.


#### Review and refactoring
increase_speed() is not good. Increasing move_increment will only make the cars  
jump over bigger distance. I should speed up the game by reducing the time.sleep()  
in main loop. Is it possible to have a CarManager class to control that?

When generating new cars instructor took interesting solution, instead of  
counting the loop iterations like me, she calls random.randint(1, 6) inside  
carmanager.create_car() so cars have a random chance of spawning. If "dice"  
roll equals 1 than spawn the car.

#tags: readme,
