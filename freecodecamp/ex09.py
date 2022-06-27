#Scientific Computing with Python
##Python for Everybody
###Dictionaries and Loops

# find most common word in file

fname = input('enter file name: ')
# default file if input blank:
if len(fname) < 1 : fname = 'dummy_short.txt'
hand = open(fname)

di = dict()
for lin in hand:
    lin = lin.rstrip()
    wds = lin.split()
    for w in wds:
        # idiom: retrieve/create/update counter
        di[w] = di.get(w,0) + 1
#print(di)

# now we want to find the most common word
largest = -1
theword = None
for k,v in di.items():
    if v > largest:
        largest = v
        theword = k #capture/remember the word that is largest
print(theword, largest)


