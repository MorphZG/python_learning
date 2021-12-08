'''
Make several dictionaries, where each dictionary represents a different pet
In each dictionary, include the kind of animal and the owner's name
Store these dictionaries in a list called pets
Next, loop through your list and as you do print everything you know about each pet
'''

pet1 = {
    'animal type': 'ribica',
    'name': 'jackie',
    'eats': 'bugs',
    'owner': 'zoran'
}

pet2 = {
    'animal type': 'zamorac',
    'name': 'jura',
    'eats': 'grass',
    'owner': 'mirjana'
}

pet3 = {
    'animal type': 'pas',
    'name': 'rocky',
    'eats': 'meat',
    'owner': 'tina'
}

pets = [pet1, pet2, pet3]

for pet in pets:
    print(f"\nHere's what I know about {pet['name'].title()}:")
    for key, value in pet.items():
        print(f"\t{key}: {value}")

'''
Autorova rjesenje:
https://ehmatthes.github.io/pcc_2e/solutions/chapter_6/
'''

#tags: dictionary, list, for loop, format,