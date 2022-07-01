**day 33**

# API and International Space Station

## Introduction

An Application Programming Interface, API, is a set of commands, functions, protocols,  
and objects that programmers can use to create software or interact with an external  
system. We can interact with other websites and pull live data through their API.  
It is an interface which allows us to use the perscribed rules and make a request to  
the external system for some piece of data.

One of important aspects of API is API Endpoint, it can be imagined as a location  
where data is stored, usually an URL address. In addition to knowing the Endpoint  
you also have to make one of API Requests. Simplest API request is a GET Request,  
which allows you retrieve some data from an API.

To send requests we can use code, instructor wants me to install `requests` library.  
It is a simple python library for sending HTTP requests. You usually get some kind  
of response code after sending the request. Here is the short breakdown of response codes  

  Wikipedia [Link](https://en.wikipedia.org/wiki/List_of_HTTP_status_codes)

```
Informational responses (100–199)
Successful responses (200–299)
Redirection messages (300–399)
Client error responses (400–499)
Server error responses (500–599)
```

## Kanye quotes

First API i will work on is very simple.
Use the tkinter code provided by the instructor. Create a function that will:  

1. Make a get() request to the Kanye Rest API `https://api.kanye.rest/`
2. Raise an exception if the request returned an unsuccessful status code.
3. Parse the JSON to obtain the quote text.
4. Display the quote in the canvas' `quote_text` widget

## API parameters - Match sunset times with the current time

To prepare for main project where i will track the position of ISS (International  
Space Station) i am pulling the data about sunset and sunrise. It will be easier  
to see the ISS after the sunset. I took my latitude and longitude positons and  
sent the API request to this endpoint: `https://api.sunrise-sunset.org/json`.  
Using `datetime` module i can compare my current local hours with local sunset  
and sunrise times.  

## Connecting coordinates and local time

Now it's time to match local sunrise/sunset times with the position of ISS.  
Must admit i was having a hard time comparing my position and the position of ISS.  
If ISS is between my latitude and longitude with the tolerance of +/- 5 defined  
function should return True. Simple but at the time not so obvious solution is:  

```python
if my_latitude-5 <= iss_latitude <= my_latitude+5:
    if my_longitude-5 <= iss_longitude <= my_longitude+5:
        return
```

I didn't know i can chain the comparisons like that so i had some complicated ideas  
if both latitudes are positive than do this... but if one of them is below zero  
than do something else.... crazy. I knew i there is a better, "pythonic" approach  
and after some googling i found it.

Official documentation on comparisons, [Link](https://docs.python.org/3/reference/expressions.html#comparisons)

If ISS is close than check for nighttime, using the `datetime` module i check the  
local hours, if hour is between local sunset and sunrise than we for sure have a  
nighttime :) Since `https://api.sunrise-sunset.org/json` returns time format i  
don't like `2022-06-28T04:10:36+00:00` i have to filter the hours only. First  
i make the split the string at 'T' than take the last item and again split at ':'  
and than first item should be hours. Convert the string to the integer and the  
whole thing should look like this:  

```python
sunrise_hrs = int(data['results']['sunrise'].split('T')[-1].split(':')[0])
sunset_hrs = int(data['results']['sunset'].split('T')[-1].split(':')[0])
```

Rest of the program is simple, all i have to do is run the checks. Goal is to make  
the code run every 60 seconds. So i set the while loop to always run but include  
the `time.sleep(60)` method to make the 60 second pause between checks. Must stop  
the program manualy by pressing the `CTRL + C`


#tags: readme,