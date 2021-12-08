# Chapter 10, Files and exceptions
# Solutions:
# https://ehmatthes.github.io/pcc_2e/solutions/solutions/

''' Silent Cats and Dogs
Modify your except block in 10-8 to fail silently if either file is missing.
'''

print('''
    I will try to open and read two files.
    In case one of the files is missing i will fail silently.
    ''')

cats_file = 'dump_files/cats.txt'
dogs_file = 'dump_files/dogs.txt'

list_of_files = [cats_file, dogs_file]

for file in list_of_files:
    try:
        with open(file) as f:
            names = f.read()
    except FileNotFoundError:
        pass
    else:    
        print(f'\n\tReading the file {file}')
        print(names)


#tags: files, exception, error, open(), read(), for loop, i/o stream, dogs.txt, cats.txt