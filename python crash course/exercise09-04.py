# Chapter 9, Classes
# Solutions:
# https://ehmatthes.github.io/pcc_2e/solutions/solutions/

'''Number Served
Start with your program from 9-1. Add and attribute called number_served with
a default value of 0. Create an instace called restaurant from this class.
Print the number of customers the restaurant has served, and than change
this value and print it again.

Add a method called set_number_served() that lets you set the number of
customers that have been served. Call this method with a new number and
print the value again.

Add a method called increment_number_served() that lets you increment the
number of customers who've been served. Call this method with any number
you like that could represent how many customers were served in, say, a
day of business.
'''


# build class called Restaurant
class Restaurant:
    ''' creates the class Restaurant '''

    def __init__(self, restaurant_name, cuisine_type):
        ''' initialize Restaurant instance '''
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0  # additional attribute, not passed as parameter

    def describe_restaurant(self):
        ''' method that prints the name and cuisine type '''
        print(f"{self.restaurant_name} is a restaurant with {self.cuisine_type} kitchen.")

    def open_restaurant(self):
        ''' method that opens the restaurant '''
        print(f"{self.restaurant_name} is now open!")

    def set_number_served(self, number):
        ''' change the number of served customers '''
        if number >= self.number_served:
            self.number_served = number
        else:
            print('you cant lower the number of served customers')

    def increment_number_served(self, increment):
        ''' increment number of served customers '''
        if increment >= 0:
            self.number_served += increment
        else:
            print('you cant lower the number of served customers')


# make instance called restaurant
restaurant = Restaurant('Murter', 'fine food')

# number of served customers at default 0
print(f'number of served customers: {restaurant.number_served}')

# changing the value to 7
restaurant.number_served = 7
print(f'number of served customers: {restaurant.number_served}')

# call the method to change the value of served customers
restaurant.set_number_served(15)
print(f'number of served customers: {restaurant.number_served}')

# call the method to increment the number of served customers
restaurant.increment_number_served(10)
print(f'number of served customers: {restaurant.number_served}')


#tags: class, basics, self, __init__(), initialize, method