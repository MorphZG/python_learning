**day 22**  
### Pong, arcade game  

This one should be fun. Instructor starts by letting me think. I will start by  
writing the project blueprint. What components i need, how would i structure  
different elements and define game logic? As always, break down the problem in  
smaller parts and start solving them piece by piece.  

My initial thought, the very first idea that i got was to create classes for  
the stick (instructor says its a paddle so i will stick to the convention),  
the ball, scoreboard and terrain. Not sure will i need terrain class but the  
final solution will crystalize along the way. So 4 modules, paddle, ball,  
scoreboard and terrain imported in to main.py. Could possibly take some code  
snippets from "Snake game" i did in previous section. I will compare my notes  
with instructor. See how they differ from the final project and reflect on them.  


My breakdown (compare with instructor later):
```
- define the environment
    - screen and window
    - add separator, white line on Y axis (cosmetic, can come later)
- create the paddle (player controled) for each player
    - one stick on each side (West and East)
    - must move on Y axis, vertical movement
- create the ball
    - moves constantly
    - must bounce of side walls and sticks
    - spawn at center, winer of last round serves (move ball toward him)
- define scoreboard class
    - set the rules for scoring (maybe store results in .json)
    - set the winning score
```


Instructors breakdown:
```
- create the screen
- create and move the paddle
- create another paddle
- create the ball and make it move
- detect collision with wall and bounce
- detect collision with paddle
- detect when paddle misses
- keep score
```

#### Create the screen
My first assignment is to screate the screen. Size will be set to (800, 600),  
and colored black. Should stay on screen, even if user clicks on it so instead  
exitonclick() i should find another solution.  

#### Create and move a paddle
I must find a solution for creating the paddles on both sides of the screen,  
West and East. Paddle class will inherit from Turtle. Paddles will initialize  
with the following attributes:  
`width=20, height=100, X_position=350(east), Y_position=0`  
  
I need a method that will detect key press and move the paddle up or down  
by 20 pixels. Player 1 will use the 'W' and 'S' keys while player 2 will use  
'Up' and 'Down' arrow keys.   

Official documentation recommends setting tracer() to zero to improve complex  
animations. If tracer() is set to zero i have to manualy update the changes  
on screen with update(). Will try to play with different tracer() options  

#### Create the ball and make it move
Ball will be created as separate class.  
`width=20, height=20, X_position=0, Y_position=0`  

Here comes the tricky part. When screen refreshes the ball should start moving  
toward the upper right corner of the screen. It should change the X and Y  
coordinates on every refresh.

I thought i was doing something wrong while doing this one. After creating the  
ball class i found very simple solution for ball movement but somehow ball  
dissapeard from the screen. Was not sure why. Maybe screen.update() or tracer()  
is causing me problems? Maybe method definition is wrong? Whatever i tried  
was wrong. Ball just dissapears from the screen. Crazy! Lets try to fix the  
coordinates, set the static position. Set (x, y) to (350, 350)... same thing  
again. There is no ball on screen. After i set the (x, y) to (200, 200) ball  
was visible again.  

Good! Now make it move again. And again, ball dissapears. This is madness.  
I cant afford to loose the whole day solving this. I will watch just few  
seconds of video to help me with solution. Than i realized.... My code was  
fine but the moving ball and manual screen update was to fast for me to see  
it on screen. In ball.py i had to drop the number of traveling distance from  
20 to 5 and in main.py add time.sleep(0.1) after every screen update.  

#### Detect collision with wall and bounce
Detect collision with top and bottom walls. How to make the ball bounce?  
If we think how ball actually travels from A to B, how X and Y coordinates  
change. What happens to coordinates when the ball bounce? Think how X and Y  
changes while ball is traveling? Instructor shares a small hint to consider  
creating two new attributes in the Ball class to track it's movement.  
But if Ball inherits from Turtle class than it already have turtle.position()  
and turtle.xcor() and turtle.ycor(). These methods returns the coordinates.  

What i need is another method that will change the vertical movement on the  
Y axis in the opposite direction while horizontal X stays the same.  
There is a few different solutions. How to flip the Y movement in opposite  
direction? I will define two attributes under initializer, x_distance and  
y_distance. Than use the ball.bounce() to flip the y_distance.  

#### Detect collision with the paddle
This is probably the hardest part of the program so instructor explains the  
logic behind it. When measuring distance between two objects or object and a   
single coordinate we can use the turtle.distance() built-in method.  
The problem with this is the size of the paddle. ball.distance(paddle) would  
return the distance between the center of the ball and paddle. If ball hits  
the edge of the padle it would not register as a collision.  

Instructor proposes solution. If the ball is past the certain point on the  
x axis, if it is gone far enough to the right or left and its at least 50px  
from the center of the paddle than we have a contact.

#### Detect when paddle misses
Add mechanic of miss. Check if the ball goes out of bounds at the edge of the  
screen. If yes, reset the ball's position to the center of the screen. The ball  
should then start moving towards the other player.  

**WORK IN PROGRESS**




#tags: readme,
