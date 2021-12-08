'''
Write a loop that prompts the user to enter a series of pizza topings
until they enter a "quit" value.
As they enter each topping, print you'll add that topping to their pizza.
'''

prompt = 'enter your pizza toppings: \n>'


while True:
    topping = input(prompt)
    if topping == 'quit':
        break
    else:
        print(f'\n- we are adding {topping.upper()} to your pizza\n')