# https://replit.com/@appbrewery
# day-10
# Calculator

# original program from the day_10 have loop feature so you can calculate
# until user decide to quit. I wanted to keep the code clean with focus
# on functions inside dictionary. Dictionary actually doesnt store functions,
# instead it holds the names that you later pass to a variable.
# Add parenthesis to that variable and you have function.
# stored_name(param1, param2)


def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

#   <! --- will call functions from this dictionary
operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}

num1 = int(input('Enter first number: '))
num2 = int(input('Enter second number: '))

for k in operations:
    print(k)

# user inputs dictionary key
operation_key = input('Pick an operation from the line above: ')

# i got the key on right so i can pull the value to variable on left
calculation_name = operations[operation_key]
result_1 = calculation_name(num1, num2)  # calculation_name() is actually one of the functions on top

print(f'{num1} {operation_key} {num2} = {result_1}')

# chain calculations
print('Type "y" to continue calculating with {result_1} or type "n" to exit')
loop_again = input('>>> ')


#tags: call function from dictionary, calculator