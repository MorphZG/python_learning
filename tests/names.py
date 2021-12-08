from name_function import get_formatted_name


print('enter "q" at any time to quit.')

while True:
    first = input('Please give me your first name: ')
    if first == 'q':
        break
    last = input('Please give me your last name: ')
    if last == 'q':
        break

    formatted_name = get_formatted_name(first, last)
    print(f'Neatly formatted name: {formatted_name}.')