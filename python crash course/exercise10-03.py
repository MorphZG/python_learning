# Chapter 10, Files and exceptions
# Solutions:
# https://ehmatthes.github.io/pcc_2e/solutions/solutions/

'''Guest
Write a program that prompts the user for their name. When they respond,
write their name to a file called guest.txt
'''

text_file = 'dump_files/guest.txt'
prompt = 'What is your name? '
name = input(prompt)
with open(text_file, 'w') as file_object:
    file_object.write(name)


#tags: files, i/o stream, guest.txt