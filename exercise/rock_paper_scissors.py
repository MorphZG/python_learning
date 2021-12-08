'''
Rock Paper Scissors
https://www.practicepython.org/exercise/2014/03/26/08-rock-paper-scissors.html

Exercise 8
Make a two-player Rock-Paper-Scissors game.
(Hint: Ask for player plays (using input), compare them, print out
a message of congratulations to the winner, and ask if the players
want to start a new game)

Remember the rules:

    Rock beats scissors
    Scissors beats paper
    Paper beats rock
'''


import random  # random list item choice

'''
program radi ali kod moze biti puno efikasniji i kraci
trenutno radim na boljoj verziji u koju je ukljuceno i bodovanje
mozda probati sa enumerate()
'''

# random.choice(actions) --> programm will pick random item from list:
actions = ['rock', 'paper', 'scissors']

flag = 'on'
while flag == 'on':
    player_answer = input('\n\trock, paper or scissors? (type "stop" to quit)\n>')
    ai_answer = random.choice(actions)
    if player_answer == 'rock':
        if ai_answer == 'scissors':
            print(f'\tAI took {ai_answer} player wins!')
        elif ai_answer == 'paper':
            print(f'\tAI took {ai_answer} AI wins!')
        elif ai_answer == 'rock':
            print(f"\tAI took {ai_answer} it's a tie!")
    elif player_answer == 'scissors':
        if ai_answer == 'scissors':
            print(f"\tAI took {ai_answer} it's a tie!")
        elif ai_answer == 'paper':
            print(f'\tAI took {ai_answer} player wins!')
        elif ai_answer == 'rock':
            print(f'\tAI took {ai_answer} AI wins!')
    elif player_answer == 'paper':
        if ai_answer == 'scissors':
            print(f'\tAI took {ai_answer} AI wins!')
        elif ai_answer == 'paper':
            print(f"\tAI took {ai_answer} it's a tie!")
        elif ai_answer == 'rock':
            print(f'\tAI took {ai_answer} player wins!')
    elif player_answer == 'stop':
        flag = 'off'
        
#modules: random
#tags: while loop, dictionary, game