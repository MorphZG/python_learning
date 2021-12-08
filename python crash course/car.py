""" A set of classes used to represent gas and electric cars. 
    Docstrings should briefly describe content of every module.
"""

class Car:
    ''' a simple attempt to represent a car. '''

    def __init__(self, make, model, year):
        ''' initialize attributes describing a car '''

        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odomoter(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odomoeter!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles


class Electric_car(Car):
    ''' represent aspects of a car, specific to electric vehicles '''

    def __init__(self, make, model, year):
        ''' initialize all attributes of the parent class with super() '''
        super().__init__(make, model, year)
        # initialize specific attributes of subclass
        self.battery = Battery()        # Instance as attribute, every time
                                        # we initialize Electric_car, it will
                                        # also create an instance of Battery()

    def describe_battery(self):
        ''' print a statement describing the battery size. '''
        print(f"This car has a {self.battery_size}-kwh battery.")


class Battery:
    ''' simple attempt to model a battery for an electric car '''

    def __init__(self, battery_size=75):
        ''' initialize the battery '''
        self.battery_size = battery_size

    def describe_battery(self):
        ''' print a statement describing the battery size. '''
        print(f"This car has a {self.battery_size}-kwh battery.")

    def get_range(self):
        ''' print a statement about the range this battery provides. '''
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
        print(f"This car can go about {range} miles on a full charge.")


#tags: class, inheritance, subclass, super(), __init__(), module