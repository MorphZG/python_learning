# Chapter 9, Classes
# Solutions:
# https://ehmatthes.github.io/pcc_2e/solutions/solutions/

'''Admin
An administrator is a special kind of user. Write a class called Admin that
inherits from the User class you wrote in 9-3 or 9-5. Add an attribute,
privileges, that stores a list of strings like "can add post",
"can delete post", "can ban user" and so on. Write a method called
show_privileges() that lists the administrators's set of privileges. Create an
instance of Admin and call your method.
'''

# primjer autorovog rjesenja nalazi se u komentarima na dnu


# modified User class from exercise9-5
class User:
    ''' users of service '''

    def __init__(self, first_name, last_name, email):
        ''' initialize User '''
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.email = email
        # additional attributes:
        self.phone = 'instance.phone = number_as_string'
        self.login_attempts = 0

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


class Administrator(User):
    ''' subclass of User '''

    def __init__(self, first_name, last_name, email):
        ''' initialize basic attributes '''
        super().__init__(first_name, last_name, email)
        self.privileges = ['can add post', 'can delete post', 'can ban user']

    def show_privileges(self):
        ''' prints privileges '''
        print(self.privileges)


# create instance of Administrator class
zoran = Administrator('zoran', 'topic', 'zoran1607@gmail.com')

# call method that prints privileges attribute
zoran.show_privileges()

# testing additional attributes:
zoran.phone = '099/6395-089'
print(zoran.phone)
help(zoran)


'''
                INTERESANTNO AUTOROVO RJESENJE

class User():
    """Represent a simple user profile."""

    def __init__(self, first_name, last_name, username, email, location):
        """Initialize the user."""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.email = email
        self.location = location.title()
        self.login_attempts = 0

    def describe_user(self):
        """Display a summary of the user's information."""
        print(f"\n{self.first_name} {self.last_name}")
        print(f"  Username: {self.username}")
        print(f"  Email: {self.email}")
        print(f"  Location: {self.location}")

    def greet_user(self):
        """Display a personalized greeting to the user."""
        print(f"\nWelcome back, {self.username}!")

    def increment_login_attempts(self):
        """Increment the value of login_attempts."""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Reset login_attempts to 0."""
        self.login_attempts = 0


class Admin(User):
    """A user with administrative privileges."""

    def __init__(self, first_name, last_name, username, email, location):
        """Initialize the admin."""
        super().__init__(first_name, last_name, username, email, location)
        self.privileges = []

    def show_privileges(self):
        """Display the privileges this administrator has."""
        print("\nPrivileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")


eric = Admin('eric', 'matthes', 'e_matthes', 'e_matthes@example.com', 'alaska')
eric.describe_user()

eric.privileges = [
    'can reset passwords',
    'can moderate discussions',
    'can suspend accounts',
    ]

eric.show_privileges()
'''

#tags: class, inheritance, subclass, super(), __init__(), attributes