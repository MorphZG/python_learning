'''
Make a list called sandwich_orders and fill it with the names of sandwiches.
Make an empty list called finished_sandwiches.
Loop through the list of sandwich orders and print a message for each order,
such as 'i made a tuna sandwich'.
As sandwich is made move it to the list of finished sandwiches.
After all the sandwiches have been made, print a message listing each sandwich.
'''

sandwich_orders = ['katsu', 'chicken chick', 'roastbeef', 'vegetarian']
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f'i am working on your {current_sandwich} sandwich...')
    finished_sandwiches.append(current_sandwich)

print('\n')
for sandwich in finished_sandwiches:
    print(f'i made {sandwich} sandwich')

#tags: list, while loop