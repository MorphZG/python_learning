# Chapter 9, Classes
# Solutions:
# https://ehmatthes.github.io/pcc_2e/solutions/solutions/

'''
Start with your class from 9-1. Create three different instances from the class,
and call describe_restaurant() for each instance.
'''


# build class called Restaurant
class Restaurant:
    ''' creates the class Restaurant '''

    def __init__(self, restaurant_name, cuisine_type):
        ''' initialize Restaurant instance '''
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        ''' method that prints the name and cuisine type '''
        print(f"{self.restaurant_name} is a restaurant with {self.cuisine_type} kitchen.")

    def open_restaurant(self):
        ''' method that opens the restaurant '''
        print(f"{self.restaurant_name} is now open!")


# make first instance
restaurant01 = Restaurant('Swing', 'American')
restaurant02 = Restaurant('Hammingway', 'British')
restaurant03 = Restaurant('Gladne oci', 'Croatian')

# call describe_restaurant() for each instance
restaurant01.describe_restaurant()
restaurant02.describe_restaurant()
restaurant03.describe_restaurant()

#tags: class, basics, self, method