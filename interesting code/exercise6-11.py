''':
Python crash course 2e
page 112, exercise 6-11
https://ehmatthes.github.io/pcc_2e/solutions/chapter_6/
'''

# nested dict()
cities = {

    'zagreb':{
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

# varijable postavljene unutar for loopa
# formatiranje teksta je tada puno jednostavnije
for key, value in cities.items():
    drzava = value['country']
    pop = value['population']
    cinjenica = value['fact']

    print(f'{key.title()} is in {drzava}')
    print(f'It have {pop} people living there')


#tags: dictionary, output format, for key, value