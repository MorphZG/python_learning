# Create a program that simulates how website ensure that everyone has unique username
# Make a list of five or more usernames called current_users
# Make another list of five usernames called new_users, make sure one or two new usernames
# are also in the current_users list
# Loop through the new_users list to see if each new username has already been used.
# If it has, print 'choose another username'
# If a username has not been used print 'username is available'
# Make sure your comparison is case insensitive (John == JOHN)
# (to do this you'll need to make a copy of current_users containing lowercase versions of all existing users.)

current_users = ['jura', 'MIHA', 'stef', 'perica', 'Slavek', 'Lovro', 'luka', 'marina', 'ivana', ]
new_users = ['neno', 'stjepan', 'marko', 'miha', 'tomo', 'Slavek', 'matej']

# Mozemo napraviti kopiju originalne liste sa .lower()
current_users = [user.lower() for user in current_users]  # List comprehension
new_users = [user.lower() for user in new_users]  # List comprehension

for name in new_users:
    if name in current_users:
        print(f'{name} is taken, choose another username')
    else:
        print(f'{name} username is available')

#tags: list, comprehension, for loop