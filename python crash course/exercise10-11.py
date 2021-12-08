# Chapter 10, Files and exceptions
# Solutions:
# https://ehmatthes.github.io/pcc_2e/solutions/solutions/

'''Favorite number
Write a program that prompts for the user's favorite number.
Use json.dump() to store this number in a file. Write a separate program that
reads in this value and prints the message, "I know your favorite number is..."
'''

import json

filename = 'dump_files/favorite_number.json'

# write favorite number to .json file
favorite_number = input('What is your favorite number? ')

with open(filename, 'w') as f:
    json.dump(favorite_number, f)


# read favorite number from .json file
with open(filename) as f:
    json.load(f)
    print(f'Your favorite number is {favorite_number}!')



#modules: json
#tags: dump(), i/o stream, files, function