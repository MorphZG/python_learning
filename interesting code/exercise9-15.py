# Chapter 9, Classes
# Solutions:
# https://ehmatthes.github.io/pcc_2e/solutions/solutions/

'''
Lottery Analysis
You can use a loop to see how hard it might be to win the kind of lottery
you just modeled. Make a list or tuple called my_ticket. Write a loop that
keeps pulling numbers until your ticket wins. Print a message reporting
how many times the loop had to run to give you a winning ticket.
'''

from random import choice

# simple list of numbers and letters. draw winner from here
choose_from = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e']

# this is my lucky ticket
my_ticket = [7, 9, 'c', 3]

# draw tickets until my_ticket wins
# count number of turns
turn = 0
winner = []

while my_ticket != winner:
    winner = []  # empty the winning ticket at start of each turn
    while len(winner) < 4:  # build winning ticket
        draw = choice(choose_from)
        if draw not in winner:
            winner.append(draw)
    turn += 1  # count end of turn
print(f'winning ticket is: {winner}')
print(f'number of turns: {turn}')

'''
    moj kod nije ispravan jer osim sto usporedujem brojeve i slova
    unutar my_ticket i winner, moj kod usporeduje i redosljed.
    ako je moja kombinacija [7, 9, c, 3], a dobitna kombinacija [9, 7, c, 3]
    moj kod ce nastaviti sa loopom dok ne pogodi tocan redosljed.
'''
print('\n\nOVDJE POCINJE AUTOROVO RJESENJE\n\n')
#       <! --- AUTOROVO RJESENJE


def get_winning_ticket(possibilities):
    """Return a winning ticket from a set of possibilities."""
    winning_ticket = []

    # We don't want to repeat winning numbers or letters, so we'll use a
    #   while loop.
    while len(winning_ticket) < 4:
        pulled_item = choice(possibilities)

        # Only add the pulled item to the winning ticket if it hasn't
        #   already been pulled.
        if pulled_item not in winning_ticket:
            winning_ticket.append(pulled_item)

    return winning_ticket

def check_ticket(played_ticket, winning_ticket):
    # Check all elements in the played ticket. If any are not in the 
    #   winning ticket, return False.
    for element in played_ticket:
        if element not in winning_ticket:
            return False

    # We must have a winning ticket!
    return True

def make_random_ticket(possibilities):
    """Return a random ticket from a set of possibilities."""
    ticket = []
    # We don't want to repeat numbers or letters, so we'll use a while loop.
    while len(ticket) < 4:
        pulled_item = choice(possibilities)

        # Only add the pulled item to the ticket if it hasn't already
        #   been pulled.
        if pulled_item not in ticket:
            ticket.append(pulled_item)

    return ticket


possibilities = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e']
winning_ticket = get_winning_ticket(possibilities)

plays = 0
won = False

# Let's set a max number of tries, in case this takes forever!
max_tries = 1_000_000

while not won:
    new_ticket = make_random_ticket(possibilities)
    won = check_ticket(new_ticket, winning_ticket)
    plays += 1
    if plays >= max_tries:
        break

if won:
    print("We have a winning ticket!")
    print(f"Your ticket: {new_ticket}")
    print(f"Winning ticket: {winning_ticket}")
    print(f"It only took {plays} tries to win!")
else:
    print(f"Tried {plays} times, without pulling a winner. :(")
    print(f"Your ticket: {new_ticket}")
    print(f"Winning ticket: {winning_ticket}")

#       <! --- KRAJ

#modules: random
#tags: choice(), loops, lottery, flag (while True/False), function