lista1 = ['a', 'a', 'b', 'c', 'd', 'd']
lista2 = []

# Using simple for loop
# Add items if not in lista2
for i in lista1:
    if i not in lista2:
        lista2.append(i)

print(lista1)
print(lista2)

print(id(lista1))
print(id(lista2))

'''
Python 3 code to demonstrate 
removing duplicated from list 
using list comprehension
'''
lista3 = []
[lista3.append(x) for x in lista1 if x not in lista3]

lista4 = [x for x in lista1]

print(lista3)
print(id(lista3))

# if you have a list where ordering is not important you can convert to set()

lista5 = ['Marko', 'Marko', 'Zoran', 'Mirjana']
lista5 = set(lista5)
print(lista5)


#tags: remove duplicates, comprehension