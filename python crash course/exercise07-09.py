'''
Using the list sandwich_orders from 7-8,
Make sure the sandwich 'pastrami' appears in the list at least three times.
Add code near the beginning of your program to print 'deli has run out of pastrami'
Use a while loop to remove all occurrences of 'pastrami' from sandwich_orders
Make sure no pastrami sandwiches end up in finished_sandwiches.
'''

sandwich_orders = [
    'katsu', 'pastrami', 'chicken chick',
    'pastrami', 'roastbeef', 'pastrami', 'vegetarian'
    ]

finished_sandwiches = []

print('deli has run out of pastrami')

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f'i am working on your {current_sandwich} sandwich...')
    finished_sandwiches.append(current_sandwich)

print('\n')
for sandwich in finished_sandwiches:
    print(f'i made {sandwich} sandwich')

#tags: list, while loop