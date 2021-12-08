'''
List Overlap
https://www.practicepython.org/exercise/2014/03/05/05-list-overlap.html

Exercise 5

Take two lists, say for example these two:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

and write a program that returns a list that contains only the elements
that are common between the lists (without duplicates). Make sure your
program works on two lists of different sizes.

Extras:

    - Randomly generate two lists to test this
    - Write this in one line of Python
    (don’t worry if you can’t figure this out at this point)

'''

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = []

for number in a:
    if number in b:
        if number not in c:
            c.append(number)
print(c)

print()  # new line

# Oneliner is list converted to set, set() eliminates all duplicates
d = set([number for number in a if number in b])
print(d)

#tags: duplicate removal, set(), list, comprehension