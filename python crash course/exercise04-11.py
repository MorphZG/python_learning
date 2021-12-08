# Start with programm from 4-1
# Make the copy of the list of pizzas and call it friend_pizzas
# Add a new pizza to the original list
# Add a different pizza to the friend_pizzas
# Prove that you have two separate lists
# Print 'My favorite pizzas are:' and use for loop to print first list
# Print 'My friend favorite pizzas are:' and use for loop to print second list
# Make sure each new pizza is stored in appropriate list

pizzas = ['margarita', 'mjesana', 'slavonska']
for pizza in pizzas:
    print(pizza)
    print(f"i really like {pizza.upper()} with good cheese\n")
print('I eat pizza once a month')

friend_pizzas = pizzas[:]

pizzas.append('nova pizza')
friend_pizzas.append('different pizza')

print('\nWe have two separate pizza list')
print(pizzas)
print(friend_pizzas)

print('\nMy favorite pizzas are: ')
for i in pizzas:
    print(i)

print('\nMy friend favorite pizzas are: ')
for i in friend_pizzas:
    print(i)


#tags: list, for loop, slice,        