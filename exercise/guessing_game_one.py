'''
Guessing Game One
Exercise 9
https://www.practicepython.org/exercise/2014/04/02/09-guessing-game-one.html

Generate a random number between 1 and 9 (including 1 and 9).
Ask the user to guess the number, then tell them whether they
guessed too low, too high, or exactly right.
(Hint: remember to use the user input lessons from the very first exercise)

Extras:

Keep the game going until the user types “exit”
Keep track of how many guesses the user has taken,
and when the game ends, print this out.
'''

import random

secret = random.randint(1, 9)
playing = True  # flag za while loop
count = 1       # brojac pokusaja

while playing:
    print('type "stop" to quit the game')
    answer = input('try to guess the secret number: ')
    # svaki input je string, ako input nije 'stop' prebacujem ga u integer:
    if answer != 'stop':
        answer = int(answer)
        if answer < secret:
            count += 1
            print('you are to low')
        elif answer > secret:
            count += 1
            print('you are to high')
        else:
            print('you are correct!', '\nnumber of tries: ', count)
            break
    else:
        break
'''
Concepts for this week:

    Modules
    Random numbers
    User input


Random Numbers (and Modules)

This is your first exposure to using Python code that somebody else wrote.
In Python, these formally-distributed code packages are called modules.
The thing we want from a module in this exercise is the ability to generate
random numbers. This comes from the random module.

To use a module, at the top of your file, type

    import random

This means you are allowing your Python program to use a module
called random in the rest of your code.

To use it (and generate a random integer), now type:

    a = random.randint(2, 6)

Once you run this program, the variable a will have a random integer that
the computer made for you, between 2 and 6 (including 2 and 6).
The specific documentation for this method is here:

https://docs.python.org/3.3/library/random.html#random.randint

There are many ways you can generate random numbers:
integers, decimals, and much more.
The Python documentation has much more detailed information about
what is possible from the random module.
'''

#modules: random
#tags: randint(), input(), while loop, game