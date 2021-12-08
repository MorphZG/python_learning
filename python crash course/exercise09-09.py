# Chapter 9, Classes
# Solutions:
# https://ehmatthes.github.io/pcc_2e/solutions/solutions/

'''
Use the final version of electric_car.py from this section.
Add a method to the Battery class upgrade_battery(). This method
should check the battery size and set the capacity to 100 if it
isn't already. Make an electric car with a default battery size,
call get_range() once, and than call get_range() second time after
upgrading the battery. You should see an increase in the car's range. 
'''

# primjer autorovog rjesenja nalazi se u komentarima na dnu

class Car:
    ''' a simple attempt to represent a car. '''

    def __init__(self, make, model, year):
        ''' initialize attributes of car '''
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        ''' return descriptive name '''
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        ''' print car's mileage '''
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odomoter(self, mileage):
        '''
        set the odometer to given value
        reject the change if it tries to roll back miles
        '''
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odomoeter!")

    def increment_odometer(self, miles):
        ''' add the given amounts to odometer reading '''
        self.odometer_reading += miles


class Electric_car(Car):
    ''' represent aspects of a car, specific to electric vehicles '''

    def __init__(self, make, model, year):
        '''
        initialize all attributes of the parent class with super()
        than initialize attributes specific to subclass
        '''
        super().__init__(make, model, year)
        
        self.battery = Battery()        # Instance as attribute, every time
                                        # we initialize Electric_car, it will
                                        # also create an instance of Battery()

    def describe_battery(self):
        ''' print a statement describing the battery size. '''
        print(f"This car has a {self.battery_size}-kwh battery.")


class Battery:
    ''' simple attempt to model a battery for an electric car '''

    def __init__(self, battery_size=75):
        ''' initialize the battery's attributes. '''
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

    def upgrade_battery(self):
        ''' increase the battery size '''
        if self.battery_size < 100:
            print('upgrading the battery...')
            self.battery_size = 100
        else:
            print('battery is already at max capacity')


# create instance of Electric_car
moj_auto = Electric_car('tesla', 'one', 2020)

# call get_range(), upgrade_battery(), get_range()
moj_auto.battery.get_range()
moj_auto.battery.upgrade_battery()
moj_auto.battery.get_range()


'''
                    AUTOROVO RJESENJE

class Car():
    """A simple attempt to represent a car."""

    def __init__(self, manufacturer, model, year):
        """Initialize attributes to describe a car."""
        self.manufacturer = manufacturer
        self.model = model
        self.year = year
        self.odometer_reading = 0
        
    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.manufacturer} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")
        
    def update_odometer(self, mileage):
        """
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    
    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles

class Battery():
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size=75):
        """Initialize the batteery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
            
        message = f"This car can go approximately {range}"
        message += " miles on a full charge."
        print(message)

    def upgrade_battery(self):
        """Upgrade the battery if possible."""
        if self.battery_size == 75:
            self.battery_size = 100
            print("Upgraded the battery to 100 kWh.")
        else:
            print("The battery is already upgraded.")
    
        
class ElectricCar(Car):
    """Models aspects of a car, specific to electric vehicles."""

    def __init__(self, manufacturer, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(manufacturer, model, year)
        self.battery = Battery()


print("Make an electric car, and check the range:")
my_tesla = ElectricCar('tesla', 'roadster', 2019)
my_tesla.battery.get_range()

print("\nUpgrade the battery, and check the range again:")
my_tesla.battery.upgrade_battery()
my_tesla.battery.get_range()
'''

#tags: class, inheritance, subclass, super(), __init__(), attribute