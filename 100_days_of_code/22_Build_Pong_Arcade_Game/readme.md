**day 22**  
### Pong, arcade game  

This one should be fun. Instructor starts by letting me think. I will start by  
writing the project blueprint. What components i need, how would i structure  
different elements and define game logic? As always, break down the problem in  
smaller parts and start solving them piece by piece.  

My initial thought, the very first idea that i got was to create classes for  
the stick (could not find the better word, hopefuly you know what it is),  
the ball, scoreboard and terrain. Not sure will i need terrain class but the  
final solution will crystalize along the way. So 4 modules, stick (instructor  
say its a paddle), ball, scoreboard and terrain imported in to main.py.  
Could possibly take some code snippets from "Snake game" i did in previous  
section. I will compare my notes with instructor. See how they differ from   
the final project and reflect on them.  


My breakdown (compare with instructor later):
```
- define the environment
    - screen and window
    - add separator, white line on Y axis
- create sticks (player controled) for each player
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
Instructors says its a paddle so lets stick to the naming convention and call  
it paddle instead of stick.  


#tags: readme,
