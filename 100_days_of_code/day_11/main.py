# if computer have BJ it wins no matter what
# if an ace is drawn, count it as 11. but if total goes over 21, count as 1
# game ends immediately if user goes over 21 or if the user or comp gets a BJ
# ask the user if they want another card
# once the user is done and no longer wants to draw, let the computer play.
# computer should keep drawing unless they score goes over 16.
# compare scores for win, loss or draw.
# print out the player's and computers final hand and their scores at the end
# after game ends, ask the user if he wants to play again
# clear the console for a fresh start.

import random

def deal_cards(deck_of_cards, number, destination):
    '''
    Pulls number of items from the sequence and appends to destination
    Use random.choices(sequence, weight=None, population)
    Weight can be distributed: weight=[5, 1, 1]; first item have 5x chance
    :param1: sequence or list
    :param2: number of items you need
    :param3: list where you want to append the items
    :return: list with appended items
    '''
    random_choices = random.choices(deck_of_cards, k=number)
    for card in random_choices:
        destination.append(card)
    
    return destination


def calculate_score(list_of_cards):
    ''' calculates the score in the list of cards '''
    score = 0
    for value in list_of_cards:
        score += value

    return score

# first card is Ace
card_deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user_cards = []
computer_cards = []

# always 'y' while in production
wanna_play = 'y' #input('Do you want to play game of blackjack? (y/n)')

if wanna_play == 'y':
    # deal first 2 cards to user
    cards = deal_cards(card_deck, 2, user_cards)
    user_score = calculate_score(user_cards)
    print(f'Your cards: {user_cards}, your score: {user_score}')
    # user bj check
    if user_score == 21:
        print('User have a blackjack!')
    # deal first 2 cards to computer but print only first
    cards = deal_cards(card_deck, 2, computer_cards)
    computer_score = calculate_score(computer_cards)
    print(f'Computers first and second card: {computer_cards[0]}, {computer_cards[1]}')
    # computer bj check
    if computer_score == 21:
        print('Computer have a blackjack!')





'''
print(f'Your cards: [card_1, card_2], current score: {score}')
print(f'Computers first card: {card_1}')

input('Type "y" to get another card, type "n" to pass')
if y:
    print(f'Your final hand: [card_1, card_2], final score: {score}')
    print(f'Computers final hand: [card_1, card_2, card_3], final score: {score}')
    print('You lose')
'''

#modules: replit, random
#tags: choices(), choice()