# Chapter 9, Classes
# Solutions:
# https://ehmatthes.github.io/pcc_2e/solutions/solutions/

'''Privileges
Write a separate Privileges class. The class should have one attribute,
privileges, that stores a list of strings as described in exercise9-7.
Move the show_privileges() method to this class. Make a Privileges instance
as an attribute in the Admin class. Create a new instance of Admin and use
your method to show its privileges.
'''

# primjer autorovog rjesenja nalazi se u komentarima na dnu


# copy class User from 9-7
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


# copy subclass Administrator from 9-7
# create attribute privileges that builds instance of class Privileges()
class Administrator(User):
    ''' subclass of User '''

    def __init__(self, first_name, last_name, email):
        ''' initialize basic attributes '''
        super().__init__(first_name, last_name, email)

        self.privileges = Privileges()  # instance as attribute
                                        # when initializing Administrator
                                        # create instance of Privileges()
                                        # under attribute self.privileges


# create new class Privileges
class Privileges:
    ''' class to store Administrator privileges '''

    def __init__(self):
        ''' initialize attributes '''
        self.privileges = ['can add post', 'can delete post', 'can ban user']

    def show_privileges(self):
        ''' prints the list of privileges '''
        print(self.privileges)


# create instance of Administrator class
zoran = Administrator('zoran', 'topic', 'zoran1607@gmail.com')

# instance . attribute . method
zoran.privileges.show_privileges()


'''
                INTERESANTNO AUTOROVO RJESENJE

pogledaj kako je odradio listu privilegija. napravio je praznu listu
kao parametar. onda je izgradio erika kao admina. napravio je listu njegovih
privilegija kao zasebnu listu i dodjelio ih je varijabli eric_privileges.
na kraju je samo usmjerio erikove atribute prema varijabli eric_privileges.


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
        
        # Initialize an empty set of privileges.
        self.privileges = Privileges()


class Privileges():
    """A class to store an admin's privileges."""

    def __init__(self, privileges=[]):
        self.privileges = privileges

    def show_privileges(self):
        print("\nPrivileges:")
        if self.privileges:
            for privilege in self.privileges:
                print(f"- {privilege}")
        else:
            print("- This user has no privileges.")


eric = Admin('eric', 'matthes', 'e_matthes', 'e_matthes@example.com', 'alaska')
eric.describe_user()

eric.privileges.show_privileges()

print("\nAdding privileges...")
eric_privileges = [
    'can reset passwords',
    'can moderate discussions',
    'can suspend accounts',
    ]
eric.privileges.privileges = eric_privileges
eric.privileges.show_privileges()
'''

#tags: class, inheritance, subclass, super(), __init__(), attributes