'''
Make a dictionary called favorite_places.
Think of three names to use as keys, and store one to three
favorite places for each person.
Ask some friends to name a few of their favorite places, 
Loop through the dictionary and print each persons name and their places
'''

favorite_places = {
    'igor': ['bjelovar', 'zagreb', 'varazdin'],
    'tomislav': ['virovitica', 'split', 'murter'],
    'bruno': ['zagreb', 'ogulin', 'murter']
}

for key, places in favorite_places.items():
    print(f'Favorite place of {key.title()} is:')
    for place in places:
        print(f'\t-{place.title()}')


'''
Autorova rjesenja
https://ehmatthes.github.io/pcc_2e/solutions/chapter_6/
'''

#tags: dictionary, list, for loop, format,