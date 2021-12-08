# Chapter 9, Classes
# Solutions:
# https://ehmatthes.github.io/pcc_2e/solutions/solutions/

'''Dice
Make a class Die with one attribute called sides, which has a default value
of 6. Write a method called roll_die() that prints a random number between
1 and the number of sides the die has. Make a 6-sided die and roll it 10 times.

Make a 10 sided die and a 20 sided die. Roll each die 10 times.
'''

from random import randint

class Die():
    ''' represent a die '''

    def __init__(self, sides=6):
        ''' initialize a simple die '''
        self.sides = sides  # default sides 6

    def roll_die(self):
        ''' return random number, depending on number of die sides '''
        roll = randint(1, self.sides)
        return roll


# create a die instance with default number of sides
die_d6 = Die()
print('I created an instance from your Die class')
print('With default number of sides, we have:')
print(die_d6.sides, 'sides')

# roll it 10 times
print()
print('I will roll the dice 10 times and print the results: ')

rezultati = []
for roll in range(10):
    result = die_d6.roll_die()
    rezultati.append(result)

print(rezultati)


# create dice instances with 10 and 20 sides
die_d10 = Die(10)
die_d20 = Die(20)

print('I created two different instances from your Die class')
print('We have:')
print(f'\tdie_d10 with {die_d10.sides} sides')
print(f'\tdie_d20 with {die_d20.sides} sides')

# roll them 10 times
print()
print('I will roll d10 and d20 10 times and print the results: ')

rezultati_d10 = []
rezultati_d20 = []

for roll in range(10):
    
    result_1 = die_d10.roll_die()
    rezultati_d10.append(result_1)

    result_2 = die_d20.roll_die()
    rezultati_d20.append(result_2)

print(rezultati_d10)
print(rezultati_d20)

#modules: random
#tags: class, randint()