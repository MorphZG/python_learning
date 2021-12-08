'''
Fibonacci
Exercise 13 (and Solution)
https://www.practicepython.org/exercise/2014/04/30/13-fibonacci.html

Write a program that asks the user how many Fibonnaci numbers to generate
and then generates them. Take this opportunity to think about how you can
use functions. Make sure to ask the user to enter the number of numbers
in the sequence to generate.(Hint: The Fibonnaci seqence is a sequence of
numbers where the next number in the sequence is the sum of the previous
two numbers in the sequence. The sequence looks like this:
1, 1, 2, 3, 5, 8, 13, …)
'''


def izracunaj_fib(x):
    ''' ako je x broj 5 racuna fib petog broja u nizu,
        a ne fib od broja pet
    '''
    if x <= 1:
        return x
    else:
        return(izracunaj_fib(x-1) + izracunaj_fib(x-2))


duljina = int(input('how many fib numbers you need?'))
fibonacci_sequence = []

for num in range(duljina):
    fibonacci_sequence.append(izracunaj_fib(num))
print(fibonacci_sequence)


# alternativni kod, bez funkcije, while loop.

user_input = 10
counted = 0

fibonacci_sequence = []
n1, n2 = 0, 1   # prva dva broja da bi mogao zadati pravila zbrajanja

while counted < user_input:
    fibonacci_sequence.append(n1)
    next = n1 + n2
    n1 = n2
    n2 = next
    counted += 1

print(fibonacci_sequence)


'''
Calculating the Fibonacci Sequence is a perfect use case for recursion.
A recursive function is a function that calls on itself to solve a problem.

In function calculate_fib() we call the same function inside it self to
calculate the sum of the preceding two items in the sequence.

this formula can describe the sequence:
f(1) = 0     ---------------------- prvi broj u nizu
f(2) = 1     ---------------------- drugi broj u nizu
f(n) = f(n-1) + f(n-2) if n > 2 --- ostatak niza
'''



def calculate_fib(num):  # ova funkcija daje fib num broja u nizu
    if num <= 1:
        return num
    else:
        return(calculate_fib(num-1) + calculate_fib(num-2))


user_input = 10
for x in range(user_input):
    print(calculate_fib(x), end=', ')

# Read more about similar code:
# https://www.pythontutorial.net/advanced-python/python-fibonacci-sequence/

#tags: fibonacci, loop, recursion, funcion,