# Cubes
# A number raised to a third power is called a cube.
# The cube of 2 is written as 2**3 in Python.
# Make a list of first 10 cubes (cube of integers from 1 thorugh 10)
# Use a for loop to print each cube
# Use a list comprehension to generate list of first 10 cubes.

cubes = [value**3 for value in range(1, 11)] # list comprehension
print(cubes)

for cube in cubes:
    print(cube)


#tags: list, comprehension, range()