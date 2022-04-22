**day 27**

## Tkinter, *args, **kwargs and GUI programs

### Optional args and kwargs

This lesson starts with optional arguments and functions with default values.  
Later instructor explains *args, function with *args parameter can take any  
number of arguments. The key is single asterix and not the word args which is  
only the naming convention. We can also use double asterix or **kwargs to input  
any number of keyword arguments.  

Interesting fact that i didnt know before. If i type check default type of *args  
we will get tuple but **kwargs are of dictionary type. So we can be creative  
and use them in different ways. We can access values by looking for a key just  
like in dictionaries `kwargs['key']` and than execute only that part of the  
function. I have a file named `exercise.py` where i experiment with code from  
the lesson.

### Tkinter

Tkinter is python interface to Tk. The opensource and cross-platform GUI toolkit  
for Tcl (scripting language) and many other programming languages. Drop a look  
at links below for more info. You can also find useful information inside python  
documentation since Tkinter is part of it's built-in library and comes together  
with python installation. It is very easy to learn and very well documented.  

Documentation links:  

- [tcl.tk](http://tcl.tk/man/)
- [tkdocs.com](https://tkdocs.com/)
- [python.org](https://docs.python.org/3/library/tk.html)

Basic building blocks of Tkinter are widgets. Button, label, entry, scale, text,  
listbox, spinbox, checkbutton... After creating a widget it must be placed on  
screen with one of the three available layout managers: pack, place or grid.

### Mile to kilometers converter

After learning about basics of Tkinter library and solving few small assignments  
along the way, instructor presents a small project. Mile to km converter. All  
widgets are positioned in a 3x3 grid, we have 4 labels, 1 entry and 1 button.  
First i have to position all the elements on the screen correctly using the grid.  
Than define a function that multiplies number typed in to entry field by 1.609  
and display the result as a label text when button is pressed.

This lesson was really simple and i could possibly expand upon it and add some  
more features for different conversions. I am eager to see what next lesson is  
all about so this little project will stay as is, maybe in future i will return  
and upgrade it.


#tags: readme
