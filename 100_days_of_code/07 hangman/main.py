# https://replit.com/@appbrewery
# Hangman game

import random
from hangman_art import stages, logo
from hangman_words import word_list

print(logo)

# choose a ranodm word from the list
chosen_word = random.choice(word_list)
word_lenght = len(chosen_word)
lives = 6


print(f'the chose word is: {chosen_word}')
# build empty list with "hidden letters"
# for every letter in chosen word, add '_' to display
display = []
for _ in range(word_lenght):
    display.append('_')
# print display list as a signle string
print(' '.join(display))
print(stages[lives])

# flag to stop the while loop
end_of_game = False
while not end_of_game:
    # guess a letter from chosen word
    guess = input('guess a letter: ').lower()
    if guess in display:
        print(f'You already have letter {guess}')
    # vrtim sve indekse odabrane rjeci
    # letter je u svakoj iteraciji novi indeks
    # ako se poklapa sa mojim slovom stavi ga u display
    for position in range(word_lenght):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    print(' '.join(display))
    # lose life if guess is wrong
    # flag, conditions for win/loss
    if guess not in chosen_word:
        lives -= 1
        print(f'The letter {guess} is Wrong!')
        print(stages[lives])
        if lives == 0:
            end_of_game = True
            print('Game over!')
    if '_' not in display:
        end_of_game = True
        print('You won!')

#modules: random
#tags: hangman, game, while loop