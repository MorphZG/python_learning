'''
https://www.practicepython.org/exercises/

Exercise 02: Odd or Even
https://www.practicepython.org/exercise/2014/02/05/02-odd-or-even.html

'''
prompt01 = 'Enter int number: '
number = int(input(prompt01))

if number % 2 == 0:
    if number % 4 == 0:
        print('number is multiple of 4')
    else:
        print('number is even')
else:
    print('number is odd')