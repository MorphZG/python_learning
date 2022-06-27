import smtplib
import datetime as dt
import pandas as pd
from random import choice

SENDER = 'jimmijones442@gmail.com'  # dummy account
SENDER_PASS = 'azsylpkamllwkpta'  # dummy account


def send_email(sender, receiver, password, mail_content):
    """ send the email, watch for imput parameters """ 

    print(f'\n=== Building the email for: {receiver} ===\n')
    connection = smtplib.SMTP('smtp.gmail.com')  # gmail smtp server
    connection.starttls()  # security feature that encrypts the connection
    connection.login(user=sender, password=password)
    connection.sendmail(
    from_addr=sender, to_addrs=receiver,  
    msg=f'Subject:Happy Birthday!\n\n{mail_content}'# \n\n separates mail title 
    )
    connection.close()
    print(f'=== You have just emailed this message ===\n{mail_content}')


# current date
now = dt.datetime.now()
current_month = now.month
current_day = now.day

# csv separate check for day and month of birth
data = pd.read_csv('birthdays.csv')
birth_day = data[data.day == current_day]
birth_month = data[data.month == current_month]

# check for both day and month
# select row based on day column and month column
filtered_data = data.loc[(data['day'] == current_day) & (data['month'] == current_month)]

# convert dataframe object to string
receiver_email = filtered_data['email'].to_string(index=False)
receiver_name = filtered_data['name'].to_string(index=False)

# open random letter from letter_templates directory
# replace [NAME] with actual person's name
letter01 = 'letter_templates/letter_1.txt'
letter02 = 'letter_templates/letter_2.txt'
letter03 = 'letter_templates/letter_3.txt'
letter_list = [letter01, letter02, letter03]
random_letter = choice(letter_list)
# alternative oneliner:
# file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"

with open(random_letter) as file:
    letter_content = file.read()  # full letter content as a single string
    formatted_letter = letter_content.replace('[NAME]', receiver_name)

# send the email
send_email(SENDER, receiver_email, SENDER_PASS, formatted_letter)


"""     <! --- Author's solution

# To run and test the code you need to update 4 places:
# 1. Change MY_EMAIL/MY_PASSWORD to your own details.
# 2. Go to your email provider and make it allow less secure apps.
# 3. Update the SMTP ADDRESS to match your email provider.
# 4. Update birthdays.csv to contain today's month and day.


from datetime import datetime
import pandas
import random
import smtplib

MY_EMAIL = "YOUR EMAIL"
MY_PASSWORD = "YOUR PASSWORD"

today = datetime.now()
today_tuple = (today.month, today.day)

data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}
if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("YOUR EMAIL PROVIDER SMTP SERVER ADDRESS") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthday_person["email"],
            msg=f"Subject:Happy Birthday!\n\n{contents}"
        )
"""

#modules: smtplib, datetime, pandas, random
#tags: smtp, automation, dataframe, series, loc, regex, read_csv(), email