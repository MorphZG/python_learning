**day 29**

## Password manager GUI app with Tkinter

### Passwords are bullshit

Passwords are bullshit, that is the title of blog post writen by Jeff Atwood.  
Main idea is that most passwords are either very unsecure, easy to remeber but  
also very easy to crack or they are hard to remember but still easy to crack.  
Passwords with 10 characters, at least one upper or lowercase letter, one number  
and at least one special character can be broken in less than 3 days. Example is  
`Tr0ub4dor&3` - password that is easy to crack but hard to remember but most of us  
will consider it to be a good password. On the other side passwords with more  
characters like four random words `correct horse battery staple` can be easy to  
remember and much harder to crack. Problem is that most websites will not accept  
such password with no number and no special characters.

You can read the blog post here: [codinghorror "passwords are bullshit"](https://blog.codinghorror.com/password-rules-are-bullshit)

### UI grid setup, canvas and other widgets

First things first. Create the main window, Canvas and PhotoImage widgets that will  
hold the image on the screen. `PhotoImage(file)` is a widget that holds the image  
file while `Canvas(**kwargs)` holds different graphical elements and will display  
image loaded by `PhotoImage()`.

After initializing buttons, labels and entry fields i will setup the grid but this  
time i will include columnspan parameter that can stretch single widget across two  
or more columns `widget.grid(columnspan=2)`.

### Saving the passwords

Passwords will be saved in a simple .txt file. Ofcourse without encryption and  
zero security measures this is not a viable option for storing the passwords.  
I will define `save()` and pass it as a command argument for "Add" button. When you  
press the button, `save()` will capture the data from the entry fields, append it  
to `data.txt` and clear the entry fields. Two builtin methods i need are `entry.get()`  
and `entry.delete(start, end)`.

Standard dialogs, tkinter's system for different types of popup messages. One of  
popular standard dialogs are "message boxes". I will create one inside `save()`  
function. Some of the available message boxes are:

```
messagebox.showinfo()
messagebox.showwarning()
messagebox.askquestion()
messagebox.askyesno()
messagebox.askokcancel()
messagebox.askretrycancel()
```
I have created `messagebox.askyesno()` that will display all the details user have  
entered. User can than verify the info and click yes to save the data or no to  
dismiss everything. The function returns boolean True or False after user clicks  
Yes or No. I will assign that value to a variable `is_ok`. If `is_ok` is True than 
open `data.txt` and append the data there.

I should implement another feature that will check all entries and warn the user  
any of the entry fields is empty. Simply check `if len() == 0` than run  
`messagebox.showwarning()`

### Password generator

Now is time to add funcionality to "Generate password" button. I already built  
simple password manager in another exercise, so to find it i just have to grep  
thorugh directories.  

Open terminal, cd in to repository root folder and type:
`$ grep -rnB1 "#tags.*password"`
If you never used grep, it is a search tool that uses regular expressions to find  
string patterns inside files. -rnB1 are options i use:
- r (recursive search)
- n (shows line number)
- B1 (also prints the previous line,)
- "#tags.*password" (this is the actual patter i am looking for)

The result of grep search returned two files. One of them is file i am currently  
working on because at the bottom i have included `#tags: password` and the second  
file is under `python_learning/exercise/password_generator.py` and that is the one  
i will modify and use again in this project. Instructor wants me to use code from  
this course but it was very early, around day 5 or 6 so it is really very basic and  
i found my own solution better.  

It is always strange to revisit older projects and see how different i was thinking  
about code. I like to document and comment my code, as you can see from these  
readme files so understanding the older code was actualy really easy. I had to  
take and modify only one small part of that older password generator. Remove some  
unneccesary features and add simple corrections. I had to remove the option to  
select the password lenght and complexity. There is only one option now. When you  
press the "Generate password" button it will generate 15 character string with  
ASCII letters, digits and punctation symbols. If i ever revisit this project in  
future i could add many improvements.



#tags: readme,
