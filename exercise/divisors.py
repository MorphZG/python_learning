'''
Divisors
https://www.practicepython.org/exercise/2014/02/26/04-divisors.html

Exercise 4

Create a program that asks the user for a number and then prints out
a list of all the divisors of that number. (If you don’t know what a
divisor is, it is a number that divides evenly into another number.
For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)

The topics that you need for this exercise combine lists, conditionals,
and user input. There is a new concept of creating lists.

There is an easy way to programmatically create lists of numbers in Python.
To create a list of numbers from 2 to 10, just use the following code:

  x = [num for num in range(2, 11)]

Then the variable x will contain the list [2, 3, 4, 5, 6, 7, 8, 9, 10].
Note that the second number in the range() function is not included in
the original list.

Now that x is a list of numbers, the same for loop can be used with the
list:

  for elem in x: 
    print elem

Will yield the result:

  2
  3
  4
  5
  6
  7
  8
  9
  10

'''

prompt = 'Pick the number, i will print out a list of all divisors: '
user_number = int(input(prompt))

# one liner:
print([div for div in range(1, user_number+1) if user_number % div == 0])

# regular code:
divisors = []
for div in range(1, user_number+1):
    if user_number % div == 0:
        divisors.append(div)
print(divisors)
