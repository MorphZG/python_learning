'''
Write a program that asks the user how many people are in their dinner group.
If the answer is more than eight, print they'll have to wait for the table.
Otherwise, report that their table is ready.
'''

question = 'How many people is in your group for dinner? '
answer = int(input(question))

if answer >= 8:
    report = 'You will have to wait for your table'
else:
    report = 'Your table is ready'
    
print(report)

'''
Autorova rjesenja:
https://ehmatthes.github.io/pcc_2e/solutions/solutions/
'''