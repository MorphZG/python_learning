#Scientific Computing with Python
##Python for Everybody
###Dictionaries and Loops

# Find most common word in a file

# <!--- this part is copied from exercise 9
fname = input('enter file name: ')
# default file if input blank:
if len(fname) < 1 : fname = 'dummy_short.txt' 
hand = open(fname)

di = dict()
# go through all lines and strip white space (extract words)
for lin in hand:
    lin = lin.rstrip()
    wds = lin.split()
    for w in wds:
        # idiom: retrieve/create/update counter
        di[w] = di.get(w,0) + 1           
#print(di)
# <!--- end

tmp = list()
for k,v in di.items():
    newt = (v,k)
    tmp.append(newt)

#print('Flipped', tmp)

tmp = sorted(tmp, reverse=True) # can sort by key or value, which ever comes first (thats why we flipped v,k)
#print('Sorted', tmp[:5])

for v,k in tmp[:5]:
    print(k,v)