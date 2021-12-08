# Chapter 9, Classes
# Solutions:
# https://ehmatthes.github.io/pcc_2e/solutions/solutions/

'''Lottery
Make a list or tuple containing a series of 10 numbers and five letters.
Randomly select four numbers or letters from the list and print a message
saying that any ticket matching these four numbers or letters wins a prize.
'''

# from string module, import string variables ascii_letters and digits
# from random module, import functions randint, choice and choices
from string import ascii_letters, digits
from random import randint, choice, choices

# create empty list to store possible numbers and letters
choose_from = []

# select 10 random numbers between 1 and 99 and append to list
turn = 0
while turn < 10:
    x = randint(1,99)
    if x not in choose_from:
        choose_from.append(x)
        turn += 1
    else:
        continue

# select 5 random letters and append to list
turn = 0
while turn < 5:
    x = choice(ascii_letters)
    if x not in choose_from:
        choose_from.append(x)
        turn += 1
    else:
        continue


# print list of 10 numbers and 5 letters
print('I will pick 4 items from this list of letters and numbers:')
print(choose_from)

# pick 4 items from that list as lottery winner
# autor ovdje koristi while loop, len(winner) < 4, choice()
# random.choices(sequence, weight=None, population)
# Weight in choices have None as default but can be distributed for every item:
# weight=[4, 2, 1, 1]; first item have 4x chance than last two and 2x than second
winner = choices(choose_from, k=4)
print(f'\nThe winning combination is... \n\t{winner}')




#modules: random, string
#tags: ascii, choice(), choices(), randint(), while loop, lottery