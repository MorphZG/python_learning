'''Large Shirts
Modify the make_shirt() function so that shirts are large by default
with a message that reads 'I love python.'
Make a large shirt and a medium shirt with the default message,
and a shirt of any size with a different message
'''


def make_shirt(message='I love python', size='Large'):
    ''' ovdje ide objasnjenje funkcije 
    help(ime_funkcije) printa ovaj komentar '''
    print(f'this shirt is {size} size')
    print(f'message says: {message}')
    print('\n')


# Default message and default size
make_shirt()

# Default message, size medium
make_shirt(size='medium')

# Different message, different size
make_shirt(size='small', message='No message')


help(make_shirt)

#tags: function, help(), docstring,