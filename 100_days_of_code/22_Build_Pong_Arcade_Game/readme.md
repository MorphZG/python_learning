**day 22**  
### Pong, arcade game  

This one should be fun. Instructor starts by letting me think. I will start by  
writing the project blueprint. What components i need, how would i structure  
different elements and define game logic? As always, break down the problem in  
smaller parts and start solving them piece by piece.  

My initial thought, the very first idea that i got was to create classes for  
the stick (instructor says its a paddle so i will stick to the convention),  
the ball, scoreboard and terrain. Not sure will i need terrain class but the  
final solution will crystalize along the way. So 4 modules, stick, ball,  
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

#### create the screen
My first assignment is to screate the screen. Size will be set to (800, 600),  
and colored black. Should stay on screen, even if user clicks on it so instead  
exitonclick() i should find another solution.  

#### create and move a paddle
I must find a solution for creating the paddles on both sides of the screen,  
West and East. Paddle class will inherit from Turtle. Paddles will initialize  
with the following parameters:  
`width=20; height=100; X_position=350(east); Y_position=0` 
I need a method that will detect key press and move the paddle up or down  
by 20 pixels. Player 1 will use the 'W' and 'S' keys while player 2 will use  
'Up' and 'Down' arrow keys.   

Official documentation recommends setting tracer() to zero to improve complex  
animations. But if tracer() is set to zero i have to manualy update the changes  
on screen with update(). Will try to play with different tracer() options  

#tags: readme,
