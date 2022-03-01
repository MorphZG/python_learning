from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()


# remove these when done
coffee_maker.report()
money_machine.report()

machine_on = True
while machine_on:
    menu_items = menu.get_items()  # return str, names of all items on menu
    user_choice = input(f'What would you like? {menu_items} ')  # let user choose menu_items
    if user_choice == 'off':
        machine_on = False
    elif user_choice == 'report':
        coffee_maker.report()  # print report
        money_machine.report()  # print report
    else:
        drink = menu.find_drink(user_choice)  # returns MenuItem object, i will use it to access its atributes (name, cost, ingridients)
        print(f'chosen drink is {drink.name}')
        if coffee_maker.is_resource_sufficient(drink):  # returns True if resources sufficient
            if money_machine.make_payment(drink.cost):  # return True if user inserts enough coins
                coffee_maker.make_coffee(drink)  # parameter drink must be MenuItem object


#note: interesting classes provided, readme.txt
#tags: *class, objects