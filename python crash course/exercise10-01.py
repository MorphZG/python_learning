# Chapter 10, Files and exceptions
# Solutions:
# https://ehmatthes.github.io/pcc_2e/solutions/solutions/

''' Learning Python
Open a blank file in your text editor and write a few lines summarizing
what you've learned about Python so far. Start each line with the phrase
In Python you can...
Save the file as learning_python.txt in the same directory as your exercises
from this chapter. Write a program that reads the file and prints what
you wrote three times. Print the contents once by reading in the entire file,
once by looping over the file object, and once by storing the lines in a list
and then working with them outside the with block.
'''

file = 'dump_files/learning_python.txt'

# when calling open() function you can add second argument after file name
# 'r'(default) for read
# 'w' write
# 'a' append
# 'r+' read and write

# help(open) will print info about open function


# --- read the entire file
print('.read() will read the entire file at once\n')
with open(file) as file_object:
    full_content = file_object.read()
    print(full_content)


# --- loop over file object and print
print('for loop inside with block will print line by line\n')
with open(file) as file_object:
    for line in file_object:
        print(line.rstrip())


# --- store the lines in a list and work with them outside of with block
print('''
.readlines() will create list with every line as a single list item.
I store that list under list_of_lines and than print each item with for loop
''')
with open(file) as file_object:
    list_of_lines = file_object.readlines()

for line in list_of_lines:
    print(line.rstrip())

#tags: files, with, open(), read(), readlines(), for loop, i/o stream