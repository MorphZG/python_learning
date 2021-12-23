
Building a simpler Higher/Lower game. Check it out at: higherlowergame.com
The goal is to keep playing as long as you can and hit the higher score.

I will build the program by myself, from planning and coding to testing,
debugging and final solution. Here is how i will do it: 

- Breakdown the problem in to smaller parts and solve them one by one
- Make a todo list and start with simple problems
- Run the code often, fix mistakes before moving on to next problem
- Use comments and make the code easy to read
- Refactor and optimize at the end
- Check the authors solution only when i am done and compare

Go to https://replit.com/@appbrewery and look for higher-lower-final and try
the final version of the game so i can understand exactly what is happening
and how it works. After that i can fork the starting project with data for
the game, higher-lower-start. Starting project contains no code, only data so
i can construct the comparison lines.

    <! --- Breakdown:

- print ascii art from art.py

- first try to print and format all data from game_data.py
    - ['name'], ['description'] from ['country']
    - ['follower_count']
    
- question should look like this:
    Compare A: Gigi Hadid, a Model, from United States.
    Against B: Cardi B, a Musician, from United States.
    Who has the more followers? A / B

- define function to pull random person from game_data.py

- define function to compare the followers count and check for correct answer

- pick random person from data list and compare it to another random
person from that list. To avoid duplicates i will pop() items from data list
and append() them to new, empty list.

- no matter who wins, person at position B should stay in game and jump to
position A to compare with new person B

- count score on correct answer

- clear the screen after every round and display ascii art from art.py above each statement

- quit the game on wrong answer