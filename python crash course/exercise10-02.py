# Chapter 10, Files and exceptions
# Solutions:
# https://ehmatthes.github.io/pcc_2e/solutions/solutions/

''' Learning C
Read in each line from the file you just created, learning_python.txt, and
replace the word Python with the name of another language, such as C.
Print each modified line to the screen.
'''

file = 'dump_files/learning_python.txt'

# when calling open() function you can add second argument after file name
# 'r'(default) for read
# 'w' write
# 'a' append
# 'r+' read and write

# help(open) will print info about open function

# open file as object and read()
with open(file) as file_object:
    content = file_object.read()

# print the content replacing Python with C
print(content.replace('Python', 'C'))


#   <! --- AUTOROVO RJESENJE

'''
filename = 'dump_files/learning_python.txt'

with open(filename) as f:
    lines = f.readlines()

for line in lines:
    # Get rid of newline, then replace Python with C.
    line = line.rstrip()
    print(line.replace('Python', 'C'))
'''

#tags: files, with, open(), read(), readlines(), replace(), i/o stream