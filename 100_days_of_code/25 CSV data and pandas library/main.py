import pandas
import turtle


# screen setup
screen = turtle.Screen()
screen.title("U.S. States Game")
screen.bgpic("blank_states_img.gif")
#turtle.addshape(image)
#turtle.shape(image)

# turtle setup
turtle.hideturtle()
turtle.penup()

data = pandas.read_csv("50_states.csv")
guessed_states = []
missing_states = []

while len(guessed_states) < 50:

    answer = screen.textinput(title=f"{len(guessed_states)}/50 correct",
                              prompt="What's another state's name").title()

    # check if answer is in the list of states
    if answer in data["state"].values and answer not in guessed_states:
        # get the index of a row with user answer
        inum = data.loc[data['state'] == answer].index[0]
        # pull the X and Y columns and access values in indexed row
        x = data['x'].iloc[inum]
        y = data['y'].iloc[inum]
        # store the XY values as a tuple
        answer_coor = (x, y)
        turtle.goto(answer_coor)
        turtle.write(answer)

        # get only state name
        # append to list of guessed states
        state_name = data[data['state'] == answer]['state'].item()
        guessed_states.append(state_name)
        print(guessed_states)

    elif answer in guessed_states:
        print('You already have that state!')
        continue

    # build list of missing states and export it to .csv
    elif answer == 'Exit':
        for state in data['state'].values:
            if state not in guessed_states:
                missing_states.append(state)
        print(f'This is the list of states you should learn: {missing_states}')
        print('Exporting the list to states_to_learn.csv file...')
        # create new, single column dataframe and export to .csv
        missing_states_dataframe = pandas.DataFrame(missing_states)
        missing_states_dataframe.to_csv('states_to_learn.csv')
        print(missing_states_dataframe)
        break

screen.mainloop()
#screen.exitonclick()

#modules: pandas, turtle,
#tags: data, game, dataframe, series, item(), to_csv(), read_csv()
