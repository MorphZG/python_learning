**day 26**
## List comprehension and NATO alphabet

### List comprehension
Learning about python unique feature, list and dictionary comprehension. We can  
use comprehension on any iterable object.  
Instructor starts the lesson wih basic comprehensions inside python console  
before moving on to main assignment with NATO alphabet. 

Instructor mentioned few simple syntax versions for comprehension, most valuable  
is probably the extended formula with condition or "test" included.
```
[expression for element in iterator if condition]

numbers_list = [2, 3, 4, 10, 12, 14, 13, 11, 9]
less_than_ten = [num for num in numbers_list if num < 10]
even_numbers = [num for num in numbers_list if num % 2 == 0]

list_of_names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
short_names = [name for name in list_of_names if len(name) < 5]
```
I should probably skip whole day_26 since i already know most of the content  
and would really like to move on to more advanced lessons.  
But why refuse a chance to confirm the knowledge, have fun with coding and  
complete the exercise.  

### exercise 01
Instructor points me to her replit page at:  
[replit.com/@appbrewery](https://replit.com/@appbrewery/day-26-1-exercise)
There is a readme.md file with instructions on how to complete the exercise.

**NOTE**
Code for every exercise will be in a file `exercise.py`

**Instructions**
You are going to write a list comprehension to create a new list called
"squared_numbers". This new list should contain every number in the list "numbers"
but each number should be squared.
```
e.g. 4 * 4 = 16
4 squared equals 16.
```
Do not modify the list `numbers` directly. Try to use list comprehension instead
of a loop.

Example Output
`[1, 1, 4, 9, 25, 64, 169, 441, 1156, 3025]`


### exercise 02
**Instructions**
You are going to write a List Comprehension to create a new list called result.  
This new list should only contain the even numbers from the list of numbers.  

DO NOT modify the List numbers directly. Try to use List Comprehension instead  

`numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]`

Example Output  
`[2, 8, 34]`


### exercise 03
**Instructions**  
Read file1.txt and file2.txt. They each contain a bunch of numbers, each number on a new line.
You are going to create a list called result which contains the numbers that are  
common in both files. 

IMPORTANT: The result should be a list that contains Integers, not Strings.  
Try to use List Comprehension instead of a Loop.  


### Apply comprehension to US States game
Instructor wants me to go back to previous assignment and modify the main file.  
By using list comprehension i could cut down the lenght of code by few lines.  
Since i want this whole projects to be clean as much as possible should probably  
copy that file in this folder but than i also have to copy the all the files  
that goes with it. To keep it simple i will just copy the main.py as without other  
files so it will not work if you try to run it but what i did with the code will  
clearly be visible. File copied as `modified day25.py`.


### Dictionary comprehension
Basic and advanced comprehension formula (syntax) for building dictionary:  
` new_dict = {new_key:new_value for item in list} `  
` new_dict = {new_key:new_value for (key,value) in dict.items()} `  
` new_dict = {new_key:new_value for (key,value) in dict.items() if condition} `  


### exercise 04
Take a list of names and some random scores. Use dictionary comprehension by  
looping through the list of names and assign them a random score.

Than build another dictionary but add a condition into it. Every student with  
a score higher than 60 will pass the test and be a part of `passed_students`


### exercise 05
**Instructions**
You are going to use Dictionary Comprehension to create a dictionary called  
`result` that takes each word in the given sentence and calculates the number  
of letters in each word.  

Try Googling to find out how to convert a sentence into a list of words.
 - Link to official documentation: [string.split()](https://docs.python.org/3/library/stdtypes.html#str.split)
Use Dictionary Comprehension instead of a Loop.  


### exercise 06
**Instructions**
You are going to use Dictionary Comprehension to create a dictionary called  
`weather_f` that takes each temperature in degrees Celsius and converts it into  
degrees Fahrenheit.  

To convert temp_c into temp_f:  
`(temp_c * 9/5) + 32 = temp_f`

Use Dictionary Comprehension instead of a Loop.


### How to iterate over Pandas dataframe
After building a simple dictionary with list of names and list of scores i will  
call `pandas.DataFrame()` to create small dataframe with two columns and few  
rows. I can loop through it just like i would with dictionary.  
```
for key, value in dataframe.items():
    print(key, value)
```
Pandas have inbuilt loop that allows looping through rows `dataframe.iterrows()`  
```
for index, row in dataframe.iterrows():
    print(index, row)
```
Each row in Dataframe is Series object so we can access any single value in a  
row by using `row.title` or `row["title"]`.   
For more details look at exercise07 at `exercise.py`


### Nato Alphabet
Instructor shares the starting files `main.py` with few basic lines of code and  
`nato_phonetic_alphabet.csv` with two columns, one with capital letters and  
other with code word. My task is to first build a dictionary from .csv file  
and than use keys to build a list of values depending on user input.

It is a short assignment but it made me think. Day 26 completed!  


#tags: readme,
