'''
Write a function called city_country()
It takes the name of a city and its country.
Function should return a string formated like this:
'Santiago, Chile'
Call your function with at least three city country pairs and
print values that are returned
'''


def city_country(city, country):
    """Return a string like 'Santiago, Chile'."""
    return f"{city.title()}, {country.title()}"


city = city_country('santiago', 'chile')
print(city)

city = city_country('ushuaia', 'argentina')
print(city)

city = city_country('longyearbyen', 'svalbard')
print(city)


'''
Autorova rjesenja
https://ehmatthes.github.io/pcc_2e/solutions/chapter_6/
'''
