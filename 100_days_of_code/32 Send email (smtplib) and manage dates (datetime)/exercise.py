import smtplib
import datetime as dt
from random import choice

SENDER = 'sender@email.com'  # dummy accounts
SENDER_PASS = 'password1234'
RECEIVER = 'receiver@email.com'


def select_quote():
    """ select the random quote from the file """

    with open('quotes.txt', mode='r') as file:
        quotes_list = file.readlines()
        random_quote = choice(quotes_list)

    return random_quote


def send_email(sender, receiver, password):
    """ send email with the random line from quote.txt """

    message = select_quote()
    connection = smtplib.SMTP('smtp.gmail.com')  # gmail smtp server
    connection.starttls()  # security feature that encrypts the connection
    connection.login(user=sender, password=password)
    connection.sendmail(
        from_addr=sender, to_addrs=receiver,  
        msg=f'Subject:Motivation\n\n{message}') # \n\n separates mail title 
    connection.close()
    print(f'=== You have just emailed this message ===\n{message}')


now = dt.datetime.now()
today = now.weekday()

if today == 5:  # Monday == 0, Sunday == 6
    send_email(SENDER, RECEIVER, SENDER_PASS)


#modules: smtplib, datetime
#tags: smtp, automation, email