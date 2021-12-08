'''
Simple character counting with dictionary and setdefault() method
which is very similar to get()
'''

message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1

print(count)



# Pretty print

import pprint

message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1

print('\n\n This is printed using pprint module: ')
pprint.pprint(count)


#tags: counting, get(), setdefault(), dictionary, method, pprint