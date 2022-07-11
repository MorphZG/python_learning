"""
English words to learn.
Reads the file with 5k English words and Croatian translation.
Display the tkinter GUI with one of the English words, if user knows the word,
program will remove it from the list and save as remaining-english-words.csv
"""

import pandas as pd
from tkinter import *
from random import choice


BACKGROUND_COLOR = "#B1DDC6"
current_card = {}  # single pair {'English':'word', 'Croatian':'rijec'}
words_to_learn = {}

try:
    dataframe = pd.read_csv('data/remaining-english-words.csv')  # read csv file as dataframe
except FileNotFoundError:
    dataframe = pd.read_csv('data/english-words.csv')
finally:
    words_to_learn = dataframe.to_dict(orient='records')  # dataframe -> dictionary


def new_word():
    """display new English word on card_front_img"""
    global current_card, flip_timer
    window.after_cancel(flip_timer)  # reset the timer
    current_card = choice(words_to_learn)
    canvas.itemconfig(canvas_title, text='English', fill='black')  # itemconfig(item_id=canvas_title)
    canvas.itemconfig(canvas_word, text=current_card['English'], fill='black')  # itemconfig(item_id=canvas_word)
    canvas.itemconfig(canvas_image, image=card_front_img)
    flip_timer = window.after(3000, flip_card)  # flip_card after 3s
    print(len(words_to_learn))  # prints the lenght of remaining words to learn


def flip_card():
    """change canvas to display translation and background of card image"""
    canvas.itemconfig(canvas_title, text='Croatian', fill='white')
    canvas.itemconfig(canvas_word, text=current_card['Croatian'], fill='white')
    canvas.itemconfig(canvas_image, image=card_back_img)


def known_word():
    """remove current word from words_to_learn and save to new csv file"""
    words_to_learn.remove(current_card)
    dataframe = pd.DataFrame(words_to_learn)
    dataframe.to_csv('data/remaining-english-words.csv', index=False)
    new_word()


window = Tk()
window.title('Flashy')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, flip_card)  # flip card after 3s

# canvas
# when placing text or image on canvas you must provide position
# IndexError: tuple index out of range
card_front_img = PhotoImage(file='images/card_front.png')
card_back_img = PhotoImage(file='images/card_back.png')
canvas = Canvas(width=800, height=526, highlightthickness=0)
canvas_image = canvas.create_image(400, 263, image=card_front_img)  # x, y relative to canvas width, hight
canvas_title = canvas.create_text(400, 150, text='Title', font=('Ariel', 40, 'italic'))  # canvas_title will be used as itemid
canvas_word = canvas.create_text(400, 263, text='Word', font=('Ariel', 60, 'bold'))  # canvas_word will be used as itemid
canvas.config(bg=BACKGROUND_COLOR)
canvas.grid(row=0, column=0, columnspan=2)

# buttons
green_img = PhotoImage(file='images/right.png')
green_button = Button(image=green_img, highlightthickness=0, command=known_word)
green_button.grid(column=1, row=1)

red_img = PhotoImage(file='images/wrong.png')
red_button = Button(image=red_img, highlightthickness=0, command=new_word)
red_button.grid(column=0, row=1)

new_word()  # show the new word when program starts

window.mainloop()


#modules: tkinter, pandas
#tags: after(), after_cancel(), gui, itemconfig(), csv, file,
