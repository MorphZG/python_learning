''' import class from module car.py '''
from car import Car, Electric_car

# create instance of Electric_car and call
# method from it's parent class
my_tesla = Electric_car('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())

# look at instance my_tesla, find its battery attribute
# and call available methods
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

'''
as with functions (chapter 8), when importing classes you can:

    - import a single class:
    from module import class

    - import multiple classes from module:
    from module import class1, class2, class3

    - import entire module:
    import module

    - import all classes from a module:
    from module import *

dont forget you can use aliases:
    - from [module] import [class] as [alias]
'''



#tags: class import,