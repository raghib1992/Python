from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
ingredients = Menu()


money_machine.report()
coffee_maker.report()
ingredients.get_items()