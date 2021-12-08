'''
Zadatak sa zanimljiv rjesenjima, totalno drugacijim od mojih:
https://www.practicepython.org/exercise/2014/03/26/08-rock-paper-scissors.html


pogledaj prvu verziju rock_paper_scissors.py
to sam odradio bez problema. ovdje me najvise mucilo bodovanje.
prvo sam htio da sve radi jedna funkcija ali sam na kraju
ipak podjelio zadatke. prva funkcija odabire pobjednika,
a druga funkcija popunjava bodove u dictionary.

zato je bitno odabrati return vrjednost funkcije
i score{} dictionary mora biti u global scope
kako bi rezultat ostao zapamcen do kraja igre

    > different code versions can be found at:
https://realpython.com/python-rock-paper-scissors/
https://realpython.com/python-enumerate/

# mozda je count_score() nebitna funkcija jer se mora totalno izmjeniti da bi
# bila korisna u drugacijem okruzenju, hocu reci da sam mogao to napraviti
# i bez definiranja funkcije
# compare action bi bila bolja kada bi promjenili parametre
# u player1 i player2 ali onda treba promjeniti i kljuceve u dictionary
'''


import random  # random list item choice


def compare_actions(player, ai):
    '''
    takes 2 actions and returns a winner
    '''
    if player == ai:
        print(f'----> ai took {ai} action, player took {player} action')
        # print('it is a tie! GG!')
        winner = 'ai', 'player'
    elif player == 'rock':
        if ai == 'paper':
            print(f'----> ai took {ai} action, player took {player} action')
            # print('ai wins!')
            winner = 'ai'
        else:
            print(f'----> ai took {ai} action, player took {player} action')
            # print('player wins')
            winner = 'player'
    elif player == 'paper':
        if ai == 'scissors':
            print(f'----> ai took {ai} action, player took {player} action')
            # print('ai wins!')
            winner = 'ai'
        else:
            print(f'----> ai took {ai} action, player took {player} action')
            # print('player wins!')
            winner = 'player'
    elif player == 'scissors':
        if ai == 'rock':
            print(f'----> ai took {ai} action, player took {player} action')
            # print('ai wins!')
            winner = 'ai'
        else:
            print(f'----> ai took {ai} action, player took {player} action')
            # print('player wins!')
            winner = 'player'
    return winner


def count_score(winner):
    '''
    funkcija popunjava dictionary
    score = {'ai': 0, 'player': 0}
    mora biti definiran globalno
    jer u suprotnom nece pamtiti prijasnje rezultate
    '''

    if winner == 'player':
        score['player'] += 1
    elif winner == 'ai':
        score['ai'] += 1
    elif winner == 'tie':
        pass

    return score


# programm will pick random item from this list:
actions = ['rock', 'paper', 'scissors']

# score must be defined as global if you want it to store results until the end
score = {'ai': 0, 'player': 0}

while True:
    player = input('type stop to quit\nplease input your answer:\n>')
    if player == 'stop':
        break
    ai = random.choice(actions)
    winner = compare_actions(player, ai)
    score = count_score(winner)
    print(f'the winner is: {winner}!')
    print(score)


'''
Prvo rjesenje sa stranice zadatka:
https://www.practicepython.org/exercise/2014/03/26/08-rock-paper-scissors.html

import sys

user1 = input("What's your name?")
user2 = input("And your name?")
user1_answer = input("%s, do yo want to choose rock, paper or scissors?" % user1)
user2_answer = input("%s, do you want to choose rock, paper or scissors?" % user2)

def compare(u1, u2):
    if u1 == u2:
        return("It's a tie!")
    elif u1 == 'rock':
        if u2 == 'scissors':
            return("Rock wins!")
        else:
            return("Paper wins!")
    elif u1 == 'scissors':
        if u2 == 'paper':
            return("Scissors win!")
        else:
            return("Rock wins!")
    elif u1 == 'paper':
        if u2 == 'rock':
            return("Paper wins!")
        else:
            return("Scissors win!")
    else:
        return("Invalid input! You have not entered rock, paper or scissors, try again.")
        sys.exit()

print(compare(user1_answer, user2_answer))
'''

'''
Drugo rjesnje sa stranice zadatka:
https://www.practicepython.org/exercise/2014/03/26/08-rock-paper-scissors.html

print("""Please pick one:
            rock
            scissors
            paper""")

while True:
    game_dict = {'rock': 1, 'scissors': 2, 'paper': 3}
    player_a = str(input("Player a: "))
    player_b = str(input("Player b: "))
    a = game_dict.get(player_a)
    b = game_dict.get(player_b)
    dif = a - b

    if dif in [-1, 2]:
        print('player a wins.')
        if str(input('Do you want to play another game, yes or no?\n')) == 'yes':
            continue
        else:
            print('game over.')
            break
    elif dif in [-2, 1]:
        print('player b wins.')
        if str(input('Do you want to play another game, yes or no?\n')) == 'yes':
            continue
        else:
            print('game over.')
            break
    else:
        print('Draw.Please continue.')
        print('')

'''

#modules: random
#tags: function, return, count(), dictionary, score, winner, game