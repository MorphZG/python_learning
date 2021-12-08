'''Messages
Make a list containing a series of short text messages.
Pass the list to a function called show_messages() that prints each text msg
'''

from time import sleep

list_messages = [
    'message me when you gone',
    'close the doors behind you',
    'you left while didnt try sarma', ]


def show_messages(xlist):
    ''' prints msgs in a list '''
    print('i will print messages from your list')
    print('thanks for using me!')
    print('have a nice day\n')
    sleep(3)
    print('Loading... please wait')

    for msg in xlist:
        sleep(2)
        print(msg)

    sleep(1)
    print('All done !!')
    return xlist


show_messages(list_messages)

#modules: time
#tags: function, list