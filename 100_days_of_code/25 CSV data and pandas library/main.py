import pandas

data = pandas.read_csv("weather_data.csv")
#print(data)
#
## two main data structures in pandas
## dataframe and series
#print(type(data))
#print(type(data["temp"]))
#
## convert temperature series to list
#temp_list = data["temp"].to_list()
#
## calculate average temperature
#average = sum(temp_list) / len(temp_list)
#print(average)
#
## calculate average using pandas
#average = data["temp"].mean()
#print(average)
#
## calculate maximum temperature
#maxtemp = data["temp"].max()
#print(maxtemp)
#
# print the row where day is monday
#monday = data[data.day == "Monday"]
#print(monday)
# print the row with maximum temperature
#print(data[data.temp == data.temp.max()])
#
# convert monday temperature to fahrenheit
monday = data[data.day == "Monday"]  # returns whole monday row
print(monday.temp)  # print temp attribute for monday
fahrenheit = monday.temp * (9/5) + 32  # conversion to fah.
print(fahrenheit)
#
#
# create a dataframe from scratch
data_dict = {
    "students": ["Amy", "James", "Fernando"],
    "scores": [76, 56, 65]
}

data = pandas.DataFrame(data_dict)  # dataframe
print(data)
data.to_csv("new_data.csv")  # export to csv file



#modules: pandas
#tags: data, csv,
