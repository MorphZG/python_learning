'''
Reverse Word Order
Exercise 15
https://www.practicepython.org/exercise/2014/05/21/15-reverse-word-order.html

Write a program (using functions!) that asks the user for a long string
containing multiple words. Print back to the user the same string, except
with the words in backwards order. For example, say I type the string:

    My name is Michele

Then I would see the string:

    Michele is name My
'''

a = input('give me few words and i will mess up everything:\n>')
print('this is the string i need reversed:\n\t', a)


def revstr(a):
    ''' reverses the words in string a '''
    a = a.split()  # every word is split in to list
    a = a[::-1]
    a = ' '.join(a)
    return a


def reverse_v2(a):  # short "oneline" function
    return ' '.join(a.split()[::-1])


def reverse_v3(a):
    a = a.split()
    return " ".join(reversed(a))


def reverse_v4(a):
    a = a.split()
    a.reverse()
    return " ".join(a)


print(revstr(a))
print(reverse_v2(a))
print(reverse_v3(a))
print(reverse_v4(a))

'''
Python has a lot of interesting things you can do with strings. I will show
a few here, but you can see many more methods that may or may not be useful
at the official Python documentation about the string format.
https://docs.python.org/3.3/library/stdtypes.html?highlight=strings#string-methods

Remember that strings are lists:
https://www.practicepython.org/exercise/2014/03/12/06-string-lists.html

Splitting strings
You can “split” or tear apart strings based on a given set of characters.
For example:

    teststring = "this is a test"
    result = teststring.split("t")

And at the end, result will contain the list:

    ['', 'his is a ', 'es', '']

Instead of "t", you can write any character you want. If you do not include
any character, it means “split on all whitespace”:

    teststring = "  this      has a lot    of   spaces and    tabs"
    result = testring.split()

Then result contains:

    ['this', 'has', 'a', 'lot', 'of', 'spaces', 'and', 'tabs']

Joining strings
You can also relatively easily “join” or “smush” strings together:

    listofstrings = ['a', 'b', 'c']
    result = "**".join(listofstrings)

Then result will contain the string:

    a**b**c

Take a look at the official Python documentation for more information.
https://docs.python.org/3.3/library/stdtypes.html?highlight=strings#string-methodss
'''

#tags: function, string, reverse(), list, oneliner