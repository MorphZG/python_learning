import pandas

data = pandas.read_csv("weather_data.csv")
print(data)
print('--------------------')

# two main data structures in pandas
# dataframe and series
print(type(data))
print(type(data["temp"]))
print('--------------------')

# convert temperature series to list
temp_list = data["temp"].to_list()
print('--------------------')

# calculate average temperature
average = sum(temp_list) / len(temp_list)
print(average)
print('--------------------')

# calculate average using pandas
average = data["temp"].mean()
print(average)
print('--------------------')

# calculate maximum temperature
maxtemp = data["temp"].max()
print(maxtemp)
print('--------------------')

# print the row where day is monday
monday = data[data.day == "Monday"]
print(monday)
# print the row with maximum temperature
print(data[data.temp == data.temp.max()])
print('--------------------')

# print x/y value depending on another value in same row
print('print value from another column but in same row')
answer = input('input "day" value: ').title()
irow = data.loc[data['day'] == answer].index[0]  # get the index of row with value
temp_value = data.temp.loc[irow]  # look for "temp" column and get the value in row with index
condition_value = data.condition.loc[irow]  # look for "condition column and get the value in row with index
print(f'temp value: {temp_value}\ncondition value: {condition_value}')
print('--------------------')

# alternative option
print('alternative')
print('print value from another column but in same row')
answer = input('input "day" value: ').title()
print(data[data['day'] == answer]['temp'].item())  # without item() you also get object info
print(data[data['day'] == answer]['condition'].item())  # without item() you also get object info
print('--------------------')

# convert monday temperature to fahrenheit
monday = data[data.day == "Monday"]  # returns whole monday row
print(monday.temp)  # print temp attribute for monday
fahrenheit = monday.temp * (9/5) + 32  # conversion to fah.
print(fahrenheit)
print('--------------------')

# create new dataframe from dictionary
data_dict = {
    "students": ["Amy", "James", "Fernando"],
    "scores": [76, 56, 65]
}

data = pandas.DataFrame(data_dict)  # dataframe
print(data)
data.to_csv("new_data.csv")  # export to csv file


# read from .csv
data = pandas.read_csv("Squirrel-Data.csv")

# <! --- exercise 01
# extract Fur Color column
# count squirrels of each color
# build new dataframe from it and export to csv

furcolors = data.value_counts(data["Primary Fur Color"])  # type series

print('----------------------------')
print(f'.values {furcolors.values}')
print('----------------------------')
print(f'.index {furcolors.index}')
print('----------------------------')
print(f'.array {furcolors.array}')
print('----------------------------')

dict = {
    "Colors": furcolors.index,
    "Count": furcolors.values
}
new_dataframe = pandas.DataFrame(dict)
print(new_dataframe)
# <! --- end

#modules: pandas
#tags: data, dataframe, series, index, row, column, value, item()
