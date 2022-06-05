**day 30**

## Errors, exceptions and saving JSON data

### Introduction

Will revisit some older projects and trying to improve on them. Focusing on error  
handling, loading and saving data to .json file. 

Catching errors to prevent program failing is today's topic.  
Python have few keywords i will use:  

```
try:
    something that might cause an exception
except:
    do this if there was an exception
else:
    do this if there were no exceptions
finally:
    do this no matter what happens
    
```

Would be good to read more about specific  
error types from official documentation. Some of the errors i will work with:
**FileNotFound, KeyError, IndexError, TypeError**... It is also possible to  
raise your own exceptions and error messages with `raise` keyword.

### Exercise

After video introduction and explanation of error handling, instructor shares  
few exercises, "challanges" where i handle few different error types. Instructor  
provided buggy code and all i have to do is add right keywords, organize the code  
in blocks and keep the program running.

### Improving upon earlier projects

**NATO alphabet**
Goal is to catch the KeyError when user enters a character that is not in the  
dictionary. Characters like symbols or numbers. Will organize the code in to  
"try" and "except" blocks and continue prompting the user until they enter a  
valid word.  

### JSON file format and password manager

The goal is to add the search funcionality. Will step up from the current .txt  
file format to .json which is very simple to read from because of it's structure.  
It is composed of bunch of nested lists and dictionaries and have it's data  
organized in key:value pairs. Python have inbuilt json library so it's also very  
simple to read, write and update .json files with only few methods:
`json.dump()` `json.load()` `json.update()`

First i modify definition of `save()` and i assign new dictionary to `new_data`  
variable. Instead of opening data.txt, i open .json. Split the file opening in  
two blocks. While in read mode `json.load()` reads the file, than update the   
`new_data` dictionary with loaded data and `json.update()`. In write mode `json.dump()`  
writes the `new_data` inside existing .json structure.

### Password manager and FileNotFoundError

Most obvious problem happens when there is no data.json file to open and read  
data from. Must reorganize the code into `try`, `except` and `else` blocks to keep  
the program running. Again, trying to open the file in read mode, read the data  
and store it under the `loaded_data` variable. In `else` block i am using that  
variable to update `new_data` dictionary and than dump it to the file.  
`except` there is no data.json file than i write one and dump the data to it.
Here is how it looks:  

```
try:
    with open('data.json', mode='r') as datafile:
        loaded_data = json.load(datafile)
        
except FileNotFoundError:
    with open('data.json', mode='w') as datafile:
        json.dump(new_data, datafile, indent=4)
        
else:
    loaded_data.update(new_data)
    with open('data.json', mode='w') as datafile:
        json.dump(loaded_data, datafile, indent=4)
    
```

### Search button

Here is the assignment for search feature. 
 
- Add a "search" button next to the website entry field.
- Adjust the layout and the other widgets as needed to get the desired look.
- Create a function called `find_password()` that gets triggerred when the "search" is pressed.
- Check if the user's text entry matches an item in the data.json
- If yes, show a messagebox with the website's name and password.
- Catch an exception that might occur trying to access the data.json showing a messagebox
  with the text: **"No data file found"**
- If the user's website does not exist inside data.json, show a messagebox that reads
  **"No details for the website exists"**


#tags: readme
