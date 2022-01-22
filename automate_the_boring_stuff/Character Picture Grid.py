# Automate boring stuff with python
# Exercise
# "Character Picture Grid"
# You can think of grid[x][y] as being the character at the x- and y-coordinates of a “picture” drawn with text characters.
# The (0, 0) origin will be in the upper-left corner, the x-coordinates increase going right, and the y-coordinates increase going down.
# Copy the previous grid value, and write code that uses it to print the image.
# Hint:
# You will need to use a loop in a loop in order to print grid[0][0], then grid[1][0], then grid[2][0], and so on, up to grid[8][0].
# This will finish the first row, so then print a newline. Then your program should print grid[0][1], then grid[1][1], then grid[2][1],and so on.
# The last thing your program will print is grid[8][5].
# Also, remember to pass the end keyword argument to print() if you don’t want a newline printed automatically after each print() call.

grid = [['.', '.', '.', '.', '.', '.'],
        ['.', '0', '0', '.', '.', '.'],
        ['0', '0', '0', '0', '.', '.'],
        ['0', '0', '0', '0', '0', '.'],
        ['.', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0', '.'],
        ['0', '0', '0', '0', '.', '.'],
        ['.', '0', '0', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]
        
# top_left = grid[0][0]
# bottom_left = grid[8][0]
# top_right = grid[0][5]
# bottom_right = grid[8][5]
# for x in range(len(grid)):
#     for y in range(len(grid)):
#         print(f'index of XY is {y}{x} {grid[x]}')
for x in range(6):
    for y in range(len(grid)):
        print(f'{grid[y][x]}', end='')
    print('')

#tags: pattern