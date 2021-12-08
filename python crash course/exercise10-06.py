# Chapter 10, Files and exceptions
# Solutions:
# https://ehmatthes.github.io/pcc_2e/solutions/solutions/

''' Addition
One common problem when promting for numerical input occurs when people
provide text instead of numbers. When you try to convert the input to an
int, you'll get a ValueError. Write a program that prompts for two numbers.
Add them together and print the result. Catch the ValueError if either input
value is not a number, and print a friendly error message. Test your program
by entering two numbers and then by entering some text instead of a number.
'''

try:
    x = int(input('Enter first number: '))
    y = int(input('Enter second number: '))
except ValueError:
    print('\tWrong input!')
    print('\tEnter only numbers')
else:
    total = x + y
    print(f'your total is: {total}')

#tags: exception, error, try-except-else,