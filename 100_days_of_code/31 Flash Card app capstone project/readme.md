**day 31**

## Fash card app, Capstone project

### Introduction

Learning a new language is not easy. Chinese for example have around 50k characters,  
each have a different meaning and different pronounciation. But average profesor  
who is very eloquent and can talk with ease only knows around 10k characters while  
average person knows around 8k. You can get well with even 3k words in your day  
to day life. Of course, those 3k words are not just any random words. To learn  
the right words you need a frequency list with most frequent words.  

This is the capstone project where i complete the project without instructor's  
help. It will round up the knowledge i got so far. Goal is to build a Flash card  
app that will show the word on a foreign language while user is trying to guess  
the meaning and learn the language along the way.

There is a wiki page with frequency list for most common languages. Words are taken  
from the subtitles of popular movies and TV shows. Instructor have already provided  
the .csv file with 5k French words but i would to have my own list so copied the  
top 5k English words that i will be translating to Croatian. Paste English words     
in to google sheets and translate them to Croatian by using the following formula  
`=GOOGLETRANSLATE(text,[source language],[target language])`. If translating from  
English to Croatian it looks like `=GOOGLETRANSLATE(A1,"en","hr")`.

### Create the GUI with tkinter

Instructor provided the starting files and set of instructions for building the GUI.  
I got csv file with list of French and English words and images for buttons and cards.  
I have created my own csv file with English and Croatian words, promoting Croatian.   

After downloading the starting files can create the buttons with images:
```
my_image = PhotoImage(file='path/to/image.png')
button = Button(image=my_image, highlightthickness=0)
```
- Window must have x and y padding of 50.
- Window is split into 2 by 2 grid.
- Canvas must take 2 columns
- Canvas width is 800, height 526.
- Canvas will hold the card image and 2 pieces of text.
- First text piece is at x=400, y=150, Ariel size 40, italic.
- Second text piece is at x=400, y=263, Ariel size 60, bold.

### Create new flash cards

- Read the data from the french_words.csv file in the data folder.
- Pick a random french word/translation and put the word into the flashcard. Every  
  time you press ❌ or ✅ buttons, it should generate a new random word to display.
- You'll need to use pandas to access the csv file and generate a dataframe. To get  
  all the words/translation rows out as a list of dictionaries e.g.  
  `[{french1:english1}, {french2:english2}, {french3:english3}]`
  
  You could use: `DataFrame.to_dict(orient='records')`  
  `orient` parameter sets the display format.  
  Documentation [Link](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_dict.html) 

### Flip the cards

- After a delay of 3s(3000ms), the card should flip and display the English  
  translation of the current word.
- The card image should change to the card_back.png and the text should change  
  to white. The title of the card should change to 'English' from 'French'
- To change the canvas image, you'll need a reference to the image, like what  
  you have with the text created in the canvas. Then you can set the image  
  attribute using `itemconfig()`
```
new_image = PhotoImage(file="new_image.png")
old_image = PhotoImage(file="old_image.png")
canvas_image = canvas.create_image(300, 300, image=old_image)
#To change the image:
canvas.itemconfig(canvas_image, image=new_image)
```
NOTE: **PhotoImage objects should not be created inside a function.**

- To change the color of the text in a canvas element, use the `fill` parameter
- Remember in the `mainloop()` you should **not** create additional delayed loops  
  with `time.sleep()` but instead, use `window.after()`
- You can cancel a `window.after()` loop using `window.after_cancel()`

Documentation [Link](https://tcl.tk/man/tcl8.6/TclCmd/after.htm)

### Save your progress

- When the user presses on the ✅ button, it means that they know the current  
  word on the flashcard and that word should be removed from the list of words  
  that might come up.
- The updated data should be saved to a new file called words_to_learn.csv
- The next time the program is run, it should check if there is a words_to_learn.csv  
  file. If it exists, the program should use those words to put on the flashcards.  
  If the words_to_learn.csv does not exist (the first time program is run), then  
  it should use the words in the french_words.csv
  
  We want our flashcard program to only test us on the things we don't know. So  
  if the user presses the ✅ button, that means the current card should not come  
  up again.
  
- The `remove()` method can remove elements from a list: [Link](https://www.w3schools.com/python/ref_list_remove.asp)
- You can create a new csv file from a dictionary using `DataFrame.to_csv()`: [Link](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_csv.html)
- If you don't want to create an index for the new csv, you can set the `index`  
  parameter to `False` like this: `data.to_csv('filename.csv', index=False)`

  
%% How to build frequency dictionary
%% https://en.wiktionary.org/wiki/Wiktionary:Frequency_lists  
%% copy words and paste them in to google sheets, all in single column  
%% to get the translation of word in A2, select B2 and type =GOOGLETRANSLATE(A2,"hr","en")  
%% there is documentation for the formula  

#tags: readme,
