'''
Movie theater charges different ticket prices depending on a persons age
If a person is under the age of 3 the ticket is free,
If they are between 3 and 12 the ticket is $10
If the are over age 12 the ticket is $15.
Write a loop in which you ask users their age and then tell them the cost
'''

prompt = 'How old are you'

while True:
    age = input(prompt)
    if age == 'quit':
        break
    
    age = int(age)
    if age < 3:
        print('Your ticket is free')
    elif age <= 12:
        print('Your ticket cost $10')
    else:
        print('Your ticket cost $15')

#tags: input(), while loop, if, elif, else,