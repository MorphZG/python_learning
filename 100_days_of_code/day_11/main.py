
import random
import replit
from art import logo
from rules import show_help


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
    '''
    return 0 if blackjack
    replace 11 with 1 if score goes above 21
    return sum(list_of_cards)
    '''
    score = sum(list_of_cards)

    if len(list_of_cards) == 2 and score == 21:
        return 0  # represent blackjack with zero

    elif score > 21 and 11 in list_of_cards:
        list_of_cards.remove(11)
        list_of_cards.append(1)
        score = sum(list_of_cards)
        return score

    else:
        return score


def compare(user_score, computer_score):
    '''
    compare score between 2 players
    detect blackjack if score is 0
    print the text string as a result
    '''
    if user_score == computer_score:
        print(f'User score: {user_score}, Computer score: {computer_score}')
        print('Its a draw!')
    elif computer_score == 0:
        print('Computer have a BLACKJACK! You loose!')
    elif user_score == 0:
        print('User have a BLACKJACK! You win!')
    elif user_score > 21:
        print('You went over! You loose!')
    elif computer_score > 21:
        print('Computer went over! You win!')
    else:
        if user_score > computer_score:
            print(f'User score: {user_score}, Comp score: {computer_score} you win!')
        elif user_score < computer_score:
            print(f'Computer score: {computer_score}, User score: {user_score} you loose!')




def play_game():
    ''' game start '''

    # first card is Ace, counts as 1 if you go over 21
    card_deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    user_cards = []
    user_score = 0
    computer_cards = []
    computer_score = 0
    game_on = True  # flag

    deal_cards(card_deck, 2, user_cards)
    deal_cards(card_deck, 2, computer_cards)
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)

    print(f'\tuser cards: {user_cards}, score: {user_score}')
    print(f'\tcomputer cards: {computer_cards[0]}')


# early finish, BLACKJACK in first hand
    if computer_score == 0:
        print('Computer have a BLACKJACK!')
        game_on = False
        play = input('Do you want to play a game of blackjack? (y/n) ')
        if play == 'y':
            replit.clear()
            print(logo)
            play_game()
        else:
            exit()

# early finish, BLACKJACK in first hand
    elif user_score == 0:
        print('User have a BLACKJACK!')
        game_on = False
        play = input('Do you want to play a game of blackjack? (y/n) ')
        if play == 'y':
            replit.clear()
            print(logo)
            play_game()
        else:
            exit()

# enter main loop after first hand
    while game_on:
        draw_more = input('Do you want another card?')
        
        # user draw cards if you answer 'y' in main loop
        if draw_more == 'y':
            deal_cards(card_deck, 1, user_cards)
            user_score = calculate_score(user_cards)
            print(f'\tuser cards: {user_cards}, score: {user_score}')
            if user_score > 21:
                compare(user_score, computer_score)
                play = input('Would you like to play again? (y/n) ')
                if play == 'y':
                    replit.clear()
                    print(logo)
                    play_game()
                else:
                    exit()

        # computer draw cards if you answer 'n' in main loop
        elif draw_more == 'n':
            while draw_more:
                
                if computer_score < 17:
                    deal_cards(card_deck, 1, computer_cards)
                    computer_score = calculate_score(computer_cards)
                
                elif computer_score > 21:
                    draw_more = False
                    compare(user_score, computer_score)
                    print()
                    play = input('Would you like to play again? (y/n) ')
                    if play == 'y':
                        replit.clear()
                        print(logo)
                        play_game()
                    else:
                        exit()
  
                else:
                    draw_more = False
                    compare(user_score, computer_score)
                    print()
                    play = input('Would you like to play again? (y/n) ')
                    if play == 'y':
                        replit.clear()
                        print(logo)
                        play_game()
                    else:
                        exit()
    return


# program start here. call play_game() if answer is 'y'
# or show help if answer is 'help'
while True:
    print('Type "help" for more info about game rules')
    play = input('Do you want to play a game of blackjack? (y/n) ')
    if play == 'y':
        replit.clear()
        print(logo)
        play_game()
    elif play == 'help':
        show_help()
    else:
        exit()


#modules: replit, random
#tags: choices(), input(), function, loop, if, elif, else, game