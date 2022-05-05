**day 28**

## Tkinter, Dynamic typing and Pomodoro GUI app

### Introduction

Before the lesson, instructor introduce us to history of GUI. Quarrel between  
Microsoft and Apple, apparently Bill Gates stole the idea of GUI based operating  
system. There was also another company Xerox Parc, very few people knows about  
them today but they are responsible for technological breakthroughs we use today.  
First mouse, LAN cables, first object oriented programing language and ofcourse  
the first GUI. Apple somehow considered they are the only right owners for GUI  
operating systems. Luckily such big advancements in technology are imposible to  
control.  

I will probably buy the books, biographies of Steve Jobs and Bill Gates. That  
should be a good reading for sure. 

### Pomodoro technique and my first GUI

Pomodoro is a time management system where you split the work on smaller time  
chunks with short rest in between. You focus on work for 25 or 30 minutes with  
short 5 minute breaks. After 4 or 5 work sessions you take the longer break of  
20 minutes. I will be building the GUI app that will track the time.

In first lesson i setup the window, background image and colors. Instructor have  
defined some constant variables for colors, font type and lenght of work and break  
timers.

My first challange is to create the grid like structure. Add buttons for 'start'  
and 'reset', add label above the main image and a checkmark that will show how  
many work sessions (pomodoros) user completed. Funcionality will be added later,  
now i just have to organize the elements on the screen while using `tkinter.grid()`  
instead of `tkinter.pack()`.

### Countdown mechanism

After placing all elements on screen it is time to add some functionality. Adding  
the countdown mechanism will be my first task. When working with the command line  
interface i could code countdown inside while loop, but with graphical interface  
that would not work. GUI's are usually event driven, interface must wait for user  
to make some action. That is the reason Tkinter have `mainloop()` or Turtle have  
`exitonclick()`. App must stay active all the time, loop and wait for the user  
to click or press a key. App must listen for events. Tkinter have few builtin  
methods for every widget that can wait for event before doing some action.  

`after()` takes the ammount of time it should wait and than calls the funcion  
together with the arguments you pass in. It is used in `count_down()` where it  
waits 1000ms or 1sec before calling `count_down()` again. Here i have few linked  
mechanisms. When the button is clicked, it checks the command parameter where   
`command=start_timer`. `start_timer()` will call `count_down(count)` while also  
modify 'count' parameter which can be set as work time, short break or long break.  

### Timer control

Timer must work in three modes. I defined global variable that counts repetitions.  
Every 1/3/5/7 rep is 25min work time, repetitions 2/4/6 are 5min short break and  
every 8th repetition is a 20min long break. When timer starts it will also change  
label text and color to display current mode. 


#tags: readme,
