import pandas


data = pandas.read_csv("50_states.csv")
data2 = data.copy()

answer = input('Name the state: ')
answer = answer.title()

# slice
# row with index location 43, column 1 to 3 (not including 3)
print(data.iloc[43, 1:3])
print('--------------------')

print(data.loc[data['state'] == answer])
print('--------------------')

# series x and series y
x = data.x.loc[43]  # row index 43
y = data.y.loc[43]  # row index 43
print(f'x value: {x}\ny value: {y}')
print('--------------------')

# how to get index number of a row, depending on another value in same row?
irow = data.loc[data['state'] == answer].index[0]
x = data.x.loc[irow]
y = data.y.loc[irow]
print(f'x value: {x}\ny value: {y}')
print('--------------------')

x = data[data['state'] == answer]['x']
y = data[data['state'] == answer]['y']
print(x)
print(y)
print('--------------------')

# print row where state is equal to user answer
print(data[data['state'] == answer])
print('--------------------')

# print only state name
state_name = data[data['state'] == answer]['state'].item()
print(state_name)
print('--------------------')

# print value from another column but in same row
print(data[data['state'] == answer]['x'])
print(f"\n.item() returns clean value without object info")
print(data[data['state'] == answer]['x'].item())
print('--------------------')

#tags: pandas, dataframe, series, value, row, column, scalar, item()
