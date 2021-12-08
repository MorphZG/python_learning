# Chapter 9, Classes
# Solutions:
# https://ehmatthes.github.io/pcc_2e/solutions/solutions/

'''
Make a class called Restaurant. the __init__() method for Restaurant should
store two attributes: a restaurant_name and a cuisine_type.
Make a method called describe_restaurant() that prints these two pieces of
information, and a method called open_restaurant() that prints a message
indicating that restaurant is open.

Make an instance called restaurant01 from your class. Print the two attributes
individually, and than call both methods.
'''

'''
__init__() is a special method that python runs automatically whenever
we create a new instance of a class. This method have leading and trailing
dunder (double underscore), a convention that helps prevent default method
names from conflicting with user method names.

We define __init__() to have first required parameter self, before all others.
Doesnt have to be called self (it is name by convention) but must be included
in the definition as first parameter. When python calls __init__() method
later (to create the instance of class) the method call will automatically
pass the self argument which is the reference to the instance itself, it
gives the individual instance access to the attributes and methods in the
class

We can define aditional attributes under __init__() method that are not passed
as parameters. Look at exercise9-4 to see example.
'''


# build class called Restaurant
class Restaurant:
    ''' creates the class Restaurant '''

    def __init__(self, restaurant_name, cuisine_type):
        ''' initialize Restaurant instance '''
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.location = 'Zagreb'  # additional attribute

    def describe_restaurant(self):
        ''' method that prints the name and cuisine type '''
        print(f"{self.restaurant_name} is a restaurant with {self.cuisine_type} kitchen.")

    def open_restaurant(self):
        ''' method that opens the restaurant '''
        print(f"{self.restaurant_name} is now open!")


# make instance called restaurant01
restaurant01 = Restaurant('Gladne oci', 'American')

# printing the attrubutes of restaurant
print(restaurant01.restaurant_name)
print(restaurant01.cuisine_type)

# calling the methods of restaurant
restaurant01.describe_restaurant()
restaurant01.open_restaurant()

# printing additional attribute that is not passed as parameter
print(restaurant01.location)

#tags: class, basics, self, __init__(), initialize, method,