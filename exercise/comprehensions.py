'''
List Comprehensions
https://www.practicepython.org/exercise/2014/03/19/07-list-comprehensions.html

Exercise 7
Let’s say I give you a list saved in a variable:
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
Write one line of Python that takes this list a and makes a new list
that has only the even elements of this list in it.
'''

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
evens = [number for number in a if number % 2 == 0]
print(evens)

'''
List comprehensions

The idea of a list comprehension is to make code more compact to accomplish
tasks involving lists. Take for example this code:

  years_of_birth = [1990, 1991, 1990, 1990, 1992, 1991]
  ages = []
  for year in years_of_birth: 
    ages.append(2014 - year)

And at the end, the variable ages has the list [24, 23, 24, 24, 22, 23].
What this code did was translate the years of birth into ages, and it took
us a for loop and an append statement to a new list to do that.

Compare to this piece of code:

  years_of_birth = [1990, 1991, 1990, 1990, 1992, 1991]
  ages = [2014 - year for year in years_of_birth]

The second line here - the line with ages is a list comprehension.

It accomplishes the same thing as the first code sample - at the end,
the ages variable has a list containing [24, 23, 24, 24, 22, 23],
the ages corresponding to all the birthdates.

The idea of the list comprehension is to condense the for loop and the list
appending into one simple line. Notice that the for loop just shifted to
the end of the list comprehension, and the part before the for keyword is the
thing to append to the end of the new list.

You can also embed if statements into the list comprehension.
check out this reference to help you out:
https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions

There are many examples and a better explanation than I can ever give.

'''

# List Comprehension can be used to avail the list of indices of all
# the occurrences of a particular element in a List.

#  syntax formula !!!!
#   [expression for element in iterator if condition]
lista = [10, 20, 30, 10, 50, 10, 45, 10]
# get index numbers of elements equal to 10
res = [x for x in range(len(lista)) if lista[x] == 10]
print(res)



#tags: list comprehension,
