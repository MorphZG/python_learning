# Instructions for every exercise are listed inside readme.md file
# requires pandas and random library

# <! --- exercise 01
print('\n==== exercise 01 ==== ')
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# build list of squared numbers from the list of numbers
# squared number is multiplied by itself
squared_numbers = [num*num for num in numbers]
print(f'list of squared numbers: {squared_numbers}')
# < --- end


# <! --- exercise 02
print('\n==== exercise 02 ==== ')
# read readme.md for instructions
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# build list of even numbers from the list of numbers
result = [num for num in numbers if num % 2 == 0]
print(f'filtered list of even numbers: {result}')
# < --- end


# <! --- exercise 03
print('\n==== exercise 03 ==== ')
with open('./file1.txt') as f1:
    content1 = f1.readlines()  # list of string items

with open('./file2.txt') as f2:
    content2 = f2.readlines()  # list of string items

result = [int(num) for num in content1 if num in content2]  # convert to int
print(f'common integers in both files: {result}')
# < --- end

# <! --- exercise 04
print('\n==== exercise 04 ==== ')
from random import randint

list_of_names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
# looping through list_of_names, assign each name a value
students_score = {student: randint(1, 100) for student in list_of_names}
print(students_score)
# loop through previous dictionary, add condition
passed_students = {student: score for (student, score) in students_score.items() if score > 60}
print(passed_students)
# < --- end

# <! --- exercise 05
print('\n==== exercise 05 ==== ')
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
words = sentence.split()
print(f'This is the list of words in a sentence:\n{words}')

print('\nThis is the dictionary with word as a key and len(word) as a value')
result = {word: len(word) for word in words}
print(result)
# < --- end

# <! --- exercise 06
print('\n==== exercise 06 ==== ')

# temperatures in celsius degrees
weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}
print(f'Temperatures in celsius degrees:\n{weather_c}')

# conversion formula: (temp_c * 9/5) + 32
weather_f = {day: (temp_c * 9/5) + 32 for (day, temp_c) in weather_c.items()}
print(f'\nTemperatures in fahrenheit degrees:\n{weather_f}')
# < --- end

# <! --- exercise 07
print('\n==== exercise 07 ==== ')
import pandas

student_dict = {
    'student': ['Angela', 'Ana', 'James'],
    'score': [56, 99, 70]
}

student_dataframe = pandas.DataFrame(student_dict)

# loop through rows of a data frame
for index, row in student_dataframe.iterrows():
    # access index and row
    # access by attribute: row.student or row.score
    # access by key: row['student'] or row['score']
    pass

print('\n==== here is the first loop ==== ')
for index, row in student_dataframe.iterrows():
    print(f'This is row {index}: ')
    print(row)
    print('-------------')

print('\n==== here is the second loop ==== ')
for index, row in student_dataframe.iterrows():
    print(f'These are only the scores:')
    print(row['score'])

print('\n==== here is the third loop ==== ')
for index, row in student_dataframe.iterrows():
    print(f'These are only the students:')
    print(row['student'])

#modules: pandas, random
#tags: list, dictionary, *comprehension, dataframe, iterrows()
