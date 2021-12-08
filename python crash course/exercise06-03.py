# Python dictionary can be used to model an actual dictionary.
# However, to avoid confusion, let's call it a glossary.
# Think of five programming words you've learned about in the previous chapters
# Use these words as the keys in your glossary, and store meanings as values
# Print each word and its meaning as neatly formatted output.
# You might print the word follwed by a colon and then its meaning
# Or print the word on one line and then print its meaning indented on a second line
# Use the new line character \n to insert a blank line between each word meaning pair in your output

glossary = {
    'argument': 'A value passed to a function. Keyword argument or positional argument',
    'list comprehension': 'A compact way to process elements in a sequence and return a list with the results',
    'method': 'A function called on an object, defined inside class body. See "function"',
    'object': 'Any data with state and defined behavior. Also the ultimate base class of any new-style class.',
    'package': 'A Python module which can contain submodules or recursively, subpackages. Technically, a package is a Python module with an __path__ attribute.',
}

# print(glossary.keys())
# print(glossary.values())
# print(glossary.items())
argument = glossary['argument']
list_comprehension = glossary['list comprehension']
method = glossary['method']
object = glossary['object']
package = glossary['package']

print(f'argument:\n    {argument}\n')
print(f'list_comprehension:\n    {list_comprehension}\n')
print(f'method:\n    {method}\n')
print(f'object:\n    {object}\n')
print(f'package:\n    {package}\n')


#tags: dictionary, items(), keys(), values(),