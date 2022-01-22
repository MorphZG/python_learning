import pprint


message = 'tajna poruka, brojimo slova i slazemo dictionary'
count = {}

for char in message:
    count.setdefault(char, 0)
    count[char] +=1
print(pprint.pformat(count))

#modules: pprint
#tags: