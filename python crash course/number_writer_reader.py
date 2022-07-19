# page 203.
# Using json.dump() and json.load()

import json

# list of numbers we would like to store
numbers = [1, 2, 3, 4, 5, 6, 7]

filename = 'dump_files/numbers.json'

#   <! --- NUMBER WRITER
# open the filename for write
# dump() takes 2 arguments
# first is data to store and second is file object it can use
with open(filename, 'w') as f:
    json.dump(numbers, f)

#   <! --- NUMBER READER
# open the filename for read
# json.load() will load the data from file back to program memory
# store it to variable numbers
with open(filename) as f:
    numbers = json.load(f)

print(numbers)

#modules: json
#tags: files, i/o stream, json,