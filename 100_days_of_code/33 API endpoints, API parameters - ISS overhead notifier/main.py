import smtplib
import requests
import time
from datetime import datetime

MY_LAT = 45.815010  # iss between 40.81 and 50.81
MY_LONG = 15.981919  # iss between 10.98 and 20.98
SENDER = 'sender@email.com'
RECEIVER = 'receiver@email.com'
PASS = 'password123'
MESSAGE = 'Alert! ISS is flying overhead!'


def iss_is_close():
    """ return True if ISS is within +5 or -5 degrees of my positions """
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data['iss_position']['latitude'])
    iss_longitude = float(data['iss_position']['longitude'])
    iss_position = (iss_latitude, iss_longitude)
    print(f'iss position (lat, long):{iss_position}')
    print(f'my position (lat, long): ({MY_LAT}, {MY_LONG})')

    # ISS latitude and longitude is between mine, tolerance +/-5
    if MY_LAT-5 <= iss_latitude <= MY_LAT+5:
        if MY_LONG-5 <= iss_longitude <= MY_LONG+5:
            return True


def is_nighttime():
    """return True if it is nighttime"""

    parameters = {
        'lat': MY_LAT,
        'long': MY_LONG,
        'formatted': 0  # turn off formating, will format manualy
    }

    response = requests.get('https://api.sunrise-sunset.org/json', params=parameters)
    response.raise_for_status()  # raise error if not successful
    data = response.json()

    # current time format: 2022-06-28T04:10:36+00:00
    # pull out only hours, read from left to right
    sunrise_hrs = int(data['results']['sunrise'].split('T')[-1].split(':')[0])
    sunset_hrs = int(data['results']['sunset'].split('T')[-1].split(':')[0])

    time_now = datetime.now()
    current_hrs = time_now.hour

    if sunrise_hrs < current_hrs < sunset_hrs:
        return True


def send_email(sender, receiver, password, content):
    """ send the email """
    print(f'\n=== Building the email for: {receiver} ===\n')

    connection = smtplib.SMTP('smtp.gmail.com')  # gmail smtp server
    connection.starttls()  # security feature that encrypts the connection
    connection.login(user=sender, password=password)
    connection.sendmail(
        from_addr=sender, to_addrs=receiver,
        msg=f'Subject:ISS IS CLOSE!\n\n{content}')  # \n\n separates mail title
    connection.close()

    print(f'=== You have just emailed this message ===\n{content}')


# code will continuously run the checks every 60 seconds
# must stop it manualy
while True:
    if iss_is_close():
        if is_nighttime():
            send_email(SENDER, RECEIVER, PASS, MESSAGE)
    time.sleep(60)


#modules: requests, datetime, time, smtplib
#tags: api, get(), email, coordinates