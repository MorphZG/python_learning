# Add an if test to 5-8 to make sure the list of users is not empty
# If the list is empty print 'we need to find some users'
# Remove all users from list to make sure correct msg is printed

users = []

if users:
    for user in users:
        if user == 'admin':
            print('hello admin! would you like a status report?')
        else:
            print(f'hello {user}! thanks for logging in')
else:
    print('we need to find some users')
    