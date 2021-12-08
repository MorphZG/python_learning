# Think of five basic foods and store them in a tuple
# Use a for loop to print each food
# Try to modify one of them and make sure that Python rejects the change.
# Add the line that rewrites the tuple, change 2 items (overwrite the variable)
# Use a for loop to print each of the items in a revised tuple

foods = ('jabuka', 'kruh', 'lubenica', 'kruska', 'breskva')
print(type(foods))

print()
for item in foods:
    print(item)

foods = ('jaje', 'marelica', 'lubenica', 'kruska', 'breskva')

print()
for item in foods:
    print(item)