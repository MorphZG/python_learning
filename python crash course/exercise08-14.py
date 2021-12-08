'''Cars
Write a function that stores information about car in a dictionary.
The function should always receive a manufacturer and a model name.
It should than accept an arbitrary number of keyword arguments.
Call the function with the required information and two other name-value
pairs, such as a color or and optional feature. Your function should work
for a call like this one:
  
    > car = make_car('subaru', 'outback', color='blue', tow_package=True)

Print the dictionary that's returned to make sure all the
information was stored correctly.
'''


# gradim klasican dictionary za poznate parametre(ime i prezime)
# obzirom da neznam koliko ce biti ostalih itema
# njih odredujem kao **kwargs
# radim for loop koji ce popuniti prethodno definirani dictionary

def make_car(manufacturer, model, **kwargs):
    ''' make a dict() representing a car '''

    car_dict = {
    'proizvodjac': manufacturer,
    'vrsta': model,
    }

    for k, v in kwargs.items():
        car_dict[k] = v

    return car_dict


car = make_car('subaru', 'outback', godina='1998', registracija=None)
car2 = make_car('toyota', 'corola', godina='2010', registracija=True, color='black')
print(car, car2, sep='\n')

# single asterix * represents optional number of positional arguments
# while double asterix ** represents optional number of keyword arguments

#tags: function, dictionary, arg, kwarg,