'''
https://www.practicepython.org/exercise/2014/02/15/03-list-less-than-ten.html
Exercise 3

Take a list, say for example this one:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

and write a program that prints out all the elements of the list
that are less than 5.

Extras:

    -Instead of printing the elements one by one,
    make a new list that has all the elements less than 5
    from this list in it and print out this new list.
    -Write this in one line of Python.
    -Ask the user for a number and return a list that contains
    only elements from the original list a that are smaller than
    that number given by the user.

'''

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
aa = []
for num in a:
    if num < 5:
        aa.append(num) # building a new list aa
print(aa)

# One liner
print('\nextra exercise number 2, do all above in one line of code: ')
print([aa for aa in a if aa < 5])

#tags: list comprehension

'''
RELATED TO:
exercise list_less_than_ten.py

A list comprehension behaves like this:
[output] for [item] in [list] if [filter]

As you can see there are 4 components in its syntax:
output, item, list and filter.

In the case of Sachin's code [aa for aa in a if aa < 5]:

output = aa
item = aa
list = a
filter = aa < 5

What this means is that I'm outputting the variable 'aa'
which refers to each item in the list (a).

Since 'aa' is set to refer to each item in list (a),
the output will print the items in list (a). However,
I also have a filter specified at the end of the code "if aa < 5".

This means that only the items in the list (referred to as aa)
that are below 5 are printed out.

It does help if you use labels that are more intuitive in your code.
For example instead of naming the list a, I can name the list "number_list":

number_list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

My list comprehension will go like this:

[number for number in number_list if number < 5]

You will get the same output.
'''