# Clean up the code from exercise6-3 by replacing your series of print() calls
# with a loop that runs through the dictionary keys and values.
# When you are sure that loop works add five more Python terms to your glossary.
# New words and meanings should automaticaly be included in the output

# ------------ OVO JE STARI KOD IZ 6-3
glossary = {
    'argument': 'A value passed to a function. Keyword argument or positional argument',
    'list comprehension': 'A compact way to process elements in a sequence and return a list with the results',
    'method': 'A function called on an object, defined inside class body. See "function"',
    'object': 'Any data with state and defined behavior. Also the ultimate base class of any new-style class.',
    'package': 'A Python module which can contain submodules or recursively, subpackages. Technically, a package is a Python module with an __path__ attribute.',
}
# --------------- KRAJ !

# !-- Rjesenje zadatka. Treba samo dodati jos 2 itema u glossary{}
for k, v in glossary.items():
    print(f'{k}:\n\t{v}\n')  # \n oznacuje novi red, \t oznacuje tab space
