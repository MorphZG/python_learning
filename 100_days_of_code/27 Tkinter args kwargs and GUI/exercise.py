# <! --- exercise 01
# Modify the add function to take an unlimited number of arguments. Use a loop
# to sum all the arguments inside the function. Test it out by calling add() to
# calculate sum of some argumbents.

def add(*args):
    """ returns the sum of all numbers passed in as arguments """
    total = 0
    for num in args:
        total += num
    return total

sum_of_numbers = add(7, 7, 7, 7)
print(f'here is the result of add() ---> {sum_of_numbers}')

print('\n')

# <! --- exercise 02
def calculate(num, **kwargs):
    """ experiment with **kwargs, can use them as dictionary """
    print('--- calling calculacte() ----')
    print(type(kwargs))

    for key, value in kwargs.items():
        print(f'this is key: {key}')
        print(f'this is value: {value}')

    num += kwargs['add']
    print(f'this is first, positional argument: {num}')
    num *= kwargs['multiply']
    print(f'this is first, positional argument: {num}')


# call calculate with different key/value pairs
calculate(2, add=3, multiply=5)





#tags: args, kwargs
