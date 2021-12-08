# Ordinal numbers indicate their position in a list
# Such as 1st or 2nd.
# Most ordinal numbers end in th except 1, 2 and 3
# Store numbers 1 through 9 in a list
# Loop through list
# Use an if-elif-else chain inside the loop to print the proper ordinal ending for each
# Your output should read: 1st, 2nd, 3rd, 4th, 5th, 6th, 7th, 8th, 9th
# With each result on a separate line

numbers = [i for i in range(1, 10)]  # List comprehension

for x in numbers:
    if x == 1:
        print('1st')
    elif x == 2:     # probaj umjesto elif staviti if
        print('2nd')
    elif x == 3:     # probaj umjesto elif staviti if
        print('3rd')
    else:
        print(x, 'th', sep='')

#tags: list, comprehension, if, elif, else