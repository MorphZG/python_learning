# Chapter 10, Files and exceptions
# Solutions:
# https://ehmatthes.github.io/pcc_2e/solutions/solutions/

''' Common Words
Visit Project Gutenberg (https://gutenberg.org/) and find a few texts you'd
like to analyze. Download the text files for these works, or copy the raw text
from your browser into a text file on your computer.

You can use the count() method to find out how many times a word or phrase
appears in a string. For example, the following code counts the number of
times 'row' appears in a string:

    line = "Row, row, row your boat"
    line.count('row')
    >>> 2
    line.lower().count('row')
    >>> 3

Notice that converting the string to lowercase using lower() catches all
appearances of the word you're looking for, regardless of how it's formatted.

Write a program that reads the files you founded at Project Gutenberg and
determines how many times the word 'the' appears in each text. This will be
an approximation because it will also count words such as 'then' and 'there'.
Try counting 'the ', with a space in the string, and see how much lower your
count is.
'''

# this program can be very simple:
filename = 'dump_files/moby_dick.txt'

# with open(filename) as f:
#     content = f.read()
#     print(content.lower().count('the '))


# but i will use custom function and exceptions
def count_words(filename, word):
    ''' returns number of words in a text file '''
    try:
        with open(filename) as f:
            content = f.read()
    except FileNotFoundError:
        pass
    else:
        count = content.lower().count(word)
        print(f'Number of "{word}" in a {filename} is {count}')

count_words(filename, 'the ')

#tags: exception, files, i/o stream, with, function