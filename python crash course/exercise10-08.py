# Chapter 10, Files and exceptions
# Solutions:
# https://ehmatthes.github.io/pcc_2e/solutions/solutions/

''' Cats and dogs
Make two files, cats.txt and dogs.txt. Store at least three names of cats in
the first file and three names of dogs in the second file. Write a program
that tries to read these files and print the contents of the file to the
screen. Wrap your code in a try-except block to catch the FileNotFound error,
and print a friendly message if a file is missing. Move one of the files to a
different location on your system, and make sure the code in the except block
executes properly.
'''

print('''
    I will try to open and read two files, will catch the FileNotFoundError
    in case there is no such file on specified location
    ''')

cats_file = 'dump_files/cats.txt'
dogs_file = 'dump_files/dogs.txt'

list_of_files = [cats_file, dogs_file]

for file in list_of_files:
    print(f'\n\tReading the file {file}')
    try:
        with open(file) as f:
            names = f.read()
            print(names)
    except FileNotFoundError:
        print('Cannot find the specified file')


#tags: files, exception, error, open(), read(), for loop, i/o stream, dogs.txt, cats.txt