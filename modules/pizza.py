
def make_pizza(size, *toppings):
    '''Sumarize the pizza we are about to make'''
    print(f'\nMaking a{size}-inch pizza with the following toppings: ')
    for topping in toppings:
        print(f'- {toppings}')


