# Chapter 10, Files and exceptions
# Solutions:
# https://ehmatthes.github.io/pcc_2e/solutions/solutions/

'''Verify User
The final listing for remember_me.py assumes either that the user has already
entered their username or that the program is running for the first time.
We should modify it in case the current user is not the person who last used
the program.

Before printing a welcome back message in greet_user(), ask the user if this
is the correct username. If it’s not, call get_new_username() to get the
correct username.
'''

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


def get_new_username():
    ''' prompt for new username '''
    username = input('What is your username? ')
    filename = 'dump_files/username.json'
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username


# greet_user() will call on previous two functions.
# check do we have right username, if no than call get_new_username()
def greet_user():
    ''' Greet user by name '''
    username = get_stored_username()
    if username:
        print(f'Hi {username}!')
        name_check = input('Is that you? (yes/no)')
        if name_check == 'yes':
            print(f'Welcome back {username}!')
        else:
            username = get_new_username()
            print(f"We'll remember you when you come back, {username}!")


greet_user()



'''
        <! --- AUTOROV KOMENTAR
You might notice the identical else blocks in this version of greet_user().
One way to clean this function up is to use an empty return statement.
An empty return statement tells Python to leave the function without
running any more code in the function.

Here’s a cleaner version of greet_user():

    def greet_user():
        """Greet the user by name."""
        username = get_stored_username()
        if username:
            correct = input(f"Are you {username}? (y/n) ")
            if correct == 'y':
                print(f"Welcome back, {username}!")
                return
        # We got a username, but it's not correct.
        # Let's prompt for a new username.
        username = get_new_username()
        print(f"We'll remember you when you come back, {username}!")

The return statement means the code in the function stops running after
printing the welcome back message. When the username doesn’t exist, or
the username is incorrect, the return statement is never reached. The
second part of the function will only run when the if statements fail,
so we don’t need an else block. Now the function prompts for a new username
when either if statement fails.

The only thing left to address is the nested if statements. This can be
cleaned up by moving the code that checks whether the username is correct
to a separate function. If you’re enjoying this exercise, you might try
making a new function called check_username() and see if you can remove
the nested if statement from greet_user().

'''

#modules: json
#tags: dump(), i/o stream, files, function