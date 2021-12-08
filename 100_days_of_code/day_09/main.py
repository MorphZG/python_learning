# https://replit.com/@appbrewery
# Blind auction

from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.

print(logo)

bidding_data = {}

# construct the bidding_data dictionary with names and bid price
while True:
    name = input('What is your name? ')
    bid_price = int(input('What is your bid? $'))
    more_users = input('Is there any more bidders? (yes/no)')

    bidding_data[name] = bid_price

    if more_users == 'yes':
        clear()
        continue
    else:
        break


# declare the winner
highest_value = 1
for key, value in bidding_data.items():
    current_value = value
    if current_value > highest_value:
        highest_value = current_value
        winner = key
print(f'highest bidder and auction winner is: {winner} - {highest_value}usd')

#modules: replit
#tags: dictionary, list, nest,