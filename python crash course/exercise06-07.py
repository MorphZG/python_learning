'''
Start with the programm you wrote in 6-1 page 99
Make two new dictionaries representing different people
Store all three dictionaries in a list called people
Loop through the list, print every info about each person
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

# !--- Prva solucija
a = 1  # Counting variable
for friend in people:  # Kako formatirati print? print(f'') neradi (rjesenje na line 41)
    print(f'{a} prijatelj: ')
    print(friend['fname'], end=' ')
    print(friend['lname'])
    print(friend['age'])
    print(friend['city'])
    a += 1
    print('')  # Ovo dodaje prazni redak nakon svake iteracije
# !--- kraj


# !--- Druga solucija
# Odlicno rjesenje za format teksta. Dodao sam nove varijable
# kod je tako puno pregledniji i output se lakse formatira
for friend in people:
    ime = friend['fname']
    prezime = friend['lname']
    godine = friend['age']
    grad = friend['city']
    print(f'{ime} {prezime} ima {godine} god. i zivi u {grad}')
# !--- kraj

'''
Rjesenje od autora knjige, nadjeno na:
https://ehmatthes.github.io/pcc/solutions/README.html
'''

#tags: dictionary, list, for loop, output format,