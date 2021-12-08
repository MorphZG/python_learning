'''
-Make dictionary called cities
-Use the name of three cities as keys
-Create dictionary of information about each city
-Include the country that each city is in, approximate population,
and one fact about that city.
-The keys for each city's dictionary should be something like:
country, population, and fact
-Print the name of each city and all of the information you have
stored about it
'''

# Build nested dict()
# dictionary inside dictionary
cities = {

    'zagreb': {
        'country': 'croatia',
        'population': '806.341',
        'fact': 'nepoznato'
    },
    'bjelovar': {
        'country': 'croatia',
        'population': '40.276',
        'fact': 'nepoznato'
    },
    'varazdin': {
        'country': 'croatia',
        'population': '46.943',
        'fact': 'nepoznato'
    }

}

for key, value in cities.items():
    print(key.title())
    for value in value.items():
        print(value, end='')
    print('\n')


'''
Autorovo rjesenje
https://ehmatthes.github.io/pcc_2e/solutions/chapter_6/
'''

for key, value in cities.items():
    drzava = value['country']
    pop = value['population']
    cinjenica = value['fact']

    print(f'{key.title()} is in {drzava}')
    print(f'It have {pop} people living there')
    print('\n')

#tags: dictionary, output format, for loop, items()