'''T-Shirt
Write a function called make_shirt()
It must accept size and the text of amessage that should be printed on shirt.
Function should print a sentence summarizing the size of the shirt and the message on it.
Call the function once using positional arguments.
Call it second time using keyword arguments.
'''


def make_shirt(size, message):
    print(f'This shirt size is {size}')
    print(f'Message printed is {message}')
    print('\n')


# Function call with positional arguments
make_shirt('L', 'adidas')

# Function call with keyword arguments
make_shirt(message='adidas', size='L')
