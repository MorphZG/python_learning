# collatz(number)
# if number is even, collatz() prints number//2, return
# if number is odd, collatz() prints 3*number+1, return
# even numbers calculation: (num % 2) == 0
# odd numbers calculation: num % 2 == 1
#
# let user type a number and call collatz() on that number
# until the function returns value 1.

def collatz(number):
    if (number % 2) == 0:
        number = number // 2
        print(number)
        return number
    else:
        number = 3 * number + 1
        print(number)
        return number

user_num = int(input("Give me a number: "))

while user_num != 1:
    user_num = collatz(user_num)
