#Python for everybody
#www.py4e.com
#exercise 08
#https://www.youtube.com/watch?v=-9TfJF2dwHI

#  DEBUGGING

han = open('dummy_short.txt')

for line in han:
    line = line.rstrip()
    #print('Line', line) #3.Adding print lines to isolate traceback part
    wds = line.split()
    #print('Words: ', wds) #1.Added 'Words' before traceback
    #guardian part:
    if len(wds) < 1: #!solution (line was empty so indexing was out of range)
        continue #!solution

    if wds[0] != 'From': #0 Traceback line
        #print('Ignore') #2.Added Ignore after traceback
        continue
    print(wds[2])
