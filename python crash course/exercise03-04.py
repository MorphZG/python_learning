import copy
# exercise 3-4 Guest List
guests0 = ['Tina', 'Mirjana', 'Zoran']
message0 = f'Hello {guests0[0]}! You have been invited to dinner.'
message1 = f'Hello {guests0[1]}! You have been invited to dinner.'
message2 = f'Hello {guests0[2]}! You have been invited to dinner.'
print(message0, message1, message2, sep='\n')
print('\n')

# exercise 3-5 Changing Guest List
print(f'{guests0[2]} cant make it and will be replaced')
print('--- index of "Zoran" is: ', guests0.index('Zoran'), '---')
guests2 = copy.copy(guests0)
guests2[2] = 'Davidenko'
message0 = f'Hello {guests2[0]}! You have been invited to dinner.'
message1 = f'Hello {guests2[1]}! You have been invited to dinner.'
message2 = f'Hello {guests2[2]}! You have been invited to dinner.'
print(message0, message1, message2, sep='\n')
print('\n')

# exercise 3-6 More Guests
guests3 = copy.copy(guests2)
print('Good news everyone! We found a bigger table so we can invite more people!')
guests3.insert(0, 'Luka')
guests3.insert(2, 'Blanka')
guests3.append('Nikola')
for g in guests3:  # i am ahead of book here, no for loop by now.
    print(f'Hello {g}! You have been invited to dinner----msg for all----.')
print('\n')

# exercise 3-7 Shrinking Guest List
message = 'We have several lists named "guests" : \n'
print(message)
print('guests0 > ', *guests0, '\n', 'guests2 > ', *guests2, '\n', 'guests3 > ', *guests3)
message = 'Because of some technical problems we can invite only 2 guests!'
print('\n', message)

# leave 2 names in list, pop() everyone else.
message = f'Sorry {guests3[5]} your invite is canceled'
guests3.pop(5)
print(message)
message = f'Sorry {guests3[4]} your invite is canceled'
guests3.pop(4)
print(message)
message = f'Sorry {guests3[3]} your invite is canceled'
guests3.pop(3)
print(message)
message = f'Sorry {guests3[2]} your invite is canceled'
guests3.pop(2)
print(message)
print(*guests3, '> You are still invited, no need to worry')
# delete everyone but keep empty list
del guests3[:]
print(f'list guests3 is empty > ', guests3)

#modules: copy
#tags: list, insert(), append(), pop()