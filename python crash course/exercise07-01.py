'''
Write a program that asks the user what kind of rental car they would like.
Print a message about that car, such as: "Let me see if i can find you a Subaru.
'''

car = input('What kind of rental car you would like: ')
message = f'Let me see if i can find you a {car.title()}'
print(message)
