# Refactoring
# page: 206
# Often, you'll come to a point where your code will work, but you'll recognize
# that you could improve the code by breaking it up into a series of functions
# that have specific jobs. This process is called refactoring.
# Refactoring makes your code cleaner, easier to understand and extend.


import json

# Load the username, if it has been stored previously.
def get_stored_username():
    ''' return stored username if available '''
    filename = 'dump_files/username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username

# If not, create and store new username.
def get_new_username():
    ''' prompt for new username '''
    username = input('What is your username? ')
    filename = 'dump_files/username.json'
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username


# greet_user() will call on previous two functions.
def greet_user():
    ''' Greet user by name '''
    username = get_stored_username()
    if username:
        print(f'Welcome back {username}!')
    else:
        username = get_new_username()
        print(f"We'll remember you when you come back, {username}!")

# we have 3 separate functions now so each of them deals with single task.

greet_user()

#modules: json
#tags: dump(), i/o stream, files, refactoring, function