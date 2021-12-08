'''Sandwiches
Write a function that accepts a list of items a person wants on sandwich.
The function should have one parameter that collects as many items as the function
call provides, and it should print a summary of the sandwich that's being ordered.
Call the function three times, using a different number of arguments each time.
'''

def sandwich(*dodatci):
    ''' builds a sandwich with :*dodatci: '''
    print(f'radim sandwich sa sljedecim dodatcima:\n\t{dodatci}\n')

sandwich('shunka', 'sir')
sandwich('shunka', 'paprika', 'mozzarela')
sandwich('sirni namaz', 'mortadela')
sandwich('pohanac')

# single asterix * represents optional number of positional arguments
# while double asterix ** represents optional number of keyword arguments
# when writing def block, both must be placed after all other parameters

#tags: function, arg, kwarg