'''
https://pynative.com/python-basic-exercise-for-beginners/

Exercise 10: Given a two list of numbers create a new list such
that new list should contain only odd numbers from the first list
and even numbers from the second list

Expected output:

list1 =  [10, 20, 23, 11, 17]
list2 = [13, 43, 24, 36, 12]

result List is [23, 11, 17, 24, 36, 12]
'''

def mix_list(lista1, lista2):
    ''' take odd numbers from param1 and even numbers from param2 '''
    lista3 = []
    for num in lista1:
        if num %2 == 1:
            lista3.append(num)

    for num in lista2:
        if num %2 == 0:
            lista3.append(num)

    print(f'The result is: {lista3}')





first_list =  [10, 20, 23, 11, 17]
second_list = [13, 43, 24, 36, 12]

mix_list(first_list, second_list)

