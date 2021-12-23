import replit
import random
from game_data import data as data_
import art


def get_person(source):
    ''' works with index numbers
    get random person from source list, return index number'''
    index_list = [index for index, value in enumerate(source)]
    i = random.choice(index_list)
    return i  # random index, int


def get_person2(source):
    '''works with values
    get random person from source list, return 4 key dictionary'''
    random_choice = random.choice(source)
    return random_choice  # 4 key dictionary 


def compare_ab(follower_count_a, follower_count_b):
    '''compares the follower count and returns "a" or "b"'''
    if follower_count_a > follower_count_b:
        return 'a'
    else:
        return 'b'


print(art.logo)
score = 0  # score should equal number of winners in list
game_on = True  # flag < ------------------------------------------- Flag!!

# person at position B should stay in game and jump to position A to compare with new person B
# need first person to be out of the loop, will switch place later
person_b = get_person2(data_)
while game_on:
    ## variables person A
    person_a = person_b  # person B jumps to position A
    name_a = person_a["name"]
    description_a = person_a["description"]
    country_a = person_a["country"]
    followers_a = person_a["follower_count"]
    ## variables person B
    person_b = get_person2(data_)  # new person B
    name_b = person_b["name"]
    description_b = person_b["description"]
    country_b = person_b["country"]
    followers_b = person_b["follower_count"]
    ## prevent comparison between same entries
    if person_b == person_a:
        person_b = get_person2(data_)  # new person B


    ## prints
    print(f"Compare A: {name_a}, {description_a} from {country_a}")
    print(f"Person A followers: {followers_a}")
    print(art.vs)
    print(f"Compare B: {name_b}, {description_b} from {country_b}")
    print(f"Person B followers: {followers_b}")
    answer = input('Who has the more followers? A / B: ').lower()

    ## clear the screen, show the score and loop again
    replit.clear() 

    ## compare followers count
    if answer == compare_ab(followers_a, followers_b):
        score += 1
        print(f'Correct!, Your final score: {score}')
    else:
        game_on = False
        print(f'Game over! Your final score: {score}')


'''
    <! --- AUTHOR'S SOLUTION


'''

#module: random, replit
#tags: game, score, function, choice(), while loop