# Make a list of 5 usernames, include the name 'admin'
# Print a greeting to each user after they log in.
# Loop through a list and print a greeting to each user.
# If the username is admin print special greeting 'hello admin! would you like report?'
# Otherwise print a generic greeting such as 'hello {user} thanks for logging'

users = ['admin', 'zoki', 'mirjana', 'tina', 'blanka']

for user in users:
    if user == 'admin':
        print('hello admin! would you like a status report?')
    else:
        print(f'hello {user}! thanks for logging in')
