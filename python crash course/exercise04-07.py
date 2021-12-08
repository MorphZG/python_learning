# Make a list of multiples of 3 from 3 to 30
# Use a for loop to print the numbers in list

multiples = [i*3 for i in range(0,11)] # list comprehension
print(multiples)

for number in multiples:
    print(number)

#tags: list, comprehension, range()