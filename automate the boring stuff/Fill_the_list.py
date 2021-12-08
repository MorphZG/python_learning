catNames = []

while True:
    print("enter cat name " + str(len(catNames) +1))
    name = input()
    if name == "":
        break
    catNames = catNames + [name]

print("your cat names are:")
for name in catNames:
    print(name)