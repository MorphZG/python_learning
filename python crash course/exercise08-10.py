'''Sending Messages
Sart with a copy from 8-9.
Write a function called send_messages() that prints each text message
and moves each message to a new list called sent_messages as it's printed.
After calling a function, print both of your lists to make sure that messages were moved correctly.
'''

# bezveze ubacio sleep funkciju iz time modula
# cisto iz fore, output je zanimljiviji ako se pojavljuje u intervalima

from time import sleep

# setup liste poruka za slanje
list_messages = [
    'message me when you gone',
    'close the doors behind you',
    'you left while didnt try sarma', ]

# prazna lista poslanih poruka
sent_messages = []

# definiram show funkciju
def show_messages(xlist):
    ''' prints msgs in a xlist '''
    print('i will print messages from your list')
    print('thanks for using me!')
    print('have a nice day\n')
    sleep(3)
    print('Loading... please wait')

    for msg in xlist:
        sleep(2)
        print(msg)
    return xlist

# definiram send funkciju
def send_messages(xlist, ylist):
    ''' move msgs from xlist to ylist '''
    while xlist:
        ylist.append(xlist.pop())

    sleep(1)
    print('All done !!')
    return xlist, ylist


# pozivam show i send funkcije na 2 liste sa pocetka
show_messages(list_messages)
send_messages(list_messages, sent_messages)

# kontrola. poruke moraju biti prebacene iz jedne u drugu listu
sleep(3)
print('')
print(f'this is the original list with messages:\n\t', list_messages)
print(f'this is the new list with sent messages:\n\t', sent_messages)


'''
send_messages() koristi while loop umjesto for loop
while loop je bolji izbor kada moramo micati items iz liste
for loop ima problem jer prilikom brisanja itema, index se stalno mjenja    
'''

'''
Autorova rjesenja
https://ehmatthes.github.io/pcc_2e/solutions/chapter_8/
'''

#modules: time
#tags: function, list, append(), pop()