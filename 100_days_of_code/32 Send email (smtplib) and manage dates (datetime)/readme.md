**day 32**

# Email SMTP and the datetime module

## Introduction

Will automate emails using python `smtplib` module. It is possible to get the  
error "smtplib.SMTPServerDisconnected: Connection unexpectedly closed", which  
might happen due to a number of things.

- Make sure you've got the correct smtp address for your email provider:
  (you can google for email provider SMTP address)
  - Gmail: smtp.gmail.com
  - Hotmail: smtp.live.com
  - Outlook: outlook.office365.com
  - Yahoo: smtp.mail.yahoo.com

Below are steps specific to users sending email from gmail addresses.

- Make sure you've enabled less secure apps if you are sending from a gmail account.
- Try to go through the gmail captcha here while logged in to the gmail account:
  - [DisplayUnlockCaptcha](https://accounts.google.com/displayunlockcaptcha)
- Add a port number by changing your code to this:
  - `smtplib.SMTP("smtp.gmail.com", port=587)`

Python library, smtp documentation [Link](https://docs.python.org/3/library/smtplib.html)

## Setup

Sending emails from person to person, or from server of a sender to server of  
recipient relies on SMTP protocol. Simple Mail Transfer Protocol.  
To start the assignment i will setup two fresh email accounts. Gmail and Yahoo.  
These accounts will need some settings that will make them a bit less secure so  
use dummy account instead your personal email.

I had problems with autorization but after some googling i found the solution.  
Must enable 2FA to get access to "App password" option. Instead of usual login  
with main password i must use "app pasword" if sending email over third party  
app.

```yahoo_dummy
Jimmi Jones
jimmijones442@yahoo.com
kocka442kapa442auto442
January, 01.1991.
```

```gmail_dummy
Jimmi Jones
jimmijones442@gmail.com
kocka442kapa442auto442
January, 01.1991.
```

## Exercise

I am starting the lesson by learning about `datetime` module and doing my first  
challange. I was able to send email with python code and `smtplib` module. Now  
i must combine those 2 modules and send email on the current weekday.  

I have list of quotes in quotes.txt file and must select random one to send.  
Each quote is on it's own line so extracting the clean text should be easy.  
My first approach is to define two functions, one for selecting the random quote  
and one to send the email. Later i just have to check for the required day of the  
week to do the job.

## Automated birthday wisher

Again, instructor splits the level of challange in to three levels. "Extra Hard",  
with only few short notes, "Hard" with a bit more guidance and "Normal" with much  
more notes. As always i start with highest level of challange and i am very proud  
for completing the project on Extra Hard in relatively short time. When i look at  
instructor's solution now, she took the much simpler approach using dictionaries  
while i was killing myself finding the solution to match a row in a dataframe based  
on values in two columns. For future reference here is the solution:  

```python
filtered_data = data.loc[(data['day'] == current_day) & (data['month'] == current_month)]
```

### Extra hard starting project

1. Update the birthdays.csv
2. Check if today matches a birthday in the birthdays.csv
3. If step 2 is true, pick a random letter from letter templates and replace the `[NAME]` with the person's actual name from birthdays.csv
4. Send the letter generated in step 3 to that person's email address.

#### ========== Below are notes for lower difficulty ==========

### Hard starting project

1. Update the birthdays.csv with your friends & family's details.  
  HINT: Make sure one of the entries matches today's date for testing purposes.  

2. Check if today matches a birthday in the birthdays.csv  
  HINT 1: Only the month and day matter.  
  HINT 2: You could create a dictionary from birthdays.csv that looks like this:  

```python
birthdays_dict = {
  (month, day): data_row
}
```

  Then you could compare and see if today's month/day matches one of the  
keys in birthday_dict like this:

```python
if (today_month, today_day) in birthdays_dict:
```

3. If step 2 is true, pick a random letter from letter templates and replace the  
  `[NAME]` with the person's actual name from birthdays.csv
  HINT: [Help Link](https://www.w3schools.com/python/ref_string_replace.asp)

4. Send the letter generated in step 3 to that person's email address.
  HINT: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)

#### ========== Below are notes for lower difficulty ==========

### Normal starting project

1. Update the birthdays.csv with your friends & family's details.  
  HINT: Make sure one of the entries matches today's date for testing purposes.

2. Check if today matches a birthday in the birthdays.csv  
  HINT 1: Create a tuple from today's month and day using datetime. e.g.  
  `today = (today_month, today_day)`  
  HINT 2: Use pandas to read the birthdays.csv  
  HINT 3: Use dictionary comprehension to create a dictionary from birthday.csv that is formated like this:

```python
birthdays_dict = {
    (birthday_month, birthday_day): data_row
}
```

Dictionary comprehension template for pandas DataFrame looks like this:

```python
new_dict = {new_key: new_value for (index, data_row) in data.iterrows()}
```

If the birthdays.csv looked like this:

```csv
name,email,year,month,day
Angela,angela@email.com,1995,12,24
```

Then the birthdays_dict should look like this:

```python
birthdays_dict = {
    (12, 24): Angela,angela@email.com,1995,12,24
}
```

  Then you could compare and see if today's month/day tuple matches one of the keys in birthday_dict like this:

```python
if (today_month, today_day) in birthdays_dict:
```

3. If there is a match, pick a random letter (letter_1.txt/letter_2.txt/letter_3.txt)  
  from letter_templates and replace the `[NAME]` with the person's actual name from  
  birthdays.csv
  HINT 1: Think about the relative file path to open each letter. 
  HINT 2: Use the random module to get a number between 1-3 to pick a randome letter.
  HINT 3: Use the replace() method to replace `[NAME]` with the actual name.  
  [Help Link](https://www.w3schools.com/python/ref_string_replace.asp)

4. Send the letter generated in step 3 to that person's email address.
  HINT 1: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)
  HINT 2: Remember to call `.starttls()`
  HINT 3: Remember to login to your email service with email/password. Make sure your security setting is set to allow less secure apps.
  HINT 4: The message should have the Subject: Happy Birthday then after \n\n The Message Body.

### Run python code in the cloud

[pythonanywhere](https://www.pythonanywhere.com)


#tags: readme,