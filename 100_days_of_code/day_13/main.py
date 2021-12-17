
# <! --- Describe Problem

# fix indentation problems
# range(1, 20) will go to numbers between 1 and 20 but not including 20
# you should set the range to be range(1, 21) or just add +1 
def my_function():
    for i in range(1, 20+1):
        if i == 20:
            print("You got it")

my_function()


# <! --- Reproduce the Bug

# list index goes out of range sometimes, depending on randint() selection
# first try to reproduce the bug so it always outputs the same error
# randint(a, b) returns numbers from a to b, including both ends
# next, fix the error so it never goes out of range
from random import randint
dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(0, 5)
print(dice_imgs[dice_num])


# <! --- Play Computer

# if you input border years, 1980, 1994 than nothing happens
# must improve comparison operators
year = int(input("What's your year of birth?"))
if year >= 1980 and year < 1994:
    print("You are a millenial.")
elif year >= 1994:
    print("You are a Gen Z.")


# <! --- Fix the Errors

# input() returns the string type so comparison with numbers ">" doesnt work.
# print() doesnt recognize variable {age}, must add f"" to make it formated
age = int(input("How old are you?"))
if age > 18:
    print(f"You can drive at age {age}.")


# <! --- Print is Your Friend
# use print() to check the value of the variables
#print(f'test --- pages:{pages}, word_per_page:{word_per_page}')
# when you input() word_per_page the number is not stored because there is
# double == comparison operator instead of = to asign variable value
pages = 0
word_per_page = 0
#print(f'test --- pages:{pages}, word_per_page:{word_per_page}')
pages = int(input("Number of pages: "))
word_per_page = int(input("Number of words per page: "))
#print(f'test --- pages:{pages}, word_per_page:{word_per_page}')
total_words = pages * word_per_page
print(total_words)


# <! --- Use a Debugger

# statement: b_list.append(new_item) is not indented inside loop
# so variable new_item get only last value after loop is complete
def mutate(a_list):
    b_list = []
    for item in a_list:
        new_item = item * 2
        b_list.append(new_item)
    print(b_list)
mutate([1, 2, 3, 5, 8, 13])


#tags: debug, (describe reproduce fix error)