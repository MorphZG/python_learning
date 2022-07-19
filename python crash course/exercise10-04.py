# Chapter 10, Files and exceptions
# Solutions:
# https://ehmatthes.github.io/pcc_2e/solutions/solutions/

'''Guest book
Write a while loop that prompts users for their name. When they enter their
name, print a greeting to the screen and add a line recording their visit in
a file called guest_book.txt. Make sure each entry appearson a new line in file.
'''

text_file = 'dump_files/guest_book.txt'
prompt = 'What is your name? '

# open file in append mode
with open(text_file, 'a') as file_object:
    ask = True  # flag, loop while True
    while ask:  # no need for flag, you can write while True:
        name = input(prompt)
        print(f'Hello {name.title()}! I will add your name to guest_book.txt')
        # write to file, as with print() you can format with (f'tekst')
        file_object.write(f'{name.title()}\n')
        # continue the loop if there is more users
        new_user = input('Is there any new users? yes/no ')
        if new_user == 'yes':
            continue  # continue statement goes back to start
                      # pass statement does nothing and moves to next line 
        else:  
            ask = False  # flag set to False, stop the loop
            break  # break out of loop, no need for flag


#   <! --- AUTOROVO RJESENJE

'''     
filename = 'guest_book.txt'

print("Enter 'quit' when you are finished.")
while True:
    name = input("\nWhat's your name? ")
    if name == 'quit':
        break
    else:
        with open(filename, 'a') as f:
            f.write(f"{name}\n")
        print(f"Hi {name}, you've been added to the guest book.")
'''

#tags: files, i/o stream, with, while loop, flag,