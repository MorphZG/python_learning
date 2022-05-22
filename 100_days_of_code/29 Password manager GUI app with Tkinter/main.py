from tkinter import *  # stay aware of bad practice importing everything *
from tkinter import messagebox
import random
import string

# ---------------------------- PASSWORD GENERATOR -------------------------- #

def password_generator():
    """generates the 15 character password from the ASCII list of characters"""

    password_entry.delete(0, END)  # clear the entry field
    # store all characters under the single variable of string type
    password_characters = string.ascii_letters + string.digits + string.punctuation
    characters_list = [x for x in password_characters]

    # shuffle list values to make them more 'random'
    random.shuffle(characters_list)

    # initialize the empty list to store final password
    password = []

    # loop through shuffled list of characters and append to
    # empty list until we hit the desired lenght
    for _ in range(15):
        random_character = random.choice(characters_list)
        password.append(random_character)

    # we have generated the password but shuffle again
    random.shuffle(password)
    password = ''.join(password)

    # display password in the GUI
    password_entry.insert(0, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    """save unsecured passwords to .txt file"""
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()

    # check for empty entries, show warning
    if len(website) == 0 or len(password) == 0:
        messagebox.showwarning(title='warning', message='Some of your inputs are empty')
    else:
        # tkinter's standard dialog, messagebox
        is_ok = messagebox.askyesno(title=website, message=f'These are the details entered:\
                                                            Username: {username}\
                                                            Password: {password}\
                                                            \nIs it ok to save?')
        if is_ok:  # if user clicks "yes" on messagebox.askyesno popup
            # append data to data.txt
            with open('data.txt', mode='a') as datafile:
                datafile.write(f'{website} | {username} | {password}\n')
                # clear the entry fields
                website_entry.delete(0, END)
                password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------------ #

window = Tk()
window.title('Password Manager')
window.config(padx=20, pady=20)

# Canvas and PhotoImage
logo_img = PhotoImage(file='logo.png')
canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=logo_img)  # x position, y position, image
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text='Website:')
website_label.grid(column=0, row=1)

username_label = Label(text='Email/Username:')
username_label.grid(column=0, row=2)

password_label = Label(text='Password:')
password_label.grid(column=0, row=3)

# Entries
website_entry = Entry(width=35)
website_entry.focus()  # focus on entry field after app launch
website_entry.grid(column=1, row=1, columnspan=2)

username_entry = Entry(width=35)
username_entry.insert(0, 'default@email.com')  # insert string at position 0
username_entry.grid(column=1, row=2, columnspan=2)

password_entry = Entry(width=20)
password_entry.grid(column=1, row=3, columnspan=1)

# Buttons
generate_button = Button(text='Generate Password', command=password_generator)
generate_button.grid(column=2, row=3)

add_button = Button(text='Add', width=35, command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()

#modules: tkinter, string, random
#tags: password, gui, columnspan, grid(), get(), delete(), dialog, popup, messagebox
