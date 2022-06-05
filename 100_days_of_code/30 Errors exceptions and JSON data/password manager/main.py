# file copied from the previous day
# storing data in .json instead of .txt
# added search funcionality and error handling


from tkinter import *  # stay aware of bad practice importing everything *
from tkinter import messagebox
import random
import string
import json


def password_generator():
    """generates the 15 character password from the ASCII list of characters"""

    password_entry.delete(0, END)  # clear the entry field
    # store all characters under the single variable of string type
    ascii_characters = string.ascii_letters + string.digits + string.punctuation
    characters_list = [x for x in ascii_characters]

    # shuffle list values to make them more 'random'
    random.shuffle(characters_list)

    password = []
    for _ in range(15):
        random_character = random.choice(characters_list)
        password.append(random_character)

    random.shuffle(password)
    password = ''.join(password)

    # display password in the GUI
    password_entry.insert(0, password)


def find_password():
    """search for password entries in data.json
    search the file for key in the website entry field"""

    website = website_entry.get()  # search for key in website_entry

    try:
        with open('data.json', mode='r') as datafile:
            loaded_data = json.load(datafile)  # dict. type
    except FileNotFoundError:
        messagebox.showwarning(title='warning', message='No data file found')
    else:
        if website in loaded_data:
            username = loaded_data[website]['username']
            password = loaded_data[website]['password']
            messagebox.showinfo(title=website,
                                message=f'Email: {username} Password: {password}')
        else:
            messagebox.showinfo(title='Results', message='No details found')


def save():
    """save unsecured passwords to .json file"""
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "username": username,
            "password": password,
        }}

    # check for empty entries, show warning
    if len(website) == 0 or len(password) == 0:
        messagebox.showwarning(title='warning', message='Some of your inputs are empty')
    else:
        # tkinter's standard dialog, messagebox
        is_ok = messagebox.askyesno(title=website, message=f'These are the details entered:\
                                                            Username: {username}\
                                                            Password: {password}\
                                                            \nIs it ok to save?')

        if is_ok:  # user clicks "yes" on messagebox.askyesno popup
            try:
                # read data from data.json file
                with open('data.json', mode='r') as datafile:
                    loaded_data = json.load(datafile)
            except FileNotFoundError:
                # write new file and dump new_data
                with open('data.json', mode='w') as datafile:
                    json.dump(new_data, datafile, indent=4)
            else:
                # update loaded_data with new_data
                loaded_data.update(new_data)
                # write updated data to file
                with open('data.json', mode='w') as datafile:
                    json.dump(loaded_data, datafile, indent=4)
            finally:
                    # clear the entry fields
                    website_entry.delete(0, END)
                    password_entry.delete(0, END)


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

username_label = Label(text='Username:')
username_label.grid(column=0, row=2)

password_label = Label(text='Password:')
password_label.grid(column=0, row=3)

# Entries
website_entry = Entry(width=20)
website_entry.focus()  # focus on entry field after app launch
website_entry.grid(column=1, row=1, columnspan=1)

username_entry = Entry(width=37)
username_entry.insert(0, 'default@email.com')  # insert string at position 0
username_entry.grid(column=1, row=2, columnspan=2)

password_entry = Entry(width=20)
password_entry.grid(column=1, row=3, columnspan=1)

# Buttons
generate_button = Button(text='Generate Password', command=password_generator)
generate_button.grid(column=2, row=3)

add_button = Button(text='Add', width=35, command=save)
add_button.grid(column=1, row=4, columnspan=2)

search_button = Button(text='Search', width=14, command=find_password)
search_button.grid(column=2, row=1, rowspan=1)

window.mainloop()

#modules: tkinter, string, random, json
#tags: password, gui, json, dump(), load(), update(), i/o stream, error, exception
