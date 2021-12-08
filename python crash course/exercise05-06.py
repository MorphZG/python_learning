# Write an if-elif-else chain that determines persons stage of life
# Set a value for the variable age
# If the person is less than 2 years old print a msg 'Person is a baby'
# If the person is at least 2 years old but less than 4, print 'Person is a toddler'
# If at least 4 years old but less than 13, print 'Person is a kid'
# If at least 13 but less than 20, print 'Person is a teenager'
# If at least 20 but less than 65. print 'Person is an adult'
# If the persons age is 65 or older print 'Person is an elder'

import random

age = random.randrange(80)
print(f'The persons age is: {age}')

if age < 2:
    print('Person is a baby')
elif age < 4:
    print('Person is a toddler')
elif age < 13:
    print('Person is a kid')
elif age < 20:
    print('Person is a teenager')
elif age < 65:
    print('Person is adult')
else:
    print('Person is elder')


#tags: randrange(), if, elif, else,
#modules: random