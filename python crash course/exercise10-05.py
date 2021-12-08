# Chapter 10, Files and exceptions
# Solutions:
# https://ehmatthes.github.io/pcc_2e/solutions/solutions/

'''Programming poll
Write a while loop that asks people why they like programming. Each time
someone enters a reason, add their reason to a file that stores all responses.
'''

file = 'dump_files/programming_poll.txt'

while True:
    print('\t\ntype "quit" to break')
    reason = input('Why do you like programming?')
    if reason == 'quit':
        break
    else:
        with open(file, 'a') as file_object:
            file_object.write(f'{reason}\n')


#   <! --- AUTOROVO RIJESENJE

'''
filename = 'dump_files/programming_poll.txt'

responses = []
while True:
    response = input("\nWhy do you like programming? ")
    responses.append(response)

    continue_poll = input("Would you like to let someone else respond? (y/n) ")
    if continue_poll != 'y':
        break

with open(filename, 'a') as f:
    for response in responses:
        f.write(f"{response}\n")
'''

#tags: files, i/o stream, with, while loop, flag, programming_poll.txt