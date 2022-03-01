#solution at video 119
#https://replit.com/@appbrewery/guess-the-number-final?v=1

import random
from art import logo

print(logo)

game_on = True  # flag

# choose the random integer between 1 and 100
secret = random.randint(1, 100)

# Force the user to enter valid difficulty
# Infinite loop, break out only if difficulty input as "easy" or "hard"
while True:
    
    difficulty = input('Choose difficulty. Type "easy" or "hard": ').lower()
    if difficulty == 'easy':
        attempts = 10
        break
    elif difficulty == 'hard':
        attempts = 5
        break
    else:
        print('\n\tPlease choose the valid difficulty!\n')


print('''
Welcome to the number Guessing Game!
Im thinking of a number between 1 and 100''')


# main loop, check the answers, and count wrong attempts
# try/except/else block prints the warning if you input str instead of int
while game_on:

    guess = int(input('\nMake a guess '))

    if guess < secret:
        attempts -= 1
        print('\tTo low!')
        print('\tGuess again.')
        print(f'\tYou have {attempts} attempts remaining')

    elif guess > secret:
        attempts -= 1
        print('\tTo high!')
        print('\tGuess again.')
        print(f'\tYou have {attempts} attempts remaining')

    elif guess == secret:
        print('\nMagnificent!! You got it!')
        print('\n\tIts a WIN!\n\n')
        game_on = False

    if attempts == 0:
        print("You've run out of guesses, you lose.")
        game_on = False


#modules: random
#tags: while loop, numbers, randint(), guess game,