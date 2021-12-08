# Chapter 9, Classes
# Solutions:
# https://ehmatthes.github.io/pcc_2e/solutions/solutions/

'''
Make a class called User. Create two attributes called first_name and
last_name, and then create several other attributes that are typically
stored in a user profile. Make a method called describe_user() that
prints a summary of the user's information. Make another method called
greet_user() that prints a personalized greetings to a user.

Create several instances representing different users, and call both
methods for each user.
'''


# make class User
class User:
    ''' users of service '''

    def __init__(self, first_name, last_name, email, phone):
        ''' initialize User instance '''
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.email = email
        self.phone = phone

    def greet_user(self):
        print(f'hello {self.first_name}! Welcome!')

    def describe_user(self):
        print(f'{self.first_name} {self.last_name}')
        print(f' - e-mail: {self.email}')
        print(f' - phone: {self.phone}')


# create 3 instances of User class
user01 = User('ana', 'popovic', 'ana@email.com', '09934564')
user02 = User('stjepan', 'kolarevic', 'stjepan@email.com', '0911224')
user03 = User('ivona', 'popovic', 'ivona@gmail.com', '09845566')

# call both methods for each user
user01.greet_user()
user01.describe_user()
print()
user02.greet_user()
user02.describe_user()
print()
user03.greet_user()
user03.describe_user()

#tags: class, basics, self, method