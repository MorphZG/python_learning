'''
Exercise 11
https://pynative.com/python-basic-exercise-for-beginners/

Write a Program to extract each digit from an integer in the reverse order.

For example, If the given int is 7536, the output shall be “6 3 5 7“,
with a space separating the digits.
'''

number = 7536

while number > 0:
    digit = number % 10    # take the last digit
    print(digit, end=' ')  # print it out
    number = number // 10  # divide number by 10 to get new last digit



# same shit, just having fun with user input
user_number = int(input('give me a number and i will make palindrome: '))

while user_number > 0:
    digit = user_number % 10
    print(digit, end=' ')
    user_number = user_number // 10
