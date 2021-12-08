'''
Python crash course 2e
page 112, exercise 6-7
https://ehmatthes.github.io/pcc/solutions/README.html
'''

friend01 = {
    'fname': 'Marko',
    'lname': 'Juric',
    'age': 30,
    'city': 'Zagreb'
}

friend02 = {
    'fname': 'Matej',
    'lname': 'Grahovac',
    'age': 22,
    'city': 'Zagreb'
}

friend03 = {
    'fname': 'Tomislav',
    'lname': 'Jurjevic',
    'age': 43,
    'city': 'Zagreb'
}

people = [friend01, friend02, friend03]

# Odlicno rjesenje za format teksta. Dodao sam nove varijable
# kod je tako puno pregledniji i output se lakse formatira
for friend in people:
    ime = friend['fname']
    prezime = friend['lname']
    godine = friend['age']
    grad = friend['city']
    print(f'{ime} {prezime} ima {godine} god. i zivi u {grad}')

#tags: dictionary, list, for loop, output format,