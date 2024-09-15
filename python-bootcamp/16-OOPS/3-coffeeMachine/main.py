from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# object
menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

repeat = True

while repeat:
    option = menu.get_items()
    choice = input(f"what would you like? ({option}): ")
    if choice == 'off':
        print("Shut down coffee machine")
        repeat = False
    elif choice == 'report':
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
            money_machine.report()
        else:
            repeat = False
