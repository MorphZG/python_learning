# Chapter 10, Files and exceptions
# Solutions:
# https://ehmatthes.github.io/pcc_2e/solutions/solutions/

'''Favorite number Remembered
Combine the two programs from the exercise 10-11 into one file. If the number
is already stored, report the favorite number to the user. If not, prompt for
the user's favorite number and store it in file. Run the program twice to see
that it works.
'''

import json

try:  # load the number if stored
    with open('favorite_number.json') as f:
        number = json.load(f)

except FileNotFoundError:  # dump the number if there is no file
    number = input("What's your favorite number? ")
    with open('favorite_number.json', 'w') as f:
        json.dump(number, f)
    print("Thanks, I'll remember that.")

else:  # report the number if try block succeed
    print(f"I know your favorite number! It's {number}.")


#modules: json 
#tags: dump(), i/o stream, files, function