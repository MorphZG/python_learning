import random

messages = [
    'it is certain',
    'it is definitely',
    'reply hazy try again',
    'ask again later',
    'concetrate and ask again',
    'my reply is no',
    'outlook not so good',
    'very doubtful']

random_broj = messages[random.randint(0, len(messages) -1)]

print(random_broj)

'''
sa importanim random modulom za brojeve
dakle pozivamo se na random.randint da nam
izvrti random broj u listi messages[]
start random broj 0(prva vrijednost u listi)
kraj je len(messages) -1
znaci kraj ovisi o broju vrjednosti u listi
.randint(0, len(messages) - 1)
kao sto u .range(1,10) imamo start 1 i kraj 10
tako i .randint() starta od nula do len(messages) - 1
'''