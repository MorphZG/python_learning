'''
Modify your program from from 6-2 page 99
so each person can have more than one favorite number
Print each persons name along with their favorite numbers
'''


favnumbers = {
    'borna': [19, 20, 21],
    'jelena': [6, 14, 100],
    'zoran': [7, 9, 17],
    'tomislav': [44, 36, 28],
    'bruno': [28, 31, 4]
}


for key, value in favnumbers.items():
    print(f'{key} favorite numbers are: ')
    for number in value:
        print(number, end=',')
    print('\n')  # This adds new line after numbers are listed

#tags: dictionary, items()