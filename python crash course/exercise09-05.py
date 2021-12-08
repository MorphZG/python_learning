# Chapter 9, Classes
# Solutions:
# https://ehmatthes.github.io/pcc_2e/solutions/solutions/

'''Login Attempts
Add and attribute called login_attempts to your User class from 9-3.
Write a method called increment_login_attempts() that increments the
value of login_attempts by 1. Write another method called
reset_login_attempts() that resets value of login_attempts to 0.

Make an instance of the User class and call increment_login_attempts()
several times. Print the value of login_attempts to make sure it was
incremented properly, and then call reset_login_attempts(). Print
login_attempts again to make sure it was reset to 0.
'''


# make class User
class User:
    ''' users of service '''

    def __init__(self, first_name, last_name, email, phone):
        ''' initialize User '''
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.email = email
        self.phone = phone
        self.login_attempts = 0  # additional attribute, not passed as parameter

    def greet_user(self):
        ''' print basic greeting '''
        print(f'hello {self.first_name}! Welcome!')

    def describe_user(self):
        ''' print user info '''
        print(f'{self.first_name} {self.last_name}')
        print(f' - e-mail: {self.email}')
        print(f' - phone: {self.phone}')

    def increment_login_attempts(self):
        ''' increment login_attempts value by 1 '''
        self.login_attempts += 1

    def reset_login_attempts(self):
        ''' reset login_attempts to 0 '''
        self.login_attempts = 0


# create instance of User class
user01 = User('ana', 'popovic', 'ana@email.com', '09934564')


# calling the increment_login_attempts()
# it should increment the value by 1 for ever call
user01.increment_login_attempts()
user01.increment_login_attempts()
user01.increment_login_attempts()

# test, the value should be 3
print(user01.login_attempts)

# call the reset_login_attempts()
user01.reset_login_attempts()

# value should be back to 0
print(user01.login_attempts)

#tags: class, basics, self, method