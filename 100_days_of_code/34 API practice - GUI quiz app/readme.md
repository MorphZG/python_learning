**day 34**

# API practice

## Introduction

Today we practice APIs and going back to object oriented programming.  
Project from day 17 was built using classes and OOP. I will revisit the project  
and review what i know about APIs. Send the request with different parameters to  
fetch different sets of data. At the end i will use Tkinter module to create the  
GUI for "Quizzler" app.

## Trivia questions API

I copy the starting code provided by the instructor. In the `quizzler-app` folder  
there are starting files, probably the same ones we had after completing day 17.  
Now i got the following assignments:

- Modify the data.py file.
- Make a get() request to fetch 10 True of False questions.
- Parse the JSON response and replace the value of question_data.
- Hint: Create a python dictionary for the `amount` and `type` parameters
- Endpoint:  <https://opentdb.com/api.php?amount=10&type=boolean>

### Unescaping HTML entities

After returning the data and completing the assignment i got some strange encoding  
instead of characters like `< > " ' &`. These are HTML entities that are part of  
the HTML code. When such characters are found in the content of a web page they  
must be escaped in to something else if we don't want web browsers confuse the  
content with code elements.

We can unescape these characters with python. Using the "html" module and it's  
method `html.unescape()`. Since "quiz_brain.py" is responsible for displaying the  
questions on screen i will have to modify it. Import the "html" module first and  
under the definition of `next_question()` add new line of code and also modify the  
formating of displayed string:

```python
q_text = html.unescape(self.current_question.text)
user_answer = input(f"Q.{self.question_number}: {q_text} (True/False): ")
```

## Class based Tkiner UI

It's been a while since we worked with classes so in this lesson instructor gives  
a bit of a refresher and helps to upgrade the existing knowledge. Every class in  
project have it's own file and works like a separate module. User interface will  
also be created in a separate module "ui.py". When building the GUI i can use  
tkinter like i usually do but everything will be inside definition of `__init__`  
method of `QuizInterface()` class and than created as instance in "main.py".

**Notes by future me:**  

- When placing images or text on canvas you must set the x and y positions or get  
  "IndexError: tuple index out of range"

```python
canvas_text = canvas.create_text(150, 100, text='some text', font=('Arial', 20, 'regular'))
```

- Keyword self doesn't always have to be declared. It will turn the variable to  
  the class or object property so it can be modified from anywhere else in the  
  program. When creating the `QuizInterface()` i didn't use in only when  
  creating the images for buttons.

- To wrap the question text inside the canvas you can add "width" parameter that is  
  slightly less than width of the canvas.

```python
canvas.create_text(width=280)
```

## Show the next question in GUI

Every module of quizzler app is linked and can be modified. `QuizBrain()` class  
manages the quiz, runs the questions and keeps track of score. On [day_17](https://www.google.com), same  
app but with command line interface i have used `input()` to display the question  
and store the answer. Now with tkinter and GUI i must modify the `next_question()`  
method inside `QuizBrain()` to return the question and than inside `QuizInterface()`  
create `get_next_question()` so interface can display it. To be honest, all these  
links between different modules are not 100% clear to me so i should invest more time  
in to learning OOP and python classes.  

Since quiz interface must catch the same instance of quiz brain inside "main.py"  
i must pass it as input when creating the instance. `QuizInterface()` must have  
it inside `__init__` function, i will also define the data type of the input. To  
ensure the `QuizInterface()` will not accept anything else, we can do it like this:  

```python
# def function(parameter1[: data_type], parameter2[: data_type]):
def __init__(self, quiz_brain: QuizBrain):
```

## Check the answer

This small assignment made my brain spin around. Definitely must learn more about  
classes and object oriented programming. I will give my best to solve this but i  
am not sure how to connect different modules, classes and methods to work together.  
This is the assignment:  

- Create two new methods that you can add as a command to the buttons. The methods  
  need to call `check_answer()` from the `QuizBrain()` and pass over the string "True"  
  or "False". This should print some feedback to the console.  

I got the first part. When you give a command to the button you cannot pass the  
arguments so you need different functions for each button. First one will be  
`green_click()` it will call `check_answer('True')` and pass the "True" argument while  
`red_click()` will call the same function but pass the "False" argument `check_answer('False')`  

After seeing the instructor's solution the answer was obvious. `QuizInterface()`  
already have access to `QuizBrain()` since we passed it as argument inside `__init__()`  
All i have to do is put self.quiz before calling it like this:  

```python
class QuizInterface:
    def __init__(self, quiz_brain):
        self.quiz = quiz_brain
        self.green_button = Button(command=self.green_click)

    def green_click(self):
        self.quiz.check_answer('True')
```

#tags: readme,