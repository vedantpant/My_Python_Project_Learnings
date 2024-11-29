import menu
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

serving_complete = True

# prompt the user for a response
menu_tab = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()


while serving_complete:
    options = menu_tab.get_items()
    choice = input(f"what would you like to have? ({options})")
    if choice == "off":
        print("goodbye!!")
        serving_complete = False
    elif choice == 'report':
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu_tab.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)

