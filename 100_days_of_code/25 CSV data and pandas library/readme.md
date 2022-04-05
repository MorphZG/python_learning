**day 25**
## Working with CSV files and Pandas library

### Intro
Will be working with data files and analyzing the data with Pandas library.  
Starting with basic introduction to csv module than comparing it with pandas.  
Pandas is one of most popular libraries for data analysis so it is often first  
choice when working with data :) obviously.  

Before main assignment, instructor talks more about pandas documentation and shows  
her approach when learning the new library. I find it very useful since reading  
the official documentation is not really something you will enjoy right away.  
I also learned that having good documentation is key to good understanding of  
new software.

After few pandas exercises and reading more than i probably had to, searching  
through the whole documentation, it is finaly time to start the project.


### Can you name the US states?
I am building a quiz where you have to name as many states as you can. Map of  
the US will be shown on the background and every time you guess the state it will  
be revealed on map.

1. convert the guess to Title case
2. check if the guess is among the 50 states
3. write correct guesses onto the map
4. use a loop to allow the user to keep guessing
5. record the correct guesses in a list
6. keep track of the score

After asking for user input i can print the 'state' value from the dataframe,  
i can also print the whole row with state name and both x and y coordinates.  
Had hard time finding the solution to pull the single value from 'x' and  
'y' columns that are in the same row as a value from 'state' column. Even the  
mighty google didn't help much. After almost giving up on this i found it.  
Here is the answer!  
```
get the row where dataframe['state'] == user_answer:
    row = dataframe.loc[data['state'] == answer]

get the index value of row:
    inum = dataframe.loc[data['state'] == answer].index[0]

get the values of 'x' column and 'y' column using the index value
    x = dataframe['x'].iloc[inum]
    y = dataframe['y'].iloc[inum]
```

After completing the assignment and watching the instructors solution i was even  
more surprised when i found out how she did it. She probably didn't even read  
through documentation as much as i did since she treated the whole thing like  
a dictionary and didn't even use official methods mentioned in the docs.
```
get the row where data.state == answer:
    state_data = data[data.state == answer_state]

get the x and y values from that row:
    x = state_data.x
    y = state_data.y
```

Could also be writen using keys:
```
# add .item() at the end, it returns clean value, without object info
x = data[data['state'] == answer]['x']
y = data[data['state'] == answer]['x']
```

### Saving data to .csv
Every guessed state is added to guessed_states list. There are 50 states to guess  
so as long as the lenght of the list is less than 50 game will continue. If user  
types "Exit" in to the prompt game will stop and all missing states will be added  
to the missing_states list, than converted to new, single column dataframe and  
than exported to states_to_learn.csv so user can review them later.  

I could also improve the code and add some aditional funcionality but i am more  
than eager to move on to the next project and learn more new things. Would be  
great if i later return to some of these projects and build upon them, expand  
them to something bigger and better.  

### Aditional files
I have created two additional files with short code snipets and description of  
what each line does. Pandas is huge library and there are many different ways to  
access information or present data to the user. Look at exercise.py and test.py 
for more info.


#tags: readme,
