# Chapter 10, Files and exceptions
# Solutions:
# https://ehmatthes.github.io/pcc_2e/solutions/solutions/

''' Addition Calculator
Wrap your code from 10-6 in a while loop so the user can continue entering
numbers even if they make a mistake and enter text instead of number.
'''

calculate = True
while calculate:
    answer = input('would you like to make some calculatons? (yes/no) : ')
    if answer == 'no':
        break
    else:
        try:
            x = int(input('Enter first number: '))
            y = int(input('Enter second number: '))
        except ValueError:
            print('\tWrong input!')
            print('\tEnter only numbers')
        else:
            total = x + y
            print(f'your total is: {total}')


#   <! --- AUTOROVO RJESENJE
'''
print("Enter 'q' at any time to quit.\n")

while True:
    try:
        x = input("\nGive me a number: ")
        if x == 'q':
            break

        x = int(x)

        y = input("Give me another number: ")
        if y == 'q':
            break

        y = int(y)

    except ValueError:
        print("Sorry, I really needed a number.")

    else:
        sum = x + y
        print(f"The sum of {x} and {y} is {sum}.")
'''

#tags: exception, error, while loop,