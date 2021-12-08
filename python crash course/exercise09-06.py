# Chapter 9, Classes
# Solutions:
# https://ehmatthes.github.io/pcc_2e/solutions/solutions/

'''Ice Cream Stand
An ice cream stand is a specific kind of restaurant. Write a class called
IceCreamStand that inherits from the Restaurant class you wrote in 9-1 or 9-4.
Either version of the class will work, just pick one you like better.
Add an attribute called flavors that stores a list of ice cream flavors.
Write a method that displays these flavors. Create an instance of
IceCreamStand and call this method.
'''


# Restaurant class copied from exercise9-4.py
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


# subclass that inherits from Restaurant class
class IceCreamStand(Restaurant):
    ''' subclass of Restaurant '''

    def __init__(self, restaurant_name, cuisine_type):
        ''' initialize all attributes from parent class with super() '''
        super().__init__(restaurant_name, cuisine_type)
        
        # adding attributes specific to subclass
        self.flavors = []

    def set_flavors(self, *args):
        ''' optional number of arguments will append to list of flavors '''
        for i in args:
            self.flavors.append(i)

    def get_flavors(self):
        ''' print list of flavors '''
        print('Ovo je nasa lista okusa!')
        print(self.flavors)
        print('\nMoguce je dobiti i pojedinacne okuse koristeci index:')
        print('\tprint([instance].flavors[index])')


# create an instance of IceCreamStand
moj_sladoled = IceCreamStand('Moj Restac', 'Slasticarna')

# fill the list of flavors with created method
moj_sladoled.set_flavors('cokolada', 'vanilija', 'cookie')
moj_sladoled.set_flavors('kokos', 'orah')

# display available flavors
moj_sladoled.get_flavors()


#tags: class, inheritance, subclass, super(), __init__(), arg, kwarg