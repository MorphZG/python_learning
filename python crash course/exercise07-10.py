'''
Write a program that polls users about their dream vaccation.
Write a prompt similar to If you could visit one place in the world, where would you go?
Include a block of code that prints the results of the poll.
'''

name_prompt = 'What is your name?\n> '
place_prompt = 'If you could visit one place in the world, where would you go?\n> '

poll_results = {}

active = True  # this is so called flag
               # alternate flag setup can be:
               #    active = False
               #    while not active:

while active:  # while active is True
    name = input(name_prompt)
    place = input(place_prompt)
    poll_results[name] = place  # name is key, place is value
    should_quit = input('should we quit Yes/No')
    if should_quit.lower() == 'yes':
        break
    else:
        continue  # continue statement goes back to start
                  # pass statement does nothing and moves to next line 

print('<!--- Rezultati --->')
for name, place in poll_results.items():
    print(f'\t{name.title()} would like to go to {place.title()}')

#tags: input(), for loop, flag, while loop,