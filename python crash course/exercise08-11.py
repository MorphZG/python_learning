'''Archived Messages
Start with your work from 8-10.
Call the function send_messages() with a copy of the list of messages.
After calling the function, print both of your lists to show that the original list has retained its messages.
'''

# kopija send funkcije iz prijasnje vjezbe
def send_messages(xlist, ylist):
    ''' move msgs from xlist to ylist '''
    while xlist:
        ylist.append(xlist.pop())

    return xlist, ylist

# lista sa porukama za slanje
list_messages = [
    'message me when you gone',
    'close the doors behind you',
    'you left while didnt try sarma', ]

sent_messages = []

# zovem funkciju ali kod unosa xliste dajem slice[:]
# na taj nacin koristim kopiju liste
send_messages(list_messages[:], sent_messages)

# obije liste su popunjene
print(f'\n\tthis is first list:\n{list_messages}')
print(f'ID: {id(list_messages)}')
print(f'\n\tthis is list of sent messages:\n{sent_messages}')
print(f'ID: {id(sent_messages)}')

#tags: function, list, append(), pop()