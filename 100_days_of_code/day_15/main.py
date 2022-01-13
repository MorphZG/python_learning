from menu import MENU, resources

money = 0


# print report
def report():
    '''prints ammount of resources left'''
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f'Money: ${money}')


# make requested drinks, spend resources and earn money
def make_espresso():
    global money
    money += 1.5
    resources['water'] -= 50
    resources['coffee'] -= 18
    print("Here is your espresso. Enjoy!")


def make_latte():
    global money
    money += 2.5
    resources['water'] -= 200
    resources['milk'] -= 150
    resources['coffee'] -= 24
    print("Here is your latte. Enjoy!")


def make_cappucino():
    global money
    money += 3.0
    resources['water'] -= 250
    resources['milk'] -= 100
    resources['coffee'] -= 24
    print("Here is your cappuccino. Enjoy!")


def check_resources(recipe):
    '''sufficient resources for requested drink'''
    for item in recipe:
        if recipe[item] > resources[item]:  # 2 dictionaries must have same item order 
            print(f"Sorry there is not enough {item}")
            return False
    return True  # return True or False


def process_coins():
    '''process the coins in to monetary value'''
    penny = int(input('how many pennies?')) * 0.01
    nickel = int(input('how many nickels?')) * 0.05
    dime = int(input('how many dimes?')) * 0.10
    quarter = int(input('how many quarters?')) * 0.25

    total = penny + nickel + dime + quarter

    return total


machine_on = True
# main loop: prompt the user, prepare drinks, print report
while machine_on:

    user_choice = input('What would you like? (espresso/latte/cappuccino)')

    if user_choice == 'off':
        machine_on = False

    elif user_choice == 'report':
        report()

    elif user_choice == 'espresso':
        # check is there enough resources to make the drink
        enough_resources = check_resources(MENU['espresso']['ingredients'])  # return True or False
        if enough_resources:  # if enough_resources is True, insert coins
            print('Please insert the coins.')
            inserted_coins = process_coins()
            if inserted_coins < MENU['espresso']['cost']:
                print("Sorry that's not enough money. Money refunded.")
            elif inserted_coins > MENU['espresso']['cost']:
                change = inserted_coins - MENU['espresso']['cost']
                print(f"Here is ${round(change,2)} dollars in change.")  # round() float to 2 decimals
                make_espresso()
            else:
                make_espresso()

    elif user_choice == 'latte':
        # check is there enough resources to make the drink
        enough_resources = check_resources(MENU['latte']['ingredients'])  # return True or False
        if enough_resources:  # if enough_resources is True, insert coins
            print('Please insert the coins.')
            inserted_coins = process_coins()
            if inserted_coins < MENU['latte']['cost']:
                print("Sorry that's not enough money. Money refunded.")
            elif inserted_coins > MENU['latte']['cost']:
                change = inserted_coins - MENU['latte']['cost']
                print(f"Here is ${round(change,2)} dollars in change.")  # round() float to 2 decimals
                make_latte()
            else:
                make_latte()


    elif user_choice == 'cappuccino':
        # check is there enough resources to make the drink
        enough_resources = check_resources(MENU['cappuccino']['ingredients'])  # return True or False
        if enough_resources:  # if enough_resources is True, insert coins
            print('Please insert the coins.')
            inserted_coins = process_coins()
            if inserted_coins < MENU['cappuccino']['cost']:
                print("Sorry that's not enough money. Money refunded.")
            elif inserted_coins > MENU['cappuccino']['cost']:
                change = inserted_coins - MENU['cappuccino']['cost']
                print(f"Here is ${round(change,2)} dollars in change.")  # round() float to 2 decimals
                make_cappucino()
            else:
                make_cappucino()


#note: dictionary structure
#tags: function, *dictionary, loop, procedure, game