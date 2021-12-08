'''
https://realpython.com/python-rock-paper-scissors/
https://realpython.com/lessons/rock-paper-scissors-overview/

enum docu:
https://docs.python.org/3/library/enum.html

strategy:
https://arstechnica.com/science/2014/05/win-at-rock-paper-scissors-by-knowing-thy-opponent/
'''

import random
from enum import IntEnum


class Action(IntEnum):
    Rock = 0
    Paper = 1
    Scissors = 2


def get_user_selection():
    choices = [f"{action.name}[{action.value}]" for action in Action]
    choices_str = ", ".join(choices)
    selection = int(input(f"Enter a choice({choices_str}): "))
    action = Action(selection)
    return action


def get_computer_selection():
    selection = random.randint(0, len(Action) - 1)
    action = Action(selection)
    return action


def determine_winner(user_action, computer_action):
    if user_action == computer_action:
        print(f"Both players selected {user_action.name}. It's a tie!")
    elif user_action == Action.Rock:
        if computer_action == Action.Scissors:
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose!")
    elif user_action == Action.Paper:
        if computer_action == Action.Rock:
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose!")
    elif user_action == Action.Scissors:
        if computer_action == Action.Paper:
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose!")


while True:
    try:
        user_action = get_user_selection()
    except ValueError as e:       # instead displaying full error msg to user
        range_str = f"[0, {len(Action) - 1}]"
        print(f"Invalid selection. Enter a value in range {range_str}")
        continue

    computer_action = get_computer_selection()
    determine_winner(user_action, computer_action)

    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        break

'''
there is more at:
https://realpython.com/python-rock-paper-scissors/

Instead of adding a lot of if … elif … else statements to your code, you can
use a dictionary to help show the relationships between actions. Dictionaries
are a great way to show a key-value relationship. In this case, the key can be
an action, like scissors, and the value can be a list of actions that it beats.

'''

#modules: random, enum
#tags: class, while loop, exception, dictionary, game,