# Make a list of the numbers from one to one million
# Use min() and max() to make sure your list actually starts at 1 and ends at 1 million.
# Use sum() function to see how quickly python can add a million numbers.

numbers = []
for i in range(1, 1000001):
    numbers.append(i)

print('highest number is: ', max(numbers))
print('lowest number is: ', min(numbers))
print('\nsum of all numbers in list is: ')
print(sum(numbers))

#tags: list, for loop, range(), max(), min(), sum()