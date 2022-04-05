"""
This is the modified version of day 25 main.py
Instructor wants me to use list comprehension and cut the number of lines
where i can. Since there is no any other required files this code will not work.

I will also delete the irrelevant parts of the code and leave only few originals
as comparison
"""

# build list of missing states and export it to .csv
elif answer == 'Exit':
    # list comprehension, new code
    missing_states = [state for state in data['state'].values if state not in guessed_states]

    # old code without comprehension
    for state in data['state'].values:
        if state not in guessed_states:
            missing_states.append(state)
    break

